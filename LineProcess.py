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

# Load an OPTIONAL code-legend document for this line, if present. Some PLC/HMI tag
# exports name a whole family of tags purely by an internal module/axis code (e.g.
# 'AG03', 'ASBL', 'GE1', 'SIKO') with no descriptive English word anywhere in the tag
# name or comment - those tags are invisible to keyword matching against the manual's
# plain-English station names no matter how the matching itself is tuned, because the
# text needed to match on simply isn't present in the tag. This file supplies it
# externally: a two-column CSV, header 'code,description' (e.g. 'AG03,Barrier/gasket
# vision-adjust axis group'). It has to come from an engineer or a wiring/PLC I/O
# reference - nothing in the OT documentation itself can be used to reconstruct it.
# See get_tags_for_station_wincc's "legend_code" strategy for how it's used.
code_legend_path = Path(PATH) / "Tag_Code_Legend.csv"
code_legend = {}
if code_legend_path.exists():
   _legend_df = pd.read_csv(code_legend_path)
   _legend_df.columns = [c.strip().lower() for c in _legend_df.columns]
   code_legend = {
      str(row["code"]).strip().upper(): str(row["description"]).strip()
      for _, row in _legend_df.iterrows()
      if pd.notna(row.get("code")) and pd.notna(row.get("description"))
   }


_STOPWORDS = {"the", "and", "for", "with", "assembly", "station", "stations", "module",
              "system", "unit", "machine", "option"}


def _stem(word: str) -> str:
   return word[:5] if len(word) > 5 else word


def _corpus_word_stats(wincc_df):
   words = set()
   haystacks = wincc_df["tag_name"].fillna("").astype(str) + " " + wincc_df["comment"].fillna("").astype(str)
   for hay in haystacks:
      words.update(re.findall(r"[a-z]+", hay.lower()))
   return words, {_stem(w) for w in words}


def _line_generic_words(stations):
   """
   Words that show up in more than one station's own descriptive name on this line
   (e.g. 'welding' across half the stations on a line built mostly of welders) can't
   discriminate between those stations - matching on them alone just means "this tag
   is part of the welding-heavy machine", not "this tag belongs to station X". Exclude
   them from keyword_stem's per-station vocabulary so they can't single-handedly
   qualify a match; only words that are actually distinctive to one station can.

   Compared by STEM, not literal string: 'punch' (one station's word) and 'punching'
   (a different station's word) look distinct as strings but collapse to the same stem,
   and the matching step itself compares by stem - so two different-but-same-stemmed
   words across two stations are just as non-discriminating as a literal repeat, and a
   literal-only check misses them (found on a line where FHP's 'hole/punch' and PPS's
   'punching' both matched via the same stem, each flooding into the other's candidates).
   """
   station_word_sets = []
   stem_to_stations = {}
   for s in stations:
      words = {w.lower() for w in re.findall(r"[A-Za-z]{4,}", s.StationName) if w.lower() not in _STOPWORDS}
      station_word_sets.append(words)
      for stem in {_stem(w) for w in words}:
         stem_to_stations.setdefault(stem, set()).add(s.StationID)

   generic_stems = {stem for stem, owners in stem_to_stations.items() if len(owners) > 1}
   return {w for words in station_word_sets for w in words if _stem(w) in generic_stems}


_TAG_GENERIC_WORD_FREQ_THRESHOLD = 0.01


def _tag_tree_generic_words(tags_root: dict) -> set:
   """
   Ignition/Kepware tag trees are usually rooted under one shared program/folder
   name (e.g. 'Application') that appears in every single tag's own opcItemPath -
   if a station's descriptive name happens to share a word with that structural
   scaffolding, get_tags_for_station's keyword strategy floods that station with
   almost the entire tree instead of a real candidate set (found on NGP2: 'Brand
   Label Application' and 'Sticky Tab Application' each matched ~76,000 of the
   line's ~76,300 tags via the word 'Application', which is just the PLC program's
   root folder name, not a station signal). Any word appearing in more than
   _TAG_GENERIC_WORD_FREQ_THRESHOLD of all tags in the tree is structural, not
   station-specific - this is the JSON-tree equivalent of _line_generic_words,
   which guards the same failure mode for the WinCC/CSV path.
   """
   freq = {}
   total = 0

   def walk(nodes):
      nonlocal total
      for tag in nodes:
         opc_path = _normalize_opc_path(tag.get("opcItemPath"))
         tag_name = tag.get("name") or ""
         haystack = f"{opc_path} {tag_name}".lower()
         total += 1
         for w in set(re.findall(r"[a-z]+", haystack)):
            freq[w] = freq.get(w, 0) + 1
         if "tags" in tag:
            walk(tag["tags"])

   walk((tags_root or {}).get("tags", []))
   if not total:
      return set()
   return {w for w, n in freq.items() if n / total > _TAG_GENERIC_WORD_FREQ_THRESHOLD}


