# Tag Matching Report - Line NGP2

This summarizes, for every station found on this line, which historian tags were kept as genuine process parameters and why. Parameters marked with a low match strategy (keyword) or below 0.5 confidence are the ones most worth a second look from someone who knows the physical machine.

## Summary

- 66 station(s) processed.
- 1864 candidate tag(s) considered across all stations -> 991 kept as genuine parameters (53% of candidates).
- 991 of this line's 76259 total historian tags (1.3%) ended up mapped to a genuine parameter - this is the actual coverage of the raw tag export, as opposed to the conversion rate above, which only measures the pre-filtered candidate pool.
- 34 kept parameter(s) below 0.5 confidence overall - worth a second look.
- 9 station(s) with no genuine parameters found at all: Remove Cap and Inflate Sleeve (1064), Foam Generator (1076), Foam Dosing (1080), Re-assemble Cap (1090), Check Cap Presence (1095), Top Label Presence Check (2042), Thumb Hole Punching (2053), Waste Grid Detection (2068), Slug Detection (2087).

## Notes on this run

- **Source document**: `MyQUMAS - Repository QPROD.pdf` (75CLR00674_Att1) is a genuine engineering-grade Manufacturing Instruction - unlike HF11/BFX's operator MI, it documents every station by its literal numeric PLC identifier (St.2057, St.1135, etc.), which is what makes numeric matching effective here.
- **Tag source**: tags.json is a genuine raw Ignition/Kepware export (76,259 atomic tags, includes the _System/_Statistics provider scaffolding), not a partial/curated subset.
- **Two matching bugs were found and fixed in LineProcess.py while processing this line** (both now live in the shared pipeline code, not just this run):
  1. *Numeric suffix matching*: this historian's tags truncate the station number's leading digit (station 2057 -> tag St057), which the original numeric strategy's exact-match comparison never matched at all. Fixed by accepting a 3-digit truncated suffix match (tagged numeric_suffix, distinct from an exact numeric match).
  2. *Generic-word flooding*: the keyword strategy matched substrings anywhere in a tag's full path, so a station name sharing a word with the tag tree's own structural scaffolding (e.g. "Application", the PLC program's root folder) or with a common word appearing inside unrelated longer identifiers ("pack" inside "PackagingRunMode") flooded that station with most of the ~76k-tag tree. Fixed with corpus-frequency-based generic-word exclusion (_tag_tree_generic_words, the JSON-tree equivalent of the existing WinCC-path _line_generic_words) plus switching substring containment to word-boundary matching.
- **Known residual limitation**: the numeric-suffix fix can still coincidentally collide when a 1xxx and 2xxx station share the same last 3 digits (e.g. station 1032 and station 2032 both truncate to "032"). This was checked for across this station list - the only such collision is 1032/2032, and the wrongly-attributed tags (Print Mark-related) have been excluded from 1032's results below with a note; they are correctly kept under 2032.
- **1xxx stations are not actually missing from this export - they're indexed by axis/fault code, not station number, so station-based matching can't reach them**: stations in the 1xxx range (catheter feeding/alignment/foam dosing) return almost no station-specific tags here beyond generic per-station fault/counter bookkeeping, while the rich, detailed setpoints and measurements live almost entirely under the 2xxx range (web/print/seal handling). Digging into the tag tree beyond what matching could reach shows this data does exist for the 1xxx domain, just under namespaces with no station-number correlation at all:
  - `Flt_x_` - 3,000 entries (`Flt_184_`, `Flt_2910_`, `Flt_2945_`...) - a separate, much larger global fault/alarm-code dictionary than the small per-station `Flt[stationID]` array matching used; its numbers fall well outside the 1001-2180 station-ID range.
  - `AxMsg_x_` / `AxFbMsg_x_` - 53 entries each, named by servo axis index (`AxMsg_38_`, `AxFbMsg_19_`), confirming this machine has roughly 53 servo axes - but indexed by axis number, not station number.
  - `sASi__x_y_` - 320 entries in a 2D-indexed matrix (`sASi__9_23_`), consistent with AS-Interface safety-bus I/O diagnostics.

  None of these can be attributed to a specific station without an axis-to-station mapping (e.g. "axis 12 = the front infeed servo on Feeding Catheter Front") - the same missing-legend problem encountered on HF11's PLC module codes, just for axis numbers instead of module codes. This is a genuine gap in what tag-name matching alone can resolve, not evidence that the file itself is partial or incomplete.
- **Excluded uniformly as internal diagnostics** (not process parameters): per-station fault bits and acknowledgement sequencing (Flt, FaultAckEnable, Flt_notACK, WaitingFor_FaultAckEnable), the interlock dependency matrix (SR_ReleaseX_DependsOnY), the reject-reason lookup view (SrView_RejectReason), and an internal counter-index mapping table (g_SLCInputCounterMap) - these repeat identically for every station and describe fault-state machinery, not a tracked physical parameter.
- **Machine: Secondary Packaging Machine 2 (SP2)** is documented in the same manual (cartons, F3/F4/F202 robots, print-and-apply) but this tags.json contains zero SP2-referencing tags - it appears to be scoped to the NGP2 controller only. SP2 needs its own historian export before it can be matched.

## Machine: Next Generation Pack Machine 2 (NGP2)

### Main Drive (1001)

- 6 candidate tag(s) considered -> 1 kept as genuine parameters (17%).
- Kept tags found by: 1 via *direct_id* (the station's raw ID string appeared literally in the tag's path/name - a strong signal).
- 1 kept parameter(s) below 0.5 confidence - flagged with warning below.

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| OEE Production Counter (low confidence) | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.SLC_OEE_COUNTER_MAPPING.g_SLC_Packaging_OEE_Counters[x].g_SLC_Packaging_OEE_Counters[1001]` | count | 0.40 | direct_id |

### Feeding Catheter Rear (1005)

- 6 candidate tag(s) considered -> 1 kept as genuine parameters (17%).
- Kept tags found by: 1 via *direct_id* (the station's raw ID string appeared literally in the tag's path/name - a strong signal).
- 1 kept parameter(s) below 0.5 confidence - flagged with warning below.

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| OEE Production Counter (low confidence) | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.SLC_OEE_COUNTER_MAPPING.g_SLC_Packaging_OEE_Counters[x].g_SLC_Packaging_OEE_Counters[1005]` | count | 0.40 | direct_id |

### Load Catheter Rear (1010)

- 8 candidate tag(s) considered -> 1 kept as genuine parameters (12%).
- Kept tags found by: 1 via *direct_id* (the station's raw ID string appeared literally in the tag's path/name - a strong signal).
- 1 kept parameter(s) below 0.5 confidence - flagged with warning below.

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| OEE Production Counter (low confidence) | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.SLC_OEE_COUNTER_MAPPING.g_SLC_Packaging_OEE_Counters[x].g_SLC_Packaging_OEE_Counters[1010]` | count | 0.40 | direct_id |

### Align Catheter and Cap Rear (1012)

- 8 candidate tag(s) considered -> 1 kept as genuine parameters (12%).
- Kept tags found by: 1 via *direct_id* (the station's raw ID string appeared literally in the tag's path/name - a strong signal).
- 1 kept parameter(s) below 0.5 confidence - flagged with warning below.

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| OEE Production Counter (low confidence) | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.SLC_OEE_COUNTER_MAPPING.g_SLC_Packaging_OEE_Counters[x].g_SLC_Packaging_OEE_Counters[1012]` | count | 0.40 | direct_id |

### Feeding Catheter Front (1025)

- 8 candidate tag(s) considered -> 1 kept as genuine parameters (12%).
- Kept tags found by: 1 via *direct_id* (the station's raw ID string appeared literally in the tag's path/name - a strong signal).
- 1 kept parameter(s) below 0.5 confidence - flagged with warning below.

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| OEE Production Counter (low confidence) | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.SLC_OEE_COUNTER_MAPPING.g_SLC_Packaging_OEE_Counters[x].g_SLC_Packaging_OEE_Counters[1025]` | count | 0.40 | direct_id |

### Load Catheter Front (1030)

- 8 candidate tag(s) considered -> 1 kept as genuine parameters (12%).
- Kept tags found by: 1 via *direct_id* (the station's raw ID string appeared literally in the tag's path/name - a strong signal).
- 1 kept parameter(s) below 0.5 confidence - flagged with warning below.

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| OEE Production Counter (low confidence) | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.SLC_OEE_COUNTER_MAPPING.g_SLC_Packaging_OEE_Counters[x].g_SLC_Packaging_OEE_Counters[1030]` | count | 0.40 | direct_id |

### Align Catheter and Cap Front (1032)

- 13 candidate tag(s) considered -> 1 kept as genuine parameters (8%).
- Kept tags found by: 1 via *direct_id* (the station's raw ID string appeared literally in the tag's path/name - a strong signal).
- 1 kept parameter(s) below 0.5 confidence - flagged with warning below.
- 5 candidate(s) excluded: Print Mark-related tags (St032_...) that numerically collide with station 2032 but semantically belong there, not here - see notes above.

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| OEE Production Counter (low confidence) | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.SLC_OEE_COUNTER_MAPPING.g_SLC_Packaging_OEE_Counters[x].g_SLC_Packaging_OEE_Counters[1032]` | count | 0.40 | direct_id |

### Positioning Tip (1052)

- 6 candidate tag(s) considered -> 1 kept as genuine parameters (17%).
- Kept tags found by: 1 via *direct_id* (the station's raw ID string appeared literally in the tag's path/name - a strong signal).
- 1 kept parameter(s) below 0.5 confidence - flagged with warning below.

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| OEE Production Counter (low confidence) | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.SLC_OEE_COUNTER_MAPPING.g_SLC_Packaging_OEE_Counters[x].g_SLC_Packaging_OEE_Counters[1052]` | count | 0.40 | direct_id |

### Remove Cap and Inflate Sleeve (1064)

- 4 candidate tag(s) considered -> 0 kept as genuine parameters (0%).

_No genuine parameters found among this station's candidates._

### Foam Generator (1076)

- 4 candidate tag(s) considered -> 0 kept as genuine parameters (0%).

_No genuine parameters found among this station's candidates._

### Foam Dosing (1080)

- 4 candidate tag(s) considered -> 0 kept as genuine parameters (0%).

_No genuine parameters found among this station's candidates._

### Re-assemble Cap (1090)

- 4 candidate tag(s) considered -> 0 kept as genuine parameters (0%).

_No genuine parameters found among this station's candidates._

### Check Cap Presence (1095)

- 4 candidate tag(s) considered -> 0 kept as genuine parameters (0%).

_No genuine parameters found among this station's candidates._

### Pick and Place Catheter (1100)

- 6 candidate tag(s) considered -> 2 kept as genuine parameters (33%).
- Kept tags found by: 2 via *direct_id* (the station's raw ID string appeared literally in the tag's path/name - a strong signal).
- 2 kept parameter(s) below 0.5 confidence - flagged with warning below.

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| Reject Count (station entry, per lane) (low confidence) | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiRO.RejectStatistic_Entry_Lane[x].RejectStatistic_Entry_Lane[1][10][0]` | count | 0.45 | direct_id |
| Station Cycle Counter (per lane) (low confidence) | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC4.CounterStatistic_Station_Lane[x,y,z].CounterStatistic_Station_Lane[1,10,0]` | count | 0.45 | direct_id |

### IPC and Hand Load Station (1110)

- 14 candidate tag(s) considered -> 8 kept as genuine parameters (57%).
- Kept tags found by: 6 via *keyword* (only a descriptive word from the station's name matched the tag's path/name - a weaker signal), 2 via *direct_id* (the station's raw ID string appeared literally in the tag's path/name - a strong signal).
- 2 kept parameter(s) below 0.5 confidence - flagged with warning below.

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| Reject Count (station entry, per lane) (low confidence) | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiRO.RejectStatistic_Entry_Lane[x].RejectStatistic_Entry_Lane[1][11][0]` | count | 0.45 | direct_id |
| Station Cycle Counter (per lane) (low confidence) | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC4.CounterStatistic_Station_Lane[x,y,z].CounterStatistic_Station_Lane[1,11,0]` | count | 0.45 | direct_id |
| St113 E L Hand | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St113_EL_Hand` | - | 0.50 | keyword |
| St109 E L Hand | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St109_EL_Hand` | - | 0.50 | keyword |
| St107 E L Hand | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St107_EL_Hand` | - | 0.50 | keyword |
| St111 E L Hand | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St111_EL_Hand` | - | 0.50 | keyword |
| St105 E L Hand | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St105_EL_Hand` | - | 0.50 | keyword |
| St115 E L Hand | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St115_EL_Hand` | - | 0.50 | keyword |

### Check Format Position (1135)

- 33 candidate tag(s) considered -> 4 kept as genuine parameters (12%).
- Kept tags found by: 2 via *direct_id* (the station's raw ID string appeared literally in the tag's path/name - a strong signal), 2 via *keyword* (only a descriptive word from the station's name matched the tag's path/name - a weaker signal).
- 2 kept parameter(s) below 0.5 confidence - flagged with warning below.

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| Reject Count (station entry, per lane) (low confidence) | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiRO.RejectStatistic_Entry_Lane[x].RejectStatistic_Entry_Lane[1][13][5]` | count | 0.45 | direct_id |
| Station Cycle Counter (per lane) (low confidence) | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC4.CounterStatistic_Station_Lane[x,y,z].CounterStatistic_Station_Lane[1,13,5]` | count | 0.45 | direct_id |
|  | `` | - | 0.50 | keyword |
| St000 H H Format | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St000_HH_Format[x].St000_HH_Format[7]` | - | 0.50 | keyword |

### Check Catheter Cap Holder Empty (1140)

- 6 candidate tag(s) considered -> 2 kept as genuine parameters (33%).
- Kept tags found by: 2 via *direct_id* (the station's raw ID string appeared literally in the tag's path/name - a strong signal).
- 2 kept parameter(s) below 0.5 confidence - flagged with warning below.

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| Reject Count (station entry, per lane) (low confidence) | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiRO.RejectStatistic_Entry_Lane[x].RejectStatistic_Entry_Lane[1][14][0]` | count | 0.45 | direct_id |
| Station Cycle Counter (per lane) (low confidence) | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC4.CounterStatistic_Station_Lane[x,y,z].CounterStatistic_Station_Lane[1,14,0]` | count | 0.45 | direct_id |

### Loading Tray (2020)

- 19 candidate tag(s) considered -> 2 kept as genuine parameters (11%).
- Kept tags found by: 2 via *numeric_suffix* (the station's numeric code's last 3 digits matched a truncated St0*<digits> token in the tag's OPC path (this historian export drops the station number's leading digit) - a strong signal).

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| St020 Move Time | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St020_MoveTime` | s | 0.75 | numeric_suffix |
| St020 Inch One Mode | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St020_InchOneMode[x].St020_InchOneMode[4]` | - | 0.75 | numeric_suffix |

### Catheter Pusher (2022)

- 33 candidate tag(s) considered -> 16 kept as genuine parameters (48%).
- Kept tags found by: 16 via *numeric_suffix* (the station's numeric code's last 3 digits matched a truncated St0*<digits> token in the tag's OPC path (this historian export drops the station number's leading digit) - a strong signal).

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| St022 Dead Time | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St022_DeadTime` | s | 0.75 | numeric_suffix |
| St022 Waiting Pos Transfer Master | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St022_WaitingPosTransfer_Master` | mm | 0.75 | numeric_suffix |
| St022 Pull Down End Pos | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St022_PullDownEndPos` | mm | 0.75 | numeric_suffix |
| St022 Window Start1 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St022_WindowStart1` | mm | 0.75 | numeric_suffix |
| St022 Cap Docking Pos Master | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St022_CapDockingPos_Master` | mm | 0.75 | numeric_suffix |
| St022 Pull Down End Pos Slave | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St022_PullDownEndPos_Slave` | mm | 0.75 | numeric_suffix |
| St022 Pos Offset | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St022_PosOffset` | mm | 0.75 | numeric_suffix |
| St022 Slave Syn Position | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St022_SlaveSynPosition` | mm | 0.75 | numeric_suffix |
| St022 Cap Docking Pos Slave | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St022_CapDockingPos_Slave` | mm | 0.75 | numeric_suffix |
| St022 Actual Pull Down Pos | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St022_ActualPullDownPos` | mm | 0.75 | numeric_suffix |
| St022 Cylinder 5 1 Man In | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St022_Cylinder_5_1_ManIn` | - | 0.75 | numeric_suffix |
| St022 Cylinder 5 1 Man Out | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St022_Cylinder_5_1_ManOut` | - | 0.75 | numeric_suffix |
| St022 Vertical Cleaning Pos | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St022_VerticalCleaningPos` | mm | 0.75 | numeric_suffix |
| St022 Inch One Mode | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St022_InchOneMode[x].St022_InchOneMode[8]` | - | 0.75 | numeric_suffix |
| St022 Tool Circumference Vertical | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St022_ToolCircumference_Vertical` | mm | 0.75 | numeric_suffix |
| St022 Tool Circumference Horizontal | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St022_ToolCircumference_Horizontal` | mm | 0.75 | numeric_suffix |

### Splice Detection Top Foil (2026)

- 13 candidate tag(s) considered -> 8 kept as genuine parameters (62%).
- Kept tags found by: 8 via *numeric_suffix* (the station's numeric code's last 3 digits matched a truncated St0*<digits> token in the tag's OPC path (this historian export drops the station number's leading digit) - a strong signal).

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| St026 Zero Point | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St026_ZeroPoint` | - | 0.75 | numeric_suffix |
| St026 Reset Splice Existent | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St026_ResetSpliceExistent` | - | 0.75 | numeric_suffix |
| St026 Tolerance Window | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St026_ToleranceWindow` | mm | 0.75 | numeric_suffix |
| St026 Distance To Winder | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St026_DistanceToWinder` | mm | 0.75 | numeric_suffix |
| St026 Splice End Pos | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St026_SpliceEndPos` | mm | 0.75 | numeric_suffix |
| St026 Splice Expected | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St026_SpliceExpected` | - | 0.75 | numeric_suffix |
| St026 Splice Start Pos | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St026_SpliceStartPos` | mm | 0.75 | numeric_suffix |
| St026 Splice Check Rest Distance | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St026_SpliceCheckRestDistance` | mm | 0.75 | numeric_suffix |

### Top Foil Pull Rolls (2029)

- 40 candidate tag(s) considered -> 23 kept as genuine parameters (57%).
- Kept tags found by: 23 via *numeric_suffix* (the station's numeric code's last 3 digits matched a truncated St0*<digits> token in the tag's OPC path (this historian export drops the station number's leading digit) - a strong signal).

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| St029 Control Current Limit | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St029_ControlCurrentLimit` | - | 0.75 | numeric_suffix |
| St029 Pressure Tol Plus Pull Rolls | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St029_PressureTolPlus_PullRolls` | bar | 0.75 | numeric_suffix |
| St029 Print Mark K P | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St029_PrintMark_KP` | - | 0.75 | numeric_suffix |
| St029 Pressure Set Point Pull Rolls | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St029_PressureSetPoint_PullRolls` | bar | 0.75 | numeric_suffix |
| St029 Print Mark Position Set Point Lane1 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St029_PrintMarkPositionSetPoint_Lane1` | mm | 0.75 | numeric_suffix |
| St029 P M Enable | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St029_PMEnable` | - | 0.75 | numeric_suffix |
| St029 Reset Memory | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St029_ResetMemory` | - | 0.75 | numeric_suffix |
| St029 Pressure Tol Minus Pull Rolls | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St029_PressureTolMinus_PullRolls` | bar | 0.75 | numeric_suffix |
| St029 Vel Offset Lane1 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St029_VelOffset_Lane1` | mm/s | 0.75 | numeric_suffix |
| St029 Tol D M | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St029_TolDM` | - | 0.75 | numeric_suffix |
| St029 Print Mark K I | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St029_PrintMark_KI` | - | 0.75 | numeric_suffix |
| St029 Pressure Act Val Per Cent Pull Rolls | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St029_PressureActValPerCentPullRolls` | bar | 0.75 | numeric_suffix |
| St029 Print Mark Act Pos Dev Lane1 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St029_PrintMarkActPosDev_Lane1` | mm | 0.75 | numeric_suffix |
| St029 Control Done | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St029_ControlDone` | - | 0.75 | numeric_suffix |
| St029 Act Control Current | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St029_ActControlCurrent` | - | 0.75 | numeric_suffix |
| St029 Print Mark Act Pos Lane1 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St029_PrintMarkActPos_Lane1` | mm | 0.75 | numeric_suffix |
| St029 Print Mark Act Length Lane1 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St029_PrintMarkActLength_Lane1` | - | 0.75 | numeric_suffix |
| St029 act Status | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St029_actStatus` | - | 0.75 | numeric_suffix |
| St029 Pressure Act Val Pull Rolls | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St029_PressureActValPullRolls` | bar | 0.75 | numeric_suffix |
| St029 Inch One Mode | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St029_InchOneMode[x].St029_InchOneMode[2]` | - | 0.75 | numeric_suffix |
| St029 Man Open Lane1 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St029_ManOpen_Lane1` | - | 0.75 | numeric_suffix |
| St029 Man Close Lane1 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St029_ManClose_Lane1` | - | 0.75 | numeric_suffix |
| St029 Tool Circumference | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St029_ToolCircumference` | mm | 0.75 | numeric_suffix |

### Print Mark Printing (2032)

- 10 candidate tag(s) considered -> 5 kept as genuine parameters (50%).
- Kept tags found by: 5 via *numeric_suffix* (the station's numeric code's last 3 digits matched a truncated St0*<digits> token in the tag's OPC path (this historian export drops the station number's leading digit) - a strong signal).

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| St032 Tol Minus P M | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St032_TolMinus_PM` | - | 0.75 | numeric_suffix |
| St032 Print Offset | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St032_PrintOffset` | mm | 0.75 | numeric_suffix |
| St032 Tol Plus P M | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St032_TolPlus_PM` | - | 0.75 | numeric_suffix |
| St032 Print Mark Position Set Point | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St032_PrintMarkPositionSetPoint` | mm | 0.75 | numeric_suffix |
| St032 Print Mark Position | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St032_PrintMarkPosition` | mm | 0.75 | numeric_suffix |

### Fixed Printing (2035)

- 124 candidate tag(s) considered -> 43 kept as genuine parameters (35%).
- Kept tags found by: 43 via *numeric_suffix* (the station's numeric code's last 3 digits matched a truncated St0*<digits> token in the tag's OPC path (this historian export drops the station number's leading digit) - a strong signal).

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| St035 Cross Travel Service Pos Vel | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St035_CrossTravel_ServicePosVel` | mm/s | 0.75 | numeric_suffix |
| St035 Printer Enable | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St035_Printer_Enable[x].St035_Printer_Enable[2]` | - | 0.75 | numeric_suffix |
| St035 Cross Travel Basic Pos Vel | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St035_CrossTravel_BasicPosVel` | mm/s | 0.75 | numeric_suffix |
| St035 Printing Challenge Test On | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St035_Printing_ChallengeTestOn` | - | 0.75 | numeric_suffix |
| St035 Printing Trigger Pos Dead Time | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St035_Printing_TriggerPos_DeadTime[x].St035_Printing_TriggerPos_DeadTime[1]` | s | 0.75 | numeric_suffix |
| St035 Printing Challenge Test Repeat | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St035_Printing_ChallengeTestRepeat` | - | 0.75 | numeric_suffix |
| St035 Printing Web Pos Set Point | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St035_Printing_WebPosSetPoint[x].St035_Printing_WebPosSetPoint[1]` | mm | 0.75 | numeric_suffix |
| St035 Printing Trigger Pos | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St035_Printing_TriggerPos[x].St035_Printing_TriggerPos[2][1]` | mm | 0.75 | numeric_suffix |
| St035 Cross Travel Working Pos Vel | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St035_CrossTravel_WorkingPosVel` | mm/s | 0.75 | numeric_suffix |
| St035 Printing Trigger Pos Setting Wizard Value Basis | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St035_Printing_TriggerPosSettingWizardValueBasis[x].St035_Printing_TriggerPosSettingWizardValueBasis[2]` | mm | 0.75 | numeric_suffix |
| St035 Printing Web Pos Deviation Max | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St035_Printing_WebPosDeviationMax[x].St035_Printing_WebPosDeviationMax[1]` | mm | 0.75 | numeric_suffix |
| St035 Printing Trigger Pos Setting Wizard Enable | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St035_Printing_TriggerPosSettingWizardEnable[x].St035_Printing_TriggerPosSettingWizardEnable[2]` | - | 0.75 | numeric_suffix |
| St035 Printing Challenge Test Start Offset | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St035_Printing_ChallengeTestStartOffset[x].St035_Printing_ChallengeTestStartOffset[2]` | mm | 0.75 | numeric_suffix |
| St035 Printing Trigger Pos Setting Wizard Value Set | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St035_Printing_TriggerPosSettingWizardValueSet[x].St035_Printing_TriggerPosSettingWizardValueSet[1]` | mm | 0.75 | numeric_suffix |
| St035 Cross Travel Service Pos | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St035_CrossTravel_ServicePos` | mm/s | 0.75 | numeric_suffix |
| St035 Printing Web Pos Trigger Pos Auto Corr On | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St035_Printing_WebPosTriggerPosAutoCorrOn[x].St035_Printing_WebPosTriggerPosAutoCorrOn[1]` | - | 0.75 | numeric_suffix |
| St035 Cross Travel Basic Pos | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St035_CrossTravel_BasicPos` | mm/s | 0.75 | numeric_suffix |
| St035 Printing Trigger Enable | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St035_Printing_TriggerEnable[x].St035_Printing_TriggerEnable[2][4]` | - | 0.75 | numeric_suffix |
| St035 Printing Trigger Pos Setting Wizard Value | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St035_Printing_TriggerPosSettingWizardValue[x].St035_Printing_TriggerPosSettingWizardValue[2]` | mm | 0.75 | numeric_suffix |
| St035 Printing Web Pos Sensor Offset | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St035_Printing_WebPosSensorOffset[x].St035_Printing_WebPosSensorOffset[2]` | mm | 0.75 | numeric_suffix |
| St035 Cross Travel Working Pos | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St035_CrossTravel_WorkingPos` | mm/s | 0.75 | numeric_suffix |
| St035 Printing Web Pos Act Value Valid | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St035_Printing_WebPosActValueValid[x].St035_Printing_WebPosActValueValid[1]` | - | 0.75 | numeric_suffix |
| St035 Printing Trigger Pos Out Of Range Error Txt | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St035_Printing_TriggerPos_OutOfRange_Error_Txt[x].St035_Printing_TriggerPos_OutOfRange_Error_Txt[1]` | mm | 0.75 | numeric_suffix |
| St035 Cross Travel Working Pos Reached | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St035_CrossTravel_WorkingPosReached` | - | 0.75 | numeric_suffix |
| St035 Printing Web Pos Deviation O K | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St035_Printing_WebPosDeviationOK[x].St035_Printing_WebPosDeviationOK[1]` | - | 0.75 | numeric_suffix |
| St035 Cross Travel Service Pos Reached | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St035_CrossTravel_ServicePosReached` | - | 0.75 | numeric_suffix |
| St035 Printing Web Pos Act Value | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St035_Printing_WebPosActValue[x].St035_Printing_WebPosActValue[2]` | mm | 0.75 | numeric_suffix |
| St035 Cross Travel Basic Pos Reached | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St035_CrossTravel_BasicPosReached` | - | 0.75 | numeric_suffix |
| St035 Printing Trigger Pos Out Of Range Error Num | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St035_Printing_TriggerPos_OutOfRange_Error_Num[x].St035_Printing_TriggerPos_OutOfRange_Error_Num[1]` | mm | 0.75 | numeric_suffix |
| St035 Printing Challenge Test Cycle Count | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St035_Printing_ChallengeTestCycleCount` | count | 0.75 | numeric_suffix |
| St035 Act Job Name Right | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St035_ActJobNameRight` | - | 0.75 | numeric_suffix |
| St035 Act Job Name Left | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St035_ActJobNameLeft` | - | 0.75 | numeric_suffix |
| St035 Printing Web Pos Deviation | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St035_Printing_WebPosDeviation[x].St035_Printing_WebPosDeviation[1]` | mm | 0.75 | numeric_suffix |
| St035 Job Name | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St035_JobName` | - | 0.75 | numeric_suffix |
| St035 Use Vacuum Strips | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St035_UseVacuumStrips` | - | 0.75 | numeric_suffix |
| St035 Inch One Mode | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St035_InchOneMode[x].St035_InchOneMode[1]` | - | 0.75 | numeric_suffix |
| St035 Cross Travel Service Pos Positioning Manually | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St035_CrossTravel_ServicePosPositioningManually` | mm/s | 0.75 | numeric_suffix |
| St035 Cross Travel Working Pos Positioning Manually | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St035_CrossTravel_WorkingPosPositioningManually` | mm/s | 0.75 | numeric_suffix |
| St035 Cross Travel One Working Cycle Positioning Manually | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St035_CrossTravel_OneWorkingCyclePositioningManually` | mm/s | 0.75 | numeric_suffix |
| St035 Job Name | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St035_JobName[x].St035_JobName[10]` | - | 0.75 | numeric_suffix |
| St035 Cross Travel Basic Pos Positioning Manually | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St035_CrossTravel_BasicPosPositioningManually` | mm/s | 0.75 | numeric_suffix |
| St035 Job Nr | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St035_JobNr` | - | 0.75 | numeric_suffix |
| St035 Print Data | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St035_PrintData[x].St035_PrintData[12]` | - | 0.75 | numeric_suffix |

