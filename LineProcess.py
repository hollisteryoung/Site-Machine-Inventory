import fitz
import json
import Schema
import pandas as pd
import re
from pathlib import Path
from anthropic import Anthropic
from pydantic import TypeAdapter
import pytesseract
from PIL import Image
import io 

PATH = "Ballina/Continence/PS1"
EXCEL = r"C:\Site Machine Inventory\OT Historian Metadata Model_3852.xlsx"

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\youngcz\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"


pdf_search = Path(PATH).glob("*.pdf")
pdf_files = pdf_files = [str(file.absolute()) for file in pdf_search] 

df = pd.read_excel(EXCEL, sheet_name="Lines")
machine_sheet = pd.read_excel(EXCEL, sheet_name="Machines")

meta = PATH.split("/")
site = meta[0]
area = meta[1]
line = meta[2]

enrich_line = False
next_id = None
next_param_id = None

# Load Parameters (Tags) sheet once at startup, used only to seed the next ParameterID
params_sheet = pd.read_excel(EXCEL, sheet_name="Parameters (Tags)")

# Load the raw historian tag tree for this line, if present
tags_path = Path(PATH) / "tags" / "tags.json"
tags_data = {}
if tags_path.exists():
   with open(tags_path, "r", encoding="utf-8") as f:
      tags_data = json.load(f)

# Load the WinCC HMI tag export for this line, if present (UTF-16, tab-delimited,
# 25-line "#" legend preamble, no header row - column meaning comes from the legend).
wincc_path = Path(PATH) / "Tags.csv"
wincc_df = None
if wincc_path.exists():
   _wincc_cols = ['tag_name','connection','address','data_type','length','array_count',
                  'acq_mode','acq_cycle','upper','add_upper','add_lower','lower',
                  'linear_scaling','plc_upper','plc_lower','hmi_upper','hmi_lower',
                  'start_value','update_id','comment']
   wincc_df = pd.read_csv(wincc_path, encoding='utf-16', sep='\t', skiprows=25,
                          names=_wincc_cols, quotechar='"', engine='python', on_bad_lines='skip')
   wincc_df = wincc_df[wincc_df['tag_name'].notna()]


_STOPWORDS = {"the", "and", "for", "with", "assembly", "station", "module", "system", "unit"}

def ocr_page(page):
   pix = page.get_pixmap(dpi=300)
   bits = pix.tobytes("png")
   png = io.BytesIO(bits)
   img = Image.open(png)
   text = pytesseract.image_to_string(img)
   return text


def _extract_station_number(text: str):
   match = re.search(r"(\d+)", text)
   return match.group(1) if match else None


def _normalize_opc_path(raw_path) -> str:
   # Templated array tags store opcItemPath as {"bindType": ..., "binding": "..."}
   # instead of a plain string - normalize to the underlying path string.
   return raw_path.get("binding", "") if isinstance(raw_path, dict) else (raw_path or "")


def _text_matches(candidate: str, id_key: str, name_words: list) -> bool:
   if not candidate:
      return False
   candidate_alnum = re.sub(r"[^a-z0-9]", "", candidate.lower())
   if id_key and id_key in candidate_alnum:
      return True
   candidate_lower = candidate.lower()
   return any(word.lower() in candidate_lower for word in name_words)


