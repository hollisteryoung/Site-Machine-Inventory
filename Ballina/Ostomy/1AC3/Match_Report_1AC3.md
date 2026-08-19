# Tag Matching Report - Line 1AC3

Auto Coiner (MC002). This summarizes which historian tags were kept as genuine process parameters for each station and why. Parameters found only by a weak match strategy, or whose unit was inferred rather than stated, are the ones most worth a second look from someone who knows the physical machine.

## Summary

- 25 station(s) processed against a `rslogix_csv` export of 1430 tags.
- 1689 candidate tag(s) considered (excluding tags already recorded in the workbook from earlier runs) -> **116 kept** as genuine parameters (7% of candidates).
- The workbook now holds **259 parameters across 15 of the 25 stations** (was 143 across 14).
- **12 kept parameters have a unit stated literally in the source** (descriptions containing "(F)" or "(C)"), so those are not naming-convention guesses. The rest are inferred.
- 1196 of the candidates were already wired to an operator HMI screen and 493 exist only in the controller; of the parameters actually kept, 35 are HMI-wired and 81 are controller-only. That second group is invisible to the traditional approach of picking a tag off an HMI.

## Tag export conventions this run assumed

Discovered by the profiling step and cached to `Tag_Source_Profile.json`. If a whole line matches badly, suspect these first - and correct that file rather than the code, since every later run reads it back.

- Station identity read from: description, tag_path. This export's tag names are largely opaque device codes, but its DESCRIPTION column names the station in plain English for 97% of tags.
- Station code style: *mixed*. No numeric station codes - this machine's stations are named, not numbered.
- 16 export-scaffolding token(s) excluded from keyword matching: `hmi`, `animation`, `push`, `button`, `screen`, `part`, `data`, `stream`, `cell`, `machine`, `piece`, `array`, `display`, `msg`, `comms`, `ethernet`.
- 10 opaque device code(s) resolved to plain English **from the export itself, with no hand-written legend file**: `DRV01` = MAIN DIAL SERVO, `DRV02` = BARRIER INFEED MAGAZINE SERVO, `DRV03` = BARRIER INFEED ELEVATOR SERVO, `DRV04` = BARRIER PRESS-N-CURE STATION SERVO, `DRV05` = BARRIER PICK-N-PLACE/CORONA TREAT SERVO, `DRV06` = BARRIER PICK-N-PLACE/CORONA TREAT STEPPER, `DRV08` = BAG GRIPPER STEPPER, `R1` = BAG LOAD ROBOT, `R2` = BARRIER LOAD/BAG OFFLOAD ROBOT, `VISION` = VISION INSPECTION STATION.
- Three shared I/O modules (`MAN01`, `MAN02`, `MAN03`) were deliberately kept OUT of that legend: each one's description names several stations at once, so admitting them would pull a single tag family into five different stations.

**Coverage caveat:** This is the controller export for the 1-PIECE BAG configuration only (file: Rigid_Film_Conv_1PC_PN3_AC3_R18). The machine's insert/drumhead product configuration is documented in the manual but has NO presence in this export: 'INK'/'JET'/'LABEL'/'APPLICAT' return zero hits across all 1430 tags, and 'INSERT'/'DRUM' return only incidental ones. So Ink Jet Station, Label Applicator Conveyor, Insert & Drumhead Infeed System, Insert/Drumhead Load Robot, Insert Assembly Station, Insert Corona/Glue Station, Insert Press Station, Drumhead Pre-placement Station and Drumhead Assembly Station are expected to yield nothing here - that is a genuine scope limit of this file, not a matching failure, and no tuning will fill them in. A separate controller export would be needed. Second caveat: the phrase 'MAIN DIAL PART DATA STREAM' is a shared data-structure wrapper appearing in ~30% of tags across many different stations, so tags mentioning Main Dial are frequently owned by another station and must be judged on which station the description actually attributes them to. Three shared I/O modules (MAN01, MAN02, MAN03) were deliberately excluded from the code legend because each one's description names several stations at once and would otherwise pull a whole tag family into all of them.

