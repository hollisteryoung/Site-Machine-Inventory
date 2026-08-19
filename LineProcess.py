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

# Load an OPTIONAL code-legend document for this line, if present. Some PLC/HMI tag
# exports name a whole family of tags purely by an internal module/axis code (e.g.
# 'AG03', 'ASBL', 'GE1', 'SIKO') with no descriptive English word anywhere in the tag
# name or comment - those tags are invisible to keyword matching against the manual's
# plain-English station names no matter how the matching itself is tuned, because the
# text needed to match on simply isn't present in the tag. This file supplies it
# externally: a two-column CSV, header 'code,description' (e.g. 'AG03,Barrier/gasket
# vision-adjust axis group').
#
# Prefer NOT to hand-write this: profile_tag_source derives the same mapping straight
# from the export when the file makes it recoverable (see TagSourceProfile.
# inline_code_legend - e.g. an RSLogix module tag 'DRV02' whose DESCRIPTION column
# reads 'BARRIER INFEED MAGAZINE SERVO'). This external file is the fallback for
# exports that carry no descriptive text at all, where the mapping can only come from
# an engineer or a wiring/PLC I/O reference. Both are merged at match time.
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


# ==============================================================================
# TAG SOURCE READERS - normalize every export format to one record shape
# ==============================================================================
# Each reader does PARSING ONLY and contains no matching logic, so support for a new
# historian/PLC export format means adding one reader here rather than another
# matching function. A normalized TagRecord is a dict:
#   tag_path    - the historian/OPC identifier; this is what lands in Historian_Tag
#   name        - short leaf name, where the format distinguishes one
#   description - descriptive text the export carries (WinCC 'comment', RSLogix
#                 'DESCRIPTION'); '' when the format carries none (Ignition JSON)
#   data_type   - PLC/HMI data type, to help infer Data_Type downstream
#   context     - extra structural text that is NOT the tag's own identity (folder
#                 ancestry, alias target address); matched only if the profile says to
#   hmi_exposed - True/False when the export distinguishes HMI-wired tags, else None


def _tag_record(tag_path, name="", description="", data_type="", context="", hmi_exposed=None):
   return {
      "tag_path": str(tag_path or ""),
      "name": str(name or ""),
      "description": str(description or ""),
      "data_type": str(data_type or ""),
      "context": str(context or ""),
      "hmi_exposed": hmi_exposed,
   }


def _normalize_opc_path(raw_path) -> str:
   # Templated array tags store opcItemPath as {"bindType": ..., "binding": "..."}
   # instead of a plain string - normalize to the underlying path string.
   return raw_path.get("binding", "") if isinstance(raw_path, dict) else (raw_path or "")


def read_ignition_json(path: Path) -> list:
   """
   Ignition/Kepware tag-tree export (nested JSON). Flattens the tree, carrying each
   tag's folder ancestry into 'context' so structural position is still available to
   the matcher without polluting the tag's own identity. These exports carry no
   description/documentation field at all (verified on NGP2: every one of 77,165 nodes
   has only name/tagType/dataType/opcItemPath/opcServer/valueSource/tags), which is
   why 'description' comes back empty here.
   """
   with open(path, "r", encoding="utf-8") as f:
      tree = json.load(f)

   records = []

   def walk(nodes, ancestry):
      for tag in nodes:
         tag_name = tag.get("name") or ""
         opc_path = _normalize_opc_path(tag.get("opcItemPath"))
         if opc_path or tag.get("tagType") == "AtomicTag":
            records.append(_tag_record(
               tag_path=opc_path or ".".join(ancestry + [tag_name]),
               name=tag_name,
               data_type=tag.get("dataType") or tag.get("tagType") or "",
               context=" ".join(ancestry),
            ))
         if "tags" in tag:
            walk(tag["tags"], ancestry + [tag_name])

   walk(tree.get("tags", []), [])
   return records


def read_wincc_csv(path: Path) -> list:
   """
   Siemens WinCC HMI tag export: UTF-16, tab-delimited, 25-line '#' legend preamble,
   no header row - column meaning comes from that legend, hence the explicit names.
   """
   cols = ['tag_name', 'connection', 'address', 'data_type', 'length', 'array_count',
           'acq_mode', 'acq_cycle', 'upper', 'add_upper', 'add_lower', 'lower',
           'linear_scaling', 'plc_upper', 'plc_lower', 'hmi_upper', 'hmi_lower',
           'start_value', 'update_id', 'comment']
   df_ = pd.read_csv(path, encoding='utf-16', sep='\t', skiprows=25, names=cols,
                     quotechar='"', engine='python', on_bad_lines='skip')
   df_ = df_[df_['tag_name'].notna()]
   return [
      _tag_record(
         tag_path=row['tag_name'],
         name=str(row['tag_name']).split('.')[-1],
         description=row['comment'] if pd.notna(row.get('comment')) else "",
         data_type=row.get('data_type') if pd.notna(row.get('data_type')) else "",
         context=row.get('address') if pd.notna(row.get('address')) else "",
      )
      for _, row in df_.iterrows()
   ]