def get_tags_for_station(station_id: str, station_name: str, tags_root: dict) -> list:
   """
   Recursively walk the tags.json tree and collect candidate tags for a station.

   Stations aren't always clean numeric/PLC codes (e.g. "St1016") — some are
   only ever named modules ("Module A", "Infeed Turret Assembly") with no
   digit anywhere in their ID, and their tags don't necessarily repeat the
   module name individually. To handle all of this it tries four matching
   strategies and tags each candidate with which one found it, so the Claude
   matching step can weigh confidence accordingly:
      1. numeric      - station's digits match a "St0*<digits>" token in the path.
      2. direct_id    - the raw station_id (alnum only) appears in the path/name.
      3. keyword      - a significant word from the station name appears in the path/name.
      4. folder_match - ONLY applied when the station has no numeric code at all. A
                         Folder/UdtInstance's own name (or its Machine/ShortName/
                         TagPath/MachineName parameter) matches the station, so its
                         ENTIRE tag subtree is included even if individual leaf tags
                         don't mention the station by name (e.g. "OEE", "GuardsOpen"
                         under a "Sleever" folder).

   Args:
      station_id: The extracted StationID (e.g., "St019", "1015", "Module A")
      station_name: The extracted StationName (e.g., "Eye Punching")
      tags_root: The parsed tags.json document

   Returns:
      List of dicts with name/opcItemPath/tagType/match_reason. Empty if none found.
   """
   target_num = _extract_station_number(station_id)
   id_key = re.sub(r"[^a-z0-9]", "", station_id.lower())
   name_words = [w for w in re.findall(r"[A-Za-z]{4,}", station_name) if w.lower() not in _STOPWORDS]

   found = {}

   def consider(tag, opc_path, reason):
      key = opc_path or tag.get("name")
      if key and key not in found:
         found[key] = {
            "name": tag.get("name"),
            "opcItemPath": opc_path,
            "tagType": tag.get("tagType"),
            "match_reason": reason
         }

   def collect_subtree(nodes, reason):
      for tag in nodes:
         opc_path = _normalize_opc_path(tag.get("opcItemPath"))
         if opc_path or tag.get("tagType") == "AtomicTag":
            consider(tag, opc_path, reason)
         if "tags" in tag:
            collect_subtree(tag["tags"], reason)

   def folder_matches(tag) -> bool:
      if _text_matches(tag.get("name") or "", id_key, name_words):
         return True
      params = tag.get("parameters") or {}
      for meta_key in ("Machine", "ShortName", "TagPath", "MachineName"):
         entry = params.get(meta_key)
         val = entry.get("value") if isinstance(entry, dict) else None
         if isinstance(val, str) and _text_matches(val, id_key, name_words):
            return True
      return False

   def walk(nodes):
      for tag in nodes:
         opc_path = _normalize_opc_path(tag.get("opcItemPath"))
         tag_name = tag.get("name") or ""
         haystack = f"{opc_path} {tag_name}".lower()
         haystack_alnum = re.sub(r"[^a-z0-9]", "", haystack)

         if target_num:
            tag_match = re.search(r"st0*(\d+)", opc_path.lower())
            if tag_match and int(tag_match.group(1)) == int(target_num):
               consider(tag, opc_path, "numeric")

         if id_key and id_key in haystack_alnum:
            consider(tag, opc_path, "direct_id")

         if any(word.lower() in haystack for word in name_words):
            consider(tag, opc_path, "keyword")

         if "tags" in tag:
            # Only fall back to whole-subtree folder matching when the station has no
            # numeric code at all (pure module names). If a numeric code exists, numeric
            # matching is precise enough on its own - folder name/keyword overlap tends to
            # over-match (e.g. a shared "Punching" folder spanning many station numbers).
            if target_num is None and tag.get("tagType") in ("Folder", "UdtInstance") and folder_matches(tag):
               collect_subtree(tag["tags"], "folder_match")
            walk(tag["tags"])

   walk(tags_root.get("tags", []))
   return list(found.values())


def get_tags_for_station_wincc(module_codes, wincc_df):
   """
   Find WinCC tags for a station by matching the station's PDF module code(s)
   as a segment within each tag name (e.g. 'FWC' in 'LO1S_FWC_DB_CFF2_PSI...').

   module_codes: list of code strings for this station, e.g. ['ASB','ASC'].
   wincc_df:     parsed WinCC export (tag_name, address, data_type, comment).
   Returns: candidate dicts, same shape as get_tags_for_station.
   """
   # Expand each base code to the variants that actually appear in THIS file's tag
   # names (e.g. 'ASB' -> 'ASB','ASBL','ASBR'). Data-driven on purpose: it adapts to
   # whatever machine's export it's given rather than relying on a hardcoded, machine-
   # specific variant table. A variant is a token that starts with the base code and
   # adds only a short (<=2 char) suffix, so 'ASB'->'ASBL' but 'INS' won't grab 'INSPECT'.
   tokens = set()
   for t in wincc_df["tag_name"].astype(str):
      tokens.update(re.findall(r"[A-Za-z0-9]+", t))
   codes = set()
   for base in module_codes:
      codes.add(base)
      for tok in tokens:
         if tok != base and tok.startswith(base) and len(tok) - len(base) <= 2:
            codes.add(tok)

   # One boundary-anchored pattern per code: segment match, not substring,
   # so 'AF' matches 'L01_AF_DB' but not 'SHAFT'.
   patterns = [(c, re.compile(rf"(?<![A-Za-z]){re.escape(c)}(?![A-Za-z])")) for c in codes]

   found = []
   for _, row in wincc_df.iterrows():
      tag = str(row.get("tag_name", ""))
      matched_code = next((c for c, pat in patterns if pat.search(tag)), None)
      if not matched_code:
         continue

      comment = row.get("comment")
      description = str(comment) if pd.notna(comment) else tag

      found.append({
         "name": description,
         "opcItemPath": tag,                          # the real tag string / Historian_Tag
         "tagType": str(row.get("data_type", "")),    # Bool / Word / Real -> helps Claude infer Data_Type
         "match_reason": f"module_segment:{matched_code}",
      })

   return found