### Variable Printing (2037)

- 123 candidate tag(s) considered -> 43 kept as genuine parameters (35%).
- Kept tags found by: 43 via *numeric_suffix* (the station's numeric code's last 3 digits matched a truncated St0*<digits> token in the tag's OPC path (this historian export drops the station number's leading digit) - a strong signal).

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| St037 Printing Trigger Pos Setting Wizard Value | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St037_Printing_TriggerPosSettingWizardValue[x].St037_Printing_TriggerPosSettingWizardValue[1]` | mm | 0.75 | numeric_suffix |
| St037 Printing Web Pos Set Point | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St037_Printing_WebPosSetPoint[x].St037_Printing_WebPosSetPoint[2]` | mm | 0.75 | numeric_suffix |
| St037 Printing Challenge Test Start Offset | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St037_Printing_ChallengeTestStartOffset[x].St037_Printing_ChallengeTestStartOffset[2]` | mm | 0.75 | numeric_suffix |
| St037 Cross Travel Service Pos Vel | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St037_CrossTravel_ServicePosVel` | mm/s | 0.75 | numeric_suffix |
| St037 Cross Travel Working Pos | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St037_CrossTravel_WorkingPos` | mm/s | 0.75 | numeric_suffix |
| St037 Printing Trigger Pos Setting Wizard Enable | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St037_Printing_TriggerPosSettingWizardEnable[x].St037_Printing_TriggerPosSettingWizardEnable[1]` | - | 0.75 | numeric_suffix |
| St037 Printing Trigger Pos Setting Wizard Value Set | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St037_Printing_TriggerPosSettingWizardValueSet[x].St037_Printing_TriggerPosSettingWizardValueSet[2]` | mm | 0.75 | numeric_suffix |
| St037 Printing Trigger Enable | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St037_Printing_TriggerEnable[x].St037_Printing_TriggerEnable[2][2]` | - | 0.75 | numeric_suffix |
| St037 Printing Trigger Pos | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St037_Printing_TriggerPos[x].St037_Printing_TriggerPos[1][5]` | mm | 0.75 | numeric_suffix |
| St037 Printer Enable | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St037_Printer_Enable[x].St037_Printer_Enable[1]` | - | 0.75 | numeric_suffix |
| St037 Printing Web Pos Sensor Offset | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St037_Printing_WebPosSensorOffset[x].St037_Printing_WebPosSensorOffset[2]` | mm | 0.75 | numeric_suffix |
| St037 Printing Web Pos Trigger Pos Auto Corr On | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St037_Printing_WebPosTriggerPosAutoCorrOn[x].St037_Printing_WebPosTriggerPosAutoCorrOn[1]` | - | 0.75 | numeric_suffix |
| St037 Cross Travel Working Pos Vel | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St037_CrossTravel_WorkingPosVel` | mm/s | 0.75 | numeric_suffix |
| St037 Printing Challenge Test On | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St037_Printing_ChallengeTestOn` | - | 0.75 | numeric_suffix |
| St037 Cross Travel Basic Pos | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St037_CrossTravel_BasicPos` | mm/s | 0.75 | numeric_suffix |
| St037 Cross Travel Service Pos | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St037_CrossTravel_ServicePos` | mm/s | 0.75 | numeric_suffix |
| St037 Printing Trigger Pos Dead Time | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St037_Printing_TriggerPos_DeadTime[x].St037_Printing_TriggerPos_DeadTime[1]` | s | 0.75 | numeric_suffix |
| St037 Cross Travel Basic Pos Vel | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St037_CrossTravel_BasicPosVel` | mm/s | 0.75 | numeric_suffix |
| St037 Printing Challenge Test Repeat | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St037_Printing_ChallengeTestRepeat` | - | 0.75 | numeric_suffix |
| St037 Printing Web Pos Deviation Max | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St037_Printing_WebPosDeviationMax[x].St037_Printing_WebPosDeviationMax[1]` | mm | 0.75 | numeric_suffix |
| St037 Printing Trigger Pos Setting Wizard Value Basis | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St037_Printing_TriggerPosSettingWizardValueBasis[x].St037_Printing_TriggerPosSettingWizardValueBasis[2]` | mm | 0.75 | numeric_suffix |
| St037 Cross Travel Basic Pos Reached | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St037_CrossTravel_BasicPosReached` | - | 0.75 | numeric_suffix |
| St037 Printing Web Pos Act Value Valid | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St037_Printing_WebPosActValueValid[x].St037_Printing_WebPosActValueValid[2]` | - | 0.75 | numeric_suffix |
| St037 Printing Challenge Test Cycle Count | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St037_Printing_ChallengeTestCycleCount` | count | 0.75 | numeric_suffix |
| St037 Printing Web Pos Deviation O K | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St037_Printing_WebPosDeviationOK[x].St037_Printing_WebPosDeviationOK[2]` | - | 0.75 | numeric_suffix |
| St037 Cross Travel Working Pos Reached | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St037_CrossTravel_WorkingPosReached` | - | 0.75 | numeric_suffix |
| St037 Act Job Name Right | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St037_ActJobNameRight` | - | 0.75 | numeric_suffix |
| St037 Printing Trigger Pos Out Of Range Error Txt | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St037_Printing_TriggerPos_OutOfRange_Error_Txt[x].St037_Printing_TriggerPos_OutOfRange_Error_Txt[2]` | mm | 0.75 | numeric_suffix |
| St037 Act Job Name Left | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St037_ActJobNameLeft` | - | 0.75 | numeric_suffix |
| St037 Printing Web Pos Deviation | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St037_Printing_WebPosDeviation[x].St037_Printing_WebPosDeviation[2]` | mm | 0.75 | numeric_suffix |
| St037 Printing Trigger Pos Out Of Range Error Num | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St037_Printing_TriggerPos_OutOfRange_Error_Num[x].St037_Printing_TriggerPos_OutOfRange_Error_Num[2]` | mm | 0.75 | numeric_suffix |
| St037 Cross Travel Service Pos Reached | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St037_CrossTravel_ServicePosReached` | - | 0.75 | numeric_suffix |
| St037 Printing Web Pos Act Value | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St037_Printing_WebPosActValue[x].St037_Printing_WebPosActValue[2]` | mm | 0.75 | numeric_suffix |
| St037 Job Name | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St037_JobName` | - | 0.75 | numeric_suffix |
| St037 Cross Travel Service Pos Positioning Manually | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St037_CrossTravel_ServicePosPositioningManually` | mm/s | 0.75 | numeric_suffix |
| St037 Cross Travel Basic Pos Positioning Manually | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St037_CrossTravel_BasicPosPositioningManually` | mm/s | 0.75 | numeric_suffix |
| St037 Inch One Mode | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St037_InchOneMode[x].St037_InchOneMode[11]` | - | 0.75 | numeric_suffix |
| St037 Use Vacuum Strips | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St037_UseVacuumStrips` | - | 0.75 | numeric_suffix |
| St037 Cross Travel Working Pos Positioning Manually | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St037_CrossTravel_WorkingPosPositioningManually` | mm/s | 0.75 | numeric_suffix |
| St037 Print Data | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St037_PrintData[x].St037_PrintData[19]` | - | 0.75 | numeric_suffix |
| St037 Job Name | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St037_JobName[x].St037_JobName[8]` | - | 0.75 | numeric_suffix |
| St037 Cross Travel One Working Cycle Positioning Manually | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St037_CrossTravel_OneWorkingCyclePositioningManually` | mm/s | 0.75 | numeric_suffix |
| St037 Job Nr | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St037_JobNr` | - | 0.75 | numeric_suffix |

### Top Foil Pull Rollers (2039)

- 46 candidate tag(s) considered -> 30 kept as genuine parameters (65%).
- Kept tags found by: 30 via *numeric_suffix* (the station's numeric code's last 3 digits matched a truncated St0*<digits> token in the tag's OPC path (this historian export drops the station number's leading digit) - a strong signal).

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| St039 Pressure Tol Plus Dancer | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St039_PressureTolPlus_Dancer` | bar | 0.75 | numeric_suffix |
| St039 Pressure Set Point Dancer | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St039_PressureSetPoint_Dancer` | bar | 0.75 | numeric_suffix |
| St039 Pressure Set Point Pull Rolls | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St039_PressureSetPoint_PullRolls` | bar | 0.75 | numeric_suffix |
| St039 P M Controlling | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St039_PM_Controlling` | - | 0.75 | numeric_suffix |
| St039 Pressure Tol Minus Pull Rolls | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St039_PressureTolMinus_PullRolls` | bar | 0.75 | numeric_suffix |
| St039 Print Mark Position Set Point Lane1 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St039_PrintMarkPositionSetPoint_Lane1` | mm | 0.75 | numeric_suffix |
| St039 Pressure Tol Minus Dancer | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St039_PressureTolMinus_Dancer` | bar | 0.75 | numeric_suffix |
| St039 Pressure Tol Plus Pull Rolls | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St039_PressureTolPlus_PullRolls` | bar | 0.75 | numeric_suffix |
| St039 Dancer Pos Setpoint | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St039_DancerPosSetpoint` | mm | 0.75 | numeric_suffix |
| St039 Dancer Pos Max | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St039_DancerPosMax` | mm | 0.75 | numeric_suffix |
| St039 Print Mark Act Pos Lane1 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St039_PrintMarkActPos_Lane1` | mm | 0.75 | numeric_suffix |
| St039 Print Mark Act Pos Dev Lane1 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St039_PrintMarkActPosDev_Lane1` | mm | 0.75 | numeric_suffix |
| St039 Pressure Act Val Dancer | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St039_PressureActVal_Dancer` | bar | 0.75 | numeric_suffix |
| St039 act Status | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St039_actStatus` | - | 0.75 | numeric_suffix |
| St039 Current Process Time | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St039_CurrentProcessTime` | s | 0.75 | numeric_suffix |
| St039 Dancer Pos Act Per Cent | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St039_DancerPosActPerCent` | mm | 0.75 | numeric_suffix |
| St039 Pressure Act Val Per Cent Dancer | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St039_PressureActValPerCentDancer` | bar | 0.75 | numeric_suffix |
| St039 Dancer Pos Act | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St039_DancerPosAct` | mm | 0.75 | numeric_suffix |
| St039 Dancer Pos Min | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St039_DancerPosMin` | mm | 0.75 | numeric_suffix |
| St039 Dancer Pos Mid | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St039_DancerPosMid` | mm | 0.75 | numeric_suffix |
| St039 Pressure Act Val Pull Rolls | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St039_PressureActValPullRolls` | bar | 0.75 | numeric_suffix |
| St039 Print Mark T P Deviation | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St039_PrintMarkTPDeviation` | - | 0.75 | numeric_suffix |
| St039 Pressure Act Val Per Cent Pull Rolls | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St039_PressureActValPerCentPullRolls` | bar | 0.75 | numeric_suffix |
| St039 Print Mark Act Length Lane1 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St039_PrintMarkActLength_Lane1` | - | 0.75 | numeric_suffix |
| St039 Release Calibrate Dancer | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St039_ReleaseCalibrateDancer` | - | 0.75 | numeric_suffix |
| St039 Man Open Lane1 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St039_ManOpen_Lane1` | - | 0.75 | numeric_suffix |
| St039 Man Close Lane1 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St039_ManClose_Lane1` | - | 0.75 | numeric_suffix |
| St039 Inch One Mode | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St039_InchOneMode[x].St039_InchOneMode[4]` | - | 0.75 | numeric_suffix |
| St039 Calibrate Dancer | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St039_CalibrateDancer` | - | 0.75 | numeric_suffix |
| St039 Tool Circumference | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St039_ToolCircumference` | mm | 0.75 | numeric_suffix |

### Vision System Printing (2041)

- 84 candidate tag(s) considered -> 80 kept as genuine parameters (95%).
- Kept tags found by: 80 via *numeric_suffix* (the station's numeric code's last 3 digits matched a truncated St0*<digits> token in the tag's OPC path (this historian export drops the station number's leading digit) - a strong signal).

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| St041 1 B1 Consecutive Fault Code No Read Cycles | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St041_1B1_ConsecutiveFault_CodeNoRead_Cycles` | - | 0.75 | numeric_suffix |
| St041 1 B1 Trigger Position | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St041_1B1_TriggerPosition` | mm | 0.75 | numeric_suffix |
| St041 Light Intensity | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St041_LightIntensity` | - | 0.75 | numeric_suffix |
| St041 1 B1 Print Mark Adjustment O N | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St041_1B1_PrintMarkAdjustmentON` | - | 0.75 | numeric_suffix |
| St041 1 B1 Consecutive Fault Code No Read Faults | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St041_1B1_ConsecutiveFault_CodeNoRead_Faults` | - | 0.75 | numeric_suffix |
| St041 1 B1 Counter Cycle Time Overrun | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St041_1B1_CounterCycleTimeOverrun_` | s | 0.75 | numeric_suffix |
| Results Lane4 Result Fix Print Lane4 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St041_1B1_CameraResult.ResultsLane4_ResultFixPrintLane4` | - | 0.75 | numeric_suffix |
| Results Lane3 Result Var Print Lane3 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St041_1B1_CameraResult.ResultsLane3_ResultVarPrintLane3` | - | 0.75 | numeric_suffix |
| Results Lane2 Result Var Print Lane2 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St041_1B1_CameraResult.ResultsLane2_ResultVarPrintLane2` | - | 0.75 | numeric_suffix |
| Reserved Bit18 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St041_1B1_CameraResult.ReservedBit18` | - | 0.75 | numeric_suffix |
| Reserved Bit15 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St041_1B1_CameraResult.ReservedBit15` | - | 0.75 | numeric_suffix |
| Results Lane5 Result Var Print Lane5 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St041_1B1_CameraResult.ResultsLane5_ResultVarPrintLane5` | - | 0.75 | numeric_suffix |
| Reserved Bit23 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St041_1B1_CameraResult.ReservedBit23` | - | 0.75 | numeric_suffix |
| Result Light Level Light Level Value | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St041_1B1_CameraResult.ResultLightLevel_LightLevelValue` | mm/s | 0.75 | numeric_suffix |
| Reserved Bit31 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St041_1B1_CameraResult.ReservedBit31` | - | 0.75 | numeric_suffix |
| Reserved Bit12 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St041_1B1_CameraResult.ReservedBit12` | - | 0.75 | numeric_suffix |
| Reserved Bit13 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St041_1B1_CameraResult.ReservedBit13` | - | 0.75 | numeric_suffix |
| Reserved Bit28 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St041_1B1_CameraResult.ReservedBit28` | - | 0.75 | numeric_suffix |
| Results Lane5 Result Fix Print Lane5 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St041_1B1_CameraResult.ResultsLane5_ResultFixPrintLane5` | - | 0.75 | numeric_suffix |
| Results Lane1 Result Var Print Lane1 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St041_1B1_CameraResult.ResultsLane1_ResultVarPrintLane1` | - | 0.75 | numeric_suffix |
| Reserved Bit25 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St041_1B1_CameraResult.ReservedBit25` | - | 0.75 | numeric_suffix |
| Results Lane4 Result Var Print Lane4 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St041_1B1_CameraResult.ResultsLane4_ResultVarPrintLane4` | - | 0.75 | numeric_suffix |
| Reserved Bit30 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St041_1B1_CameraResult.ReservedBit30` | - | 0.75 | numeric_suffix |
| Reserved Bit14 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St041_1B1_CameraResult.ReservedBit14` | - | 0.75 | numeric_suffix |
| Reserved Bit16 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St041_1B1_CameraResult.ReservedBit16` | - | 0.75 | numeric_suffix |
| Reserved Bit27 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St041_1B1_CameraResult.ReservedBit27` | - | 0.75 | numeric_suffix |
| Reserved Bit22 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St041_1B1_CameraResult.ReservedBit22` | - | 0.75 | numeric_suffix |
| Results Lane1 Result Fix Print Lane1 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St041_1B1_CameraResult.ResultsLane1_ResultFixPrintLane1` | - | 0.75 | numeric_suffix |
| Reserved Bit21 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St041_1B1_CameraResult.ReservedBit21` | - | 0.75 | numeric_suffix |
| Reserved Bit29 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St041_1B1_CameraResult.ReservedBit29` | - | 0.75 | numeric_suffix |
| Results Lane3 Result Fix Print Lane3 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St041_1B1_CameraResult.ResultsLane3_ResultFixPrintLane3` | - | 0.75 | numeric_suffix |
| Reserved Bit19 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St041_1B1_CameraResult.ReservedBit19` | - | 0.75 | numeric_suffix |
| Reserved Bit24 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St041_1B1_CameraResult.ReservedBit24` | - | 0.75 | numeric_suffix |
| Reserved Bit11 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St041_1B1_CameraResult.ReservedBit11` | - | 0.75 | numeric_suffix |
| Results Lane2 Result Fix Print Lane2 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St041_1B1_CameraResult.ResultsLane2_ResultFixPrintLane2` | - | 0.75 | numeric_suffix |
| Reserved Bit20 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St041_1B1_CameraResult.ReservedBit20` | - | 0.75 | numeric_suffix |
| Reserved Bit26 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St041_1B1_CameraResult.ReservedBit26` | - | 0.75 | numeric_suffix |
| Reserved Bit17 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St041_1B1_CameraResult.ReservedBit17` | - | 0.75 | numeric_suffix |
| Result Light Level Light Level Result | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St041_1B1_CameraResult.ResultLightLevel_LightLevelResult` | mm/s | 0.75 | numeric_suffix |
| St041 1 B1 Io Buffer Error Code | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St041_1B1_IoBufferErrorCode` | - | 0.75 | numeric_suffix |
| St041 1 B1 Camera Data Dummy String | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St041_1B1_CameraDataDummyString` | - | 0.75 | numeric_suffix |
| St041 1 B1 Camera Data Dummy Real | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St041_1B1_CameraDataDummyReal` | - | 0.75 | numeric_suffix |
| St041 1 B1 P N Error Code | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St041_1B1_PN_ErrorCode` | - | 0.75 | numeric_suffix |
| St041 1 B1 T C P Error Code | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St041_1B1_TCP_ErrorCode` | - | 0.75 | numeric_suffix |
| St041 1 B1 Io Interface Error Msg | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St041_1B1_IoInterfaceErrorMsg` | - | 0.75 | numeric_suffix |
| St041 1 B1 Print Mark Position | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St041_1B1_PrintMarkPosition` | mm | 0.75 | numeric_suffix |
| St041 1 B1 Pm Pos Act Val | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St041_1B1_PmPosActVal` | mm | 0.75 | numeric_suffix |
| St041 1 B1 Pm Len Act Val | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St041_1B1_PmLenActVal` | - | 0.75 | numeric_suffix |
| St041 1 B1 Tcp Error Msg | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St041_1B1_TcpErrorMsg` | - | 0.75 | numeric_suffix |
| St041 1 B1 Camera Data Dummy Bool | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St041_1B1_CameraDataDummyBool` | - | 0.75 | numeric_suffix |
| St041 1 B1 Camera Data Dummy Real | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St041_1B1_CameraDataDummyReal` | - | 0.75 | numeric_suffix |
| St041 1 B1 Camera Data Dummy String | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St041_1B1_CameraDataDummyString` | - | 0.75 | numeric_suffix |
| Variable Print Lane24 L O T Lane24 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St041_1B1_CameraData.VariablePrintLane24_LOTLane24` | - | 0.75 | numeric_suffix |
| Light Level Light Level Min | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St041_1B1_CameraData.LightLevel_LightLevelMin` | mm/s | 0.75 | numeric_suffix |
| Variable Print Lane24 D M Code01 Lane24 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St041_1B1_CameraData.VariablePrintLane24_DMCode01Lane24` | - | 0.75 | numeric_suffix |
| Variable Print Lane135 Exp Date Lane135 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St041_1B1_CameraData.VariablePrintLane135_ExpDateLane135` | - | 0.75 | numeric_suffix |
| Variable Print Lane135 Production Date Lane135 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St041_1B1_CameraData.VariablePrintLane135_ProductionDateLane135` | - | 0.75 | numeric_suffix |
| Variable Print Lane135 D M Code17 Lane135 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St041_1B1_CameraData.VariablePrintLane135_DMCode17Lane135` | - | 0.75 | numeric_suffix |
| Variable Print Lane24 D M Code11 Lane24 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St041_1B1_CameraData.VariablePrintLane24_DMCode11Lane24` | - | 0.75 | numeric_suffix |
| Variable Print Lane24 D M Code17 Lane24 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St041_1B1_CameraData.VariablePrintLane24_DMCode17Lane24` | - | 0.75 | numeric_suffix |
| Variable Print Lane135 R E F Lane135 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St041_1B1_CameraData.VariablePrintLane135_REFLane135` | - | 0.75 | numeric_suffix |
| Variable Print Lane24 Production Date Lane24 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St041_1B1_CameraData.VariablePrintLane24_ProductionDateLane24` | - | 0.75 | numeric_suffix |
| Variable Print Lane135 L O T Lane135 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St041_1B1_CameraData.VariablePrintLane135_LOTLane135` | - | 0.75 | numeric_suffix |
| Variable Print Lane135 Size135 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St041_1B1_CameraData.VariablePrintLane135_Size135` | - | 0.75 | numeric_suffix |
| Variable Print Lane24 R E F Lane24 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St041_1B1_CameraData.VariablePrintLane24_REFLane24` | - | 0.75 | numeric_suffix |
| Variable Print Lane24 Exp Date Lane24 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St041_1B1_CameraData.VariablePrintLane24_ExpDateLane24` | - | 0.75 | numeric_suffix |
| Variable Print Lane135 S K U Lane135 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St041_1B1_CameraData.VariablePrintLane135_SKULane135` | - | 0.75 | numeric_suffix |
| Variable Print Lane135 D M Code11 Lane135 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St041_1B1_CameraData.VariablePrintLane135_DMCode11Lane135` | - | 0.75 | numeric_suffix |
| Threshold O C R Threshold O C R | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St041_1B1_CameraData.ThresholdOCR_ThresholdOCR` | - | 0.75 | numeric_suffix |
| Light Level Light Level Max | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St041_1B1_CameraData.LightLevel_LightLevelMax` | mm/s | 0.75 | numeric_suffix |
| Variable Print Lane135 Sizemm Lane135 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St041_1B1_CameraData.VariablePrintLane135_SizemmLane135` | - | 0.75 | numeric_suffix |
| Fixed Print Deviation | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St041_1B1_CameraData.FixedPrint_Deviation` | - | 0.75 | numeric_suffix |
| Variable Print Lane24 Size Lane24 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St041_1B1_CameraData.VariablePrintLane24_SizeLane24` | - | 0.75 | numeric_suffix |
| Variable Print Lane24 S K U Lane24 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St041_1B1_CameraData.VariablePrintLane24_SKULane24` | - | 0.75 | numeric_suffix |
| Variable Print Lane24 Sizemm Lane24 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St041_1B1_CameraData.VariablePrintLane24_SizemmLane24` | - | 0.75 | numeric_suffix |
| Variable Print Lane24 D M Code10 Lane24 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St041_1B1_CameraData.VariablePrintLane24_DMCode10Lane24` | - | 0.75 | numeric_suffix |
| Variable Print Lane135 D M Code01 Lane135 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St041_1B1_CameraData.VariablePrintLane135_DMCode01Lane135` | - | 0.75 | numeric_suffix |
| Variable Print Lane135 Dm Code10 Lane135 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St041_1B1_CameraData.VariablePrintLane135_DmCode10Lane135` | - | 0.75 | numeric_suffix |
| St041 1 B1 Man Trigger | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St041_1B1_ManTrigger` | - | 0.75 | numeric_suffix |
| St041 1 B1 Light Man On | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St041_1B1_LightManOn` | - | 0.75 | numeric_suffix |

### Top Label Presence Check (2042)

- 4 candidate tag(s) considered -> 0 kept as genuine parameters (0%).

_No genuine parameters found among this station's candidates._

### Waste Grid Pull Rolls (2043)

- 21 candidate tag(s) considered -> 5 kept as genuine parameters (24%).
- Kept tags found by: 5 via *numeric_suffix* (the station's numeric code's last 3 digits matched a truncated St0*<digits> token in the tag's OPC path (this historian export drops the station number's leading digit) - a strong signal).

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| St043 Vel Offset Lane1 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St043_VelOffset_Lane1` | mm/s | 0.75 | numeric_suffix |
| St043 Reset Memory | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St043_ResetMemory` | - | 0.75 | numeric_suffix |
| St043 act Status | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St043_actStatus` | - | 0.75 | numeric_suffix |
| St043 Tool Circumference | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St043_ToolCircumference` | mm | 0.75 | numeric_suffix |
| St043 Inch One Mode | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St043_InchOneMode[x].St043_InchOneMode[3]` | - | 0.75 | numeric_suffix |

