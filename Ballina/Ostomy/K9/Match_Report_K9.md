# Tag Matching Report - Line K9

This summarizes, for every station found on this line, which historian tags were kept as genuine process parameters and why. Parameters marked with a low match strategy (keyword/keyword_stem/legend_code/folder_match) or below 0.5 confidence are the ones most worth a second look from someone who knows the physical machine.

## Summary

- 17 station(s) processed.
- 2072 candidate tag(s) considered across all stations -> 799 kept as genuine parameters (39% of candidates).
- 799 of this line's 3019 total historian tags (26.5%) ended up mapped to a genuine parameter - this is the actual coverage of the raw tag export, as opposed to the conversion rate above, which only measures the pre-filtered candidate pool.
- 67 kept parameter(s) below 0.5 confidence overall - worth a second look.
- 1 station(s) with no genuine parameters found at all: ABF Binder FLAP stamping/welding unit (MC004-ABF).

## Machine: Inline System KIT 70/20

### UWS unwinding unit (MC004-UWS)

- 81 candidate tag(s) considered -> 44 kept as genuine parameters (54%).
- Kept tags found by: 44 via *module_segment* (the tag name contains this station's own PLC/module code as a literal segment - the strongest signal available).

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| Web 1 Film End Threshold - Lower Roll | `DB_02UWS_WEB_01.WEB_01.Val_ThFoilEndLower` | mm | 0.55 | module_segment |
| Web 1 Film End Threshold - Upper Roll | `DB_02UWS_WEB_01.WEB_01.Val_ThFoilEndUpper` | mm | 0.55 | module_segment |
| Web 2 Film End Threshold - Lower Roll | `DB_02UWS_WEB_02.WEB_02.Val_ThFoilEndLower` | mm | 0.55 | module_segment |
| Web 2 Film End Threshold - Upper Roll | `DB_02UWS_WEB_02.WEB_02.Val_ThFoilEndUpper` | mm | 0.55 | module_segment |
| Web 3 Film End Threshold - Lower Roll | `DB_02UWS_WEB_03.WEB_03.Val_ThFoilEndLower` | mm | 0.55 | module_segment |
| Web 3 Film End Threshold - Upper Roll | `DB_02UWS_WEB_03.WEB_03.Val_ThFoilEndUpper` | mm | 0.55 | module_segment |
| Web 4 Film End Threshold - Lower Roll | `DB_02UWS_WEB_04.WEB_04.Val_ThFoilEndLower` | mm | 0.55 | module_segment |
| Web 4 Film End Threshold - Upper Roll | `DB_02UWS_WEB_04.WEB_04.Val_ThFoilEndUpper` | mm | 0.55 | module_segment |
| Web 1 Ultrasonic Sensor Reading - Lower Roll | `DB_02UWS_WEB_01.WEB_01.DISP_SensorRollLower` | mm | 0.60 | module_segment |
| Web 1 Ultrasonic Sensor Reading - Upper Roll | `DB_02UWS_WEB_01.WEB_01.DISP_SensorRollUpper` | mm | 0.60 | module_segment |
| Web 1 Magnet Powder Brake Factor - Lower Roll | `DB_02UWS_WEB_01.WEB_01.Val_FaktorRollLower` | - | 0.60 | module_segment |
| Web 1 Magnet Powder Brake Factor - Upper Roll | `DB_02UWS_WEB_01.WEB_01.Val_FaktorRollUpper` | - | 0.60 | module_segment |
| Web 2 Ultrasonic Sensor Reading - Lower Roll | `DB_02UWS_WEB_02.WEB_02.DISP_SensorRollLower` | mm | 0.60 | module_segment |
| Web 2 Ultrasonic Sensor Reading - Upper Roll | `DB_02UWS_WEB_02.WEB_02.DISP_SensorRollUpper` | mm | 0.60 | module_segment |
| Web 2 Magnet Powder Brake Factor - Lower Roll | `DB_02UWS_WEB_02.WEB_02.Val_FaktorRollLower` | - | 0.60 | module_segment |
| Web 2 Magnet Powder Brake Factor - Upper Roll | `DB_02UWS_WEB_02.WEB_02.Val_FaktorRollUpper` | - | 0.60 | module_segment |
| Web 3 Ultrasonic Sensor Reading - Lower Roll | `DB_02UWS_WEB_03.WEB_03.DISP_SensorRollLower` | mm | 0.60 | module_segment |
| Web 3 Ultrasonic Sensor Reading - Upper Roll | `DB_02UWS_WEB_03.WEB_03.DISP_SensorRollUpper` | mm | 0.60 | module_segment |
| Web 3 Magnet Powder Brake Factor - Lower Roll | `DB_02UWS_WEB_03.WEB_03.Val_FaktorRollLower` | - | 0.60 | module_segment |
| Web 3 Magnet Powder Brake Factor - Upper Roll | `DB_02UWS_WEB_03.WEB_03.Val_FaktorRollUpper` | - | 0.60 | module_segment |
| Web 4 Ultrasonic Sensor Reading - Lower Roll | `DB_02UWS_WEB_04.WEB_04.DISP_SensorRollLower` | mm | 0.60 | module_segment |
| Web 4 Ultrasonic Sensor Reading - Upper Roll | `DB_02UWS_WEB_04.WEB_04.DISP_SensorRollUpper` | mm | 0.60 | module_segment |
| Web 4 Magnet Powder Brake Factor - Lower Roll | `DB_02UWS_WEB_04.WEB_04.Val_FaktorRollLower` | - | 0.60 | module_segment |
| Web 4 Magnet Powder Brake Factor - Upper Roll | `DB_02UWS_WEB_04.WEB_04.Val_FaktorRollUpper` | - | 0.60 | module_segment |
| Web 1 Actual Cross Adjustment Y | `DB_02UWS_WEB_01.WEB_01.ActualYAdjustment` | 0.1 mm | 0.75 | module_segment |
| Web 1 Remaining Cycles After Foil End (Display) | `DB_02UWS_WEB_01.WEB_01.DISP_WebRemCycles` | cycles | 0.75 | module_segment |
| Web 1 Remaining Cycles After Foil End (Value 1) | `DB_02UWS_WEB_01.WEB_01.Val_WebRemCycles_1` | cycles | 0.75 | module_segment |
| Web 1 Remaining Cycles After Foil End (Value 2) | `DB_02UWS_WEB_01.WEB_01.Val_WebRemCycles_2` | cycles | 0.75 | module_segment |
| Web 2 Actual Cross Adjustment Y | `DB_02UWS_WEB_02.WEB_02.ActualYAdjustment` | 0.1 mm | 0.75 | module_segment |
| Web 2 Remaining Cycles After Foil End (Display) | `DB_02UWS_WEB_02.WEB_02.DISP_WebRemCycles` | cycles | 0.75 | module_segment |
| Web 2 Remaining Cycles After Foil End (Value 1) | `DB_02UWS_WEB_02.WEB_02.Val_WebRemCycles_1` | cycles | 0.75 | module_segment |
| Web 2 Remaining Cycles After Foil End (Value 2) | `DB_02UWS_WEB_02.WEB_02.Val_WebRemCycles_2` | cycles | 0.75 | module_segment |
| Web 3 Actual Cross Adjustment Y | `DB_02UWS_WEB_03.WEB_03.ActualYAdjustment` | 0.1 mm | 0.75 | module_segment |
| Web 3 Remaining Cycles After Foil End (Display) | `DB_02UWS_WEB_03.WEB_03.DISP_WebRemCycles` | cycles | 0.75 | module_segment |
| Web 3 Remaining Cycles After Foil End (Value 1) | `DB_02UWS_WEB_03.WEB_03.Val_WebRemCycles_1` | cycles | 0.75 | module_segment |
| Web 3 Remaining Cycles After Foil End (Value 2) | `DB_02UWS_WEB_03.WEB_03.Val_WebRemCycles_2` | cycles | 0.75 | module_segment |
| Web 4 Actual Cross Adjustment Y | `DB_02UWS_WEB_04.WEB_04.ActualYAdjustment` | 0.1 mm | 0.75 | module_segment |
| Web 4 Remaining Cycles After Foil End (Display) | `DB_02UWS_WEB_04.WEB_04.DISP_WebRemCycles` | cycles | 0.75 | module_segment |
| Web 4 Remaining Cycles After Foil End (Value 1) | `DB_02UWS_WEB_04.WEB_04.Val_WebRemCycles_1` | cycles | 0.75 | module_segment |
| Web 4 Remaining Cycles After Foil End (Value 2) | `DB_02UWS_WEB_04.WEB_04.Val_WebRemCycles_2` | cycles | 0.75 | module_segment |
| Web 1 Target Cross Adjustment Y | `DB_02UWS_WEB_01.WEB_01.TargetYAdjustment` | 0.1 mm | 0.80 | module_segment |
| Web 2 Target Cross Adjustment Y | `DB_02UWS_WEB_02.WEB_02.TargetYAdjustment` | 0.1 mm | 0.80 | module_segment |
| Web 3 Target Cross Adjustment Y | `DB_02UWS_WEB_03.WEB_03.TargetYAdjustment` | 0.1 mm | 0.80 | module_segment |
| Web 4 Target Cross Adjustment Y | `DB_02UWS_WEB_04.WEB_04.TargetYAdjustment` | 0.1 mm | 0.80 | module_segment |

### FAC roll magazine (MC004-FAC)

- 68 candidate tag(s) considered -> 6 kept as genuine parameters (9%).
- Kept tags found by: 6 via *module_segment* (the tag name contains this station's own PLC/module code as a literal segment - the strongest signal available).

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| Adjustment 1 Position OK | `DB_FAC_Data.Pos_ok_Adjust1` | - | 0.55 | module_segment |
| Adjustment 2 Position OK | `DB_FAC_Data.Pos_ok_Adjust2` | - | 0.55 | module_segment |
| Actual Position Sensor Adjustment 1 | `DB_FAC_Data.ActualAdjustment1` | mm | 0.65 | module_segment |
| Actual Position Sensor Adjustment 2 | `DB_FAC_Data.ActualAdjustment2` | mm | 0.65 | module_segment |
| Target Position Sensor Adjustment 1 | `DB_FAC_Data.TargetAdjustment1` | mm | 0.65 | module_segment |
| Target Position Sensor Adjustment 2 | `DB_FAC_Data.TargetAdjustment2` | mm | 0.65 | module_segment |

### INS gripper-feed system & chain conveyor (MC004-INS)

- 146 candidate tag(s) considered -> 131 kept as genuine parameters (90%).
- Kept tags found by: 131 via *module_segment* (the tag name contains this station's own PLC/module code as a literal segment - the strongest signal available).
- 10 kept parameter(s) below 0.5 confidence - flagged with ⚠ below.

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| Foil Tack 1 Heater Controller Setting ⚠ | `04INS_Heater_Data.FT_1.ControlerSetting` | % | 0.40 | module_segment |
| Foil Tack 1 Heater Correction Value ⚠ | `04INS_Heater_Data.FT_1.CorrectionValue` | - | 0.40 | module_segment |
| Foil Tack 2 Heater Controller Setting ⚠ | `04INS_Heater_Data.FT_2.ControlerSetting` | % | 0.40 | module_segment |
| Foil Tack 2 Heater Correction Value ⚠ | `04INS_Heater_Data.FT_2.CorrectionValue` | - | 0.40 | module_segment |
| Foil Tack 3 Heater Controller Setting ⚠ | `04INS_Heater_Data.FT_3.ControlerSetting` | % | 0.40 | module_segment |
| Foil Tack 3 Heater Correction Value ⚠ | `04INS_Heater_Data.FT_3.CorrectionValue` | - | 0.40 | module_segment |
| Foil Tack 4 Heater Controller Setting ⚠ | `04INS_Heater_Data.FT_4.ControlerSetting` | % | 0.40 | module_segment |
| Foil Tack 4 Heater Correction Value ⚠ | `04INS_Heater_Data.FT_4.CorrectionValue` | - | 0.40 | module_segment |
| Foil Tack 5 Heater Controller Setting ⚠ | `04INS_Heater_Data.FT_5.ControlerSetting` | % | 0.40 | module_segment |
| Foil Tack 5 Heater Correction Value ⚠ | `04INS_Heater_Data.FT_5.CorrectionValue` | - | 0.40 | module_segment |
| Foil Tack 1 Heater Solid State Relay Output | `04INS_Heater_Data.FT_1.OutputSSD` | - | 0.50 | module_segment |
| Foil Tack 1 Heater Scale Curve Y Maximum | `04INS_Heater_Data.FT_1.YScaleMax` | °C | 0.50 | module_segment |
| Foil Tack 1 Heater Scale Curve Y Minimum | `04INS_Heater_Data.FT_1.YScaleMin` | °C | 0.50 | module_segment |
| Foil Tack 2 Heater Solid State Relay Output | `04INS_Heater_Data.FT_2.OutputSSD` | - | 0.50 | module_segment |
| Foil Tack 2 Heater Scale Curve Y Maximum | `04INS_Heater_Data.FT_2.YScaleMax` | °C | 0.50 | module_segment |
| Foil Tack 2 Heater Scale Curve Y Minimum | `04INS_Heater_Data.FT_2.YScaleMin` | °C | 0.50 | module_segment |
| Foil Tack 3 Heater Solid State Relay Output | `04INS_Heater_Data.FT_3.OutputSSD` | - | 0.50 | module_segment |
| Foil Tack 3 Heater Scale Curve Y Maximum | `04INS_Heater_Data.FT_3.YScaleMax` | °C | 0.50 | module_segment |
| Foil Tack 3 Heater Scale Curve Y Minimum | `04INS_Heater_Data.FT_3.YScaleMin` | °C | 0.50 | module_segment |
| Foil Tack 4 Heater Solid State Relay Output | `04INS_Heater_Data.FT_4.OutputSSD` | - | 0.50 | module_segment |
| Foil Tack 4 Heater Scale Curve Y Maximum | `04INS_Heater_Data.FT_4.YScaleMax` | °C | 0.50 | module_segment |
| Foil Tack 4 Heater Scale Curve Y Minimum | `04INS_Heater_Data.FT_4.YScaleMin` | °C | 0.50 | module_segment |
| Foil Tack 5 Heater Solid State Relay Output | `04INS_Heater_Data.FT_5.OutputSSD` | - | 0.50 | module_segment |
| Foil Tack 5 Heater Scale Curve Y Maximum | `04INS_Heater_Data.FT_5.YScaleMax` | °C | 0.50 | module_segment |
| Foil Tack 5 Heater Scale Curve Y Minimum | `04INS_Heater_Data.FT_5.YScaleMin` | °C | 0.50 | module_segment |
| Servo Axis - Jog Backward (Setting Mode) | `04INS_Servo_Data.Servo.SP_TippBWD` | - | 0.50 | module_segment |
| Servo Axis - Jog Forward (Setting Mode) | `04INS_Servo_Data.Servo.SP_TippFWD` | - | 0.50 | module_segment |
| Feed Nipper 1 Selection | `04INS_Data.SelectionFeedNipper01` | - | 0.55 | module_segment |
| Feed Nipper 2 Selection | `04INS_Data.SelectionFeedNipper02` | - | 0.55 | module_segment |
| Feed Nipper 3 Selection | `04INS_Data.SelectionFeedNipper03` | - | 0.55 | module_segment |
| Feed Nipper 4 Selection | `04INS_Data.SelectionFeedNipper04` | - | 0.55 | module_segment |
| Feed Nipper 5 Selection | `04INS_Data.SelectionFeedNipper05` | - | 0.55 | module_segment |
| Feed Nipper 6 Selection | `04INS_Data.SelectionFeedNipper06` | - | 0.55 | module_segment |
| Feed Nipper 7 Selection | `04INS_Data.SelectionFeedNipper07` | - | 0.55 | module_segment |
| Feed Nipper 8 Selection | `04INS_Data.SelectionFeedNipper08` | - | 0.55 | module_segment |
| Feed Nipper 9 Selection | `04INS_Data.SelectionFeedNipper09` | - | 0.55 | module_segment |
| Feed Nipper 10 Selection | `04INS_Data.SelectionFeedNipper10` | - | 0.55 | module_segment |
| Open Nipper Field 4 Selection | `04INS_Data.SelectionOpenNippers4` | - | 0.55 | module_segment |
| Open Nipper Field 7 Selection | `04INS_Data.SelectionOpenNippers7` | - | 0.55 | module_segment |
| Stretching Nipper 1 Selection | `04INS_Data.SelectionStreching01` | - | 0.55 | module_segment |
| Stretching Nipper 2 Selection | `04INS_Data.SelectionStreching02` | - | 0.55 | module_segment |
| Stretching Nipper 3 Selection | `04INS_Data.SelectionStreching03` | - | 0.55 | module_segment |
| Stretching Nipper 4 Selection | `04INS_Data.SelectionStreching04` | - | 0.55 | module_segment |
| Stretching Nipper 5 Selection | `04INS_Data.SelectionStreching05` | - | 0.55 | module_segment |
| Jogging Step Sequence (Chain) | `04INS_Data.SequenceJogging` | - | 0.55 | module_segment |
| Infeed Chain Saranex Sensor Zeroing (Softkey) | `04INS_Data.SoftkeyZeroSensorInCH` | - | 0.55 | module_segment |
| Infeed Chain Sensor Zeroing (Softkey) | `04INS_Data.SoftkeyZeroSensorInf` | - | 0.55 | module_segment |
| Lower Non-Woven Sensor Zeroing (Softkey) | `04INS_Data.SoftkeyZeroSensorLoNW` | - | 0.55 | module_segment |
| Non-Woven Sensor Zeroing (Softkey) | `04INS_Data.SoftkeyZeroSensorNW` | - | 0.55 | module_segment |
| PTFE Belt Sensor Zeroing (Softkey) | `04INS_Data.SoftkeyZeroSensorPTFE` | - | 0.55 | module_segment |
| Saranex Sensor Zeroing (Softkey) | `04INS_Data.SoftkeyZeroSensorSara` | - | 0.55 | module_segment |
| Station In Home Position Status | `04INS_Data.StatusInHomePosition` | - | 0.55 | module_segment |
| Foil Tack 1 Heater Actual Temperature | `04INS_Heater_Data.FT_1.ActualValue` | °C | 0.55 | module_segment |
| Foil Tack 1 Heater Heater On/Off Setpoint | `04INS_Heater_Data.FT_1.HeaterSelection` | - | 0.55 | module_segment |
| Foil Tack 1 Heater Lower Temperature Limit | `04INS_Heater_Data.FT_1.LowerBorder` | °C | 0.55 | module_segment |
| Foil Tack 1 Heater Upper Temperature Limit | `04INS_Heater_Data.FT_1.UpperBorder` | °C | 0.55 | module_segment |
| Foil Tack 2 Heater Actual Temperature | `04INS_Heater_Data.FT_2.ActualValue` | °C | 0.55 | module_segment |
| Foil Tack 2 Heater Heater On/Off Setpoint | `04INS_Heater_Data.FT_2.HeaterSelection` | - | 0.55 | module_segment |
| Foil Tack 2 Heater Lower Temperature Limit | `04INS_Heater_Data.FT_2.LowerBorder` | °C | 0.55 | module_segment |
| Foil Tack 2 Heater Upper Temperature Limit | `04INS_Heater_Data.FT_2.UpperBorder` | °C | 0.55 | module_segment |
| Foil Tack 3 Heater Actual Temperature | `04INS_Heater_Data.FT_3.ActualValue` | °C | 0.55 | module_segment |
| Foil Tack 3 Heater Heater On/Off Setpoint | `04INS_Heater_Data.FT_3.HeaterSelection` | - | 0.55 | module_segment |
| Foil Tack 3 Heater Lower Temperature Limit | `04INS_Heater_Data.FT_3.LowerBorder` | °C | 0.55 | module_segment |
| Foil Tack 3 Heater Upper Temperature Limit | `04INS_Heater_Data.FT_3.UpperBorder` | °C | 0.55 | module_segment |
| Foil Tack 4 Heater Actual Temperature | `04INS_Heater_Data.FT_4.ActualValue` | °C | 0.55 | module_segment |
| Foil Tack 4 Heater Heater On/Off Setpoint | `04INS_Heater_Data.FT_4.HeaterSelection` | - | 0.55 | module_segment |
| Foil Tack 4 Heater Lower Temperature Limit | `04INS_Heater_Data.FT_4.LowerBorder` | °C | 0.55 | module_segment |
| Foil Tack 4 Heater Upper Temperature Limit | `04INS_Heater_Data.FT_4.UpperBorder` | °C | 0.55 | module_segment |
| Foil Tack 5 Heater Actual Temperature | `04INS_Heater_Data.FT_5.ActualValue` | °C | 0.55 | module_segment |
| Foil Tack 5 Heater Heater On/Off Setpoint | `04INS_Heater_Data.FT_5.HeaterSelection` | - | 0.55 | module_segment |
| Foil Tack 5 Heater Lower Temperature Limit | `04INS_Heater_Data.FT_5.LowerBorder` | °C | 0.55 | module_segment |
| Foil Tack 5 Heater Upper Temperature Limit | `04INS_Heater_Data.FT_5.UpperBorder` | °C | 0.55 | module_segment |
| Servo Axis - Release For Zeroing | `04INS_Servo_Data.Servo.SP_ReleaseforZeroing` | - | 0.55 | module_segment |
| Servo Axis - Setting Mode | `04INS_Servo_Data.Servo.SP_SettingMode` | - | 0.55 | module_segment |
| Servo Axis - Zeroing Command | `04INS_Servo_Data.Servo.SP_Zeroing` | - | 0.55 | module_segment |
| Flange Check Selection (mounted after 11FWC) | `04INS_Data.SelectionFlangeCheck` | - | 0.60 | module_segment |
| Foil Tack 1 Selection | `04INS_Data.SelectionFoilTack01` | - | 0.60 | module_segment |
| Foil Tack 2 Selection | `04INS_Data.SelectionFoilTack02` | - | 0.60 | module_segment |
| Foil Tack 3 Selection | `04INS_Data.SelectionFoilTack03` | - | 0.60 | module_segment |
| Foil Tack 4 Selection | `04INS_Data.SelectionFoilTack04` | - | 0.60 | module_segment |
| Foil Tack 5 Selection | `04INS_Data.SelectionFoilTack05` | - | 0.60 | module_segment |
| Ionization Selection | `04INS_Data.SelectionIonization` | - | 0.60 | module_segment |
| All Nippers Open Selection | `04INS_Data.SelectionNippersOpen` | - | 0.60 | module_segment |
| PTFE Belt Selection | `04INS_Data.SelectionPTFEBelt` | - | 0.60 | module_segment |
| Upper Non-Woven Selection | `04INS_Data.SelectionUpperNW` | - | 0.60 | module_segment |
| Upper Saranex Film Selection | `04INS_Data.SelectionUpperSaranex` | - | 0.60 | module_segment |
| Servo Axis - Current Position (Display) | `04INS_Servo_Data.Servo.DSP_CurrentPosition` | - | 0.60 | module_segment |
| Servo Axis - Acceleration Setpoint 01 | `04INS_Servo_Data.Servo.SP_Acc_01` | - | 0.60 | module_segment |
| Servo Axis - Acceleration Setpoint 02 | `04INS_Servo_Data.Servo.SP_Acc_02` | - | 0.60 | module_segment |
| Servo Axis - Deceleration Setpoint 01 | `04INS_Servo_Data.Servo.SP_Dec_01` | - | 0.60 | module_segment |
| Servo Axis - Deceleration Setpoint 02 | `04INS_Servo_Data.Servo.SP_Dec_02` | - | 0.60 | module_segment |
| Servo Axis - Speed Setpoint 01 | `04INS_Servo_Data.Servo.SP_Speed_01` | - | 0.60 | module_segment |
| Servo Axis - Speed Setpoint 02 | `04INS_Servo_Data.Servo.SP_Speed_02` | - | 0.60 | module_segment |
| Foil Tack 1 Heater On/Off Setpoint | `DB_INS_Tack1.Heat.HeaterSelection` | - | 0.60 | module_segment |
| Foil Tack 2 Heater On/Off Setpoint | `DB_INS_Tack2.Heat.HeaterSelection` | - | 0.60 | module_segment |
| Foil Tack 3 Heater On/Off Setpoint | `DB_INS_Tack3.Heat.HeaterSelection` | - | 0.60 | module_segment |
| Foil Tack 4 Heater On/Off Setpoint | `DB_INS_Tack4.Heat.HeaterSelection` | - | 0.60 | module_segment |
| Foil Tack 5 Heater On/Off Setpoint | `DB_INS_Tack5.Heat.HeaterSelection` | - | 0.60 | module_segment |
| Foil Tack 1 Heater Target Temperature Setpoint | `04INS_Heater_Data.FT_1.TargetValue` | °C | 0.60 | module_segment |
| Foil Tack 2 Heater Target Temperature Setpoint | `04INS_Heater_Data.FT_2.TargetValue` | °C | 0.60 | module_segment |
| Foil Tack 3 Heater Target Temperature Setpoint | `04INS_Heater_Data.FT_3.TargetValue` | °C | 0.60 | module_segment |
| Foil Tack 4 Heater Target Temperature Setpoint | `04INS_Heater_Data.FT_4.TargetValue` | °C | 0.60 | module_segment |
| Foil Tack 5 Heater Target Temperature Setpoint | `04INS_Heater_Data.FT_5.TargetValue` | °C | 0.60 | module_segment |
| Infeed Chain Adjustment Sensor In Position | `04INS_Data.AdjInfeedChainInPosition` | - | 0.65 | module_segment |
| Non-Woven Adjustment Sensor In Position | `04INS_Data.AdjNWInPosition` | - | 0.65 | module_segment |
| PTFE Belt Adjustment Sensor In Position | `04INS_Data.AdjPTFEBeltInPosition` | - | 0.65 | module_segment |
| Saranex Adjustment Sensor In Position | `04INS_Data.AdjSaranexInPosition` | - | 0.65 | module_segment |
| Infeed Chain Saranex Position Sensor - Actual | `04INS_Data.ActualPositionSensorInCH` | - | 0.65 | module_segment |
| Infeed Chain Position Sensor - Actual | `04INS_Data.ActualPositionSensorInf` | - | 0.65 | module_segment |
| Lower Non-Woven Position Sensor - Actual | `04INS_Data.ActualPositionSensorLoNW` | - | 0.65 | module_segment |
| Non-Woven Position Sensor - Actual | `04INS_Data.ActualPositionSensorNW` | - | 0.65 | module_segment |
| PTFE Belt Position Sensor - Actual | `04INS_Data.ActualPositionSensorPTFE` | - | 0.65 | module_segment |
| Saranex Position Sensor - Actual | `04INS_Data.ActualPositionSensorSara` | - | 0.65 | module_segment |
| Infeed Chain Selection | `04INS_Data.SelectionInfeedChain` | - | 0.65 | module_segment |
| Semiautomatic Mode Selection | `04INS_Data.SelectionSemiAutomatic` | - | 0.65 | module_segment |
| Station Selection | `04INS_Data.SelectionStation` | - | 0.65 | module_segment |
| Infeed Chain Saranex Position Sensor - Setpoint | `04INS_Data.TargetPositionSensorInCH` | - | 0.65 | module_segment |
| Infeed Chain Position Sensor - Setpoint | `04INS_Data.TargetPositionSensorInf` | - | 0.65 | module_segment |
| Lower Non-Woven Position Sensor - Setpoint | `04INS_Data.TargetPositionSensorLoNW` | - | 0.65 | module_segment |
| Non-Woven Position Sensor - Setpoint | `04INS_Data.TargetPositionSensorNW` | - | 0.65 | module_segment |
| PTFE Belt Position Sensor - Setpoint | `04INS_Data.TargetPositionSensorPTFE` | - | 0.65 | module_segment |
| Saranex Position Sensor - Setpoint | `04INS_Data.TargetPositionSensorSara` | - | 0.65 | module_segment |
| Servo Axis - Position Setpoint 01 | `04INS_Servo_Data.Servo.SP_Position_01` | - | 0.65 | module_segment |
| Servo Axis - Position Setpoint 02 | `04INS_Servo_Data.Servo.SP_Position_02` | - | 0.65 | module_segment |
| Fault Count - Feed System | `Data_Collection_MPI_IOs.FAULT_COUNT_INS` | - | 0.70 | module_segment |
| Flange Check Testing Time | `04INS_Data.TestTimeFlangeCheck` | s | 0.70 | module_segment |
| Foil Tack 1 Welding Time | `04INS_Data.WeldingTimeTack01` | s | 0.75 | module_segment |
| Foil Tack 2 Welding Time | `04INS_Data.WeldingTimeTack02` | s | 0.75 | module_segment |
| Foil Tack 3 Welding Time | `04INS_Data.WeldingTimeTack03` | s | 0.75 | module_segment |
| Foil Tack 4 Welding Time | `04INS_Data.WeldingTimeTack04` | s | 0.75 | module_segment |
| Foil Tack 5 Welding Time | `04INS_Data.WeldingTimeTack05` | s | 0.75 | module_segment |

### FSR HP filter welding station (MC004-FSR)

- 320 candidate tag(s) considered -> 48 kept as genuine parameters (15%).
- Kept tags found by: 48 via *module_segment* (the tag name contains this station's own PLC/module code as a literal segment - the strongest signal available).
- 14 kept parameter(s) below 0.5 confidence - flagged with ⚠ below.

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| Jogging Sequence Mode ⚠ | `DB_FSR_Data.SequenceJogging` | - | 0.40 | module_segment |
| Jog Backward (Setting Mode) ⚠ | `DB_FSR_Data.Servo.SP_TippBWD` | - | 0.40 | module_segment |
| Jog Forward (Setting Mode) ⚠ | `DB_FSR_Data.Servo.SP_TippFWD` | - | 0.40 | module_segment |
| Zero Adjust X (Softkey) ⚠ | `DB_FSR_Data.SoftkeyZeroAdjustingX` | - | 0.40 | module_segment |
| Zero Adjust Y (Softkey) ⚠ | `DB_FSR_Data.SoftkeyZeroAdjustingY` | - | 0.40 | module_segment |
| Heater Controller Setting ⚠ | `DB_FSR_DataHeater.LH.ControlerSetting` | - | 0.40 | module_segment |
| Expeller Delay ⚠ | `FSR_Expeller_Delay` | s | 0.40 | module_segment |
| Station Selection ⚠ | `DB_FSR_Data.SelectionStation` | - | 0.45 | module_segment |
| Nominal Acceleration 01 ⚠ | `DB_FSR_Data.Servo.SP_Acc_01` | mm/s² | 0.45 | module_segment |
| Nominal Deceleration 01 ⚠ | `DB_FSR_Data.Servo.SP_Dec_01` | mm/s² | 0.45 | module_segment |
| Release for Zeroing ⚠ | `DB_FSR_Data.Servo.SP_ReleaseforZeroing` | - | 0.45 | module_segment |
| Zeroing Command ⚠ | `DB_FSR_Data.Servo.SP_Zeroing` | - | 0.45 | module_segment |
| Heater Solid State Output Status ⚠ | `DB_FSR_DataHeater.LH.OutputSSD` | - | 0.45 | module_segment |
| Continuous Reject (Open Nipper) ⚠ | `FSR_OpenNipper` | - | 0.45 | module_segment |
| Heater Temperature (DINT Representation) | `TEMP_CONVERSION.FSR_HEATER_TEMP` | °C | 0.50 | module_segment |
| Feed Nipper Belt Selection | `DB_FSR_Data.SelectionFeedNipperBelt` | - | 0.50 | module_segment |
| Semi-Automatic Mode Selection | `DB_FSR_Data.SelectionSemiAutomatic` | - | 0.50 | module_segment |
| Vision System Reject Count (Non-resettable) | `Data_Collection_MPI_IOs.FSR_Vision_Rejects_Act` | count | 0.55 | module_segment |
| Filter Check Sensor 1 | `07FSR_06_S1` | - | 0.55 | module_segment |
| Filter Check Sensor 2 | `07FSR_06_S2` | - | 0.55 | module_segment |
| Filter Check Sensor 3 | `07FSR_06_S3` | - | 0.55 | module_segment |
| Filter Position Sensor | `07FSR_PositionFilter` | - | 0.55 | module_segment |
| Distance 1 | `DB_FSR_Data.Distance_1` | mm | 0.55 | module_segment |
| Distance 2 | `DB_FSR_Data.Distance_2` | mm | 0.55 | module_segment |
| Distance 4 | `DB_FSR_Data.Distance_4` | mm | 0.55 | module_segment |
| Distance 5 | `DB_FSR_Data.Distance_5` | mm | 0.55 | module_segment |
| Punch Selection | `DB_FSR_Data.SelectionPunch` | - | 0.55 | module_segment |
| Nominal Speed 01 | `DB_FSR_Data.Servo.SP_Speed_01` | mm/s | 0.55 | module_segment |
| Reject Parts Counter (Filter Vision, Right) | `Data_Collection_MPI_IOs.Counter_Reject_FSR_Cam` | count | 0.60 | module_segment |
| Filter Check Selection | `DB_FSR_Data.SelectionFilterCheck` | - | 0.60 | module_segment |
| Target Hole Punch Time | `DB_FSR_Data.TargetHolePunchTime` | s | 0.60 | module_segment |
| Target Periphery Punch Time | `DB_FSR_Data.TargetPeripheryPunchTime` | s | 0.60 | module_segment |
| Heater ON/OFF Setpoint | `DB_FSR_DataHeater.LH.HeaterSelection` | - | 0.60 | module_segment |
| Actual X-Adjustment | `DB_FSR_Data.ActualXAdjustment` | mm | 0.65 | module_segment |
| Actual Y-Adjustment | `DB_FSR_Data.ActualYAdjustment` | mm | 0.65 | module_segment |
| Current Servo Position | `DB_FSR_Data.Servo.DSP_CurrentPosition` | mm | 0.65 | module_segment |
| Nominal Position 01 | `DB_FSR_Data.Servo.SP_Position_01` | mm | 0.65 | module_segment |
| Nominal Position 02 | `DB_FSR_Data.Servo.SP_Position_02` | mm | 0.65 | module_segment |
| Target X-Adjustment | `DB_FSR_Data.TargetXAdjustment` | mm | 0.65 | module_segment |
| Target Y-Adjustment | `DB_FSR_Data.TargetYAdjustment` | mm | 0.65 | module_segment |
| Heater Lower Temperature Limit | `DB_FSR_DataHeater.LH.LowerBorder` | °C | 0.65 | module_segment |
| Heater Upper Temperature Limit | `DB_FSR_DataHeater.LH.UpperBorder` | °C | 0.65 | module_segment |
| Actual Steps to Filter End | `DB_FSR_Data.ActualStepsFilterEnd` | steps | 0.70 | module_segment |
| Target Steps Filter End | `DB_FSR_Data.TargetStepsFilterEnd` | steps | 0.70 | module_segment |
| Heater Temperature Correction Value | `DB_FSR_DataHeater.LH.CorrectionValue` | 1/10 °C | 0.70 | module_segment |
| Target Welding Time | `DB_FSR_Data.TargetWeldingTime` | s | 0.75 | module_segment |
| Actual Heater Temperature | `DB_FSR_DataHeater.LH.ActualValue` | °C | 0.75 | module_segment |
| Heater Nominal Temperature Setpoint | `DB_FSR_DataHeater.LH.TargetValue` | °C | 0.80 | module_segment |

### FSL HP filter welding station (MC004-FSL)

- 325 candidate tag(s) considered -> 55 kept as genuine parameters (17%).
- Kept tags found by: 55 via *module_segment* (the tag name contains this station's own PLC/module code as a literal segment - the strongest signal available).
- 15 kept parameter(s) below 0.5 confidence - flagged with ⚠ below.

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| Jogging Sequence Mode ⚠ | `DB_FSL_Data.SequenceJogging` | - | 0.40 | module_segment |
| Release for Zeroing (Alt) ⚠ | `DB_FSL_Data.Servo.SP_ReleaseforZeroing_0` | - | 0.40 | module_segment |
| Jog Forward (Setting Mode) ⚠ | `DB_FSL_Data.Servo.SP_TippFWD` | - | 0.40 | module_segment |
| Zero Adjust X (Softkey) ⚠ | `DB_FSL_Data.SoftkeyZeroAdjustingX` | - | 0.40 | module_segment |
| Zero Adjust Y (Softkey) ⚠ | `DB_FSL_Data.SoftkeyZeroAdjustingY` | - | 0.40 | module_segment |
| Heater Controller Setting ⚠ | `DB_FSL_DataHeater.LH.ControlerSetting` | - | 0.40 | module_segment |
| Expeller Delay ⚠ | `FSL_Expeller_Delay` | s | 0.40 | module_segment |
| Punch Selection (Alt) ⚠ | `DB_FSL_Data.SelectionPunch_0` | - | 0.45 | module_segment |
| Station Selection ⚠ | `DB_FSL_Data.SelectionStation` | - | 0.45 | module_segment |
| Nominal Acceleration 01 ⚠ | `DB_FSL_Data.Servo.SP_Acc_01` | mm/s² | 0.45 | module_segment |
| Nominal Deceleration 01 ⚠ | `DB_FSL_Data.Servo.SP_Dec_01` | mm/s² | 0.45 | module_segment |
| Release for Zeroing ⚠ | `DB_FSL_Data.Servo.SP_ReleaseforZeroing` | - | 0.45 | module_segment |
| Belt Welding Sequence Step ⚠ | `DB_FSL_Data.SQ_BeltWelding` | - | 0.45 | module_segment |
| Heater Solid State Output Status ⚠ | `DB_FSL_DataHeater.LH.OutputSSD` | - | 0.45 | module_segment |
| Continuous Reject (Open Nipper) ⚠ | `FSL_OpenNipper` | - | 0.45 | module_segment |
| Heater Temperature (DINT Representation) | `TEMP_CONVERSION.FSL_HEATER_TEMP` | °C | 0.50 | module_segment |
| Feed Nipper Belt Selection | `DB_FSL_Data.SelectionFeedNipperBelt` | - | 0.50 | module_segment |
| Semi-Automatic Mode Selection | `DB_FSL_Data.SelectionSemiAutomatic` | - | 0.50 | module_segment |
| Start Belt Welding | `DB_FSL_Data.SK_StartBeltWelding` | - | 0.50 | module_segment |
| Stop Belt Welding | `DB_FSL_Data.SK_StopBeltWelding` | - | 0.50 | module_segment |
| Vision System Reject Count (Non-resettable) | `Data_Collection_MPI_IOs.FSL_Vision_Rejects_Act` | count | 0.55 | module_segment |
| Filter Check Sensor 1 | `06FSL_06_S1` | - | 0.55 | module_segment |
| Filter Check Sensor 2 | `06FSL_06_S2` | - | 0.55 | module_segment |
| Filter Check Sensor 3 | `06FSL_06_S3` | - | 0.55 | module_segment |
| Distance 1 | `DB_FSL_Data.Distance_1` | mm | 0.55 | module_segment |
| Distance 2 | `DB_FSL_Data.Distance_2` | mm | 0.55 | module_segment |
| Distance 3 | `DB_FSL_Data.Distance_3` | mm | 0.55 | module_segment |
| Distance 4 | `DB_FSL_Data.Distance_4` | mm | 0.55 | module_segment |
| Distance 5 | `DB_FSL_Data.Distance_5` | mm | 0.55 | module_segment |
| Belt Welding Selection | `DB_FSL_Data.SelectionBeltWelding` | - | 0.55 | module_segment |
| Punch Selection | `DB_FSL_Data.SelectionPunch` | - | 0.55 | module_segment |
| Nominal Speed 01 | `DB_FSL_Data.Servo.SP_Speed_01` | mm/s | 0.55 | module_segment |
| Reject Parts Counter (Filter Vision, Left) | `Data_Collection_MPI_IOs.Counter_Reject_FSL_Cam` | count | 0.60 | module_segment |
| Filter Check Selection | `DB_FSL_Data.SelectionFilterCheck` | - | 0.60 | module_segment |
| Nominal Position 04 | `DB_FSL_Data.Servo.SP_Position_04` | mm | 0.60 | module_segment |
| Target Hole Punch Time | `DB_FSL_Data.TargetHolePunchTime` | s | 0.60 | module_segment |
| Target Periphery Punch Time | `DB_FSL_Data.TargetPeripheryPunchTime` | s | 0.60 | module_segment |
| Heater ON/OFF Setpoint | `DB_FSL_DataHeater.LH.HeaterSelection` | - | 0.60 | module_segment |
| Actual Cooling Temperature | `DB_FSL_Data.ActualCoolingTemperatur` | °C | 0.65 | module_segment |
| Actual X-Adjustment | `DB_FSL_Data.ActualXAdjustment` | mm | 0.65 | module_segment |
| Actual Y-Adjustment | `DB_FSL_Data.ActualYAdjustment` | mm | 0.65 | module_segment |
| Current Servo Position | `DB_FSL_Data.Servo.DSP_CurrentPosition` | mm | 0.65 | module_segment |
| Nominal Position 01 | `DB_FSL_Data.Servo.SP_Position_01` | mm | 0.65 | module_segment |
| Nominal Position 02 | `DB_FSL_Data.Servo.SP_Position_02` | mm | 0.65 | module_segment |
| Target X-Adjustment | `DB_FSL_Data.TargetXAdjustment` | mm | 0.65 | module_segment |
| Target Y-Adjustment | `DB_FSL_Data.TargetYAdjustment` | mm | 0.65 | module_segment |
| Heater Lower Temperature Limit | `DB_FSL_DataHeater.LH.LowerBorder` | °C | 0.65 | module_segment |
| Heater Upper Temperature Limit | `DB_FSL_DataHeater.LH.UpperBorder` | °C | 0.65 | module_segment |
| Actual Steps to Filter End | `DB_FSL_Data.ActualStepsFilterEnd` | steps | 0.70 | module_segment |
| Target Cooling Temperature | `DB_FSL_Data.TargetCoolingTemperature` | °C | 0.70 | module_segment |
| Target Steps Filter End | `DB_FSL_Data.TargetStepsFilterEnd` | steps | 0.70 | module_segment |
| Heater Temperature Correction Value | `DB_FSL_DataHeater.LH.CorrectionValue` | 1/10 °C | 0.70 | module_segment |
| Target Welding Time | `DB_FSL_Data.TargetWeldingTime` | s | 0.75 | module_segment |
| Actual Heater Temperature | `DB_FSL_DataHeater.LH.ActualValue` | °C | 0.75 | module_segment |
| Heater Nominal Temperature Setpoint | `DB_FSL_DataHeater.LH.TargetValue` | °C | 0.80 | module_segment |

### PRI printing unit (MC004-PRI)

- 49 candidate tag(s) considered -> 12 kept as genuine parameters (24%).
- Kept tags found by: 12 via *module_segment* (the tag name contains this station's own PLC/module code as a literal segment - the strongest signal available).

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| X Reference OK | `DB_PRI_Data.DISP_Xref_ok` | - | 0.50 | module_segment |
| Heater Temperature (Converted) - Left | `TEMP_CONVERSION.PRIL_HEATER_TEMP` | °C | 0.50 | module_segment |
| Heater Temperature (Converted) - Right | `TEMP_CONVERSION.PRIR_HEATER_TEMP` | °C | 0.50 | module_segment |
| X Position OK | `DB_PRI_Data.DISP_Xpos_ok` | - | 0.55 | module_segment |
| Heater Actual Temperature - Left | `DB_PRI_DataHeater.LHS.ActualValue` | °C | 0.60 | module_segment |
| Heater Target Temperature - Left | `DB_PRI_DataHeater.LHS.TargetValue` | °C | 0.60 | module_segment |
| Heater Actual Temperature - Right | `DB_PRI_DataHeater.RHS.ActualValue` | °C | 0.60 | module_segment |
| Heater Target Temperature - Right | `DB_PRI_DataHeater.RHS.TargetValue` | °C | 0.60 | module_segment |
| Actual X Adjustment | `DB_PRI_Data.ActualXAdjustment` | 0.1 mm | 0.65 | module_segment |
| Target X Adjustment | `DB_PRI_Data.TargetXAdjustment` | 0.1 mm | 0.65 | module_segment |
| Embossing/Printing Time - Left | `DB_PRI_Data.TargetPrintingTimeLeft` | s | 0.70 | module_segment |
| Embossing/Printing Time - Right | `DB_PRI_Data.TargetPrintingTimeRight` | s | 0.70 | module_segment |

### FHP/FPW flange hole-punch unit (MC004-FHP)

- 77 candidate tag(s) considered -> 38 kept as genuine parameters (49%).
- Kept tags found by: 38 via *module_segment* (the tag name contains this station's own PLC/module code as a literal segment - the strongest signal available).
- 1 kept parameter(s) below 0.5 confidence - flagged with ⚠ below.

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| Upper Hole Punch Selection (Non-Woven) ⚠ | `FHP_SelUpperPunch` | - | 0.40 | module_segment |
| Upper Left Punch - X Reference OK | `DB_FHP_UL_Data.DISP_Xref_ok_UpperLeft` | - | 0.50 | module_segment |
| LowerLeft Punch - X Position OK | `DB_FHP_LL_Data.DISP_Xpos_ok_LowerLeft` | - | 0.55 | module_segment |
| LowerLeft Punch - Y Position OK | `DB_FHP_LL_Data.DISP_Ypos_ok_LowerLeft` | - | 0.55 | module_segment |
| LowerRight Punch - X Position OK | `DB_FHP_LR_Data.DISP_Xpos_ok_LowerRight` | - | 0.55 | module_segment |
| LowerRight Punch - Y Position OK | `DB_FHP_LR_Data.DISP_Ypos_ok_LowerRight` | - | 0.55 | module_segment |
| UpperLeft Punch - X Position OK | `DB_FHP_UL_Data.DISP_Xpos_ok_UpperLeft` | - | 0.55 | module_segment |
| UpperLeft Punch - Y Position OK | `DB_FHP_UL_Data.DISP_Ypos_ok_UpperLeft` | - | 0.55 | module_segment |
| UpperRight Punch - X Position OK | `DB_FHP_UR_Data.DISP_Xpos_ok_UpperRight` | - | 0.55 | module_segment |
| UpperRight Punch - Y Position OK | `DB_FHP_UR_Data.DISP_Ypos_ok_UpperRight` | - | 0.55 | module_segment |
| LowerLeft Punch - Target Expeller Delay | `DB_FHP_LL_Data.TargetDelayPusherTime` | s | 0.65 | module_segment |
| LowerRight Punch - Target Expeller Delay | `DB_FHP_LR_Data.TargetDelayPusherTime` | s | 0.65 | module_segment |
| UpperLeft Punch - Target Expeller Delay | `DB_FHP_UL_Data.TargetDelayPusherTime` | s | 0.65 | module_segment |
| UpperRight Punch - Target Expeller Delay | `DB_FHP_UR_Data.TargetDelayPusherTime` | s | 0.65 | module_segment |
| LowerLeft Punch - Actual Punching Time | `DB_FHP_LL_Data.ActualPunchTime` | s | 0.70 | module_segment |
| LowerLeft Punch - Target Punching Time | `DB_FHP_LL_Data.TargetPunchTime` | s | 0.70 | module_segment |
| LowerRight Punch - Actual Punching Time | `DB_FHP_LR_Data.ActualPunchTime` | s | 0.70 | module_segment |
| LowerRight Punch - Target Punching Time | `DB_FHP_LR_Data.TargetPunchTime` | s | 0.70 | module_segment |
| UpperLeft Punch - Actual Punching Time | `DB_FHP_UL_Data.ActualPunchTime` | s | 0.70 | module_segment |
| UpperLeft Punch - Target Punching Time | `DB_FHP_UL_Data.TargetPunchTime` | s | 0.70 | module_segment |
| UpperRight Punch - Actual Punching Time | `DB_FHP_UR_Data.ActualPunchTime` | s | 0.70 | module_segment |
| UpperRight Punch - Target Punching Time | `DB_FHP_UR_Data.TargetPunchTime` | s | 0.70 | module_segment |
| LowerLeft Punch - Actual X Adjustment | `DB_FHP_LL_Data.ActualXAdjust_LowerLeft` | 0.1 mm | 0.75 | module_segment |
| LowerLeft Punch - Actual Y Adjustment | `DB_FHP_LL_Data.ActualYAdjust_LowerLeft` | 0.1 mm | 0.75 | module_segment |
| LowerRight Punch - Actual X Adjustment | `DB_FHP_LR_Data.ActualXAdjust_LowerRight` | 0.1 mm | 0.75 | module_segment |
| LowerRight Punch - Actual Y Adjustment | `DB_FHP_LR_Data.ActualYAdjust_LowerRight` | 0.1 mm | 0.75 | module_segment |
| UpperLeft Punch - Actual X Adjustment | `DB_FHP_UL_Data.ActualXAdjust_UpperLeft` | 0.1 mm | 0.75 | module_segment |
| UpperLeft Punch - Actual Y Adjustment | `DB_FHP_UL_Data.ActualYAdjust_UpperLeft` | 0.1 mm | 0.75 | module_segment |
| UpperRight Punch - Actual X Adjustment | `DB_FHP_UR_Data.ActualXAdjust_UpperRight` | 0.1 mm | 0.75 | module_segment |
| UpperRight Punch - Actual Y Adjustment | `DB_FHP_UR_Data.ActualYAdjust_UpperRight` | 0.1 mm | 0.75 | module_segment |
| LowerLeft Punch - Target X Adjustment | `DB_FHP_LL_Data.TargetXAdjust_LowerLeft` | 0.1 mm | 0.80 | module_segment |
| LowerLeft Punch - Target Y Adjustment | `DB_FHP_LL_Data.TargetYAdjust_LowerLeft` | 0.1 mm | 0.80 | module_segment |
| LowerRight Punch - Target X Adjustment | `DB_FHP_LR_Data.TargetXAdjust_LowerRight` | 0.1 mm | 0.80 | module_segment |
| LowerRight Punch - Target Y Adjustment | `DB_FHP_LR_Data.TargetYAdjust_LowerRight` | 0.1 mm | 0.80 | module_segment |
| UpperLeft Punch - Target X Adjustment | `DB_FHP_UL_Data.TargetXAdjust_UpperLeft` | 0.1 mm | 0.80 | module_segment |
| UpperLeft Punch - Target Y Adjustment | `DB_FHP_UL_Data.TargetYAdjust_UpperLeft` | 0.1 mm | 0.80 | module_segment |
| UpperRight Punch - Target X Adjustment | `DB_FHP_UR_Data.TargetXAdjust_UpperRight` | 0.1 mm | 0.80 | module_segment |
| UpperRight Punch - Target Y Adjustment | `DB_FHP_UR_Data.TargetYAdjust_UpperRight` | 0.1 mm | 0.80 | module_segment |

### BSW welding unit, BACKING SEAL (MC004-BSW)

- 146 candidate tag(s) considered -> 20 kept as genuine parameters (14%).
- Kept tags found by: 20 via *module_segment* (the tag name contains this station's own PLC/module code as a literal segment - the strongest signal available).
- 3 kept parameter(s) below 0.5 confidence - flagged with ⚠ below.

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| Station Status Word ⚠ | `BSW` | - | 0.30 | module_segment |
| Upper Heater Controller Setting ⚠ | `DB_BSW_HeaterData.UH.ControlerSetting` | % | 0.45 | module_segment |
| Upper Heater Correction Value ⚠ | `DB_BSW_HeaterData.UH.CorrectionValue` | - | 0.45 | module_segment |
| Upper Heater Scale Curve Y Maximum | `DB_BSW_HeaterData.UH.YScaleMax` | °C | 0.50 | module_segment |
| Upper Heater Scale Curve Y Minimum | `DB_BSW_HeaterData.UH.YScaleMin` | °C | 0.50 | module_segment |
| Jogging Step Sequence | `DB_BSW_Data.SequenceJogging` | - | 0.55 | module_segment |
| X-Adjustment Zeroing (Softkey) | `DB_BSW_Data.SoftkeyZeroAdjustingX` | - | 0.55 | module_segment |
| X-Position OK (Display) | `DB_BSW_Data.DISP_Xpos_ok` | - | 0.60 | module_segment |
| Heater On/Off Setpoint | `BSW_HeaterSelection` | - | 0.60 | module_segment |
| Upper Heater Actual Temperature | `DB_BSW_HeaterData.UH.ActualValue` | °C | 0.60 | module_segment |
| Upper Heater Lower Temperature Limit | `DB_BSW_HeaterData.UH.LowerBorder` | °C | 0.60 | module_segment |
| Upper Heater Solid State Relay Output | `DB_BSW_HeaterData.UH.OutputSSD` | - | 0.60 | module_segment |
| Upper Heater Upper Temperature Limit | `DB_BSW_HeaterData.UH.UpperBorder` | °C | 0.60 | module_segment |
| Semiautomatic Mode Selection | `DB_BSW_Data.SelectionSemiAutomatic` | - | 0.65 | module_segment |
| Station Selection | `DB_BSW_Data.SelectionStation` | - | 0.65 | module_segment |
| Upper Heater Heater On/Off Setpoint | `DB_BSW_HeaterData.UH.HeaterSelection` | - | 0.65 | module_segment |
| Upper Heater Target Temperature Setpoint | `DB_BSW_HeaterData.UH.TargetValue` | °C | 0.65 | module_segment |
| X-Adjustment - Actual | `DB_BSW_Data.ActualXAdjustment` | 1/10 mm | 0.75 | module_segment |
| X-Adjustment - Setpoint | `DB_BSW_Data.TargetXAdjustment` | 1/10 mm | 0.75 | module_segment |
| Welding Time Setpoint | `DB_BSW_Data.TargetWeldingTime` | s | 0.80 | module_segment |

### FFG feeder turntable, GASKET (MC004-FFG)

- 53 candidate tag(s) considered -> 24 kept as genuine parameters (45%).
- Kept tags found by: 24 via *module_segment* (the tag name contains this station's own PLC/module code as a literal segment - the strongest signal available).

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| Pivoting Arm - Nominal Acceleration 01 | `DB_FFG_Data.pivotingarm.SP_Acc_01` | - | 0.55 | module_segment |
| Pivoting Arm - Nominal Acceleration 02 | `DB_FFG_Data.pivotingarm.SP_Acc_02` | - | 0.55 | module_segment |
| Pivoting Arm - Nominal Acceleration 03 | `DB_FFG_Data.pivotingarm.SP_Acc_03` | - | 0.55 | module_segment |
| Pivoting Arm - Nominal Deceleration 01 | `DB_FFG_Data.pivotingarm.SP_Dec_01` | - | 0.55 | module_segment |
| Pivoting Arm - Nominal Deceleration 02 | `DB_FFG_Data.pivotingarm.SP_Dec_02` | - | 0.55 | module_segment |
| Pivoting Arm - Nominal Deceleration 03 | `DB_FFG_Data.pivotingarm.SP_Dec_03` | - | 0.55 | module_segment |
| Pivoting Arm - Nominal Speed 01 | `DB_FFG_Data.pivotingarm.SP_Speed_01` | - | 0.55 | module_segment |
| Pivoting Arm - Nominal Speed 02 | `DB_FFG_Data.pivotingarm.SP_Speed_02` | - | 0.55 | module_segment |
| Pivoting Arm - Nominal Speed 03 | `DB_FFG_Data.pivotingarm.SP_Speed_03` | - | 0.55 | module_segment |
| Pivoting Drive - Position Confirmed 1 | `09FFG_03_B1a` | - | 0.55 | module_segment |
| Pivoting Drive - Position Confirmed 2 | `09FFG_03_B1b` | - | 0.55 | module_segment |
| Pivoting Arm - Current Position (Display) | `DB_FFG_Data.pivotingarm.DSP_CurrentPosition` | - | 0.60 | module_segment |
| Pivoting Arm - In Position 1 | `DB_FFG_Data.pivotingarm.DSP_Pos1` | - | 0.60 | module_segment |
| Pivoting Arm - In Position 2 | `DB_FFG_Data.pivotingarm.DSP_Pos2` | - | 0.60 | module_segment |
| Pivoting Arm - In Position 3 | `DB_FFG_Data.pivotingarm.DSP_Pos3` | - | 0.60 | module_segment |
| Pivoting Arm - Nominal Position 01 | `DB_FFG_Data.pivotingarm.SP_Position_01` | - | 0.60 | module_segment |
| Pivoting Arm - Nominal Position 02 | `DB_FFG_Data.pivotingarm.SP_Position_02` | - | 0.60 | module_segment |
| Pivoting Arm - Nominal Position 03 | `DB_FFG_Data.pivotingarm.SP_Position_03` | - | 0.60 | module_segment |
| Extractor Down Delay | `DB_FFG_Data.ExtractorDownDelay` | s | 0.65 | module_segment |
| Extractor Middle Position Delay | `DB_FFG_Data.ExtractorMiddleDelay` | s | 0.65 | module_segment |
| Gripper Closing Delay | `DB_FFG_Data.GripperClosingDelay` | s | 0.65 | module_segment |
| Gripper Opening Delay | `DB_FFG_Data.GripperOpeningDelay` | s | 0.65 | module_segment |
| Current Cycles After Gasket Finish | `DB_FFG_Data.ActualRemCycles` | cycles | 0.70 | module_segment |
| Nominal Cycles After Gasket Finish Recognition | `DB_FFG_Data.TargetRemCycles` | cycles | 0.70 | module_segment |

### FFB feeder turntable, BARRIER (MC004-FFB)

- 70 candidate tag(s) considered -> 35 kept as genuine parameters (50%).
- Kept tags found by: 35 via *module_segment* (the tag name contains this station's own PLC/module code as a literal segment - the strongest signal available).

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| Spare Delay Time | `DB_FFB_Data.DelaySpare` | s | 0.50 | module_segment |
| Pivoting Drive - Parts Check 1 | `10FFB_03_B2a` | - | 0.50 | module_segment |
| Pivoting Drive - Parts Check 2 | `10FFB_03_B2b` | - | 0.50 | module_segment |
| Lift Drive - Nominal Acceleration 01 | `DB_FFB_Data.liftdrive.SP_Acc_01` | - | 0.55 | module_segment |
| Lift Drive - Nominal Acceleration 02 | `DB_FFB_Data.liftdrive.SP_Acc_02` | - | 0.55 | module_segment |
| Lift Drive - Nominal Deceleration 01 | `DB_FFB_Data.liftdrive.SP_Dec_01` | - | 0.55 | module_segment |
| Lift Drive - Nominal Deceleration 02 | `DB_FFB_Data.liftdrive.SP_Dec_02` | - | 0.55 | module_segment |
| Lift Drive - Nominal Speed 01 | `DB_FFB_Data.liftdrive.SP_Speed_01` | - | 0.55 | module_segment |
| Lift Drive - Nominal Speed 02 | `DB_FFB_Data.liftdrive.SP_Speed_02` | - | 0.55 | module_segment |
| Pivoting Drive - Nominal Acceleration 01 | `DB_FFB_Data.pivotingdrive.SP_Acc_01` | - | 0.55 | module_segment |
| Pivoting Drive - Nominal Acceleration 02 | `DB_FFB_Data.pivotingdrive.SP_Acc_02` | - | 0.55 | module_segment |
| Pivoting Drive - Nominal Acceleration 03 | `DB_FFB_Data.pivotingdrive.SP_Acc_03` | - | 0.55 | module_segment |
| Pivoting Drive - Nominal Deceleration 01 | `DB_FFB_Data.pivotingdrive.SP_Dec_01` | - | 0.55 | module_segment |
| Pivoting Drive - Nominal Deceleration 02 | `DB_FFB_Data.pivotingdrive.SP_Dec_02` | - | 0.55 | module_segment |
| Pivoting Drive - Nominal Deceleration 03 | `DB_FFB_Data.pivotingdrive.SP_Dec_03` | - | 0.55 | module_segment |
| Pivoting Drive - Nominal Speed 01 | `DB_FFB_Data.pivotingdrive.SP_Speed_01` | - | 0.55 | module_segment |
| Pivoting Drive - Nominal Speed 02 | `DB_FFB_Data.pivotingdrive.SP_Speed_02` | - | 0.55 | module_segment |
| Pivoting Drive - Nominal Speed 03 | `DB_FFB_Data.pivotingdrive.SP_Speed_03` | - | 0.55 | module_segment |
| Pivoting Drive - Position Confirmed 1 | `10FFB_03_B1a` | - | 0.55 | module_segment |
| Pivoting Drive - Position Confirmed 2 | `10FFB_03_B1b` | - | 0.55 | module_segment |
| Lift Drive - Current Position (Display) | `DB_FFB_Data.liftdrive.DSP_CurrentPosition` | - | 0.60 | module_segment |
| Lift Drive - Nominal Position 01 | `DB_FFB_Data.liftdrive.SP_Position_01` | - | 0.60 | module_segment |
| Lift Drive - Nominal Position 02 | `DB_FFB_Data.liftdrive.SP_Position_02` | - | 0.60 | module_segment |
| Pivoting Drive - Current Position (Display) | `DB_FFB_Data.pivotingdrive.DSP_CurrentPosition` | - | 0.60 | module_segment |
| Pivoting Drive - In Position 1 | `DB_FFB_Data.pivotingdrive.DSP_Pos1` | - | 0.60 | module_segment |
| Pivoting Drive - In Position 2 | `DB_FFB_Data.pivotingdrive.DSP_Pos2` | - | 0.60 | module_segment |
| Pivoting Drive - In Position 3 | `DB_FFB_Data.pivotingdrive.DSP_Pos3` | - | 0.60 | module_segment |
| Pivoting Drive - In Position 4 | `DB_FFB_Data.pivotingdrive.DSP_Pos4` | - | 0.60 | module_segment |
| Pivoting Drive - Nominal Position 01 | `DB_FFB_Data.pivotingdrive.SP_Position_01` | - | 0.60 | module_segment |
| Pivoting Drive - Nominal Position 02 | `DB_FFB_Data.pivotingdrive.SP_Position_02` | - | 0.60 | module_segment |
| Pivoting Drive - Nominal Position 03 | `DB_FFB_Data.pivotingdrive.SP_Position_03` | - | 0.60 | module_segment |
| Residual Quantity in Magazine (Stack Height) | `DB_FFB_Data.StackHight` | - | 0.65 | module_segment |
| Pick & Place Horizontal Forward Delay | `DB_FFB_Data.DelayHorizontalForward` | s | 0.70 | module_segment |
| Pick & Place Blow-Off Time | `DB_FFB_Data.BlowOffTime` | s | 0.70 | module_segment |
| Pick & Place Suction Time | `DB_FFB_Data.SuctionTime` | s | 0.70 | module_segment |

### FWC 4S-S welding station, flange (MC004-FWC)

- 158 candidate tag(s) considered -> 31 kept as genuine parameters (20%).
- Kept tags found by: 28 via *module_segment* (the tag name contains this station's own PLC/module code as a literal segment - the strongest signal available), 3 via *unknown* (unrecognized match type).
- 4 kept parameter(s) below 0.5 confidence - flagged with ⚠ below.

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| Station Status Word ⚠ | `FWC` | - | 0.30 | module_segment |
| Left Hand Heater Controller Setting ⚠ | `DB_FWC_DataHeater.LH.ControlerSetting` | % | 0.40 | module_segment |
| Left Hand Heater Correction Value ⚠ | `DB_FWC_DataHeater.LH.CorrectionValue` | - | 0.40 | unknown |
| Left Hand Heater Zone Status ⚠ | `DB_FWC_DataHeater.LH.Heater` | - | 0.45 | module_segment |
| Left Hand Heater Scale Curve Y Maximum | `DB_FWC_DataHeater.LH.YScaleMax` | °C | 0.50 | module_segment |
| Left Hand Heater Scale Curve Y Minimum | `DB_FWC_DataHeater.LH.YScaleMin` | °C | 0.50 | module_segment |
| Left Side Selection | `DB_FWC_Data.SelectionLeft` | - | 0.55 | module_segment |
| Right Side Selection | `DB_FWC_Data.SelectionRight` | - | 0.55 | module_segment |
| Jogging Step Sequence | `DB_FWC_Data.SequenceJogging` | - | 0.55 | module_segment |
| Z-Adjustment Zeroing (Softkey) - Left | `DB_FWC_Data.SoftkeyZeroAdjZLeft` | - | 0.55 | module_segment |
| Z-Adjustment Zeroing (Softkey) - Right | `DB_FWC_Data.SoftkeyZeroAdjZRight` | - | 0.55 | module_segment |
| Left Hand Heater Actual Temperature | `DB_FWC_DataHeater.LH.ActualValue` | °C | 0.55 | module_segment |
| Left Hand Heater Lower Temperature Limit | `DB_FWC_DataHeater.LH.LowerBorder` | °C | 0.55 | unknown |
| Left Hand Heater Upper Temperature Limit | `DB_FWC_DataHeater.LH.UpperBorder` | °C | 0.55 | unknown |
| Z-Position OK - Left | `DB_FWC_Data.DISP_Zpos_okLeft` | - | 0.60 | module_segment |
| Z-Position OK - Right | `DB_FWC_Data.DISP_Zpos_okRight` | - | 0.60 | module_segment |
| Left Hand Heater Target Temperature Setpoint | `DB_FWC_DataHeater.LH.TargetValue` | °C | 0.60 | module_segment |
| Cooling Station Preselection | `DB_FWC_Data.SelectionCooling` | - | 0.65 | module_segment |
| Flange Check Preselection | `DB_FWC_Data.SelectionFlangeCheck` | - | 0.65 | module_segment |
| Semiautomatic Mode Selection | `DB_FWC_Data.SelectionSemiAutomatic` | - | 0.65 | module_segment |
| Station Selection - Left | `DB_FWC_Data.SelectionStationLeft` | - | 0.65 | module_segment |
| Station Selection - Right | `DB_FWC_Data.SelectionStationRight` | - | 0.65 | module_segment |
| Left Hand Heater Solid State Relay Output | `DB_FWC_DataHeater.LH.OutputSSD` | - | 0.70 | module_segment |
| Cooling Time Setpoint | `DB_FWC_Data.TargetCoolingTime` | s | 0.75 | module_segment |
| Left Hand Heater Heater On/Off Setpoint | `DB_FWC_DataHeater.LH.HeaterSelection` | - | 0.75 | module_segment |
| Welding Time Setpoint - Left | `DB_FWC_Data.TargetWeldingTimeLeft` | s | 0.80 | module_segment |
| Welding Time Setpoint - Right | `DB_FWC_Data.TargetWeldingTimeRight` | s | 0.80 | module_segment |
| Height Adjustment Z - Actual (Left) | `DB_FWC_Data.ActualZAdjustmentLeft` | 1/100 mm | 0.85 | module_segment |
| Height Adjustment Z - Actual (Right) | `DB_FWC_Data.ActualZAdjustmentRight` | 1/100 mm | 0.85 | module_segment |
| Height Adjustment Z - Setpoint (Left) | `DB_FWC_Data.TargetZAdjustmentLeft` | 1/100 mm | 0.85 | module_segment |
| Height Adjustment Z - Setpoint (Right) | `DB_FWC_Data.TargetZAdjustmentRight` | 1/100 mm | 0.85 | module_segment |

### ABF Binder FLAP stamping/welding unit (MC004-ABF)

- 12 candidate tag(s) considered -> 0 kept as genuine parameters (0%).

_No genuine parameters found among this station's candidates._

### ASB labelling unit, binder (MC004-ASB)

- 54 candidate tag(s) considered -> 18 kept as genuine parameters (33%).
- Kept tags found by: 18 via *module_segment* (the tag name contains this station's own PLC/module code as a literal segment - the strongest signal available).
- 2 kept parameter(s) below 0.5 confidence - flagged with ⚠ below.

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| Target Y Adjustment (legacy/duplicate tag) ⚠ | `DB_ASB_Data_TargetYAdjustment` | 0.1 mm | 0.40 | module_segment |
| Target Y Adjustment (legacy/duplicate tag) ⚠ | `DB_ASB_TargetYadjustment` | 0.1 mm | 0.40 | module_segment |
| Y Reference OK - Right | `DB_ASB_Data.DISP_Yref_ok_R` | - | 0.50 | module_segment |
| ASB Percentage Availability | `Data_Collection_MPI_IOs.ASB_Availability` | % | 0.55 | module_segment |
| X Position OK - Right | `DB_ASB_Data.DISP_Xpos_ok_R` | - | 0.55 | module_segment |
| X Position OK - Left | `DB_ASB_Data.DISP_Xpos_ok_L` | - | 0.55 | module_segment |
| Y Position OK - Left | `DB_ASB_Data.DISP_Ypos_ok_L` | - | 0.55 | module_segment |
| Y Position OK - Right | `DB_ASB_Data.DISP_Ypos_ok_R` | - | 0.55 | module_segment |
| Actual X Adjustment - Left | `DB_ASB_Data.ActualXAdjustment_L` | 0.1 mm | 0.60 | module_segment |
| Actual X Adjustment - Right | `DB_ASB_Data.ActualXAdjustment_R` | 0.1 mm | 0.60 | module_segment |
| Target X Adjustment - Left | `DB_ASB_Data.TargetXAdjustment_L` | 0.1 mm | 0.60 | module_segment |
| Target X Adjustment - Right | `DB_ASB_Data.TargetXAdjustment_R` | 0.1 mm | 0.60 | module_segment |
| Actual Cross Adjustment Y - Left | `DB_ASB_Data.ActualYAdjustment_L` | 0.1 mm | 0.70 | module_segment |
| Actual Cross Adjustment Y - Right | `DB_ASB_Data.ActualYAdjustment_R` | 0.1 mm | 0.70 | module_segment |
| Label Time - Left Side | `DB_ASB_Data.LabelTime_Left` | s | 0.70 | module_segment |
| Label Time - Right Side | `DB_ASB_Data.LabelTime_Right` | s | 0.70 | module_segment |
| Target Cross Adjustment Y - Left | `DB_ASB_Data.TargetYAdjustment_L` | 0.1 mm | 0.75 | module_segment |
| Target Cross Adjustment Y - Right | `DB_ASB_Data.TargetYAdjustment_R` | 0.1 mm | 0.75 | module_segment |

### PWC 4S-welding station, circumference (MC004-PWC)

- 261 candidate tag(s) considered -> 146 kept as genuine parameters (56%).
- Kept tags found by: 146 via *module_segment* (the tag name contains this station's own PLC/module code as a literal segment - the strongest signal available).
- 2 kept parameter(s) below 0.5 confidence - flagged with ⚠ below.

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| Lower Zone Status Word ⚠ | `PWC_LWR` | - | 0.40 | module_segment |
| Upper Zone Status Word ⚠ | `PWC_UPR` | - | 0.40 | module_segment |
| Lower Heater Zone Status | `PWC_LowerHeater` | - | 0.50 | module_segment |
| Lower Heater Zone Status - Belt | `PWC_LowerHeater_Belt` | - | 0.50 | module_segment |
| Upper Heater Zone Status | `PWC_UpperHeater` | - | 0.50 | module_segment |
| Upper Heater Zone Status - Belt | `PWC_UpperHeater_Belt` | - | 0.50 | module_segment |
| Circumference Clamp Axis - Search-Run Select Command | `DB_PWC_Data.Servo.SP_Select_SearchRun` | - | 0.50 | module_segment |
| Circumference Clamp Axis - Search-Run Take Value Command | `DB_PWC_Data.Servo.SP_TakeValue_SearchRun` | - | 0.50 | module_segment |
| Circumference Clamp Axis - Jog Backward Command | `DB_PWC_Data.Servo.SP_Tapp_BWD` | - | 0.50 | module_segment |
| Circumference Clamp Axis - Jog Forward Command | `DB_PWC_Data.Servo.SP_Tapp_FWD` | - | 0.50 | module_segment |
| Belt Welding Axis - Search-Run Select Command | `DB_PWC_Data.Servo_Belt.SP_Select_SearchRun` | - | 0.50 | module_segment |
| Belt Welding Axis - Search-Run Take Value Command | `DB_PWC_Data.Servo_Belt.SP_TakeValue_SearchRun` | - | 0.50 | module_segment |
| Belt Welding Axis - Jog Backward Command | `DB_PWC_Data.Servo_Belt.SP_Tapp_BWD` | - | 0.50 | module_segment |
| Belt Welding Axis - Jog Forward Command | `DB_PWC_Data.Servo_Belt.SP_Tapp_FWD` | - | 0.50 | module_segment |
| Belt Lower Heater Controller Setting | `DB_PWC_DataHeater.Belt_LH.ControlerSetting` | % | 0.50 | module_segment |
| Belt Lower Heater Scale Curve Y Maximum | `DB_PWC_DataHeater.Belt_LH.YScaleMax` | °C | 0.50 | module_segment |
| Belt Lower Heater Scale Curve Y Minimum | `DB_PWC_DataHeater.Belt_LH.YScaleMin` | °C | 0.50 | module_segment |
| Belt Upper Heater Controller Setting | `DB_PWC_DataHeater.Belt_UH.ControlerSetting` | % | 0.50 | module_segment |
| Belt Upper Heater Scale Curve Y Maximum | `DB_PWC_DataHeater.Belt_UH.YScaleMax` | °C | 0.50 | module_segment |
| Belt Upper Heater Scale Curve Y Minimum | `DB_PWC_DataHeater.Belt_UH.YScaleMin` | °C | 0.50 | module_segment |
| Lower Heater Controller Setting | `DB_PWC_DataHeater.LH.ControlerSetting` | % | 0.50 | module_segment |
| Lower Heater Scale Curve Y Maximum | `DB_PWC_DataHeater.LH.YScaleMax` | °C | 0.50 | module_segment |
| Lower Heater Scale Curve Y Minimum | `DB_PWC_DataHeater.LH.YScaleMin` | °C | 0.50 | module_segment |
| Upper Heater Controller Setting | `DB_PWC_DataHeater.UH.ControlerSetting` | % | 0.50 | module_segment |
| Upper Heater Scale Curve Y Maximum | `DB_PWC_DataHeater.UH.YScaleMax` | °C | 0.50 | module_segment |
| Upper Heater Scale Curve Y Minimum | `DB_PWC_DataHeater.UH.YScaleMin` | °C | 0.50 | module_segment |
| Active Step Number - Belt Welding | `PWC_SQ_BeltWelding` | - | 0.55 | module_segment |
| Jogging Step Sequence | `DB_PWC_Data.SequenceJogging` | - | 0.55 | module_segment |
| Calibration Enable | `PWC_CAL_ENABLE` | - | 0.55 | module_segment |
| Circumference Clamp Axis - Calibration Value 1 Store Command | `DB_PWC_Data.Servo.SP_Cali1_value_store` | - | 0.55 | module_segment |
| Circumference Clamp Axis - Calibration Value 2 Store Command | `DB_PWC_Data.Servo.SP_Cali2_value_store` | - | 0.55 | module_segment |
| Circumference Clamp Axis - Go To Calibration Position 1 Command | `DB_PWC_Data.Servo.SP_Go_to_Cali_1` | - | 0.55 | module_segment |
| Circumference Clamp Axis - Go To Calibration Position 2 Command | `DB_PWC_Data.Servo.SP_Go_to_Cali_2` | - | 0.55 | module_segment |
| Circumference Clamp Axis - Go To Open Position Command | `DB_PWC_Data.Servo.SP_Go_to_pos_open` | - | 0.55 | module_segment |
| Circumference Clamp Axis - Zeroing Release (Setting Mode) | `DB_PWC_Data.Servo.SP_Release_Zeroing` | - | 0.55 | module_segment |
| Circumference Clamp Axis - Calibration Select Command | `DB_PWC_Data.Servo.SP_Select_Calibration` | - | 0.55 | module_segment |
| Circumference Clamp Axis - Zeroing Set Command | `DB_PWC_Data.Servo.SP_Set_Zeroing` | - | 0.55 | module_segment |
| Circumference Clamp Axis - Search-Run Start Command | `DB_PWC_Data.Servo.SP_Start_SearchRun` | - | 0.55 | module_segment |
| Circumference Clamp Axis - Search-Run Stop Command | `DB_PWC_Data.Servo.SP_Stop_SearchRun` | - | 0.55 | module_segment |
| Belt Welding Axis - Calibration Value 1 Store Command | `DB_PWC_Data.Servo_Belt.SP_Cali1_value_store` | - | 0.55 | module_segment |
| Belt Welding Axis - Calibration Value 2 Store Command | `DB_PWC_Data.Servo_Belt.SP_Cali2_value_store` | - | 0.55 | module_segment |
| Belt Welding Axis - Calibration Select Command | `DB_PWC_Data.Servo_Belt.SP_Select_Calibration` | - | 0.55 | module_segment |
| Belt Welding Axis - Zeroing Set Command | `DB_PWC_Data.Servo_Belt.SP_Set_Zeroing` | - | 0.55 | module_segment |
| Belt Welding Axis - Search-Run Start Command | `DB_PWC_Data.Servo_Belt.SP_Start_SearchRun` | - | 0.55 | module_segment |
| Belt Welding Axis - Search-Run Stop Command | `DB_PWC_Data.Servo_Belt.SP_Stop_SearchRun` | - | 0.55 | module_segment |
| Belt Welding Axis - Tapping Mode Selection | `DB_PWC_Data.Servo_Belt.SP_TappingMode` | - | 0.55 | module_segment |
| Measuring Run Result - Belt Welding | `DB_PWC_Data.SearchStrokeResultBelt` | - | 0.60 | module_segment |
| Start Belt Welding (Softkey) | `DB_PWC_Data.SoftkeyStartBeltWelding` | - | 0.60 | module_segment |
| Station Open (Softkey) | `DB_PWC_Data.SoftkeyStationOpen` | - | 0.60 | module_segment |
| Stop Belt Welding (Softkey) | `DB_PWC_Data.SoftkeyStopBeltWelding` | - | 0.60 | module_segment |
| X Adjustment Zeroing (Softkey) | `DB_PWC_Data.SoftkeyZeroAdjustingX` | - | 0.60 | module_segment |
| Y Adjustment Zeroing (Softkey) | `DB_PWC_Data.SoftkeyZeroAdjustingY` | - | 0.60 | module_segment |
| Belt Welding Ready Status | `DB_PWC_Data.StatusBeltWeldingReady` | - | 0.60 | module_segment |
| Belt Heating Pressure Measured Value Setpoint 2 | `DB_PWC_Data.TargetTempBelt_2` | °C | 0.60 | module_segment |
| Circumference Clamp Axis - Servo Position - Actual | `DB_PWC_Data.Servo.DSP_Actual_Position` | - | 0.60 | module_segment |
| Circumference Clamp Axis - Closing Acceleration Setpoint | `DB_PWC_Data.Servo.SP_Acc_Closing` | - | 0.60 | module_segment |
| Circumference Clamp Axis - Opening Acceleration Setpoint | `DB_PWC_Data.Servo.SP_Acc_Opening` | - | 0.60 | module_segment |
| Circumference Clamp Axis - Closing Deceleration Setpoint | `DB_PWC_Data.Servo.SP_Dec_Closing` | - | 0.60 | module_segment |
| Circumference Clamp Axis - Opening Deceleration Setpoint | `DB_PWC_Data.Servo.SP_Dec_Opening` | - | 0.60 | module_segment |
| Circumference Clamp Axis - Maximum Mechanical Stroke | `DB_PWC_Data.Servo.SP_MaxPosition` | - | 0.60 | module_segment |
| Circumference Clamp Axis - Film Width Relative Position Setpoint | `DB_PWC_Data.Servo.SP_Rel_Pos_FoilWidth` | mm | 0.60 | module_segment |
| Circumference Clamp Axis - Regulation Range Relative Position Setpoint | `DB_PWC_Data.Servo.SP_Rel_Pos_RangeRegu` | - | 0.60 | module_segment |
| Circumference Clamp Axis - Closing Speed Setpoint | `DB_PWC_Data.Servo.SP_Speed_Closingg` | - | 0.60 | module_segment |
| Circumference Clamp Axis - Opening Speed Setpoint | `DB_PWC_Data.Servo.SP_Speed_Opening` | - | 0.60 | module_segment |
| Belt Welding Axis - Servo Position - Actual | `DB_PWC_Data.Servo_Belt.DSP_Actual_Position` | - | 0.60 | module_segment |
| Belt Welding Axis - Close Position Reached | `DB_PWC_Data.Servo_Belt.DSP_Position_Close` | - | 0.60 | module_segment |
| Belt Welding Axis - Open Position Reached (Drive in Position 01) | `DB_PWC_Data.Servo_Belt.DSP_Position_Open` | - | 0.60 | module_segment |
| Belt Welding Axis - Closing Acceleration Setpoint | `DB_PWC_Data.Servo_Belt.SP_Acc_Closing` | - | 0.60 | module_segment |
| Belt Welding Axis - Opening Acceleration Setpoint | `DB_PWC_Data.Servo_Belt.SP_Acc_Opening` | - | 0.60 | module_segment |
| Belt Welding Axis - Closing Deceleration Setpoint | `DB_PWC_Data.Servo_Belt.SP_Dec_Closing` | - | 0.60 | module_segment |
| Belt Welding Axis - Opening Deceleration Setpoint | `DB_PWC_Data.Servo_Belt.SP_Dec_Opening` | - | 0.60 | module_segment |
| Belt Welding Axis - Maximum Mechanical Stroke | `DB_PWC_Data.Servo_Belt.SP_MaxPosition` | - | 0.60 | module_segment |
| Belt Welding Axis - Film Width Relative Position Setpoint | `DB_PWC_Data.Servo_Belt.SP_Rel_Pos_FoilWidth` | mm | 0.60 | module_segment |
| Belt Welding Axis - Regulation Range Relative Position Setpoint | `DB_PWC_Data.Servo_Belt.SP_Rel_Pos_RangeRegu` | - | 0.60 | module_segment |
| Belt Welding Axis - Closing Speed Setpoint | `DB_PWC_Data.Servo_Belt.SP_Speed_Closingg` | - | 0.60 | module_segment |
| Belt Welding Axis - Opening Speed Setpoint | `DB_PWC_Data.Servo_Belt.SP_Speed_Opening` | - | 0.60 | module_segment |
| Belt Lower Heater Solid State Relay Output | `DB_PWC_DataHeater.Belt_LH.OutputSSD` | - | 0.65 | module_segment |
| Belt Upper Heater Solid State Relay Output | `DB_PWC_DataHeater.Belt_UH.OutputSSD` | - | 0.65 | module_segment |
| Lower Heater Solid State Relay Output | `DB_PWC_DataHeater.LH.OutputSSD` | - | 0.65 | module_segment |
| Upper Heater Solid State Relay Output | `DB_PWC_DataHeater.UH.OutputSSD` | - | 0.65 | module_segment |
| X-Position OK (Display) | `DB_PWC_Data.DISP_Xpos_ok` | - | 0.65 | module_segment |
| Y-Position OK (Display) | `DB_PWC_Data.DISP_Ypos_ok` | - | 0.65 | module_segment |
| Tox Cylinder - Actual Value | `DB_PWC_BeltWelding.ActualToxBeltWelding` | - | 0.65 | module_segment |
| Tox Cylinder - Nominal Value | `DB_PWC_BeltWelding.TargetToxBeltwelding` | - | 0.65 | module_segment |
| Semiautomatic Mode Selection | `DB_PWC_Data.SelectionSemiAutomatic` | - | 0.65 | module_segment |
| Station Selection | `DB_PWC_Data.SelectionStation` | - | 0.65 | module_segment |
| Circumference Clamp Axis - Search-Run Touch-Down Point - Detected | `DB_PWC_Data.Servo.DSP_TouchPoint_Detected` | - | 0.65 | module_segment |
| Circumference Clamp Axis - Search-Run Touch-Down Point - Regulation Start | `DB_PWC_Data.Servo.DSP_TouchPoint_Start` | - | 0.65 | module_segment |
| Circumference Clamp Axis - Search-Run Touch-Down Point - Stored | `DB_PWC_Data.Servo.DSP_TouchPoint_Stored` | - | 0.65 | module_segment |
| Circumference Clamp Axis - Open Position Setpoint | `DB_PWC_Data.Servo.SP_Position_open` | - | 0.65 | module_segment |
| Circumference Clamp Axis - Welding Pressure Tolerance - Lower Limit | `DB_PWC_Data.Servo.SP_Pressure_Tolerance_lo` | - | 0.65 | module_segment |
| Circumference Clamp Axis - Welding Pressure Tolerance - Upper Limit | `DB_PWC_Data.Servo.SP_Pressure_Tolerance_up` | - | 0.65 | module_segment |
| Belt Welding Axis - Search-Run Touch-Down Point - Detected | `DB_PWC_Data.Servo_Belt.DSP_TouchPoint_Detected` | - | 0.65 | module_segment |
| Belt Welding Axis - Search-Run Touch-Down Point - Regulation Start | `DB_PWC_Data.Servo_Belt.DSP_TouchPoint_Start` | - | 0.65 | module_segment |
| Belt Welding Axis - Search-Run Touch-Down Point - Stored | `DB_PWC_Data.Servo_Belt.DSP_TouchPoint_Stored` | - | 0.65 | module_segment |
| Belt Welding Axis - Open Position Setpoint | `DB_PWC_Data.Servo_Belt.SP_Position_open` | - | 0.65 | module_segment |
| Cooling Off Setpoint | `PWC_CoolingOFF` | - | 0.70 | module_segment |
| Belt Welding Selection | `DB_PWC_Data.SelectionBeltWelding` | - | 0.70 | module_segment |
| Cooling Station Preselection | `DB_PWC_Data.SelectionCooling` | - | 0.70 | module_segment |
| Belt Lower Heater Heater On/Off Setpoint | `DB_PWC_DataHeater.Belt_LH.HeaterSelection` | - | 0.70 | module_segment |
| Belt Upper Heater Heater On/Off Setpoint | `DB_PWC_DataHeater.Belt_UH.HeaterSelection` | - | 0.70 | module_segment |
| Lower Heater Heater On/Off Setpoint | `DB_PWC_DataHeater.LH.HeaterSelection` | - | 0.70 | module_segment |
| Upper Heater Heater On/Off Setpoint | `DB_PWC_DataHeater.UH.HeaterSelection` | - | 0.70 | module_segment |
| Lengthwise Adjustment X - Actual | `DB_PWC_Data.ActualXAdjustment` | 1/10 mm | 0.75 | module_segment |
| Cross Adjustment Y - Actual | `DB_PWC_Data.ActualYAdjustment` | 1/10 mm | 0.75 | module_segment |
| Cooling Time Setpoint | `DB_PWC_Data.TargetCoolingTime` | s | 0.75 | module_segment |
| Belt Heating-Up Temperature Setpoint 1 | `DB_PWC_Data.TargetTempBelt_1` | °C | 0.75 | module_segment |
| Belt Cooling-Down Temperature Setpoint 3 | `DB_PWC_Data.TargetTempBelt_3` | °C | 0.75 | module_segment |
| Belt Lower Heater Actual Temperature | `DB_PWC_DataHeater.Belt_LH.ActualValue` | °C | 0.75 | module_segment |
| Belt Lower Heater Lower Temperature Limit | `DB_PWC_DataHeater.Belt_LH.LowerBorder` | °C | 0.75 | module_segment |
| Belt Lower Heater Upper Temperature Limit | `DB_PWC_DataHeater.Belt_LH.UpperBorder` | °C | 0.75 | module_segment |
| Belt Upper Heater Actual Temperature | `DB_PWC_DataHeater.Belt_UH.ActualValue` | °C | 0.75 | module_segment |
| Belt Upper Heater Lower Temperature Limit | `DB_PWC_DataHeater.Belt_UH.LowerBorder` | °C | 0.75 | module_segment |
| Belt Upper Heater Upper Temperature Limit | `DB_PWC_DataHeater.Belt_UH.UpperBorder` | °C | 0.75 | module_segment |
| Lower Heater Actual Temperature | `DB_PWC_DataHeater.LH.ActualValue` | °C | 0.75 | module_segment |
| Lower Heater Lower Temperature Limit | `DB_PWC_DataHeater.LH.LowerBorder` | °C | 0.75 | module_segment |
| Lower Heater Upper Temperature Limit | `DB_PWC_DataHeater.LH.UpperBorder` | °C | 0.75 | module_segment |
| Upper Heater Actual Temperature | `DB_PWC_DataHeater.UH.ActualValue` | °C | 0.75 | module_segment |
| Upper Heater Lower Temperature Limit | `DB_PWC_DataHeater.UH.LowerBorder` | °C | 0.75 | module_segment |
| Upper Heater Upper Temperature Limit | `DB_PWC_DataHeater.UH.UpperBorder` | °C | 0.75 | module_segment |
| Cooling Agent Temperature - Actual | `DB_PWC_Data.ActualCoolingTemperatur` | °C | 0.80 | module_segment |
| Cooling Agent Temperature - Rail Actual | `DB_PWC_Data.ActualCoolingTempRail` | °C | 0.80 | module_segment |
| Cooling Agent Temperature Switching Threshold | `DB_PWC_Data.TargetCoolingTemperature` | °C | 0.80 | module_segment |
| Cooling Agent Temperature Switching Threshold - Rail | `DB_PWC_Data.TargetCoolingTempRail` | °C | 0.80 | module_segment |
| Welding Time Setpoint | `DB_PWC_Data.TargetWeldingTime` | s | 0.80 | module_segment |
| Circumference Clamp Axis - External Load Cell Calibration Measurement 1 | `DB_PWC_Data.Servo.SP_Extern_Force_1` | N | 0.80 | module_segment |
| Circumference Clamp Axis - External Load Cell Calibration Measurement 2 | `DB_PWC_Data.Servo.SP_Extern_Force_2` | N | 0.80 | module_segment |
| Circumference Clamp Axis - Load Cell Calibration Target Point 1 | `DB_PWC_Data.Servo.SP_Target_Cali_Point1` | mV | 0.80 | module_segment |
| Circumference Clamp Axis - Load Cell Calibration Target Point 2 | `DB_PWC_Data.Servo.SP_Target_Cali_Point2` | mV | 0.80 | module_segment |
| Belt Welding Axis - Load Cell Calibration Target Point 1 | `DB_PWC_Data.Servo_Belt.SP_Target_Cali_Point1` | mV | 0.80 | module_segment |
| Belt Welding Axis - Load Cell Calibration Target Point 2 | `DB_PWC_Data.Servo_Belt.SP_Target_Cali_Point2` | mV | 0.80 | module_segment |
| Belt Lower Heater Correction Value | `DB_PWC_DataHeater.Belt_LH.CorrectionValue` | 1/10 °C | 0.80 | module_segment |
| Belt Lower Heater Target Temperature Setpoint | `DB_PWC_DataHeater.Belt_LH.TargetValue` | °C | 0.80 | module_segment |
| Belt Upper Heater Correction Value | `DB_PWC_DataHeater.Belt_UH.CorrectionValue` | 1/10 °C | 0.80 | module_segment |
| Belt Upper Heater Target Temperature Setpoint | `DB_PWC_DataHeater.Belt_UH.TargetValue` | °C | 0.80 | module_segment |
| Lower Heater Correction Value | `DB_PWC_DataHeater.LH.CorrectionValue` | 1/10 °C | 0.80 | module_segment |
| Lower Heater Target Temperature Setpoint | `DB_PWC_DataHeater.LH.TargetValue` | °C | 0.80 | module_segment |
| Upper Heater Correction Value | `DB_PWC_DataHeater.UH.CorrectionValue` | 1/10 °C | 0.80 | module_segment |
| Upper Heater Target Temperature Setpoint | `DB_PWC_DataHeater.UH.TargetValue` | °C | 0.80 | module_segment |
| Lengthwise Adjustment X - Setpoint | `DB_PWC_Data.TargetXAdjustment` | 1/10 mm | 0.85 | module_segment |
| Cross Adjustment Y - Setpoint | `DB_PWC_Data.TargetYAdjustment` | 1/10 mm | 0.85 | module_segment |
| Circumference Clamp Axis - Closing Force - Actual | `DB_PWC_Data.Servo.DSP_Actual_Moment` | N | 0.85 | module_segment |
| Circumference Clamp Axis - Load Cell Output Voltage | `DB_PWC_Data.Servo.LoadCell` | mV | 0.85 | module_segment |
| Circumference Clamp Axis - Closing Force Setpoint | `DB_PWC_Data.Servo.SP_force` | N | 0.85 | module_segment |
| Belt Welding Axis - Closing Force - Actual | `DB_PWC_Data.Servo_Belt.DSP_Actual_Moment` | N | 0.85 | module_segment |
| Belt Welding Axis - Closing Force Setpoint | `DB_PWC_Data.Servo_Belt.SP_force` | N | 0.85 | module_segment |

### ASC labelling unit, re-heating station, testing station (MC004-ASC)

- 163 candidate tag(s) considered -> 150 kept as genuine parameters (92%).
- Kept tags found by: 150 via *module_segment* (the tag name contains this station's own PLC/module code as a literal segment - the strongest signal available).
- 16 kept parameter(s) below 0.5 confidence - flagged with ⚠ below.

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| Lower Left Zone Status Word ⚠ | `ASC_LL` | - | 0.40 | module_segment |
| Lower Right Zone Status Word ⚠ | `ASC_LR` | - | 0.40 | module_segment |
| Upper Left Zone Status Word ⚠ | `ASC_UL` | - | 0.40 | module_segment |
| Upper Right Zone Status Word ⚠ | `ASC_UR` | - | 0.40 | module_segment |
| Lower Heater LHS Controller Setting ⚠ | `DB_ASC_HeaterData.LH_LHS.ControlerSetting` | % | 0.40 | module_segment |
| Lower Heater LHS Correction Value ⚠ | `DB_ASC_HeaterData.LH_LHS.CorrectionValue` | - | 0.40 | module_segment |
| Lower Heater RHS Controller Setting ⚠ | `DB_ASC_HeaterData.LH_RHS.ControlerSetting` | % | 0.40 | module_segment |
| Lower Heater RHS Correction Value ⚠ | `DB_ASC_HeaterData.LH_RHS.CorrectionValue` | - | 0.40 | module_segment |
| Upper Heater LHS Controller Setting ⚠ | `DB_ASC_HeaterData.UH_LHS.ControlerSetting` | % | 0.40 | module_segment |
| Upper Heater LHS Correction Value ⚠ | `DB_ASC_HeaterData.UH_LHS.CorrectionValue` | - | 0.40 | module_segment |
| Upper Heater RHS Controller Setting ⚠ | `DB_ASC_HeaterData.UH_RHS.ControlerSetting` | % | 0.40 | module_segment |
| Upper Heater RHS Correction Value ⚠ | `DB_ASC_HeaterData.UH_RHS.CorrectionValue` | - | 0.40 | module_segment |
| LHS Y Decrease Jog (Duplicate Point) ⚠ | `DEC_ASC_LHS_Y` | - | 0.45 | module_segment |
| RHS Y Decrease Jog (Duplicate Point) ⚠ | `DEC_ASC_RHS_Y` | - | 0.45 | module_segment |
| LHS Y Increase Jog (Duplicate Point) ⚠ | `INC_ASC_LHS_Y` | - | 0.45 | module_segment |
| RHS Y Increase Jog (Duplicate Point) ⚠ | `INC_ASC_RHS_Y` | - | 0.45 | module_segment |
| LHS Y Decrease Jog | `ASC_LHS_Y_Decrease` | - | 0.50 | module_segment |
| LHS Y Increase Jog | `ASC_LHS_Y_Increase` | - | 0.50 | module_segment |
| RHS Y Decrease Jog | `ASC_RHS_Y_Decrease` | - | 0.50 | module_segment |
| RHS Y Increase Jog | `ASC_RHS_Y_Increase` | - | 0.50 | module_segment |
| Lower Right Station Selection (Alt Point) | `DB_ASC_Data.SelectionLowerRight` | - | 0.50 | module_segment |
| Heater Zone Status - Lower LHS | `DB_ASC_DataHeater.Lower_LHS` | - | 0.50 | module_segment |
| Heater Zone Status - Lower RHS | `DB_ASC_DataHeater.Lower_RHS` | - | 0.50 | module_segment |
| Heater Zone Status - Upper LHS | `DB_ASC_DataHeater.Upper_LHS` | - | 0.50 | module_segment |
| Heater Zone Status - Upper RHS | `DB_ASC_DataHeater.Upper_RHS` | - | 0.50 | module_segment |
| Lower Heater LHS Solid State Relay Output | `DB_ASC_HeaterData.LH_LHS.OutputSSD` | - | 0.50 | module_segment |
| Lower Heater LHS Scale Curve Y Maximum | `DB_ASC_HeaterData.LH_LHS.YScaleMax` | °C | 0.50 | module_segment |
| Lower Heater LHS Scale Curve Y Minimum | `DB_ASC_HeaterData.LH_LHS.YScaleMin` | °C | 0.50 | module_segment |
| Lower Heater RHS Solid State Relay Output | `DB_ASC_HeaterData.LH_RHS.OutputSSD` | - | 0.50 | module_segment |
| Lower Heater RHS Scale Curve Y Maximum | `DB_ASC_HeaterData.LH_RHS.YScaleMax` | °C | 0.50 | module_segment |
| Lower Heater RHS Scale Curve Y Minimum | `DB_ASC_HeaterData.LH_RHS.YScaleMin` | °C | 0.50 | module_segment |
| Upper Heater LHS Solid State Relay Output | `DB_ASC_HeaterData.UH_LHS.OutputSSD` | - | 0.50 | module_segment |
| Upper Heater LHS Scale Curve Y Maximum | `DB_ASC_HeaterData.UH_LHS.YScaleMax` | °C | 0.50 | module_segment |
| Upper Heater LHS Scale Curve Y Minimum | `DB_ASC_HeaterData.UH_LHS.YScaleMin` | °C | 0.50 | module_segment |
| Upper Heater RHS Solid State Relay Output | `DB_ASC_HeaterData.UH_RHS.OutputSSD` | - | 0.50 | module_segment |
| Upper Heater RHS Scale Curve Y Maximum | `DB_ASC_HeaterData.UH_RHS.YScaleMax` | °C | 0.50 | module_segment |
| Upper Heater RHS Scale Curve Y Minimum | `DB_ASC_HeaterData.UH_RHS.YScaleMin` | °C | 0.50 | module_segment |
| Test Station Jogging Step Sequence | `DB_ASC_Test_Data.SequenceJogging` | - | 0.50 | module_segment |
| Lower Left Zone Status | `ASC_LowerLeft` | - | 0.55 | module_segment |
| Lower Right Zone Status | `ASC_LowerRight` | - | 0.55 | module_segment |
| Y-Adjustment Release Popup - Lower LHS | `ASC_Popup_Y_lower_LHS` | - | 0.55 | module_segment |
| Y-Adjustment Release Popup - Upper LHS | `ASC_Popup_Y_upper_LHS` | - | 0.55 | module_segment |
| Upper Left Zone Status | `ASC_UpperLeft` | - | 0.55 | module_segment |
| Upper Right Zone Status | `ASC_UpperRight` | - | 0.55 | module_segment |
| Auto Correction Count | `ASC_AUTO_COR_CNT` | - | 0.55 | module_segment |
| Consecutive Errors Selection On/Off | `ASC_Consec_Errors_Selection` | - | 0.55 | module_segment |
| Jogging Step Sequence | `DB_ASC_Data.SequenceJogging` | - | 0.55 | module_segment |
| X-Adjustment Zeroing (Softkey) (LL) | `DB_ASC_Data.SoftkeyZeroAdjustingXLL` | - | 0.55 | module_segment |
| X-Adjustment Zeroing (Softkey) (LR) | `DB_ASC_Data.SoftkeyZeroAdjustingXLR` | - | 0.55 | module_segment |
| X-Adjustment Zeroing (Softkey) (UL) | `DB_ASC_Data.SoftkeyZeroAdjustingXUL` | - | 0.55 | module_segment |
| X-Adjustment Zeroing (Softkey) (UR) | `DB_ASC_Data.SoftkeyZeroAdjustingXUR` | - | 0.55 | module_segment |
| Y-Adjustment Zeroing (Softkey) (LL) | `DB_ASC_Data.SoftkeyZeroAdjustingYLL` | - | 0.55 | module_segment |
| Y-Adjustment Zeroing (Softkey) (LR) | `DB_ASC_Data.SoftkeyZeroAdjustingYLR` | - | 0.55 | module_segment |
| Y-Adjustment Zeroing (Softkey) (UL) | `DB_ASC_Data.SoftkeyZeroAdjustingYUL` | - | 0.55 | module_segment |
| Y-Adjustment Zeroing (Softkey) (UR) | `DB_ASC_Data.SoftkeyZeroAdjustingYUR` | - | 0.55 | module_segment |
| Lower Heater LHS Actual Temperature | `DB_ASC_HeaterData.LH_LHS.ActualValue` | °C | 0.55 | module_segment |
| Lower Heater LHS Heater On/Off Setpoint | `DB_ASC_HeaterData.LH_LHS.HeaterSelection` | - | 0.55 | module_segment |
| Lower Heater LHS Lower Temperature Limit | `DB_ASC_HeaterData.LH_LHS.LowerBorder` | °C | 0.55 | module_segment |
| Lower Heater LHS Upper Temperature Limit | `DB_ASC_HeaterData.LH_LHS.UpperBorder` | °C | 0.55 | module_segment |
| Lower Heater RHS Actual Temperature | `DB_ASC_HeaterData.LH_RHS.ActualValue` | °C | 0.55 | module_segment |
| Lower Heater RHS Heater On/Off Setpoint | `DB_ASC_HeaterData.LH_RHS.HeaterSelection` | - | 0.55 | module_segment |
| Lower Heater RHS Lower Temperature Limit | `DB_ASC_HeaterData.LH_RHS.LowerBorder` | °C | 0.55 | module_segment |
| Lower Heater RHS Upper Temperature Limit | `DB_ASC_HeaterData.LH_RHS.UpperBorder` | °C | 0.55 | module_segment |
| Upper Heater LHS Actual Temperature | `DB_ASC_HeaterData.UH_LHS.ActualValue` | °C | 0.55 | module_segment |
| Upper Heater LHS Heater On/Off Setpoint | `DB_ASC_HeaterData.UH_LHS.HeaterSelection` | - | 0.55 | module_segment |
| Upper Heater LHS Lower Temperature Limit | `DB_ASC_HeaterData.UH_LHS.LowerBorder` | °C | 0.55 | module_segment |
| Upper Heater LHS Upper Temperature Limit | `DB_ASC_HeaterData.UH_LHS.UpperBorder` | °C | 0.55 | module_segment |
| Upper Heater RHS Actual Temperature | `DB_ASC_HeaterData.UH_RHS.ActualValue` | °C | 0.55 | module_segment |
| Upper Heater RHS Heater On/Off Setpoint | `DB_ASC_HeaterData.UH_RHS.HeaterSelection` | - | 0.55 | module_segment |
| Upper Heater RHS Lower Temperature Limit | `DB_ASC_HeaterData.UH_RHS.LowerBorder` | °C | 0.55 | module_segment |
| Upper Heater RHS Upper Temperature Limit | `DB_ASC_HeaterData.UH_RHS.UpperBorder` | °C | 0.55 | module_segment |
| Re-Heat X-Adjustment Zeroing (Softkey) (L) | `DB_ASC_Reheat_Data.SoftkeyZeroAdjustingX_L` | - | 0.55 | module_segment |
| Re-Heat Y-Adjustment Zeroing (Softkey) (L) | `DB_ASC_Reheat_Data.SoftkeyZeroAdjustingY_L` | - | 0.55 | module_segment |
| Re-Heat X-Adjustment Zeroing (Softkey) (R) | `DB_ASC_Reheat_Data.SoftkeyZeroAdjustingX_R` | - | 0.55 | module_segment |
| Re-Heat Y-Adjustment Zeroing (Softkey) (R) | `DB_ASC_Reheat_Data.SoftkeyZeroAdjustingY_R` | - | 0.55 | module_segment |
| Test Station Y-Position OK (R) | `DB_ASC_Test_Data.DISP_Ypos_ok_R` | - | 0.55 | module_segment |
| Test Station X-Adjustment Zeroing (Softkey) (L) | `DB_ASC_Test_Data.SoftkeyZeroAdjustingX_L` | - | 0.55 | module_segment |
| Test Station X-Adjustment Zeroing (Softkey) (R) | `DB_ASC_Test_Data.SoftkeyZeroAdjustingX_R` | - | 0.55 | module_segment |
| Test Station Y-Adjustment Zeroing (Softkey) (R) | `DB_ASC_Test_Data.SoftkeyZeroAdjustingY_R` | - | 0.55 | module_segment |
| X-Position OK - Lower Right | `DB_ASC_Data.DISP_Xpos_ok_LR` | - | 0.60 | module_segment |
| X-Position OK - Upper Left | `DB_ASC_Data.DISP_Xpos_ok_UL` | - | 0.60 | module_segment |
| X-Position OK - Upper Right | `DB_ASC_Data.DISP_Xpos_ok_UR` | - | 0.60 | module_segment |
| Y-Position OK - Lower Left | `DB_ASC_Data.DISP_Ypos_ok_LL` | - | 0.60 | module_segment |
| Y-Position OK - Lower Right | `DB_ASC_Data.DISP_Ypos_ok_LR` | - | 0.60 | module_segment |
| Y-Position OK - Upper Left | `DB_ASC_Data.DISP_Ypos_ok_UL` | - | 0.60 | module_segment |
| Y-Position OK - Upper Right | `DB_ASC_Data.DISP_Ypos_ok_UR` | - | 0.60 | module_segment |
| Re-Heat X-Position OK - Left | `DB_ASC_Reheat_Data.DISP_Xpos_ok_L` | - | 0.60 | module_segment |
| Re-Heat X-Position OK - Right | `DB_ASC_Reheat_Data.DISP_Xpos_ok_R` | - | 0.60 | module_segment |
| Re-Heat Y-Position OK - Left | `DB_ASC_Reheat_Data.DISP_Ypos_ok_L` | - | 0.60 | module_segment |
| Re-Heat Y-Position OK - Right | `DB_ASC_Reheat_Data.DISP_Ypos_ok_R` | - | 0.60 | module_segment |
| X-Position OK - Lower Left | `DB_ASC_Data.DISP_Xpos_ok_LL` | - | 0.60 | module_segment |
| X-Position Referenced - Lower Left | `DB_ASC_Data.DISP_Xref_ok_LL` | - | 0.60 | module_segment |
| Station Cycle Time Indicator | `DB_ASC_Data.IndicatCycleTimeStation` | s | 0.60 | module_segment |
| Lower Left Station Selection | `DB_ASC_Data.Selection_LowerLeft` | - | 0.60 | module_segment |
| Lower Right Station Selection | `DB_ASC_Data.Selection_LowerRight` | - | 0.60 | module_segment |
| Upper Left Station Selection | `DB_ASC_Data.Selection_UpperLeft` | - | 0.60 | module_segment |
| Upper Right Station Selection | `DB_ASC_Data.Selection_UpperRight` | - | 0.60 | module_segment |
| Test Station - Left Selection | `DB_ASC_Test_Data.Selection_Left` | - | 0.60 | module_segment |
| Test Station - Right Selection | `DB_ASC_Test_Data.Selection_Right` | - | 0.60 | module_segment |
| Re-Heat Part Selection (Upper Left) | `DB_ASC_Reheat_Data.Selection_Left` | - | 0.60 | module_segment |
| Re-Heat Part Selection (Upper Right) | `DB_ASC_Reheat_Data.Selection_Right` | - | 0.60 | module_segment |
| Test Station Semiautomatic Mode Selection | `DB_ASC_Test_Data.SelectionSemiAutomatic` | - | 0.60 | module_segment |
| Test Station Selection | `DB_ASC_Test_Data.SelectionStation` | - | 0.60 | module_segment |
| Lower Heater LHS Target Temperature Setpoint | `DB_ASC_HeaterData.LH_LHS.TargetValue` | °C | 0.60 | module_segment |
| Lower Heater RHS Target Temperature Setpoint | `DB_ASC_HeaterData.LH_RHS.TargetValue` | °C | 0.60 | module_segment |
| Upper Heater LHS Target Temperature Setpoint | `DB_ASC_HeaterData.UH_LHS.TargetValue` | °C | 0.60 | module_segment |
| Upper Heater RHS Target Temperature Setpoint | `DB_ASC_HeaterData.UH_RHS.TargetValue` | °C | 0.60 | module_segment |
| Test Station Camera Selection | `ASC_SelectionCamera` | - | 0.65 | module_segment |
| Label Time - Lower Left | `DB_ASC_Data.LabelTime_LowerLeft` | s | 0.65 | module_segment |
| Label Time - Lower Right | `DB_ASC_Data.LabelTime_LowerRight` | s | 0.65 | module_segment |
| Label Time - Upper Left | `DB_ASC_Data.LabelTime_UpperLeft` | s | 0.65 | module_segment |
| Label Time - Upper Right | `DB_ASC_Data.LabelTime_UpperRight` | s | 0.65 | module_segment |
| Semiautomatic Mode Selection | `DB_ASC_Data.SelectionSemiAutomatic` | - | 0.65 | module_segment |
| Station Selection | `DB_ASC_Data.SelectionStation` | - | 0.65 | module_segment |
| Test Station X-Adjustment - Actual (L) | `DB_ASC_Test_Data.ActualXAdjustment_L` | 1/10 mm | 0.65 | module_segment |
| Test Station X-Adjustment - Actual (R) | `DB_ASC_Test_Data.ActualXAdjustment_R` | 1/10 mm | 0.65 | module_segment |
| Test Station X-Adjustment - Setpoint (L) | `DB_ASC_Test_Data.TargetXAdjustment_L` | 1/10 mm | 0.65 | module_segment |
| Test Station X-Adjustment - Setpoint (R) | `DB_ASC_Test_Data.TargetXAdjustment_R` | 1/10 mm | 0.65 | module_segment |
| Fault Count - Curved Members | `Data_Collection_MPI_IOs.FAULT_COUNT_ASC` | - | 0.70 | module_segment |
| Vision Rejects LHS (Non-Resettable) | `Data_Collection_MPI_IOs.LHS_ASC_Vision_Act` | - | 0.70 | module_segment |
| Vision Rejects RHS (Non-Resettable) | `Data_Collection_MPI_IOs.RHS_ASC_Vision_Act` | - | 0.70 | module_segment |
| X-Adjustment - Actual (LL) | `DB_ASC_Data.ActualXAdjustment_LL` | 1/10 mm | 0.70 | module_segment |
| X-Adjustment - Actual (LR) | `DB_ASC_Data.ActualXAdjustment_LR` | 1/10 mm | 0.70 | module_segment |
| X-Adjustment - Actual (UL) | `DB_ASC_Data.ActualXAdjustment_UL` | 1/10 mm | 0.70 | module_segment |
| X-Adjustment - Actual (UR) | `DB_ASC_Data.ActualXAdjustment_UR` | 1/10 mm | 0.70 | module_segment |
| Y-Adjustment - Actual (LL) | `DB_ASC_Data.ActualYAdjustment_LL` | 1/10 mm | 0.70 | module_segment |
| Y-Adjustment - Actual (LR) | `DB_ASC_Data.ActualYAdjustment_LR` | 1/10 mm | 0.70 | module_segment |
| Y-Adjustment - Actual (UL) | `DB_ASC_Data.ActualYAdjustment_UL` | 1/10 mm | 0.70 | module_segment |
| Y-Adjustment - Actual (UR) | `DB_ASC_Data.ActualYAdjustment_UR` | 1/10 mm | 0.70 | module_segment |
| X-Adjustment - Setpoint (LL) | `DB_ASC_Data.TargetXAdjustment_LL` | 1/10 mm | 0.70 | module_segment |
| X-Adjustment - Setpoint (LR) | `DB_ASC_Data.TargetXAdjustment_LR` | 1/10 mm | 0.70 | module_segment |
| X-Adjustment - Setpoint (UL) | `DB_ASC_Data.TargetXAdjustment_UL` | 1/10 mm | 0.70 | module_segment |
| X-Adjustment - Setpoint (UR) | `DB_ASC_Data.TargetXAdjustment_UR` | 1/10 mm | 0.70 | module_segment |
| Re-Heat X-Adjustment - Actual (L) | `DB_ASC_Reheat_Data.ActualXAdjustment_L` | 1/10 mm | 0.70 | module_segment |
| Re-Heat Y-Adjustment - Actual (L) | `DB_ASC_Reheat_Data.ActualYAdjustment_L` | 1/10 mm | 0.70 | module_segment |
| Re-Heat Heating Time (Upper Left) | `DB_ASC_Reheat_Data.HeatingTime_Left` | s | 0.70 | module_segment |
| Re-Heat X-Adjustment - Setpoint (L) | `DB_ASC_Reheat_Data.TargetXAdjustment_L` | 1/10 mm | 0.70 | module_segment |
| Re-Heat X-Adjustment - Actual (R) | `DB_ASC_Reheat_Data.ActualXAdjustment_R` | 1/10 mm | 0.70 | module_segment |
| Re-Heat Y-Adjustment - Actual (R) | `DB_ASC_Reheat_Data.ActualYAdjustment_R` | 1/10 mm | 0.70 | module_segment |
| Re-Heat Heating Time (Upper Right) | `DB_ASC_Reheat_Data.HeatingTime_Right` | s | 0.70 | module_segment |
| Re-Heat X-Adjustment - Setpoint (R) | `DB_ASC_Reheat_Data.TargetXAdjustment_R` | 1/10 mm | 0.70 | module_segment |
| Percentage Availability | `Data_Collection_MPI_IOs.ASC_Availability` | % | 0.75 | module_segment |
| Reject Parts Count - Labelling Vision Left | `Data_Collection_MPI_IOs.Counter_Reject_ASC_LHS` | - | 0.75 | module_segment |
| Reject Parts Count - Labelling Vision Right | `Data_Collection_MPI_IOs.Counter_Reject_ASC_RHS` | - | 0.75 | module_segment |
| Y-Adjustment - Setpoint (LL) | `DB_ASC_Data.TargetYAdjustment_LL` | 1/10 mm | 0.75 | module_segment |
| Y-Adjustment - Setpoint (LR) | `DB_ASC_Data.TargetYAdjustment_LR` | 1/10 mm | 0.75 | module_segment |
| Y-Adjustment - Setpoint (UL) | `DB_ASC_Data.TargetYAdjustment_UL` | 1/10 mm | 0.75 | module_segment |
| Y-Adjustment - Setpoint (UR) | `DB_ASC_Data.TargetYAdjustment_UR` | 1/10 mm | 0.75 | module_segment |
| Re-Heat Y-Adjustment - Setpoint (L) | `DB_ASC_Reheat_Data.TargetYAdjustment_L` | 1/10 mm | 0.75 | module_segment |
| Re-Heat Y-Adjustment - Setpoint (R) | `DB_ASC_Reheat_Data.TargetYAdjustment_R` | 1/10 mm | 0.75 | module_segment |

### PPS 4S-cutout station, circumference (MC004-PPS)

- 29 candidate tag(s) considered -> 12 kept as genuine parameters (41%).
- Kept tags found by: 12 via *module_segment* (the tag name contains this station's own PLC/module code as a literal segment - the strongest signal available).

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| X Position OK | `DB_PPS_Data.DISP_Xpos_ok` | - | 0.55 | module_segment |
| Y Position OK | `DB_PPS_Data.DISP_Ypos_ok` | - | 0.55 | module_segment |
| Z Position OK | `DB_PPS_Data.DISP_Zpos_ok` | - | 0.55 | module_segment |
| Station Cycle Time (Display) | `DB_PPS_Data.IndicatCycleTimeStat` | s | 0.55 | module_segment |
| Actual Punching Time | `DB_PPS_Data.ActualPunchTime` | s | 0.65 | module_segment |
| Nominal Punching Time | `DB_PPS_Data.TargetPunchTime` | s | 0.65 | module_segment |
| Actual Lengthwise Adjustment X | `DB_PPS_Data.ActualXAdjustment` | 0.1 mm | 0.65 | module_segment |
| Target Lengthwise Adjustment X | `DB_PPS_Data.TargetXAdjustment` | 0.1 mm | 0.65 | module_segment |
| Actual Cross Adjustment Y | `DB_PPS_Data.ActualYAdjustment` | 0.1 mm | 0.65 | module_segment |
| Target Cross Adjustment Y | `DB_PPS_Data.TargetYAdjustment` | 0.1 mm | 0.65 | module_segment |
| Actual Height Adjustment Z | `DB_PPS_Data.ActualZAdjustment` | 0.01 mm | 0.70 | module_segment |
| Target Height Adjustment Z | `DB_PPS_Data.TargetZAdjustment` | 0.01 mm | 0.70 | module_segment |

### ULS removal point (MC004-ULS)

- 60 candidate tag(s) considered -> 29 kept as genuine parameters (48%).
- Kept tags found by: 29 via *module_segment* (the tag name contains this station's own PLC/module code as a literal segment - the strongest signal available).

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| X Position OK | `DB_ULS_Data.DISP_Xpos_ok` | - | 0.55 | module_segment |
| Y Position OK | `DB_ULS_Data.DISP_Ypos_ok` | - | 0.55 | module_segment |
| Servo - Nominal Acceleration 01 | `DB_ULS_Data.servo.SP_Acc_01` | - | 0.55 | module_segment |
| Servo - Nominal Acceleration 02 | `DB_ULS_Data.servo.SP_Acc_02` | - | 0.55 | module_segment |
| Servo - Nominal Acceleration 03 | `DB_ULS_Data.servo.SP_Acc_03` | - | 0.55 | module_segment |
| Servo - Nominal Deceleration 01 | `DB_ULS_Data.servo.SP_Dec_01` | - | 0.55 | module_segment |
| Servo - Nominal Deceleration 02 | `DB_ULS_Data.servo.SP_Dec_02` | - | 0.55 | module_segment |
| Servo - Nominal Deceleration 03 | `DB_ULS_Data.servo.SP_Dec_03` | - | 0.55 | module_segment |
| Servo - Nominal Speed 01 | `DB_ULS_Data.servo.SP_Speed_01` | - | 0.55 | module_segment |
| Servo - Nominal Speed 02 | `DB_ULS_Data.servo.SP_Speed_02` | - | 0.55 | module_segment |
| Servo - Nominal Speed 03 | `DB_ULS_Data.servo.SP_Speed_03` | - | 0.55 | module_segment |
| Servo Position 1 Activated | `ULS_ServoPosition_1_Aktivated` | - | 0.55 | module_segment |
| Servo Position 2 Activated | `ULS_ServoPosition_2_Aktivated` | - | 0.55 | module_segment |
| Servo Position 3 Activated | `ULS_ServoPosition_3_Aktivated` | - | 0.55 | module_segment |
| Servo Actual Position | `DB_ULS_Data.Is_Position` | - | 0.60 | module_segment |
| Servo - Nominal Position 01 | `DB_ULS_Data.servo.SP_Position_01` | - | 0.60 | module_segment |
| Servo - Nominal Position 02 | `DB_ULS_Data.servo.SP_Position_02` | - | 0.60 | module_segment |
| Servo - Nominal Position 03 | `DB_ULS_Data.servo.SP_Position_03` | - | 0.60 | module_segment |
| Nominal Reverse Time (Fife) | `DB_ULS_Data.TargetReverseTimeFife` | s | 0.60 | module_segment |
| Actual Stacking Height | `DB_ULS_Data.ActualStack` | mm | 0.65 | module_segment |
| Nominal Stacking Height | `DB_ULS_Data.TargetStack` | mm | 0.65 | module_segment |
| Nominal Belt Running Time (Long Step) | `DB_ULS_Data.TargetBeltTimeLongStep` | s | 0.65 | module_segment |
| Nominal Belt Running Time (Short Step) | `DB_ULS_Data.TargetBeltTimeShortStep` | s | 0.65 | module_segment |
| Nominal Blow-Off Time | `DB_ULS_Data.TargetBlowOffTimeUnload` | s | 0.65 | module_segment |
| Nominal Suction Time | `DB_ULS_Data.TargetVacuumTimeUnloader` | s | 0.65 | module_segment |
| Actual Cross Adjustment X | `DB_ULS_Data.ActualXAdjustment` | 0.1 mm | 0.70 | module_segment |
| Actual Cross Adjustment Y | `DB_ULS_Data.ActualYAdjustment` | 0.1 mm | 0.70 | module_segment |
| Target Cross Adjustment X | `DB_ULS_Data.TargetXAdjustment` | 0.1 mm | 0.75 | module_segment |
| Target Cross Adjustment Y | `DB_ULS_Data.TargetYAdjustment` | 0.1 mm | 0.75 | module_segment |