def match_station_to_parameters(station, available_tags: list) -> list:
   """
   Use Claude to decide which pre-filtered candidate tags are genuine
   process parameters for this station, and infer their metadata.

   Args:
      station: A DiscoveredStation with StationID/StationName/Station_Type
      available_tags: Candidate tags already filtered by station number

   Returns:
      List of Schema.MatchedParameter. Empty list if no candidates.
   """
   if not available_tags:
      return []

   client = Anthropic()

   prompt = f"""
   You are matching OT historian tags to a specific machine station's tracked parameters.

   Station:
   - StationID: {station.StationID}
   - StationName: {station.StationName}
   - Station_Type: {station.Station_Type}

   Candidate tags (pre-filtered from the historian tag tree). Each candidate has a
   "match_reason" showing how it was found:
   - "numeric": the station's numeric code matched a "St0*<digits>" token in the tag's OPC path.
     This is the strongest signal.
   - "direct_id": the station's raw ID string appeared literally in the tag's path/name.
   - "keyword": only a word from the station's descriptive name matched (e.g. station is a named
     module like "Module A" with no PLC code). This is a weak signal - many of these may be
     false positives from unrelated tags that happen to share a common word. Scrutinize these
     closely and give them lower Confidence unless the tag is clearly about this exact station.
   - "folder_match": this tag lives inside a Folder/UdtInstance whose own name or machine metadata
     matched the station, so the whole subtree was pulled in even though this specific tag's name
     doesn't mention the station (common for module-style stations with no PLC code, e.g. generic
     tags like "OEE" or "GuardsOpen" grouped under a "Sleever" folder). Only keep these if the tag
     itself is plausibly a real process parameter for this station's function - exclude generic
     machine-level counters/diagnostics that just happen to live in the same folder but aren't
     specific to this station.

   {json.dumps(available_tags, indent=2)}

   For each tag that is a genuine process parameter for this station (setpoints, measurements,
   thresholds - not internal diagnostics or unrelated data), return a structured entry. Infer
   Unit_of_Measure and Data_Type from the tag name where obvious (e.g. "Width"/"Position"/"Height"
   -> mm, "Torque" -> Nm, boolean flags -> Boolean). Leave blank if not inferable. Exclude tags
   that don't genuinely belong to this station despite matching a filter heuristic.

   Return ONLY valid JSON matching this exact structure:
   {{
      "matches": [
         {{
            "ParameterName": "string",
            "Historian_Tag": "string",
            "Unit_of_Measure": "string",
            "Data_Type": "string",
            "Confidence": 0.0
         }}
      ]
   }}
   """

   response = client.messages.create(
      model='claude-opus-4-1',
      max_tokens=2048,
      messages=[
         {"role": "user", "content": prompt}
      ],
      temperature=0.1,
   )

   payload = Schema.ParameterMatchPayload.model_validate_json(response.content[0].text)
   return payload.matches


def get_next_parameter_id(current_id):
   if not current_id:
      if params_sheet.empty:
         return "PR0001"
      current_id = params_sheet.iloc[-1]["ParameterID"]
   match = re.match(r"([A-Za-z]+)(\d+)", current_id)
   if not match:
      print("Invalid ID format")

   prefix, number_str = match.groups()

   next_number = int(number_str) + 1
   padding_width = len(number_str)

   return f"{prefix}{next_number:0{padding_width}d}"