### Brand Label Application (2045)

- 92 candidate tag(s) considered -> 39 kept as genuine parameters (42%).
- Kept tags found by: 39 via *numeric_suffix* (the station's numeric code's last 3 digits matched a truncated St0*<digits> token in the tag's OPC path (this historian export drops the station number's leading digit) - a strong signal).

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| St045 Labeling Web Pos Set Point | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St045_Labeling_WebPosSetPoint[x].St045_Labeling_WebPosSetPoint[2]` | mm | 0.75 | numeric_suffix |
| St045 Labeling Challenge Test On | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St045_Labeling_ChallengeTestOn` | - | 0.75 | numeric_suffix |
| St045 Labeling Challenge Test Start Offset | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St045_Labeling_ChallengeTestStartOffset[x].St045_Labeling_ChallengeTestStartOffset[2]` | mm | 0.75 | numeric_suffix |
| St045 Cross Travel Basic Pos Vel | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St045_CrossTravel_BasicPosVel` | mm/s | 0.75 | numeric_suffix |
| St045 Cross Travel Basic Pos | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St045_CrossTravel_BasicPos` | mm/s | 0.75 | numeric_suffix |
| St045 Labeling Web Pos Trigger Pos Auto Corr On | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St045_Labeling_WebPosTriggerPosAutoCorrOn[x].St045_Labeling_WebPosTriggerPosAutoCorrOn[2]` | - | 0.75 | numeric_suffix |
| St045 Labeling Web Pos Deviation Max | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St045_Labeling_WebPosDeviationMax[x].St045_Labeling_WebPosDeviationMax[2]` | mm | 0.75 | numeric_suffix |
| St045 Labeling Trigger Pos Setting Wizard Value Basis | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St045_Labeling_TriggerPosSettingWizardValueBasis[x].St045_Labeling_TriggerPosSettingWizardValueBasis[2]` | mm | 0.75 | numeric_suffix |
| St045 Cross Travel Service Pos Vel | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St045_CrossTravel_ServicePosVel` | mm/s | 0.75 | numeric_suffix |
| St045 Labeling Trigger Pos Setting Wizard Value Set | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St045_Labeling_TriggerPosSettingWizardValueSet[x].St045_Labeling_TriggerPosSettingWizardValueSet[2]` | mm | 0.75 | numeric_suffix |
| St045 Cross Travel Working Pos Vel | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St045_CrossTravel_WorkingPosVel` | mm/s | 0.75 | numeric_suffix |
| St045 Herma Label Length | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St045_Herma_Label_Length[x].St045_Herma_Label_Length[2]` | - | 0.75 | numeric_suffix |
| St045 Cross Travel Service Pos | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St045_CrossTravel_ServicePos` | mm/s | 0.75 | numeric_suffix |
| St045 Labeling Web Pos Sensor Offset | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St045_Labeling_WebPosSensorOffset[x].St045_Labeling_WebPosSensorOffset[1]` | mm | 0.75 | numeric_suffix |
| St045 Herma Enable | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St045_Herma_Enable[x].St045_Herma_Enable[1]` | - | 0.75 | numeric_suffix |
| St045 Labeling Trigger Enable | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St045_Labeling_TriggerEnable[x].St045_Labeling_TriggerEnable[1][5]` | - | 0.75 | numeric_suffix |
| St045 Labeling Challenge Test Repeat | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St045_Labeling_ChallengeTestRepeat` | - | 0.75 | numeric_suffix |
| St045 Cross Travel Working Pos | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St045_CrossTravel_WorkingPos` | mm/s | 0.75 | numeric_suffix |
| St045 Labeling Trigger Pos Dead Time | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St045_Labeling_TriggerPos_DeadTime[x].St045_Labeling_TriggerPos_DeadTime[2]` | s | 0.75 | numeric_suffix |
| St045 Labeling Trigger Pos Setting Wizard Value | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St045_Labeling_TriggerPosSettingWizardValue[x].St045_Labeling_TriggerPosSettingWizardValue[1]` | mm | 0.75 | numeric_suffix |
| St045 Labeling Trigger Pos Setting Wizard Enable | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St045_Labeling_TriggerPosSettingWizardEnable[x].St045_Labeling_TriggerPosSettingWizardEnable[1]` | - | 0.75 | numeric_suffix |
| St045 Labeling Trigger Pos | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St045_Labeling_TriggerPos[x].St045_Labeling_TriggerPos[2][2]` | mm | 0.75 | numeric_suffix |
| St045 Labeling Trigger Pos Out Of Range Error Txt | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St045_Labeling_TriggerPos_OutOfRange_Error_Txt[x].St045_Labeling_TriggerPos_OutOfRange_Error_Txt[2]` | mm | 0.75 | numeric_suffix |
| St045 Labeling Web Pos Deviation | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St045_Labeling_WebPosDeviation[x].St045_Labeling_WebPosDeviation[1]` | mm | 0.75 | numeric_suffix |
| St045 Cross Travel Working Pos Reached | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St045_CrossTravel_WorkingPosReached` | - | 0.75 | numeric_suffix |
| St045 Labeling Web Pos Act Value | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St045_Labeling_WebPosActValue[x].St045_Labeling_WebPosActValue[2]` | mm | 0.75 | numeric_suffix |
| St045 Labeling Web Pos Act Value Valid | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St045_Labeling_WebPosActValueValid[x].St045_Labeling_WebPosActValueValid[2]` | - | 0.75 | numeric_suffix |
| St045 Labeling Challenge Test Cycle Count | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St045_Labeling_ChallengeTestCycleCount` | count | 0.75 | numeric_suffix |
| St045 Labeling Trigger Pos Out Of Range Error Num | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St045_Labeling_TriggerPos_OutOfRange_Error_Num[x].St045_Labeling_TriggerPos_OutOfRange_Error_Num[2]` | mm | 0.75 | numeric_suffix |
| St045 Labeling Web Pos Deviation O K | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St045_Labeling_WebPosDeviationOK[x].St045_Labeling_WebPosDeviationOK[2]` | - | 0.75 | numeric_suffix |
| St045 Cross Travel Basic Pos Reached | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St045_CrossTravel_BasicPosReached` | - | 0.75 | numeric_suffix |
| St045 Cross Travel Service Pos Reached | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St045_CrossTravel_ServicePosReached` | - | 0.75 | numeric_suffix |
| St045 Cross Travel One Working Cycle Positioning Manually | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St045_CrossTravel_OneWorkingCyclePositioningManually` | mm/s | 0.75 | numeric_suffix |
| St045 Cross Travel Basic Pos Positioning Manually | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St045_CrossTravel_BasicPosPositioningManually` | mm/s | 0.75 | numeric_suffix |
| St045 Cross Travel Service Pos Positioning Manually | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St045_CrossTravel_ServicePosPositioningManually` | mm/s | 0.75 | numeric_suffix |
| St045 Labeling Trigger Manual | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St045_Labeling_Trigger_Manual[x].St045_Labeling_Trigger_Manual[1]` | - | 0.75 | numeric_suffix |
| St045 Inch One Mode | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St045_InchOneMode[x].St045_InchOneMode[10]` | - | 0.75 | numeric_suffix |
| St045 Cross Travel Working Pos Positioning Manually | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St045_CrossTravel_WorkingPosPositioningManually` | mm/s | 0.75 | numeric_suffix |
| St045 Use Vacuum Strips | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St045_UseVacuumStrips` | - | 0.75 | numeric_suffix |

### Sticky Tab Application (2047)

- 5 candidate tag(s) considered -> 1 kept as genuine parameters (20%).
- Kept tags found by: 1 via *direct_id* (the station's raw ID string appeared literally in the tag's path/name - a strong signal).

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| Diag P B 032 047 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiRO.DiagPB_032_047` | - | 0.75 | direct_id |