## Results by station

| Station | Candidates | Kept this run | Total in workbook |
|---|---|---|---|
| Barrier Infeed System | 68 | 8 | 9 |
| Barrier Load Station | 91 | 0 | 4 |
| Corona Treatment | 70 | 7 | 8 |
| Main Dial | 427 | 2 | 5 |
| Barrier Preheat Station 1 | 128 | 34 | 61 |
| Barrier Preheat Station 2 | 128 | 32 | 63 |
| Barrier Forming Station | 85 | 4 | 12 |
| Barrier Punch Station | 80 | 2 | 5 |
| Barrier Print Station | 85 | 0 | 3 |
| Bag Infeed Conveyor | 5 | 0 | 2 |
| Bag Load Robot | 105 | 2 | 9 |
| Ink Jet Station | 0 | 0 | **0** |
| Glue Station | 157 | 16 | 53 |
| Press and Cure Station | 131 | 9 | 16 |
| Bag Offload Robot | 49 | 0 | 2 |
| Bag Offload Conveyor | 1 | 0 | 7 |
| Label Applicator Conveyor | 0 | 0 | **0** |
| Insert & Drumhead Infeed System | 0 | 0 | **0** |
| Insert/Drumhead Load Robot | 0 | 0 | **0** |
| Glue Weight Drawer | 1 | 0 | **0** |
| Insert Assembly Station | 2 | 0 | **0** |
| Insert Corona/Glue Station | 0 | 0 | **0** |
| Insert Press Station | 0 | 0 | **0** |
| Drumhead Pre-placement Station | 75 | 0 | **0** |
| Drumhead Assembly Station | 1 | 0 | **0** |

## Parameters kept, by station

### Barrier Infeed System

68 candidate(s) -> 8 kept.

| Parameter | Historian Tag | Unit | Type | HMI | Found via |
|---|---|---|---|---|---|
| Elevator is in position and ready for processing | `ELEVATOR_IN_POSITION` | - | Boolean | no | keyword_all |
| Elevator is out of the and clear of the magazine | `ELEVATOR_OUT_OF_MAG_POS` | - | Boolean | no | keyword_all |
| Parts not present in barrier tower sensor | `ELEVATOR_PART_NOT_PRESENT` | - | Boolean | no | keyword_all |
| The elevator is at the barrier pick position | `ELEVATOR_PICK_POS` | - | Boolean | no | keyword_all |
| Vertical position check sensor part detected | `ELEVATOR_POS_CHK` | - | Boolean | no | keyword_all |
| The elevator is at the top programmed position | `ELEVATOR_TOP_POS` | - | Boolean | no | keyword_all |
| Magazine is in position and ready for processing | `MAGAZINE_IN_POSITION` | - | Boolean | no | keyword_all |
| Tube check sensor | `MAGAZINE_TUBE_CHK` | - | Boolean | yes | keyword_all |

### Corona Treatment

70 candidate(s) -> 7 kept.

| Parameter | Historian Tag | Unit | Type | HMI | Found via |
|---|---|---|---|---|---|
| Base drive home sensor | `PNP_BASE_HOME_SENSOR` | - | Boolean | yes | keyword |
| Pick-n-place base drive is at the corona treat position | `PNP_CORONA_POS` | - | Boolean | no | keyword |
| Base drive is in position and ready for processing station | `PNP_IN_POSITION` | - | Boolean | no | keyword |
| Pick-n-place base drive is at the light table position | `PNP_LIGHT_TABLE_POS` | - | Boolean | no | keyword |
| Pick-n-place base drive is at the magazine position | `PNP_MAGAZINE_POS` | - | Boolean | no | keyword |
| Pick-n-place base drive is at the parked position | `PNP_PARK_POS` | - | Boolean | no | keyword |
| Pick head drive home sensor | `PNP_PICK_HEAD_HOME_SENSOR` | - | Boolean | yes | keyword |