def get_next_machine_id(current_id):
   if not current_id:
      current_id = machine_sheet.iloc[-1]["MachineID"]
   match = re.match(r"([A-Za-z]+)(\d+)", current_id)
   if not match:
      print("Invalid ID format")
   
   prefix, number_str = match.groups();

   next_number = int(number_str) + 1
   padding_width = len(number_str)

   return f"{prefix}{next_number:0{padding_width}d}"


def get_json_schema(pydantic_model):
   adapter = TypeAdapter(pydantic_model)
   return adapter.json_schema()

def discovery_prompt(text_document : str):
   client = Anthropic()

   prompt = """
   You are a specialized Operational Technology (OT) asset discovery engine. Your job is to extract high-fidelity plant-floor asset hierarchies from unstructured machine documentation.

   Analyze the provided engineering document and populate the requested structured JSON payload according to these rules:

   1. line_metadata (Overall Context):
      - Description: Provide a concise summary of the main manufacturing purpose or workflow of the line.
      - OEM_Manufacturer: Identify the primary engineering vendor or machine-builder responsible for the cell.
      - Install_Date: Extract official release dates, manual version markings, or validation dates.

   2. machines (Target Individual Production Units):
      - Review the document layout. Identify distinct physical standalone machine units. A single manual file may document anywhere from 1 to 3 macro-machines in an integrated cell.
      - MachineName: Extract the exact, official designation or model label used by the equipment manufacturer (e.g., 'Post Puncher', 'Sleever System').
      - Equipment_Type: Classify its technical role (e.g., Puncher, Feeder, Vision Inspection Station, Automated Outfeed).
      - Serial_Number: Look for physical factory stamp fields. Default strictly to 'Unknown' if not found.
      - Position_In_Line: Identify sequence markers. Default to '0' if order is indeterminate.
      - OEM_Contact: Extract support emails or vendor help desks. Default to 'Unknown' if missing.
      - PLC_Make: Scan description text, electrical details, or automation configurations for controller vendor signatures (e.g., Bosch Rexroth, Siemens, Allen-Bradley, B&R). Default to 'Unknown' if unspecified.
      - start_page, end_page: The GLOBAL_PAGE numbers (not per-document page numbers) where this machine is documented, per the header markers below.

   ======================================================================
   MULTI-DOCUMENT INPUT:
   ======================================================================
   The documentation below may be assembled from MULTIPLE source PDF files for this single
   production line (e.g. one manual per machine). Each page is preceded by a header:
   '===== DOCUMENT: <filename> | PAGE <n> | GLOBAL_PAGE <g> ====='.
   Treat all of it as one combined line context: identify every distinct machine across ALL
   documents, do not create duplicate machine entries if the same machine is referenced in more
   than one document, and use the GLOBAL_PAGE values (not the per-document PAGE values) for
   start_page/end_page since they index into the combined page set.

   ======================================================================
   CRITICAL ASSET SCOPING & HIERARCHY RULES:
   ======================================================================
   Keep these structural definitions strict to maintain a normalized database layout:
   - LINE: The entire production line loop (e.g., PS1).
   - MACHINE: A standalone physical piece of equipment containing its own frame, enclosure, or primary automated tracking role.
   - STATION: Functional modular sub-assemblies, tooling plates, or sequence zones INSIDE a machine (e.g., Station 1001 - Rotary Turret, Station 1015 - Eye Punching, Transfer Arm).

   WARNING: DO NOT treat internal modular tracking numbers or assembly sequence cells as independent machines. These are sub-components (Stations) belonging inside a parent machine. Collapse all internal station data into their macro-level parent machine container.

   ======================================================================
   CRITICAL POSITION INFERENCE METHODOLOGY:
   ======================================================================
   To determine the 'Position_In_Line' (e.g., "1", "2", "3"), perform a deep step-by-step analysis of the equipment layout and material flow:
   1. Scan the manual text for the introduction of product components. The machine handling raw components or initial infeed is Position "1".
   2. Trace the transport mechanism. If Machine B receives its product explicitly from the outfeed or discharge conveyor of Machine A, designate Machine B as Position "2".
   3. Look for downstream operational terminology such as "transported to downstream sleever", "passed to packaging cell", or "final outfeed staging" to map positions sequentially.
   4. If a manual documents multiple actual machines, ensure their relative 'Position_In_Line' values accurately reflect this progressive physical sequence.

   Do not invent or extrapolate parameters. Adhere strictly to defaults when technical data is omitted.

   Return ONLY valid JSON matching this exact structure:
   {
      "line_metadata": {
         "Description": "string or null",
         "OEM_Manufacturer": "string or null",
         "Install_Date": "string or null"
      },
      "machines": [
         {
            "MachineName": "string",
            "Equipment_Type": "string",
            "Serial_Number": "string",
            "Position_In_Line": "string",
            "start_page": integer or null,
            "end_page": integer or null,
            "OEM_Contact": "string",
            "PLC_Make": "string"
         }
      ]
   }
   """
   response = client.messages.create(
      model='claude-opus-4-1',
      max_tokens=4096,
      messages=[
         {"role": "user", "content" : f"{prompt}\n\nDocumentation:\n{text_document}"}
      ],
      temperature=0.1,
   )

   return Schema.UnifiedDiscoveryPayload.model_validate_json(response.content[0].text)