### Vision Check Arrow (2048)

- 99 candidate tag(s) considered -> 65 kept as genuine parameters (66%).
- Kept tags found by: 65 via *numeric_suffix* (the station's numeric code's last 3 digits matched a truncated St0*<digits> token in the tag's OPC path (this historian export drops the station number's leading digit) - a strong signal).

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| St048 Trigger Position Offset | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St048_TriggerPositionOffset` | mm | 0.75 | numeric_suffix |
| St048 Print Mark Adjustment O N | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St048_PrintMarkAdjustmentON` | - | 0.75 | numeric_suffix |
| St048 Trigger Position | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St048_TriggerPosition` | mm | 0.75 | numeric_suffix |
| St048 3 B1 P N Error Code | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St048_3B1_PN_ErrorCode` | - | 0.75 | numeric_suffix |
| St048 1 B1 Rema Fault Telnet | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St048_1B1_RemaFaultTelnet` | - | 0.75 | numeric_suffix |
| Light Level Pass | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St048_2B1_CameraData.LightLevel_Pass` | mm/s | 0.75 | numeric_suffix |
| Arrow Lane3 Blob Area | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St048_2B1_CameraData.ArrowLane3_Blob_Area` | - | 0.75 | numeric_suffix |
| Logic Overall Result Pass | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St048_2B1_CameraData.Logic_OverallResult_Pass` | - | 0.75 | numeric_suffix |
| Light Level Brightness | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St048_2B1_CameraData.LightLevel_Brightness` | mm/s | 0.75 | numeric_suffix |
| Arrow Lane3 Pass | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St048_2B1_CameraData.ArrowLane3_Pass` | - | 0.75 | numeric_suffix |
| St048 3 B1 Rema Fault Telnet | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St048_3B1_RemaFaultTelnet` | - | 0.75 | numeric_suffix |
| St048 Print Mark Length | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St048_PrintMarkLength` | - | 0.75 | numeric_suffix |
| St048 1 B1 Io Interface Error Msg | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St048_1B1_IoInterfaceErrorMsg` | - | 0.75 | numeric_suffix |
| St048 2 B1 T C P Error Code | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St048_2B1_TCP_ErrorCode` | - | 0.75 | numeric_suffix |
| St048 2 B1 Active Job | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St048_2B1_ActiveJob` | - | 0.75 | numeric_suffix |
| St048 2 B1 Io Interface Error Msg | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St048_2B1_IoInterfaceErrorMsg` | - | 0.75 | numeric_suffix |
| St048 2 B1 Rema Fault Telnet | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St048_2B1_RemaFaultTelnet` | - | 0.75 | numeric_suffix |
| St048 1 B1 Active Job | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St048_1B1_ActiveJob` | - | 0.75 | numeric_suffix |
| St048 1 B1 T C P Error Code | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St048_1B1_TCP_ErrorCode` | - | 0.75 | numeric_suffix |
| Arrow Lane2 Blob Area | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St048_1B1_CameraData.ArrowLane2_Blob_Area` | - | 0.75 | numeric_suffix |
| Light Level Brightness | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St048_1B1_CameraData.LightLevel_Brightness` | mm/s | 0.75 | numeric_suffix |
| Arrow Lane1 Pass | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St048_1B1_CameraData.ArrowLane1_Pass` | - | 0.75 | numeric_suffix |
| Logic Overall Result Pass | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St048_1B1_CameraData.Logic_OverallResult_Pass` | - | 0.75 | numeric_suffix |
| Arrow Lane1 Blob Area | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St048_1B1_CameraData.ArrowLane1_Blob_Area` | - | 0.75 | numeric_suffix |
| Arrow Lane2 Pass | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St048_1B1_CameraData.ArrowLane2_Pass` | - | 0.75 | numeric_suffix |
| Light Level Pass | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St048_1B1_CameraData.LightLevel_Pass` | mm/s | 0.75 | numeric_suffix |
| St048 3 B1 T C P Error Code | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St048_3B1_TCP_ErrorCode` | - | 0.75 | numeric_suffix |
| Light Level Pass | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St048_3B1_CameraData.LightLevel_Pass` | mm/s | 0.75 | numeric_suffix |
| Light Level Brightness | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St048_3B1_CameraData.LightLevel_Brightness` | mm/s | 0.75 | numeric_suffix |
| Arrow Lane5 Blob Area | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St048_3B1_CameraData.ArrowLane5_Blob_Area` | - | 0.75 | numeric_suffix |
| Arrow Lane4 Blob Area | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St048_3B1_CameraData.ArrowLane4_Blob_Area` | - | 0.75 | numeric_suffix |
| Arrow Lane5 Pass | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St048_3B1_CameraData.ArrowLane5_Pass` | - | 0.75 | numeric_suffix |
| Arrow Lane4 Pass | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St048_3B1_CameraData.ArrowLane4_Pass` | - | 0.75 | numeric_suffix |
| Logic Overall Result Pass | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St048_3B1_CameraData.Logic_OverallResult_Pass` | - | 0.75 | numeric_suffix |
| St048 1 B1 P N Error Code | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St048_1B1_PN_ErrorCode` | - | 0.75 | numeric_suffix |
| St048 3 B1 Io Interface Error Msg | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St048_3B1_IoInterfaceErrorMsg` | - | 0.75 | numeric_suffix |
| St048 3 B1 Active Job | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St048_3B1_ActiveJob` | - | 0.75 | numeric_suffix |
| St048 2 B1 P N Error Code | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St048_2B1_PN_ErrorCode` | - | 0.75 | numeric_suffix |
| St048 Print Mark Position | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St048_PrintMarkPosition` | mm | 0.75 | numeric_suffix |
| Light Level Minimum | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St048_3B1_CameraData.LightLevel_Minimum` | mm/s | 0.75 | numeric_suffix |
| Arrow Lane4 Maximum | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St048_3B1_CameraData.ArrowLane4_Maximum` | - | 0.75 | numeric_suffix |
| Arrow Lane5 Minimum | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St048_3B1_CameraData.ArrowLane5_Minimum` | - | 0.75 | numeric_suffix |
| Light Level Maximum | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St048_3B1_CameraData.LightLevel_Maximum` | mm/s | 0.75 | numeric_suffix |
| Arrow Lane4 Minimum | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St048_3B1_CameraData.ArrowLane4_Minimum` | - | 0.75 | numeric_suffix |
| Arrow Lane5 Maximum | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St048_3B1_CameraData.ArrowLane5_Maximum` | - | 0.75 | numeric_suffix |
| St048 Man Trigger | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St048_ManTrigger` | - | 0.75 | numeric_suffix |
| Light Level Maximum | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St048_2B1_CameraData.LightLevel_Maximum` | mm/s | 0.75 | numeric_suffix |
| Arrow Lane3 Minimum | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St048_2B1_CameraData.ArrowLane3_Minimum` | - | 0.75 | numeric_suffix |
| Light Level Minimum | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St048_2B1_CameraData.LightLevel_Minimum` | mm/s | 0.75 | numeric_suffix |
| Arrow Lane3 Maximum | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St048_2B1_CameraData.ArrowLane3_Maximum` | - | 0.75 | numeric_suffix |
| St048 2 B1 I P Address | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St048_2B1_IP_Address` | - | 0.75 | numeric_suffix |
| St048 1 B1 P C Job No | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St048_1B1_PC_JobNo` | - | 0.75 | numeric_suffix |
| St048 1 B1 I P Address | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St048_1B1_IP_Address` | - | 0.75 | numeric_suffix |
| St048 2 B1 P C Job No | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St048_2B1_PC_JobNo` | - | 0.75 | numeric_suffix |
| St048 2 B1 Pre Def Jobs | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St048_2B1_PreDefJobs[x].St048_2B1_PreDefJobs[6]` | - | 0.75 | numeric_suffix |
| Light Level Maximum | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St048_1B1_CameraData.LightLevel_Maximum` | mm/s | 0.75 | numeric_suffix |
| Light Level Minimum | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St048_1B1_CameraData.LightLevel_Minimum` | mm/s | 0.75 | numeric_suffix |
| Arrow Lane1 Maximum | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St048_1B1_CameraData.ArrowLane1_Maximum` | - | 0.75 | numeric_suffix |
| Arrow Lane1 Minimum | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St048_1B1_CameraData.ArrowLane1_Minimum` | - | 0.75 | numeric_suffix |
| Arrow Lane2 Maximum | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St048_1B1_CameraData.ArrowLane2_Maximum` | - | 0.75 | numeric_suffix |
| Arrow Lane2 Minimum | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St048_1B1_CameraData.ArrowLane2_Minimum` | - | 0.75 | numeric_suffix |
| St048 3 B1 P C Job No | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St048_3B1_PC_JobNo` | - | 0.75 | numeric_suffix |
| St048 1 B1 Pre Def Jobs | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St048_1B1_PreDefJobs[x].St048_1B1_PreDefJobs[1]` | - | 0.75 | numeric_suffix |
| St048 3 B1 I P Address | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St048_3B1_IP_Address` | - | 0.75 | numeric_suffix |
| St048 3 B1 Pre Def Jobs | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St048_3B1_PreDefJobs[x].St048_3B1_PreDefJobs[9]` | - | 0.75 | numeric_suffix |

### Label Presence Check (2049)

- 34 candidate tag(s) considered -> 15 kept as genuine parameters (44%).
- Kept tags found by: 15 via *numeric_suffix* (the station's numeric code's last 3 digits matched a truncated St0*<digits> token in the tag's OPC path (this historian export drops the station number's leading digit) - a strong signal).

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| St049 Window End 135 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St049_WindowEnd_135` | mm | 0.75 | numeric_suffix |
| St049 Window Start 24 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St049_WindowStart_24` | mm | 0.75 | numeric_suffix |
| St049 Reset Average Calculation | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St049_ResetAverageCalculation` | - | 0.75 | numeric_suffix |
| St049 Window End 24 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St049_WindowEnd_24` | mm | 0.75 | numeric_suffix |
| St049 Window Start 135 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St049_WindowStart_135` | mm | 0.75 | numeric_suffix |
| St049 Avg Diag Signal Pos | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St049_AvgDiagSignalPos[x].St049_AvgDiagSignalPos[3]` | mm | 0.75 | numeric_suffix |
| St049 Diag Signal Pos Lane3 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St049_DiagSignalPos_Lane3` | mm | 0.75 | numeric_suffix |
| St049 Diag Signal Pos Lane4 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St049_DiagSignalPos_Lane4` | mm | 0.75 | numeric_suffix |
| St049 Diag Signal Pos Lane1 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St049_DiagSignalPos_Lane1` | mm | 0.75 | numeric_suffix |
| St049 Min Diag Signal Pos | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St049_MinDiagSignalPos[x].St049_MinDiagSignalPos[2]` | mm | 0.75 | numeric_suffix |
| St049 Diag Signal Pos Lane2 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St049_DiagSignalPos_Lane2` | mm | 0.75 | numeric_suffix |
| St049 Max Diag Signal Pos | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St049_MaxDiagSignalPos[x].St049_MaxDiagSignalPos[5]` | mm | 0.75 | numeric_suffix |
| St049 Diag Signal Pos Lane5 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St049_DiagSignalPos_Lane5` | mm | 0.75 | numeric_suffix |
| St049 Preset Lane24 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St049_PresetLane24` | - | 0.75 | numeric_suffix |
| St049 Preset Lane135 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St049_PresetLane135` | - | 0.75 | numeric_suffix |

### Arrow Printing (2050)

- 120 candidate tag(s) considered -> 40 kept as genuine parameters (33%).
- Kept tags found by: 40 via *numeric_suffix* (the station's numeric code's last 3 digits matched a truncated St0*<digits> token in the tag's OPC path (this historian export drops the station number's leading digit) - a strong signal).

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| St050 Printing Trigger Pos Setting Wizard Value Basis | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St050_Printing_TriggerPosSettingWizardValueBasis[x].St050_Printing_TriggerPosSettingWizardValueBasis[2]` | mm | 0.75 | numeric_suffix |
| St050 Printing Challenge Test Start Offset | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St050_Printing_ChallengeTestStartOffset[x].St050_Printing_ChallengeTestStartOffset[1]` | mm | 0.75 | numeric_suffix |
| St050 Printing Challenge Test Repeat | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St050_Printing_ChallengeTestRepeat` | - | 0.75 | numeric_suffix |
| St050 Printing Web Pos Set Point | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St050_Printing_WebPosSetPoint[x].St050_Printing_WebPosSetPoint[2]` | mm | 0.75 | numeric_suffix |
| St050 Printing Trigger Pos Setting Wizard Enable | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St050_Printing_TriggerPosSettingWizardEnable[x].St050_Printing_TriggerPosSettingWizardEnable[1]` | - | 0.75 | numeric_suffix |
| St050 Cross Travel Working Pos Vel | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St050_CrossTravel_WorkingPosVel` | mm/s | 0.75 | numeric_suffix |
| St050 Printing Trigger Enable | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St050_Printing_TriggerEnable[x].St050_Printing_TriggerEnable[1][1]` | - | 0.75 | numeric_suffix |
| St050 Cross Travel Basic Pos | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St050_CrossTravel_BasicPos` | mm/s | 0.75 | numeric_suffix |
| St050 Printing Trigger Pos Setting Wizard Value | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St050_Printing_TriggerPosSettingWizardValue[x].St050_Printing_TriggerPosSettingWizardValue[1]` | mm | 0.75 | numeric_suffix |
| St050 Printing Trigger Pos Dead Time | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St050_Printing_TriggerPos_DeadTime[x].St050_Printing_TriggerPos_DeadTime[1]` | s | 0.75 | numeric_suffix |
| St050 Printer Enable | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St050_Printer_Enable[x].St050_Printer_Enable[2]` | - | 0.75 | numeric_suffix |
| St050 Cross Travel Working Pos | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St050_CrossTravel_WorkingPos` | mm/s | 0.75 | numeric_suffix |
| St050 Printing Web Pos Sensor Offset | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St050_Printing_WebPosSensorOffset[x].St050_Printing_WebPosSensorOffset[2]` | mm | 0.75 | numeric_suffix |
| St050 Printing Web Pos Trigger Pos Auto Corr On | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St050_Printing_WebPosTriggerPosAutoCorrOn[x].St050_Printing_WebPosTriggerPosAutoCorrOn[2]` | - | 0.75 | numeric_suffix |
| St050 Printing Trigger Pos Setting Wizard Value Set | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St050_Printing_TriggerPosSettingWizardValueSet[x].St050_Printing_TriggerPosSettingWizardValueSet[2]` | mm | 0.75 | numeric_suffix |
| St050 Printing Web Pos Deviation Max | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St050_Printing_WebPosDeviationMax[x].St050_Printing_WebPosDeviationMax[1]` | mm | 0.75 | numeric_suffix |
| St050 Printing Trigger Pos | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St050_Printing_TriggerPos[x].St050_Printing_TriggerPos[1][2]` | mm | 0.75 | numeric_suffix |
| St050 Cross Travel Service Pos | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St050_CrossTravel_ServicePos` | mm/s | 0.75 | numeric_suffix |
| St050 Cross Travel Basic Pos Vel | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St050_CrossTravel_BasicPosVel` | mm/s | 0.75 | numeric_suffix |
| St050 Cross Travel Service Pos Vel | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St050_CrossTravel_ServicePosVel` | mm/s | 0.75 | numeric_suffix |
| St050 Printing Challenge Test On | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St050_Printing_ChallengeTestOn` | - | 0.75 | numeric_suffix |
| St050 Printing Web Pos Act Value | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St050_Printing_WebPosActValue[x].St050_Printing_WebPosActValue[1]` | mm | 0.75 | numeric_suffix |
| St050 Printing Trigger Pos Out Of Range Error Num | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St050_Printing_TriggerPos_OutOfRange_Error_Num[x].St050_Printing_TriggerPos_OutOfRange_Error_Num[1]` | mm | 0.75 | numeric_suffix |
| St050 Cross Travel Service Pos Reached | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St050_CrossTravel_ServicePosReached` | - | 0.75 | numeric_suffix |
| St050 Printing Web Pos Act Value Valid | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St050_Printing_WebPosActValueValid[x].St050_Printing_WebPosActValueValid[2]` | - | 0.75 | numeric_suffix |
| St050 Cross Travel Working Pos Reached | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St050_CrossTravel_WorkingPosReached` | - | 0.75 | numeric_suffix |
| St050 Cross Travel Basic Pos Reached | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St050_CrossTravel_BasicPosReached` | - | 0.75 | numeric_suffix |
| St050 Printing Web Pos Deviation O K | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St050_Printing_WebPosDeviationOK[x].St050_Printing_WebPosDeviationOK[1]` | - | 0.75 | numeric_suffix |
| St050 Printing Web Pos Deviation | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St050_Printing_WebPosDeviation[x].St050_Printing_WebPosDeviation[1]` | mm | 0.75 | numeric_suffix |
| St050 Printing Challenge Test Cycle Count | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St050_Printing_ChallengeTestCycleCount` | count | 0.75 | numeric_suffix |
| St050 Printing Trigger Pos Out Of Range Error Txt | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St050_Printing_TriggerPos_OutOfRange_Error_Txt[x].St050_Printing_TriggerPos_OutOfRange_Error_Txt[2]` | mm | 0.75 | numeric_suffix |
| St050 Cross Travel One Working Cycle Positioning Manually | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St050_CrossTravel_OneWorkingCyclePositioningManually` | mm/s | 0.75 | numeric_suffix |
| St050 Cross Travel Basic Pos Positioning Manually | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St050_CrossTravel_BasicPosPositioningManually` | mm/s | 0.75 | numeric_suffix |
| St050 Cross Travel Working Pos Positioning Manually | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St050_CrossTravel_WorkingPosPositioningManually` | mm/s | 0.75 | numeric_suffix |
| St050 Job Nr | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St050_JobNr` | - | 0.75 | numeric_suffix |
| St050 Cross Travel Service Pos Positioning Manually | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St050_CrossTravel_ServicePosPositioningManually` | mm/s | 0.75 | numeric_suffix |
| St050 Use Vacuum Strips | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St050_UseVacuumStrips` | - | 0.75 | numeric_suffix |
| St050 Inch One Mode | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St050_InchOneMode[x].St050_InchOneMode[11]` | - | 0.75 | numeric_suffix |
| St050 Job Name | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St050_JobName[x].St050_JobName[9]` | - | 0.75 | numeric_suffix |
| St050 Print Data | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St050_PrintData[x].St050_PrintData[13]` | - | 0.75 | numeric_suffix |