def read_rslogix_csv(path: Path) -> list:
   """
   Rockwell/Allen-Bradley RSLogix 5000 controller tag export: plain ASCII CSV with a
   6-line 'remark' preamble then a TYPE,SCOPE,NAME,DESCRIPTION,DATATYPE,SPECIFIER,
   ATTRIBUTES header.

   Two row types are real tags and both are kept:
     TAG   - a controller tag.
     ALIAS - an HMI-facing alias pointing at an underlying address via SPECIFIER.
             These are literally the tags an operator sees on an HMI screen, so they
             are the strongest available signal for hmi_exposed.
   COMMENT/RCOMMENT rows are per-array-element annotations on tags already emitted,
   not tags in their own right, so they are skipped.

   '$N' is RSLogix's in-string newline escape and is flattened to a space, otherwise
   descriptions like 'BAG GLUE STATION$NPROCESS FAILED' would not word-match.
   """
   df_ = pd.read_csv(path, skiprows=6, on_bad_lines='skip')
   df_ = df_[df_['TYPE'].isin(['TAG', 'ALIAS'])]

   def clean(text):
      if pd.isna(text):
         return ""
      # strip the literal 'ALIAS ' prefix RSLogix prepends to alias descriptions
      return re.sub(r"\$N", " ", str(text)).replace("ALIAS ", "", 1).strip()

   records = []
   for _, row in df_.iterrows():
      is_alias = row['TYPE'] == 'ALIAS'
      desc = clean(row.get('DESCRIPTION'))
      records.append(_tag_record(
         tag_path=row['NAME'],
         name=row['NAME'],
         description=desc,
         data_type=row.get('DATATYPE') if pd.notna(row.get('DATATYPE')) else "",
         context=row.get('SPECIFIER') if pd.notna(row.get('SPECIFIER')) else "",
         # An alias is HMI-facing by construction; a plain TAG is only HMI-facing if
         # its own description says so (RSLogix convention on this site).
         hmi_exposed=bool(is_alias or re.search(r"(?i)\bHMI\b", desc)),
      ))
   return records


def load_tag_records(base_path: Path):
   """
   Find and read whichever tag export this line has, returning (records, source_kind).

   Format is decided by content, not just filename, because both WinCC and RSLogix
   exports ship as '*.CSV' on this site: WinCC is UTF-16 with a '#'-comment preamble,
   RSLogix is ASCII whose first line starts with 'remark,'. Sniffing avoids a rename
   silently routing a file to the wrong parser.
   """
   base_path = Path(base_path)

   json_candidates = [base_path / "tags" / "tags.json", base_path / "tags.json"]
   for cand in json_candidates:
      if cand.exists():
         return read_ignition_json(cand), "ignition_json"

   csv_candidates = sorted(set(
      list(base_path.glob("*.csv")) + list(base_path.glob("*.CSV"))
      + list(base_path.glob("tags/*.csv")) + list(base_path.glob("tags/*.CSV"))
   ))
   # Tag_Code_Legend.csv is a hand-written legend, not a tag export - never parse it here.
   csv_candidates = [c for c in csv_candidates if c.name.lower() != "tag_code_legend.csv"]

   for cand in csv_candidates:
      with open(cand, "rb") as fh:
         head = fh.read(4)
      if head[:2] in (b"\xff\xfe", b"\xfe\xff"):
         return read_wincc_csv(cand), "wincc_csv"
      with open(cand, "r", encoding="utf-8", errors="replace") as fh:
         first = fh.readline()
      if first.lower().startswith("remark"):
         return read_rslogix_csv(cand), "rslogix_csv"

   return [], "none"