def station_prompt(text_document : str, machine_name: str):
   client = Anthropic()

   prompt = f"""
   You are a specialized Operational Technology (OT) asset discovery engine focused on extracting internal station/sub-assembly details from machine documentation.

   Extract all functional stations, modular assemblies, and operational zones INSIDE the '{machine_name}' machine.

   STATION DEFINITIONS:
   - StationID: The technical identifier as it appears in PLC code, electrical schematics, control logic, or operation manuals (e.g., 'St1015', '1001', 'Turret1', 'St51PositionVerification').
   - StationName: The official name/description of the functional assembly (e.g., 'Eye Punching', 'Rotary Turret', 'Vision Inspection', 'Long Seal', 'Position Verification').
   - Station_Type: The operational function or classification. Use ONLY these specific types based on actual role:
     * Turret (rotary positioning/indexing mechanisms)
     * Vision Inspection (quality detection, splice detection, position verification)
     * Sealing (thermal or pressure sealing operations)
     * Transfer (material movement, conveyors, discharge)
     * Funnel (feeding, infeed, component insertion)
     * Cooling (thermal regulation)
     * Pressure Gauge (measurement systems)
     * DO NOT use generic 'Process'—infer the specific functional type.
   - ISA95_Level: Automation hierarchy level. Default to 'L2' (Equipment Control) unless documentation clearly indicates otherwise (L1, L3, etc.).
   - Status: Operational state. Use 'Active' unless documentation indicates 'Maintenance', 'Decommissioned', or other status.
   - start_page, end_page: Page numbers where this station is documented (if determinable).

   EXTRACTION RULES:
   1. Only extract stations that are INSIDE this machine (not separate machines or lines).
   2. Look for references in:
      - Control system flowcharts or block diagrams
      - PLC code structure or variable naming (St###, Station###)
      - Electrical schematics with functional zones
      - Operation manuals with step sequences
      - Maintenance documentation with component listings
   3. Do NOT invent stations. Only extract what is explicitly documented.
   4. If a station has sub-positions (turrets with positions, inspection heads with zones), treat the main assembly as ONE station.

   Return ONLY valid JSON matching this exact structure:
   {{
      "stations": [
         {{
            "StationID": "string",
            "StationName": "string",
            "Station_Type": "Turret|Vision Inspection|Sealing|Transfer|Funnel|Cooling|Pressure Gauge",
            "ISA95_Level": "L1|L2|L3|L4",
            "Status": "Active|Maintenance|Decommissioned",
            "start_page": integer or null,
            "end_page": integer or null
         }}
      ]
   }}
   """
   response = client.messages.create(
      model='claude-opus-4-1',
      max_tokens=4096,
      messages=[
         {"role": "user", "content" : f"{prompt}\n\nDocumentation for {machine_name}:\n{text_document}"}
      ],
      temperature=0.1,

   )

   return Schema.StationDiscoveryPayload.model_validate_json(response.content[0].text)