def _count_atomic_tags(tags_root: dict) -> int:
   """Total leaf (AtomicTag) count in a tags.json tree - the denominator for the match
   report's coverage stat, so it reflects actual tag count rather than total node count
   (which would also include Folder/UdtInstance grouping nodes)."""
   count = 0

   def walk(nodes):
      nonlocal count
      for tag in nodes:
         if tag.get("tagType") == "AtomicTag":
            count += 1
         if "tags" in tag:
            walk(tag["tags"])

   walk((tags_root or {}).get("tags", []))
   return count


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


def _contains_word(haystack: str, word: str) -> bool:
   """
   Whole-word containment, not substring - a plain `word in haystack` check lets
   short station-name words falsely match inside unrelated longer identifiers
   (e.g. "pack" matching inside "PackagingRunMode", or "reject" matching inside
   "RejectStatistic"), flooding keyword-based matching with tags that have
   nothing to do with the station. Found on NGP2, where this alone produced
   ~4,600 false candidates for a single station. Boundaries are any non-alnum
   character or start/end of string, since tag names are usually
   underscore/case-delimited rather than space-delimited.
   """
   return re.search(rf"(?<![a-z0-9]){re.escape(word.lower())}(?![a-z0-9])", haystack.lower()) is not None


def _text_matches(candidate: str, id_key: str, name_words: list) -> bool:
   if not candidate:
      return False
   candidate_alnum = re.sub(r"[^a-z0-9]", "", candidate.lower())
   if id_key and id_key in candidate_alnum:
      return True
   return any(_contains_word(candidate, word) for word in name_words)


def get_tags_for_station(station_id: str, station_name: str, tags_root: dict, tag_generic_words: set = None) -> list:
   """
   Recursively walk the tags.json tree and collect candidate tags for a station.

   Stations aren't always clean numeric/PLC codes (e.g. "St1016") — some are
   only ever named modules ("Module A", "Infeed Turret Assembly") with no
   digit anywhere in their ID, and their tags don't necessarily repeat the
   module name individually. To handle all of this it tries four matching
   strategies and tags each candidate with which one found it, so the Claude
   matching step can weigh confidence accordingly:
      1. numeric      - station's digits match a "St0*<digits>" token in the path.
                         Also accepts a truncated suffix match (station "2057" ~
                         tag "St057") - some historian exports drop the station
                         number's leading digit rather than encoding it in full
                         (found on NGP2).
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
      tag_generic_words: optional set from _tag_tree_generic_words - words that show
                 up too often across this line's whole tag tree (usually structural
                 folder scaffolding, not a station signal) to be trusted for keyword
                 matching. Pass None to skip this filtering.

   Returns:
      List of dicts with name/opcItemPath/tagType/match_reason. Empty if none found.
   """
   target_num = _extract_station_number(station_id)
   id_key = re.sub(r"[^a-z0-9]", "", station_id.lower())
   tag_generic_words = tag_generic_words or set()
   name_words = [w for w in re.findall(r"[A-Za-z]{4,}", station_name)
                 if w.lower() not in _STOPWORDS and w.lower() not in tag_generic_words]

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
            # Deliberately NOT "st0*(\d+)" - eating leading zeros here would
            # collapse a true "St057" into a 2-digit capture ("57"), which loses
            # the digit width needed to tell a genuine truncated suffix match
            # from a coincidental one (e.g. captured "57" would wrongly suffix-
            # match station 1157 as well as the real match, station 2057). The
            # exact-match comparison below is unaffected either way since int()
            # already ignores leading zeros.
            tag_match = re.search(r"st(\d+)", opc_path.lower())
            if tag_match:
               tag_num_str = tag_match.group(1)
               # Right-aligned suffix match: some historian exports truncate the
               # station number's leading digit(s) instead of encoding it in full
               # (station "2057" -> tag "St057", discovered on NGP2). Only trust
               # a full 3-digit truncated suffix - a 2-digit suffix isn't enough
               # to discriminate (e.g. "St035" collided between station 1135 and
               # the real match, station 2035, before this was tightened).
               is_suffix_match = (
                  len(tag_num_str) == 3
                  and len(tag_num_str) < len(target_num)
                  and target_num.endswith(tag_num_str)
               )
               if int(tag_num_str) == int(target_num):
                  consider(tag, opc_path, "numeric")
               elif is_suffix_match:
                  consider(tag, opc_path, "numeric_suffix")

         if id_key and id_key in haystack_alnum:
            consider(tag, opc_path, "direct_id")

         if any(_contains_word(haystack, word) for word in name_words):
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


