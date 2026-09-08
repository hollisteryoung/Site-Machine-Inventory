# PLAN: AC13 Tag Graph — Ownership, Parameters, Process Monitoring

Agreed plan. Target stack: **Neo4j (Community/Desktop)** for structure; **Ignition** for
time-series testing, designed vendor-neutral so the same model can be handed to **LITMUS**
later. Work through Phases 0–6 in order; each phase has checkboxes and an acceptance test.

---

## Context

- `tokenizer.py` parses Rockwell RSLogix 5000 `.L5X` exports (XML ladder logic) in
  `Chris_AC13/` (29 program files, controller `RFCBM_1PC_BAL_AC13`).
- It already does: instruction/tag extraction from compact ladder text (`tag_calls`),
  write-position map (`WRITES`), station ownership by program prefix `_NN_`
  (`station_of` + `find_owners`), LIM limit extraction (`find_limits`), HMI-noise
  filtering (`is_hmi_plumbing`), and a `Parameter` object builder.
- Goal now: load everything into a **graph database**, map Site → Location → Machine
  from the directory structure, filter tags by *classification* (not deletion), model
  the manufacturing process order (sequencer steps + phase bools), and enable
  "where did problems occur" queries against the historian.

**Golden rule: never delete at ingestion.** Store every tag in the graph with
classification properties; filtering happens at query time. The graph is the archive;
parameter catalogues and monitoring lists are views over it.

---

## 1. Architecture

Two layers, one bridge:

1. **Neo4j graph** = anatomy of the machine (structure only; the L5X carries no values):
   Site → Location → Machine → Station → Program → Routine → Tag, plus ownership,
   dataflow (`FLOWS_TO`), and the process-order model (Step nodes).
2. **Time-series store** = vitals. Ignition Tag Historian for testing now; LITMUS later.
   The graph stores the historian path on each Tag node as `opcItemPath`, so a query can
   jump from structure to live data regardless of vendor.

Bridge data already in the repo:
- `Ballina/Ostomy/AC13_1PC_V34_R01AG_Controller_Tags.CSV` — RSLogix controller tag
  export (NAME/DESCRIPTION/DATATYPE/SPECIFIER) to join tag names to historian paths.
- `LineProcess.py` + `Schema.py` — existing reader/profile/matcher pipeline and
  ParameterRow/StationRow schemas. Reuse: the graph should be able to *export* rows that
  satisfy `Schema.py`; `LineProcess.py`'s "profile the convention instead of hardcoding"
  philosophy should guide the classifier in Phase 3.

---

## 2. Graph schema (nodes and edges)

### Node labels and IDs

IDs are deterministic and machine-prefixed (tag names repeat across machines; station
numbers repeat across machines).

| Label      | Key properties                                                                  | ID example                          |
|------------|----------------------------------------------------------------------------------|-------------------------------------|
| `Site`     | `name`                                                                           | `Ballina`                           |
| `Location` | `name` (Ostomy / Continence)                                                     | `Ballina:Ostomy`                    |
| `Machine`  | `name`, `controller` (from L5X `<Controller>`), `software_revision`, `export_date`| `AC13`                              |
| `Station`  | `station_no` (from `_NN_` program prefix), `name`, `type`                        | `AC13:04`                           |
| `Program`  | `name`, `file`                                                                   | `AC13:_04_BAR_PNC`                  |
| `Routine`  | `name`                                                                           | `AC13:_04_BAR_PNC:AUTO`             |
| `Tag`      | `name`, `data_type`, `radix`, `description`, `alias_for`, `external_access`,     | `AC13:PNC_PRESSURE_OK`              |
|            | `opcItemPath`, `tag_class`, `monitor_rank`                                       |                                     |
| `Step`     | `station_no`, `step_no`                                                          | `AC13:04:step:20`                   |
| `Limit`    | `low`, `high`, `circular`                                                        | (child of a Tag)                    |

### Edge definitions

Every edge is directed and carries **evidence properties** (instruction, position, rung,
file) so any claim in the graph can be audited back to a rung.