### Main Dial

427 candidate(s) -> 2 kept.

| Parameter | Historian Tag | Unit | Type | HMI | Found via |
|---|---|---|---|---|---|
| Home sensor | `MAIN_DIAL_HOME_SENSOR` | - | Boolean | yes | keyword |
| Is in position and ready for processing | `MAIN_DIAL_IN_POSITION` | - | Boolean | no | keyword |

### Barrier Preheat Station 1

128 candidate(s) -> 34 kept.

| Parameter | Historian Tag | Unit | Type | HMI | Found via |
|---|---|---|---|---|---|
| Lower tool max allowable temperature hmi display | `PREHEAT1_LOW_TEMP_MAX` | F *(stated)* | Real | yes | keyword_all |
| Lower tool min allowable temperature hmi display | `PREHEAT1_LOW_TEMP_MIN` | F *(stated)* | Real | yes | keyword_all |
| Lower tool temperature within tolerance | `PREHEAT1_LOW_TEMP_OK` | - | Boolean | no | keyword_all |
| Lower tool temperature control pid | `PREHEAT1_LOW_TOOL_PID` | C *(stated)* | Real | no | keyword_all |
| Lower tool pid dynamic bias variable large part family | `PREHEAT1_LOW_TOOL_PID_DYN_BIAS_LARGE` | - | Real | no | keyword_all |
| Lower tool pid dynamic bias variable large soft-n-flexible part family | `PREHEAT1_LOW_TOOL_PID_DYN_BIAS_LG_SNF` | - | Real | no | keyword_all |
| Lower tool pid dynamic bias variable medium part family | `PREHEAT1_LOW_TOOL_PID_DYN_BIAS_MEDIUM` | - | Real | no | keyword_all |
| Lower tool pid dynamic bias variable small part family | `PREHEAT1_LOW_TOOL_PID_DYN_BIAS_SMALL` | - | Real | no | keyword_all |
| Lower tool pid dynamic bias variable small soft-n-flexible part family | `PREHEAT1_LOW_TOOL_PID_DYN_BIAS_SM_SNF` | - | Real | no | keyword_all |
| Lower tool pid process variable | `PREHEAT1_LOW_TOOL_PID_PV` | C | Real | yes | keyword_all |
| Lower tool temperature pid set point | `PREHEAT1_LOW_TOOL_PID_SP` | C | Real | yes | keyword_all |
| Lower tool pid static bias variable large part family | `PREHEAT1_LOW_TOOL_PID_STATIC_BIAS_LARGE` | - | Real | no | keyword_all |
| Lower tool pid static bias variable medium part family | `PREHEAT1_LOW_TOOL_PID_STATIC_BIAS_MEDIUM` | - | Real | no | keyword_all |
| Lower tool pid static bias variable small part family | `PREHEAT1_LOW_TOOL_PID_STATIC_BIAS_SMALL` | - | Real | no | keyword_all |
| Lower tool pid static bias variable large soft-n-flexible part family | `PREHEAT1_LOW_TOOL_PID_ST_BIAS_LG_SNF` | - | Real | no | keyword_all |
| Lower tool pid static bias variable small soft-n-flexible part family | `PREHEAT1_LOW_TOOL_PID_ST_BIAS_SM_SNF` | - | Real | no | keyword_all |
| Lower tool output control variable | `PREHEAT1_LOW_TOOL_TEMP_PID_CV` | % | Real | no | keyword_all |
| Upper tool max allowable temperature hmi display | `PREHEAT1_UP_TEMP_MAX` | F *(stated)* | Real | yes | keyword_all |
| Upper tool min allowable temperature hmi display | `PREHEAT1_UP_TEMP_MIN` | F *(stated)* | Real | yes | keyword_all |
| Upper tool temperature within tolerance | `PREHEAT1_UP_TEMP_OK` | - | Boolean | no | keyword_all |
| Upper tool temperature control pid | `PREHEAT1_UP_TOOL_PID` | C *(stated)* | Real | no | keyword_all |
| Upper tool pid dynamic bias variable large part family | `PREHEAT1_UP_TOOL_PID_DYN_BIAS_LARGE` | - | Real | no | keyword_all |
| Upper tool pid dynamic bias variable large soft-n-flexible part family | `PREHEAT1_UP_TOOL_PID_DYN_BIAS_LG_SNF` | - | Real | no | keyword_all |
| Upper tool pid dynamic bias variable medium part family | `PREHEAT1_UP_TOOL_PID_DYN_BIAS_MEDIUM` | - | Real | no | keyword_all |
| Upper tool pid dynamic bias variable small part family | `PREHEAT1_UP_TOOL_PID_DYN_BIAS_SMALL` | - | Real | no | keyword_all |
| Upper tool pid dynamic bias variable small soft-n-flexible part family | `PREHEAT1_UP_TOOL_PID_DYN_BIAS_SM_SNF` | - | Real | no | keyword_all |
| Upper tool pid process variable | `PREHEAT1_UP_TOOL_PID_PV` | C | Real | yes | keyword_all |
| Upper tool temperature pid set point | `PREHEAT1_UP_TOOL_PID_SP` | C | Real | yes | keyword_all |
| Upper tool pid static bias variable large part family | `PREHEAT1_UP_TOOL_PID_STATIC_BIAS_LARGE` | - | Real | no | keyword_all |
| Upper tool pid static bias variable medium part family | `PREHEAT1_UP_TOOL_PID_STATIC_BIAS_MEDIUM` | - | Real | no | keyword_all |
| Upper tool pid static bias variable small part family | `PREHEAT1_UP_TOOL_PID_STATIC_BIAS_SMALL` | - | Real | no | keyword_all |
| Upper tool pid static bias variable large soft-n-flexible part family | `PREHEAT1_UP_TOOL_PID_ST_BIAS_LG_SNF` | - | Real | no | keyword_all |
| Upper tool pid static bias variable small soft-n-flexible part family | `PREHEAT1_UP_TOOL_PID_ST_BIAS_SM_SNF` | - | Real | no | keyword_all |
| Upper tool output control variable | `PREHEAT1_UP_TOOL_TEMP_PID_CV` | % | Real | no | keyword_all |

