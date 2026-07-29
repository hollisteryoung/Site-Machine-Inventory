# Tag Matching Report - Line K10

This summarizes, for every station found on this line, which historian tags were kept as genuine process parameters and why. Parameters marked with a low match strategy (keyword/keyword_stem/legend_code/folder_match) or below 0.5 confidence are the ones most worth a second look from someone who knows the physical machine.

## Summary

- 17 station(s) processed.
- 1664 candidate tag(s) considered across all stations -> 538 kept as genuine parameters (32% of candidates).
- 538 of this line's 2847 total historian tags (18.9%) ended up mapped to a genuine parameter - this is the actual coverage of the raw tag export, as opposed to the conversion rate above, which only measures the pre-filtered candidate pool.
- 8 kept parameter(s) below 0.5 confidence overall - worth a second look.

## Machine: Inline System KIT 70/20

### UWS unwinding unit (MC005-UWS)

- 85 candidate tag(s) considered -> 47 kept as genuine parameters (55%).
- Kept tags found by: 47 via *module_segment* (the tag name contains this station's own PLC/module code as a literal segment - the strongest signal available).

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| Ultrasonic Sensor Reading - Lower Roll - Web 1 | `DB_02UWS_WEB_01.WEB_01.DISP_SensorRollLower` | mm | 0.70 | module_segment |
| Ultrasonic Sensor Reading - Upper Roll - Web 1 | `DB_02UWS_WEB_01.WEB_01.DISP_SensorRollUpper` | mm | 0.70 | module_segment |
| Magnetic Powder Brake Factor - Lower Roll - Web 1 | `DB_02UWS_WEB_01.WEB_01.Val_FaktorRollLower` | - | 0.70 | module_segment |
| Magnetic Powder Brake Factor - Upper Roll - Web 1 | `DB_02UWS_WEB_01.WEB_01.Val_FaktorRollUpper` | - | 0.70 | module_segment |
| Film End Detection Threshold - Lower Roll - Web 1 | `DB_02UWS_WEB_01.WEB_01.Val_ThFoilEndLower` | - | 0.70 | module_segment |
| Film End Detection Threshold - Upper Roll - Web 1 | `DB_02UWS_WEB_01.WEB_01.Val_ThFoilEndUpper` | - | 0.70 | module_segment |
| Ultrasonic Sensor Reading - Lower Roll - Web 2 | `DB_02UWS_WEB_02.WEB_02.DISP_SensorRollLower` | mm | 0.70 | module_segment |
| Ultrasonic Sensor Reading - Upper Roll - Web 2 | `DB_02UWS_WEB_02.WEB_02.DISP_SensorRollUpper` | mm | 0.70 | module_segment |
| Magnetic Powder Brake Factor - Lower Roll - Web 2 | `DB_02UWS_WEB_02.WEB_02.Val_FaktorRollLower` | - | 0.70 | module_segment |
| Magnetic Powder Brake Factor - Upper Roll - Web 2 | `DB_02UWS_WEB_02.WEB_02.Val_FaktorRollUpper` | - | 0.70 | module_segment |
| Film End Detection Threshold - Lower Roll - Web 2 | `DB_02UWS_WEB_02.WEB_02.Val_ThFoilEndLower` | - | 0.70 | module_segment |
| Film End Detection Threshold - Upper Roll - Web 2 | `DB_02UWS_WEB_02.WEB_02.Val_ThFoilEndUpper` | - | 0.70 | module_segment |
| Ultrasonic Sensor Reading - Lower Roll - Web 3 | `DB_02UWS_WEB_03.WEB_03.DISP_SensorRollLower` | mm | 0.70 | module_segment |
| Ultrasonic Sensor Reading - Upper Roll - Web 3 | `DB_02UWS_WEB_03.WEB_03.DISP_SensorRollUpper` | mm | 0.70 | module_segment |
| Magnetic Powder Brake Factor - Lower Roll - Web 3 | `DB_02UWS_WEB_03.WEB_03.Val_FaktorRollLower` | - | 0.70 | module_segment |
| Magnetic Powder Brake Factor - Upper Roll - Web 3 | `DB_02UWS_WEB_03.WEB_03.Val_FaktorRollUpper` | - | 0.70 | module_segment |
| Film End Detection Threshold - Lower Roll - Web 3 | `DB_02UWS_WEB_03.WEB_03.Val_ThFoilEndLower` | - | 0.70 | module_segment |
| Film End Detection Threshold - Upper Roll - Web 3 | `DB_02UWS_WEB_03.WEB_03.Val_ThFoilEndUpper` | - | 0.70 | module_segment |
| Ultrasonic Sensor Reading - Lower Roll - Web 4 | `DB_02UWS_WEB_04.WEB_04.DISP_SensorRollLower` | mm | 0.70 | module_segment |
| Ultrasonic Sensor Reading - Upper Roll - Web 4 | `DB_02UWS_WEB_04.WEB_04.DISP_SensorRollUpper` | mm | 0.70 | module_segment |
| Magnetic Powder Brake Factor - Lower Roll - Web 4 | `DB_02UWS_WEB_04.WEB_04.Val_FaktorRollLower` | - | 0.70 | module_segment |
| Magnetic Powder Brake Factor - Upper Roll - Web 4 | `DB_02UWS_WEB_04.WEB_04.Val_FaktorRollUpper` | - | 0.70 | module_segment |
| Film End Detection Threshold - Lower Roll - Web 4 | `DB_02UWS_WEB_04.WEB_04.Val_ThFoilEndLower` | - | 0.70 | module_segment |
| Film End Detection Threshold - Upper Roll - Web 4 | `DB_02UWS_WEB_04.WEB_04.Val_ThFoilEndUpper` | - | 0.70 | module_segment |
| Remaining Cycles After Foil End (Display) - Web 1 | `DB_02UWS_WEB_01.WEB_01.DISP_WebRemCycles` | cycles | 0.75 | module_segment |
| Remaining Cycles After Foil End (Display) - Web 2 | `DB_02UWS_WEB_02.WEB_02.DISP_WebRemCycles` | cycles | 0.75 | module_segment |
| Remaining Cycles After Foil End (Display) - Web 3 | `DB_02UWS_WEB_03.WEB_03.DISP_WebRemCycles` | cycles | 0.75 | module_segment |
| Remaining Cycles After Foil End (Display) - Web 4 | `DB_02UWS_WEB_04.WEB_04.DISP_WebRemCycles` | cycles | 0.75 | module_segment |
| Remaining Cycles After Foil End (Counter 1) - Web 1 | `DB_02UWS_WEB_01.WEB_01.Val_WebRemCycles_1` | cycles | 0.80 | module_segment |
| Remaining Cycles After Foil End (Counter 2) - Web 1 | `DB_02UWS_WEB_01.WEB_01.Val_WebRemCycles_2` | cycles | 0.80 | module_segment |
| Actual Cross Adjustment Y - Web 1 | `DB_02UWS_WEB_01.WEB_01.ActualYAdjustment` | 1/10 mm | 0.80 | module_segment |
| Remaining Cycles After Foil End (Counter 1) - Web 2 | `DB_02UWS_WEB_02.WEB_02.Val_WebRemCycles_1` | cycles | 0.80 | module_segment |
| Remaining Cycles After Foil End (Counter 2) - Web 2 | `DB_02UWS_WEB_02.WEB_02.Val_WebRemCycles_2` | cycles | 0.80 | module_segment |
| Remaining Cycles After Foil End (Counter 3) - Web 2 | `DB_02UWS_WEB_02.WEB_02.Val_WebRemCycles_3` | cycles | 0.80 | module_segment |
| Actual Cross Adjustment Y - Web 2 | `DB_02UWS_WEB_02.WEB_02.ActualYAdjustment` | 1/10 mm | 0.80 | module_segment |
| Remaining Cycles After Foil End (Counter 1) - Web 3 | `DB_02UWS_WEB_03.WEB_03.Val_WebRemCycles_1` | cycles | 0.80 | module_segment |
| Remaining Cycles After Foil End (Counter 2) - Web 3 | `DB_02UWS_WEB_03.WEB_03.Val_WebRemCycles_2` | cycles | 0.80 | module_segment |
| Remaining Cycles After Foil End (Counter 3) - Web 3 | `DB_02UWS_WEB_03.WEB_03.Val_WebRemCycles_3` | cycles | 0.80 | module_segment |
| Actual Cross Adjustment Y - Web 3 | `DB_02UWS_WEB_03.WEB_03.ActualYAdjustment` | 1/10 mm | 0.80 | module_segment |
| Remaining Cycles After Foil End (Counter 1) - Web 4 | `DB_02UWS_WEB_04.WEB_04.Val_WebRemCycles_1` | cycles | 0.80 | module_segment |
| Remaining Cycles After Foil End (Counter 2) - Web 4 | `DB_02UWS_WEB_04.WEB_04.Val_WebRemCycles_2` | cycles | 0.80 | module_segment |
| Remaining Cycles After Foil End (Counter 3) - Web 4 | `DB_02UWS_WEB_04.WEB_04.Val_WebRemCycles_3` | cycles | 0.80 | module_segment |
| Actual Cross Adjustment Y - Web 4 | `DB_02UWS_WEB_04.WEB_04.ActualYAdjustment` | 1/10 mm | 0.80 | module_segment |
| Target Cross Adjustment Y - Web 1 | `DB_02UWS_WEB_01.WEB_01.TargetYAdjustment` | 1/10 mm | 0.85 | module_segment |
| Target Cross Adjustment Y - Web 2 | `DB_02UWS_WEB_02.WEB_02.TargetYAdjustment` | 1/10 mm | 0.85 | module_segment |
| Target Cross Adjustment Y - Web 3 | `DB_02UWS_WEB_03.WEB_03.TargetYAdjustment` | 1/10 mm | 0.85 | module_segment |
| Target Cross Adjustment Y - Web 4 | `DB_02UWS_WEB_04.WEB_04.TargetYAdjustment` | 1/10 mm | 0.85 | module_segment |

### FAC roll magazine (MC005-FAC)

- 79 candidate tag(s) considered -> 4 kept as genuine parameters (5%).
- Kept tags found by: 4 via *module_segment* (the tag name contains this station's own PLC/module code as a literal segment - the strongest signal available).

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| Actual Position Sensor Adjustment 1 | `DB_FAC_Data.ActualAdjustment1` | - | 0.85 | module_segment |
| Actual Position Sensor Adjustment 2 | `DB_FAC_Data.ActualAdjustment2` | - | 0.85 | module_segment |
| Target Position Sensor Adjustment 1 | `DB_FAC_Data.TargetAdjustment1` | - | 0.85 | module_segment |
| Target Position Sensor Adjustment 2 | `DB_FAC_Data.TargetAdjustment2` | - | 0.85 | module_segment |

### INS gripper-feed system & chain conveyor (MC005-INS)

- 147 candidate tag(s) considered -> 57 kept as genuine parameters (39%).
- Kept tags found by: 57 via *module_segment* (the tag name contains this station's own PLC/module code as a literal segment - the strongest signal available).

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| Servo Nominal Acceleration 01 | `04INS_Servo_Data.Servo.SP_Acc_01` | mm/s² | 0.70 | module_segment |
| Servo Nominal Acceleration 02 | `04INS_Servo_Data.Servo.SP_Acc_02` | mm/s² | 0.70 | module_segment |
| Servo Nominal Deceleration 01 | `04INS_Servo_Data.Servo.SP_Dec_01` | mm/s² | 0.70 | module_segment |
| Servo Nominal Deceleration 02 | `04INS_Servo_Data.Servo.SP_Dec_02` | mm/s² | 0.70 | module_segment |
| Servo Nominal Speed 01 | `04INS_Servo_Data.Servo.SP_Speed_01` | mm/s | 0.70 | module_segment |
| Servo Nominal Speed 02 | `04INS_Servo_Data.Servo.SP_Speed_02` | mm/s | 0.70 | module_segment |
| Flange Check Test Time | `04INS_Data.TestTimeFlangeCheck` | s | 0.75 | module_segment |
| Heater FT_1 Controller Setting | `04INS_Heater_Data.FT_1.ControlerSetting` | % | 0.75 | module_segment |
| Heater FT_1 Correction Value | `04INS_Heater_Data.FT_1.CorrectionValue` | °C | 0.75 | module_segment |
| Heater FT_1 Lower Border (Alarm Threshold) | `04INS_Heater_Data.FT_1.LowerBorder` | °C | 0.75 | module_segment |
| Heater FT_1 Upper Border (Alarm Threshold) | `04INS_Heater_Data.FT_1.UpperBorder` | °C | 0.75 | module_segment |
| Heater FT_2 Controller Setting | `04INS_Heater_Data.FT_2.ControlerSetting` | % | 0.75 | module_segment |
| Heater FT_2 Correction Value | `04INS_Heater_Data.FT_2.CorrectionValue` | °C | 0.75 | module_segment |
| Heater FT_2 Lower Border (Alarm Threshold) | `04INS_Heater_Data.FT_2.LowerBorder` | °C | 0.75 | module_segment |
| Heater FT_2 Upper Border (Alarm Threshold) | `04INS_Heater_Data.FT_2.UpperBorder` | °C | 0.75 | module_segment |
| Heater FT_3 Controller Setting | `04INS_Heater_Data.FT_3.ControlerSetting` | % | 0.75 | module_segment |
| Heater FT_3 Correction Value | `04INS_Heater_Data.FT_3.CorrectionValue` | °C | 0.75 | module_segment |
| Heater FT_3 Lower Border (Alarm Threshold) | `04INS_Heater_Data.FT_3.LowerBorder` | °C | 0.75 | module_segment |
| Heater FT_3 Upper Border (Alarm Threshold) | `04INS_Heater_Data.FT_3.UpperBorder` | °C | 0.75 | module_segment |
| Heater FT_4 Controller Setting | `04INS_Heater_Data.FT_4.ControlerSetting` | % | 0.75 | module_segment |
| Heater FT_4 Correction Value | `04INS_Heater_Data.FT_4.CorrectionValue` | °C | 0.75 | module_segment |
| Heater FT_4 Lower Border (Alarm Threshold) | `04INS_Heater_Data.FT_4.LowerBorder` | °C | 0.75 | module_segment |
| Heater FT_4 Upper Border (Alarm Threshold) | `04INS_Heater_Data.FT_4.UpperBorder` | °C | 0.75 | module_segment |
| Heater FT_5 Controller Setting | `04INS_Heater_Data.FT_5.ControlerSetting` | % | 0.75 | module_segment |
| Heater FT_5 Correction Value | `04INS_Heater_Data.FT_5.CorrectionValue` | °C | 0.75 | module_segment |
| Heater FT_5 Lower Border (Alarm Threshold) | `04INS_Heater_Data.FT_5.LowerBorder` | °C | 0.75 | module_segment |
| Heater FT_5 Upper Border (Alarm Threshold) | `04INS_Heater_Data.FT_5.UpperBorder` | °C | 0.75 | module_segment |
| Servo Current Position | `04INS_Servo_Data.Servo.DSP_CurrentPosition` | mm | 0.75 | module_segment |
| Servo Nominal Position 01 | `04INS_Servo_Data.Servo.SP_Position_01` | mm | 0.75 | module_segment |
| Servo Nominal Position 02 | `04INS_Servo_Data.Servo.SP_Position_02` | mm | 0.75 | module_segment |
| Actual Position - Infeed Chain Saranex | `04INS_Data.ActualPositionSensorInCH` | mm | 0.80 | module_segment |
| Actual Position - Infeed Chain | `04INS_Data.ActualPositionSensorInf` | mm | 0.80 | module_segment |
| Actual Position - Lower Non-Woven | `04INS_Data.ActualPositionSensorLoNW` | mm | 0.80 | module_segment |
| Actual Position - Non-Woven | `04INS_Data.ActualPositionSensorNW` | mm | 0.80 | module_segment |
| Actual Position - PTFE Belt | `04INS_Data.ActualPositionSensorPTFE` | mm | 0.80 | module_segment |
| Actual Position - Saranex | `04INS_Data.ActualPositionSensorSara` | mm | 0.80 | module_segment |
| Target Position - Infeed Chain Saranex | `04INS_Data.TargetPositionSensorInCH` | mm | 0.80 | module_segment |
| Target Position - Infeed Chain | `04INS_Data.TargetPositionSensorInf` | mm | 0.80 | module_segment |
| Target Position - Lower Non-Woven | `04INS_Data.TargetPositionSensorLoNW` | mm | 0.80 | module_segment |
| Target Position - Non-Woven | `04INS_Data.TargetPositionSensorNW` | mm | 0.80 | module_segment |
| Target Position - PTFE Belt | `04INS_Data.TargetPositionSensorPTFE` | mm | 0.80 | module_segment |
| Target Position - Saranex | `04INS_Data.TargetPositionSensorSara` | mm | 0.80 | module_segment |
| Welding Time - Foil Tack 1 | `04INS_Data.WeldingTimeTack01` | s | 0.80 | module_segment |
| Welding Time - Foil Tack 2 | `04INS_Data.WeldingTimeTack02` | s | 0.80 | module_segment |
| Welding Time - Foil Tack 3 | `04INS_Data.WeldingTimeTack03` | s | 0.80 | module_segment |
| Welding Time - Foil Tack 4 | `04INS_Data.WeldingTimeTack04` | s | 0.80 | module_segment |
| Welding Time - Foil Tack 5 | `04INS_Data.WeldingTimeTack05` | s | 0.80 | module_segment |
| Heater FT_1 Actual Temperature | `04INS_Heater_Data.FT_1.ActualValue` | °C | 0.80 | module_segment |
| Heater FT_1 Target Temperature | `04INS_Heater_Data.FT_1.TargetValue` | °C | 0.80 | module_segment |
| Heater FT_2 Actual Temperature | `04INS_Heater_Data.FT_2.ActualValue` | °C | 0.80 | module_segment |
| Heater FT_2 Target Temperature | `04INS_Heater_Data.FT_2.TargetValue` | °C | 0.80 | module_segment |
| Heater FT_3 Actual Temperature | `04INS_Heater_Data.FT_3.ActualValue` | °C | 0.80 | module_segment |
| Heater FT_3 Target Temperature | `04INS_Heater_Data.FT_3.TargetValue` | °C | 0.80 | module_segment |
| Heater FT_4 Actual Temperature | `04INS_Heater_Data.FT_4.ActualValue` | °C | 0.80 | module_segment |
| Heater FT_4 Target Temperature | `04INS_Heater_Data.FT_4.TargetValue` | °C | 0.80 | module_segment |
| Heater FT_5 Actual Temperature | `04INS_Heater_Data.FT_5.ActualValue` | °C | 0.80 | module_segment |
| Heater FT_5 Target Temperature | `04INS_Heater_Data.FT_5.TargetValue` | °C | 0.80 | module_segment |

### FSR HP filter welding station (MC005-FSR)

- 226 candidate tag(s) considered -> 55 kept as genuine parameters (24%).
- Kept tags found by: 55 via *module_segment* (the tag name contains this station's own PLC/module code as a literal segment - the strongest signal available).

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| Distance Parameter 1 (Check/Weld Spacing) | `DB_FP1_Data.Distance_1` | mm | 0.50 | module_segment |
| Distance Parameter 3 (Check/Weld Spacing) | `DB_FP1_Data.Distance_3` | mm | 0.50 | module_segment |
| Distance Parameter 4 (Check/Weld Spacing) | `DB_FP1_Data.Distance_4` | mm | 0.50 | module_segment |
| Distance Parameter 5 (Check/Weld Spacing) | `DB_FP1_Data.Distance_5` | mm | 0.50 | module_segment |
| Filter Checking Sensor 1 | `05FP1_07_S1` | - | 0.60 | module_segment |
| Filter Checking Sensor 2 | `05FP1_07_S2` | - | 0.60 | module_segment |
| Filter Checking Sensor 3 | `05FP1_07_S3` | - | 0.60 | module_segment |
| FSR Overall Weld Result | `FP1 Result` | - | 0.60 | module_segment |
| Vision Result Reject Hole - Position S1 | `FP1_Result S1` | - | 0.60 | module_segment |
| Vision Result Reject Hole - Position S2 | `FP1_Result S2` | - | 0.60 | module_segment |
| Vision Result Reject Hole - Position S3 | `FP1_Result S3` | - | 0.60 | module_segment |
| Filter Present - Loading Position | `FP1_FilterOnLoading` | - | 0.60 | module_segment |
| Filter Present - Welding Position | `FP1_FilterOnWelding` | - | 0.60 | module_segment |
| Vision Reject-Hole Image Check Result | `FP1_Reject_Hole_Vis_DB.FP1_Image_Check_Result` | - | 0.65 | module_segment |
| Vision Reject-Hole Image Processing Time | `FP1_Reject_Hole_Vis_DB.FP1_Image_Process_Time` | ms | 0.65 | module_segment |
| Revolver Actual Position | `DB_FP1_Revolver_Data.Revolver.DSP.ActPos` | ° | 0.65 | module_segment |
| Revolver Reference Offset | `DB_FP1_Revolver_Data.Revolver.DSP.ReferenceOffset` | ° | 0.65 | module_segment |
| Distance Between Check 1 and Welding | `DB_FP1_Data.Distance_2` | mm | 0.70 | module_segment |
| Servo Nominal Acceleration 01 | `DB_FP1_Data.Servo.SP_Acc_01` | mm/s² | 0.70 | module_segment |
| Servo Nominal Deceleration 01 | `DB_FP1_Data.Servo.SP_Dec_01` | mm/s² | 0.70 | module_segment |
| Servo Nominal Speed 01 | `DB_FP1_Data.Servo.SP_Speed_01` | mm/s | 0.70 | module_segment |
| Revolver Position 01 Setpoint | `DB_FP1_Revolver_Data.Revolver.SP.Position01.Position` | ° | 0.70 | module_segment |
| Revolver Position 02 Setpoint | `DB_FP1_Revolver_Data.Revolver.SP.Position02.Position` | ° | 0.70 | module_segment |
| Actual Steps - Filter End Position | `DB_FP1_Data.ActualStepsFilterEnd` | steps | 0.75 | module_segment |
| Target Steps - Filter End Position | `DB_FP1_Data.TargetStepsFilterEnd` | steps | 0.75 | module_segment |
| Actual X-Adjustment (Camera Reference) | `DB_FP1_Data.ActualXAdj_camera` | - | 0.75 | module_segment |
| Actual X-Adjustment (Hole Reference) | `DB_FP1_Data.ActualXAdj_hole` | - | 0.75 | module_segment |
| Actual X-Adjustment | `DB_FP1_Data.ActualXAdjustment` | - | 0.75 | module_segment |
| Actual Y-Adjustment (Hole Reference) | `DB_FP1_Data.ActualYAdj_hole` | - | 0.75 | module_segment |
| Actual Y-Adjustment | `DB_FP1_Data.ActualYAdjustment` | - | 0.75 | module_segment |
| Target X-Adjustment (Camera Reference) | `DB_FP1_Data.TargetXAdj_camera` | - | 0.75 | module_segment |
| Target X-Adjustment (Hole Reference) | `DB_FP1_Data.TargetXAdj_hole` | - | 0.75 | module_segment |
| Target X-Adjustment | `DB_FP1_Data.TargetXAdjustment` | - | 0.75 | module_segment |
| Target Y-Adjustment (Hole Reference) | `DB_FP1_Data.TargetYAdj_hole` | - | 0.75 | module_segment |
| Target Y-Adjustment | `DB_FP1_Data.TargetYAdjustment` | - | 0.75 | module_segment |
| Roll Empty Prewarning Delay Time | `Roll_Empty_Prewarning_DB.FP1_Roll_Empty_Delay_Tim` | s | 0.75 | module_segment |
| Blow-Off Delay Time | `FP1_BlowOff_Delay` | s | 0.75 | module_segment |
| Blow-Off Time | `FP1_BlowOff_Time` | s | 0.75 | module_segment |
| Servo Current Position | `DB_FP1_Data.Servo.DSP_CurrentPosition` | mm | 0.75 | module_segment |
| Servo Nominal Position 01 | `DB_FP1_Data.Servo.SP_Position_01` | mm | 0.75 | module_segment |
| Servo Nominal Position 02 | `DB_FP1_Data.Servo.SP_Position_02` | mm | 0.75 | module_segment |
| Heater LH Controller Setting | `DB_FP1_DataHeater.LH.ControlerSetting` | % | 0.75 | module_segment |
| Heater LH Correction Value | `DB_FP1_DataHeater.LH.CorrectionValue` | °C | 0.75 | module_segment |
| Heater LH Lower Border (Alarm Threshold) | `DB_FP1_DataHeater.LH.LowerBorder` | °C | 0.75 | module_segment |
| Heater LH Upper Border (Alarm Threshold) | `DB_FP1_DataHeater.LH.UpperBorder` | °C | 0.75 | module_segment |
| Actual Cooling Temperature | `DB_FP1_Data.ActualCoolingTemperatur` | °C | 0.80 | module_segment |
| Target Cooling Temperature | `DB_FP1_Data.TargetCoolingTemperature` | °C | 0.80 | module_segment |
| Target Hole Punch Time | `DB_FP1_Data.TargetHolePunchTime` | s | 0.80 | module_segment |
| Target Periphery Punch Time | `DB_FP1_Data.TargetPeripheryPunchTime` | s | 0.80 | module_segment |
| Target Welding Time | `DB_FP1_Data.TargetWeldingTime` | s | 0.80 | module_segment |
| Heater LH Actual Temperature | `DB_FP1_DataHeater.LH.ActualValue` | °C | 0.80 | module_segment |
| Heater LH Target Temperature | `DB_FP1_DataHeater.LH.TargetValue` | °C | 0.80 | module_segment |
| Revolver Position 01 Acceleration | `DB_FP1_Revolver_Data.Revolver.SP.Position01.AccPct` | % | 0.80 | module_segment |
| Revolver Position 01 Deceleration | `DB_FP1_Revolver_Data.Revolver.SP.Position01.DecPct` | % | 0.80 | module_segment |
| Revolver Position 01 Velocity | `DB_FP1_Revolver_Data.Revolver.SP.Position01.VelPct` | % | 0.80 | module_segment |

### FSL HP filter welding station (MC005-FSL)

- 222 candidate tag(s) considered -> 55 kept as genuine parameters (25%).
- Kept tags found by: 55 via *module_segment* (the tag name contains this station's own PLC/module code as a literal segment - the strongest signal available).

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| Distance Parameter 1 (Check/Weld Spacing) | `DB_FP2_Data.Distance_1` | mm | 0.50 | module_segment |
| Distance Parameter 3 (Check/Weld Spacing) | `DB_FP2_Data.Distance_3` | mm | 0.50 | module_segment |
| Distance Parameter 4 (Check/Weld Spacing) | `DB_FP2_Data.Distance_4` | mm | 0.50 | module_segment |
| Distance Parameter 5 (Check/Weld Spacing) | `DB_FP2_Data.Distance_5` | mm | 0.50 | module_segment |
| Filter Checking Sensor 1 | `05FP2_07_S1` | - | 0.60 | module_segment |
| Filter Checking Sensor 2 | `05FP2_07_S2` | - | 0.60 | module_segment |
| Filter Checking Sensor 3 | `05FP2_07_S3` | - | 0.60 | module_segment |
| FSL Overall Weld Result | `FP2 Result` | - | 0.60 | module_segment |
| Vision Result Reject Hole - Position S1 | `FP2_Result S1` | - | 0.60 | module_segment |
| Vision Result Reject Hole - Position S2 | `FP2 Result S2` | - | 0.60 | module_segment |
| Vision Result Reject Hole - Position S3 | `FP2 Result S3` | - | 0.60 | module_segment |
| Filter Present - Loading Position | `FP2_FilterOnLoading` | - | 0.60 | module_segment |
| Filter Present - Welding Position | `FP2_FilterOnWelding` | - | 0.60 | module_segment |
| Vision Reject-Hole Image Check Result | `FP2_Reject_Hole_Vis_DB.FP2_Image_Check_Result` | - | 0.65 | module_segment |
| Vision Reject-Hole Image Processing Time | `FP2_Reject_Hole_Vis_DB.FP2_Image_Process_Time` | ms | 0.65 | module_segment |
| Revolver Actual Position | `DB_FP2_Revolver_Data.Revolver.DSP.ActPos` | ° | 0.65 | module_segment |
| Revolver Reference Offset | `DB_FP2_Revolver_Data.Revolver.DSP.ReferenceOffset` | ° | 0.65 | module_segment |
| Distance Between Check 1 and Welding | `DB_FP2_Data.Distance_2` | mm | 0.70 | module_segment |
| Servo Nominal Acceleration 01 | `DB_FP2_Data.Servo.SP_Acc_01` | mm/s² | 0.70 | module_segment |
| Servo Nominal Deceleration 01 | `DB_FP2_Data.Servo.SP_Dec_01` | mm/s² | 0.70 | module_segment |
| Servo Nominal Speed 01 | `DB_FP2_Data.Servo.SP_Speed_01` | mm/s | 0.70 | module_segment |
| Revolver Position 01 Setpoint | `DB_FP2_Revolver_Data.Revolver.SP.Position01.Position` | ° | 0.70 | module_segment |
| Revolver Position 02 Setpoint | `DB_FP2_Revolver_Data.Revolver.SP.Position02.Position` | ° | 0.70 | module_segment |
| Actual Steps - Filter End Position | `DB_FP2_Data.ActualStepsFilterEnd` | steps | 0.75 | module_segment |
| Target Steps - Filter End Position | `DB_FP2_Data.TargetStepsFilterEnd` | steps | 0.75 | module_segment |
| Actual X-Adjustment (Camera Reference) | `DB_FP2_Data.ActualXAdj_camera` | - | 0.75 | module_segment |
| Actual X-Adjustment (Hole Reference) | `DB_FP2_Data.ActualXAdj_hole` | - | 0.75 | module_segment |
| Actual X-Adjustment | `DB_FP2_Data.ActualXAdjustment` | - | 0.75 | module_segment |
| Actual Y-Adjustment (Hole Reference) | `DB_FP2_Data.ActualYAdj_hole` | - | 0.75 | module_segment |
| Actual Y-Adjustment | `DB_FP2_Data.ActualYAdjustment` | - | 0.75 | module_segment |
| Target X-Adjustment (Camera Reference) | `DB_FP2_Data.TargetXAdj_camera` | - | 0.75 | module_segment |
| Target X-Adjustment (Hole Reference) | `DB_FP2_Data.TargetXAdj_hole` | - | 0.75 | module_segment |
| Target X-Adjustment | `DB_FP2_Data.TargetXAdjustment` | - | 0.75 | module_segment |
| Target Y-Adjustment (Hole Reference) | `DB_FP2_Data.TargetYAdj_hole` | - | 0.75 | module_segment |
| Target Y-Adjustment | `DB_FP2_Data.TargetYAdjustment` | - | 0.75 | module_segment |
| Roll Empty Prewarning Delay Time | `Roll_Empty_Prewarning_DB.FP2_Roll_Empty_Delay_Tim` | s | 0.75 | module_segment |
| Blow-Off Delay Time | `FP2_BlowOff_Delay` | s | 0.75 | module_segment |
| Blow-Off Time | `FP2_BlowOff_Time` | s | 0.75 | module_segment |
| Servo Current Position | `DB_FP2_Data.Servo.DSP_CurrentPosition` | mm | 0.75 | module_segment |
| Servo Nominal Position 01 | `DB_FP2_Data.Servo.SP_Position_01` | mm | 0.75 | module_segment |
| Servo Nominal Position 02 | `DB_FP2_Data.Servo.SP_Position_02` | mm | 0.75 | module_segment |
| Heater LH Controller Setting | `DB_FP2_DataHeater.LH.ControlerSetting` | % | 0.75 | module_segment |
| Heater LH Correction Value | `DB_FP2_DataHeater.LH.CorrectionValue` | °C | 0.75 | module_segment |
| Heater LH Lower Border (Alarm Threshold) | `DB_FP2_DataHeater.LH.LowerBorder` | °C | 0.75 | module_segment |
| Heater LH Upper Border (Alarm Threshold) | `DB_FP2_DataHeater.LH.UpperBorder` | °C | 0.75 | module_segment |
| Actual Cooling Temperature | `DB_FP2_Data.ActualCoolingTemperatur` | °C | 0.80 | module_segment |
| Target Cooling Temperature | `DB_FP2_Data.TargetCoolingTemperature` | °C | 0.80 | module_segment |
| Target Hole Punch Time | `DB_FP2_Data.TargetHolePunchTime` | s | 0.80 | module_segment |
| Target Periphery Punch Time | `DB_FP2_Data.TargetPeripheryPunchTime` | s | 0.80 | module_segment |
| Target Welding Time | `DB_FP2_Data.TargetWeldingTime` | s | 0.80 | module_segment |
| Heater LH Actual Temperature | `DB_FP2_DataHeater.LH.ActualValue` | °C | 0.80 | module_segment |
| Heater LH Target Temperature | `DB_FP2_DataHeater.LH.TargetValue` | °C | 0.80 | module_segment |
| Revolver Position 01 Acceleration | `DB_FP2_Revolver_Data.Revolver.SP.Position01.AccPct` | % | 0.80 | module_segment |
| Revolver Position 01 Deceleration | `DB_FP2_Revolver_Data.Revolver.SP.Position01.DecPct` | % | 0.80 | module_segment |
| Revolver Position 01 Velocity | `DB_FP2_Revolver_Data.Revolver.SP.Position01.VelPct` | % | 0.80 | module_segment |

### PRI printing unit (MC005-PRI)

- 115 candidate tag(s) considered -> 18 kept as genuine parameters (16%).
- Kept tags found by: 18 via *module_segment* (the tag name contains this station's own PLC/module code as a literal segment - the strongest signal available).

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| Active Print Job Name (Printer Module 1) | `PRI_PM1.JobName` | - | 0.50 | module_segment |
| Active Print Job Name (Printer Module 2) | `PRI_PM2.JobName` | - | 0.50 | module_segment |
| Heater Controller Setting - Left-Hand Side | `DB_PRI_DataHeater.LHS.ControlerSetting` | - | 0.55 | module_segment |
| Heater Controller Setting - Right-Hand Side | `DB_PRI_DataHeater.RHS.ControlerSetting` | - | 0.55 | module_segment |
| Heater Actual Temperature - Left-Hand Side | `DB_PRI_DataHeater.LHS.ActualValue` | °C | 0.60 | module_segment |
| Heater Actual Temperature - Right-Hand Side | `DB_PRI_DataHeater.RHS.ActualValue` | °C | 0.60 | module_segment |
| Heater Target Temperature - Left-Hand Side | `DB_PRI_DataHeater.LHS.TargetValue` | °C | 0.65 | module_segment |
| Heater Target Temperature - Right-Hand Side | `DB_PRI_DataHeater.RHS.TargetValue` | °C | 0.65 | module_segment |
| Actual X-Adjustment (Printing) | `DB_PRI_Data.ActualXAdjustment` | - | 0.70 | module_segment |
| Target X-Adjustment Setpoint (Printing) | `DB_PRI_Data.TargetXAdjustment` | - | 0.70 | module_segment |
| Embossing/Printing Time Setpoint - Left-Hand | `DB_PRI_Data.TargetPrintingTimeLeft` | s | 0.70 | module_segment |
| Embossing/Printing Time Setpoint - Right-Hand | `DB_PRI_Data.TargetPrintingTimeRight` | s | 0.70 | module_segment |
| Heater On/Off Setpoint - Left-Hand Side | `DB_PRI_DataHeater.Heater_LHS` | - | 0.70 | module_segment |
| Heater On/Off Setpoint - Right-Hand Side | `DB_PRI_DataHeater.Heater_RHS` | - | 0.70 | module_segment |
| Actual X-Adjustment (Printing) | `DB_PRI_SMART_Data.ActualXAdjustment` | - | 0.75 | module_segment |
| Target X-Adjustment Setpoint (Printing) | `DB_PRI_SMART_Data.TargetXAdjustment` | - | 0.75 | module_segment |
| Embossing/Printing Time Setpoint - Left-Hand | `DB_PRI_SMART_Data.TargetPrintingTimeLeft` | s | 0.75 | module_segment |
| Embossing/Printing Time Setpoint - Right-Hand | `DB_PRI_SMART_Data.TargetPrintingTimeRight` | s | 0.75 | module_segment |

### FHP/FPW flange hole-punch unit (MC005-FHP)

- 119 candidate tag(s) considered -> 28 kept as genuine parameters (24%).
- Kept tags found by: 28 via *module_segment* (the tag name contains this station's own PLC/module code as a literal segment - the strongest signal available).

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| Actual X-Adjustment - Lower Left | `DB_FHP_LL_Data.ActualXAdjust_LowerLeft` | 0.1 mm | 0.75 | module_segment |
| Actual X-Adjustment - Lower Right | `DB_FHP_LR_Data.ActualXAdjust_LowerRight` | 0.1 mm | 0.75 | module_segment |
| Actual X-Adjustment - Upper Left | `DB_FHP_UL_Data.ActualXAdjust_UpperLeft` | 0.1 mm | 0.75 | module_segment |
| Actual X-Adjustment - Upper Right | `DB_FHP_UR_Data.ActualXAdjust_UpperRight` | 0.1 mm | 0.75 | module_segment |
| Actual Y-Adjustment - Lower Left | `DB_FHP_LL_Data.ActualYAdjust_LowerLeft` | 0.1 mm | 0.75 | module_segment |
| Actual Y-Adjustment - Lower Right | `DB_FHP_LR_Data.ActualYAdjust_LowerRight` | 0.1 mm | 0.75 | module_segment |
| Actual Y-Adjustment - Upper Left | `DB_FHP_UL_Data.ActualYAdjust_UpperLeft` | 0.1 mm | 0.75 | module_segment |
| Actual Y-Adjustment - Upper Right | `DB_FHP_UR_Data.ActualYAdjust_UpperRight` | 0.1 mm | 0.75 | module_segment |
| Actual Punch Time - Lower Left | `DB_FHP_LL_Data.ActualPunchTime` | s | 0.80 | module_segment |
| Actual Punch Time - Lower Right | `DB_FHP_LR_Data.ActualPunchTime` | s | 0.80 | module_segment |
| Actual Punch Time - Upper Left | `DB_FHP_UL_Data.ActualPunchTime` | s | 0.80 | module_segment |
| Actual Punch Time - Upper Right | `DB_FHP_UR_Data.ActualPunchTime` | s | 0.80 | module_segment |
| Expeller Delay Setpoint - Lower Left | `DB_FHP_LL_Data.TargetDelayPusherTime` | s | 0.80 | module_segment |
| Expeller Delay Setpoint - Lower Right | `DB_FHP_LR_Data.TargetDelayPusherTime` | s | 0.80 | module_segment |
| Expeller Delay Setpoint - Upper Left | `DB_FHP_UL_Data.TargetDelayPusherTime` | s | 0.80 | module_segment |
| Expeller Delay Setpoint - Upper Right | `DB_FHP_UR_Data.TargetDelayPusherTime` | s | 0.80 | module_segment |
| Punch Time Setpoint - Lower Left | `DB_FHP_LL_Data.TargetPunchTime` | s | 0.80 | module_segment |
| Punch Time Setpoint - Lower Right | `DB_FHP_LR_Data.TargetPunchTime` | s | 0.80 | module_segment |
| Punch Time Setpoint - Upper Left | `DB_FHP_UL_Data.TargetPunchTime` | s | 0.80 | module_segment |
| Punch Time Setpoint - Upper Right | `DB_FHP_UR_Data.TargetPunchTime` | s | 0.80 | module_segment |
| Stroke X-Adjustment Setpoint - Lower Left | `DB_FHP_LL_Data.TargetXAdjust_LowerLeft` | 0.1 mm | 0.85 | module_segment |
| Stroke X-Adjustment Setpoint - Lower Right | `DB_FHP_LR_Data.TargetXAdjust_LowerRight` | 0.1 mm | 0.85 | module_segment |
| Stroke X-Adjustment Setpoint - Upper Left | `DB_FHP_UL_Data.TargetXAdjust_UpperLeft` | 0.1 mm | 0.85 | module_segment |
| Stroke X-Adjustment Setpoint - Upper Right | `DB_FHP_UR_Data.TargetXAdjust_UpperRight` | 0.1 mm | 0.85 | module_segment |
| Stroke Y-Adjustment Setpoint - Lower Left | `DB_FHP_LL_Data.TargetYAdjust_LowerLeft` | 0.1 mm | 0.85 | module_segment |
| Stroke Y-Adjustment Setpoint - Lower Right | `DB_FHP_LR_Data.TargetYAdjust_LowerRight` | 0.1 mm | 0.85 | module_segment |
| Stroke Y-Adjustment Setpoint - Upper Left | `DB_FHP_UL_Data.TargetYAdjust_UpperLeft` | 0.1 mm | 0.85 | module_segment |
| Stroke Y-Adjustment Setpoint - Upper Right | `DB_FHP_UR_Data.TargetYAdjust_UpperRight` | 0.1 mm | 0.85 | module_segment |

### BSW welding unit, BACKING SEAL (MC005-BSW)

- 33 candidate tag(s) considered -> 10 kept as genuine parameters (30%).
- Kept tags found by: 10 via *module_segment* (the tag name contains this station's own PLC/module code as a literal segment - the strongest signal available).

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| Heater Temperature Correction Value - Upper Heater | `DB_BSW_HeaterData.UH.CorrectionValue` | - | 0.50 | module_segment |
| BSW Heater Temperature (Converted) | `TEMP_CONVERTOR.BSW_HEATER_TEMP` | °C | 0.55 | module_segment |
| Heater Controller Setting - Upper Heater | `DB_BSW_HeaterData.UH.ControlerSetting` | - | 0.55 | module_segment |
| Heater Lower Temperature Threshold - Upper Heater | `DB_BSW_HeaterData.UH.LowerBorder` | °C | 0.60 | module_segment |
| Heater Upper Temperature Threshold - Upper Heater | `DB_BSW_HeaterData.UH.UpperBorder` | °C | 0.60 | module_segment |
| Heater Actual Temperature - Upper Heater | `DB_BSW_HeaterData.UH.ActualValue` | °C | 0.65 | module_segment |
| Heater Target Temperature - Upper Heater | `DB_BSW_HeaterData.UH.TargetValue` | °C | 0.65 | module_segment |
| Actual X-Adjustment (Backing Seal Weld) | `DB_BSW_Data.ActualXAdjustment` | - | 0.75 | module_segment |
| Target X-Adjustment Setpoint (Backing Seal Weld) | `DB_BSW_Data.TargetXAdjustment` | - | 0.75 | module_segment |
| Welding Time Setpoint (Backing Seal) | `DB_BSW_Data.TargetWeldingTime` | s | 0.80 | module_segment |

### FFG feeder turntable, GASKET (MC005-FFG)

- 64 candidate tag(s) considered -> 25 kept as genuine parameters (39%).
- Kept tags found by: 24 via *module_segment* (the tag name contains this station's own PLC/module code as a literal segment - the strongest signal available), 1 via *keyword_stem* (no PLC code matched; kept because words from this station's descriptive name appeared in the tag's own name/comment - a weaker signal, more prone to false positives).

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| Gasket Air Jet Blow Time Setpoint | `GASKET_AIR_JET_DB.Air_Jet_Timer` | s | 0.55 | keyword_stem |
| Actual Remaining Cycles After Gasket Finish | `DB_FFG_Data.ActualRemCycles` | cycles | 0.65 | module_segment |
| Pivoting Arm Current Position | `DB_FFG_Data.pivotingarm.DSP_CurrentPosition` | - | 0.65 | module_segment |
| Pivoting Arm Acceleration Setpoint 01 | `DB_FFG_Data.pivotingarm.SP_Acc_01` | - | 0.65 | module_segment |
| Pivoting Arm Acceleration Setpoint 02 | `DB_FFG_Data.pivotingarm.SP_Acc_02` | - | 0.65 | module_segment |
| Pivoting Arm Acceleration Setpoint 03 | `DB_FFG_Data.pivotingarm.SP_Acc_03` | - | 0.65 | module_segment |
| Pivoting Arm Deceleration Setpoint 01 | `DB_FFG_Data.pivotingarm.SP_Dec_01` | - | 0.65 | module_segment |
| Pivoting Arm Deceleration Setpoint 02 | `DB_FFG_Data.pivotingarm.SP_Dec_02` | - | 0.65 | module_segment |
| Pivoting Arm Deceleration Setpoint 03 | `DB_FFG_Data.pivotingarm.SP_Dec_03` | - | 0.65 | module_segment |
| Pivoting Arm Position Setpoint 01 | `DB_FFG_Data.pivotingarm.SP_Position_01` | - | 0.65 | module_segment |
| Pivoting Arm Position Setpoint 02 | `DB_FFG_Data.pivotingarm.SP_Position_02` | - | 0.65 | module_segment |
| Pivoting Arm Position Setpoint 03 | `DB_FFG_Data.pivotingarm.SP_Position_03` | - | 0.65 | module_segment |
| Pivoting Arm Speed Setpoint 01 | `DB_FFG_Data.pivotingarm.SP_Speed_01` | - | 0.65 | module_segment |
| Pivoting Arm Speed Setpoint 02 | `DB_FFG_Data.pivotingarm.SP_Speed_02` | - | 0.65 | module_segment |
| Pivoting Arm Speed Setpoint 03 | `DB_FFG_Data.pivotingarm.SP_Speed_03` | - | 0.65 | module_segment |
| Target Remaining Cycles Threshold After Gasket Finish | `DB_FFG_Data.TargetRemCycles` | cycles | 0.65 | module_segment |
| Extractor Down Delay Setpoint (New Magazine) | `DB_FFG_Data.ExtDownDelayNewMag` | s | 0.70 | module_segment |
| Extractor Middle Delay Setpoint (New Magazine) | `DB_FFG_Data.ExtMiddleDelayNewMag` | s | 0.70 | module_segment |
| Extractor Down Delay Setpoint | `DB_FFG_Data.ExtractorDownDelay` | s | 0.70 | module_segment |
| Extractor Middle Delay Setpoint | `DB_FFG_Data.ExtractorMiddleDelay` | s | 0.70 | module_segment |
| Gripper Close Delay Setpoint - Middle Position | `DB_FFG_Data.GripCloseDelayMiddle` | s | 0.70 | module_segment |
| Gripper Close Delay Setpoint - Top Position | `DB_FFG_Data.GripCloseDelayTop` | s | 0.70 | module_segment |
| Gripper Open Delay Setpoint - Top Position | `DB_FFG_Data.GripOpenDelayTop` | s | 0.70 | module_segment |
| Gripper Closing Delay Setpoint | `DB_FFG_Data.GripperClosingDelay` | s | 0.70 | module_segment |
| Gripper Opening Delay Setpoint | `DB_FFG_Data.GripperOpeningDelay` | s | 0.70 | module_segment |

### FFB feeder turntable, BARRIER (MC005-FFB)

- 71 candidate tag(s) considered -> 27 kept as genuine parameters (38%).
- Kept tags found by: 27 via *module_segment* (the tag name contains this station's own PLC/module code as a literal segment - the strongest signal available).

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| Spare Delay Time Setpoint | `DB_FFB_Data.DelaySpare` | s | 0.60 | module_segment |
| Residual Quantity in Magazine (Stack Height) | `DB_FFB_Data.StackHight` | pcs | 0.60 | module_segment |
| Lift Drive Current Position | `DB_FFB_Data.liftdrive.DSP_CurrentPosition` | - | 0.65 | module_segment |
| Lift Drive Acceleration Setpoint 01 | `DB_FFB_Data.liftdrive.SP_Acc_01` | - | 0.65 | module_segment |
| Lift Drive Acceleration Setpoint 02 | `DB_FFB_Data.liftdrive.SP_Acc_02` | - | 0.65 | module_segment |
| Lift Drive Deceleration Setpoint 01 | `DB_FFB_Data.liftdrive.SP_Dec_01` | - | 0.65 | module_segment |
| Lift Drive Deceleration Setpoint 02 | `DB_FFB_Data.liftdrive.SP_Dec_02` | - | 0.65 | module_segment |
| Lift Drive Position Setpoint 01 | `DB_FFB_Data.liftdrive.SP_Position_01` | - | 0.65 | module_segment |
| Lift Drive Position Setpoint 02 | `DB_FFB_Data.liftdrive.SP_Position_02` | - | 0.65 | module_segment |
| Lift Drive Speed Setpoint 01 | `DB_FFB_Data.liftdrive.SP_Speed_01` | - | 0.65 | module_segment |
| Lift Drive Speed Setpoint 02 | `DB_FFB_Data.liftdrive.SP_Speed_02` | - | 0.65 | module_segment |
| Pivoting Drive Current Position | `DB_FFB_Data.pivotingdrive.DSP_CurrentPosition` | - | 0.65 | module_segment |
| Pivoting Drive Acceleration Setpoint 01 | `DB_FFB_Data.pivotingdrive.SP_Acc_01` | - | 0.65 | module_segment |
| Pivoting Drive Acceleration Setpoint 02 | `DB_FFB_Data.pivotingdrive.SP_Acc_02` | - | 0.65 | module_segment |
| Pivoting Drive Acceleration Setpoint 03 | `DB_FFB_Data.pivotingdrive.SP_Acc_03` | - | 0.65 | module_segment |
| Pivoting Drive Deceleration Setpoint 01 | `DB_FFB_Data.pivotingdrive.SP_Dec_01` | - | 0.65 | module_segment |
| Pivoting Drive Deceleration Setpoint 02 | `DB_FFB_Data.pivotingdrive.SP_Dec_02` | - | 0.65 | module_segment |
| Pivoting Drive Deceleration Setpoint 03 | `DB_FFB_Data.pivotingdrive.SP_Dec_03` | - | 0.65 | module_segment |
| Pivoting Drive Position Setpoint 01 | `DB_FFB_Data.pivotingdrive.SP_Position_01` | - | 0.65 | module_segment |
| Pivoting Drive Position Setpoint 02 | `DB_FFB_Data.pivotingdrive.SP_Position_02` | - | 0.65 | module_segment |
| Pivoting Drive Position Setpoint 03 | `DB_FFB_Data.pivotingdrive.SP_Position_03` | - | 0.65 | module_segment |
| Pivoting Drive Speed Setpoint 01 | `DB_FFB_Data.pivotingdrive.SP_Speed_01` | - | 0.65 | module_segment |
| Pivoting Drive Speed Setpoint 02 | `DB_FFB_Data.pivotingdrive.SP_Speed_02` | - | 0.65 | module_segment |
| Pivoting Drive Speed Setpoint 03 | `DB_FFB_Data.pivotingdrive.SP_Speed_03` | - | 0.65 | module_segment |
| Pick-and-Place Horizontal-Forward Delay Setpoint | `DB_FFB_Data.DelayHorizontalForward` | s | 0.70 | module_segment |
| Pick-and-Place Blow-Off Time Setpoint | `DB_FFB_Data.BlowOffTime` | s | 0.70 | module_segment |
| Pick-and-Place Suction Time Setpoint | `DB_FFB_Data.SuctionTime` | s | 0.70 | module_segment |

### FWC 4S-S welding station, flange (MC005-FWC)

- 40 candidate tag(s) considered -> 11 kept as genuine parameters (28%).
- Kept tags found by: 11 via *module_segment* (the tag name contains this station's own PLC/module code as a literal segment - the strongest signal available).

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| Heater Controller Setting - Left-Hand | `DB_FWC_DataHeater.LH.ControlerSetting` | - | 0.55 | module_segment |
| Heater Actual Temperature - Left-Hand | `DB_FWC_DataHeater.LH.ActualValue` | °C | 0.65 | module_segment |
| Heater Target Temperature - Left-Hand | `DB_FWC_DataHeater.LH.TargetValue` | °C | 0.65 | module_segment |
| Heater On/Off Setpoint - Left-Hand | `DB_FWC_DataHeater.LH.HeaterSelection` | - | 0.70 | module_segment |
| Cooling Time Setpoint | `DB_FWC_Data.TargetCoolingTime` | s | 0.80 | module_segment |
| Welding Time Setpoint - Left-Hand | `DB_FWC_Data.TargetWeldingTimeLeft` | s | 0.80 | module_segment |
| Welding Time Setpoint - Right-Hand | `DB_FWC_Data.TargetWeldingTimeRight` | s | 0.80 | module_segment |
| Actual Z-Height Adjustment - Left | `DB_FWC_Data.ActualZAdjustmentLeft` | 0.01 mm | 0.85 | module_segment |
| Actual Z-Height Adjustment - Right | `DB_FWC_Data.ActualZAdjustmentRight` | 0.01 mm | 0.85 | module_segment |
| Target Z-Height Adjustment Setpoint - Left | `DB_FWC_Data.TargetZAdjustmentLeft` | 0.01 mm | 0.85 | module_segment |
| Target Z-Height Adjustment Setpoint - Right | `DB_FWC_Data.TargetZAdjustmentRight` | 0.01 mm | 0.85 | module_segment |

### ABF Binder FLAP stamping/welding unit (MC005-ABF)

- 2 candidate tag(s) considered -> 2 kept as genuine parameters (100%).
- Kept tags found by: 2 via *keyword_stem* (no PLC code matched; kept because words from this station's descriptive name appeared in the tag's own name/comment - a weaker signal, more prone to false positives).

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| Flap Sensor LHS | `Flap sensor lhs` | - | 0.60 | keyword_stem |
| Flap Sensor RHS | `Flap sensor rhs` | - | 0.60 | keyword_stem |

### ASB labelling unit, binder (MC005-ASB)

- 50 candidate tag(s) considered -> 10 kept as genuine parameters (20%).
- Kept tags found by: 10 via *module_segment* (the tag name contains this station's own PLC/module code as a literal segment - the strongest signal available).

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| Label Application Time (Left Side) | `DB_ASB_Data.LabelTime_Left` | s | 0.80 | module_segment |
| Label Application Time (Right Side) | `DB_ASB_Data.LabelTime_Right` | s | 0.80 | module_segment |
| Actual X Adjustment (LHS) | `DB_ASB_Data.ActualXAdjustment_L` | 0.1 mm | 0.85 | module_segment |
| Actual X Adjustment (RHS) | `DB_ASB_Data.ActualXAdjustment_R` | 0.1 mm | 0.85 | module_segment |
| Actual Cross (Y) Adjustment (LHS) | `DB_ASB_Data.ActualYAdjustment_L` | 0.1 mm | 0.85 | module_segment |
| Actual Cross (Y) Adjustment (RHS) | `DB_ASB_Data.ActualYAdjustment_R` | 0.1 mm | 0.85 | module_segment |
| Target X Adjustment (LHS) | `DB_ASB_Data.TargetXAdjustment_L` | 0.1 mm | 0.85 | module_segment |
| Target X Adjustment (RHS) | `DB_ASB_Data.TargetXAdjustment_R` | 0.1 mm | 0.85 | module_segment |
| Target Cross (Y) Adjustment (LHS) | `DB_ASB_Data.TargetYAdjustment_L` | 0.1 mm | 0.90 | module_segment |
| Target Cross (Y) Adjustment (RHS) | `DB_ASB_Data.TargetYAdjustment_R` | 0.1 mm | 0.90 | module_segment |

### PWC 4S-welding station, circumference (MC005-PWC)

- 153 candidate tag(s) considered -> 89 kept as genuine parameters (58%).
- Kept tags found by: 89 via *module_segment* (the tag name contains this station's own PLC/module code as a literal segment - the strongest signal available).

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| Solid State Relay Output Status, Belt Lower Heater | `DB_PWC_DataHeater.Belt_LH.OutputSSD` | - | 0.50 | module_segment |
| Solid State Relay Output Status, Belt Upper Heater | `DB_PWC_DataHeater.Belt_UH.OutputSSD` | - | 0.50 | module_segment |
| Solid State Relay Output Status, Lower Heater | `DB_PWC_DataHeater.LH.OutputSSD` | - | 0.50 | module_segment |
| Solid State Relay Output Status, Upper Heater | `DB_PWC_DataHeater.UH.OutputSSD` | - | 0.50 | module_segment |
| External Load Cell Calibration Value 1 (Main Servo) | `DB_PWC_Data.Servo.SP_Extern_Force_1` | N | 0.55 | module_segment |
| External Load Cell Calibration Value 2 (Main Servo) | `DB_PWC_Data.Servo.SP_Extern_Force_2` | N | 0.55 | module_segment |
| Load Cell Calibration Target, Point 1 (Main Servo) | `DB_PWC_Data.Servo.SP_Target_Cali_Point1` | mV | 0.55 | module_segment |
| Load Cell Calibration Target, Point 2 (Main Servo) | `DB_PWC_Data.Servo.SP_Target_Cali_Point2` | mV | 0.55 | module_segment |
| Load Cell Calibration Target, Point 1 (Belt Servo) | `DB_PWC_Data.Servo_Belt.SP_Target_Cali_Point1` | mV | 0.55 | module_segment |
| Load Cell Calibration Target, Point 2 (Belt Servo) | `DB_PWC_Data.Servo_Belt.SP_Target_Cali_Point2` | mV | 0.55 | module_segment |
| Controller Setting, Belt Lower Heater | `DB_PWC_DataHeater.Belt_LH.ControlerSetting` | - | 0.55 | module_segment |
| Controller Setting, Belt Upper Heater | `DB_PWC_DataHeater.Belt_UH.ControlerSetting` | - | 0.55 | module_segment |
| Controller Setting, Lower Heater | `DB_PWC_DataHeater.LH.ControlerSetting` | - | 0.55 | module_segment |
| Controller Setting, Upper Heater | `DB_PWC_DataHeater.UH.ControlerSetting` | - | 0.55 | module_segment |
| Actual Tox Cylinder Value (Belt Welding) | `DB_PWC_BeltWelding.ActualToxBeltWelding` | - | 0.70 | module_segment |
| Target Tox Cylinder Value (Belt Welding) | `DB_PWC_BeltWelding.TargetToxBeltwelding` | - | 0.70 | module_segment |
| Belt Welding Measuring Run Result | `DB_PWC_Data.SearchStrokeResultBelt` | - | 0.70 | module_segment |
| Detected Touch-Down Point (Main Servo) | `DB_PWC_Data.Servo.DSP_TouchPoint_Detected` | - | 0.70 | module_segment |
| Touch-Down Point 1 / Regulation Start (Main Servo) | `DB_PWC_Data.Servo.DSP_TouchPoint_Start` | - | 0.70 | module_segment |
| Stored Touch-Down Point (Main Servo) | `DB_PWC_Data.Servo.DSP_TouchPoint_Stored` | - | 0.70 | module_segment |
| Nominal Relative Position, Foil Width (Main Servo) | `DB_PWC_Data.Servo.SP_Rel_Pos_FoilWidth` | - | 0.70 | module_segment |
| Nominal Relative Position, Regulation Range (Main Servo) | `DB_PWC_Data.Servo.SP_Rel_Pos_RangeRegu` | - | 0.70 | module_segment |
| Detected Touch-Down Point (Belt Servo) | `DB_PWC_Data.Servo_Belt.DSP_TouchPoint_Detected` | - | 0.70 | module_segment |
| Touch-Down Point 1 / Regulation Start (Belt Servo) | `DB_PWC_Data.Servo_Belt.DSP_TouchPoint_Start` | - | 0.70 | module_segment |
| Stored Touch-Down Point (Belt Servo) | `DB_PWC_Data.Servo_Belt.DSP_TouchPoint_Stored` | - | 0.70 | module_segment |
| Nominal Relative Position, Foil Width (Belt Servo) | `DB_PWC_Data.Servo_Belt.SP_Rel_Pos_FoilWidth` | - | 0.70 | module_segment |
| Nominal Relative Position, Regulation Range (Belt Servo) | `DB_PWC_Data.Servo_Belt.SP_Rel_Pos_RangeRegu` | - | 0.70 | module_segment |
| Actual Position Output (Main Servo) | `DB_PWC_Data.Servo.DSP_Actual_Position` | - | 0.75 | module_segment |
| Nominal Acceleration, Closing (Main Servo) | `DB_PWC_Data.Servo.SP_Acc_Closing` | - | 0.75 | module_segment |
| Nominal Acceleration, Opening (Main Servo) | `DB_PWC_Data.Servo.SP_Acc_Opening` | - | 0.75 | module_segment |
| Nominal Deceleration, Closing (Main Servo) | `DB_PWC_Data.Servo.SP_Dec_Closing` | - | 0.75 | module_segment |
| Nominal Deceleration, Opening (Main Servo) | `DB_PWC_Data.Servo.SP_Dec_Opening` | - | 0.75 | module_segment |
| Maximum Mechanical Stroke (Main Servo) | `DB_PWC_Data.Servo.SP_MaxPosition` | - | 0.75 | module_segment |
| Nominal Position, Open (Main Servo) | `DB_PWC_Data.Servo.SP_Position_open` | - | 0.75 | module_segment |
| Welding Pressure Tolerance, Lower Limit (Main Servo) | `DB_PWC_Data.Servo.SP_Pressure_Tolerance_lo` | - | 0.75 | module_segment |
| Welding Pressure Tolerance, Upper Limit (Main Servo) | `DB_PWC_Data.Servo.SP_Pressure_Tolerance_up` | - | 0.75 | module_segment |
| Nominal Speed, Closing (Main Servo) | `DB_PWC_Data.Servo.SP_Speed_Closingg` | - | 0.75 | module_segment |
| Nominal Speed, Opening (Main Servo) | `DB_PWC_Data.Servo.SP_Speed_Opening` | - | 0.75 | module_segment |
| Actual Position Output (Belt Servo) | `DB_PWC_Data.Servo_Belt.DSP_Actual_Position` | - | 0.75 | module_segment |
| Nominal Acceleration, Closing (Belt Servo) | `DB_PWC_Data.Servo_Belt.SP_Acc_Closing` | - | 0.75 | module_segment |
| Nominal Acceleration, Opening (Belt Servo) | `DB_PWC_Data.Servo_Belt.SP_Acc_Opening` | - | 0.75 | module_segment |
| Nominal Deceleration, Closing (Belt Servo) | `DB_PWC_Data.Servo_Belt.SP_Dec_Closing` | - | 0.75 | module_segment |
| Nominal Deceleration, Opening (Belt Servo) | `DB_PWC_Data.Servo_Belt.SP_Dec_Opening` | - | 0.75 | module_segment |
| Maximum Mechanical Stroke (Belt Servo) | `DB_PWC_Data.Servo_Belt.SP_MaxPosition` | - | 0.75 | module_segment |
| Nominal Position, Open (Belt Servo) | `DB_PWC_Data.Servo_Belt.SP_Position_open` | - | 0.75 | module_segment |
| Nominal Speed, Closing (Belt Servo) | `DB_PWC_Data.Servo_Belt.SP_Speed_Closingg` | - | 0.75 | module_segment |
| Nominal Speed, Opening (Belt Servo) | `DB_PWC_Data.Servo_Belt.SP_Speed_Opening` | - | 0.75 | module_segment |
| Nominal Heating-Up Temperature, Belt Welding (Stage 2) | `DB_PWC_Data.TargetTempBelt_2` | °C | 0.75 | module_segment |
| Heater Enable Setpoint, Belt Lower Heater | `DB_PWC_DataHeater.Belt_LH.HeaterSelection` | - | 0.75 | module_segment |
| Lower Temperature Threshold, Belt Lower Heater | `DB_PWC_DataHeater.Belt_LH.LowerBorder` | °C | 0.75 | module_segment |
| Upper Temperature Threshold, Belt Lower Heater | `DB_PWC_DataHeater.Belt_LH.UpperBorder` | °C | 0.75 | module_segment |
| Heater Enable Setpoint, Belt Upper Heater | `DB_PWC_DataHeater.Belt_UH.HeaterSelection` | - | 0.75 | module_segment |
| Lower Temperature Threshold, Belt Upper Heater | `DB_PWC_DataHeater.Belt_UH.LowerBorder` | °C | 0.75 | module_segment |
| Upper Temperature Threshold, Belt Upper Heater | `DB_PWC_DataHeater.Belt_UH.UpperBorder` | °C | 0.75 | module_segment |
| Heater Enable Setpoint, Lower Heater | `DB_PWC_DataHeater.LH.HeaterSelection` | - | 0.75 | module_segment |
| Lower Temperature Threshold, Lower Heater | `DB_PWC_DataHeater.LH.LowerBorder` | °C | 0.75 | module_segment |
| Upper Temperature Threshold, Lower Heater | `DB_PWC_DataHeater.LH.UpperBorder` | °C | 0.75 | module_segment |
| Heater Enable Setpoint, Upper Heater | `DB_PWC_DataHeater.UH.HeaterSelection` | - | 0.75 | module_segment |
| Lower Temperature Threshold, Upper Heater | `DB_PWC_DataHeater.UH.LowerBorder` | °C | 0.75 | module_segment |
| Upper Temperature Threshold, Upper Heater | `DB_PWC_DataHeater.UH.UpperBorder` | °C | 0.75 | module_segment |
| Actual Cooling Agent Temperature (Rail) | `DB_PWC_Cooling.ActualCoolingTempRail` | °C | 0.80 | module_segment |
| Cooling Agent Temperature Switching Threshold (Rail) | `DB_PWC_Cooling.TargetCoolingTempRail` | °C | 0.80 | module_segment |
| Actual Cooling Agent Temperature | `DB_PWC_Data.ActualCoolingTemperatur` | °C | 0.80 | module_segment |
| Load Cell Output Voltage (Main Servo) | `DB_PWC_Data.Servo.LoadCell` | mV | 0.80 | module_segment |
| Cooling Agent Temperature Switching Threshold | `DB_PWC_Data.TargetCoolingTemperature` | °C | 0.80 | module_segment |
| Nominal Cooling Time | `DB_PWC_Data.TargetCoolingTime` | s | 0.80 | module_segment |
| Nominal Heating-Up Temperature, Belt Welding (Stage 1) | `DB_PWC_Data.TargetTempBelt_1` | °C | 0.80 | module_segment |
| Nominal Cooling-Down Temperature, Belt Welding | `DB_PWC_Data.TargetTempBelt_3` | °C | 0.80 | module_segment |
| Nominal Welding Time | `DB_PWC_Data.TargetWeldingTime` | s | 0.80 | module_segment |
| Actual Temperature, Belt Lower Heater | `DB_PWC_DataHeater.Belt_LH.ActualValue` | °C | 0.80 | module_segment |
| Correction Value, Belt Lower Heater | `DB_PWC_DataHeater.Belt_LH.CorrectionValue` | 0.1 °C | 0.80 | module_segment |
| Actual Temperature, Belt Upper Heater | `DB_PWC_DataHeater.Belt_UH.ActualValue` | °C | 0.80 | module_segment |
| Correction Value, Belt Upper Heater | `DB_PWC_DataHeater.Belt_UH.CorrectionValue` | 0.1 °C | 0.80 | module_segment |
| Actual Temperature, Lower Heater | `DB_PWC_DataHeater.LH.ActualValue` | °C | 0.80 | module_segment |
| Correction Value, Lower Heater | `DB_PWC_DataHeater.LH.CorrectionValue` | 0.1 °C | 0.80 | module_segment |
| Actual Temperature, Upper Heater | `DB_PWC_DataHeater.UH.ActualValue` | °C | 0.80 | module_segment |
| Correction Value, Upper Heater | `DB_PWC_DataHeater.UH.CorrectionValue` | 0.1 °C | 0.80 | module_segment |
| Actual Lengthwise (X) Adjustment | `DB_PWC_Data.ActualXAdjustment` | 0.1 mm | 0.85 | module_segment |
| Actual Cross (Y) Adjustment | `DB_PWC_Data.ActualYAdjustment` | 0.1 mm | 0.85 | module_segment |
| Actual Closing Force (Main Servo) | `DB_PWC_Data.Servo.DSP_Actual_Moment` | N | 0.85 | module_segment |
| Nominal Closing Force (Main Servo) | `DB_PWC_Data.Servo.SP_force` | N | 0.85 | module_segment |
| Actual Closing Force (Belt Servo) | `DB_PWC_Data.Servo_Belt.DSP_Actual_Moment` | N | 0.85 | module_segment |
| Nominal Closing Force (Belt Servo) | `DB_PWC_Data.Servo_Belt.SP_force` | N | 0.85 | module_segment |
| Nominal Temperature, Belt Lower Heater | `DB_PWC_DataHeater.Belt_LH.TargetValue` | °C | 0.85 | module_segment |
| Nominal Temperature, Belt Upper Heater | `DB_PWC_DataHeater.Belt_UH.TargetValue` | °C | 0.85 | module_segment |
| Nominal Temperature, Lower Heater | `DB_PWC_DataHeater.LH.TargetValue` | °C | 0.85 | module_segment |
| Nominal Temperature, Upper Heater | `DB_PWC_DataHeater.UH.TargetValue` | °C | 0.85 | module_segment |
| Target Lengthwise (X) Adjustment | `DB_PWC_Data.TargetXAdjustment` | 0.1 mm | 0.90 | module_segment |
| Target Cross (Y) Adjustment | `DB_PWC_Data.TargetYAdjustment` | 0.1 mm | 0.90 | module_segment |

### ASC labelling unit, re-heating station, testing station (MC005-ASC)

- 171 candidate tag(s) considered -> 67 kept as genuine parameters (39%).
- Kept tags found by: 67 via *module_segment* (the tag name contains this station's own PLC/module code as a literal segment - the strongest signal available).
- 8 kept parameter(s) below 0.5 confidence - flagged with ⚠ below.

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| Solid State Relay Output Status, Lower Heater LHS ⚠ | `DB_ASC_HeaterData.LH_LHS.OutputSSD` | - | 0.40 | module_segment |
| Solid State Relay Output Status, Lower Heater RHS ⚠ | `DB_ASC_HeaterData.LH_RHS.OutputSSD` | - | 0.40 | module_segment |
| Solid State Relay Output Status, Upper Heater LHS ⚠ | `DB_ASC_HeaterData.UH_LHS.OutputSSD` | - | 0.40 | module_segment |
| Solid State Relay Output Status, Upper Heater RHS ⚠ | `DB_ASC_HeaterData.UH_RHS.OutputSSD` | - | 0.40 | module_segment |
| Controller Setting, Lower Heater LHS ⚠ | `DB_ASC_HeaterData.LH_LHS.ControlerSetting` | - | 0.45 | module_segment |
| Controller Setting, Lower Heater RHS ⚠ | `DB_ASC_HeaterData.LH_RHS.ControlerSetting` | - | 0.45 | module_segment |
| Controller Setting, Upper Heater LHS ⚠ | `DB_ASC_HeaterData.UH_LHS.ControlerSetting` | - | 0.45 | module_segment |
| Controller Setting, Upper Heater RHS ⚠ | `DB_ASC_HeaterData.UH_RHS.ControlerSetting` | - | 0.45 | module_segment |
| Actual Temperature, Lower Heater LHS | `DB_ASC_HeaterData.LH_LHS.ActualValue` | °C | 0.55 | module_segment |
| Correction Value, Lower Heater LHS | `DB_ASC_HeaterData.LH_LHS.CorrectionValue` | 0.1 °C | 0.55 | module_segment |
| Heater Enable Setpoint, Lower Heater LHS | `DB_ASC_HeaterData.LH_LHS.HeaterSelection` | - | 0.55 | module_segment |
| Lower Temperature Threshold, Lower Heater LHS | `DB_ASC_HeaterData.LH_LHS.LowerBorder` | °C | 0.55 | module_segment |
| Upper Temperature Threshold, Lower Heater LHS | `DB_ASC_HeaterData.LH_LHS.UpperBorder` | °C | 0.55 | module_segment |
| Actual Temperature, Lower Heater RHS | `DB_ASC_HeaterData.LH_RHS.ActualValue` | °C | 0.55 | module_segment |
| Correction Value, Lower Heater RHS | `DB_ASC_HeaterData.LH_RHS.CorrectionValue` | 0.1 °C | 0.55 | module_segment |
| Heater Enable Setpoint, Lower Heater RHS | `DB_ASC_HeaterData.LH_RHS.HeaterSelection` | - | 0.55 | module_segment |
| Lower Temperature Threshold, Lower Heater RHS | `DB_ASC_HeaterData.LH_RHS.LowerBorder` | °C | 0.55 | module_segment |
| Upper Temperature Threshold, Lower Heater RHS | `DB_ASC_HeaterData.LH_RHS.UpperBorder` | °C | 0.55 | module_segment |
| Actual Temperature, Upper Heater LHS | `DB_ASC_HeaterData.UH_LHS.ActualValue` | °C | 0.55 | module_segment |
| Correction Value, Upper Heater LHS | `DB_ASC_HeaterData.UH_LHS.CorrectionValue` | 0.1 °C | 0.55 | module_segment |
| Heater Enable Setpoint, Upper Heater LHS | `DB_ASC_HeaterData.UH_LHS.HeaterSelection` | - | 0.55 | module_segment |
| Lower Temperature Threshold, Upper Heater LHS | `DB_ASC_HeaterData.UH_LHS.LowerBorder` | °C | 0.55 | module_segment |
| Upper Temperature Threshold, Upper Heater LHS | `DB_ASC_HeaterData.UH_LHS.UpperBorder` | °C | 0.55 | module_segment |
| Actual Temperature, Upper Heater RHS | `DB_ASC_HeaterData.UH_RHS.ActualValue` | °C | 0.55 | module_segment |
| Correction Value, Upper Heater RHS | `DB_ASC_HeaterData.UH_RHS.CorrectionValue` | 0.1 °C | 0.55 | module_segment |
| Heater Enable Setpoint, Upper Heater RHS | `DB_ASC_HeaterData.UH_RHS.HeaterSelection` | - | 0.55 | module_segment |
| Lower Temperature Threshold, Upper Heater RHS | `DB_ASC_HeaterData.UH_RHS.LowerBorder` | °C | 0.55 | module_segment |
| Upper Temperature Threshold, Upper Heater RHS | `DB_ASC_HeaterData.UH_RHS.UpperBorder` | °C | 0.55 | module_segment |
| Nominal Temperature, Lower Heater LHS | `DB_ASC_HeaterData.LH_LHS.TargetValue` | °C | 0.60 | module_segment |
| Nominal Temperature, Lower Heater RHS | `DB_ASC_HeaterData.LH_RHS.TargetValue` | °C | 0.60 | module_segment |
| Nominal Temperature, Upper Heater LHS | `DB_ASC_HeaterData.UH_LHS.TargetValue` | °C | 0.60 | module_segment |
| Nominal Temperature, Upper Heater RHS | `DB_ASC_HeaterData.UH_RHS.TargetValue` | °C | 0.60 | module_segment |
| Indicated Cycle Time, Station | `DB_ASC_Data.IndicatCycleTimeStation` | s | 0.70 | module_segment |
| Label Application Time (Lower Left) | `DB_ASC_Data.LabelTime_LowerLeft` | s | 0.80 | module_segment |
| Label Application Time (Lower Right) | `DB_ASC_Data.LabelTime_LowerRight` | s | 0.80 | module_segment |
| Label Application Time (Upper Left) | `DB_ASC_Data.LabelTime_UpperLeft` | s | 0.80 | module_segment |
| Label Application Time (Upper Right) | `DB_ASC_Data.LabelTime_UpperRight` | s | 0.80 | module_segment |
| Heating Time, Reheat (Upper Left Side) | `DB_ASC_Reheat_Data.HeatingTime_Left` | s | 0.80 | module_segment |
| Heating Time, Reheat (Upper Right Side) | `DB_ASC_Reheat_Data.HeatingTime_Right` | s | 0.80 | module_segment |
| Actual X Adjustment, Test Station (Left) | `DB_ASC_Test_Data.ActualXAdjustment_L` | 0.1 mm | 0.80 | module_segment |
| Actual X Adjustment, Test Station (Right) | `DB_ASC_Test_Data.ActualXAdjustment_R` | 0.1 mm | 0.80 | module_segment |
| Target X Adjustment, Test Station (Left) | `DB_ASC_Test_Data.TargetXAdjustment_L` | 0.1 mm | 0.80 | module_segment |
| Target X Adjustment, Test Station (Right) | `DB_ASC_Test_Data.TargetXAdjustment_R` | 0.1 mm | 0.80 | module_segment |
| Actual X Adjustment (Lower Left) | `DB_ASC_Data.ActualXAdjustment_LL` | 0.1 mm | 0.85 | module_segment |
| Actual X Adjustment (Lower Right) | `DB_ASC_Data.ActualXAdjustment_LR` | 0.1 mm | 0.85 | module_segment |
| Actual X Adjustment (Upper Left) | `DB_ASC_Data.ActualXAdjustment_UL` | 0.1 mm | 0.85 | module_segment |
| Actual X Adjustment (Upper Right) | `DB_ASC_Data.ActualXAdjustment_UR` | 0.1 mm | 0.85 | module_segment |
| Actual Cross (Y) Adjustment (Lower Left) | `DB_ASC_Data.ActualYAdjustment_LL` | 0.1 mm | 0.85 | module_segment |
| Actual Cross (Y) Adjustment (Lower Right) | `DB_ASC_Data.ActualYAdjustment_LR` | 0.1 mm | 0.85 | module_segment |
| Actual Cross (Y) Adjustment (Upper Left) | `DB_ASC_Data.ActualYAdjustment_UL` | 0.1 mm | 0.85 | module_segment |
| Actual Cross (Y) Adjustment (Upper Right) | `DB_ASC_Data.ActualYAdjustment_UR` | 0.1 mm | 0.85 | module_segment |
| Target X Adjustment (Lower Left) | `DB_ASC_Data.TargetXAdjustment_LL` | 0.1 mm | 0.85 | module_segment |
| Target X Adjustment (Lower Right) | `DB_ASC_Data.TargetXAdjustment_LR` | 0.1 mm | 0.85 | module_segment |
| Target X Adjustment (Upper Left) | `DB_ASC_Data.TargetXAdjustment_UL` | 0.1 mm | 0.85 | module_segment |
| Target X Adjustment (Upper Right) | `DB_ASC_Data.TargetXAdjustment_UR` | 0.1 mm | 0.85 | module_segment |
| Actual X Adjustment, Reheat (Left) | `DB_ASC_Reheat_Data.ActualXAdjustment_L` | 0.1 mm | 0.85 | module_segment |
| Actual X Adjustment, Reheat (Right) | `DB_ASC_Reheat_Data.ActualXAdjustment_R` | 0.1 mm | 0.85 | module_segment |
| Actual Cross (Y) Adjustment, Reheat (Left) | `DB_ASC_Reheat_Data.ActualYAdjustment_L` | 0.1 mm | 0.85 | module_segment |
| Actual Cross (Y) Adjustment, Reheat (Right) | `DB_ASC_Reheat_Data.ActualYAdjustment_R` | 0.1 mm | 0.85 | module_segment |
| Target X Adjustment, Reheat (Left) | `DB_ASC_Reheat_Data.TargetXAdjustment_L` | 0.1 mm | 0.85 | module_segment |
| Target X Adjustment, Reheat (Right) | `DB_ASC_Reheat_Data.TargetXAdjustment_R` | 0.1 mm | 0.85 | module_segment |
| Target Cross (Y) Adjustment (Lower Left) | `DB_ASC_Data.TargetYAdjustment_LL` | 0.1 mm | 0.90 | module_segment |
| Target Cross (Y) Adjustment (Lower Right) | `DB_ASC_Data.TargetYAdjustment_LR` | 0.1 mm | 0.90 | module_segment |
| Target Cross (Y) Adjustment (Upper Left) | `DB_ASC_Data.TargetYAdjustment_UL` | 0.1 mm | 0.90 | module_segment |
| Target Cross (Y) Adjustment (Upper Right) | `DB_ASC_Data.TargetYAdjustment_UR` | 0.1 mm | 0.90 | module_segment |
| Target Cross (Y) Adjustment, Reheat (Left) | `DB_ASC_Reheat_Data.TargetYAdjustment_L` | 0.1 mm | 0.90 | module_segment |
| Target Cross (Y) Adjustment, Reheat (Right) | `DB_ASC_Reheat_Data.TargetYAdjustment_R` | 0.1 mm | 0.90 | module_segment |

### PPS 4S-cutout station, circumference (MC005-PPS)

- 28 candidate tag(s) considered -> 9 kept as genuine parameters (32%).
- Kept tags found by: 9 via *module_segment* (the tag name contains this station's own PLC/module code as a literal segment - the strongest signal available).

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| Indicated Cycle Time, Station SQ | `DB_PPS_Data.IndicatCycleTimeStat` | s | 0.70 | module_segment |
| Current Punching Time | `DB_PPS_Data.ActualPunchTime` | - | 0.75 | module_segment |
| Nominal Punching Time | `DB_PPS_Data.TargetPunchTime` | - | 0.75 | module_segment |
| Actual Lengthwise (X) Adjustment | `DB_PPS_Data.ActualXAdjustment` | 0.1 mm | 0.85 | module_segment |
| Actual Cross (Y) Adjustment | `DB_PPS_Data.ActualYAdjustment` | 0.1 mm | 0.85 | module_segment |
| Actual Height (Z) Adjustment | `DB_PPS_Data.ActualZAdjustment` | 0.01 mm | 0.90 | module_segment |
| Target Lengthwise (X) Adjustment | `DB_PPS_Data.TargetXAdjustment` | 0.1 mm | 0.90 | module_segment |
| Target Cross (Y) Adjustment | `DB_PPS_Data.TargetYAdjustment` | 0.1 mm | 0.90 | module_segment |
| Target Height (Z) Adjustment | `DB_PPS_Data.TargetZAdjustment` | 0.01 mm | 0.90 | module_segment |

### ULS removal point (MC005-ULS)

- 59 candidate tag(s) considered -> 24 kept as genuine parameters (41%).
- Kept tags found by: 24 via *module_segment* (the tag name contains this station's own PLC/module code as a literal segment - the strongest signal available).

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| Actual Stacking Height | `DB_ULS_Data.ActualStack` | - | 0.75 | module_segment |
| Actual Servo Position | `DB_ULS_Data.Is_Position` | - | 0.75 | module_segment |
| Nominal Acceleration 1 (Servo) | `DB_ULS_Data.servo.SP_Acc_01` | - | 0.75 | module_segment |
| Nominal Acceleration 2 (Servo) | `DB_ULS_Data.servo.SP_Acc_02` | - | 0.75 | module_segment |
| Nominal Acceleration 3 (Servo) | `DB_ULS_Data.servo.SP_Acc_03` | - | 0.75 | module_segment |
| Nominal Deceleration 1 (Servo) | `DB_ULS_Data.servo.SP_Dec_01` | - | 0.75 | module_segment |
| Nominal Deceleration 2 (Servo) | `DB_ULS_Data.servo.SP_Dec_02` | - | 0.75 | module_segment |
| Nominal Deceleration 3 (Servo) | `DB_ULS_Data.servo.SP_Dec_03` | - | 0.75 | module_segment |
| Nominal Position 1 (Servo) | `DB_ULS_Data.servo.SP_Position_01` | - | 0.75 | module_segment |
| Nominal Position 2 (Servo) | `DB_ULS_Data.servo.SP_Position_02` | - | 0.75 | module_segment |
| Nominal Position 3 (Servo) | `DB_ULS_Data.servo.SP_Position_03` | - | 0.75 | module_segment |
| Nominal Speed 1 (Servo) | `DB_ULS_Data.servo.SP_Speed_01` | - | 0.75 | module_segment |
| Nominal Speed 2 (Servo) | `DB_ULS_Data.servo.SP_Speed_02` | - | 0.75 | module_segment |
| Nominal Speed 3 (Servo) | `DB_ULS_Data.servo.SP_Speed_03` | - | 0.75 | module_segment |
| Nominal Reverse Time, Fife | `DB_ULS_Data.TargetReverseTimeFife` | s | 0.75 | module_segment |
| Nominal Stacking Height | `DB_ULS_Data.TargetStack` | - | 0.75 | module_segment |
| Actual Lengthwise (X) Adjustment | `DB_ULS_Data.ActualXAdjustment` | 0.1 mm | 0.80 | module_segment |
| Actual Cross (Y) Adjustment | `DB_ULS_Data.ActualYAdjustment` | 0.1 mm | 0.80 | module_segment |
| Nominal Belt Running Time, Long Step | `DB_ULS_Data.TargetBeltTimeLongStep` | s | 0.80 | module_segment |
| Nominal Belt Running Time, Short Step | `DB_ULS_Data.TargetBeltTimeShortStep` | s | 0.80 | module_segment |
| Nominal Blow-Off Time, Unload | `DB_ULS_Data.TargetBlowOffTimeUnload` | s | 0.80 | module_segment |
| Nominal Suction (Vacuum) Time, Unloader | `DB_ULS_Data.TargetVacuumTimeUnloader` | s | 0.80 | module_segment |
| Target Lengthwise (X) Adjustment | `DB_ULS_Data.TargetXAdjustment` | 0.1 mm | 0.85 | module_segment |
| Target Cross (Y) Adjustment | `DB_ULS_Data.TargetYAdjustment` | 0.1 mm | 0.85 | module_segment |
