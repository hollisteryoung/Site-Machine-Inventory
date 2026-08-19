# Tag Matching Report - Line 1AC3

This summarizes, for every station found on this line, which historian tags were kept as genuine process parameters and why. Parameters found by a weak match strategy (`keyword`, `keyword_all`, `legend_code`) or below 0.5 confidence are the ones most worth a second look from someone who knows the physical machine.

## Summary

- 25 station(s) processed against a `rslogix_csv` export of 1430 tags.
- 1895 candidate tag(s) considered across all stations.
- 1266 of those candidates are already wired to an operator HMI screen; 629 exist only in the controller. Tags in that second group are invisible to the traditional approach of picking a tag off an HMI, and are the clearest thing this catalogue adds.
- 6 station(s) returned no candidates at all: Ink Jet Station, Label Applicator Conveyor, Insert & Drumhead Infeed System, Insert/Drumhead Load Robot, Insert Corona/Glue Station, Insert Press Station.
- **This run re-did the matching stage only.** 14 of these stations already hold 139 parameters in the workbook from an earlier run; those were not re-judged here. Judging in this run was limited to the two stations the workbook has nothing for, which is where the actual gap was.

## Tag export conventions this run assumed

Discovered by the profiling step and cached to `Tag_Source_Profile.json`. If a whole line matches badly, suspect these first - and correct that file by hand rather than the code, since every later run reads it back.