### Barrier Preheat Station 2

128 candidate(s) -> 32 kept.

| Parameter | Historian Tag | Unit | Type | HMI | Found via |
|---|---|---|---|---|---|
| Lower tool max allowable temperature hmi display | `PREHEAT2_LOW_TEMP_MAX` | F *(stated)* | Real | yes | keyword_all |
| Lower tool min allowable temperature hmi display | `PREHEAT2_LOW_TEMP_MIN` | F *(stated)* | Real | yes | keyword_all |
| Lower tool temperature control pid | `PREHEAT2_LOW_TOOL_PID` | C *(stated)* | Real | no | keyword_all |
| Lower tool pid dynamic bias variable large part family | `PREHEAT2_LOW_TOOL_PID_DYN_BIAS_LARGE` | - | Real | no | keyword_all |
| Lower tool pid dynamic bias variable large soft-n-flexible part family | `PREHEAT2_LOW_TOOL_PID_DYN_BIAS_LG_SNF` | - | Real | no | keyword_all |
| Lower tool pid dynamic bias variable medium part family | `PREHEAT2_LOW_TOOL_PID_DYN_BIAS_MEDIUM` | - | Real | no | keyword_all |
| Lower tool pid dynamic bias variable small part family | `PREHEAT2_LOW_TOOL_PID_DYN_BIAS_SMALL` | - | Real | no | keyword_all |
| Lower tool pid dynamic bias variable small soft-n-flexible part family | `PREHEAT2_LOW_TOOL_PID_DYN_BIAS_SM_SNF` | - | Real | no | keyword_all |
| Lower tool pid process variable | `PREHEAT2_LOW_TOOL_PID_PV` | C | Real | yes | keyword_all |
| Lower tool temperature pid set point | `PREHEAT2_LOW_TOOL_PID_SP` | C | Real | yes | keyword_all |
| Lower tool pid static bias variable large part family | `PREHEAT2_LOW_TOOL_PID_STATIC_BIAS_LARGE` | - | Real | no | keyword_all |
| Lower tool pid static bias variable medium part family | `PREHEAT2_LOW_TOOL_PID_STATIC_BIAS_MEDIUM` | - | Real | no | keyword_all |
| Lower tool pid static bias variable small part family | `PREHEAT2_LOW_TOOL_PID_STATIC_BIAS_SMALL` | - | Real | no | keyword_all |
| Lower tool pid static bias variable large soft-n-flexible part family | `PREHEAT2_LOW_TOOL_PID_ST_BIAS_LG_SNF` | - | Real | no | keyword_all |
| Lower tool pid static bias variable small soft-n-flexible part family | `PREHEAT2_LOW_TOOL_PID_ST_BIAS_SM_SNF` | - | Real | no | keyword_all |
| Lower tool output control variable | `PREHEAT2_LOW_TOOL_TEMP_PID_CV` | % | Real | no | keyword_all |
| Upper tool max allowable temperature hmi display | `PREHEAT2_UP_TEMP_MAX` | F *(stated)* | Real | yes | keyword_all |
| Upper tool min allowable temperature hmi display | `PREHEAT2_UP_TEMP_MIN` | F *(stated)* | Real | yes | keyword_all |
| Upper tool temperature control pid | `PREHEAT2_UP_TOOL_PID` | C *(stated)* | Real | no | keyword_all |
| Upper tool pid dynamic bias variable large part family | `PREHEAT2_UP_TOOL_PID_DYN_BIAS_LARGE` | - | Real | no | keyword_all |
| Upper tool pid dynamic bias variable large soft-n-flexible part family | `PREHEAT2_UP_TOOL_PID_DYN_BIAS_LG_SNF` | - | Real | no | keyword_all |
| Upper tool pid dynamic bias variable medium part family | `PREHEAT2_UP_TOOL_PID_DYN_BIAS_MEDIUM` | - | Real | no | keyword_all |
| Upper tool pid dynamic bias variable small part family | `PREHEAT2_UP_TOOL_PID_DYN_BIAS_SMALL` | - | Real | no | keyword_all |
| Upper tool pid dynamic bias variable small soft-n-flexible part family | `PREHEAT2_UP_TOOL_PID_DYN_BIAS_SM_SNF` | - | Real | no | keyword_all |
| Upper tool pid process variable | `PREHEAT2_UP_TOOL_PID_PV` | C | Real | yes | keyword_all |
| Upper tool temperature pid set point | `PREHEAT2_UP_TOOL_PID_SP` | C | Real | yes | keyword_all |
| Upper tool pid static bias variable large part family | `PREHEAT2_UP_TOOL_PID_STATIC_BIAS_LARGE` | - | Real | no | keyword_all |
| Upper tool pid static bias variable medium part family | `PREHEAT2_UP_TOOL_PID_STATIC_BIAS_MEDIUM` | - | Real | no | keyword_all |
| Upper tool pid static bias variable small part family | `PREHEAT2_UP_TOOL_PID_STATIC_BIAS_SMALL` | - | Real | no | keyword_all |
| Upper tool pid static bias variable large soft-n-flexible part family | `PREHEAT2_UP_TOOL_PID_ST_BIAS_LG_SNF` | - | Real | no | keyword_all |
| Upper tool pid static bias variable small soft-n-flexible part family | `PREHEAT2_UP_TOOL_PID_ST_BIAS_SM_SNF` | - | Real | no | keyword_all |
| Upper tool output control variable | `PREHEAT2_UP_TOOL_TEMP_PID_CV` | % | Real | no | keyword_all |