### Bottom Foil Pull Rollers (2051)

- 50 candidate tag(s) considered -> 34 kept as genuine parameters (68%).
- Kept tags found by: 34 via *numeric_suffix* (the station's numeric code's last 3 digits matched a truncated St0*<digits> token in the tag's OPC path (this historian export drops the station number's leading digit) - a strong signal).

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| St051 Vel Offset Lane1 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St051_VelOffset_Lane1` | mm/s | 0.75 | numeric_suffix |
| St051 Pressure Tol Plus Dancer | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St051_PressureTolPlus_Dancer` | bar | 0.75 | numeric_suffix |
| St051 P M Controlling | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St051_PM_Controlling` | - | 0.75 | numeric_suffix |
| St051 Pressure Tol Minus Dancer | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St051_PressureTolMinus_Dancer` | bar | 0.75 | numeric_suffix |
| St051 Reset Remanent Controller Values | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St051_ResetRemanentControllerValues` | - | 0.75 | numeric_suffix |
| St051 Dancer Pos Setpoint | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St051_DancerPosSetpoint` | mm | 0.75 | numeric_suffix |
| St051 Pressure Set Point Pull Rolls | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St051_PressureSetPoint_PullRolls` | bar | 0.75 | numeric_suffix |
| St051 Pressure Set Point Dancer | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St051_PressureSetPoint_Dancer` | bar | 0.75 | numeric_suffix |
| St051 Label Position Setpoint | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St051_LabelPositionSetpoint` | mm | 0.75 | numeric_suffix |
| St051 Pressure Tol Minus Pull Rolls | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St051_PressureTolMinus_PullRolls` | bar | 0.75 | numeric_suffix |
| St051 Pressure Tol Plus Pull Rolls | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St051_PressureTolPlus_PullRolls` | bar | 0.75 | numeric_suffix |
| St051 Dancer Pos Min | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St051_DancerPosMin` | mm | 0.75 | numeric_suffix |
| St051 Actual Pos Control Deviation | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St051_ActualPosControlDeviation` | mm | 0.75 | numeric_suffix |
| St051 Act Job Name | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St051_ActJobName` | - | 0.75 | numeric_suffix |
| St051 Pressure Act Val Per Cent Dancer | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St051_PressureActValPerCentDancer` | bar | 0.75 | numeric_suffix |
| St051 Pm Len Act Val | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St051_PmLenActVal` | - | 0.75 | numeric_suffix |
| St051 Pressure Act Val Per Cent Pull Rolls | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St051_PressureActValPerCentPullRolls` | bar | 0.75 | numeric_suffix |
| St051 Pressure Act Val Pull Rolls | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St051_PressureActValPullRolls` | bar | 0.75 | numeric_suffix |
| St051 Printer State | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St051_PrinterState` | - | 0.75 | numeric_suffix |
| St051 Dancer Pos Act | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St051_DancerPosAct` | mm | 0.75 | numeric_suffix |
| St051 Actual Controller Value | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St051_ActualControllerValue` | - | 0.75 | numeric_suffix |
| St051 Dancer Pos Act Per Cent | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St051_DancerPosActPerCent` | mm | 0.75 | numeric_suffix |
| St051 Actual Remanent Controller Value | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St051_ActualRemanentControllerValue` | - | 0.75 | numeric_suffix |
| St051 Control Done | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St051_ControlDone` | - | 0.75 | numeric_suffix |
| St051 Current Process Time | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St051_CurrentProcessTime` | s | 0.75 | numeric_suffix |
| St051 Dancer Pos Max | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St051_DancerPosMax` | mm | 0.75 | numeric_suffix |
| St051 Dancer Pos Mid | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St051_DancerPosMid` | mm | 0.75 | numeric_suffix |
| St051 Pressure Act Val Dancer | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St051_PressureActVal_Dancer` | bar | 0.75 | numeric_suffix |
| St051 Man Open Lane1 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St051_ManOpen_Lane1` | - | 0.75 | numeric_suffix |
| St051 Tool Circumference | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St051_ToolCircumference` | mm | 0.75 | numeric_suffix |
| St051 Man Close Lane1 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St051_ManClose_Lane1` | - | 0.75 | numeric_suffix |
| St051 Inch One Mode | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St051_InchOneMode[x].St051_InchOneMode[9]` | - | 0.75 | numeric_suffix |
| St051 Release Calibrate Dancer | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St051_ReleaseCalibrateDancer` | - | 0.75 | numeric_suffix |
| St051 Calibrate Dancer | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St051_CalibrateDancer` | - | 0.75 | numeric_suffix |

### Thumb Hole Punching (2053)

- 4 candidate tag(s) considered -> 0 kept as genuine parameters (0%).

_No genuine parameters found among this station's candidates._

### Bottom Foil Pull Rollers 2 (2055)

- 29 candidate tag(s) considered -> 13 kept as genuine parameters (45%).
- Kept tags found by: 13 via *numeric_suffix* (the station's numeric code's last 3 digits matched a truncated St0*<digits> token in the tag's OPC path (this historian export drops the station number's leading digit) - a strong signal).

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| St055 Pressure Tol Minus Pull Rolls | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St055_PressureTolMinus_PullRolls` | bar | 0.75 | numeric_suffix |
| St055 Pressure Tol Plus Pull Rolls | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St055_PressureTolPlus_PullRolls` | bar | 0.75 | numeric_suffix |
| St055 Reset Memory | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St055_ResetMemory` | - | 0.75 | numeric_suffix |
| St055 Vel Offset Lane1 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St055_VelOffset_Lane1` | mm/s | 0.75 | numeric_suffix |
| St055 Pressure Set Point Pull Rolls | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St055_PressureSetPoint_PullRolls` | bar | 0.75 | numeric_suffix |
| St055 act Status | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St055_actStatus` | - | 0.75 | numeric_suffix |
| St055 Pressure Act Val Per Cent Pull Rolls | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St055_PressureActValPerCentPullRolls` | bar | 0.75 | numeric_suffix |
| St055 Pressure Act Val Pull Rolls | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St055_PressureActValPullRolls` | bar | 0.75 | numeric_suffix |
| St055 Control Done | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St055_ControlDone` | - | 0.75 | numeric_suffix |
| St055 Tool Circumference | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St055_ToolCircumference` | mm | 0.75 | numeric_suffix |
| St055 Man Open Lane1 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St055_ManOpen_Lane1` | - | 0.75 | numeric_suffix |
| St055 Inch One Mode | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St055_InchOneMode[x].St055_InchOneMode[11]` | - | 0.75 | numeric_suffix |
| St055 Man Close Lane1 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St055_ManClose_Lane1` | - | 0.75 | numeric_suffix |

### Splice Detection Bottom Foil (2056)

- 12 candidate tag(s) considered -> 8 kept as genuine parameters (67%).
- Kept tags found by: 8 via *numeric_suffix* (the station's numeric code's last 3 digits matched a truncated St0*<digits> token in the tag's OPC path (this historian export drops the station number's leading digit) - a strong signal).

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| St056 Reset Splice Existent | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St056_ResetSpliceExistent` | - | 0.75 | numeric_suffix |
| St056 Tolerance Window | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St056_ToleranceWindow` | mm | 0.75 | numeric_suffix |
| St056 Distance To Winder | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St056_DistanceToWinder` | mm | 0.75 | numeric_suffix |
| St056 Zero Point | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St056_ZeroPoint` | - | 0.75 | numeric_suffix |
| St056 Splice End Pos | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St056_SpliceEndPos` | mm | 0.75 | numeric_suffix |
| St056 Splice Expected1 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St056_SpliceExpected1` | - | 0.75 | numeric_suffix |
| St056 Splice Start Pos | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St056_SpliceStartPos` | mm | 0.75 | numeric_suffix |
| St056 Splice Check Rest Distance1 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St056_SpliceCheckRestDistance1` | mm | 0.75 | numeric_suffix |

### Rotary Sealing (2057)

- 63 candidate tag(s) considered -> 47 kept as genuine parameters (75%).
- Kept tags found by: 47 via *numeric_suffix* (the station's numeric code's last 3 digits matched a truncated St0*<digits> token in the tag's OPC path (this historian export drops the station number's leading digit) - a strong signal).

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| St057 Print Mark Adjustment O N | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St057_PrintMarkAdjustmentON` | - | 0.75 | numeric_suffix |
| St057 Pressure Set Point Front | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St057_PressureSetPoint_Front` | bar | 0.75 | numeric_suffix |
| St057 Temperature Tol Minus | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St057_TemperatureTolMinus` | °C | 0.75 | numeric_suffix |
| St057 Pressure Tol Minus | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St057_PressureTolMinus` | bar | 0.75 | numeric_suffix |
| St057 Pressure Set Point Back | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St057_PressureSetPoint_Back` | bar | 0.75 | numeric_suffix |
| St057 Print Mark Adjustment K P | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St057_PrintMarkAdjustment_KP` | - | 0.75 | numeric_suffix |
| St057 Print Mark Adjustment Position Set Point | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St057_PrintMarkAdjustment_PositionSetPoint` | mm | 0.75 | numeric_suffix |
| St057 Temperature Set Point | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St057_TemperatureSetPoint` | °C | 0.75 | numeric_suffix |
| St057 Temperature Tol Plus | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St057_TemperatureTolPlus` | °C | 0.75 | numeric_suffix |
| St057 Burned Time | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St057_BurnedTime` | s | 0.75 | numeric_suffix |
| St057 Sync Vel Offset | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St057_SyncVelOffset` | mm/s | 0.75 | numeric_suffix |
| St057 Pressure Set Point After Start Up Back | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St057_PressureSetPointAfterStartUp_Back` | bar | 0.75 | numeric_suffix |
| St057 Print Mark Position Set Point | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St057_PrintMarkPositionSetPoint` | mm | 0.75 | numeric_suffix |
| St057 Pressure Set Point After Start Up Front | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St057_PressureSetPointAfterStartUp_Front` | bar | 0.75 | numeric_suffix |
| St057 Pos Offset | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St057_PosOffset` | mm | 0.75 | numeric_suffix |
| St057 Cycles Before Pressure Change | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St057_CyclesBeforePressureChange` | bar | 0.75 | numeric_suffix |
| St057 Pressure Tol Plus | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St057_PressureTolPlus` | bar | 0.75 | numeric_suffix |
| St057 Print Mark Adjustment Tolerance | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St057_PrintMarkAdjustment_Tolerance` | - | 0.75 | numeric_suffix |
| St057 Tol Minus P M | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St057_TolMinus_PM` | - | 0.75 | numeric_suffix |
| St057 Tol Plus P M | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St057_TolPlus_PM` | - | 0.75 | numeric_suffix |
| St057 Start Force Measurement | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St057_StartForceMeasurement` | N | 0.75 | numeric_suffix |
| St057 Pressure Act Val Front | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St057_PressureActValFront` | bar | 0.75 | numeric_suffix |
| St057 Pressure Act Val Per Cent Back | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St057_PressureActValPerCentBack` | bar | 0.75 | numeric_suffix |
| St057 Actual Force Front | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St057_ActualForce_Front` | N | 0.75 | numeric_suffix |
| St057 Pressure Act Val Per Cent Front | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St057_PressureActValPerCentFront` | bar | 0.75 | numeric_suffix |
| St057 Le Pos | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St057_LePos` | mm | 0.75 | numeric_suffix |
| St057 Actual Force Back | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St057_ActualForce_Back` | N | 0.75 | numeric_suffix |
| St057 Print Mark Act Pos | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St057_PrintMarkActPos` | mm | 0.75 | numeric_suffix |
| St057 Temperature Act Val Guard Plate | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St057_TemperatureActValGuardPlate` | °C | 0.75 | numeric_suffix |
| St057 Temperature Act Val Suspension | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St057_TemperatureActValSuspension` | °C | 0.75 | numeric_suffix |
| St057 Pressure Act Val Back | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St057_PressureActValBack` | bar | 0.75 | numeric_suffix |
| St057 Move To Safe Pos | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St057_MoveToSafePos` | mm | 0.75 | numeric_suffix |
| St057 Vertical Production Pos | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St057_VerticalProductionPos` | mm | 0.75 | numeric_suffix |
| St057 Man Close | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St057_ManClose` | - | 0.75 | numeric_suffix |
| St057 Man Open | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St057_ManOpen` | - | 0.75 | numeric_suffix |
| St057 Num Cutting Edges | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St057_NumCuttingEdges` | - | 0.75 | numeric_suffix |
| St057 Cylinder 11 1 Man In | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St057_Cylinder_11_1_ManIn` | - | 0.75 | numeric_suffix |
| St057 Sync Dist | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St057_SyncDist` | - | 0.75 | numeric_suffix |
| St057 Vertical Stop Pos | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St057_VerticalStopPos` | mm | 0.75 | numeric_suffix |
| St057 Move To Setpoint | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St057_MoveToSetpoint` | - | 0.75 | numeric_suffix |
| St057 Tool Circumference2 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St057_ToolCircumference2` | mm | 0.75 | numeric_suffix |
| St057 Tool Circumference | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St057_ToolCircumference` | mm | 0.75 | numeric_suffix |
| St057 Heat Plate Man Out | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St057_HeatPlate_ManOut` | - | 0.75 | numeric_suffix |
| St057 Start Calib Procedure | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St057_StartCalibProcedure` | - | 0.75 | numeric_suffix |
| St057 Cylinder 11 1 Man Out | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St057_Cylinder_11_1_ManOut` | - | 0.75 | numeric_suffix |
| St057 Inch One Mode | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St057_InchOneMode[x].St057_InchOneMode[8]` | - | 0.75 | numeric_suffix |
| St057 Heat Plate Man In | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St057_HeatPlate_ManIn` | - | 0.75 | numeric_suffix |

### Pack Pull Rollers (2059)