- Station identity read from: description, tag_path (this export's tag names are largely opaque device codes, but its DESCRIPTION column names the station in plain English for 97% of tags).
- Station code style: *mixed*.
- Numeric station codes: none - this machine's stations are named, not numbered.
- 16 export-scaffolding token(s) excluded from keyword matching: `hmi`, `animation`, `push`, `button`, `screen`, `part`, `data`, `stream`, `cell`, `machine`, `piece`, `array`, `display`, `msg`, `comms`, `ethernet`.
- 10 opaque device code(s) resolved to plain English **from the export itself, with no hand-written legend**: `DRV01` = MAIN DIAL SERVO, `DRV02` = BARRIER INFEED MAGAZINE SERVO, `DRV03` = BARRIER INFEED ELEVATOR SERVO, `DRV04` = BARRIER PRESS-N-CURE STATION SERVO, `DRV05` = BARRIER PICK-N-PLACE/CORONA TREAT SERVO, `DRV06` = BARRIER PICK-N-PLACE/CORONA TREAT STEPPER, `DRV08` = BAG GRIPPER STEPPER, `R1` = BAG LOAD ROBOT, `R2` = BARRIER LOAD/BAG OFFLOAD ROBOT, `VISION` = VISION INSPECTION STATION.
- Three shared I/O modules (`MAN01`, `MAN02`, `MAN03`) were deliberately kept OUT of that legend: each one's description names several stations at once, so admitting them would pull one tag family into five different stations.

**Coverage caveat:** This is the controller export for the 1-PIECE BAG configuration only (file: Rigid_Film_Conv_1PC_PN3_AC3_R18). The machine's insert/drumhead product configuration is documented in the manual but has NO presence in this export: 'INK'/'JET'/'LABEL'/'APPLICAT' return zero hits across all 1430 tags, and 'INSERT'/'DRUM' return only incidental ones. So Ink Jet Station, Label Applicator Conveyor, Insert & Drumhead Infeed System, Insert/Drumhead Load Robot, Insert Assembly Station, Insert Corona/Glue Station, Insert Press Station, Drumhead Pre-placement Station and Drumhead Assembly Station are expected to yield nothing here - that is a genuine scope limit of this file, not a matching failure, and no tuning will fill them in. A separate controller export would be needed. Second caveat: the phrase 'MAIN DIAL PART DATA STREAM' is a shared data-structure wrapper appearing in ~30% of tags across many different stations, so tags mentioning Main Dial are frequently owned by another station and must be judged on which station the description actually attributes them to. Three shared I/O modules (MAN01, MAN02, MAN03) were deliberately excluded from the code legend because each one's description names several stations at once and would otherwise pull a whole tag family into all of them.

## Machine: Auto Coiner (MC002)

| Station | Candidates | HMI-wired | PLC-only | Params already in workbook | Judged this run |
|---|---|---|---|---|---|
| Barrier Infeed System | 69 | 33 | 36 | 1 | - |
| Barrier Load Station | 97 | 58 | 39 | **0** | 4 |
| Corona Treatment | 71 | 42 | 29 | 1 | - |
| Main Dial | 430 | 382 | 48 | 3 | - |
| Barrier Preheat Station 1 | 186 | 77 | 109 | 27 | - |
| Barrier Preheat Station 2 | 186 | 77 | 109 | 31 | - |
| Barrier Forming Station | 93 | 77 | 16 | 8 | - |
| Barrier Punch Station | 83 | 71 | 12 | 3 | - |
| Barrier Print Station | 89 | 77 | 12 | 3 | - |
| Bag Infeed Conveyor | 5 | 3 | 2 | 2 | - |
| Bag Load Robot | 117 | 60 | 57 | 7 | - |
| Ink Jet Station | 0 | 0 | 0 | **0** | - |
| Glue Station | 194 | 137 | 57 | 37 | - |
| Press and Cure Station | 138 | 104 | 34 | 7 | - |
| Bag Offload Robot | 54 | 24 | 30 | 2 | - |
| Bag Offload Conveyor | 1 | 0 | 1 | 7 | - |
| Label Applicator Conveyor | 0 | 0 | 0 | **0** | - |
| Insert & Drumhead Infeed System | 0 | 0 | 0 | **0** | - |
| Insert/Drumhead Load Robot | 0 | 0 | 0 | **0** | - |
| Glue Weight Drawer | 1 | 1 | 0 | **0** | 0 |
| Insert Assembly Station | 2 | 0 | 2 | **0** | - |
| Insert Corona/Glue Station | 0 | 0 | 0 | **0** | - |
| Insert Press Station | 0 | 0 | 0 | **0** | - |
| Drumhead Pre-placement Station | 78 | 42 | 36 | **0** | - |
| Drumhead Assembly Station | 1 | 1 | 0 | **0** | - |

## Parameters judged in this run

### Barrier Load Station (MC002-BarrierLoadStation)

- 97 candidate(s) considered -> 4 kept as genuine parameters.

| Parameter | Historian Tag | Unit | Type | Confidence | Why |
|---|---|---|---|---|---|
| Barrier Placement X-Axis Adjustment | `R2_BARRIER_ADJUST_X_AXIS` | mm | Real | 0.75 | operator-adjustable barrier placement offset on the load robot's X axis |
| Barrier Placement Y-Axis Adjustment | `R2_Barrier_Adjust_Y_Axis` | mm | Real | 0.75 | as above, Y axis |
| Barrier Present Sensor | `BARRIER_LOAD_BARRIER_PRESENT` | - | Boolean | 0.70 | description attributes it explicitly to BARRIER LOAD STATION |
| Barrier Vacuum On | `R2_BARRIER_VAC_ON` | - | Boolean | 0.60 | end-effector vacuum state for the barrier pick |

**Excluded from this station's 97 candidates, and why** - this is the interesting part, because the exclusions are all one of four recognisable kinds:

- **~35 `BARRIER_LOAD_DATA_*` shared-data-stream flags.** These read e.g. `HMI ANIMATION PREHEAT STATION 1 LOWER TEMP OK  MAIN DIAL PART DATA STREAM  BARRIER LOAD STATION`. They mention Barrier Load because that is the dial position the data is read at, but they report *other* stations' status (preheat temp, forming pressure, punch complete, vision complete). Exactly the failure mode the coverage caveat predicted, and the single largest group here.
- **~30 `R2_*` robot diagnostics and HMI controls** - fault, e-stop, teach-pendant enable, comms OK, battery low, screen navigation buttons. Real signals, but equipment diagnostics and UI plumbing rather than tracked process parameters.
- **~12 inter-station handshakes** (`*_PICK_REQ`, `*_PROCESS_DONE`, `*_INDEX_DIAL_REQ`) - sequencing traffic between stations, not measurements.
- **Representation duplicates** of the two axis adjustments (`_SCALE`, `_INT`, `_BINARY_CONV`, `_REAL_TO_DINT`, `_POS_NEG_SEL`) - the same physical signal in different numeric forms, so only the base tag is kept as the parameter.

Two tags were also rejected as belonging to a *different* station despite matching: `FORMING_LOAD_ANALOG_MAN_SETTINGS` and `PNC_LOAD_ANALOG_MAN_SETTINGS` matched only on the word 'LOAD' and belong to Barrier Forming and Press-and-Cure respectively.

### Glue Weight Drawer (MC002-GlueWeightDrawer)

- 1 candidate(s) considered -> 0 kept as genuine parameters.

_No genuine parameters. Its single candidate, `GLUE_SAMPLE_CYCLE_PB`, is an HMI pushbutton that starts a glue-weight sample cycle and whose own description attributes it to BAG GLUE STATION - an operator command belonging to another station, not a tracked parameter of this one._

## Known limitations of this run

- **Barrier Preheat Station 1 and 2 are indistinguishable** by name matching: they return an identical 186 candidates each, because the only thing separating their names is a trailing digit that the keyword vocabulary does not carry. Their 27 and 31 existing workbook parameters were separated by some earlier means and should not be assumed reproducible from this export alone.
- **Main Dial over-matches at 430 candidates** for the same reason the data-stream flags above were excluded: the phrase 'MAIN DIAL PART DATA STREAM' appears in roughly 30% of all tags on this machine. 'Main' and 'dial' cannot be treated as export scaffolding either, since they are also the station's only identity - so this one genuinely needs either a judging pass with a larger budget or an engineer-supplied rule.
- **`Drumhead Pre-placement Station` returns 78 candidates but should return ~0.** Its word 'placement' stems to 'place', which collides with the machine's PICK-N-PLACE vocabulary. A stemming false positive, not real coverage.