### Barrier Forming Station

85 candidate(s) -> 4 kept.

| Parameter | Historian Tag | Unit | Type | HMI | Found via |
|---|---|---|---|---|---|
| Barrier release from form tooling blow start time forming station | `FORMING_BARRIER_RELEASE_BLOW_START_TIME` | s | Real | no | keyword |
| Max allowable pressure (psi) hmi display | `FORMING_PRESSURE_MAX` | PSI | Real | yes | keyword |
| Min allowable pressure (psi) hmi display | `FORMING_PRESSURE_MIN` | PSI | Real | yes | keyword |
| Pneumatic scaling paramters | `FORMING_PRESSURE_SCALING_PARAM` | PSI | Real | no | keyword |

### Barrier Punch Station

80 candidate(s) -> 2 kept.

| Parameter | Historian Tag | Unit | Type | HMI | Found via |
|---|---|---|---|---|---|
| Punch_moon_blow_time | `PUNCH_MOON_BLOW_TIME` | s | Real | no | keyword |
| Punch pressure ok | `PUNCH_PRESSURE_OK` | - | Boolean | yes | keyword |

### Bag Load Robot

105 candidate(s) -> 2 kept.

| Parameter | Historian Tag | Unit | Type | HMI | Found via |
|---|---|---|---|---|---|
| Bag gripper is in picked position | `R1_GRIPPER_PICK_POS` | - | Boolean | no | legend_code |
| Bag gripper is in released position | `R1_GRIPPER_REL_POS` | - | Boolean | no | legend_code |