if __name__ == '__main__':
   row_match = df[df["LineID"] == line]
   if not row_match.empty:
      line_name  = row_match["LineName"].values[0]
      raw_description = row_match["Description"].values[0]
      raw_OEM = row_match["OEM_Manufacturer"].values[0]
      raw_date = row_match["Install_Date"].values[0]

      is_line = pd.isna(line_name)
      is_desc = pd.isna(raw_description)
      is_OEM = pd.isna(raw_OEM)
      is_date = pd.isna(raw_date)

      if is_desc or is_line or is_OEM or is_date:
         enrich_line = True
   else:
      enrich_line = True


   # Build one combined page index across ALL PDFs for this line, so Claude sees the
   # full line context in a single discovery pass. This matters for two reasons:
   # 1. Position_In_Line inference requires seeing every machine together to judge
   #    relative up/downstream order - it can't be inferred correctly if each manual
   #    is analyzed in isolation.
   # 2. If the same machine is referenced across multiple manuals, a per-pdf pass
   #    would create duplicate machine entries instead of recognizing it once.
   pages_index = []
   combined_text = ""
   for pdf in pdf_files:
      with fitz.open(pdf) as doc:
         for page_num, page in enumerate(doc):
            text = page.get_text()
            if not text.strip():
               text = ocr_page(page)
            global_page = len(pages_index)
            pages_index.append(text)
            combined_text += f"\n\n===== DOCUMENT: {Path(pdf).name} | PAGE {page_num} | GLOBAL_PAGE {global_page} =====\n{text}"

   found_machines = discovery_prompt(combined_text)

   if enrich_line:
      final_line_data = Schema.LineRow(
         LineID=line,
         LineName=line,
         Site=site,
         Area=area,
         Description=found_machines.line_metadata.Description,
         OEM_Manufacturer=found_machines.line_metadata.OEM_Manufacturer or "Unknown",
         Install_Date=found_machines.line_metadata.Install_Date
      )

      print(final_line_data)
      enrich_line = False

   for machine in found_machines.machines:

      next_id = get_next_machine_id(next_id)

      final_machine_row = Schema.MachineRow(
         MachineID=next_id,
         LineID=line,
         MachineName=machine.MachineName,
         Equipment_Type=machine.Equipment_Type,
         Serial_Number=machine.Serial_Number,
         Position_In_Line=machine.Position_In_Line,
         OEM_Contact=machine.OEM_Contact,
         PLC_Make=machine.PLC_Make,
         PLC_Credentials_Status='true'
         )

      start_page = machine.start_page if machine.start_page is not None else 0
      end_page = machine.end_page if machine.end_page is not None else (len(pages_index) - 1)
      machine_text = "".join(pages_index[start_page:end_page + 1])
      found_stations = station_prompt(machine_text, machine.MachineName)

      for station in found_stations.stations:
         # Create station row
         station_row = Schema.StationRow(
            StationID=station.StationID,
            StationName=station.StationName,
            MachineID=next_id,
            Station_Type=station.Station_Type,
            ISA95_Level=station.ISA95_Level,
            Status=station.Status
         )
         print(station_row)

         # Narrow the historian tags down to candidates for this station, then
         # let Claude decide which candidates are genuine parameters. Which source
         # depends on what this line has: WinCC HMI export (module-code segment match)
         # or the nested Ignition tags.json tree (numeric/keyword/folder match).
         if wincc_df is not None:
            candidate_tags = get_tags_for_station_wincc([station.StationID], wincc_df)
         else:
            candidate_tags = get_tags_for_station(station.StationID, station.StationName, tags_data)
         matched_params = match_station_to_parameters(station, candidate_tags)

         if matched_params:
            print(f"  Found {len(matched_params)} parameters for {station.StationID}:")
            for match in matched_params:
               next_param_id = get_next_parameter_id(next_param_id)
               param_row = Schema.ParameterRow(
                  ParameterID=next_param_id,
                  ParameterName=match.ParameterName,
                  StationID=station.StationID,
                  Unit_of_Measure=match.Unit_of_Measure,
                  Data_Type=match.Data_Type,
                  Historian_Tag=match.Historian_Tag
               )
               print(f"    - {param_row.ParameterName} ({param_row.ParameterID}): {param_row.Historian_Tag} [confidence={match.Confidence}]")
         else:
            print(f"  No parameters found for {station.StationID}")

      print(final_machine_row)
   
   