def _line_generic_words(stations):
   """
   Words that show up in more than one station's own descriptive name on this line
   (e.g. 'welding' across half the stations on a line built mostly of welders) can't
   discriminate between those stations - matching on them alone just means "this tag
   is part of the welding-heavy machine", not "this tag belongs to station X". Exclude
   them from the keyword strategy's per-station vocabulary so they can't single-handedly
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


# Deliberately set very high. This is a LAST-RESORT net for tokens that cannot possibly
# identify one station out of many because they appear in nearly every tag - vendor/server
# prefixes and PLC program roots (NGP2: 'nsu', 'kepserverex', 'codesys', 'bacc',
# 'application' all at 100%). An earlier 1% threshold looked reasonable on a 76,000-tag
# export but was destructive on a small one: on 1AC3 (1,430 tags) 1% is 14 tags, so it
# excluded 90 tokens including 'cure', 'elevator', 'magazine', 'forming', 'punch',
# 'vision' and 'gripper' - every one of them a real station's identity - and silently
# drove several stations to zero candidates. An absolute share threshold does not
# transfer across corpus sizes, so the blunt statistical net is now reserved for the
# near-universal case and the nuanced judgement is left to the profiler's
# structural_tokens, which can tell a shared data-structure wrapper from a station name.
_TAG_GENERIC_WORD_FREQ_THRESHOLD = 0.90


def _frequent_tokens(tag_records: list) -> set:
   """
   Words appearing in more than _TAG_GENERIC_WORD_FREQ_THRESHOLD of ALL tags in this
   export are the export's own scaffolding, not any station's identity - matching on
   one floods a station with most of the file (found on NGP2: 'Brand Label Application'
   and 'Sticky Tab Application' each matched ~76,000 of ~76,300 tags via 'Application',
   which is just the PLC program's root folder name).

   This is a cheap statistical safety net that runs regardless of what the profiler
   returns, so a profile that misses a structural token - or a line processed with a
   default profile and no profiling step at all - still cannot melt down this way.
   TagSourceProfile.structural_tokens is the principled, model-identified counterpart
   and the two are unioned at match time.
   """
   freq = {}
   total = len(tag_records)
   for rec in tag_records:
      blob = f"{rec['tag_path']} {rec['name']} {rec['context']}".lower()
      for w in set(re.findall(r"[a-z]+", blob)):
         freq[w] = freq.get(w, 0) + 1
   if not total:
      return set()
   return {w for w, n in freq.items() if n / total > _TAG_GENERIC_WORD_FREQ_THRESHOLD}


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



def _contains_word(haystack: str, word: str) -> bool:
   """
   Whole-word containment, not substring - a plain `word in haystack` check lets
   short station-name words falsely match inside unrelated longer identifiers
   (e.g. "pack" matching inside "PackagingRunMode", or "reject" matching inside
   "RejectStatistic"), flooding keyword matching with tags that have nothing to do
   with the station. Found on NGP2, where this alone produced ~4,600 false
   candidates for a single station. Boundaries are any non-alphanumeric character
   or start/end of string, since tag names are usually underscore/dot/case-delimited
   rather than space-delimited.
   """
   return re.search(rf"(?<![a-z0-9]){re.escape(word.lower())}(?![a-z0-9])", haystack.lower()) is not None


def _is_code_like(station_id: str) -> bool:
   """
   Whether a StationID reads as a short PLC/module CODE ('UWS', '2057', 'St1015') rather
   than a descriptive name ('MainDial', 'BarrierPreheatStation1'). Only for codes is a
   literal appearance inside a tag strong evidence that the tag belongs to that station -
   see the direct_id strategy. The length cap matters as much as the digit test:
   'BarrierPreheatStation1' contains a digit but is plainly a description.
   """
   key = re.sub(r"[^a-z0-9]", "", station_id.lower())
   if not key or len(key) > 8:
      return False
   return bool(re.search(r"\d", key)) or len(key) <= 6


def _station_code_variants(station_id: str, tag_records: list) -> set:
   """
   Expand a station's own code to the variants that actually occur in THIS export
   (e.g. 'ASB' -> 'ASB','ASBL','ASBR'). Data-driven on purpose so it adapts to
   whatever machine's export it is given instead of relying on a hardcoded,
   machine-specific variant table. A variant must start with the base code and add
   at most 2 characters, so 'ASB'->'ASBL' but 'INS' will not grab 'INSPECT'.
   """
   codes = {station_id}
   if len(station_id) < 2:
      return codes
   tokens = set()
   for rec in tag_records:
      tokens.update(re.findall(r"[A-Za-z0-9]+", rec["tag_path"]))
   for tok in tokens:
      if tok != station_id and tok.startswith(station_id) and len(tok) - len(station_id) <= 2:
         codes.add(tok)
   return codes


def prepare_tag_index(tag_records: list, profile, code_legend: dict = None) -> list:
   """
   Precompute, ONCE per line, everything the matcher needs per tag: the searchable
   haystack (built only from the fields the profile says carry station identity), its
   word/stem sets, and any legend description resolved for an opaque leading code.

   Done once for all stations rather than per station because the old per-format
   matchers re-walked the entire source for every station - on NGP2 that meant
   re-walking a 76,259-tag tree 66 times. Precomputing turns the whole line's matching
   from minutes into seconds, and is only possible now that every format arrives as
   one flat normalized record list.
   """
   code_legend = dict(code_legend or {})
   # Profile-derived legend is merged UNDER any externally supplied one, so a
   # hand-written Tag_Code_Legend.csv entry from an engineer always wins over an
   # inferred description for the same code.
   merged_legend = dict(getattr(profile, "inline_code_legend", {}) or {})
   merged_legend.update(code_legend)

   fields = list(getattr(profile, "station_identity_fields", None)
                 or ["tag_path", "name", "description"])
   numeric_pat = getattr(profile, "numeric_tag_pattern", None)
   compiled_numeric = re.compile(numeric_pat, re.IGNORECASE) if numeric_pat else None
   hmi_pat = getattr(profile, "hmi_exposure_marker", None)
   compiled_hmi = re.compile(hmi_pat, re.IGNORECASE) if hmi_pat else None

   index = []
   for rec in tag_records:
      parts = [rec.get(f, "") for f in fields if rec.get(f)]
      haystack = " ".join(parts).lower()

      leading = re.match(r"[A-Za-z0-9]+", rec["tag_path"] or "")
      leading_code = leading.group(0).upper() if leading else ""
      legend_desc = merged_legend.get(leading_code, "")
      if legend_desc:
         haystack = f"{haystack} {legend_desc.lower()}"

      words = set(re.findall(r"[a-z]+", haystack))
      tag_num = None
      if compiled_numeric:
         m = compiled_numeric.search(rec["tag_path"] or "")
         if m and m.groups():
            tag_num = m.group(1)

      hmi = rec.get("hmi_exposed")
      if hmi is None and compiled_hmi:
         hmi = bool(compiled_hmi.search(f"{rec['tag_path']} {rec['description']}"))

      index.append({
         "rec": rec,
         "haystack": haystack,
         "alnum": re.sub(r"[^a-z0-9]", "", haystack),
         "words": words,
         "stems": {_stem(w) for w in words},
         "legend_desc": legend_desc,
         "tag_num": tag_num,
         "hmi_exposed": hmi,
      })
   return index


def get_tags_for_station(station, tag_index: list, profile,
                         line_generic_words: set = None, tag_records: list = None) -> list:
   """
   Collect candidate tags for one station from a normalized, pre-indexed tag export.

   This is the SINGLE matcher for every export format. What used to be two divergent
   per-format functions (an Ignition-JSON walker and a WinCC-CSV scanner, each with its
   own strategies, thresholds and bugs) is now one algorithm whose behaviour is
   parameterized by a TagSourceProfile. Format-specific work is confined to the readers,
   which only parse; naming-convention-specific work is confined to the profile, which
   is only data. Adding an export format needs a reader, not a matcher; adding an export
   *convention* needs neither.

   Strategies, strongest first. Each candidate records which one found it so the
   downstream Claude judging step and the SME-facing report can weight confidence:

     numeric        - a numeric station code in the tag matches the station's, extracted
                      via profile.numeric_tag_pattern.
     numeric_suffix - same, but the export truncates the documented station number by
                      profile.numeric_truncated_digits leading digits (station '2057'
                      appears as 'St057'). Only allowed at the exact expected truncated
                      width, because a loose right-aligned match collides across ranges
                      (station 1032 vs 2032 both end '032').
     direct_id      - the station's raw ID appears literally in an identity field.
     module_segment - the station's code (or a data-derived variant) appears as a whole
                      delimiter-bounded segment of the tag path.
     legend_code    - the tag's own name is an opaque code carrying no descriptive text,
                      but a legend (inline-derived or engineer-supplied) gave it a
                      description that matches this station's name. Formerly its own
                      WinCC-only strategy; now just keyword matching over a haystack
                      that legend text was folded into.
     keyword        - only descriptive words from the station name matched. Weakest, and
                      the one that needs the most guarding (see the exclusions below).

   station:            a DiscoveredStation (StationID / StationName / Station_Type).
   tag_index:          output of prepare_tag_index for this line.
   profile:            TagSourceProfile describing this export's conventions.
   line_generic_words: words shared across several station names on this machine, which
                       therefore cannot discriminate between them (see _line_generic_words).
   tag_records:        raw records, needed only to derive module-code variants.
   """
   line_generic_words = line_generic_words or set()
   station_id = str(station.StationID)
   station_name = str(station.StationName)

   id_key = re.sub(r"[^a-z0-9]", "", station_id.lower())
   target_num = _extract_station_number(station_id)
   truncate = int(getattr(profile, "numeric_truncated_digits", 0) or 0)
   structural = {w.lower() for w in (getattr(profile, "structural_tokens", None) or [])}

   # Keyword vocabulary for this station, after removing every class of word that
   # cannot discriminate on its own: generic English, words shared with sibling stations
   # on this machine, and this export's own structural scaffolding.
   own_words = [
      w.lower() for w in re.findall(r"[A-Za-z]{4,}", station_name)
      if w.lower() not in _STOPWORDS
   ]
   name_words = [
      w for w in own_words
      if w not in line_generic_words and w not in structural
   ]

   # A station whose every word is shared with its siblings would otherwise be left with
   # NO vocabulary at all and silently score zero - which is worse than over-matching,
   # because it looks identical to "this station genuinely has no tags". Machines built
   # from one taxonomy hit this constantly: on 1AC3 'Glue Station', 'Bag Load Robot',
   # 'Barrier Preheat Station 1' and four others were reduced to nothing, since 'glue',
   # 'load', 'robot', 'barrier' and 'preheat' each recur across sibling stations.
   #
   # The insight the per-word exclusion misses: 'barrier' alone cannot discriminate and
   # 'preheat' alone cannot either, but requiring BOTH together can. So rather than
   # dropping the station, fall back to demanding the station's FULL phrase - every word
   # present in the one tag. Short words are admitted here (3+ rather than 4+ letters,
   # so 'Bag' counts) precisely because the conjunction makes them safe.
   require_all = False
   if not name_words:
      fallback = [
         w.lower() for w in re.findall(r"[A-Za-z]{3,}", station_name)
         if w.lower() not in _STOPWORDS and w.lower() not in structural
      ]
      if fallback:
         name_words = fallback
         require_all = True

   codes = _station_code_variants(station_id, tag_records or []) if tag_records else {station_id}
   seg_patterns = [
      (c, re.compile(rf"(?<![A-Za-z]){re.escape(c)}(?![A-Za-z])"))
      for c in codes if len(c) >= 2
   ]

   found = {}

   def consider(entry, reason):
      key = entry["rec"]["tag_path"] or entry["rec"]["name"]
      if key and key not in found:
         rec = entry["rec"]
         found[key] = {
            # Prefer the description as the display name when the export has one -
            # it is what makes an opaque tag path legible to a reviewer.
            "name": rec["description"] or rec["name"] or rec["tag_path"],
            "opcItemPath": rec["tag_path"],
            "tagType": rec["data_type"],
            "match_reason": reason,
            "hmi_exposed": entry["hmi_exposed"],
         }

   for entry in tag_index:
      # --- numeric / numeric_suffix ---
      if target_num and entry["tag_num"] is not None:
         tag_num = entry["tag_num"]
         if int(tag_num) == int(target_num):
            consider(entry, "numeric")
            continue
         if truncate and len(tag_num) == max(1, len(target_num) - truncate) \
               and target_num.endswith(tag_num):
            consider(entry, f"numeric_suffix:{tag_num}")
            continue

      # --- direct_id ---
      # Only for CODE-LIKE station IDs. A literal appearance of a short code ('UWS',
      # '2057', 'St1015') is strong evidence of ownership. A descriptive ID is not:
      # matching 'MainDial' as an alnum substring also hits every tag whose text reads
      # 'MAIN DIAL PART DATA STREAM' - a shared wrapper phrase used by other stations'
      # tags - which on 1AC3 handed Main Dial 429 candidates at the strength of a strong
      # signal. For descriptive IDs this strategy only duplicates what keyword matching
      # already does, with boundary checks and an honestly weaker confidence, so it is
      # skipped rather than allowed to over-claim.
      if id_key and len(id_key) >= 3 and _is_code_like(id_key) and id_key in entry["alnum"]:
         consider(entry, "direct_id")
         continue

      # --- module_segment ---
      matched_code = next((c for c, pat in seg_patterns if pat.search(entry["rec"]["tag_path"])), None)
      if matched_code:
         consider(entry, f"module_segment:{matched_code}")
         continue

      # --- keyword / legend_code ---
      # Majority rather than strict AND, since compound station names routinely split
      # their vocabulary across different tags ('Barrier Preheat Station 1' will not
      # have every word in any single tag).
      if name_words:
         hits = {w for w in name_words
                 if w in entry["words"] or _stem(w) in entry["stems"]}
         threshold = len(name_words) if require_all else max(1, -(-len(name_words) // 2))
         if len(hits) >= threshold:
            label = "keyword_all" if require_all else "keyword"
            reason = f"{label}:{','.join(sorted(hits))}"
            if entry["legend_desc"]:
               reason = f"legend_code|{reason}"
            consider(entry, reason)

   return list(found.values())


def _derive_inline_legend(tag_records: list) -> dict:
   """
   Recover an opaque-code -> description mapping from the export itself, where the
   export makes that possible.

   Some formats include a module/device-level tag whose own name IS the opaque code and
   whose description names the equipment in plain English - e.g. RSLogix 1AC3 carries
   'DRV02' described as 'BARRIER INFEED MAGAZINE SERVO' and 'R2' as 'BARRIER LOAD/BAG
   OFFLOAD ROBOT'. That is exactly the mapping Tag_Code_Legend.csv was invented to
   supply by hand for HF11, available for free here.

   Only codes with a single consistent description are kept: a code described one way
   on its input module and another on its output module is ambiguous, and guessing
   would attach a whole tag family to the wrong station.
   """
   by_code = {}
   for rec in tag_records:
      leading = re.match(r"([A-Za-z]+\d*)\b", rec["tag_path"] or "")
      if not leading or not rec["description"]:
         continue
      code = leading.group(1).upper()
      # A code is only "opaque" if it is short and not itself a descriptive word.
      if len(code) > 8 or len(code) < 2:
         continue
      by_code.setdefault(code, set()).add(rec["description"].strip())

   legend = {}
   for code, descs in by_code.items():
      # Collapse near-duplicates that differ only by an INPUTS/OUTPUTS suffix, which is
      # the common case for a paired I/O module rather than genuine ambiguity.
      norm = {re.sub(r"(?i)\b(inputs?|outputs?|from|to)\b|\bPLC\b", " ", d) for d in descs}
      norm = {re.sub(r"\s+", " ", n).strip() for n in norm}
      if len(norm) == 1:
         legend[code] = sorted(descs, key=len)[0]
   return legend


def profile_tag_source(tag_records: list, source_kind: str, station_names: list,
                       cache_path=None, sample_size: int = 60) -> Schema.TagSourceProfile:
   """
   Discover THIS export's naming conventions before any matching happens, so the single
   matcher can adapt to them instead of the codebase accumulating a hardcoded branch per
   export it has ever seen.

   Every matching fix made on this project so far was really a convention discovered by
   hand and then frozen into code: NGP2's truncated station numbers ('2057' -> 'St057'),
   NGP2's 'Application' program root flooding keyword matching, HF11's opaque module
   codes needing an external legend, 1AC3 keeping station identity in a DESCRIPTION
   column rather than the tag name. This step makes that discovery a first-class,
   inspectable pipeline output instead.

   Cheap by construction: it reads a sample of tags (not all of them - NGP2 has 76,259)
   and returns structure, so cost does not scale with export size.

   Writes/reads Tag_Source_Profile.json next to the line's data. The cached file is meant
   to be human-reviewable and hand-correctable - a controls engineer who knows the machine
   can fix a wrong inference once and every later run inherits it.
   """
   if cache_path is not None:
      cache_path = Path(cache_path)
      if cache_path.exists():
         with open(cache_path, "r", encoding="utf-8") as f:
            return Schema.TagSourceProfile.model_validate(json.load(f))

   populated = sum(1 for r in tag_records if r["description"].strip())
   frac_desc = (populated / len(tag_records)) if tag_records else 0.0
   derived_legend = _derive_inline_legend(tag_records)

   # Sample across the whole export rather than the head, so a profile is not drawn
   # only from one alphabetical corner (e.g. all the 'A*' tags of one station).
   step = max(1, len(tag_records) // sample_size)
   sample = tag_records[::step][:sample_size]
   sample_view = [
      {"tag_path": r["tag_path"], "description": r["description"][:160],
       "data_type": r["data_type"], "context": r["context"][:80]}
      for r in sample
   ]

   client = Anthropic()
   prompt = f"""
   You are analyzing the STRUCTURE and NAMING CONVENTIONS of an industrial historian/PLC
   tag export, so that a downstream matcher can attribute tags to machine stations. You
   are NOT matching tags to stations yourself - you are describing how this export encodes
   station identity.

   Detected file format: {source_kind}
   Total tags in export: {len(tag_records)}
   Share of tags carrying descriptive text: {frac_desc:.0%}

   The documented station names for this line (from its manual) are:
   {json.dumps(station_names, indent=2)}

   A representative sample of {len(sample_view)} tags, evenly spaced through the export:
   {json.dumps(sample_view, indent=2)}

   A code -> description mapping mechanically derived from module-level tags in this
   export, i.e. from REAL descriptions (may be empty if the export carries no descriptive
   text, or if no code appears as a standalone module tag):
   {json.dumps(derived_legend, indent=2)}

   Determine:

   1. station_identity_fields - which of 'tag_path', 'name', 'description', 'context'
      actually carry station identity here, MOST RELIABLE FIRST. Critical judgement: if
      tag paths are opaque device codes but the description column names the station in
      plain English, rank 'description' first. Omit fields that carry no station signal -
      including them only adds false matches. Do NOT include 'context' unless structural
      position genuinely identifies the station.

   2. station_code_style - 'descriptive_words' if a station's real name or a recognisable
      abbreviation of it appears as text; 'numeric_coded' if a numeric station code
      appears; 'opaque_module_code' if only internal codes appear with no descriptive
      text anywhere; 'mixed'; or 'absent' if station attribution simply is not recoverable.

   3. numeric_tag_pattern - a regex with EXACTLY ONE capture group that pulls a numeric
      station code out of a tag path, or null if this export has none. Look at how the
      numbers in the sample are actually prefixed and delimited before answering.

   4. numeric_truncated_digits - compare the numeric codes in the sample against the
      documented station names above. If the export consistently drops leading digits
      (a station documented as 2057 appearing as 'St057'), report how many digits are
      dropped. Report 0 if the full number is present. Be careful: this is the difference
      between matching everything and matching nothing.

   5. segment_delimiters - the characters that separate meaningful segments of a tag name.

   6. structural_tokens - lowercase words belonging to the export's own scaffolding rather
      than to any station: PLC program or folder roots, HMI screen-group names, array
      wrappers, vendor/server prefixes. Judge by whether a word appears across tags that
      clearly belong to DIFFERENT stations. Getting this right matters enormously: a
      station whose name shares a word with the program root would otherwise match nearly
      every tag in the file. Do not list a word that genuinely identifies one station.

   7. description_populated - whether there is enough descriptive text to be worth matching on.

   8. inline_code_legend - the code -> description mapping to actually use. Start from the
      derived mapping above, but DROP any entry whose description names several different
      stations at once (a shared I/O module such as 'BARRIER FORMING, BARRIER PUNCH, BAG
      GLUE INPUTS' cannot be attributed to one station and would wrongly pull a whole tag
      family into all of them). Keep entries that name a single piece of equipment.

   9. hmi_exposure_marker - a regex identifying tags already wired to an operator HMI
      screen, if this export distinguishes them at all (some exports mark HMI-facing
      aliases, or prefix descriptions with things like 'HMI PUSH BUTTON'). Null if not
      distinguishable.

   10. coverage_note - one or two plain sentences on what this export does and does NOT
       cover, comparing the sample against the documented station list. If whole groups of
       documented stations have no presence in this export at all, say so explicitly - that
       is a genuine scope limit of the file and must not be mistaken later for a matching
       failure.

   Return ONLY valid JSON of this exact shape:
   {{
      "profile": {{
         "station_identity_fields": ["string"],
         "station_code_style": "string",
         "numeric_tag_pattern": "string or null",
         "numeric_truncated_digits": 0,
         "segment_delimiters": ["string"],
         "structural_tokens": ["string"],
         "description_populated": true,
         "inline_code_legend": {{"CODE": "description"}},
         "hmi_exposure_marker": "string or null",
         "coverage_note": "string"
      }}
   }}
   """

   response = client.messages.create(
      model='claude-opus-4-1',
      max_tokens=3072,
      messages=[{"role": "user", "content": prompt}],
      temperature=0.1,
   )
   profile = Schema.TagSourceProfilePayload.model_validate_json(response.content[0].text).profile

   if cache_path is not None:
      cache_path.write_text(json.dumps(profile.model_dump(), indent=2), encoding="utf-8")
      print(f"Wrote tag source profile to {cache_path}")
   return profile
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

   Candidate tags (pre-filtered from this line's tag export). Each candidate carries:
   - "opcItemPath": the real tag identifier.
   - "name": the tag's descriptive text where the export has any, else its raw name.
   - "tagType": the PLC/HMI data type.
   - "hmi_exposed": true if this tag is already wired to an operator HMI screen, false if it
     exists only in the controller, null if this export can't distinguish. Do NOT treat false
     as a reason to reject - a parameter that is real but not currently displayed anywhere is
     precisely the kind this catalogue exists to surface.
   - "match_reason": how it was found, which tells you how much to trust the attribution:
     * "numeric" / "numeric_suffix": the station's numeric code matched a numeric code in the
       tag ("numeric_suffix" means this export truncates the station number's leading digits).
       Strongest signal.
     * "direct_id": the station's raw ID appeared literally in the tag. Strong signal.
     * "module_segment": the station's PLC/module code appeared as a whole delimiter-bounded
       segment of the tag path. Strong signal.
     * "legend_code": the tag's own name is an opaque device code, but a code legend supplied a
       plain-English description that matched this station. Trust the description, but note the
       code may cover a shared multi-station module - reject if the description names several
       different stations rather than this one.
     * "keyword": only descriptive words from the station name matched. WEAK - many will be
       false positives from unrelated tags sharing a common word. Scrutinize closely and give
       lower Confidence unless the tag is clearly about this exact station. In particular, a
       tag whose text mentions THIS station's function but attributes itself to a DIFFERENT
       station (e.g. a status flag reading "PRINTING STATION COMPLETE ... BAG LOAD STATION"
       belongs to Bag Load, not to the print station) must be rejected.

   {json.dumps(available_tags, indent=2)}

   For each tag that is a genuine process parameter for this station (setpoints, measurements,
   thresholds - not internal diagnostics or unrelated data), return a structured entry. Infer
   Unit_of_Measure and Data_Type from the tag name where obvious (e.g. "Width"/"Position"/"Height"
   -> mm, "Torque" -> Nm, boolean flags -> Boolean). Leave blank if not inferable. Exclude tags
   that don't genuinely belong to this station despite matching a filter heuristic.

   FOLDING LIMIT/TARGET TAGS INTO THEIR BASE PARAMETER: some candidates are not independent
   parameters at all - they are a naming-convention low-limit, high-limit, or target/setpoint
   companion to a real measurement/setpoint tag that is ALSO present in this same candidate list
   (e.g. base tag "CapTorque" alongside companions "CapTorque_Min"/"CapTorque_LoLimit"/
   "CapTorque_LL", "CapTorque_Max"/"CapTorque_HiLimit"/"CapTorque_HH", and
   "CapTorque_Target"/"CapTorque_SP"). Recognize these by naming-convention suffixes/prefixes or by
   a comment that explicitly says "high limit"/"low limit"/"target"/"setpoint". When you find one:
   - Do NOT return the companion tag as its own separate match entry.
   - Instead, set Min_Threshold/Max_Threshold/Target_Threshold on the BASE parameter's entry to the
     companion tag's own Historian_Tag path (not a number - these are live, operator/PLC-adjustable
     values, so only a pointer to the tag stays accurate).
   Only fold a candidate this way when its base measurement/setpoint tag is genuinely present in
   this candidate list. If a limit/target-looking tag has no such base tag alongside it, do not
   invent a pairing or drop it - return it as its own independent parameter instead.

   AMBIGUOUS DUPLICATE LIMITS: sometimes more than one candidate plausibly fills the same slot for
   the same base parameter (e.g. both "_MAX" and "_MAX_ALLOWED" look like the high limit for the
   same measurement, or two different setpoint tags could both be "the" target). Do NOT guess which
   one is "the real" limit and silently drop the other. When this happens, leave Min_Threshold/
   Max_Threshold/Target_Threshold null on the base parameter and instead return EVERY tag in the
   ambiguous group as its own independent parameter, so a human reviewer can decide - folding only
   one of several plausible candidates would silently hide the other from the parameter list.

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
            "Min_Threshold": "string or null",
            "Max_Threshold": "string or null",
            "Target_Threshold": "string or null",
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
   "numeric": "the station's numeric code matched a numeric code in the tag, using the pattern the profiler found for this export - a strong signal",
   "numeric_suffix": "the station's numeric code matched a TRUNCATED numeric code in the tag (this export drops leading digits, e.g. station 2057 appears as 'St057') - a strong signal, marginally less certain than an exact full-number match",
   "direct_id": "the station's raw ID string appeared literally in the tag - a strong signal",
   "module_segment": "the tag path contains this station's own PLC/module code as a whole delimiter-bounded segment - a strong signal",
   "legend_code": "the tag's own name is an opaque code carrying no descriptive text, but a code legend (derived from a real module-level description in the export itself, or supplied by an engineer in Tag_Code_Legend.csv) gave it a description that matched this station's name",
   "keyword": "only descriptive words from the station's name matched the tag's text - the weakest signal and the most prone to false positives, especially where several stations on the machine share vocabulary",
   "keyword_all": "every word of this station's name had to appear in the tag, because each word on its own is shared with a sibling station and so cannot discriminate (e.g. 'Barrier Preheat' on a machine full of Barrier stations) - the conjunction is meaningful even though no single word is, but it still cannot separate two stations whose names differ only by a trailing number or a word shorter than three letters",
}


def write_match_report(line_id, station_reports, output_path=None, total_tags=None, profile=None):
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
   profile: the Schema.TagSourceProfile discovered for this line's export. Reported so a
      reviewer can see WHICH CONVENTIONS the matching actually assumed - a wrong profile
      is the most likely cause of a whole line matching badly, and it is far easier to
      spot a wrong assumption stated in plain English than to infer it from bad results.
      Pass None to omit that section.
   """
   output_path = Path(output_path) if output_path else Path(PATH) / f"Match_Report_{line_id}.md"
   out = [
      f"# Tag Matching Report - Line {line_id}",
      "",
      "This summarizes, for every station found on this line, which historian tags were "
      "kept as genuine process parameters and why. Parameters marked with a low match "
      "strategy (keyword/legend_code) or below 0.5 confidence are the ones most worth a "
      "second look from someone who knows the physical machine.",
      "",
   ]

   all_matched = [m for entry in station_reports for m in entry["matched_params"]]
   all_candidates = [c for entry in station_reports for c in entry["candidate_tags"]]
   zero_match_stations = [
      f"{entry['station_name']} ({entry['global_station_id']})"
      for entry in station_reports if not entry["matched_params"]
   ]
   n_low_conf = sum(1 for m in all_matched if m.Confidence < 0.5)
   n_folded = sum(
      1 for m in all_matched
      for t in (m.Min_Threshold, m.Max_Threshold, m.Target_Threshold) if t
   )

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
   if n_folded:
      out.append(
         f"- {n_folded} candidate tag(s) folded into another parameter's Min/Max/Target_Threshold "
         "field(s) as limit/setpoint companions, rather than kept as their own parameter row."
      )
   if zero_match_stations:
      out.append(
         f"- {len(zero_match_stations)} station(s) with no genuine parameters found at all: "
         + ", ".join(zero_match_stations) + "."
      )

   # HMI-exposed split. This is the concrete answer to "what does this model give us that
   # reading the HMI doesn't": PLC-only parameters are ones no operator screen currently
   # shows, so they are invisible to the traditional approach of picking tags off an HMI.
   hmi_flags = [c.get("hmi_exposed") for entry in station_reports for c in entry["candidate_tags"]]
   if any(f is not None for f in hmi_flags):
      kept_tags = {m.Historian_Tag for m in all_matched}
      kept_hmi = sum(
         1 for entry in station_reports for c in entry["candidate_tags"]
         if c["opcItemPath"] in kept_tags and c.get("hmi_exposed")
      )
      out.append(
         f"- Of the kept parameters, {kept_hmi} are already wired to an operator HMI screen and "
         f"{len(all_matched) - kept_hmi} exist in the controller but are NOT displayed on any HMI - "
         "the latter are what this catalogue adds over picking tags off an HMI by hand."
      )
   out.append("")

   if profile is not None:
      out.append("## Tag export conventions this run assumed")
      out.append("")
      out.append(
         "Discovered by the profiling step and cached to `Tag_Source_Profile.json`. If a whole "
         "line matched badly, suspect these first - and correct that file by hand rather than "
         "the code, since every later run reads it back."
      )
      out.append("")
      out.append(f"- Station identity read from: {', '.join(profile.station_identity_fields)}.")
      out.append(f"- Station code style: *{profile.station_code_style}*.")
      if profile.numeric_tag_pattern:
         trunc = (f", with the documented station number's leading "
                  f"{profile.numeric_truncated_digits} digit(s) dropped in the tag"
                  if profile.numeric_truncated_digits else ", carrying the full station number")
         out.append(f"- Numeric station codes extracted with `{profile.numeric_tag_pattern}`{trunc}.")
      out.append(
         f"- Descriptive text present and matched against: {'yes' if profile.description_populated else 'no'}."
      )
      if profile.structural_tokens:
         out.append(
            f"- {len(profile.structural_tokens)} export-scaffolding token(s) excluded from keyword "
            f"matching: {', '.join('`' + t + '`' for t in profile.structural_tokens[:15])}"
            + (" ..." if len(profile.structural_tokens) > 15 else "") + "."
         )
      if profile.inline_code_legend:
         out.append(
            f"- {len(profile.inline_code_legend)} opaque code(s) resolved to plain English from the "
            "export itself (no hand-written legend needed): "
            + ", ".join(f"`{k}` = {v}" for k, v in list(profile.inline_code_legend.items())[:8])
            + (" ..." if len(profile.inline_code_legend) > 8 else "") + "."
         )
      if profile.coverage_note:
         out.append(f"- **Coverage caveat:** {profile.coverage_note}")
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
            out.append("| Parameter | Historian Tag | Unit | Min/Max/Target Threshold Tags | Confidence | Found via |")
            out.append("|---|---|---|---|---|---|")
            for m in sorted(matched, key=lambda m: m.Confidence):
               cat = reason_by_tag.get(m.Historian_Tag, "unknown")
               flag = " ⚠" if m.Confidence < 0.5 else ""
               thresholds = ", ".join(
                  f"{label}=`{tag}`" for label, tag in
                  (("Min", m.Min_Threshold), ("Max", m.Max_Threshold), ("Target", m.Target_Threshold))
                  if tag
               ) or "-"
               out.append(f"| {m.ParameterName}{flag} | `{m.Historian_Tag}` | {m.Unit_of_Measure or '-'} | {thresholds} | {m.Confidence:.2f} | {cat} |")
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

   # Load whichever tag export this line has, normalized to one record shape, then
   # discover its naming conventions ONCE before matching anything. Everything
   # downstream is format-agnostic from here on: the readers absorbed the format
   # differences, the profile absorbs the convention differences.
   tag_records, tag_source_kind = load_tag_records(Path(PATH))
   print(f"Loaded {len(tag_records)} tag(s) from a '{tag_source_kind}' export")

   all_station_names = []
   machine_stations = []
   for machine in found_machines.machines:
      start_page = machine.start_page if machine.start_page is not None else 0
      end_page = machine.end_page if machine.end_page is not None else (len(pages_index) - 1)
      machine_text = "".join(pages_index[start_page:end_page + 1])
      stations = station_prompt(machine_text, machine.MachineName).stations
      machine_stations.append((machine, stations))
      all_station_names.extend(s.StationName for s in stations)

   tag_profile = Schema.TagSourceProfile()
   tag_index = []
   frequent_tokens = set()
   if tag_records:
      # Profiled against the FULL station list for the line, since judging whether a
      # token is structural scaffolding or a real station name requires seeing every
      # station the export is supposed to cover.
      tag_profile = profile_tag_source(
         tag_records, tag_source_kind, all_station_names,
         cache_path=Path(PATH) / "Tag_Source_Profile.json",
      )
      frequent_tokens = _frequent_tokens(tag_records)
      tag_index = prepare_tag_index(tag_records, tag_profile, code_legend)

   for machine, found_stations_list in machine_stations:

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

      line_generic_words = _line_generic_words(found_stations_list)

      for station in found_stations_list:
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

         # Narrow the tag export down to candidates for this station, then let Claude
         # decide which candidates are genuine parameters. One matcher regardless of
         # export format - the profile carries whatever this export does differently.
         #
         # Three complementary exclusion sources are unioned into the keyword
         # vocabulary guard, each catching a different way a word can fail to
         # discriminate between stations:
         #   frequent_tokens      - statistically ubiquitous across THIS export (safety net)
         #   structural_tokens    - identified by the profiler as export scaffolding
         #   line_generic_words   - shared across several STATION NAMES on this machine
         #                          (e.g. 'Barrier' on a machine of barrier stations)
         #
         # NOTE: matching uses the raw, machine-local station.StationID - the tags are
         # scoped to this machine's own controller, so there's no cross-machine collision
         # risk here the way there is for the stored, MachineID-namespaced StationID.
         candidate_tags = get_tags_for_station(
            station, tag_index, tag_profile,
            line_generic_words=line_generic_words | frequent_tokens,
            tag_records=tag_records,
         ) if tag_index else []
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
                  Min_Threshold=match.Min_Threshold,
                  Max_Threshold=match.Max_Threshold,
                  Target_Threshold=match.Target_Threshold,
                  Historian_Tag=match.Historian_Tag
               )
               print(f"    - {param_row.ParameterName} ({param_row.ParameterID}): {param_row.Historian_Tag} [confidence={match.Confidence}]")
         else:
            print(f"  No parameters found for {global_station_id}")

      print(final_machine_row)

   write_match_report(line, station_reports,
                      total_tags=len(tag_records) or None,
                      profile=tag_profile if tag_records else None)