### Glue Station

157 candidate(s) -> 16 kept.

| Parameter | Historian Tag | Unit | Type | HMI | Found via |
|---|---|---|---|---|---|
| Axis are at bag presence check position | `GLUE_AT_PART_CHK_POS` | - | Boolean | no | keyword_all |
| Axis are at glue sample position | `GLUE_AT_SAMPLE_POS` | - | Boolean | no | keyword_all |
| Bag present sensor | `GLUE_BAG_PRESENT` | - | Boolean | yes | keyword_all |
| Glue melter input side pressure (psi) acceptable | `GLUE_IN_PRESSURE_OK` | - | Boolean | no | keyword_all |
| Pneumatic scaling paramters | `GLUE_IN_PRESSURE_SCALING_PARAM` | PSI | Real | no | keyword_all |
| Glue_melt_glow_glue_present | `GLUE_MELT_GLOW_GLUE_PRESENT` | - | Boolean | yes | keyword_all |
| Glue melter level ok | `GLUE_MELT_LEVEL_OK` | - | Boolean | yes | keyword_all |
| Output side glue pressure (psi) control pid | `GLUE_OUT_PRESSURE_PID` | PSI | Real | no | keyword_all |
| Output side glue pressure control variable | `GLUE_OUT_PRESSURE_PID_CV` | % | Real | no | keyword_all |
| Output side glue pressure process variable | `GLUE_OUT_PRESSURE_PID_PV` | PSI | Real | yes | keyword_all |
| Output side glue pressure pid set point | `GLUE_OUT_PRESSURE_PID_SP` | PSI | Real | yes | keyword_all |
| Output side glue pressure (psi) at post process is within tolerance | `GLUE_OUT_PRESSURE_POST_OK` | - | Boolean | no | keyword_all |
| Output side glue pressure (psi) at pre process is within tolerance | `GLUE_OUT_PRESSURE_PRE_OK` | - | Boolean | no | keyword_all |
| Glue present sensor | `GLUE_TEMP_PRESENT` | - | Boolean | yes | keyword_all |
| X-axis drive home sensor | `GLUE_X_HOME_SENSOR` | - | Boolean | yes | keyword_all |
| Y-axis drive home sensor | `GLUE_Y_HOME_SENSOR` | - | Boolean | yes | keyword_all |

### Press and Cure Station

131 candidate(s) -> 9 kept.