- 27 candidate tag(s) considered -> 11 kept as genuine parameters (41%).
- Kept tags found by: 11 via *numeric_suffix* (the station's numeric code's last 3 digits matched a truncated St0*<digits> token in the tag's OPC path (this historian export drops the station number's leading digit) - a strong signal).

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| St059 Vel Offset | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St059_VelOffset` | mm/s | 0.75 | numeric_suffix |
| St059 Pressure Set Point Pull Rolls | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St059_PressureSetPoint_PullRolls` | bar | 0.75 | numeric_suffix |
| St059 Pressure Tol Minus Pull Rolls | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St059_PressureTolMinus_PullRolls` | bar | 0.75 | numeric_suffix |
| St059 Pressure Tol Plus Pull Rolls | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St059_PressureTolPlus_PullRolls` | bar | 0.75 | numeric_suffix |
| St059 Pressure Act Val Per Cent Pull Rolls | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St059_PressureActValPerCentPullRolls` | bar | 0.75 | numeric_suffix |
| St059 act Status | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St059_actStatus` | - | 0.75 | numeric_suffix |
| St059 Pressure Act Val Pull Rolls | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St059_PressureActValPullRolls` | bar | 0.75 | numeric_suffix |
| St059 Inch One Mode | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St059_InchOneMode[x].St059_InchOneMode[1]` | - | 0.75 | numeric_suffix |
| St059 Man Close | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St059_ManClose` | - | 0.75 | numeric_suffix |
| St059 Tool Circumference | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St059_ToolCircumference` | mm | 0.75 | numeric_suffix |
| St059 Man Open | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St059_ManOpen` | - | 0.75 | numeric_suffix |

### Detection Sealing Area (2060)

- 64 candidate tag(s) considered -> 60 kept as genuine parameters (94%).
- Kept tags found by: 55 via *numeric_suffix* (the station's numeric code's last 3 digits matched a truncated St0*<digits> token in the tag's OPC path (this historian export drops the station number's leading digit) - a strong signal), 5 via *keyword* (only a descriptive word from the station's name matched the tag's path/name - a weaker signal).

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| Arrow Lane3 Blob Area | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St048_2B1_CameraData.ArrowLane3_Blob_Area` | - | 0.50 | keyword |
| Arrow Lane2 Blob Area | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St048_1B1_CameraData.ArrowLane2_Blob_Area` | - | 0.50 | keyword |
| Arrow Lane1 Blob Area | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St048_1B1_CameraData.ArrowLane1_Blob_Area` | - | 0.50 | keyword |
| Arrow Lane5 Blob Area | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St048_3B1_CameraData.ArrowLane5_Blob_Area` | - | 0.50 | keyword |
| Arrow Lane4 Blob Area | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St048_3B1_CameraData.ArrowLane4_Blob_Area` | - | 0.50 | keyword |
| St060 Catheter Height Limit | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St060_CatheterHeightLimit` | - | 0.75 | numeric_suffix |
| St060 Window Start Insert Area 135 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St060_WindowStartInsertArea_135` | mm | 0.75 | numeric_suffix |
| St060 Funnel Height Limit | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St060_FunnelHeightLimit` | - | 0.75 | numeric_suffix |
| St060 Window End 135 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St060_WindowEnd_135` | mm | 0.75 | numeric_suffix |
| St060 Station Trend Selection 2 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St060_StationTrendSelection_2` | - | 0.75 | numeric_suffix |
| St060 Insert Area Height Limit | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St060_InsertAreaHeightLimit` | - | 0.75 | numeric_suffix |
| St060 Window End Funnel 135 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St060_WindowEndFunnel_135` | mm | 0.75 | numeric_suffix |
| St060 Window Start 24 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St060_WindowStart_24` | mm | 0.75 | numeric_suffix |
| St060 Window End Insert Area 24 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St060_WindowEndInsertArea_24` | mm | 0.75 | numeric_suffix |
| St060 Window End Insert Area 135 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St060_WindowEndInsertArea_135` | mm | 0.75 | numeric_suffix |
| St060 Window End 24 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St060_WindowEnd_24` | mm | 0.75 | numeric_suffix |
| St060 Window Start Funnel 24 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St060_WindowStartFunnel_24` | mm | 0.75 | numeric_suffix |
| St060 Window Start 135 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St060_WindowStart_135` | mm | 0.75 | numeric_suffix |
| St060 Window Start Funnel 135 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St060_WindowStartFunnel_135` | mm | 0.75 | numeric_suffix |
| St060 Window Start Insert Area 24 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St060_WindowStartInsertArea_24` | mm | 0.75 | numeric_suffix |
| St060 Window End Funnel 24 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St060_WindowEndFunnel_24` | mm | 0.75 | numeric_suffix |
| St060 Station Trend Selection 1 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St060_StationTrendSelection_1` | - | 0.75 | numeric_suffix |
| St060 Trend Shown Pos | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St060_TrendShownPos` | mm | 0.75 | numeric_suffix |
| St060 Height Lane2 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St060_HeightLane2` | - | 0.75 | numeric_suffix |
| St060 Height Lane3 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St060_HeightLane3` | - | 0.75 | numeric_suffix |
| St060 Height Lane4 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St060_HeightLane4` | - | 0.75 | numeric_suffix |
| St060 Height Lane5 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St060_HeightLane5` | - | 0.75 | numeric_suffix |
| St060 Height Lane1 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St060_HeightLane1` | - | 0.75 | numeric_suffix |
| St060 Start Calib Min Lane2 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St060_StartCalibMin_Lane2` | - | 0.75 | numeric_suffix |
| St060 Start Calib Max Lane1 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St060_StartCalibMax_Lane1` | - | 0.75 | numeric_suffix |
| St060 Max Calib Lane4 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St060_MaxCalib_Lane4` | - | 0.75 | numeric_suffix |
| St060 Max Calib Input Lane5 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St060_MaxCalibInput_Lane5` | - | 0.75 | numeric_suffix |
| St060 Min Calib Lane4 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St060_MinCalib_Lane4` | - | 0.75 | numeric_suffix |
| St060 Max Calib Lane5 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St060_MaxCalib_Lane5` | - | 0.75 | numeric_suffix |
| St060 Max Calib Lane2 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St060_MaxCalib_Lane2` | - | 0.75 | numeric_suffix |
| St060 Start Calib Max Lane2 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St060_StartCalibMax_Lane2` | - | 0.75 | numeric_suffix |
| St060 Min Calib Lane3 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St060_MinCalib_Lane3` | - | 0.75 | numeric_suffix |
| St060 Start Calib Max Lane3 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St060_StartCalibMax_Lane3` | - | 0.75 | numeric_suffix |
| St060 Max Calib Input Lane4 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St060_MaxCalibInput_Lane4` | - | 0.75 | numeric_suffix |
| St060 Start Calib Max Lane5 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St060_StartCalibMax_Lane5` | - | 0.75 | numeric_suffix |
| St060 Min Calib Input Lane1 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St060_MinCalibInput_Lane1` | - | 0.75 | numeric_suffix |
| St060 Max Calib Input Lane2 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St060_MaxCalibInput_Lane2` | - | 0.75 | numeric_suffix |
| St060 Min Calib Input Lane4 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St060_MinCalibInput_Lane4` | - | 0.75 | numeric_suffix |
| St060 Start Calib Max Lane4 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St060_StartCalibMax_Lane4` | - | 0.75 | numeric_suffix |
| St060 Min Calib Input Lane3 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St060_MinCalibInput_Lane3` | - | 0.75 | numeric_suffix |
| St060 Start Calib Min Lane3 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St060_StartCalibMin_Lane3` | - | 0.75 | numeric_suffix |
| St060 Min Calib Input Lane2 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St060_MinCalibInput_Lane2` | - | 0.75 | numeric_suffix |
| St060 Max Calib Input Lane3 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St060_MaxCalibInput_Lane3` | - | 0.75 | numeric_suffix |
| St060 Min Calib Lane1 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St060_MinCalib_Lane1` | - | 0.75 | numeric_suffix |
| St060 Scroll Trend Negative | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St060_ScrollTrendNegative` | - | 0.75 | numeric_suffix |
| St060 Min Calib Lane2 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St060_MinCalib_Lane2` | - | 0.75 | numeric_suffix |
| St060 Start Calib Min Lane4 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St060_StartCalibMin_Lane4` | - | 0.75 | numeric_suffix |
| St060 Max Calib Lane1 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St060_MaxCalib_Lane1` | - | 0.75 | numeric_suffix |
| St060 Min Calib Input Lane5 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St060_MinCalibInput_Lane5` | - | 0.75 | numeric_suffix |
| St060 Start Calib Min Lane1 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St060_StartCalibMin_Lane1` | - | 0.75 | numeric_suffix |
| St060 Max Calib Input Lane1 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St060_MaxCalibInput_Lane1` | - | 0.75 | numeric_suffix |
| St060 Scroll Trend Positive | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St060_ScrollTrendPositive` | mm | 0.75 | numeric_suffix |
| St060 Min Calib Lane5 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St060_MinCalib_Lane5` | - | 0.75 | numeric_suffix |
| St060 Max Calib Lane3 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St060_MaxCalib_Lane3` | - | 0.75 | numeric_suffix |
| St060 Start Calib Min Lane5 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St060_StartCalibMin_Lane5` | - | 0.75 | numeric_suffix |

### Pack Cooling (2061)

- 20 candidate tag(s) considered -> 4 kept as genuine parameters (20%).
- Kept tags found by: 4 via *numeric_suffix* (the station's numeric code's last 3 digits matched a truncated St0*<digits> token in the tag's OPC path (this historian export drops the station number's leading digit) - a strong signal).

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| St061 Dead Time | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St061_DeadTime` | s | 0.75 | numeric_suffix |
| St061 Window End | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St061_WindowEnd` | mm | 0.75 | numeric_suffix |
| St061 Window Start | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St061_WindowStart` | mm | 0.75 | numeric_suffix |
| St061 Inch One Mode | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St061_InchOneMode[x].St061_InchOneMode[11]` | - | 0.75 | numeric_suffix |

### Detection of Filled Pouches (2062)

- 14 candidate tag(s) considered -> 10 kept as genuine parameters (71%).
- Kept tags found by: 10 via *numeric_suffix* (the station's numeric code's last 3 digits matched a truncated St0*<digits> token in the tag's OPC path (this historian export drops the station number's leading digit) - a strong signal).

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| St062 Window Start 135 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St062_WindowStart_135` | mm | 0.75 | numeric_suffix |
| St062 Catheter Height Presence Control | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St062_CatheterHeightPresenceControl` | - | 0.75 | numeric_suffix |
| St062 Window End 24 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St062_WindowEnd_24` | mm | 0.75 | numeric_suffix |
| St062 Window Start 24 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St062_WindowStart_24` | mm | 0.75 | numeric_suffix |
| St062 Window End 135 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St062_WindowEnd_135` | mm | 0.75 | numeric_suffix |
| St062 Diag Signal Pos Lane4 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St062_DiagSignalPos_Lane4` | mm | 0.75 | numeric_suffix |
| St062 Diag Signal Pos Lane2 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St062_DiagSignalPos_Lane2` | mm | 0.75 | numeric_suffix |
| St062 Diag Signal Pos Lane3 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St062_DiagSignalPos_Lane3` | mm | 0.75 | numeric_suffix |
| St062 Diag Signal Pos Lane1 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St062_DiagSignalPos_Lane1` | mm | 0.75 | numeric_suffix |
| St062 Diag Signal Pos Lane5 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St062_DiagSignalPos_Lane5` | mm | 0.75 | numeric_suffix |

### Pack Pull Rollers 2 (2063)

- 33 candidate tag(s) considered -> 17 kept as genuine parameters (52%).
- Kept tags found by: 17 via *numeric_suffix* (the station's numeric code's last 3 digits matched a truncated St0*<digits> token in the tag's OPC path (this historian export drops the station number's leading digit) - a strong signal).

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| St063 Reset Memory | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St063_ResetMemory` | - | 0.75 | numeric_suffix |
| St063 Current Target | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St063_CurrentTarget` | - | 0.75 | numeric_suffix |
| St063 Pressure Set Point Pull Rolls | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St063_PressureSetPoint_PullRolls` | bar | 0.75 | numeric_suffix |
| St063 Vel Offset Lane1 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St063_VelOffset_Lane1` | mm/s | 0.75 | numeric_suffix |
| St063 Pressure Tol Minus Pull Rolls | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St063_PressureTolMinus_PullRolls` | bar | 0.75 | numeric_suffix |
| St063 Pressure Tol Plus Pull Rolls | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St063_PressureTolPlus_PullRolls` | bar | 0.75 | numeric_suffix |
| St063 Current Target Without Cutting | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St063_CurrentTargetWithoutCutting` | - | 0.75 | numeric_suffix |
| St063 Pressure Act Val Pull Rolls | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St063_PressureActValPullRolls` | bar | 0.75 | numeric_suffix |
| St063 Print Mark Act Pos Lane1 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St063_PrintMarkActPos_Lane1` | mm | 0.75 | numeric_suffix |
| St063 Pressure Act Val Per Cent Pull Rolls | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St063_PressureActValPerCentPullRolls` | bar | 0.75 | numeric_suffix |
| St063 act Status | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St063_actStatus` | - | 0.75 | numeric_suffix |
| St063 Current Average | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St063_CurrentAverage` | - | 0.75 | numeric_suffix |
| St063 Print Mark Act Length Lane1 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St063_PrintMarkActLength_Lane1` | - | 0.75 | numeric_suffix |
| St063 Tool Circumference | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St063_ToolCircumference` | mm | 0.75 | numeric_suffix |
| St063 Inch One Mode | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St063_InchOneMode[x].St063_InchOneMode[6]` | - | 0.75 | numeric_suffix |
| St063 Man Open | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St063_ManOpen` | - | 0.75 | numeric_suffix |
| St063 Man Close | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St063_ManClose` | - | 0.75 | numeric_suffix |

### Pack Advance (2065)

- 11 candidate tag(s) considered -> 7 kept as genuine parameters (64%).
- Kept tags found by: 7 via *numeric_suffix* (the station's numeric code's last 3 digits matched a truncated St0*<digits> token in the tag's OPC path (this historian export drops the station number's leading digit) - a strong signal).

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| St065 Pressure Tol Minus Pull Rolls | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St065_PressureTolMinus_PullRolls` | bar | 0.75 | numeric_suffix |
| St065 Pressure Set Point Pull Rolls | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St065_PressureSetPoint_PullRolls` | bar | 0.75 | numeric_suffix |
| St065 Pressure Tol Plus Pull Rolls | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St065_PressureTolPlus_PullRolls` | bar | 0.75 | numeric_suffix |
| St065 Pressure Act Val Pull Rolls | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St065_PressureActValPullRolls` | bar | 0.75 | numeric_suffix |
| St065 Pressure Act Val Per Cent Pull Rolls | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St065_PressureActValPerCentPullRolls` | bar | 0.75 | numeric_suffix |
| St065 Man Open | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St065_ManOpen` | - | 0.75 | numeric_suffix |
| St065 Man Close | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St065_ManClose` | - | 0.75 | numeric_suffix |

### Pack Contour Cut (2067)

- 46 candidate tag(s) considered -> 30 kept as genuine parameters (65%).
- Kept tags found by: 30 via *numeric_suffix* (the station's numeric code's last 3 digits matched a truncated St0*<digits> token in the tag's OPC path (this historian export drops the station number's leading digit) - a strong signal).

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| St067 Pos Offset | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St067_PosOffset` | mm | 0.75 | numeric_suffix |
| St067 Print Mark Adjustment Position Set Point | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St067_PrintMarkAdjustment_PositionSetPoint` | mm | 0.75 | numeric_suffix |
| St067 Dead Time | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St067_DeadTime` | s | 0.75 | numeric_suffix |
| St067 Cutting Tool Reset Counter Female | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St067_CuttingToolResetCounterFemale` | count | 0.75 | numeric_suffix |
| St067 Print Mark Length Tolerance | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St067_PrintMarkLength_Tolerance` | - | 0.75 | numeric_suffix |
| St067 Print Mark Adjustment O N | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St067_PrintMarkAdjustmentON` | - | 0.75 | numeric_suffix |
| St067 Pressure Tol Plus | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St067_PressureTolPlus` | bar | 0.75 | numeric_suffix |
| St067 Zero Point | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St067_ZeroPoint` | - | 0.75 | numeric_suffix |
| St067 Sync Vel Offset | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St067_SyncVelOffset` | mm/s | 0.75 | numeric_suffix |
| St067 Print Mark Adjustment K P | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St067_PrintMarkAdjustment_KP` | - | 0.75 | numeric_suffix |
| St067 Window End | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St067_WindowEnd` | mm | 0.75 | numeric_suffix |
| St067 Print Mark Adjustment Tolerance | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St067_PrintMarkAdjustment_Tolerance` | - | 0.75 | numeric_suffix |
| St067 Window Start | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St067_WindowStart` | mm | 0.75 | numeric_suffix |
| St067 Cutting Tool Reset Counter Male | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St067_CuttingToolResetCounterMale` | count | 0.75 | numeric_suffix |
| St067 Pressure Set Point | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St067_PressureSetPoint` | bar | 0.75 | numeric_suffix |
| St067 Pressure Tol Minus | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St067_PressureTolMinus` | bar | 0.75 | numeric_suffix |
| St067 Pressure Act Val | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St067_PressureActVal` | bar | 0.75 | numeric_suffix |
| St067 Print Mark Position | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St067_PrintMarkPosition` | mm | 0.75 | numeric_suffix |
| St067 Print Mark Deviation | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St067_PrintMarkDeviation` | - | 0.75 | numeric_suffix |
| St067 Pressure Act Val Per Cent | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St067_PressureActValPerCent` | bar | 0.75 | numeric_suffix |
| St067 Le Pos | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St067_LePos` | mm | 0.75 | numeric_suffix |
| St067 Cutting Tool Nr Of Cuts Female | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St067_CuttingToolNrOfCutsFemale` | - | 0.75 | numeric_suffix |
| St067 Print Mark Length | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St067_PrintMarkLength` | - | 0.75 | numeric_suffix |
| St067 Cutting Tool Nr Of Cuts Male | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St067_CuttingToolNrOfCutsMale` | - | 0.75 | numeric_suffix |
| St067 Man Close | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St067_ManClose` | - | 0.75 | numeric_suffix |
| St067 Tool Circumference | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St067_ToolCircumference` | mm | 0.75 | numeric_suffix |
| St067 Sync Dist | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St067_SyncDist` | - | 0.75 | numeric_suffix |
| St067 Num Cutting Edges | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St067_NumCuttingEdges` | - | 0.75 | numeric_suffix |
| St067 Inch One Mode | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St067_InchOneMode[x].St067_InchOneMode[9]` | - | 0.75 | numeric_suffix |
| St067 Man Open | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St067_ManOpen` | - | 0.75 | numeric_suffix |

### Waste Grid Detection (2068)

- 4 candidate tag(s) considered -> 0 kept as genuine parameters (0%).

_No genuine parameters found among this station's candidates._

### Outfeed Belt 1 (2069)

- 20 candidate tag(s) considered -> 4 kept as genuine parameters (20%).
- Kept tags found by: 4 via *numeric_suffix* (the station's numeric code's last 3 digits matched a truncated St0*<digits> token in the tag's OPC path (this historian export drops the station number's leading digit) - a strong signal).

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| St069 Vel Offset | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St069_VelOffset` | mm/s | 0.75 | numeric_suffix |
| St069 act Status | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St069_actStatus` | - | 0.75 | numeric_suffix |
| St069 Tool Circumference | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St069_ToolCircumference` | mm | 0.75 | numeric_suffix |
| St069 Inch One Mode | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St069_InchOneMode[x].St069_InchOneMode[10]` | - | 0.75 | numeric_suffix |

### Pack Presence Check Outfeed (2070)

- 13 candidate tag(s) considered -> 9 kept as genuine parameters (69%).
- Kept tags found by: 9 via *numeric_suffix* (the station's numeric code's last 3 digits matched a truncated St0*<digits> token in the tag's OPC path (this historian export drops the station number's leading digit) - a strong signal).

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| St070 Window Start24 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St070_WindowStart24` | mm | 0.75 | numeric_suffix |
| St070 Window Start | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St070_WindowStart` | mm | 0.75 | numeric_suffix |
| St070 Window End24 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St070_WindowEnd24` | mm | 0.75 | numeric_suffix |
| St070 Window End | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St070_WindowEnd` | mm | 0.75 | numeric_suffix |
| St070 Diag Signal Pos Lane1 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St070_DiagSignalPos_Lane1` | mm | 0.75 | numeric_suffix |
| St070 Diag Signal Pos Lane2 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St070_DiagSignalPos_Lane2` | mm | 0.75 | numeric_suffix |
| St070 Diag Signal Pos Lane4 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St070_DiagSignalPos_Lane4` | mm | 0.75 | numeric_suffix |
| St070 Diag Signal Pos Lane5 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St070_DiagSignalPos_Lane5` | mm | 0.75 | numeric_suffix |
| St070 Diag Signal Pos Lane3 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St070_DiagSignalPos_Lane3` | mm | 0.75 | numeric_suffix |

### Pack Presence Check Before Reject (2071)

- 11 candidate tag(s) considered -> 7 kept as genuine parameters (64%).
- Kept tags found by: 7 via *numeric_suffix* (the station's numeric code's last 3 digits matched a truncated St0*<digits> token in the tag's OPC path (this historian export drops the station number's leading digit) - a strong signal).

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| St071 Window End | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St071_WindowEnd` | mm | 0.75 | numeric_suffix |
| St071 Window Start | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St071_WindowStart` | mm | 0.75 | numeric_suffix |
| St071 Diag Signal Pos Lane4 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St071_DiagSignalPos_Lane4` | mm | 0.75 | numeric_suffix |
| St071 Diag Signal Pos Lane5 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St071_DiagSignalPos_Lane5` | mm | 0.75 | numeric_suffix |
| St071 Diag Signal Pos Lane3 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St071_DiagSignalPos_Lane3` | mm | 0.75 | numeric_suffix |
| St071 Diag Signal Pos Lane1 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St071_DiagSignalPos_Lane1` | mm | 0.75 | numeric_suffix |
| St071 Diag Signal Pos Lane2 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St071_DiagSignalPos_Lane2` | mm | 0.75 | numeric_suffix |

### Pack Reject 1 (2073)

- 36 candidate tag(s) considered -> 20 kept as genuine parameters (56%).
- Kept tags found by: 20 via *numeric_suffix* (the station's numeric code's last 3 digits matched a truncated St0*<digits> token in the tag's OPC path (this historian export drops the station number's leading digit) - a strong signal).

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| St073 Window Start | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St073_WindowStart` | mm | 0.75 | numeric_suffix |
| St073 Vel Conveyor | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St073_Vel_Conveyor` | mm/s | 0.75 | numeric_suffix |
| St073 Station To Test | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St073_StationToTest` | - | 0.75 | numeric_suffix |
| St073 Window End | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St073_WindowEnd` | mm | 0.75 | numeric_suffix |
| St073 dead Time | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St073_deadTime` | s | 0.75 | numeric_suffix |
| St073 Test Mode | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St073_TestMode` | - | 0.75 | numeric_suffix |
| St073 Query Stations Off | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St073_QueryStationsOff` | - | 0.75 | numeric_suffix |
| St073 Test Mode Auto Off Count Down | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St073_TestModeAutoOffCountDown` | count | 0.75 | numeric_suffix |
| St073 Man Close Lane1 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St073_ManClose_Lane1` | - | 0.75 | numeric_suffix |
| St073 Man Close Lane3 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St073_ManClose_Lane3` | - | 0.75 | numeric_suffix |
| St073 Man Close Lane4 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St073_ManClose_Lane4` | - | 0.75 | numeric_suffix |
| St073 Man Close Lane2 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St073_ManClose_Lane2` | - | 0.75 | numeric_suffix |
| St073 Inch One Mode | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St073_InchOneMode[x].St073_InchOneMode[0]` | - | 0.75 | numeric_suffix |
| St073 Man Open Lane4 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St073_ManOpen_Lane4` | - | 0.75 | numeric_suffix |
| St073 Man Close Lane5 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St073_ManClose_Lane5` | - | 0.75 | numeric_suffix |
| St073 Conveyor On | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St073_ConveyorOn` | - | 0.75 | numeric_suffix |
| St073 Man Open Lane2 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St073_ManOpen_Lane2` | - | 0.75 | numeric_suffix |
| St073 Man Open Lane3 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St073_ManOpen_Lane3` | - | 0.75 | numeric_suffix |
| St073 Man Open Lane1 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St073_ManOpen_Lane1` | - | 0.75 | numeric_suffix |
| St073 Man Open Lane5 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St073_ManOpen_Lane5` | - | 0.75 | numeric_suffix |

### Pack Presence Check In Reject (2075)

- 13 candidate tag(s) considered -> 9 kept as genuine parameters (69%).
- Kept tags found by: 9 via *numeric_suffix* (the station's numeric code's last 3 digits matched a truncated St0*<digits> token in the tag's OPC path (this historian export drops the station number's leading digit) - a strong signal).

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| St075 Window End | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St075_WindowEnd` | mm | 0.75 | numeric_suffix |
| St075 Window Start24 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St075_WindowStart24` | mm | 0.75 | numeric_suffix |
| St075 Window Start | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St075_WindowStart` | mm | 0.75 | numeric_suffix |
| St075 Window End24 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St075_WindowEnd24` | mm | 0.75 | numeric_suffix |
| St075 Diag Signal Pos Lane4 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St075_DiagSignalPos_Lane4` | mm | 0.75 | numeric_suffix |
| St075 Diag Signal Pos Lane2 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St075_DiagSignalPos_Lane2` | mm | 0.75 | numeric_suffix |
| St075 Diag Signal Pos Lane1 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St075_DiagSignalPos_Lane1` | mm | 0.75 | numeric_suffix |
| St075 Diag Signal Pos Lane3 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St075_DiagSignalPos_Lane3` | mm | 0.75 | numeric_suffix |
| St075 Diag Signal Pos Lane5 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St075_DiagSignalPos_Lane5` | mm | 0.75 | numeric_suffix |