def get_tags_for_station_wincc(station, wincc_df, code_legend=None, line_generic_words=None):
   """
   Find WinCC tags for a station using three complementary strategies, unioned together:

   1. module_segment - the station's own StationID is (or resembles) a short PLC/module
      code that appears as a whole segment inside tag names (e.g. 'ASB' in
      'L01_ASB_DB...'). Strongest signal, and the original design of this function -
      works when the manual documents real per-station codes.
   2. keyword_stem - the station's descriptive StationName words (stemmed, majority-
      must-match rather than strict AND, since compound names often split their
      vocabulary across different tags) are looked for directly in each tag's own
      name/comment. Needed for machines whose stations are documented by plain English
      name only, with no PLC code at all (module_segment finds nothing there).
   3. legend_code - some tags carry ONLY an opaque internal code (e.g. 'AG03', 'ASBL',
      'GE1', 'SIKO') with no descriptive English word anywhere in the tag itself, so
      strategy 2 can never find them no matter how matching is tuned - the descriptive
      text needed to match on simply isn't present in the tag. If an optional
      Tag_Code_Legend.csv document (see top of file) supplies a plain-English
      description for that code, this reuses strategy 2's keyword matching against the
      legend's description text instead of the tag's own (blank) vocabulary.

   station:      A DiscoveredStation (StationID/StationName/Station_Type).
   wincc_df:     parsed WinCC export (tag_name, address, data_type, comment).
   code_legend:  optional {CODE: "plain English description"} dict. Pass {}/None if
                 no Tag_Code_Legend.csv exists for this line - strategies 1 and 2
                 still run on their own.
   line_generic_words: optional set of lowercase words to exclude from strategy 2's
                 vocabulary because they're shared across multiple stations on this
                 line (see _line_generic_words) and so can't discriminate between
                 them. Pass None to skip this filtering.
   Returns: candidate dicts, same shape as get_tags_for_station.
   """
   code_legend = code_legend or {}
   line_generic_words = line_generic_words or set()
   found = {}

   def consider(tag_name, comment, data_type, reason):
      if tag_name not in found:
         found[tag_name] = {
            "name": comment if comment else tag_name,
            "opcItemPath": tag_name,                       # the real tag string / Historian_Tag
            "tagType": data_type,                          # Bool / Word / Real -> helps Claude infer Data_Type
            "match_reason": reason,
         }

   # --- Strategy 1: module-code segment match ---
   # Expand the station's own StationID to the variants that actually appear in THIS
   # file's tag names (e.g. 'ASB' -> 'ASB','ASBL','ASBR'). Data-driven on purpose: it
   # adapts to whatever machine's export it's given rather than relying on a hardcoded,
   # machine-specific variant table. A variant is a token that starts with the base
   # code and adds only a short (<=2 char) suffix, so 'ASB'->'ASBL' but 'INS' won't
   # grab 'INSPECT'.
   tokens = set()
   for t in wincc_df["tag_name"].astype(str):
      tokens.update(re.findall(r"[A-Za-z0-9]+", t))
   codes = {station.StationID}
   for tok in tokens:
      if tok != station.StationID and tok.startswith(station.StationID) and len(tok) - len(station.StationID) <= 2:
         codes.add(tok)

   # One boundary-anchored pattern per code: segment match, not substring,
   # so 'AF' matches 'L01_AF_DB' but not 'SHAFT'.
   patterns = [(c, re.compile(rf"(?<![A-Za-z]){re.escape(c)}(?![A-Za-z])")) for c in codes]

   for _, row in wincc_df.iterrows():
      tag = str(row.get("tag_name", ""))
      matched_code = next((c for c, pat in patterns if pat.search(tag)), None)
      if matched_code:
         comment = row.get("comment")
         consider(tag, str(comment) if pd.notna(comment) else "", str(row.get("data_type", "")),
                   f"module_segment:{matched_code}")

   # --- Strategies 2 & 3: keyword/stem match against the tag's own text, OR (if the
   # tag's leading code is in the legend) against the legend's description instead. ---
   name_words = [w.lower() for w in re.findall(r"[A-Za-z]{4,}", station.StationName)
                 if w.lower() not in _STOPWORDS and w.lower() not in line_generic_words]
   if name_words:
      corpus_words, corpus_stems = _corpus_word_stats(wincc_df)
      expanded = [w for w in name_words if w in corpus_words or _stem(w) in corpus_stems
                  or any(w in d.lower() for d in code_legend.values())]

      if expanded:
         threshold = max(1, -(-len(expanded) // 2))  # ceil(n / 2)
         for _, row in wincc_df.iterrows():
            tag = str(row.get("tag_name", ""))
            comment = str(row.get("comment", "") or "")
            leading_code = re.match(r"[A-Za-z0-9]+", tag)
            legend_desc = code_legend.get(leading_code.group(0).upper(), "") if leading_code else ""
            haystack = f"{tag} {comment} {legend_desc}".lower()
            haystack_words = set(re.findall(r"[a-z]+", haystack))
            haystack_stems = {_stem(w) for w in haystack_words}
            matched = [w for w in expanded if w in haystack_words or _stem(w) in haystack_stems]
            if len(set(matched)) >= threshold:
               reason = f"keyword_stem:{','.join(sorted(set(matched)))}"
               if legend_desc:
                  reason = f"legend_code:{leading_code.group(0)}|{reason}"
               consider(tag, comment, str(row.get("data_type", "")), reason)

   return list(found.values())


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

   Unit_Verified: set this True ONLY if the unit is explicitly stated somewhere in the tag data
   itself (a literal unit string in a comment/description) - set it False if you're inferring the
   unit from the parameter name's naming convention or general plausibility, which is the common
   case since most historian exports never state units explicitly. Default to False when unsure.
   If the same physical measurement appears under more than one tag (e.g. a raw/internal "_REAL"
   representation and a separate "_DISPLAY" representation of the same signal), give them the SAME
   Unit_of_Measure - do not invent a different guessed unit for each one just because their names
   differ; a control loop's internal value and its HMI display for the same signal are essentially
   always the same physical unit unless the documentation explicitly shows a conversion between them.

   Return ONLY valid JSON matching this exact structure:
   {{
      "matches": [
         {{
            "ParameterName": "string",
            "Historian_Tag": "string",
            "Unit_of_Measure": "string",
            "Unit_Verified": false,
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


_MATCH_REASON_EXPLANATIONS = {
   "module_segment": "the tag name contains this station's own PLC/module code as a literal segment - the strongest signal available",
   "keyword_stem": "no PLC code matched; kept because words from this station's descriptive name appeared in the tag's own name/comment - a weaker signal, more prone to false positives",
   "legend_code": "the tag's own code is opaque with no descriptive text of its own, but a Tag_Code_Legend.csv entry supplied a description that matched this station's descriptive name",
   "numeric": "the station's numeric code matched a St0*<digits> token in the tag's OPC path - a strong signal",
   "numeric_suffix": "the station's numeric code's last 2-3 digits matched a truncated St0*<digits> token in the tag's OPC path (the historian export drops the station number's leading digit) - a strong signal, slightly less certain than an exact full-number match",
   "direct_id": "the station's raw ID string appeared literally in the tag's path/name - a strong signal",
   "keyword": "only a descriptive word from the station's name matched the tag's path/name - a weaker signal",
   "folder_match": "the tag lives inside a folder/UDT instance whose own name matched this station, so its whole subtree was pulled in even though this specific tag doesn't mention the station",
}


def write_match_report(line_id, station_reports, output_path=None, total_tags=None):
   """
   Write a short, plain-English report explaining which historian tags were matched to
   which stations and why. Meant to be handed to an SME or controls engineer to sanity-
   check the pipeline's output without reading raw JSON or match_reason codes - the
   confidence-weighted breakdown by match strategy is exactly the information they'd
   need to judge whether a given parameter is trustworthy or worth a second look.

   station_reports: list of dicts, one per station actually processed for this line:
      {"machine_name": str, "global_station_id": str, "station_name": str,
       "candidate_tags": list, "matched_params": list[Schema.MatchedParameter]}
   output_path: where to write the .md file. Defaults to "{PATH}/Match_Report_{line_id}.md".
   total_tags: total tag count in this line's raw historian source (the WinCC CSV row
      count, or the JSON tag tree's atomic-tag count) - the denominator for a coverage
      stat ("X of the line's Y total historian tags ended up mapped to a parameter"),
      distinct from the candidate-tag conversion rate reported per station, which only
      measures how many of the PRE-FILTERED candidates were kept. Pass None to omit the
      coverage line (e.g. when the source tag count isn't available).
   """
   output_path = Path(output_path) if output_path else Path(PATH) / f"Match_Report_{line_id}.md"
   out = [
      f"# Tag Matching Report - Line {line_id}",
      "",
      "This summarizes, for every station found on this line, which historian tags were "
      "kept as genuine process parameters and why. Parameters marked with a low match "
      "strategy (keyword/keyword_stem/legend_code/folder_match) or below 0.5 confidence "
      "are the ones most worth a second look from someone who knows the physical machine.",
      "",
   ]

   all_matched = [m for entry in station_reports for m in entry["matched_params"]]
   all_candidates = [c for entry in station_reports for c in entry["candidate_tags"]]
   zero_match_stations = [
      f"{entry['station_name']} ({entry['global_station_id']})"
      for entry in station_reports if not entry["matched_params"]
   ]
   n_low_conf = sum(1 for m in all_matched if m.Confidence < 0.5)

   out.append("## Summary")
   out.append("")
   out.append(f"- {len(station_reports)} station(s) processed.")
   out.append(
      f"- {len(all_candidates)} candidate tag(s) considered across all stations -> "
      f"{len(all_matched)} kept as genuine parameters "
      f"({(len(all_matched) / len(all_candidates) * 100) if all_candidates else 0:.0f}% of candidates)."
   )
   if total_tags:
      out.append(
         f"- {len(all_matched)} of this line's {total_tags} total historian tags "
         f"({len(all_matched) / total_tags * 100:.1f}%) ended up mapped to a genuine parameter - "
         "this is the actual coverage of the raw tag export, as opposed to the conversion rate "
         "above, which only measures the pre-filtered candidate pool."
      )
   if n_low_conf:
      out.append(f"- {n_low_conf} kept parameter(s) below 0.5 confidence overall - worth a second look.")
   if zero_match_stations:
      out.append(
         f"- {len(zero_match_stations)} station(s) with no genuine parameters found at all: "
         + ", ".join(zero_match_stations) + "."
      )
   out.append("")

   by_machine = {}
   for entry in station_reports:
      by_machine.setdefault(entry["machine_name"], []).append(entry)

   for machine_name, entries in by_machine.items():
      out.append(f"## Machine: {machine_name}")
      out.append("")
      for entry in entries:
         candidates = entry["candidate_tags"]
         matched = entry["matched_params"]
         reason_by_tag = {c["opcItemPath"]: c["match_reason"].split(":")[0] for c in candidates}

         kept_by_reason = {}
         for m in matched:
            cat = reason_by_tag.get(m.Historian_Tag, "unknown")
            kept_by_reason[cat] = kept_by_reason.get(cat, 0) + 1

         pct = (len(matched) / len(candidates) * 100) if candidates else 0
         out.append(f"### {entry['station_name']} ({entry['global_station_id']})")
         out.append("")
         out.append(
            f"- {len(candidates)} candidate tag(s) considered -> {len(matched)} kept as genuine parameters ({pct:.0f}%)."
         )
         if kept_by_reason:
            breakdown = ", ".join(
               f"{n} via *{cat}* ({_MATCH_REASON_EXPLANATIONS.get(cat, 'unrecognized match type')})"
               for cat, n in sorted(kept_by_reason.items(), key=lambda kv: -kv[1])
            )
            out.append(f"- Kept tags found by: {breakdown}.")
         low_conf = [m for m in matched if m.Confidence < 0.5]
         if low_conf:
            out.append(f"- {len(low_conf)} kept parameter(s) below 0.5 confidence - flagged with ⚠ below.")
         out.append("")

         if matched:
            out.append("| Parameter | Historian Tag | Unit | Confidence | Found via |")
            out.append("|---|---|---|---|---|")
            for m in sorted(matched, key=lambda m: m.Confidence):
               cat = reason_by_tag.get(m.Historian_Tag, "unknown")
               flag = " ⚠" if m.Confidence < 0.5 else ""
               out.append(f"| {m.ParameterName}{flag} | `{m.Historian_Tag}` | {m.Unit_of_Measure or '-'} | {m.Confidence:.2f} | {cat} |")
         else:
            out.append("_No genuine parameters found among this station's candidates._")
         out.append("")

   output_path.write_text("\n".join(out), encoding="utf-8")
   print(f"Wrote match report to {output_path}")
   return output_path


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
   - StationID: The technical identifier as it appears in PLC code, electrical schematics, control logic, or operation manuals (e.g., 'St1015', '1001', 'Turret1', 'St51PositionVerification'). Many machines have NO numeric or PLC-style code documented at all - in that case use the station's descriptive/module name itself (e.g., 'MainDial', 'BarrierPunchStation') rather than inventing one. This only needs to be unique within THIS machine's own stations, not across other machines or lines - the pipeline namespaces it downstream.
   - StationName: The official name/description of the functional assembly (e.g., 'Eye Punching', 'Rotary Turret', 'Vision Inspection', 'Long Seal', 'Position Verification').
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

   station_reports = []
   tag_generic_words = _tag_tree_generic_words(tags_data) if tags_data else set()

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
      line_generic_words = _line_generic_words(found_stations.stations)

      for station in found_stations.stations:
         # Raw station.StationID is only unique within this machine's own documentation
         # (see Schema.DiscoveredStation.StationID) - clone/replicated machine models across
         # different lines commonly reuse the same internal station numbering or naming, so
         # the stored/global key is namespaced with the MachineID to stay unique site-wide.
         global_station_id = f"{next_id}-{station.StationID}"

         # Create station row
         station_row = Schema.StationRow(
            StationID=global_station_id,
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
         # NOTE: tag matching uses the raw, machine-local station.StationID - the historian
         # tags themselves are scoped to this machine's own controller, so there's no
         # cross-machine collision risk here the way there is for the stored StationID.
         if wincc_df is not None:
            candidate_tags = get_tags_for_station_wincc(station, wincc_df, code_legend, line_generic_words)
         else:
            # Union both generic-word sources: tag_generic_words excludes words that are
            # structural scaffolding across the WHOLE tag tree (e.g. "Application"), while
            # line_generic_words excludes words shared across multiple STATION NAMES on this
            # machine (e.g. "Front"/"Rear" repeated across several catheter-handling stations,
            # which would otherwise let one station's keyword match flood into its siblings').
            candidate_tags = get_tags_for_station(station.StationID, station.StationName, tags_data, tag_generic_words | line_generic_words)
         matched_params = match_station_to_parameters(station, candidate_tags)

         station_reports.append({
            "machine_name": machine.MachineName,
            "global_station_id": global_station_id,
            "station_name": station.StationName,
            "candidate_tags": candidate_tags,
            "matched_params": matched_params,
         })

         if matched_params:
            print(f"  Found {len(matched_params)} parameters for {global_station_id}:")
            for match in matched_params:
               next_param_id = get_next_parameter_id(next_param_id)
               # Fold the verification flag into the stored text itself rather than adding a
               # column - most Unit_of_Measure values are a naming-convention guess, not
               # something actually read from the source documentation, and that distinction
               # needs to travel with the value wherever this sheet gets used.
               unit_text = match.Unit_of_Measure
               if unit_text and not match.Unit_Verified:
                  unit_text = f"{unit_text} (unverified)"
               param_row = Schema.ParameterRow(
                  ParameterID=next_param_id,
                  ParameterName=match.ParameterName,
                  StationID=global_station_id,
                  Unit_of_Measure=unit_text,
                  Data_Type=match.Data_Type,
                  Historian_Tag=match.Historian_Tag
               )
               print(f"    - {param_row.ParameterName} ({param_row.ParameterID}): {param_row.Historian_Tag} [confidence={match.Confidence}]")
         else:
            print(f"  No parameters found for {global_station_id}")

      print(final_machine_row)

   total_tags = len(wincc_df) if wincc_df is not None else (_count_atomic_tags(tags_data) if tags_data else None)
   write_match_report(line, station_reports, total_tags=total_tags)