| Parameter | Historian Tag | Unit | Type | HMI | Found via |
|---|---|---|---|---|---|
| Home sensor barrier | `PNC_HOME_SENSOR` | - | Boolean | yes | keyword |
| Press head is in position and ready for processing barrier | `PNC_IN_POSITION` | - | Boolean | no | keyword |
| Pick head rotation barrier | `PNC_PICK_ROT_POS` | - | Boolean | yes | keyword |
| Max allowable pressure (psi) barrier hmi display | `PNC_PRESSURE_MAX` | PSI | Real | yes | keyword |
| Min allowable pressure (psi) barrier hmi display | `PNC_PRESSURE_MIN` | PSI | Real | yes | keyword |
| Pressure within tolerance barrier | `PNC_PRESSURE_OK` | - | Boolean | no | keyword |
| Pneumatic scaling paramters barrier | `PNC_PRESSURE_SCALING_PARAM` | PSI | Real | no | keyword |
| Press head is rotationally in the first half of rotation pick | `PNC_SIDE_1_AT_CURE_POS` | - | Boolean | no | keyword |
| Press head is rotationally in the second half of rotation pick | `PNC_SIDE_2_AT_CURE_POS` | - | Boolean | no | keyword |

## How candidates were rejected

Roughly 93% of candidates were rejected, in four recognisable families. Naming them matters, because each is a pattern a reviewer can check rather than a black-box verdict:

- **Shared data-stream flags (723 candidates, the single largest group).** Tags reading e.g. `HMI ANIMATION PREHEAT STATION 1 LOWER TEMP OK  MAIN DIAL PART DATA STREAM  BARRIER LOAD STATION`. They name a station because that is the dial position the data is read at, but they report *another* station's status. Rejected wherever the description attributed the tag elsewhere.
- **Device diagnostics and drive status (116).** Faults, e-stops, comms OK, battery low, homing and indexing state. Real signals, but equipment health rather than tracked process parameters.
- **Operator controls and HMI plumbing (206).** Pushbuttons, screen navigation, visibility flags. Some escape a `_PB` suffix rule, so the description is checked too - `GLUE_X_Y_POS` looks like a position but reads 'HMI PUSH BUTTON SERIES FOR X-Y POSITION CONTROL'.
- **Inter-station handshakes (100) and numeric representation duplicates (54).** Sequencing traffic between stations, and the same signal re-expressed via `_SCALE`, `_INT`, `_BINARY_CONV`, `_REAL_TO_DINT` - only the base tag is kept.

## Notes and limitations

- **Barrier Preheat 1 and 2 were separated at the judging stage, not the matching stage.** The matcher returned an identical 186 candidates for both, because the only thing distinguishing their names is a trailing digit that the keyword vocabulary drops. Their tags do keep it (`PREHEAT1_*` vs `PREHEAT2_*`), so requiring each tag's own description to name its station resolved them cleanly - 34 and 32 parameters respectively, with no cross-contamination.
- **Main Dial over-matched at 427 candidates and yielded only 2.** The phrase 'MAIN DIAL PART DATA STREAM' appears in roughly 30% of all tags on this machine. 'Main' and 'dial' cannot be excluded as scaffolding either, since they are also the station's only identity. Its real parameters are likely under-represented and it deserves a dedicated look with an engineer.
- **`Drumhead Pre-placement Station` drew 75 candidates and correctly kept none.** Its word 'placement' stems to 'place', colliding with the machine's PICK-N-PLACE vocabulary - a stemming false positive, not real coverage.
- **Ten stations hold no parameters**, nine of them because this export does not cover them at all (see the coverage caveat), plus Glue Weight Drawer, whose single candidate is a glue-weight sample-cycle pushbutton belonging to Bag Glue Station.
- **Units are written to the workbook in plain form** (`F`, `PSI`) to match the 4,000+ rows already there. `LineProcess.py` would instead append "(unverified)" to inferred units; introducing that convention for a subset of rows would break anyone filtering on the column, so the stated-vs-inferred distinction lives in this report instead. Worth settling before the next line is run.