### Outfeed Belt 2 (2077)

- 20 candidate tag(s) considered -> 4 kept as genuine parameters (20%).
- Kept tags found by: 4 via *numeric_suffix* (the station's numeric code's last 3 digits matched a truncated St0*<digits> token in the tag's OPC path (this historian export drops the station number's leading digit) - a strong signal).

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| St077 Vel Offset | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St077_VelOffset` | mm/s | 0.75 | numeric_suffix |
| St077 act Status | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St077_actStatus` | - | 0.75 | numeric_suffix |
| St077 Tool Circumference | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St077_ToolCircumference` | mm | 0.75 | numeric_suffix |
| St077 Inch One Mode | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St077_InchOneMode[x].St077_InchOneMode[0]` | - | 0.75 | numeric_suffix |

### Pack Reject 2 (2081)

- 25 candidate tag(s) considered -> 21 kept as genuine parameters (84%).
- Kept tags found by: 21 via *numeric_suffix* (the station's numeric code's last 3 digits matched a truncated St0*<digits> token in the tag's OPC path (this historian export drops the station number's leading digit) - a strong signal).

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| St081 Flap Time | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St081_FlapTime` | s | 0.75 | numeric_suffix |
| St081 Num Samples | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St081_NumSamples` | - | 0.75 | numeric_suffix |
| St081 Station To Test | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St081_StationToTest` | - | 0.75 | numeric_suffix |
| St081 dead Time | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St081_deadTime` | s | 0.75 | numeric_suffix |
| St081 Window Start | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St081_WindowStart` | mm | 0.75 | numeric_suffix |
| St081 Sample Request | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St081_SampleRequest` | - | 0.75 | numeric_suffix |
| St081 Window End | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St081_WindowEnd` | mm | 0.75 | numeric_suffix |
| St081 Test Mode | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St081_TestMode` | - | 0.75 | numeric_suffix |
| St081 Sample Cancel | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St081_SampleCancel` | - | 0.75 | numeric_suffix |
| St081 Query Stations Off | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St081_QueryStationsOff` | - | 0.75 | numeric_suffix |
| St081 Test Mode Auto Off Count Down | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St081_TestModeAutoOffCountDown` | count | 0.75 | numeric_suffix |
| St081 Man Close Lane5 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St081_ManClose_Lane5` | - | 0.75 | numeric_suffix |
| St081 Man Open Lane5 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St081_ManOpen_Lane5` | - | 0.75 | numeric_suffix |
| St081 Man Close Lane1 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St081_ManClose_Lane1` | - | 0.75 | numeric_suffix |
| St081 Man Open Lane4 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St081_ManOpen_Lane4` | - | 0.75 | numeric_suffix |
| St081 Man Close Lane4 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St081_ManClose_Lane4` | - | 0.75 | numeric_suffix |
| St081 Man Close Lane2 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St081_ManClose_Lane2` | - | 0.75 | numeric_suffix |
| St081 Man Open Lane2 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St081_ManOpen_Lane2` | - | 0.75 | numeric_suffix |
| St081 Man Open Lane1 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St081_ManOpen_Lane1` | - | 0.75 | numeric_suffix |
| St081 Man Open Lane3 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St081_ManOpen_Lane3` | - | 0.75 | numeric_suffix |
| St081 Man Close Lane3 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St081_ManClose_Lane3` | - | 0.75 | numeric_suffix |

### Pack Presence Check 2 (2083)

- 13 candidate tag(s) considered -> 9 kept as genuine parameters (69%).
- Kept tags found by: 9 via *numeric_suffix* (the station's numeric code's last 3 digits matched a truncated St0*<digits> token in the tag's OPC path (this historian export drops the station number's leading digit) - a strong signal).

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| St083 Window End | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St083_WindowEnd` | mm | 0.75 | numeric_suffix |
| St083 Window End24 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St083_WindowEnd24` | mm | 0.75 | numeric_suffix |
| St083 Window Start24 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St083_WindowStart24` | mm | 0.75 | numeric_suffix |
| St083 Window Start | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St083_WindowStart` | mm | 0.75 | numeric_suffix |
| St083 Diag Signal Pos Lane3 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St083_DiagSignalPos_Lane3` | mm | 0.75 | numeric_suffix |
| St083 Diag Signal Pos Lane1 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St083_DiagSignalPos_Lane1` | mm | 0.75 | numeric_suffix |
| St083 Diag Signal Pos Lane2 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St083_DiagSignalPos_Lane2` | mm | 0.75 | numeric_suffix |
| St083 Diag Signal Pos Lane5 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St083_DiagSignalPos_Lane5` | mm | 0.75 | numeric_suffix |
| St083 Diag Signal Pos Lane4 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St083_DiagSignalPos_Lane4` | mm | 0.75 | numeric_suffix |

### Outfeed Belt 3 (2085)

- 20 candidate tag(s) considered -> 4 kept as genuine parameters (20%).
- Kept tags found by: 4 via *numeric_suffix* (the station's numeric code's last 3 digits matched a truncated St0*<digits> token in the tag's OPC path (this historian export drops the station number's leading digit) - a strong signal).

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| St085 Vel Offset | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St085_VelOffset` | mm/s | 0.75 | numeric_suffix |
| St085 act Status | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St085_actStatus` | - | 0.75 | numeric_suffix |
| St085 Tool Circumference | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St085_ToolCircumference` | mm | 0.75 | numeric_suffix |
| St085 Inch One Mode | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St085_InchOneMode[x].St085_InchOneMode[11]` | - | 0.75 | numeric_suffix |

### Slug Detection (2087)

- 4 candidate tag(s) considered -> 0 kept as genuine parameters (0%).

_No genuine parameters found among this station's candidates._

### Web Guiding Top Foil (2105)

- 21 candidate tag(s) considered -> 17 kept as genuine parameters (81%).
- Kept tags found by: 15 via *numeric_suffix* (the station's numeric code's last 3 digits matched a truncated St0*<digits> token in the tag's OPC path (this historian export drops the station number's leading digit) - a strong signal), 2 via *direct_id* (the station's raw ID string appeared literally in the tag's path/name - a strong signal).
- 2 kept parameter(s) below 0.5 confidence - flagged with warning below.

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| Reject Count (station entry, per lane) (low confidence) | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiRO.RejectStatistic_Entry_Lane[x].RejectStatistic_Entry_Lane[2][10][5]` | count | 0.45 | direct_id |
| Station Cycle Counter (per lane) (low confidence) | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC4.CounterStatistic_Station_Lane[x,y,z].CounterStatistic_Station_Lane[2,10,5]` | count | 0.45 | direct_id |
| St105 E L Jog Right | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St105_EL_JogRight` | - | 0.75 | numeric_suffix |
| St105 E L Web Offset St P Set Plus | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St105_EL_WebOffset_StP_SetPlus` | mm | 0.75 | numeric_suffix |
| St105 E L Web Offset St P | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St105_EL_WebOffset_StP` | mm | 0.75 | numeric_suffix |
| St105 E L Web Offset St P Set Absolut | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St105_EL_WebOffset_StP_SetAbsolut` | mm | 0.75 | numeric_suffix |
| St105 E L Jog Left | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St105_EL_JogLeft` | - | 0.75 | numeric_suffix |
| St105 E L Web Offset St P Format Para Set Absolut | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St105_EL_WebOffset_StP_FormatPara_SetAbsolut` | mm | 0.75 | numeric_suffix |
| St105 E L Web Offset St P Format Para | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St105_EL_WebOffset_StP_FormatPara` | mm | 0.75 | numeric_suffix |
| St105 E L Web Offset St P Set Minus | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St105_EL_WebOffset_StP_SetMinus` | mm | 0.75 | numeric_suffix |
| St105 E L Offset | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St105_EL_Offset` | mm | 0.75 | numeric_suffix |
| St105 E L Actual Pos | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St105_EL_ActualPos` | mm | 0.75 | numeric_suffix |
| St105 E L Actual Pos Actuator | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St105_EL_ActualPosActuator` | mm | 0.75 | numeric_suffix |
| St105 E L Center | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St105_EL_Center` | - | 0.75 | numeric_suffix |
| St105 E L Run Simulation On | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St105_EL_RunSimulationOn` | - | 0.75 | numeric_suffix |
| St105 E L Auto | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St105_EL_Auto` | - | 0.75 | numeric_suffix |
| St105 E L Hand | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St105_EL_Hand` | - | 0.75 | numeric_suffix |

### Web Guiding Top Foil 2 (2107)

- 21 candidate tag(s) considered -> 17 kept as genuine parameters (81%).
- Kept tags found by: 15 via *numeric_suffix* (the station's numeric code's last 3 digits matched a truncated St0*<digits> token in the tag's OPC path (this historian export drops the station number's leading digit) - a strong signal), 2 via *direct_id* (the station's raw ID string appeared literally in the tag's path/name - a strong signal).
- 2 kept parameter(s) below 0.5 confidence - flagged with warning below.

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| Reject Count (station entry, per lane) (low confidence) | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiRO.RejectStatistic_Entry_Lane[x].RejectStatistic_Entry_Lane[2][10][7]` | count | 0.45 | direct_id |
| Station Cycle Counter (per lane) (low confidence) | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC4.CounterStatistic_Station_Lane[x,y,z].CounterStatistic_Station_Lane[2,10,7]` | count | 0.45 | direct_id |
| St107 E L Web Offset St P Set Minus | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St107_EL_WebOffset_StP_SetMinus` | mm | 0.75 | numeric_suffix |
| St107 E L Web Offset St P Set Absolut | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St107_EL_WebOffset_StP_SetAbsolut` | mm | 0.75 | numeric_suffix |
| St107 E L Web Offset St P Format Para Set Absolut | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St107_EL_WebOffset_StP_FormatPara_SetAbsolut` | mm | 0.75 | numeric_suffix |
| St107 E L Web Offset St P Set Plus | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St107_EL_WebOffset_StP_SetPlus` | mm | 0.75 | numeric_suffix |
| St107 E L Web Offset St P | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St107_EL_WebOffset_StP` | mm | 0.75 | numeric_suffix |
| St107 E L Web Offset St P Format Para | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St107_EL_WebOffset_StP_FormatPara` | mm | 0.75 | numeric_suffix |
| St107 E L Jog Left | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St107_EL_JogLeft` | - | 0.75 | numeric_suffix |
| St107 E L Jog Right | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St107_EL_JogRight` | - | 0.75 | numeric_suffix |
| St107 E L Actual Pos Actuator | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St107_EL_ActualPosActuator` | mm | 0.75 | numeric_suffix |
| St107 E L Offset | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St107_EL_Offset` | mm | 0.75 | numeric_suffix |
| St107 E L Actual Pos | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St107_EL_ActualPos` | mm | 0.75 | numeric_suffix |
| St107 E L Auto | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St107_EL_Auto` | - | 0.75 | numeric_suffix |
| St107 E L Hand | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St107_EL_Hand` | - | 0.75 | numeric_suffix |
| St107 E L Center | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St107_EL_Center` | - | 0.75 | numeric_suffix |
| St107 E L Run Simulation On | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St107_EL_RunSimulationOn` | - | 0.75 | numeric_suffix |

### Web Guiding Bottom Foil (2109)

- 19 candidate tag(s) considered -> 15 kept as genuine parameters (79%).
- Kept tags found by: 15 via *numeric_suffix* (the station's numeric code's last 3 digits matched a truncated St0*<digits> token in the tag's OPC path (this historian export drops the station number's leading digit) - a strong signal).

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| St109 E L Web Offset St P Format Para | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St109_EL_WebOffset_StP_FormatPara` | mm | 0.75 | numeric_suffix |
| St109 E L Jog Left | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St109_EL_JogLeft` | - | 0.75 | numeric_suffix |
| St109 E L Web Offset St P Format Para Set Absolut | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St109_EL_WebOffset_StP_FormatPara_SetAbsolut` | mm | 0.75 | numeric_suffix |
| St109 E L Web Offset St P Set Absolut | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St109_EL_WebOffset_StP_SetAbsolut` | mm | 0.75 | numeric_suffix |
| St109 E L Web Offset St P | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St109_EL_WebOffset_StP` | mm | 0.75 | numeric_suffix |
| St109 E L Jog Right | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St109_EL_JogRight` | - | 0.75 | numeric_suffix |
| St109 E L Web Offset St P Set Minus | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St109_EL_WebOffset_StP_SetMinus` | mm | 0.75 | numeric_suffix |
| St109 E L Web Offset St P Set Plus | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St109_EL_WebOffset_StP_SetPlus` | mm | 0.75 | numeric_suffix |
| St109 E L Actual Pos | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St109_EL_ActualPos` | mm | 0.75 | numeric_suffix |
| St109 E L Actual Pos Actuator | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St109_EL_ActualPosActuator` | mm | 0.75 | numeric_suffix |
| St109 E L Offset | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St109_EL_Offset` | mm | 0.75 | numeric_suffix |
| St109 E L Hand | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St109_EL_Hand` | - | 0.75 | numeric_suffix |
| St109 E L Center | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St109_EL_Center` | - | 0.75 | numeric_suffix |
| St109 E L Auto | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St109_EL_Auto` | - | 0.75 | numeric_suffix |
| St109 E L Run Simulation On | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St109_EL_RunSimulationOn` | - | 0.75 | numeric_suffix |

### Web Guiding Bottom Foil 2 (2111)

- 22 candidate tag(s) considered -> 17 kept as genuine parameters (77%).
- Kept tags found by: 15 via *numeric_suffix* (the station's numeric code's last 3 digits matched a truncated St0*<digits> token in the tag's OPC path (this historian export drops the station number's leading digit) - a strong signal), 2 via *direct_id* (the station's raw ID string appeared literally in the tag's path/name - a strong signal).
- 2 kept parameter(s) below 0.5 confidence - flagged with warning below.

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| Reject Count (station entry, per lane) (low confidence) | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiRO.RejectStatistic_Entry_Lane[x].RejectStatistic_Entry_Lane[2][11][1]` | count | 0.45 | direct_id |
| Station Cycle Counter (per lane) (low confidence) | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC4.CounterStatistic_Station_Lane[x,y,z].CounterStatistic_Station_Lane[2,11,1]` | count | 0.45 | direct_id |
| St111 E L Jog Left | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St111_EL_JogLeft` | - | 0.75 | numeric_suffix |
| St111 E L Web Offset St P Set Absolut | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St111_EL_WebOffset_StP_SetAbsolut` | mm | 0.75 | numeric_suffix |
| St111 E L Web Offset St P Set Plus | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St111_EL_WebOffset_StP_SetPlus` | mm | 0.75 | numeric_suffix |
| St111 E L Web Offset St P Format Para | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St111_EL_WebOffset_StP_FormatPara` | mm | 0.75 | numeric_suffix |
| St111 E L Web Offset St P Set Minus | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St111_EL_WebOffset_StP_SetMinus` | mm | 0.75 | numeric_suffix |
| St111 E L Web Offset St P | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St111_EL_WebOffset_StP` | mm | 0.75 | numeric_suffix |
| St111 E L Jog Right | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St111_EL_JogRight` | - | 0.75 | numeric_suffix |
| St111 E L Web Offset St P Format Para Set Absolut | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St111_EL_WebOffset_StP_FormatPara_SetAbsolut` | mm | 0.75 | numeric_suffix |
| St111 E L Actual Pos | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St111_EL_ActualPos` | mm | 0.75 | numeric_suffix |
| St111 E L Offset | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St111_EL_Offset` | mm | 0.75 | numeric_suffix |
| St111 E L Actual Pos Actuator | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St111_EL_ActualPosActuator` | mm | 0.75 | numeric_suffix |
| St111 E L Center | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St111_EL_Center` | - | 0.75 | numeric_suffix |
| St111 E L Hand | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St111_EL_Hand` | - | 0.75 | numeric_suffix |
| St111 E L Run Simulation On | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St111_EL_RunSimulationOn` | - | 0.75 | numeric_suffix |
| St111 E L Auto | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St111_EL_Auto` | - | 0.75 | numeric_suffix |

### Web Guiding Top Foil 3 (2113)