| Edge              | Direction                 | Evidence properties                                        |
|-------------------|---------------------------|------------------------------------------------------------|
| `HAS_LOCATION`    | Site → Location           | —                                                          |
| `HAS_MACHINE`     | Location → Machine        | `source_folder`                                            |
| `CONTAINS`        | Machine → Station, Station → Program, Program → Routine | —                         |
| `WRITES`          | Routine → Tag             | `instruction`, `position`, `rung_number`, `latch` (OTL/OTU), `literal_value` |
| `READS`           | Tag → Routine             | `instruction`, `rung_number`                               |
| `OWNS`            | Station → Tag             | `evidence` = `single_writer` or `shared` (keep ambiguity, don't drop) |
| `ALIASES`         | Tag → Tag                 | `alias_for` from declaration                               |
| `HAS_LIMIT`       | Tag → Limit               | `rung_number`                                              |
| `FLOWS_TO`        | Tag → Tag                 | `instruction`, `rung_number` — from instruction semantics: `MOV(A,B)` → A→B; `ADD(A,B,C)` → A→C, B→C; `LIM(L,V,H)` → L→V, H→V |
| `TRANSITIONS_TO`  | Step → Step               | `when_condition` (list of condition tags), `next_value`    |
| `SETS`            | Step → Tag                | action/value written in that step                          |
| `PHASE`           | Station → Tag             | `order` (integer position in the station's process)        |

Rules:
- Dedupe WRITES/READS per (routine, rung, tag, instruction) and store a `count`
  property — frequency is an importance signal.
- Uniqueness constraints: `(Machine, Tag.name)`, `(Machine, Station.station_no)`,
  `(Machine, Program.name)`. Use `MERGE` on IDs everywhere.
- Do NOT create Tag→Tag edges from name similarity — only from actual rung dataflow
  (`FLOWS_TO`) and aliases (`ALIASES`).

Example Cypher for constraints:

```cypher
CREATE CONSTRAINT tag_uid IF NOT EXISTS
FOR (t:Tag) REQUIRE (t.machine, t.name) IS UNIQUE;
CREATE CONSTRAINT station_uid IF NOT EXISTS
FOR (s:Station) REQUIRE (s.machine, s.station_no) IS UNIQUE;
```

---

## 3. Tag filtering — classify, don't delete

Replace the binary keep/drop in `tokenizer.py` (`is_hmi_plumbing` drop) with a
**5-rank classifier**. All tags are stored; `monitor_rank` and `tag_class` decide which
views they appear in.

| Rank | Class                | Signals                                                                               | Use                                        |
|------|----------------------|---------------------------------------------------------------------------------------|--------------------------------------------|
| 1    | Measurement/Setpoint | `REAL`/`INT` + `Radix=Float`; names `PRESSURE`, `TEMP`, `POS`, `CYCLE_TIME`, `_SP`, `_RECIPE`, `_MIN/_MAX/_ALLOWED` | Parameter catalogue (`Schema.py` ParameterRow) |
| 2    | Process-state bool   | `BOOL` + `*_DONE`, `*_COMPLETE`, `*_STARTED`, `*_OK`, `*_FAILED`, `*_REJECT`, `*_IN_POSITION` | Manufacturing-order signals               |
| 3    | Sequencer & alarm    | `STEP_AUTO[*]`, `STEP_HOME`, `STEP_ALARM[*]`, `*_EX` (cycle-time excess)              | State machine, bottleneck, fault decoding |
| 4    | HMI plumbing         | `_PB`, `_PB_VIS`, `_VIS`, `ANIMATION`, `HMI PUSH BUTTON`/`HMI VISIBILITY`/`HMI ANIMATION`/`HMI INDICATOR` in description | Store, exclude from catalogues            |
| 5    | Infrastructure       | `TIMER_*`, `ONS_ARRAY`, `MOTION_*`, raw I/O aliases (`MAN02:I.Data…`)                 | Root-cause tracing only                   |

Classification signals, in priority order:

1. **L5X attributes**: `TagType=Alias` + `AliasFor` target (drive status vs raw I/O),
   `DataType`/`Radix`, `ExternalAccess`.
2. **Description keywords**: HMI markers, `CYCLE TIME`, `RECIPE`, unit words.
3. **Name suffixes/prefixes**: `_PB`, `_VIS`, `_PB_VIS`, `_EX`, `_SP`, `_MIN`, `_MAX`,
   `_ALLOWED`, `DONE/FAILED/OK`, `PNC_/CELL_/DRV_` station prefixes.
4. **How logic uses it**: OTE inside an `HMI` routine = plumbing; MOV/ADD destination =
   computed value; only-XIC'd tag = sensor input.

Two deliberate fixes to current behaviour:

- **Read-only tags are currently dropped** (`find_owners` only keeps tags that are
  *written*). Raw feedback/sensor tags are only read and never owned. Fix: read-only
  tags become candidates for ownership by the station that *reads* them (weaker
  evidence, `OWNS.evidence = 'single_reader'`), so raw measurements reach Rank 1.
- **`extract_unit` returns all words, not units.** Replace with a unit dictionary map:
  `PRESSURE → bar`, `TEMP → °C`, `TIME → s`, `POS → mm`, `TORQUE → Nm`, `SPEED → rpm`.
  Fall back to blank; never guess a unit from a tag that only says `_REAL`/`_DISPLAY`
  (see `Schema.py` Unit_Verified guidance).

---

## 4. Process order — tracking the bools to find where problems occur

Three layers, each answering a different question.

### 4.1 State machine from the sequencer (structure only, no historian)

The rungs encode a per-station state machine: `STEP_AUTO[i]` is the current step
integer, and each rung is `EQU(STEP_AUTO[i], X) …conditions… MOV(Y, STEP_AUTO[i])`.

Example (station 04, `_04_BAR_PNC_Program.L5X` rung 3):
`EQU(STEP_AUTO[4],5)[OTE(PNC_INDEX_DIAL_REQ) ,XIC(MAIN_DIAL_INDEX_DONE) MOV(8,STEP_AUTO[4]) ]`
→ in step 5, set `PNC_INDEX_DIAL_REQ`; when `MAIN_DIAL_INDEX_DONE` is true, go to step 8.

Algorithm:
1. For each station's program files, find every `EQU(STEP_AUTO[i], N)` rung.
2. Create Step node `N`; the OTE/OTL/MOV tags inside become `SETS` edges.
3. Every `MOV(Y, STEP_AUTO[i])` creates `TRANSITIONS_TO` from the current step to `Y`,
   with `when_condition` = the XIC/XIO tags in scope.

The comment at rung 11 of `_04_BAR_PNC` gives the station→index map (BARRIER LOAD=1,
BAG LOAD=2, PREHEAT1=3, PREHEAT2=4, FORMING=5, PUNCH=6, PRINT=7, BAG GLUE=8, PNC=9,
BAG OFFLOAD=10) — use it to name Step/Station nodes.

### 4.2 Phase-bool ordering per station

From rung order and the `*_DATA_*` alias groups, derive the expected phase order, e.g.
for PNC: `BARRIER_LOADED → GLUE_STARTED → PNC_STARTED → PRESS_OK → CURE_COMPLETE →
PROCESS_DONE`, with `*_REJECT` / `*_FAILED` as exit paths. Store as
`(Station)-[:PHASE {order:N}]->(Tag)`. Where the L5X alone can't fix the order, leave
`order` null rather than guessing.

### 4.3 Runtime diagnosis (graph + historian)

Graph query answers **where**; historian answers **when**:

- **Fault localisation**: find the writer of `*_FAILED` and its `SETS`/`READS`/`FLOWS_TO`
  neighbourhood → "step 20 (wait for cure time / pressure OK) sets `PNC_PROCESS_FAILED`
  and depends on `TIMER_OPER[10]`, `PNC_SIDE_1_AT_CURE_POS`, `PNC_PRESSURE_OK`".
- **Historian event scan**: for each `*_FAILED`/`*_REJECT` tag, pull its rising edges
  from the historian; at each timestamp also read `STEP_AUTO[i]` and the phase bools →
  "failures cluster in step 20 between 14:00–15:00".
- **Bottleneck**: `CELL_CYCLE_TIME[0].*` holds per-station cycle times; the `*_EX`
  tags are REAL accumulators of "cycle time excess" (the station being critical path),
  and the `ST_TIME_CRITICAL[0..1]` array holds the ranked top-2 critical stations
  (STATION + CYCLE_TIME) — see `_04_BAR_PNC` rungs 10–11
  (`DIV(TIMER_OPER[11].ACC,1000,CELL_CYCLE_TIME[0].PNC)`). Bottleneck = station held in
  `ST_TIME_CRITICAL[0]`, or fastest-growing `*_EX` accumulator per shift in the historian.
- **Alarm decoding**: `STEP_ALARM[*]` (INT array) is an alarm code per station; map each
  code back to the rung that sets it for a fault decoder table.

Vendor-neutrality for the LITMUS handover: keep the historian dependency to ONE
property (`opcItemPath`) plus a documented query pattern ("rising edge of tag X, joined
with tag Y at same timestamp"). Ignition Tag Historian supports this today; LITMUS will
need the same two primitives.

---

## 5. Course of action

### Phase 0 — Stabilize the extractor (do this first; bugs poison everything downstream)

- [ ] Fix `read_references` loop scope (`tokenizer.py` line 117: `root.iter('Rung')` →
      `routine.iter('Rung')`) — currently every rung is duplicated per routine and
      routine names are wrong.
- [ ] Fix trailing-comma tuples in `Parameter.__init__` (lines 211, 215, 216 —
      `radix`, `max_value`, `circular` become 1-tuples).
- [ ] Fix `find_limits` string comparison (line 182: `if low > high` is lexicographic;
      parse to float, handle circular limits numerically).
- [ ] Convert to an importable module with a CLI; emit JSON output; remove module-level
      execution, the `input()` pause loop, and dead code (lines 29–30).
- [ ] Keep rung-level context (rung number, routine, file) in every reference record.

**Acceptance:** one deterministic run over all 29 L5X files produces one reference row
per (routine, rung, tag, instruction); output is JSON, no interactive pauses.

### Phase 1 — Schema & database

- [ ] Install Neo4j Community/Desktop; create a local database.
- [ ] Write `graph_schema.md` from §2; create uniqueness constraints (see Cypher above).
- [ ] Hand-load a small sample (one station, one routine) to prove the model.

**Acceptance:** the sample subgraph round-trips: same nodes/edges/properties read back.

### Phase 2 — Ingest the hierarchy

- [ ] Write the site manifest (`sites.yaml`) from the §9 inventory; align machine/line
      IDs with `Data Hierachry/OT Historian Metadata Model_3852.xlsx` (the canonical
      Lines/Machines/Parameters workbook `LineProcess.py` already uses).
- [ ] Map directory → Site/Location/Machine via the manifest (`Ballina/Ostomy/...`,
      `Chris_AC13/...`), falling back to L5X `<Controller>` metadata (name, software
      revision, export date) — never hardcode paths in code.
- [ ] Load Programs → Routines → Tags (controller + program scope), declarations,
      aliases (`ALIASES`), WRITES/READS edges with evidence, `OWNS` (single_writer /
      shared / single_reader).
- [ ] Merge `_03_REG_EVENT_PROG`, `_03_REG_INPUT_STATUS`, `_03_BAR_ELEV` etc. into the
      same Station node (shared `_NN_` prefix).

**Acceptance:** AC13 fully loaded; node/edge counts match an independent file scan;
`OWNS` ambiguity is stored, not discarded.

### Phase 3 — Classification & parameters

- [ ] Implement the 5-rank classifier (§3) with the four signal groups; store
      `tag_class` + `monitor_rank` on every Tag.
- [ ] Fix limit extraction (numeric, circular), add unit dictionary, extract
      `HAS_LIMIT` nodes.
- [ ] Export a Parameter catalogue view (Cypher) whose rows satisfy `Schema.py`
      `ParameterRow`/`StationRow`.

**Acceptance:** HMI-plumbing tags are excluded from the catalogue but present in the
graph; each Rank 1/2 tag appears exactly once in the catalogue with unit/limits.

### Phase 4 — Process-order model

- [ ] Extract `STEP_AUTO` state machines → Step / `TRANSITIONS_TO` / `SETS` (§4.1).
- [ ] Derive phase-bool ordering → `PHASE` edges (§4.2).
- [ ] Map `STEP_ALARM` codes and `*_FAILED`/`*_REJECT` writers.
- [ ] Implement `FLOWS_TO` with a full instruction-semantics table (extend the `WRITES`
      map: every instruction's operand roles — sources vs destination vs condition).

**Acceptance:** for station 04, the query "all paths into `PNC_PROCESS_FAILED`" returns
its setting step, transition conditions, and upstream tags.

### Phase 5 — Historian bridge (Ignition now, LITMUS-ready later)

- [ ] Join `Ballina/Ostomy/AC13_1PC_V34_R01AG_Controller_Tags.CSV` (and any
      Kepware/Ignition `tags.json` for AC13) onto Tag nodes; populate `opcItemPath`.
- [ ] Where no export path exists, derive the convention `[Area]/[Line]/[Machine]/
      [Station]/[Tag]` (see `LineProcess.py`/`Schema.py` examples) and mark the node
      `path_source = 'inferred'`.
- [ ] Document the two historian query primitives (rising-edge of tag; value of tag at
      timestamp) so LITMUS can implement the same contract.

**Acceptance:** at least one Rank 1 tag verified end-to-end: graph node → `opcItemPath`
→ live Ignition value → graph query result.

### Phase 6 — Query & report layer

- [ ] Save three reusable Cypher queries: fault localisation, bottleneck/critical-path,
      parameter catalogue export.
- [ ] Regenerate the pyvis explorer from the graph (optional); add a per-station
      monitoring checklist report (measurements + limits + phase bools + alarm codes).

**Acceptance:** each of the §4.3 questions is answerable as a saved query run against
the real DB; report generator runs offline from the graph alone.

---

## 6. Decisions agreed

- Graph DB: **Neo4j Community/Desktop** (Cypher).
- Time-series for testing: **Ignition Tag Historian**; final target **LITMUS** — the
  graph model keeps the historian dependency to `opcItemPath` + two query primitives so
  the handover is a contract, not a rewrite.
- Plan saved as this file; phases are checklist-scoped and do not require model access
  to execute.

---

## 7. Python implementation guidelines (detailed)

Working principles that apply to every phase:

- **Every stage writes a JSON artifact** (parse → extract → classify → sequence → load).
  Downstream stages read artifacts, so you can re-run any step without re-parsing L5X.
- **Extract once, load idempotently** — re-running the loader must not duplicate
  anything (MERGE on node IDs).
- **Pure functions, no side effects**: no module-level file I/O or prints except under
  an entry point. Progress messages go to stderr; data goes to files.
- **Version every artifact** (`{"schema": "l5x-extract", "version": 1, ...}`) so later
  code can detect old files.
- **Every derived claim carries its evidence** (file, routine, rung, instruction) — this
  is what makes the graph auditable, and it survives from `tokenizer.py`'s reference
  records into the WRITES/READS edge properties.
- **Never silently drop**: anything skipped (unparseable rung, unknown instruction,
  unclassified tag) goes into a `skipped.json` artifact with a reason.

### 7.1 Phase 0 — extractor restructure

Suggested module layout (package `l5xgraph/`):

- `tokenize.py` — keep the existing regex token spec and `tag_calls` logic, split into
  two functions: `tokenize(text)` (tokens with spans) and `iter_calls(text)` (yields
  instruction + operand list). This part of `tokenizer.py` is sound; do not rewrite it.
- `l5x.py` — the XML layer: `read_declarations(root)` and `read_references(root)` with
  the fixes below.
- `models.py` — plain dataclasses (`Reference`, `Declaration`, `Limit`); no stray
  trailing commas (the current `Parameter.__init__` makes tuples by accident).
- `cli.py` — entry point: `python -m l5xgraph extract Chris_AC13 -o artifacts/refs.json`,
  plus `--limit-files N` and `--sample N` flags for eyeballing.

`read_references` contract:

- Iterate programs with `Use == "Target"` → their routines → **`routine.iter('Rung')`**
  (fixes the duplication bug at `tokenizer.py` line 117).
- Per rung: read the `Number` attribute, guard missing `<Text>`, run `iter_calls`,
  skip `JSR`, validate with `is_tag_operand`, record: file, program, routine,
  rung_number, instruction, position, is_write, latch flag (OTL/OTU), and
  `literal_value` when the operand is a constant.
- Dedupe by (file, routine, rung_number, instruction, base_tag, position) with a
  `count` — one row per key.

`read_declarations` contract:

- Iterate `root.iter('Tags')` direct children; capture Name, DataType, Radix, TagType,
  AliasFor, Constant, ExternalAccess, Description (guard `None`), and the scope
  (controller vs program).
- Key by (scope, base_name); do NOT let program-scope silently overwrite controller-scope
  — record `declared_in` on conflicts.
- Skip UDT `<Member>` elements in v1 (there are 1,554 of them); count them into the
  artifact stats and revisit later.

Validation harness (no model needed):

- Assert rung coverage: parsed rungs ≤ the known total (1,393 across the folder).
- Assert dedupe: exactly one row per dedupe key.
- `--sample` flag prints parsed calls next to the raw rung text — verify rung 3 of
  `_04_BAR_PNC` by hand (step 5 → `OTE(PNC_INDEX_DIAL_REQ)`, `MAIN_DIAL_INDEX_DONE` →
  step 8).
- Keep the first good run as a golden file; later changes must diff against it only
  where intended.

### 7.2 Phase 1 — Neo4j setup

- Use the official `neo4j` Python driver; no ORM in v1.
- Connection from environment variables (URI/user/password), never in code.
- One small `db.py` exposing a query runner and a batched writer that chunks rows
  through `UNWIND` (500–1,000 per transaction).
- Keep a `schema.cypher` file as the single source of truth for constraints/labels/
  relationship types; apply it from a `db init` CLI command.
- Constraint violations should be logged with the offending ID, never crash the load.

### 7.3 Phase 2 — ingestion

- A small config file (YAML/JSON) maps folders → site/location/machine; machine identity
  falls back to the L5X `<Controller>` Name / SoftwareRevision / ExportDate. Never
  hardcode paths in code.
- Load order: Site → Location → Machine → Program → Routine → Tag → edges. MERGE by ID
  everywhere; a re-run must be a no-op.
- Ownership rules (record the evidence on the `OWNS` edge):
  - exactly one writing station → `single_writer`
  - more than one writing station → `shared` (list the stations, keep the edge)
  - no writers but readers in exactly one station → `single_reader`
  - no references at all → no OWNS edge (declaration-only tag)
- Aliases: `ALIASES` edge + keep `alias_for` on the node; do not create nodes for raw
  I/O targets in v1.
- After loading, print counts per label and per edge type and save them — compare
  against the file scan (29 files, 3,546 tag declarations) to catch silent losses.

### 7.4 Phase 3 — classification

Rule-engine shape:

- An ordered list of rule functions; each returns `(rank, tag_class, source)` or `None`;
  first hit wins; nothing hitting is rank 0 `unclassified` — which must be visible, not
  silent.
- Rule order (strongest signal first):
  1. **L5X attributes** — `AliasFor` to raw I/O (`I:`/`MAN`…) → rank 5; analog
     `DataType`/`Radix=Float` → rank 1 candidate.
  2. **Description keywords** — HMI markers → rank 4; `CYCLE TIME`/`RECIPE` → rank 1.
  3. **Name patterns** — `_SP/_MIN/_MAX/_ALLOWED` → rank 1;
     `_DONE/_COMPLETE/_OK/_FAILED/_REJECT/_STARTED/_IN_POSITION` → rank 2;
     `STEP_*` / `*_EX` → rank 3; `_PB/_VIS/ANIMATION` → rank 4;
     `TIMER_*/ONS_/MOTION_` → rank 5.
  4. **Usage** — written by OTE inside an `HMI` routine → rank 4; read-only analog →
     rank 1 (single_reader).
- Store `class_source` (which rule fired) on the Tag for audit.
- Tuning loop: dump every `unclassified` tag to a file, review it by hand, add rules —
  the same "profile the convention instead of hardcoding" philosophy as `LineProcess.py`.
  Do this before trusting the catalogue.
- Units: small dictionary token → unit (`PRESSURE→bar`, `TEMP→°C`, `TIME→s`, `POS→mm`,
  `TORQUE→Nm`, `SPEED→rpm`); match against description + name tokens; blank when no hit;
  `Unit_Verified=false` unless the description literally states the unit.
- Limits: parse low/high as floats when both are literals (`circular = low > high`
  numerically); when low/high are tag operands, store pointer references instead (like
  `Schema.py` Min/Max_Threshold); record `limit.kind` = literal | tag.
- Parameter catalogue export: rows satisfying `Schema.py`; deterministic `ParameterID`
  from a counter over stable sort order (machine, station_no, tag name); Rank 1 before
  Rank 2.

### 7.5 Phase 4 — process-order model

- Sequencer detection: array names matching `STEP_`; the station index is the array
  subscript in `EQU(STEP_AUTO[i], N)`.
- Per rung: find step-defining EQUs (first operand a STEP array, second a literal) — a
  rung can define several steps; find transitions `MOV(literal, STEP_AUTO[i])` → edge
  from each in-scope step to the literal.
- `when_condition` = the XIC/XIO operands between the EQU and the MOV. **v1
  approximation**: use rung-level scope (all XIC/XIO in the rung) and record
  `extraction_version=1`, `scope='rung'` on the edge — parallel branches `[... , ...]`
  are flattened. v2 can scope per branch using the paren-depth the tokenizer already
  tracks.
- PHASE ordering: rank-2 tags ordered by rung number of their first write within the
  station's programs; store `order` only when unambiguous; `*_REJECT/*_FAILED` get
  `phase_type='exit'` and no order.
- `FLOWS_TO` semantics table (extend the existing `WRITES` map — roles per instruction):

| Instruction | Reads (sources) | Writes (dest) |
|---|---|---|
| XIC, XIO | 0 | — |
| OTE, OTL, OTU | — | 0 |
| MOV, TRN | 0 | 1 |
| ADD, SUB, MUL, DIV | 0, 1 | 2 |
| EQU, NEQ, GRT, GEQ, LES, LEQ | 0, 1 | — |
| LIM | 0, 1, 2 (low, test, high) | — (limit relationship on test) |
| TON, RTO, CTU, CTD | 0 (timer tag), 1 | 0 (PRE); ACC/DN are reads of the timer tag |
| RES | — | 0 |
| ONS | — | 0 (internal one-shot bit) |
| JSR | skip | — |

- Edge-volume guard: only materialise `FLOWS_TO` when at least one end is Rank 1–3.
  This is the only place edge counts could explode; with ~1.4k rungs it stays small.

### 7.6 Phase 5 — historian bridge

- Join: exact case-insensitive match of L5X tag names against the RSLogix CSV `NAME`
  column; aliases joined via `SPECIFIER` ↔ `AliasFor`; set `path_source` =
  `export` | `inferred` per tag.
- Where no export path exists, build the path by the site's OPC convention seen in
  `LineProcess.py`/`Schema.py` examples (`[Area]/[Line]/[Machine]/[Station]/[Tag]`) and
  mark it inferred.
- Document the two primitives in a `historian_contract.md`: (1) rising edges of tag X
  over an interval; (2) value of tag X at timestamp T. Verify both in Ignition (Script
  Console history query) before calling the bridge done — this is the contract LITMUS
  must later implement.

### 7.7 Phase 6 — queries & reports

- Fault localisation: from each Rank-2 `FAILED/REJECT` tag, walk `<-[:SETS]-(Step)`,
  expand `when_condition` and `FLOWS_TO` upstream, return distinct paths.
- Bottleneck: read the `CELL_CYCLE_TIME` writes — `ST_TIME_CRITICAL[0..1]` holds the
  ranked top-2 critical stations; trend `*_EX` accumulators per shift in the historian.
- Catalogue: filter Rank 1–2, join OWNS + Limit, emit `Schema.py`-shaped rows.
- Report generator: plain Python reading the DB through `db.py`, emitting markdown —
  use `LineProcess.write_match_report` as a *style reference*, not a dependency.

### 7.8 Cross-cutting pitfalls

- Idempotency: every load step must survive being run twice.
- Artifacts over memory: never re-parse when a saved artifact exists (L5X parsing is the
  slow step; classification/loading are fast).
- Keep the golden-file diff habit from Phase 0 for every stage.
- Test against the measured constants: 29 files, 3,546 tag declarations, 1,554 UDT
  members, 1,393 rungs, 544 HMI-marker descriptions.

---

## 8. Why keep the HMI plumbing (and how to cap it)

Measured on AC13: **3,546 tag declarations total**; 544 carry HMI-marker descriptions
(~15%), plus 344 `*_PB` and 119 `*_VIS` names. The "noise" is a few hundred nodes out
of a few thousand — trivial for Neo4j Community. Node count is not the cost driver;
**edges** are, and those are bounded by the 1,393 rungs.

Reasons to keep them (as nodes, excluded from views):

1. **Operator actions are audit context.** `CELL_DRY_CYCLE_MODE_PB`, bypass/abort
   buttons — when a failure investigation asks "was dry-cycle mode active?", deleting
   these makes the question unanswerable without re-ingesting.
2. **Visibility flags encode machine state.** `*_PB_VIS` tags are written *by process
   logic* (e.g. drive-enable button visible only when faulted and ready); dropping them
   removes real state logic from the graph.
3. **Buttons connect to parameters.** The HMI surface is often the only human-readable
   link to a setpoint; keeping plumbing preserves that link for SMEs reviewing the model.
4. **Deletion is irreversible; keeping is reversible.** If kept with `monitor_rank=4`,
   removing them later is one query (`MATCH (t:Tag {monitor_rank:4}) DETACH DELETE t`).
   If deleted now and needed later, the whole ingest must be re-run. Cheap-to-defer
   decisions should be deferred.
5. **It's less code, not more.** The current code goes out of its way to drop them
   (`is_hmi_plumbing` + the skip in `build_parameters`); stopping the deletion and
   setting a property instead is a simplification.

If the graph still feels too heavy, the compromise is: **keep every node**, but
(a) default every view/query to `monitor_rank <= 3`, and (b) once OWNS has been
computed, skip WRITES/READS edges for rank 4/5 (or only keep edges touching rank 1–3).
Nodes cost nothing; edges are the only thing worth capping.

---

## 9. Rollout: site → area → machine

The same pipeline repeats per machine. What differs per machine is only the **data
tier** and the **manifest entry** — the graph schema is identical.

### Current inventory (measured)

| Area | Machines | Tag data | Notes |
|---|---|---|---|
| Continence | 16: HOS3, NGP1, NGP2, PFS2, PFS5, PS1–PS8, VCL4, VCL5, VCL6 | `tags.json` each (Ignition) | NGP2 has a Match_Report (pipeline precedent) |
| Ostomy | 18: 1AC3–1AC8, AC13, AC14, BFX, BIM03, HF11, HU2, HU3, K2, K3, K9, K10, K13, K14, P16 | 1AC3–1AC8, K2, K3, K9, K10, K13, K14, HF11: CSV exports; BFX, BIM03: `tags.json`; HU2, HU3, P16: PDFs only | area root holds the AC13/AC14 controller CSVs + `tags.json`; 1AC3, K9, K10, K13, K14 have Match_Reports |
| (workspace root) | `Chris_AC13/` | 29 `.L5X` | the only logic export so far; belongs to Ballina/Ostomy/AC13 |

### Three ingest tiers (same schema, different edge completeness)

1. **L5X tier (full logic graph)** — AC13 only today: WRITES/READS, Step/TRANSITIONS_TO/
   SETS/PHASE, FLOWS_TO, ownership from logic. AC14 joins this tier when its L5X export
   arrives.
2. **Export tier (tags only)** — all Continence JSON machines and the Ostomy CSV/JSON
   machines: Tag nodes + declarations + classification + `OWNS` from the
   `LineProcess.py` matcher's station attribution (evidence `numeric`/`keyword`/etc.),
   no logic edges. This is where `LineProcess.py` and the graph meet: its
   `Match_Report_*.md` stations are the Station nodes.
3. **PDF tier (hierarchy only)** — HU2, HU3, P16: Machine/Station nodes discovered from
   the PDFs (the existing `LineProcess.py` discovery path), no Tag nodes until an export
   exists.

### Machine identity and merge rules

- **Manifest-driven**: `sites.yaml` entries `{site, area, machine_id, folders, sources}`.
  One machine can have several folders/sources — AC13 is `Chris_AC13/*.L5X` + the
  area-root `AC13_1PC_V34_R01AG_Controller_Tags.CSV`, both loading into the same
  Machine node via MERGE on `machine_id`.
- **Align IDs with the canonical workbook**: `Data Hierachry/OT Historian Metadata
  Model_3852.xlsx` (Lines/Machines/Parameters sheets) is what `LineProcess.py` already
  reads/writes. The graph's LineID/MachineID/StationID values must match it so the
  catalogue can be written back into that workbook later.
- **Never rename folders**: the manifest maps reality (e.g. the `Chris_AC13` dump vs the
  `Ballina/Ostomy` layout mismatch is a manifest line, not a file move).
- **Cross-machine safety**: tags and stations are machine-prefixed in the ID scheme;
  Site/Location nodes are shared and MERGE'd; nothing merges across machines unless the
  manifest says so.
- **Cell/global tags** (AC13 `_00_CELL_*` program, area-root `tags.json`) attach to the
  Machine or a per-machine `CELL` station, never to a physical station.

### Rollout order

1. **AC13** (L5X tier) — proves the full pipeline; already planned as Phases 0–6.
2. **Ostomy CSVs**: 1AC3 first (has a Match_Report to compare against), then 1AC4–1AC8,
   K2, K3, K9, K10, K13, K14, HF11.
3. **Continence JSON**: NGP2 first (Match_Report + known profile exist), then the
   remaining 15 machines.
4. **BFX, BIM03** (JSON), then hierarchy-only **HU2, HU3, P16**.
5. **AC14** whenever its L5X arrives — every new L5X dump is treated as tier 1.

### Per-machine checklist (repeat for every machine)

- [ ] Manifest entry exists; IDs match the Excel workbook.
- [ ] Source format sniffed by content (`LineProcess.load_tag_records` logic) — never
      assumed from file extension.
- [ ] Load is idempotent (re-run produces identical counts).
- [ ] `unclassified` tag dump reviewed before the catalogue export.
- [ ] Report emitted per machine (Match_Report style).

---

## Phase 7 — Roll out site-wide (added to the course of action)

- [ ] Write `sites.yaml` from the §9 inventory; align IDs with the Excel metadata model.
- [ ] Implement the three-tier loader (L5X / export-only / PDF-only) on top of the same
      schema — tiers differ only in which edge types they populate.
- [ ] Load Ostomy CSV machines (1AC3 first; compare its graph against its existing
      Match_Report).
- [ ] Load Continence JSON machines (NGP2 first).
- [ ] Load BFX/BIM03, then hierarchy-only HU2/HU3/P16.
- [ ] Add AC14 to the manifest and load it when its L5X export arrives.

**Acceptance:** every machine folder is covered by the manifest or explicitly listed as
"awaiting data"; every machine with a tag export has Tag nodes + `OWNS` +
classification in the graph; a full-site re-run is a no-op (idempotent).