- 22 candidate tag(s) considered -> 17 kept as genuine parameters (77%).
- Kept tags found by: 15 via *numeric_suffix* (the station's numeric code's last 3 digits matched a truncated St0*<digits> token in the tag's OPC path (this historian export drops the station number's leading digit) - a strong signal), 2 via *direct_id* (the station's raw ID string appeared literally in the tag's path/name - a strong signal).
- 2 kept parameter(s) below 0.5 confidence - flagged with warning below.

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| Reject Count (station entry, per lane) (low confidence) | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiRO.RejectStatistic_Entry_Lane[x].RejectStatistic_Entry_Lane[2][11][3]` | count | 0.45 | direct_id |
| Station Cycle Counter (per lane) (low confidence) | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC4.CounterStatistic_Station_Lane[x,y,z].CounterStatistic_Station_Lane[2,11,3]` | count | 0.45 | direct_id |
| St113 E L Jog Left | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St113_EL_JogLeft` | - | 0.75 | numeric_suffix |
| St113 E L Web Offset St P Format Para Set Absolut | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St113_EL_WebOffset_StP_FormatPara_SetAbsolut` | mm | 0.75 | numeric_suffix |
| St113 E L Web Offset St P Set Minus | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St113_EL_WebOffset_StP_SetMinus` | mm | 0.75 | numeric_suffix |
| St113 E L Web Offset St P Set Absolut | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St113_EL_WebOffset_StP_SetAbsolut` | mm | 0.75 | numeric_suffix |
| St113 E L Web Offset St P Format Para | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St113_EL_WebOffset_StP_FormatPara` | mm | 0.75 | numeric_suffix |
| St113 E L Jog Right | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St113_EL_JogRight` | - | 0.75 | numeric_suffix |
| St113 E L Web Offset St P | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St113_EL_WebOffset_StP` | mm | 0.75 | numeric_suffix |
| St113 E L Web Offset St P Set Plus | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St113_EL_WebOffset_StP_SetPlus` | mm | 0.75 | numeric_suffix |
| St113 E L Actual Pos | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St113_EL_ActualPos` | mm | 0.75 | numeric_suffix |
| St113 E L Actual Pos Actuator | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St113_EL_ActualPosActuator` | mm | 0.75 | numeric_suffix |
| St113 E L Offset | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St113_EL_Offset` | mm | 0.75 | numeric_suffix |
| St113 E L Hand | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St113_EL_Hand` | - | 0.75 | numeric_suffix |
| St113 E L Run Simulation On | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St113_EL_RunSimulationOn` | - | 0.75 | numeric_suffix |
| St113 E L Auto | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St113_EL_Auto` | - | 0.75 | numeric_suffix |
| St113 E L Center | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St113_EL_Center` | - | 0.75 | numeric_suffix |

### Top Foil Web Guiding (2115)

- 11 candidate tag(s) considered -> 6 kept as genuine parameters (55%).
- Kept tags found by: 4 via *numeric_suffix* (the station's numeric code's last 3 digits matched a truncated St0*<digits> token in the tag's OPC path (this historian export drops the station number's leading digit) - a strong signal), 2 via *direct_id* (the station's raw ID string appeared literally in the tag's path/name - a strong signal).
- 2 kept parameter(s) below 0.5 confidence - flagged with warning below.

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| Reject Count (station entry, per lane) (low confidence) | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiRO.RejectStatistic_Entry_Lane[x].RejectStatistic_Entry_Lane[2][11][5]` | count | 0.45 | direct_id |
| Station Cycle Counter (per lane) (low confidence) | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC4.CounterStatistic_Station_Lane[x,y,z].CounterStatistic_Station_Lane[2,11,5]` | count | 0.45 | direct_id |
| St115 E L Auto | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St115_EL_Auto` | - | 0.75 | numeric_suffix |
| St115 E L Center | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St115_EL_Center` | - | 0.75 | numeric_suffix |
| St115 E L Run Simulation On | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St115_EL_RunSimulationOn` | - | 0.75 | numeric_suffix |
| St115 E L Hand | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St115_EL_Hand` | - | 0.75 | numeric_suffix |

### Top Foil Unwind (2152)

- 74 candidate tag(s) considered -> 58 kept as genuine parameters (78%).
- Kept tags found by: 56 via *numeric_suffix* (the station's numeric code's last 3 digits matched a truncated St0*<digits> token in the tag's OPC path (this historian export drops the station number's leading digit) - a strong signal), 2 via *direct_id* (the station's raw ID string appeared literally in the tag's path/name - a strong signal).
- 2 kept parameter(s) below 0.5 confidence - flagged with warning below.

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| Reject Count (station entry, per lane) (low confidence) | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiRO.RejectStatistic_Entry_Lane[x].RejectStatistic_Entry_Lane[2][15][2]` | count | 0.45 | direct_id |
| Station Cycle Counter (per lane) (low confidence) | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC4.CounterStatistic_Station_Lane[x,y,z].CounterStatistic_Station_Lane[2,15,2]` | count | 0.45 | direct_id |
| St152 Diameter Prewarning | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St152_DiameterPrewarning` | - | 0.75 | numeric_suffix |
| St152 Pressure Tol Plus Pull Rolls | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St152_PressureTolPlus_PullRolls` | bar | 0.75 | numeric_suffix |
| St152 Pressure Tol Plus | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St152_PressureTolPlus` | bar | 0.75 | numeric_suffix |
| St152 Pressure Set Point Dancer | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St152_PressureSetPoint_Dancer` | bar | 0.75 | numeric_suffix |
| St152 Diameter Kalib Max2 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St152_DiameterKalib_Max2` | - | 0.75 | numeric_suffix |
| St152 Stop Position Winder1 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St152_StopPositionWinder1` | mm | 0.75 | numeric_suffix |
| St152 Pressure Set Point Up | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St152_PressureSetPoint_Up` | bar | 0.75 | numeric_suffix |
| St152 Diameter Kalib Max1 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St152_DiameterKalib_Max1` | - | 0.75 | numeric_suffix |
| St152 Diameter Kalib Min Per Cent2 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St152_DiameterKalib_MinPerCent2` | - | 0.75 | numeric_suffix |
| St152 Diameter Kalib Min1 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St152_DiameterKalib_Min1` | - | 0.75 | numeric_suffix |
| St152 Pressure Set Point | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St152_PressureSetPoint` | bar | 0.75 | numeric_suffix |
| St152 Pressure Tol Minus Dancer | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St152_PressureTolMinus_Dancer` | bar | 0.75 | numeric_suffix |
| St152 Stop Position Winder2 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St152_StopPositionWinder2` | mm | 0.75 | numeric_suffix |
| St152 Diameter Kalib Min Per Cent1 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St152_DiameterKalib_MinPerCent1` | - | 0.75 | numeric_suffix |
| St152 Diameter Kalib Max Per Cent1 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St152_DiameterKalib_MaxPerCent1` | - | 0.75 | numeric_suffix |
| St152 Pressure Tol Plus Dancer | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St152_PressureTolPlus_Dancer` | bar | 0.75 | numeric_suffix |
| St152 Stop With Printmark | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St152_StopWithPrintmark` | - | 0.75 | numeric_suffix |
| St152 Pressure Set Point Pull Rolls | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St152_PressureSetPoint_PullRolls` | bar | 0.75 | numeric_suffix |
| St152 Material Thickness | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St152_MaterialThickness` | - | 0.75 | numeric_suffix |
| St152 Pressure Tol Minus | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St152_PressureTolMinus` | bar | 0.75 | numeric_suffix |
| St152 Change To Other Winder | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St152_ChangeToOtherWinder` | - | 0.75 | numeric_suffix |
| St152 Diameter Min | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St152_DiameterMin` | - | 0.75 | numeric_suffix |
| St152 Winder1 Active | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St152_Winder1Active` | - | 0.75 | numeric_suffix |
| St152 Disable Auto Splicer | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St152_DisableAutoSplicer` | - | 0.75 | numeric_suffix |
| St152 Pressure Tol Minus Pull Rolls | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St152_PressureTolMinus_PullRolls` | bar | 0.75 | numeric_suffix |
| St152 Diameter Kalib Max Per Cent2 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St152_DiameterKalib_MaxPerCent2` | - | 0.75 | numeric_suffix |
| St152 Diameter Kalib Min2 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St152_DiameterKalib_Min2` | - | 0.75 | numeric_suffix |
| St152 Product Remaining | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St152_ProductRemaining` | - | 0.75 | numeric_suffix |
| St152 Act Diameter Per Cent Right | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St152_ActDiameterPerCentRight` | - | 0.75 | numeric_suffix |
| St152 Pressure Act Val | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St152_PressureActVal` | bar | 0.75 | numeric_suffix |
| St152 Rest Time | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St152_RestTime` | s | 0.75 | numeric_suffix |
| St152 Dancer Position | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St152_DancerPosition` | mm | 0.75 | numeric_suffix |
| St152 Pressure Act Val Dancer | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St152_PressureActValDancer` | bar | 0.75 | numeric_suffix |
| St152 Dancer Position Feeder | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St152_DancerPositionFeeder` | mm | 0.75 | numeric_suffix |
| St152 Splicer Ready | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St152_SplicerReady` | - | 0.75 | numeric_suffix |
| St152 Dancer Min Feeder | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St152_DancerMinFeeder` | - | 0.75 | numeric_suffix |
| St152 Dancer Max | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St152_DancerMax` | - | 0.75 | numeric_suffix |
| St152 Pressure Act Val Pull Rolls | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St152_PressureActValPullRolls` | bar | 0.75 | numeric_suffix |
| St152 Act Diameter | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St152_ActDiameter` | - | 0.75 | numeric_suffix |
| St152 Act Diameter Per Cent | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St152_ActDiameterPerCent` | - | 0.75 | numeric_suffix |
| St152 Pressure Act Val Per Cent | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St152_PressureActValPerCent` | bar | 0.75 | numeric_suffix |
| St152 Pressure Act Val Per Cent Pull Rolls | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St152_PressureActValPerCentPullRolls` | bar | 0.75 | numeric_suffix |
| St152 Act Diameter Right | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St152_ActDiameterRight` | - | 0.75 | numeric_suffix |
| St152 Splice Steps | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St152_SpliceSteps` | - | 0.75 | numeric_suffix |
| St152 Pressure Act Val Per Cent Dancer | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St152_PressureActValPerCentDancer` | bar | 0.75 | numeric_suffix |
| St152 Act Diameter Per Cent Left | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St152_ActDiameterPerCentLeft` | - | 0.75 | numeric_suffix |
| St152 Act Diameter Left | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St152_ActDiameterLeft` | - | 0.75 | numeric_suffix |
| St152 Dancer Max Feeder | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St152_DancerMaxFeeder` | - | 0.75 | numeric_suffix |
| St152 Dancer Min | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St152_DancerMin` | - | 0.75 | numeric_suffix |
| St152 Calibrate Dancer Buffer | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St152_CalibrateDancerBuffer` | - | 0.75 | numeric_suffix |
| St152 With Printmark | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St152_WithPrintmark` | - | 0.75 | numeric_suffix |
| St152 Calibrate Dancer Pull Rolls | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St152_CalibrateDancerPullRolls` | - | 0.75 | numeric_suffix |
| St152 Inch One Mode | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St152_InchOneMode[x].St152_InchOneMode[7]` | - | 0.75 | numeric_suffix |
| St152 Select Single Step Splicer | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St152_SelectSingleStepSplicer` | - | 0.75 | numeric_suffix |
| St152 Man Open | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St152_ManOpen` | - | 0.75 | numeric_suffix |
| St152 Man Close | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St152_ManClose` | - | 0.75 | numeric_suffix |

### Bottom Foil Unwind (2154)

- 74 candidate tag(s) considered -> 58 kept as genuine parameters (78%).
- Kept tags found by: 56 via *numeric_suffix* (the station's numeric code's last 3 digits matched a truncated St0*<digits> token in the tag's OPC path (this historian export drops the station number's leading digit) - a strong signal), 2 via *direct_id* (the station's raw ID string appeared literally in the tag's path/name - a strong signal).
- 2 kept parameter(s) below 0.5 confidence - flagged with warning below.

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| Reject Count (station entry, per lane) (low confidence) | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiRO.RejectStatistic_Entry_Lane[x].RejectStatistic_Entry_Lane[2][15][4]` | count | 0.45 | direct_id |
| Station Cycle Counter (per lane) (low confidence) | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC4.CounterStatistic_Station_Lane[x,y,z].CounterStatistic_Station_Lane[2,15,4]` | count | 0.45 | direct_id |
| St154 Stop With Printmark | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St154_StopWithPrintmark` | - | 0.75 | numeric_suffix |
| St154 Diameter Prewarning | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St154_DiameterPrewarning` | - | 0.75 | numeric_suffix |
| St154 Pressure Tol Plus Dancer | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St154_PressureTolPlus_Dancer` | bar | 0.75 | numeric_suffix |
| St154 Diameter Kalib Min Per Cent1 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St154_DiameterKalib_MinPerCent1` | - | 0.75 | numeric_suffix |
| St154 Change To Other Winder | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St154_ChangeToOtherWinder` | - | 0.75 | numeric_suffix |
| St154 Diameter Kalib Max2 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St154_DiameterKalib_Max2` | - | 0.75 | numeric_suffix |
| St154 Pressure Set Point Pull Rolls | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St154_PressureSetPoint_PullRolls` | bar | 0.75 | numeric_suffix |
| St154 Diameter Kalib Max Per Cent1 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St154_DiameterKalib_MaxPerCent1` | - | 0.75 | numeric_suffix |
| St154 Diameter Kalib Min Per Cent2 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St154_DiameterKalib_MinPerCent2` | - | 0.75 | numeric_suffix |
| St154 Stop Position Winder2 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St154_StopPositionWinder2` | mm | 0.75 | numeric_suffix |
| St154 Pressure Tol Plus Pull Rolls | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St154_PressureTolPlus_PullRolls` | bar | 0.75 | numeric_suffix |
| St154 Material Thickness | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St154_MaterialThickness` | - | 0.75 | numeric_suffix |
| St154 Stop Position Winder1 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St154_StopPositionWinder1` | mm | 0.75 | numeric_suffix |
| St154 Pressure Set Point | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St154_PressureSetPoint` | bar | 0.75 | numeric_suffix |
| St154 Pressure Tol Minus Pull Rolls | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St154_PressureTolMinus_PullRolls` | bar | 0.75 | numeric_suffix |
| St154 Disable Auto Splicer | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St154_DisableAutoSplicer` | - | 0.75 | numeric_suffix |
| St154 Pressure Tol Minus Dancer | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St154_PressureTolMinus_Dancer` | bar | 0.75 | numeric_suffix |
| St154 Diameter Kalib Max Per Cent2 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St154_DiameterKalib_MaxPerCent2` | - | 0.75 | numeric_suffix |
| St154 Diameter Kalib Min1 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St154_DiameterKalib_Min1` | - | 0.75 | numeric_suffix |
| St154 Winder1 Active | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St154_Winder1Active` | - | 0.75 | numeric_suffix |
| St154 Diameter Kalib Min2 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St154_DiameterKalib_Min2` | - | 0.75 | numeric_suffix |
| St154 Pressure Tol Plus | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St154_PressureTolPlus` | bar | 0.75 | numeric_suffix |
| St154 Diameter Kalib Max1 | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St154_DiameterKalib_Max1` | - | 0.75 | numeric_suffix |
| St154 Pressure Tol Minus | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St154_PressureTolMinus` | bar | 0.75 | numeric_suffix |
| St154 Pressure Set Point Up | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St154_PressureSetPoint_Up` | bar | 0.75 | numeric_suffix |
| St154 Diameter Min | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St154_DiameterMin` | - | 0.75 | numeric_suffix |
| St154 Pressure Set Point Dancer | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St154_PressureSetPoint_Dancer` | bar | 0.75 | numeric_suffix |
| St154 Dancer Position | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St154_DancerPosition` | mm | 0.75 | numeric_suffix |
| St154 Splicer Ready | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St154_SplicerReady` | - | 0.75 | numeric_suffix |
| St154 Dancer Min Feeder | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St154_DancerMinFeeder` | - | 0.75 | numeric_suffix |
| St154 Act Diameter | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St154_ActDiameter` | - | 0.75 | numeric_suffix |
| St154 Act Diameter Right | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St154_ActDiameterRight` | - | 0.75 | numeric_suffix |
| St154 Dancer Position Feeder | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St154_DancerPositionFeeder` | mm | 0.75 | numeric_suffix |
| St154 Splice Steps | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St154_SpliceSteps` | - | 0.75 | numeric_suffix |
| St154 Act Diameter Per Cent Right | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St154_ActDiameterPerCentRight` | - | 0.75 | numeric_suffix |
| St154 Pressure Act Val Per Cent Dancer | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St154_PressureActValPerCentDancer` | bar | 0.75 | numeric_suffix |
| St154 Product Remaining | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St154_ProductRemaining` | - | 0.75 | numeric_suffix |
| St154 Pressure Act Val Per Cent Pull Rolls | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St154_PressureActValPerCentPullRolls` | bar | 0.75 | numeric_suffix |
| St154 Act Diameter Left | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St154_ActDiameterLeft` | - | 0.75 | numeric_suffix |
| St154 Dancer Max Feeder | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St154_DancerMaxFeeder` | - | 0.75 | numeric_suffix |
| St154 Act Diameter Per Cent | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St154_ActDiameterPerCent` | - | 0.75 | numeric_suffix |
| St154 Pressure Act Val Dancer | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St154_PressureActValDancer` | bar | 0.75 | numeric_suffix |
| St154 Pressure Act Val Pull Rolls | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St154_PressureActValPullRolls` | bar | 0.75 | numeric_suffix |
| St154 Act Diameter Per Cent Left | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St154_ActDiameterPerCentLeft` | - | 0.75 | numeric_suffix |
| St154 Rest Time | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St154_RestTime` | s | 0.75 | numeric_suffix |
| St154 Pressure Act Val Per Cent | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St154_PressureActValPerCent` | bar | 0.75 | numeric_suffix |
| St154 Dancer Min | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St154_DancerMin` | - | 0.75 | numeric_suffix |
| St154 Pressure Act Val | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St154_PressureActVal` | bar | 0.75 | numeric_suffix |
| St154 Dancer Max | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St154_DancerMax` | - | 0.75 | numeric_suffix |
| St154 Calibrate Dancer Pull Rolls | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St154_CalibrateDancerPullRolls` | - | 0.75 | numeric_suffix |
| St154 With Printmark | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St154_WithPrintmark` | - | 0.75 | numeric_suffix |
| St154 Man Open | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St154_ManOpen` | - | 0.75 | numeric_suffix |
| St154 Calibrate Dancer Buffer | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St154_CalibrateDancerBuffer` | - | 0.75 | numeric_suffix |
| St154 Inch One Mode | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St154_InchOneMode[x].St154_InchOneMode[5]` | - | 0.75 | numeric_suffix |
| St154 Man Close | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St154_ManClose` | - | 0.75 | numeric_suffix |
| St154 Select Single Step Splicer | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St154_SelectSingleStepSplicer` | - | 0.75 | numeric_suffix |

### Rewind (2170)

- 23 candidate tag(s) considered -> 7 kept as genuine parameters (30%).
- Kept tags found by: 5 via *numeric_suffix* (the station's numeric code's last 3 digits matched a truncated St0*<digits> token in the tag's OPC path (this historian export drops the station number's leading digit) - a strong signal), 2 via *direct_id* (the station's raw ID string appeared literally in the tag's path/name - a strong signal).
- 2 kept parameter(s) below 0.5 confidence - flagged with warning below.

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| Reject Count (station entry, per lane) (low confidence) | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiRO.RejectStatistic_Entry_Lane[x].RejectStatistic_Entry_Lane[2][17][0]` | count | 0.45 | direct_id |
| Station Cycle Counter (per lane) (low confidence) | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC4.CounterStatistic_Station_Lane[x,y,z].CounterStatistic_Station_Lane[2,17,0]` | count | 0.45 | direct_id |
| St170 Pressure Set Point Dancer | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St170_PressureSetPoint_Dancer` | bar | 0.75 | numeric_suffix |
| St170 Delaytime | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St170_Delaytime` | s | 0.75 | numeric_suffix |
| St170 Pressure Act Val Dancer | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St170_PressureActValDancer` | bar | 0.75 | numeric_suffix |
| St170 Pressure Act Val Per Cent Dancer | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St170_PressureActValPerCentDancer` | bar | 0.75 | numeric_suffix |
| St170 Inch One Mode | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St170_InchOneMode[x].St170_InchOneMode[2]` | - | 0.75 | numeric_suffix |

### Encoder (2180)

- 16 candidate tag(s) considered -> 12 kept as genuine parameters (75%).
- Kept tags found by: 10 via *numeric_suffix* (the station's numeric code's last 3 digits matched a truncated St0*<digits> token in the tag's OPC path (this historian export drops the station number's leading digit) - a strong signal), 2 via *direct_id* (the station's raw ID string appeared literally in the tag's path/name - a strong signal).
- 2 kept parameter(s) below 0.5 confidence - flagged with warning below.

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| Reject Count (station entry, per lane) (low confidence) | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiRO.RejectStatistic_Entry_Lane[x].RejectStatistic_Entry_Lane[2][18][0]` | count | 0.45 | direct_id |
| Station Cycle Counter (per lane) (low confidence) | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC4.CounterStatistic_Station_Lane[x,y,z].CounterStatistic_Station_Lane[2,18,0]` | count | 0.45 | direct_id |
| St180 Product Len Offset | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC5.St180_ProductLenOffset` | mm | 0.75 | numeric_suffix |
| St180 Product Len Average Dev | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St180_ProductLenAverageDev` | - | 0.75 | numeric_suffix |
| St180 Inc Encoder Feed Constant | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St180_IncEncoderFeedConstant` | - | 0.75 | numeric_suffix |
| St180 Product Len Act Dev | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St180_ProductLenActDev` | - | 0.75 | numeric_suffix |
| St180 Product Len Act Val | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC6.St180_ProductLenActVal` | - | 0.75 | numeric_suffix |
| St180 Foil With Printmark | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St180_FoilWithPrintmark` | - | 0.75 | numeric_suffix |
| St180 W C counter Value | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St180_WC_counterValue` | count | 0.75 | numeric_suffix |
| St180 W C external Measured Value | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St180_WC_externalMeasuredValue` | - | 0.75 | numeric_suffix |
| St180 W C Calibration Start | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St180_WC_CalibrationStart` | - | 0.75 | numeric_suffix |
| St180 W C reset | `nsu=KEPServerEX;s=BACC_CODESYS.BACC_NGP2.Application.TmpHmi_Var.TmpHmiC7.St180_WC_reset` | - | 0.75 | numeric_suffix |

## Machine: Secondary Packaging Machine 2 (SP2)

Documented stations (non-numeric - no PLC code given in the manual): Carton Building (F3 Robot), Trans-modules, Pack Picking (F4 Robots/Spider robots), Carton closing/Literature picking (F202 robot), Outfeed conveyor, Reject station 1, Print and apply, Reject station 2, Manual infeed.

_No candidate tags - this tags.json export contains no SP2-referencing paths. SP2 runs on a separate controller from NGP2 and needs its own historian tag export before matching can run against it._
