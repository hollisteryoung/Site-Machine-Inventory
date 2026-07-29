# Tag Matching Report - Line K14

This summarizes, for every station found on this line, which historian tags were kept as genuine process parameters and why. Parameters marked with a low match strategy (keyword/keyword_stem/legend_code/folder_match) or below 0.5 confidence are the ones most worth a second look from someone who knows the physical machine.

## Summary

- 19 station(s) processed.
- 4599 candidate tag(s) considered across all stations -> 1110 kept as genuine parameters (24% of candidates).
- 1110 of this line's 5843 total historian tags (19.0%) ended up mapped to a genuine parameter - this is the actual coverage of the raw tag export, as opposed to the conversion rate above, which only measures the pre-filtered candidate pool.
- 114 kept parameter(s) below 0.5 confidence overall - worth a second look.
- 1 station(s) with no genuine parameters found at all: COR corona surface-treatment station (printer control module) (MC007-COR).

## Machine: Inline System KIT 70/20

### UWS unwinding station (MC007-UWS)

- 306 candidate tag(s) considered -> 105 kept as genuine parameters (34%).
- Kept tags found by: 105 via *module_segment* (the tag name contains this station's own PLC/module code as a literal segment - the strongest signal available).
- 12 kept parameter(s) below 0.5 confidence - flagged with ⚠ below.

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| UWS Web 1 Dancer Force Control Active ⚠ | `L01S_UWS_DB_HMI_connect.Web_1.Dancer.DFC_ON` | - | 0.35 | module_segment |
| UWS Web 2 Dancer Force Control Active ⚠ | `L01S_UWS_DB_HMI_connect.Web_2.Dancer.DFC_ON` | - | 0.35 | module_segment |
| UWS Web 3 Dancer Force Control Active ⚠ | `L01S_UWS_DB_HMI_connect.Web_3.Dancer.DFC_ON` | - | 0.35 | module_segment |
| UWS Web 4 Dancer Force Control Active ⚠ | `L01S_UWS_DB_HMI_connect.Web_4.Dancer.DFC_ON` | - | 0.35 | module_segment |
| UWS Web 1 Dancer Position Lower Limit ⚠ | `L01S_UWS_DB_HMI_connect.Web_1.Dancer.LowerLimit` | mm | 0.40 | module_segment |
| UWS Web 1 Dancer Position Upper Limit ⚠ | `L01S_UWS_DB_HMI_connect.Web_1.Dancer.UpperLimit` | mm | 0.40 | module_segment |
| UWS Web 2 Dancer Position Lower Limit ⚠ | `L01S_UWS_DB_HMI_connect.Web_2.Dancer.LowerLimit` | mm | 0.40 | module_segment |
| UWS Web 2 Dancer Position Upper Limit ⚠ | `L01S_UWS_DB_HMI_connect.Web_2.Dancer.UpperLimit` | mm | 0.40 | module_segment |
| UWS Web 3 Dancer Position Lower Limit ⚠ | `L01S_UWS_DB_HMI_connect.Web_3.Dancer.LowerLimit` | mm | 0.40 | module_segment |
| UWS Web 3 Dancer Position Upper Limit ⚠ | `L01S_UWS_DB_HMI_connect.Web_3.Dancer.UpperLimit` | mm | 0.40 | module_segment |
| UWS Web 4 Dancer Position Lower Limit ⚠ | `L01S_UWS_DB_HMI_connect.Web_4.Dancer.LowerLimit` | mm | 0.40 | module_segment |
| UWS Web 4 Dancer Position Upper Limit ⚠ | `L01S_UWS_DB_HMI_connect.Web_4.Dancer.UpperLimit` | mm | 0.40 | module_segment |
| UWS Invert Direction Unwinder 1 | `L01S_UWS_DB_HMI_connect.Selections.InvDirUw_1` | - | 0.50 | module_segment |
| UWS Invert Direction Unwinder 2 | `L01S_UWS_DB_HMI_connect.Selections.InvDirUw_2` | - | 0.50 | module_segment |
| UWS Invert Direction Unwinder 3 | `L01S_UWS_DB_HMI_connect.Selections.InvDirUw_3` | - | 0.50 | module_segment |
| UWS Invert Direction Unwinder 4 | `L01S_UWS_DB_HMI_connect.Selections.InvDirUw_4` | - | 0.50 | module_segment |
| UWS Invert Direction Unwinder 5 | `L01S_UWS_DB_HMI_connect.Selections.InvDirUw_5` | - | 0.50 | module_segment |
| UWS Invert Direction Unwinder 6 | `L01S_UWS_DB_HMI_connect.Selections.InvDirUw_6` | - | 0.50 | module_segment |
| UWS Invert Direction Unwinder 7 | `L01S_UWS_DB_HMI_connect.Selections.InvDirUw_7` | - | 0.50 | module_segment |
| UWS Invert Direction Unwinder 8 | `L01S_UWS_DB_HMI_connect.Selections.InvDirUw_8` | - | 0.50 | module_segment |
| UWS Unwinding Enabled - Web 1 | `L01S_UWS_DB_setpoint.Selections.Enabled_Web_1` | - | 0.55 | module_segment |
| UWS Unwinding Enabled - Web 2 | `L01S_UWS_DB_setpoint.Selections.Enabled_Web_2` | - | 0.55 | module_segment |
| UWS Unwinding Enabled - Web 3 | `L01S_UWS_DB_setpoint.Selections.Enabled_Web_3` | - | 0.55 | module_segment |
| UWS Unwinding Enabled - Web 4 | `L01S_UWS_DB_setpoint.Selections.Enabled_Web_4` | - | 0.55 | module_segment |
| UWS Web 1 Unwinder Down Cycles After Film Finished (Setpoint) | `L01S_UWS_DB_setpoint.Web_1._Unwinder._Down.CyclesAfterFinished` | - | 0.55 | module_segment |
| UWS Web 1 Unwinder Top Cycles After Film Finished (Setpoint) | `L01S_UWS_DB_setpoint.Web_1._Unwinder._Top.CyclesAfterFinished` | - | 0.55 | module_segment |
| UWS Web 2 Unwinder Down Cycles After Film Finished (Setpoint) | `L01S_UWS_DB_setpoint.Web_2._Unwinder._Down.CyclesAfterFinished` | - | 0.55 | module_segment |
| UWS Web 2 Unwinder Top Cycles After Film Finished (Setpoint) | `L01S_UWS_DB_setpoint.Web_2._Unwinder._Top.CyclesAfterFinished` | - | 0.55 | module_segment |
| UWS Web 3 Unwinder Down Cycles After Film Finished (Setpoint) | `L01S_UWS_DB_setpoint.Web_3._Unwinder._Down.CyclesAfterFinished` | - | 0.55 | module_segment |
| UWS Web 3 Unwinder Top Cycles After Film Finished (Setpoint) | `L01S_UWS_DB_setpoint.Web_3._Unwinder._Top.CyclesAfterFinished` | - | 0.55 | module_segment |
| UWS Web 4 Unwinder Down Cycles After Film Finished (Setpoint) | `L01S_UWS_DB_setpoint.Web_4._Unwinder._Down.CyclesAfterFinished` | - | 0.55 | module_segment |
| UWS Web 4 Unwinder Top Cycles After Film Finished (Setpoint) | `L01S_UWS_DB_setpoint.Web_4._Unwinder._Top.CyclesAfterFinished` | - | 0.55 | module_segment |
| UWS Cycle Time (T01) | `L01S_UWS_DB_HMI_connect.HMIActualTimes.T01` | ms | 0.55 | module_segment |
| UWS Web 1 Unwinder Down Cycles After Film Finished (Actual) | `L01S_UWS_DB_HMI_connect.Web_1.Unwinder.Down.CyclesAfter` | - | 0.55 | module_segment |
| UWS Web 1 Unwinder Top Cycles After Film Finished (Actual) | `L01S_UWS_DB_HMI_connect.Web_1.Unwinder.Top.CyclesAfter` | - | 0.55 | module_segment |
| UWS Web 2 Unwinder Down Cycles After Film Finished (Actual) | `L01S_UWS_DB_HMI_connect.Web_2.Unwinder.Down.CyclesAfter` | - | 0.55 | module_segment |
| UWS Web 2 Unwinder Top Cycles After Film Finished (Actual) | `L01S_UWS_DB_HMI_connect.Web_2.Unwinder.Top.CyclesAfter` | - | 0.55 | module_segment |
| UWS Web 3 Unwinder Down Cycles After Film Finished (Actual) | `L01S_UWS_DB_HMI_connect.Web_3.Unwinder.Down.CyclesAfter` | - | 0.55 | module_segment |
| UWS Web 3 Unwinder Top Cycles After Film Finished (Actual) | `L01S_UWS_DB_HMI_connect.Web_3.Unwinder.Top.CyclesAfter` | - | 0.55 | module_segment |
| UWS Web 4 Unwinder Down Cycles After Film Finished (Actual) | `L01S_UWS_DB_HMI_connect.Web_4.Unwinder.Down.CyclesAfter` | - | 0.55 | module_segment |
| UWS Web 4 Unwinder Top Cycles After Film Finished (Actual) | `L01S_UWS_DB_HMI_connect.Web_4.Unwinder.Top.CyclesAfter` | - | 0.55 | module_segment |
| UWS Fife Web 1 Offset Position | `L01_INS_DB_setpoint.Adjust_UWS_Fife_Web_1.Offset_Pos` | mm | 0.70 | module_segment |
| UWS Fife Web 1 Target Position | `L01_INS_DB_setpoint.Adjust_UWS_Fife_Web_1.Target_Pos` | mm | 0.70 | module_segment |
| UWS Fife Web 2 Offset Position | `L01_INS_DB_setpoint.Adjust_UWS_Fife_Web_2.Offset_Pos` | mm | 0.70 | module_segment |
| UWS Fife Web 2 Target Position | `L01_INS_DB_setpoint.Adjust_UWS_Fife_Web_2.Target_Pos` | mm | 0.70 | module_segment |
| UWS Fife Web 1 Actual Position | `L01_INS_DB_HMI_connect.Adjust_UWS_Fife_Web_1.ActPos` | mm | 0.70 | module_segment |
| UWS Fife Web 2 Actual Position | `L01_INS_DB_HMI_connect.Adjust_UWS_Fife_Web_2.ActPos` | mm | 0.70 | module_segment |
| UWS Web 1 Dancer Release Foil Feed Window | `L01S_UWS_DB_setpoint.Web_1._Dancer.ReleaseWindow` | ° | 0.70 | module_segment |
| UWS Web 1 Unwinder Down Start Speed Factor | `L01S_UWS_DB_setpoint.Web_1._Unwinder._Down.StartVelocity` | % | 0.70 | module_segment |
| UWS Web 1 Unwinder Top Start Speed Factor | `L01S_UWS_DB_setpoint.Web_1._Unwinder._Top.StartVelocity` | % | 0.70 | module_segment |
| UWS Web 2 Dancer Release Foil Feed Window | `L01S_UWS_DB_setpoint.Web_2._Dancer.ReleaseWindow` | ° | 0.70 | module_segment |
| UWS Web 2 Unwinder Down Start Speed Factor | `L01S_UWS_DB_setpoint.Web_2._Unwinder._Down.StartVelocity` | % | 0.70 | module_segment |
| UWS Web 2 Unwinder Top Start Speed Factor | `L01S_UWS_DB_setpoint.Web_2._Unwinder._Top.StartVelocity` | % | 0.70 | module_segment |
| UWS Web 3 Dancer Release Foil Feed Window | `L01S_UWS_DB_setpoint.Web_3._Dancer.ReleaseWindow` | ° | 0.70 | module_segment |
| UWS Web 3 Unwinder Down Start Speed Factor | `L01S_UWS_DB_setpoint.Web_3._Unwinder._Down.StartVelocity` | % | 0.70 | module_segment |
| UWS Web 3 Unwinder Top Start Speed Factor | `L01S_UWS_DB_setpoint.Web_3._Unwinder._Top.StartVelocity` | % | 0.70 | module_segment |
| UWS Web 4 Dancer Release Foil Feed Window | `L01S_UWS_DB_setpoint.Web_4._Dancer.ReleaseWindow` | ° | 0.70 | module_segment |
| UWS Web 4 Unwinder Down Start Speed Factor | `L01S_UWS_DB_setpoint.Web_4._Unwinder._Down.StartVelocity` | % | 0.70 | module_segment |
| UWS Web 4 Unwinder Top Start Speed Factor | `L01S_UWS_DB_setpoint.Web_4._Unwinder._Top.StartVelocity` | % | 0.70 | module_segment |
| UWS AdjustFife 1 Actual Position | `L01S_UWS_DB_HMI_connect.AdjustFife_1.ActPos` | mm | 0.70 | module_segment |
| UWS AdjustFife 2 Actual Position | `L01S_UWS_DB_HMI_connect.AdjustFife_2.ActPos` | mm | 0.70 | module_segment |
| UWS Web 1 Dancer Control Target Position | `L01S_UWS_DB_setpoint.Web_1._Dancer._Control.Position` | ° | 0.75 | module_segment |
| UWS Web 1 Dancer Empty Target Position | `L01S_UWS_DB_setpoint.Web_1._Dancer._Empty.Position` | ° | 0.75 | module_segment |
| UWS Web 1 Dancer Stop Acceleration | `L01S_UWS_DB_setpoint.Web_1._Dancer._Stop.Acc` | % | 0.75 | module_segment |
| UWS Web 1 Dancer Stop Deceleration | `L01S_UWS_DB_setpoint.Web_1._Dancer._Stop.Dec` | % | 0.75 | module_segment |
| UWS Web 1 Dancer Stop Target Position | `L01S_UWS_DB_setpoint.Web_1._Dancer._Stop.Position` | ° | 0.75 | module_segment |
| UWS Web 1 Dancer Stop Velocity | `L01S_UWS_DB_setpoint.Web_1._Dancer._Stop.Velocity` | % | 0.75 | module_segment |
| UWS Web 2 Dancer Control Target Position | `L01S_UWS_DB_setpoint.Web_2._Dancer._Control.Position` | ° | 0.75 | module_segment |
| UWS Web 2 Dancer Empty Target Position | `L01S_UWS_DB_setpoint.Web_2._Dancer._Empty.Position` | ° | 0.75 | module_segment |
| UWS Web 2 Dancer Stop Acceleration | `L01S_UWS_DB_setpoint.Web_2._Dancer._Stop.Acc` | % | 0.75 | module_segment |
| UWS Web 2 Dancer Stop Deceleration | `L01S_UWS_DB_setpoint.Web_2._Dancer._Stop.Dec` | % | 0.75 | module_segment |
| UWS Web 2 Dancer Stop Target Position | `L01S_UWS_DB_setpoint.Web_2._Dancer._Stop.Position` | ° | 0.75 | module_segment |
| UWS Web 2 Dancer Stop Velocity | `L01S_UWS_DB_setpoint.Web_2._Dancer._Stop.Velocity` | % | 0.75 | module_segment |
| UWS Web 3 Dancer Control Target Position | `L01S_UWS_DB_setpoint.Web_3._Dancer._Control.Position` | ° | 0.75 | module_segment |
| UWS Web 3 Dancer Empty Target Position | `L01S_UWS_DB_setpoint.Web_3._Dancer._Empty.Position` | ° | 0.75 | module_segment |
| UWS Web 3 Dancer Stop Acceleration | `L01S_UWS_DB_setpoint.Web_3._Dancer._Stop.Acc` | % | 0.75 | module_segment |
| UWS Web 3 Dancer Stop Deceleration | `L01S_UWS_DB_setpoint.Web_3._Dancer._Stop.Dec` | % | 0.75 | module_segment |
| UWS Web 3 Dancer Stop Target Position | `L01S_UWS_DB_setpoint.Web_3._Dancer._Stop.Position` | ° | 0.75 | module_segment |
| UWS Web 3 Dancer Stop Velocity | `L01S_UWS_DB_setpoint.Web_3._Dancer._Stop.Velocity` | % | 0.75 | module_segment |
| UWS Web 4 Dancer Control Target Position | `L01S_UWS_DB_setpoint.Web_4._Dancer._Control.Position` | ° | 0.75 | module_segment |
| UWS Web 4 Dancer Empty Target Position | `L01S_UWS_DB_setpoint.Web_4._Dancer._Empty.Position` | ° | 0.75 | module_segment |
| UWS Web 4 Dancer Stop Acceleration | `L01S_UWS_DB_setpoint.Web_4._Dancer._Stop.Acc` | % | 0.75 | module_segment |
| UWS Web 4 Dancer Stop Deceleration | `L01S_UWS_DB_setpoint.Web_4._Dancer._Stop.Dec` | % | 0.75 | module_segment |
| UWS Web 4 Dancer Stop Target Position | `L01S_UWS_DB_setpoint.Web_4._Dancer._Stop.Position` | ° | 0.75 | module_segment |
| UWS Web 4 Dancer Stop Velocity | `L01S_UWS_DB_setpoint.Web_4._Dancer._Stop.Velocity` | % | 0.75 | module_segment |
| UWS Web 1 Unwinder Down Actual Velocity | `L01S_UWS_DB_HMI_connect.Web_1.Unwinder.Down.ActVelocity` | % | 0.75 | module_segment |
| UWS Web 1 Unwinder Top Actual Velocity | `L01S_UWS_DB_HMI_connect.Web_1.Unwinder.Top.ActVelocity` | % | 0.75 | module_segment |
| UWS Web 2 Unwinder Down Actual Velocity | `L01S_UWS_DB_HMI_connect.Web_2.Unwinder.Down.ActVelocity` | % | 0.75 | module_segment |
| UWS Web 2 Unwinder Top Actual Velocity | `L01S_UWS_DB_HMI_connect.Web_2.Unwinder.Top.ActVelocity` | % | 0.75 | module_segment |
| UWS Web 3 Unwinder Down Actual Velocity | `L01S_UWS_DB_HMI_connect.Web_3.Unwinder.Down.ActVelocity` | % | 0.75 | module_segment |
| UWS Web 3 Unwinder Top Actual Velocity | `L01S_UWS_DB_HMI_connect.Web_3.Unwinder.Top.ActVelocity` | % | 0.75 | module_segment |
| UWS Web 4 Unwinder Down Actual Velocity | `L01S_UWS_DB_HMI_connect.Web_4.Unwinder.Down.ActVelocity` | % | 0.75 | module_segment |
| UWS Web 4 Unwinder Top Actual Velocity | `L01S_UWS_DB_HMI_connect.Web_4.Unwinder.Top.ActVelocity` | % | 0.75 | module_segment |
| UWS Web 1 Dancer Force Setpoint | `L01S_UWS_DB_setpoint.Web_1._Dancer.Force` | kg | 0.80 | module_segment |
| UWS Web 2 Dancer Force Setpoint | `L01S_UWS_DB_setpoint.Web_2._Dancer.Force` | kg | 0.80 | module_segment |
| UWS Web 3 Dancer Force Setpoint | `L01S_UWS_DB_setpoint.Web_3._Dancer.Force` | kg | 0.80 | module_segment |
| UWS Web 4 Dancer Force Setpoint | `L01S_UWS_DB_setpoint.Web_4._Dancer.Force` | kg | 0.80 | module_segment |
| UWS Web 1 Dancer Actual Force | `L01S_UWS_DB_HMI_connect.Web_1.Dancer.ActForce` | kg | 0.80 | module_segment |
| UWS Web 1 Dancer Actual Position | `L01S_UWS_DB_HMI_connect.Web_1.Dancer.ActPos` | mm | 0.80 | module_segment |
| UWS Web 2 Dancer Actual Force | `L01S_UWS_DB_HMI_connect.Web_2.Dancer.ActForce` | kg | 0.80 | module_segment |
| UWS Web 2 Dancer Actual Position | `L01S_UWS_DB_HMI_connect.Web_2.Dancer.ActPos` | mm | 0.80 | module_segment |
| UWS Web 3 Dancer Actual Force | `L01S_UWS_DB_HMI_connect.Web_3.Dancer.ActForce` | kg | 0.80 | module_segment |
| UWS Web 3 Dancer Actual Position | `L01S_UWS_DB_HMI_connect.Web_3.Dancer.ActPos` | mm | 0.80 | module_segment |
| UWS Web 4 Dancer Actual Force | `L01S_UWS_DB_HMI_connect.Web_4.Dancer.ActForce` | kg | 0.80 | module_segment |
| UWS Web 4 Dancer Actual Position | `L01S_UWS_DB_HMI_connect.Web_4.Dancer.ActPos` | mm | 0.80 | module_segment |

### FPW filter welding station (MC007-FPW)

- 625 candidate tag(s) considered -> 190 kept as genuine parameters (30%).
- Kept tags found by: 190 via *module_segment* (the tag name contains this station's own PLC/module code as a literal segment - the strongest signal available).
- 47 kept parameter(s) below 0.5 confidence - flagged with ⚠ below.

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| FPW Left Filter Register Invert Position Setpoint ⚠ | `L01S_FPWL_DB_HMI_connect.FilterRegister.CMD.InvertPosition` | - | 0.35 | module_segment |
| FPW Right Filter Register Invert Position Setpoint ⚠ | `L01S_FPWR_DB_HMI_connect.FilterRegister.CMD.InvertPosition` | - | 0.35 | module_segment |
| FPW Left LinMot1 Home Offset ⚠ | `L01S_FPWL_IDB_LinMot1.HomeOffset` | - | 0.35 | module_segment |
| FPW Left LinMot2 Home Offset ⚠ | `L01S_FPWL_IDB_LinMot2.HomeOffset` | - | 0.35 | module_segment |
| FPW Right LinMot1 Home Offset ⚠ | `L01S_FPWR_IDB_LinMot1.HomeOffset` | - | 0.35 | module_segment |
| FPW Right LinMot2 Home Offset ⚠ | `L01S_FPWR_IDB_LinMot2.HomeOffset` | - | 0.35 | module_segment |
| FPW Left Heater Y-Scaling Groundpoint Boundary ⚠ | `L01S_FPWL_DB_setpoint.Heater.Y_Scaling_groundpoint` | - | 0.40 | module_segment |
| FPW Left Heater Y-Scaling Toppoint Boundary ⚠ | `L01S_FPWL_DB_setpoint.Heater.Y_Scaling_toppoint` | - | 0.40 | module_segment |
| FPW Right Heater Y-Scaling Groundpoint Boundary ⚠ | `L01S_FPWR_DB_setpoint.Heater.Y_Scaling_groundpoint` | - | 0.40 | module_segment |
| FPW Right Heater Y-Scaling Toppoint Boundary ⚠ | `L01S_FPWR_DB_setpoint.Heater.Y_Scaling_toppoint` | - | 0.40 | module_segment |
| FPW Left Heater1 Self-Tuning Excitation Delta ⚠ | `L01S_FPWL_DB_HMI_connect.Heater1.Control.TUN_DLMN` | % | 0.40 | module_segment |
| FPW Right Heater1 Self-Tuning Excitation Delta ⚠ | `L01S_FPWR_DB_HMI_connect.Heater1.Control.TUN_DLMN` | % | 0.40 | module_segment |
| FPW Left FP03: All Clamps Open ⚠ | `L01S_FPWL_DB_HMI_connect.Selections.FP_03` | - | 0.40 | module_segment |
| FPW Right FP03: All Clamps Open ⚠ | `L01S_FPWR_DB_HMI_connect.Selections.FP_03` | - | 0.40 | module_segment |
| FPW Left Filter Transport Pos1 Acceleration ⚠ | `L01S_FPWL_DB_setpoint.FilterTransport._Pos1.Acc` | - | 0.45 | module_segment |
| FPW Left Filter Transport Pos1 Deceleration ⚠ | `L01S_FPWL_DB_setpoint.FilterTransport._Pos1.Dec` | - | 0.45 | module_segment |
| FPW Left Filter Transport Pos1 Velocity ⚠ | `L01S_FPWL_DB_setpoint.FilterTransport._Pos1.Velocity` | - | 0.45 | module_segment |
| FPW Right Filter Transport Pos1 Acceleration ⚠ | `L01S_FPWR_DB_setpoint.FilterTransport._Pos1.Acc` | - | 0.45 | module_segment |
| FPW Right Filter Transport Pos1 Deceleration ⚠ | `L01S_FPWR_DB_setpoint.FilterTransport._Pos1.Dec` | - | 0.45 | module_segment |
| FPW Right Filter Transport Pos1 Position ⚠ | `L01S_FPWR_DB_setpoint.FilterTransport._Pos1.Position` | - | 0.45 | module_segment |
| FPW Right Filter Transport Pos1 Velocity ⚠ | `L01S_FPWR_DB_setpoint.FilterTransport._Pos1.Velocity` | - | 0.45 | module_segment |
| FPW Left Inspection Job Number (Setpoint) ⚠ | `L01S_FPWL_DB_setpoint.Inspection.JobNr` | - | 0.45 | module_segment |
| FPW Right Inspection Job Number (Setpoint) ⚠ | `L01S_FPWR_DB_setpoint.Inspection.JobNr` | - | 0.45 | module_segment |
| FPW Left Revolver Pos1 Acceleration ⚠ | `L01S_FPWL_DB_setpoint.Revolver._Pos1.Acc` | - | 0.45 | module_segment |
| FPW Left Revolver Pos1 Deceleration ⚠ | `L01S_FPWL_DB_setpoint.Revolver._Pos1.Dec` | - | 0.45 | module_segment |
| FPW Left Revolver Pos1 Velocity ⚠ | `L01S_FPWL_DB_setpoint.Revolver._Pos1.Velocity` | - | 0.45 | module_segment |
| FPW Right Revolver Pos1 Acceleration ⚠ | `L01S_FPWR_DB_setpoint.Revolver._Pos1.Acc` | - | 0.45 | module_segment |
| FPW Right Revolver Pos1 Deceleration ⚠ | `L01S_FPWR_DB_setpoint.Revolver._Pos1.Dec` | - | 0.45 | module_segment |
| FPW Right Revolver Pos1 Position ⚠ | `L01S_FPWR_DB_setpoint.Revolver._Pos1.Position` | - | 0.45 | module_segment |
| FPW Right Revolver Pos1 Velocity ⚠ | `L01S_FPWR_DB_setpoint.Revolver._Pos1.Velocity` | - | 0.45 | module_segment |
| FPW Right Revolver Pos2 Position ⚠ | `L01S_FPWR_DB_setpoint.Revolver._Pos2.Position` | - | 0.45 | module_segment |
| FPW Left Filter Register Position - Electrical Check ⚠ | `L01S_FPWL_DB_HMI_connect.FilterRegister.Set.PosCheckElectrical` | - | 0.45 | module_segment |
| FPW Left Filter Register Position - Mechanical Check ⚠ | `L01S_FPWL_DB_HMI_connect.FilterRegister.Set.PosCheckMechanical` | - | 0.45 | module_segment |
| FPW Left Filter Register Position - Punch ⚠ | `L01S_FPWL_DB_HMI_connect.FilterRegister.Set.PosPunch` | - | 0.45 | module_segment |
| FPW Right Filter Register Position - Electrical Check ⚠ | `L01S_FPWR_DB_HMI_connect.FilterRegister.Set.PosCheckElectrical` | - | 0.45 | module_segment |
| FPW Right Filter Register Position - Mechanical Check ⚠ | `L01S_FPWR_DB_HMI_connect.FilterRegister.Set.PosCheckMechanical` | - | 0.45 | module_segment |
| FPW Right Filter Register Position - Punch ⚠ | `L01S_FPWR_DB_HMI_connect.FilterRegister.Set.PosPunch` | - | 0.45 | module_segment |
| FPW Left Inspection Job Number (Actual) ⚠ | `L01S_FPWL_DB_HMI_connect.Inspection.JobNr` | - | 0.45 | module_segment |
| FPW Right Inspection Job Number (Actual) ⚠ | `L01S_FPWR_DB_HMI_connect.Inspection.JobNr` | - | 0.45 | module_segment |
| FPW Left Revolver Actual Position ⚠ | `L01S_FPWL_DB_HMI_connect.Revolver.ActPos` | - | 0.45 | module_segment |
| FPW Left Revolver Reference Offset ⚠ | `L01S_FPWL_DB_HMI_connect.Revolver.ReferenceOffset` | - | 0.45 | module_segment |
| FPW Right Revolver Actual Position ⚠ | `L01S_FPWR_DB_HMI_connect.Revolver.ActPos` | - | 0.45 | module_segment |
| FPW Right Revolver Reference Offset ⚠ | `L01S_FPWR_DB_HMI_connect.Revolver.ReferenceOffset` | - | 0.45 | module_segment |
| FPW Left FP02: Inspection Enabled ⚠ | `L01S_FPWL_DB_HMI_connect.Selections.FP_02` | - | 0.45 | module_segment |
| FPW Left FP01: Operation Mode Semi-Automatic ⚠ | `L01S_FPWL_DB_HMI_connect.Selections.SemiAuto` | - | 0.45 | module_segment |
| FPW Right FP02: Inspection Enabled ⚠ | `L01S_FPWR_DB_HMI_connect.Selections.FP_02` | - | 0.45 | module_segment |
| FPW Right FP01: Operation Mode Semi-Automatic ⚠ | `L01S_FPWR_DB_HMI_connect.Selections.SemiAuto` | - | 0.45 | module_segment |
| Gap 23: FPWL Inspection to FPWL Station Welding (Web2) | `GE1_DB_setpoint.StationGaps.FPWL_Insp_FPWL_StWe` | mm | 0.50 | module_segment |
| Gap 28: FPWL Station Hole Punch to PRIH Tack Seal (Web12) | `GE1_DB_setpoint.StationGaps.FPWL_StHp_PRIH_Ts` | mm | 0.50 | module_segment |
| Gap 24: FPWL Station Welding to FPWL Station Hole Punch (Web2) | `GE1_DB_setpoint.StationGaps.FPWL_StWe_FPWL_StHp` | mm | 0.50 | module_segment |
| Gap 20: FPWR Inspection to FPWR Station Welding (Web2) | `GE1_DB_setpoint.StationGaps.FPWR_Insp_FPWR_StWe` | mm | 0.50 | module_segment |
| Gap 22: FPWR Station Hole Punch to FPWL Inspection (Web2) | `GE1_DB_setpoint.StationGaps.FPWR_StHp_FPWL_Insp` | mm | 0.50 | module_segment |
| Gap 21: FPWR Station Welding to FPWR Station Hole Punch (Web2) | `GE1_DB_setpoint.StationGaps.FPWR_StWe_FPWR_StHp` | mm | 0.50 | module_segment |
| FPW Left FP01: Station Enabled | `L01S_FPWL_DB_setpoint.Selections.StationEnabled` | - | 0.50 | module_segment |
| FPW Right FP01: Station Enabled | `L01S_FPWR_DB_setpoint.Selections.StationEnabled` | - | 0.50 | module_segment |
| FPW Right FP02: Heater Enabled | `L01S_FPWR_DB_setpoint.Selections.HeaterEnabled` | - | 0.50 | module_segment |
| FPW Left Filter Transport Actual Position | `L01S_FPWL_DB_HMI_connect.FilterTransport.ActPos` | mm | 0.50 | module_segment |
| FPW Left Filter Transport Position Offset | `L01S_FPWL_DB_HMI_connect.FilterTransport.PositionOffset` | mm | 0.50 | module_segment |
| FPW Left Filter Transport Target Position | `L01S_FPWL_DB_HMI_connect.FilterTransport.TargetPos` | mm | 0.50 | module_segment |
| FPW Right Filter Transport Actual Position | `L01S_FPWR_DB_HMI_connect.FilterTransport.ActPos` | mm | 0.50 | module_segment |
| FPW Right Filter Transport Position Offset | `L01S_FPWR_DB_HMI_connect.FilterTransport.PositionOffset` | mm | 0.50 | module_segment |
| FPW Right Filter Transport Target Position | `L01S_FPWR_DB_HMI_connect.FilterTransport.TargetPos` | mm | 0.50 | module_segment |
| FPW Left Heater1 PID Proportional Gain | `L01S_FPWL_DB_HMI_connect.Heater1.Control.GAIN` | - | 0.50 | module_segment |
| FPW Left Heater1 Manipulated Variable High Limit | `L01S_FPWL_DB_HMI_connect.Heater1.Control.LMN_HLM` | % | 0.50 | module_segment |
| FPW Left Heater1 Manipulated Variable Low Limit | `L01S_FPWL_DB_HMI_connect.Heater1.Control.LMN_LLM` | % | 0.50 | module_segment |
| FPW Left Heater1 Manual Output Value | `L01S_FPWL_DB_HMI_connect.Heater1.Control.MAN` | % | 0.50 | module_segment |
| FPW Left Heater1 Manual-Switch Temperature Deviation | `L01S_FPWL_DB_HMI_connect.Heater1.Control.MAN_ON_VALUE` | °C | 0.50 | module_segment |
| FPW Left Heater1 PID Derivative Time | `L01S_FPWL_DB_HMI_connect.Heater1.Control.TD` | s | 0.50 | module_segment |
| FPW Left Heater1 PID Integration Time | `L01S_FPWL_DB_HMI_connect.Heater1.Control.TI` | s | 0.50 | module_segment |
| FPW Right Heater1 PID Proportional Gain | `L01S_FPWR_DB_HMI_connect.Heater1.Control.GAIN` | - | 0.50 | module_segment |
| FPW Right Heater1 Manipulated Variable High Limit | `L01S_FPWR_DB_HMI_connect.Heater1.Control.LMN_HLM` | % | 0.50 | module_segment |
| FPW Right Heater1 Manipulated Variable Low Limit | `L01S_FPWR_DB_HMI_connect.Heater1.Control.LMN_LLM` | % | 0.50 | module_segment |
| FPW Right Heater1 Manual Output Value | `L01S_FPWR_DB_HMI_connect.Heater1.Control.MAN` | % | 0.50 | module_segment |
| FPW Right Heater1 Manual-Switch Temperature Deviation | `L01S_FPWR_DB_HMI_connect.Heater1.Control.MAN_ON_VALUE` | °C | 0.50 | module_segment |
| FPW Right Heater1 PID Derivative Time | `L01S_FPWR_DB_HMI_connect.Heater1.Control.TD` | s | 0.50 | module_segment |
| FPW Right Heater1 PID Integration Time | `L01S_FPWR_DB_HMI_connect.Heater1.Control.TI` | s | 0.50 | module_segment |
| FPW Left LinMot1 Target Position (Status) | `L01S_FPWL_DB_HMI_connect.LinMot1.Status.Target_Pos` | mm | 0.50 | module_segment |
| FPW Right LinMot1 Target Position (Status) | `L01S_FPWR_DB_HMI_connect.LinMot1.Status.Target_Pos` | mm | 0.50 | module_segment |
| FPW Left Heater Controller Proportional Gain (Raw) | `L01S_FPWL_IDB_Heater.DI_TCONT_CP.GAIN` | - | 0.50 | module_segment |
| FPW Left Heater Controller Derivative Time (Raw) | `L01S_FPWL_IDB_Heater.DI_TCONT_CP.TD` | s | 0.50 | module_segment |
| FPW Left Heater Controller Reset (Integral) Time (Raw) | `L01S_FPWL_IDB_Heater.DI_TCONT_CP.TI` | s | 0.50 | module_segment |
| FPW Right Heater Controller Proportional Gain (Raw) | `L01S_FPWR_IDB_Heater.DI_TCONT_CP.GAIN` | - | 0.50 | module_segment |
| FPW Right Heater Controller Derivative Time (Raw) | `L01S_FPWR_IDB_Heater.DI_TCONT_CP.TD` | s | 0.50 | module_segment |
| FPW Right Heater Controller Reset (Integral) Time (Raw) | `L01S_FPWR_IDB_Heater.DI_TCONT_CP.TI` | s | 0.50 | module_segment |
| FPW Left Filter Coil Counter To End | `L01S_FPWL_DB_setpoint.FilterCoil.CounterToEnd` | - | 0.55 | module_segment |
| FPW Right Filter Coil Counter To End | `L01S_FPWR_DB_setpoint.FilterCoil.CounterToEnd` | - | 0.55 | module_segment |
| FPW Left Filter Register Coil Counter at End (Actual) | `L01S_FPWL_DB_HMI_connect.FilterRegister.States.CoilCounter` | - | 0.55 | module_segment |
| FPW Right Filter Register Coil Counter at End (Actual) | `L01S_FPWR_DB_HMI_connect.FilterRegister.States.CoilCounter` | - | 0.55 | module_segment |
| FPW Left Cycle Time (Actual, T01) | `L01S_FPWL_DB_HMI_connect.HMIActualTimes.T01` | ms | 0.55 | module_segment |
| FPW Right Cycle Time (Actual, T01) | `L01S_FPWR_DB_HMI_connect.HMIActualTimes.T01` | ms | 0.55 | module_segment |
| FPW Heat Tolerance (Recipe) | `MASTER_RECIPE_GENERAL.FPW_HEAT_TOL` | °C | 0.55 | module_segment |
| FPW Left Cooling Plate Temperature | `GE1_DB_interface.FPWL_COMMUNICATION._FROM.TempCoolingPlate` | °C | 0.60 | module_segment |
| FPW Right Filter Transport Override Velocity | `L01S_FPWR_DB_setpoint.FilterTransport.OVR_Velocity` | % | 0.60 | module_segment |
| FPW Left Heater Correction Value | `L01S_FPWL_DB_setpoint.Heater.Correction_Value` | °K | 0.60 | module_segment |
| FPW Right Heater Correction Value | `L01S_FPWR_DB_setpoint.Heater.Correction_Value` | °K | 0.60 | module_segment |
| FPW Right Revolver Override Velocity | `L01S_FPWR_DB_setpoint.Revolver.OVR_Velocity` | % | 0.60 | module_segment |
| FPW Left Cycle Counter | `L01S_FPWL_DB_HMI_connect.Count.CycleCounter` | - | 0.60 | module_segment |
| FPW Right Cycle Counter | `L01S_FPWR_DB_HMI_connect.Count.CycleCounter` | - | 0.60 | module_segment |
| FPW Left Heater1 PID Output | `L01S_FPWL_DB_HMI_connect.Heater1.Status.LMN` | % | 0.60 | module_segment |
| FPW Right Heater1 PID Output | `L01S_FPWR_DB_HMI_connect.Heater1.Status.LMN` | % | 0.60 | module_segment |
| FPW Heat Alarm High (Recipe) | `MASTER_RECIPE_GENERAL.FPW_HEAT_ALARM_HIGH` | °C | 0.60 | module_segment |
| FPW Heat Alarm Low (Recipe) | `MASTER_RECIPE_GENERAL.FPW_HEAT_ALARM_LOW` | °C | 0.60 | module_segment |
| FPW Seal Time (Recipe) | `MASTER_RECIPE_GENERAL.FPW_SEAL_TIME` | ms | 0.60 | module_segment |
| FPW Left T01: Cycle Time Setpoint | `L01S_FPWL_DB_setpoint.Times.CycleTime` | ms | 0.65 | module_segment |
| FPW Right T01: Cycle Time Setpoint | `L01S_FPWR_DB_setpoint.Times.CycleTime` | ms | 0.65 | module_segment |
| FPW Left X1-Adjust Offset Position | `L01S_FPWL_DB_setpoint.Adujst_X1.Offset_Pos` | mm | 0.70 | module_segment |
| FPW Left X1-Adjust Target Position | `L01S_FPWL_DB_setpoint.Adujst_X1.Target_Pos` | mm | 0.70 | module_segment |
| FPW Left X2-Adjust Offset Position | `L01S_FPWL_DB_setpoint.Adujst_X2.Offset_Pos` | mm | 0.70 | module_segment |
| FPW Left X2-Adjust Target Position | `L01S_FPWL_DB_setpoint.Adujst_X2.Target_Pos` | mm | 0.70 | module_segment |
| FPW Left X3-Adjust Offset Position | `L01S_FPWL_DB_setpoint.Adujst_X3.Offset_Pos` | mm | 0.70 | module_segment |
| FPW Left X3-Adjust Target Position | `L01S_FPWL_DB_setpoint.Adujst_X3.Target_Pos` | mm | 0.70 | module_segment |
| FPW Left Y1-Adjust Offset Position | `L01S_FPWL_DB_setpoint.Adujst_Y1.Offset_Pos` | mm | 0.70 | module_segment |
| FPW Left Y1-Adjust Target Position | `L01S_FPWL_DB_setpoint.Adujst_Y1.Target_Pos` | mm | 0.70 | module_segment |
| FPW Left Y2-Adjust Offset Position | `L01S_FPWL_DB_setpoint.Adujst_Y2.Offset_Pos` | mm | 0.70 | module_segment |
| FPW Left Y2-Adjust Target Position | `L01S_FPWL_DB_setpoint.Adujst_Y2.Target_Pos` | mm | 0.70 | module_segment |
| FPW Right X1-Adjust Offset Position | `L01S_FPWR_DB_setpoint.Adujst_X1.Offset_Pos` | mm | 0.70 | module_segment |
| FPW Right X1-Adjust Target Position | `L01S_FPWR_DB_setpoint.Adujst_X1.Target_Pos` | mm | 0.70 | module_segment |
| FPW Right X2-Adjust Offset Position | `L01S_FPWR_DB_setpoint.Adujst_X2.Offset_Pos` | mm | 0.70 | module_segment |
| FPW Right X2-Adjust Target Position | `L01S_FPWR_DB_setpoint.Adujst_X2.Target_Pos` | mm | 0.70 | module_segment |
| FPW Right X3-Adjust Offset Position | `L01S_FPWR_DB_setpoint.Adujst_X3.Offset_Pos` | mm | 0.70 | module_segment |
| FPW Right X3-Adjust Target Position | `L01S_FPWR_DB_setpoint.Adujst_X3.Target_Pos` | mm | 0.70 | module_segment |
| FPW Right Y1-Adjust Offset Position | `L01S_FPWR_DB_setpoint.Adujst_Y1.Offset_Pos` | mm | 0.70 | module_segment |
| FPW Right Y1-Adjust Target Position | `L01S_FPWR_DB_setpoint.Adujst_Y1.Target_Pos` | mm | 0.70 | module_segment |
| FPW Right Y2-Adjust Offset Position | `L01S_FPWR_DB_setpoint.Adujst_Y2.Offset_Pos` | mm | 0.70 | module_segment |
| FPW Right Y2-Adjust Target Position | `L01S_FPWR_DB_setpoint.Adujst_Y2.Target_Pos` | mm | 0.70 | module_segment |
| FPW Left Heater Lower Alarm Boundary | `L01S_FPWL_DB_setpoint.Heater.Alarm_Boundary_Down` | °C | 0.70 | module_segment |
| FPW Left Heater Upper Alarm Boundary | `L01S_FPWL_DB_setpoint.Heater.Alarm_Boundary_Up` | °C | 0.70 | module_segment |
| FPW Right Heater Lower Alarm Boundary | `L01S_FPWR_DB_setpoint.Heater.Alarm_Boundary_Down` | °C | 0.70 | module_segment |
| FPW Right Heater Upper Alarm Boundary | `L01S_FPWR_DB_setpoint.Heater.Alarm_Boundary_Up` | °C | 0.70 | module_segment |
| FPW Left LinMot1 Pos1 Acceleration | `L01S_FPWL_DB_setpoint.LinMot1_Positions.Pos1.Acceleration` | m/s^2 | 0.70 | module_segment |
| FPW Left LinMot1 Pos1 Deceleration | `L01S_FPWL_DB_setpoint.LinMot1_Positions.Pos1.Deceleration` | m/s^2 | 0.70 | module_segment |
| FPW Left LinMot1 Pos1 Max Velocity | `L01S_FPWL_DB_setpoint.LinMot1_Positions.Pos1.Velocity` | m/s | 0.70 | module_segment |
| FPW Left LinMot2 Pos1 Acceleration | `L01S_FPWL_DB_setpoint.LinMot2_Positions.Pos1.Acceleration` | m/s^2 | 0.70 | module_segment |
| FPW Left LinMot2 Pos1 Deceleration | `L01S_FPWL_DB_setpoint.LinMot2_Positions.Pos1.Deceleration` | m/s^2 | 0.70 | module_segment |
| FPW Left LinMot2 Pos1 Max Velocity | `L01S_FPWL_DB_setpoint.LinMot2_Positions.Pos1.Velocity` | m/s | 0.70 | module_segment |
| FPW Right LinMot1 Pos1 Acceleration | `L01S_FPWR_DB_setpoint.LinMot1_Positions.Pos1.Acceleration` | m/s^2 | 0.70 | module_segment |
| FPW Right LinMot1 Pos1 Deceleration | `L01S_FPWR_DB_setpoint.LinMot1_Positions.Pos1.Deceleration` | m/s^2 | 0.70 | module_segment |
| FPW Right LinMot1 Pos1 Max Velocity | `L01S_FPWR_DB_setpoint.LinMot1_Positions.Pos1.Velocity` | m/s | 0.70 | module_segment |
| FPW Right LinMot2 Pos1 Acceleration | `L01S_FPWR_DB_setpoint.LinMot2_Positions.Pos1.Acceleration` | m/s^2 | 0.70 | module_segment |
| FPW Right LinMot2 Pos1 Deceleration | `L01S_FPWR_DB_setpoint.LinMot2_Positions.Pos1.Deceleration` | m/s^2 | 0.70 | module_segment |
| FPW Right LinMot2 Pos1 Max Velocity | `L01S_FPWR_DB_setpoint.LinMot2_Positions.Pos1.Velocity` | m/s | 0.70 | module_segment |
| FPW Left T03: Waste Removal Time | `L01S_FPWL_DB_setpoint.Times._03` | ms | 0.70 | module_segment |
| FPW Left T04: Filter Punching Time | `L01S_FPWL_DB_setpoint.Times._04` | ms | 0.70 | module_segment |
| FPW Left T05: Hole Punch Time | `L01S_FPWL_DB_setpoint.Times._05` | ms | 0.70 | module_segment |
| FPW Left T06: LinMot Blow Time | `L01S_FPWL_DB_setpoint.Times._06` | ms | 0.70 | module_segment |
| FPW Left T07: Revolver Blow Time | `L01S_FPWL_DB_setpoint.Times._07` | ms | 0.70 | module_segment |
| FPW Left T08: Revolver Down Delay | `L01S_FPWL_DB_setpoint.Times._08` | ms | 0.70 | module_segment |
| FPW Right T03: Waste Removal Time | `L01S_FPWR_DB_setpoint.Times._03` | ms | 0.70 | module_segment |
| FPW Right T04: Filter Punching Time | `L01S_FPWR_DB_setpoint.Times._04` | ms | 0.70 | module_segment |
| FPW Right T05: Hole Punch Time | `L01S_FPWR_DB_setpoint.Times._05` | ms | 0.70 | module_segment |
| FPW Right T06: LinMot Blow Time | `L01S_FPWR_DB_setpoint.Times._06` | ms | 0.70 | module_segment |
| FPW Right T07: Revolver Blow Time | `L01S_FPWR_DB_setpoint.Times._07` | ms | 0.70 | module_segment |
| FPW Right T08: Revolver Down Delay | `L01S_FPWR_DB_setpoint.Times._08` | ms | 0.70 | module_segment |
| FPW Left X1-Adjust Actual Position | `L01S_FPWL_DB_HMI_connect.Adujst_X1.ActPos` | mm | 0.70 | module_segment |
| FPW Left X2-Adjust Actual Position | `L01S_FPWL_DB_HMI_connect.Adujst_X2.ActPos` | mm | 0.70 | module_segment |
| FPW Left X3-Adjust Actual Position | `L01S_FPWL_DB_HMI_connect.Adujst_X3.ActPos` | mm | 0.70 | module_segment |
| FPW Left Y1-Adjust Actual Position | `L01S_FPWL_DB_HMI_connect.Adujst_Y1.ActPos` | mm | 0.70 | module_segment |
| FPW Left Y2-Adjust Actual Position | `L01S_FPWL_DB_HMI_connect.Adujst_Y2.ActPos` | mm | 0.70 | module_segment |
| FPW Right X1-Adjust Actual Position | `L01S_FPWR_DB_HMI_connect.Adujst_X1.ActPos` | mm | 0.70 | module_segment |
| FPW Right X2-Adjust Actual Position | `L01S_FPWR_DB_HMI_connect.Adujst_X2.ActPos` | mm | 0.70 | module_segment |
| FPW Right X3-Adjust Actual Position | `L01S_FPWR_DB_HMI_connect.Adujst_X3.ActPos` | mm | 0.70 | module_segment |
| FPW Right Y1-Adjust Actual Position | `L01S_FPWR_DB_HMI_connect.Adujst_Y1.ActPos` | mm | 0.70 | module_segment |
| FPW Right Y2-Adjust Actual Position | `L01S_FPWR_DB_HMI_connect.Adujst_Y2.ActPos` | mm | 0.70 | module_segment |
| FPW Left LinMot1 Actual Position | `L01S_FPWL_DB_HMI_connect.LinMot1.Status.ActualPosition` | mm | 0.70 | module_segment |
| FPW Left LinMot2 Actual Position | `L01S_FPWL_DB_HMI_connect.LinMot2.Status.ActualPosition` | mm | 0.70 | module_segment |
| FPW Right LinMot1 Actual Position | `L01S_FPWR_DB_HMI_connect.LinMot1.Status.ActualPosition` | mm | 0.70 | module_segment |
| FPW Right LinMot2 Actual Position | `L01S_FPWR_DB_HMI_connect.LinMot2.Status.ActualPosition` | mm | 0.70 | module_segment |
| FPW Left Revolver Target Position | `L01S_FPWL_DB_HMI_connect.Revolver.TargetPos` | mm | 0.70 | module_segment |
| FPW Right Revolver Target Position | `L01S_FPWR_DB_HMI_connect.Revolver.TargetPos` | mm | 0.70 | module_segment |
| FPW Left LinMot1 Pos1 Target Position | `L01S_FPWL_DB_setpoint.LinMot1_Positions.Pos1.Position` | mm | 0.75 | module_segment |
| FPW Left LinMot1 Pos2 Target Position | `L01S_FPWL_DB_setpoint.LinMot1_Positions.Pos2.Position` | mm | 0.75 | module_segment |
| FPW Left LinMot1 Pos3 Target Position | `L01S_FPWL_DB_setpoint.LinMot1_Positions.Pos3.Position` | mm | 0.75 | module_segment |
| FPW Left LinMot1 Pos4 Target Position | `L01S_FPWL_DB_setpoint.LinMot1_Positions.Pos4.Position` | mm | 0.75 | module_segment |
| FPW Left LinMot1 Pos5 Target Position | `L01S_FPWL_DB_setpoint.LinMot1_Positions.Pos5.Position` | mm | 0.75 | module_segment |
| FPW Left LinMot2 Pos1 Target Position | `L01S_FPWL_DB_setpoint.LinMot2_Positions.Pos1.Position` | mm | 0.75 | module_segment |
| FPW Left LinMot2 Pos2 Target Position | `L01S_FPWL_DB_setpoint.LinMot2_Positions.Pos2.Position` | mm | 0.75 | module_segment |
| FPW Right LinMot1 Pos1 Target Position | `L01S_FPWR_DB_setpoint.LinMot1_Positions.Pos1.Position` | mm | 0.75 | module_segment |
| FPW Right LinMot1 Pos2 Target Position | `L01S_FPWR_DB_setpoint.LinMot1_Positions.Pos2.Position` | mm | 0.75 | module_segment |
| FPW Right LinMot1 Pos3 Target Position | `L01S_FPWR_DB_setpoint.LinMot1_Positions.Pos3.Position` | mm | 0.75 | module_segment |
| FPW Right LinMot1 Pos4 Target Position | `L01S_FPWR_DB_setpoint.LinMot1_Positions.Pos4.Position` | mm | 0.75 | module_segment |
| FPW Right LinMot1 Pos5 Target Position | `L01S_FPWR_DB_setpoint.LinMot1_Positions.Pos5.Position` | mm | 0.75 | module_segment |
| FPW Right LinMot2 Pos1 Target Position | `L01S_FPWR_DB_setpoint.LinMot2_Positions.Pos1.Position` | mm | 0.75 | module_segment |
| FPW Right LinMot2 Pos2 Target Position | `L01S_FPWR_DB_setpoint.LinMot2_Positions.Pos2.Position` | mm | 0.75 | module_segment |
| FPW Left T02: Welding Time | `L01S_FPWL_DB_setpoint.Times._02` | ms | 0.75 | module_segment |
| FPW Right T02: Welding Time | `L01S_FPWR_DB_setpoint.Times._02` | ms | 0.75 | module_segment |
| FPW Heat Setpoint (Recipe) | `MASTER_RECIPE_GENERAL.FPW_HEAT_SP` | °C | 0.75 | module_segment |
| FPW Left Heater Temperature Setpoint | `L01S_FPWL_DB_setpoint.Heater.Temp_Set` | °C | 0.90 | module_segment |
| FPW Right Heater Temperature Setpoint | `L01S_FPWR_DB_setpoint.Heater.Temp_Set` | °C | 0.90 | module_segment |
| FPW Left Heater1 Actual Temperature | `L01S_FPWL_DB_HMI_connect.Heater1.Status.Actual` | °C | 0.90 | module_segment |
| FPW Right Heater1 Actual Temperature | `L01S_FPWR_DB_HMI_connect.Heater1.Status.Actual` | °C | 0.90 | module_segment |

### PRI printing unit (Corona printer control module) (MC007-PRI)

- 247 candidate tag(s) considered -> 75 kept as genuine parameters (30%).
- Kept tags found by: 75 via *module_segment* (the tag name contains this station's own PLC/module code as a literal segment - the strongest signal available).

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| Gap: PRH2 Station to PRIH Tack Seal (Web1) | `GE1_DB_setpoint.StationGaps.PRH2_St_PRIH_TS` | mm | 0.50 | module_segment |
| Gap: PRIH Inspection to PRIH Station | `GE1_DB_setpoint.StationGaps.PRIH_Insp_PRIH_St` | mm | 0.50 | module_segment |
| Gap: PRIH Station to Splice (Web1) | `GE1_DB_setpoint.StationGaps.PRIH_St_SPLICE_W1` | mm | 0.50 | module_segment |
| Gap: PRIH Station to Splice (Web2) | `GE1_DB_setpoint.StationGaps.PRIH_St_SPLICE_W2` | mm | 0.50 | module_segment |
| Gap: PRIH Tack Seal to PRIH Inspection | `GE1_DB_setpoint.StationGaps.PRIH_TS_PRIH_Insp` | mm | 0.50 | module_segment |
| PRIH Cycles After Film Finished Left (Setpoint) | `L01S_PRIH_DB_setpoint.CyclesAfterFilmFinished._left` | - | 0.50 | module_segment |
| PRIH Cycles After Film Finished Right (Setpoint) | `L01S_PRIH_DB_setpoint.CyclesAfterFilmFinished._right` | - | 0.50 | module_segment |
| PRIH Inspection LHS Job Number (Setpoint) | `L01S_PRIH_DB_setpoint.Inspection_LHS.JobNr` | - | 0.50 | module_segment |
| PRIH Inspection RHS Job Number (Setpoint) | `L01S_PRIH_DB_setpoint.Inspection_RHS.JobNr` | - | 0.50 | module_segment |
| PRIH Clamp Feed Lower Enabled (FP07) | `L01S_PRIH_DB_setpoint.Selections.FP07` | - | 0.50 | module_segment |
| PRIH Cycles After Film Finished Left (Actual) | `L01S_PRIH_DB_HMI_connect.CyclesAfterFilmFinished._left` | - | 0.50 | module_segment |
| PRIH Cycles After Film Finished Right (Actual) | `L01S_PRIH_DB_HMI_connect.CyclesAfterFilmFinished._right` | - | 0.50 | module_segment |
| PRIH Inspection LHS Job Number (Actual) | `L01S_PRIH_DB_HMI_connect.Inspection._LHS.JobNr` | - | 0.50 | module_segment |
| PRIH Inspection RHS Job Number (Actual) | `L01S_PRIH_DB_HMI_connect.Inspection._RHS.JobNr` | - | 0.50 | module_segment |
| PRIH Print Inspection LHS Enabled (FP03) | `L01S_PRIH_DB_HMI_connect.Selections.FP02` | - | 0.50 | module_segment |
| PRIH Print Inspection RHS Enabled (FP04) | `L01S_PRIH_DB_HMI_connect.Selections.FP03` | - | 0.50 | module_segment |
| PRIH Operation Mode Semiautomatic (FP01) | `L01S_PRIH_DB_HMI_connect.Selections.SemiAuto` | - | 0.50 | module_segment |
| PRIH Station Enabled (FP01) | `L01S_PRIH_DB_setpoint.Selections.HotStamp` | - | 0.55 | module_segment |
| PRIH Tack Sealer Enabled (FP06) | `L01S_PRIH_DB_setpoint.Selections.TackSealer` | - | 0.55 | module_segment |
| Print Station Heat Alarm High | `MASTER_RECIPE_GENERAL.PRI_HEAT_ALARM_HIGH` | °C | 0.70 | module_segment |
| Print Station Heat Alarm Low | `MASTER_RECIPE_GENERAL.PRI_HEAT_ALARM_LOW` | °C | 0.70 | module_segment |
| PRIH Cycle Counter Left | `L01S_PRIH_DB_HMI_connect.Count.CycleCounterLeft` | - | 0.70 | module_segment |
| PRIH Cycle Counter Right | `L01S_PRIH_DB_HMI_connect.Count.CycleCounterRight` | - | 0.70 | module_segment |
| Print Station Heat Tolerance | `MASTER_RECIPE_GENERAL.PRI_HEAT_TOL` | °C | 0.75 | module_segment |
| Print Station Seal Time | `MASTER_RECIPE_GENERAL.PRI_SEAL_TIME` | ms | 0.75 | module_segment |
| PRIH Lower Clamp Feed Gearing Factor Sync | `L01S_PRIH_DB_setpoint.LowerClampFeed.GearingFactorSync` | % | 0.75 | module_segment |
| PRIH Cycle Time Setpoint (T01) | `L01S_PRIH_DB_setpoint.Times.CycleTime` | ms | 0.75 | module_segment |
| PRIH Printing Time Left Setpoint (T02) | `L01S_PRIH_DB_setpoint.Times.PrintingTimeLeft` | ms | 0.75 | module_segment |
| PRIH Printing Time Right Setpoint (T03) | `L01S_PRIH_DB_setpoint.Times.PrintingTimeRight` | ms | 0.75 | module_segment |
| PRIH Tack Seal Time Setpoint (T04) | `L01S_PRIH_DB_setpoint.Times.TackSealTime` | ms | 0.75 | module_segment |
| PRIH Actual Cycle Time (T01) | `L01S_PRIH_DB_HMI_connect.HMIActualTimes.T01` | ms | 0.75 | module_segment |
| Print Station Heat Setpoint | `MASTER_RECIPE_GENERAL.PRI_HEAT_SP` | °C | 0.80 | module_segment |
| PRIH Adjust X (Camera) Offset Position | `L01S_PRIH_DB_setpoint.Adjust_X_C.Offset_Pos` | mm | 0.80 | module_segment |
| PRIH Adjust X (Camera) Target Position | `L01S_PRIH_DB_setpoint.Adjust_X_C.Target_Pos` | mm | 0.80 | module_segment |
| PRIH Adjust X (Hot Stamp) Offset Position | `L01S_PRIH_DB_setpoint.Adjust_X_HS.Offset_Pos` | mm | 0.80 | module_segment |
| PRIH Adjust X (Hot Stamp) Target Position | `L01S_PRIH_DB_setpoint.Adjust_X_HS.Target_Pos` | mm | 0.80 | module_segment |
| PRIH Adjust X (Tack Sealer) Offset Position | `L01S_PRIH_DB_setpoint.Adjust_X_TS.Offset_Pos` | mm | 0.80 | module_segment |
| PRIH Adjust X (Tack Sealer) Target Position | `L01S_PRIH_DB_setpoint.Adjust_X_TS.Target_Pos` | mm | 0.80 | module_segment |
| PRIH Adjust Y (Hot Stamp LHS) Offset Position | `L01S_PRIH_DB_setpoint.Adjust_Y_HS_LHS.Offset_Pos` | mm | 0.80 | module_segment |
| PRIH Adjust Y (Hot Stamp LHS) Target Position | `L01S_PRIH_DB_setpoint.Adjust_Y_HS_LHS.Target_Pos` | mm | 0.80 | module_segment |
| PRIH Adjust Y (Hot Stamp RHS) Offset Position | `L01S_PRIH_DB_setpoint.Adjust_Y_HS_RHS.Offset_Pos` | mm | 0.80 | module_segment |
| PRIH Adjust Y (Hot Stamp RHS) Target Position | `L01S_PRIH_DB_setpoint.Adjust_Y_HS_RHS.Target_Pos` | mm | 0.80 | module_segment |
| PRIH Heater1 (Hot Stamp Left) Correction Value | `L01S_PRIH_DB_setpoint.Heater1.Correction_Value` | °K | 0.80 | module_segment |
| PRIH Heater2 (Hot Stamp Right) Correction Value | `L01S_PRIH_DB_setpoint.Heater2.Correction_Value` | °K | 0.80 | module_segment |
| PRIH Tack Seal Heater Correction Value | `L01S_PRIH_DB_setpoint.HeaterTackSeal.Correction_Value` | °K | 0.80 | module_segment |
| PRIH Lower Clamp Feed Backward Acceleration | `L01S_PRIH_DB_setpoint.LowerClampFeed.Backward.Acc` | % | 0.80 | module_segment |
| PRIH Lower Clamp Feed Backward Deceleration | `L01S_PRIH_DB_setpoint.LowerClampFeed.Backward.Dec` | % | 0.80 | module_segment |
| PRIH Lower Clamp Feed Backward Target Position | `L01S_PRIH_DB_setpoint.LowerClampFeed.Backward.Position` | mm | 0.80 | module_segment |
| PRIH Lower Clamp Feed Backward Velocity | `L01S_PRIH_DB_setpoint.LowerClampFeed.Backward.Velocity` | % | 0.80 | module_segment |
| PRIH Lower Clamp Feed Forward Target Position | `L01S_PRIH_DB_setpoint.LowerClampFeed.Forward.Position` | mm | 0.80 | module_segment |
| PRIH Adjust X (Camera) Actual Position | `L01S_PRIH_DB_HMI_connect.Adjust_X_C.ActPos` | mm | 0.80 | module_segment |
| PRIH Adjust X (Hot Stamp) Actual Position | `L01S_PRIH_DB_HMI_connect.Adjust_X_HS.ActPos` | mm | 0.80 | module_segment |
| PRIH Adjust X (Tack Sealer) Actual Position | `L01S_PRIH_DB_HMI_connect.Adjust_X_TS.ActPos` | mm | 0.80 | module_segment |
| PRIH Adjust Y (Hot Stamp LHS) Actual Position | `L01S_PRIH_DB_HMI_connect.Adjust_Y_HS_LHS.ActPos` | mm | 0.80 | module_segment |
| PRIH Adjust Y (Hot Stamp RHS) Actual Position | `L01S_PRIH_DB_HMI_connect.Adjust_Y_HS_RHS.ActPos` | mm | 0.80 | module_segment |
| PRIH Lower Clamp Feed Actual Position | `L01S_PRIH_DB_HMI_connect.LowerClampFeed.ActPos` | mm | 0.80 | module_segment |
| PRIH Lower Clamp Feed Target Position | `L01S_PRIH_DB_HMI_connect.LowerClampFeed.TargetPos` | mm | 0.80 | module_segment |
| PRI Left PSI Setpoint (FWC Pressure Cylinder) | `LO1S_FWC_DB_CFF2_PSI.Left_PRI_PSI_Setpoint` | PSI | 0.85 | module_segment |
| PRI Left PSI Setpoint Maximum | `LO1S_FWC_DB_CFF2_PSI.Left_PRI_PSI_SP_Max` | PSI | 0.85 | module_segment |
| PRI Left PSI Setpoint Minimum | `LO1S_FWC_DB_CFF2_PSI.Left_PRI_PSI_SP_Min` | PSI | 0.85 | module_segment |
| PRI Right PSI Setpoint | `LO1S_FWC_DB_CFF2_PSI.Right_PRI_PSI_Setpoint` | PSI | 0.85 | module_segment |
| PRI Right PSI Setpoint Maximum | `LO1S_FWC_DB_CFF2_PSI.Right_PRI_PSI_SP_Max` | PSI | 0.85 | module_segment |
| PRI Right PSI Setpoint Minimum | `LO1S_FWC_DB_CFF2_PSI.Right_PRI_PSI_SP_Min` | PSI | 0.85 | module_segment |
| PRIH Heater1 (Hot Stamp Left) Lower Alarm Boundary | `L01S_PRIH_DB_setpoint.Heater1.Alarm_Boundary_Down` | °C | 0.85 | module_segment |
| PRIH Heater1 (Hot Stamp Left) Upper Alarm Boundary | `L01S_PRIH_DB_setpoint.Heater1.Alarm_Boundary_Up` | °C | 0.85 | module_segment |
| PRIH Heater2 (Hot Stamp Right) Lower Alarm Boundary | `L01S_PRIH_DB_setpoint.Heater2.Alarm_Boundary_Down` | °C | 0.85 | module_segment |
| PRIH Heater2 (Hot Stamp Right) Upper Alarm Boundary | `L01S_PRIH_DB_setpoint.Heater2.Alarm_Boundary_Up` | °C | 0.85 | module_segment |
| PRIH Tack Seal Heater Lower Alarm Boundary | `L01S_PRIH_DB_setpoint.HeaterTackSeal.Alarm_Boundary_Down` | °C | 0.85 | module_segment |
| PRIH Tack Seal Heater Upper Alarm Boundary | `L01S_PRIH_DB_setpoint.HeaterTackSeal.Alarm_Boundary_Up` | °C | 0.85 | module_segment |
| PRIH Heater1 (Hot Stamp Left) Temperature Setpoint | `L01S_PRIH_DB_setpoint.Heater1.Temp_Set` | °C | 0.90 | module_segment |
| PRIH Heater2 (Hot Stamp Right) Temperature Setpoint | `L01S_PRIH_DB_setpoint.Heater2.Temp_Set` | °C | 0.90 | module_segment |
| PRIH Tack Seal Heater Temperature Setpoint | `L01S_PRIH_DB_setpoint.HeaterTackSeal.Temp_Set` | °C | 0.90 | module_segment |
| PRIH Heater1 (Hot Stamp Left) Actual Temperature | `L01S_PRIH_DB_HMI_connect.Heater1.Status.Actual` | °C | 0.90 | module_segment |
| PRIH Heater2 (Hot Stamp Right) Actual Temperature | `L01S_PRIH_DB_HMI_connect.Heater2.Status.Actual` | °C | 0.90 | module_segment |
| PRIH Tack Seal Heater Actual Temperature | `L01S_PRIH_DB_HMI_connect.HeaterTackSeal.Status.Actual` | °C | 0.90 | module_segment |

### FOR filter welding station (Corona printer control module) (MC007-FOR)

- 12 candidate tag(s) considered -> 6 kept as genuine parameters (50%).
- Kept tags found by: 6 via *module_segment* (the tag name contains this station's own PLC/module code as a literal segment - the strongest signal available).

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| FOR Fife Web 3 Offset Position | `L01_INS_DB_setpoint.Adjust_FOR_Fife_Web_3.Offset_Pos` | mm | 0.70 | module_segment |
| FOR Fife Web 3 Target Position | `L01_INS_DB_setpoint.Adjust_FOR_Fife_Web_3.Target_Pos` | mm | 0.70 | module_segment |
| FOR Fife Web 4 Offset Position | `L01_INS_DB_setpoint.Adjust_FOR_Fife_Web_4.Offset_Pos` | mm | 0.70 | module_segment |
| FOR Fife Web 4 Target Position | `L01_INS_DB_setpoint.Adjust_FOR_Fife_Web_4.Target_Pos` | mm | 0.70 | module_segment |
| FOR Fife Web 3 Actual Position | `L01_INS_DB_HMI_connect.Adjust_FOR_Fife_Web_3.ActPos` | mm | 0.70 | module_segment |
| FOR Fife Web 4 Actual Position | `L01_INS_DB_HMI_connect.Adjust_FOR_Fife_Web_4.ActPos` | mm | 0.70 | module_segment |

### COR corona surface-treatment station (printer control module) (MC007-COR)

- 0 candidate tag(s) considered -> 0 kept as genuine parameters (0%).

_No genuine parameters found among this station's candidates._

### FHP flange hole-punch station (MC007-FHP)

- 159 candidate tag(s) considered -> 41 kept as genuine parameters (26%).
- Kept tags found by: 41 via *module_segment* (the tag name contains this station's own PLC/module code as a literal segment - the strongest signal available).
- 7 kept parameter(s) below 0.5 confidence - flagged with ⚠ below.

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| FHP Tacking Nippers Self-Tuning Excitation Delta ⚠ | `L01S_FHP_DB_HMI_connect.TackingNippers.Control.TUN_DLMN` | % | 0.40 | module_segment |
| FHP Tacking Nippers Heater Y-Scaling Groundpoint Boundary ⚠ | `L01S_FHP_DB_setpoint.TackingNippers.Y_Scaling_groundpoint` | - | 0.40 | module_segment |
| FHP Tacking Nippers Heater Y-Scaling Toppoint Boundary ⚠ | `L01S_FHP_DB_setpoint.TackingNippers.Y_Scaling_toppoint` | - | 0.40 | module_segment |
| FHP FP01: Operation Mode Semi-Automatic ⚠ | `L01S_FHP_DB_HMI_connect.Selections.SemiAuto` | - | 0.45 | module_segment |
| FHP Tacking Nippers Derivative Factor (TD/TM_LAG) ⚠ | `L01S_FHP_DB_HMI_connect.TackingNippers.Control.D_F` | - | 0.45 | module_segment |
| FHP FP02: Stretching Clamp ⚠ | `L01S_FHP_DB_HMI_connect.Selections.FP02` | - | 0.45 | module_segment |
| FHP FP06: Tack Sealer Enabled ⚠ | `L01S_FHP_DB_setpoint.Selections.TackSealer` | - | 0.45 | module_segment |
| Gap 15: FHP Station to Splice Web 3 | `GE1_DB_setpoint.StationGaps.FHP_St_SPLICE_W3` | mm | 0.50 | module_segment |
| FHP FP01: Station Enabled | `L01S_FHP_DB_setpoint.Selections.StationEnabled` | - | 0.50 | module_segment |
| Gap 39: FHP Station to SPU Station (Web4) | `GE1_DB_setpoint.StationGaps.FHP_St_SPU_St` | mm | 0.50 | module_segment |
| FHP Tacking Nippers PID Proportional Gain | `L01S_FHP_DB_HMI_connect.TackingNippers.Control.GAIN` | - | 0.50 | module_segment |
| FHP Tacking Nippers Manipulated Variable High Limit | `L01S_FHP_DB_HMI_connect.TackingNippers.Control.LMN_HLM` | % | 0.50 | module_segment |
| FHP Tacking Nippers Manipulated Variable Low Limit | `L01S_FHP_DB_HMI_connect.TackingNippers.Control.LMN_LLM` | % | 0.50 | module_segment |
| FHP Tacking Nippers Manual Output Value | `L01S_FHP_DB_HMI_connect.TackingNippers.Control.MAN` | % | 0.50 | module_segment |
| FHP Tacking Nippers Manual-Switch Temperature Deviation | `L01S_FHP_DB_HMI_connect.TackingNippers.Control.MAN_ON_VALUE` | °C | 0.50 | module_segment |
| FHP Tacking Nippers PID Derivative Time | `L01S_FHP_DB_HMI_connect.TackingNippers.Control.TD` | s | 0.50 | module_segment |
| FHP Tacking Nippers PID Integration Time | `L01S_FHP_DB_HMI_connect.TackingNippers.Control.TI` | s | 0.50 | module_segment |
| FHP Tacking Nippers Controller Proportional Gain (Raw) | `L01S_FHP_IDB_TackingNipp.DI_TCONT_CP.GAIN` | - | 0.50 | module_segment |
| FHP Tacking Nippers Controller Derivative Time (Raw) | `L01S_FHP_IDB_TackingNipp.DI_TCONT_CP.TD` | s | 0.50 | module_segment |
| FHP Tacking Nippers Controller Reset (Integral) Time (Raw) | `L01S_FHP_IDB_TackingNipp.DI_TCONT_CP.TI` | s | 0.50 | module_segment |
| FHP Cycle Time (Actual, T01) | `L01S_FHP_DB_HMI_connect.HMIActualTimes.T01` | ms | 0.55 | module_segment |
| FHP Cycle Counter | `L01S_FHP_DB_HMI_connect.Count.CycleCounter` | - | 0.60 | module_segment |
| FHP Tacking Nippers PID Output | `L01S_FHP_DB_HMI_connect.TackingNippers.Status.LMN` | % | 0.60 | module_segment |
| FHP Tacking Nippers Heater Correction Value | `L01S_FHP_DB_setpoint.TackingNippers.Correction_Value` | °K | 0.60 | module_segment |
| FHP T03: Delay of Press Out | `L01S_FHP_DB_setpoint.Times._03` | ms | 0.65 | module_segment |
| FHP T01: Cycle Time Setpoint | `L01S_FHP_DB_setpoint.Times.CycleTime` | ms | 0.65 | module_segment |
| FHP T04: Tack Seal Time | `L01S_FHP_DB_setpoint.Times.TackSealTime` | ms | 0.65 | module_segment |
| FHP X-Adjust Offset Position | `L01S_FHP_DB_setpoint.Adujst_X.Offset_Pos` | mm | 0.70 | module_segment |
| FHP X-Adjust Target Position | `L01S_FHP_DB_setpoint.Adujst_X.Target_Pos` | mm | 0.70 | module_segment |
| FHP Y-Adjust Offset Position | `L01S_FHP_DB_setpoint.Adujst_Y.Offset_Pos` | mm | 0.70 | module_segment |
| FHP Y-Adjust Target Position | `L01S_FHP_DB_setpoint.Adujst_Y.Target_Pos` | mm | 0.70 | module_segment |
| FHP Y-Adjust Expeller Offset Position | `L01S_FHP_DB_setpoint.Adujst_Y_Expeller.Offset_Pos` | mm | 0.70 | module_segment |
| FHP Y-Adjust Expeller Target Position | `L01S_FHP_DB_setpoint.Adujst_Y_Expeller.Target_Pos` | mm | 0.70 | module_segment |
| FHP T02: Punching Time | `L01S_FHP_DB_setpoint.Times._02` | ms | 0.70 | module_segment |
| FHP X-Adjust Actual Position | `L01S_FHP_DB_HMI_connect.Adujst_X.ActPos` | mm | 0.70 | module_segment |
| FHP Y-Adjust Actual Position | `L01S_FHP_DB_HMI_connect.Adujst_Y.ActPos` | mm | 0.70 | module_segment |
| FHP Y-Adjust Expeller Actual Position | `L01S_FHP_DB_HMI_connect.Adujst_Y_Expeller.ActPos` | mm | 0.70 | module_segment |
| FHP Tacking Nippers Lower Alarm Boundary | `L01S_FHP_DB_setpoint.TackingNippers.Alarm_Boundary_Down` | °C | 0.70 | module_segment |
| FHP Tacking Nippers Upper Alarm Boundary | `L01S_FHP_DB_setpoint.TackingNippers.Alarm_Boundary_Up` | °C | 0.70 | module_segment |
| FHP Tacking Nippers Actual Temperature | `L01S_FHP_DB_HMI_connect.TackingNippers.Status.Actual` | °C | 0.90 | module_segment |
| FHP Tacking Nippers Temperature Setpoint | `L01S_FHP_DB_setpoint.TackingNippers.Temp_Set` | °C | 0.90 | module_segment |

### BSW backing-seal welding station (MC007-BSW)

- 129 candidate tag(s) considered -> 20 kept as genuine parameters (16%).
- Kept tags found by: 20 via *module_segment* (the tag name contains this station's own PLC/module code as a literal segment - the strongest signal available).
- 1 kept parameter(s) below 0.5 confidence - flagged with ⚠ below.

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| BSW Delay Cooling Fan On (Actual Time, T22) ⚠ | `L01S_BSW_DB_HMI_connect.HMIActualTimes.T22` | ms | 0.40 | module_segment |
| Gap: BSW Station to FHP Station | `GE1_DB_setpoint.StationGaps.BSW_St_FHP_St` | mm | 0.50 | module_segment |
| BSW Stretching Clamp Enabled (FP02) | `L01S_BSW_DB_HMI_connect.Selections.FP02` | - | 0.50 | module_segment |
| BSW Operation Mode Semiautomatic (FP01) | `L01S_BSW_DB_HMI_connect.Selections.SemiAuto` | - | 0.50 | module_segment |
| BSW Station Enabled (FP01) | `L01S_BSW_DB_setpoint.Selections.StationEnabled` | - | 0.55 | module_segment |
| BSW Cycle Counter | `L01S_BSW_DB_HMI_connect.Count.CycleCounter` | - | 0.70 | module_segment |
| BSW Welding Time Setpoint (T02) | `L01S_BSW_DB_setpoint.Times._02` | ms | 0.75 | module_segment |
| BSW Cycle Time Setpoint (T01) | `L01S_BSW_DB_setpoint.Times.CycleTime` | ms | 0.75 | module_segment |
| BSW Actual Cycle Time (T01) | `L01S_BSW_DB_HMI_connect.HMIActualTimes.T01` | ms | 0.75 | module_segment |
| BSW Adjust X Offset Position | `L01S_BSW_DB_setpoint.Adujst_X.Offset_Pos` | mm | 0.80 | module_segment |
| BSW Adjust X Target Position | `L01S_BSW_DB_setpoint.Adujst_X.Target_Pos` | mm | 0.80 | module_segment |
| BSW Adjust Y Offset Position | `L01S_BSW_DB_setpoint.Adujst_Y.Offset_Pos` | mm | 0.80 | module_segment |
| BSW Adjust Y Target Position | `L01S_BSW_DB_setpoint.Adujst_Y.Target_Pos` | mm | 0.80 | module_segment |
| BSW Heater Correction Value | `L01S_BSW_DB_setpoint.Heater.Correction_Value` | °K | 0.80 | module_segment |
| BSW Adjust X Actual Position | `L01S_BSW_DB_HMI_connect.Adujst_X.ActPos` | mm | 0.80 | module_segment |
| BSW Adjust Y Actual Position | `L01S_BSW_DB_HMI_connect.Adujst_Y.ActPos` | mm | 0.80 | module_segment |
| BSW Heater Lower Alarm Boundary | `L01S_BSW_DB_setpoint.Heater.Alarm_Boundary_Down` | °C | 0.85 | module_segment |
| BSW Heater Upper Alarm Boundary | `L01S_BSW_DB_setpoint.Heater.Alarm_Boundary_Up` | °C | 0.85 | module_segment |
| BSW Heater Temperature Setpoint | `L01S_BSW_DB_setpoint.Heater.Temp_Set` | °C | 0.90 | module_segment |
| BSW Heater Actual Temperature | `L01S_BSW_DB_HMI_connect.Heater1.Status.Actual` | °C | 0.90 | module_segment |

### FWC flange welding station (MC007-FWC)

- 173 candidate tag(s) considered -> 55 kept as genuine parameters (32%).
- Kept tags found by: 55 via *module_segment* (the tag name contains this station's own PLC/module code as a literal segment - the strongest signal available).

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| Gap: FWC Inspection to FWC Station | `GE1_DB_setpoint.StationGaps.FWC_Insp_FWC_St` | mm | 0.50 | module_segment |
| Gap: FWC Station to BSW Station | `GE1_DB_setpoint.StationGaps.FWC_St_BSW_St` | mm | 0.50 | module_segment |
| FWC Inspection LHS Job Number (Setpoint) | `L01S_FWC_DB_setpoint.Inspection_LHS.JobNr` | - | 0.50 | module_segment |
| FWC Inspection RHS Job Number (Setpoint) | `L01S_FWC_DB_setpoint.Inspection_RHS.JobNr` | - | 0.50 | module_segment |
| FWC Welding Belt Selected (FP04) | `L01S_FWC_DB_setpoint.Selections.WeldingBelt` | - | 0.50 | module_segment |
| FWC Inspection LHS Job Number (Actual) | `L01S_FWC_DB_HMI_connect.Inspection._LHS.JobNr` | - | 0.50 | module_segment |
| FWC Inspection RHS Job Number (Actual) | `L01S_FWC_DB_HMI_connect.Inspection._RHS.JobNr` | - | 0.50 | module_segment |
| FWC Flange Inspection LHS Enabled (FP03) | `L01S_FWC_DB_HMI_connect.Selections.FP02` | - | 0.50 | module_segment |
| FWC Flange Inspection RHS Enabled (FP04) | `L01S_FWC_DB_HMI_connect.Selections.FP03` | - | 0.50 | module_segment |
| FWC Operation Mode Semiautomatic (FP01) | `L01S_FWC_DB_HMI_connect.Selections.SemiAuto` | - | 0.50 | module_segment |
| FWC CFF2 Left Pressure Setpoint | `FWC_DB_CFF2_Left.pressure_SP` | PSI | 0.55 | module_segment |
| FWC LHS Sealer Blow-Off Enable | `GEN_ADDITIONAL_FUNCTIONS.FWC_LHS_BLOWOFF` | - | 0.55 | module_segment |
| FWC RHS Sealer Blow-Off Enable | `GEN_ADDITIONAL_FUNCTIONS.FWC_RHS_BLOWOFF` | - | 0.55 | module_segment |
| FWC Station Enabled (FP01) | `L01S_FWC_DB_setpoint.Selections.StationEnabled` | - | 0.55 | module_segment |
| FWC LHS Sealer Blow-Off Time | `GEN_ADDITIONAL_FUNCTIONS.FWC_LHS_BLOWOFF_TIME` | ms | 0.60 | module_segment |
| FWC RHS Sealer Blow-Off Time | `GEN_ADDITIONAL_FUNCTIONS.FWC_RHS_BLOWOFF_TIME` | ms | 0.60 | module_segment |
| FWC Delay Cooling Fan On (Actual Time, T22) | `L01S_FWC_DB_HMI_connect.HMIActualTimes.T22` | ms | 0.60 | module_segment |
| FWC Heater Alarm High | `MASTER_RECIPE_FWC.FWC_HEATER_ALM_HIGH` | °C | 0.70 | module_segment |
| FWC Heater Alarm Low | `MASTER_RECIPE_FWC.FWC_HEATER_ALM_LOW` | °C | 0.70 | module_segment |
| FWC Seal Height | `MASTER_RECIPE_FWC.FWC_HEIGHT` | mm | 0.70 | module_segment |
| FWC Cycle Counter | `L01S_FWC_DB_HMI_connect.Count.CycleCounter` | - | 0.70 | module_segment |
| FWC Left PRI Pressure Reading | `LO1S_FWC_DB_CFF2_PSI.IW0452SCALED` | PSI | 0.75 | module_segment |
| FWC Right PRI Pressure Reading | `LO1S_FWC_DB_CFF2_PSI.IW0454SCALED` | PSI | 0.75 | module_segment |
| FWC Heater Tolerance | `MASTER_RECIPE_FWC.FWC_HEATER_TOL` | °C | 0.75 | module_segment |
| FWC Seal Time | `MASTER_RECIPE_FWC.FWC_SEAL_TIME` | ms | 0.75 | module_segment |
| FWC Cycle Time Setpoint (T01) | `L01S_FWC_DB_setpoint.Times.CycleTime` | ms | 0.75 | module_segment |
| FWC Welding Time Setpoint (T02) | `L01S_FWC_DB_setpoint.Times.WeldingTime` | ms | 0.75 | module_segment |
| FWC Welding Top Close Jerk | `L01S_FWC_DB_setpoint.WeldingTop.Jerk_Close` | % | 0.75 | module_segment |
| FWC Welding Top Open Jerk | `L01S_FWC_DB_setpoint.WeldingTop.Jerk_Open` | % | 0.75 | module_segment |
| FWC Welding Top Relative Load Position | `L01S_FWC_DB_setpoint.WeldingTop.Pos_RelLoad` | 1/100 mm | 0.75 | module_segment |
| FWC Actual Cycle Time (T01) | `L01S_FWC_DB_HMI_connect.HMIActualTimes.T01` | ms | 0.75 | module_segment |
| FWC Welding Top Maximum Position | `L01S_FWC_DB_HMI_connect.WeldingTop.MaxPos` | mm | 0.75 | module_segment |
| FWC Bottom Pressure Setpoint | `LO1S_FWC_DB_CFF2_PSI.Bottom_Pressure_Setpoint` | PSI | 0.80 | module_segment |
| FWC Bottom Pressure Setpoint Maximum | `LO1S_FWC_DB_CFF2_PSI.Bottom_Pressure_SP_Max` | PSI | 0.80 | module_segment |
| FWC Bottom Pressure Setpoint Minimum | `LO1S_FWC_DB_CFF2_PSI.Bottom_Pressure_SP_Min` | PSI | 0.80 | module_segment |
| FWC Heater Setpoint | `MASTER_RECIPE_FWC.FWC_HEATER_SP` | °C | 0.80 | module_segment |
| FWC Adjust X Offset Position | `L01S_FWC_DB_setpoint.Adjust_X.Offset_Pos` | mm | 0.80 | module_segment |
| FWC Adjust X Target Position | `L01S_FWC_DB_setpoint.Adjust_X.Target_Pos` | mm | 0.80 | module_segment |
| FWC Lower Heater Correction Value | `L01S_FWC_DB_setpoint.HeaterLower.Correction_Value` | 1/10 °K | 0.80 | module_segment |
| FWC Welding Top Close Acceleration | `L01S_FWC_DB_setpoint.WeldingTop.Acc_Close` | % | 0.80 | module_segment |
| FWC Welding Top Open Acceleration | `L01S_FWC_DB_setpoint.WeldingTop.Acc_Open` | % | 0.80 | module_segment |
| FWC Welding Top Close Deceleration | `L01S_FWC_DB_setpoint.WeldingTop.Dec_Close` | % | 0.80 | module_segment |
| FWC Welding Top Open Deceleration | `L01S_FWC_DB_setpoint.WeldingTop.Dec_Open` | % | 0.80 | module_segment |
| FWC Welding Top Close Position | `L01S_FWC_DB_setpoint.WeldingTop.Pos_Close` | 1/100 mm | 0.80 | module_segment |
| FWC Welding Top Die-Change Position | `L01S_FWC_DB_setpoint.WeldingTop.Pos_DieChange` | 1/100 mm | 0.80 | module_segment |
| FWC Welding Top Open Position | `L01S_FWC_DB_setpoint.WeldingTop.Pos_Open` | 1/100 mm | 0.80 | module_segment |
| FWC Welding Top Close Velocity | `L01S_FWC_DB_setpoint.WeldingTop.Velocity_Close` | % | 0.80 | module_segment |
| FWC Welding Top Open Velocity | `L01S_FWC_DB_setpoint.WeldingTop.Velocity_Open` | % | 0.80 | module_segment |
| FWC Adjust X Actual Position | `L01S_FWC_DB_HMI_connect.Adjust_X.ActPos` | mm | 0.80 | module_segment |
| FWC Welding Top Actual Position | `L01S_FWC_DB_HMI_connect.WeldingTop.ActPos` | mm | 0.80 | module_segment |
| FWC Welding Top Target Position | `L01S_FWC_DB_HMI_connect.WeldingTop.TargetPos` | mm | 0.80 | module_segment |
| FWC Lower Heater Lower Alarm Boundary | `L01S_FWC_DB_setpoint.HeaterLower.Alarm_Boundary_Down` | 1/10 °C | 0.85 | module_segment |
| FWC Lower Heater Upper Alarm Boundary | `L01S_FWC_DB_setpoint.HeaterLower.Alarm_Boundary_Up` | 1/10 °C | 0.85 | module_segment |
| FWC Lower Heater Temperature Setpoint | `L01S_FWC_DB_setpoint.HeaterLower.Temp_Set` | 1/10 °C | 0.90 | module_segment |
| FWC Lower Heater Actual Temperature | `L01S_FWC_DB_HMI_connect.HeaterLower.Status.Actual` | °C | 0.90 | module_segment |

### AF binder-flap welding station (MC007-AF)

- 419 candidate tag(s) considered -> 66 kept as genuine parameters (16%).
- Kept tags found by: 66 via *module_segment* (the tag name contains this station's own PLC/module code as a literal segment - the strongest signal available).
- 18 kept parameter(s) below 0.5 confidence - flagged with ⚠ below.

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| AFL Unwinder Low Speed ⚠ | `L01S_AFL_DB_setpoint.Unwinder.LowSpeed` | - | 0.40 | module_segment |
| AFL Upper Heater PID Output ⚠ | `L01S_AFL_DB_HMI_connect.HeaterUpper.Status.LMN` | % | 0.40 | module_segment |
| AFL Turntable Actual Position ⚠ | `L01S_AFL_DB_HMI_connect.Turntable.ActPos` | - | 0.40 | module_segment |
| AFL Turntable Target Position ⚠ | `L01S_AFL_DB_HMI_connect.Turntable.TargetPos` | - | 0.40 | module_segment |
| AFR Unwinder Low Speed ⚠ | `L01S_AFR_DB_setpoint.Unwinder.LowSpeed` | - | 0.40 | module_segment |
| AFR Upper Heater PID Output ⚠ | `L01S_AFR_DB_HMI_connect.HeaterUpper.Status.LMN` | % | 0.40 | module_segment |
| AFR Turntable Actual Position ⚠ | `L01S_AFR_DB_HMI_connect.Turntable.ActPos` | - | 0.40 | module_segment |
| AFR Turntable Target Position ⚠ | `L01S_AFR_DB_HMI_connect.Turntable.TargetPos` | - | 0.40 | module_segment |
| AFL Turntable Position 1 Setpoint ⚠ | `L01S_AFL_DB_setpoint.Turntable._Pos1.Position` | - | 0.45 | module_segment |
| AFL Turntable Position 2 Setpoint ⚠ | `L01S_AFL_DB_setpoint.Turntable._Pos2.Position` | - | 0.45 | module_segment |
| AFL Cycle Counter ⚠ | `L01S_AFL_DB_HMI_connect.Count.CycleCounter` | - | 0.45 | module_segment |
| AFL Flap Punch Register Position Setpoint ⚠ | `L01S_AFL_DB_HMI_connect.FlapFeedRegister.Set.PosPunch` | mm | 0.45 | module_segment |
| AFL Flap Coil Actual Counter At End ⚠ | `L01S_AFL_DB_HMI_connect.FlapFeedRegister.States.CoilCounter` | - | 0.45 | module_segment |
| AFR Turntable Position 1 Setpoint ⚠ | `L01S_AFR_DB_setpoint.Turntable._Pos1.Position` | - | 0.45 | module_segment |
| AFR Turntable Position 2 Setpoint ⚠ | `L01S_AFR_DB_setpoint.Turntable._Pos2.Position` | - | 0.45 | module_segment |
| AFR Cycle Counter ⚠ | `L01S_AFR_DB_HMI_connect.Count.CycleCounter` | - | 0.45 | module_segment |
| AFR Flap Punch Register Position Setpoint ⚠ | `L01S_AFR_DB_HMI_connect.FlapFeedRegister.Set.PosPunch` | mm | 0.45 | module_segment |
| AFR Flap Coil Actual Counter At End ⚠ | `L01S_AFR_DB_HMI_connect.FlapFeedRegister.States.CoilCounter` | - | 0.45 | module_segment |
| AFL Flap Coil Counter To End | `L01S_AFL_DB_setpoint.FlapCoil.CounterToEnd` | - | 0.50 | module_segment |
| AFL Blow Off Punch Time (T05) | `L01S_AFL_DB_setpoint.Times.BlowOffPunchTime` | ms | 0.50 | module_segment |
| AFL Feed Clamp Closing Delay (T06) | `L01S_AFL_DB_setpoint.Times.FeedClampDelay` | ms | 0.50 | module_segment |
| AFL Punch Time (T03) | `L01S_AFL_DB_setpoint.Times.PunchTime` | ms | 0.50 | module_segment |
| AFL Vacuum Load Time (T04) | `L01S_AFL_DB_setpoint.Times.VacLoadTime` | ms | 0.50 | module_segment |
| AFL Actual Cycle Time (T01) | `L01S_AFL_DB_HMI_connect.HMIActualTimes.T01` | ms | 0.50 | module_segment |
| AFR Flap Coil Counter To End | `L01S_AFR_DB_setpoint.FlapCoil.CounterToEnd` | - | 0.50 | module_segment |
| AFR Blow Off Punch Time (T05) | `L01S_AFR_DB_setpoint.Times.BlowOffPunchTime` | ms | 0.50 | module_segment |
| AFR Feed Clamp Closing Delay (T06) | `L01S_AFR_DB_setpoint.Times.FeedClampDelay` | ms | 0.50 | module_segment |
| AFR Punch Time (T03) | `L01S_AFR_DB_setpoint.Times.PunchTime` | ms | 0.50 | module_segment |
| AFR Vacuum Load Time (T04) | `L01S_AFR_DB_setpoint.Times.VacLoadTime` | ms | 0.50 | module_segment |
| AFR Actual Cycle Time (T01) | `L01S_AFR_DB_HMI_connect.HMIActualTimes.T01` | ms | 0.50 | module_segment |
| Flap Seal Time | `MASTER_RECIPE_GENERAL.AF_SEAL_TIME` | ms | 0.55 | module_segment |
| Gap: AF Station to FPWR Inspection | `GE1_DB_setpoint.StationGaps.AF_St_FPWR_Insp` | mm | 0.55 | module_segment |
| AFL Cycle Time Setpoint (T01) | `L01S_AFL_DB_setpoint.Times.CycleTime` | ms | 0.55 | module_segment |
| AFL Welding Time (T02) | `L01S_AFL_DB_setpoint.Times.WeldingTime` | ms | 0.55 | module_segment |
| AFR Cycle Time Setpoint (T01) | `L01S_AFR_DB_setpoint.Times.CycleTime` | ms | 0.55 | module_segment |
| AFR Welding Time (T02) | `L01S_AFR_DB_setpoint.Times.WeldingTime` | ms | 0.55 | module_segment |
| Flap Heat Alarm High | `MASTER_RECIPE_GENERAL.AF_HEAT_ALARM_HIGH` | °C | 0.60 | module_segment |
| Flap Heat Alarm Low | `MASTER_RECIPE_GENERAL.AF_HEAT_ALARM_LOW` | °C | 0.60 | module_segment |
| Flap Heat Tolerance | `MASTER_RECIPE_GENERAL.AF_HEAT_TOL` | °C | 0.60 | module_segment |
| AFL X-Axis Adjust Auto-Correct Setpoint Position | `L01S_AFL_DB_HMI_connect.Adjust_X.AutoCorrectSPPos` | mm | 0.60 | module_segment |
| AFL Y-Axis Adjust Auto-Correct Setpoint Position | `L01S_AFL_DB_HMI_connect.Adjust_Y.AutoCorrectSPPos` | mm | 0.60 | module_segment |
| AFR X-Axis Adjust Auto-Correct Setpoint Position | `L01S_AFR_DB_HMI_connect.Adjust_X.AutoCorrectSPPos` | mm | 0.60 | module_segment |
| AFR Y-Axis Adjust Auto-Correct Setpoint Position | `L01S_AFR_DB_HMI_connect.Adjust_Y.AutoCorrectSPPos` | mm | 0.60 | module_segment |
| Flap Heat Setpoint | `MASTER_RECIPE_GENERAL.AF_HEAT_SP` | °C | 0.65 | module_segment |
| AFL Upper Heater Correction Value | `L01S_AFL_DB_setpoint.HeaterUpper.Correction_Value` | °C | 0.65 | module_segment |
| AFR Upper Heater Correction Value | `L01S_AFR_DB_setpoint.HeaterUpper.Correction_Value` | °C | 0.65 | module_segment |
| AFL Upper Heater Lower Alarm Boundary | `L01S_AFL_DB_setpoint.HeaterUpper.Alarm_Boundary_Down` | °C | 0.70 | module_segment |
| AFL Upper Heater Upper Alarm Boundary | `L01S_AFL_DB_setpoint.HeaterUpper.Alarm_Boundary_Up` | °C | 0.70 | module_segment |
| AFL X-Axis Adjust Actual Position | `L01S_AFL_DB_HMI_connect.Adjust_X.ActPos` | mm | 0.70 | module_segment |
| AFL Y-Axis Adjust Actual Position | `L01S_AFL_DB_HMI_connect.Adjust_Y.ActPos` | mm | 0.70 | module_segment |
| AFR Upper Heater Lower Alarm Boundary | `L01S_AFR_DB_setpoint.HeaterUpper.Alarm_Boundary_Down` | °C | 0.70 | module_segment |
| AFR Upper Heater Upper Alarm Boundary | `L01S_AFR_DB_setpoint.HeaterUpper.Alarm_Boundary_Up` | °C | 0.70 | module_segment |
| AFR X-Axis Adjust Actual Position | `L01S_AFR_DB_HMI_connect.Adjust_X.ActPos` | mm | 0.70 | module_segment |
| AFR Y-Axis Adjust Actual Position | `L01S_AFR_DB_HMI_connect.Adjust_Y.ActPos` | mm | 0.70 | module_segment |
| AFL X-Axis Adjust Offset Position | `L01S_AFL_DB_setpoint.Adujst_X.Offset_Pos` | mm | 0.75 | module_segment |
| AFL X-Axis Adjust Target Position | `L01S_AFL_DB_setpoint.Adujst_X.Target_Pos` | mm | 0.75 | module_segment |
| AFL Y-Axis Adjust Offset Position | `L01S_AFL_DB_setpoint.Adujst_Y.Offset_Pos` | mm | 0.75 | module_segment |
| AFL Y-Axis Adjust Target Position | `L01S_AFL_DB_setpoint.Adujst_Y.Target_Pos` | mm | 0.75 | module_segment |
| AFR X-Axis Adjust Offset Position | `L01S_AFR_DB_setpoint.Adujst_X.Offset_Pos` | mm | 0.75 | module_segment |
| AFR X-Axis Adjust Target Position | `L01S_AFR_DB_setpoint.Adujst_X.Target_Pos` | mm | 0.75 | module_segment |
| AFR Y-Axis Adjust Offset Position | `L01S_AFR_DB_setpoint.Adujst_Y.Offset_Pos` | mm | 0.75 | module_segment |
| AFR Y-Axis Adjust Target Position | `L01S_AFR_DB_setpoint.Adujst_Y.Target_Pos` | mm | 0.75 | module_segment |
| AFL Upper Heater Temperature Setpoint | `L01S_AFL_DB_setpoint.HeaterUpper.Temp_Set` | °C | 0.85 | module_segment |
| AFL Upper Heater Actual Temperature | `L01S_AFL_DB_HMI_connect.HeaterUpper.Status.Actual` | °C | 0.85 | module_segment |
| AFR Upper Heater Temperature Setpoint | `L01S_AFR_DB_setpoint.HeaterUpper.Temp_Set` | °C | 0.85 | module_segment |
| AFR Upper Heater Actual Temperature | `L01S_AFR_DB_HMI_connect.HeaterUpper.Status.Actual` | °C | 0.85 | module_segment |

### VOP viewing-option (vision inspection) station (MC007-VOP)

- 548 candidate tag(s) considered -> 124 kept as genuine parameters (23%).
- Kept tags found by: 124 via *module_segment* (the tag name contains this station's own PLC/module code as a literal segment - the strongest signal available).

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| Gap: VOP Smiley Cut to VOP Smash Seal | `GE1_DB_setpoint.StationGaps.VOP_SmCt_VOP_SmSe` | mm | 0.50 | module_segment |
| Gap: VOP Smash Seal to PRH2 Inspection | `GE1_DB_setpoint.StationGaps.VOP_SmSe_PRH2_Insp` | mm | 0.50 | module_segment |
| Gap: VOP Water Trap to AF Station | `GE1_DB_setpoint.StationGaps.VOP_WaTr_AF_St` | mm | 0.50 | module_segment |
| Gap: VOP Water Trap to VOP Smiley Cut | `GE1_DB_setpoint.StationGaps.VOP_WaTr_VOP_SmCt` | mm | 0.50 | module_segment |
| VOP Counter To Film End - Unwinder Bottom LHS (Setpoint) | `L01S_VOP_DB_setpoint.CounterToEnd.Unwinder_Bottom_LHS` | - | 0.50 | module_segment |
| VOP Counter To Film End - Unwinder Bottom RHS (Setpoint) | `L01S_VOP_DB_setpoint.CounterToEnd.Unwinder_Bottom_RHS` | - | 0.50 | module_segment |
| VOP Counter To Film End - Unwinder Top LHS (Setpoint) | `L01S_VOP_DB_setpoint.CounterToEnd.Unwinder_Top_LHS` | - | 0.50 | module_segment |
| VOP Counter To Film End - Unwinder Top RHS (Setpoint) | `L01S_VOP_DB_setpoint.CounterToEnd.Unwinder_Top_RHS` | - | 0.50 | module_segment |
| VOP Enable Clamp Feed Mechanism (FP07) | `L01S_VOP_DB_setpoint.Selections.FP07` | - | 0.50 | module_segment |
| VOP Smash Seal Enabled (FP04) | `L01S_VOP_DB_setpoint.Selections.SmashSealEnabled` | - | 0.50 | module_segment |
| VOP Smiley Cut Enabled (FP05) | `L01S_VOP_DB_setpoint.Selections.SmileyCutEnabled` | - | 0.50 | module_segment |
| VOP Water Trap Enabled (FP06) | `L01S_VOP_DB_setpoint.Selections.WaterTrapEnabled` | - | 0.50 | module_segment |
| VOP Unwinder LHS Low Speed Setpoint | `L01S_VOP_DB_setpoint.Unwinder_LHS.LowSpeed` | - | 0.50 | module_segment |
| VOP Unwinder RHS Low Speed Setpoint | `L01S_VOP_DB_setpoint.Unwinder_RHS.LowSpeed` | - | 0.50 | module_segment |
| VOP Counter To Film End - Unwinder Bottom LHS (Actual) | `L01S_VOP_DB_HMI_connect.CoilCounter.Unwinder_Bottom_LHS` | - | 0.50 | module_segment |
| VOP Counter To Film End - Unwinder Bottom RHS (Actual) | `L01S_VOP_DB_HMI_connect.CoilCounter.Unwinder_Bottom_RHS` | - | 0.50 | module_segment |
| VOP Counter To Film End - Unwinder Top LHS (Actual) | `L01S_VOP_DB_HMI_connect.CoilCounter.Unwinder_Top_LHS` | - | 0.50 | module_segment |
| VOP Counter To Film End - Unwinder Top RHS (Actual) | `L01S_VOP_DB_HMI_connect.CoilCounter.Unwinder_Top_RHS` | - | 0.50 | module_segment |
| VOP Unwinder Top Active LHS (FP04) | `L01S_VOP_DB_HMI_connect.Selections.FP04` | - | 0.50 | module_segment |
| VOP Unwinder Top Active RHS (FP05) | `L01S_VOP_DB_HMI_connect.Selections.FP05` | - | 0.50 | module_segment |
| VOP Stretching Clamp Enabled (FP06) | `L01S_VOP_DB_HMI_connect.Selections.FP06` | - | 0.50 | module_segment |
| VOP Reinforcement Control Deactivated (FP07) | `L01S_VOP_DB_HMI_connect.Selections.FP07` | - | 0.50 | module_segment |
| VOP Unwinder Turning Direction LHS (FP02) | `L01S_VOP_DB_HMI_connect.Selections.InvDirUw_LHS` | - | 0.50 | module_segment |
| VOP Unwinder Turning Direction RHS (FP03) | `L01S_VOP_DB_HMI_connect.Selections.InvDirUw_RHS` | - | 0.50 | module_segment |
| VOP Operation Mode Semiautomatic (FP01) | `L01S_VOP_DB_HMI_connect.Selections.SemiAuto` | - | 0.50 | module_segment |
| VOP Clamp Feed Enable | `GEN_ADDITIONAL_FUNCTIONS.VOP_CLAMP_FEED_ENABLE` | - | 0.55 | module_segment |
| VOP Film Low Sensor - Unwinder Bottom LHS | `L01S_VOP_DB_HMI_connect.CoilCounter.FilmLow_Bottom_LHS` | - | 0.55 | module_segment |
| VOP Film Low Sensor - Unwinder Bottom RHS | `L01S_VOP_DB_HMI_connect.CoilCounter.FilmLow_Bottom_RHS` | - | 0.55 | module_segment |
| VOP Film Low Sensor - Unwinder Top LHS | `L01S_VOP_DB_HMI_connect.CoilCounter.FilmLow_Top_LHS` | - | 0.55 | module_segment |
| VOP Film Low Sensor - Unwinder Top RHS | `L01S_VOP_DB_HMI_connect.CoilCounter.FilmLow_Top_RHS` | - | 0.55 | module_segment |
| VOP Splice Detected Sensor LHS | `L01S_VOP_DB_HMI_connect.SpliceRegister.SpliceDet_LHS` | - | 0.55 | module_segment |
| VOP Splice Detected Sensor RHS | `L01S_VOP_DB_HMI_connect.SpliceRegister.SpliceDet_RHS` | - | 0.55 | module_segment |
| VOP Splice-to-Weld Distance LHS | `L01S_VOP_DB_setpoint.SpliceRegister.DistToWeld_LHS` | mm | 0.60 | module_segment |
| VOP Splice-to-Weld Distance RHS | `L01S_VOP_DB_setpoint.SpliceRegister.DistToWeld_RHS` | mm | 0.60 | module_segment |
| VOP Delay Cooling Fan On (Actual Time, T22) | `L01S_VOP_DB_HMI_connect.HMIActualTimes.T22` | ms | 0.60 | module_segment |
| VOP Smash Seal Close Delay Time Setpoint (T09) | `L01S_VOP_DB_setpoint.Times._09` | ms | 0.65 | module_segment |
| VOP Smash Seal Heat Alarm High | `MASTER_RECIPE_GENERAL.VOP_SS_HEAT_ALARM_HIGH` | °C | 0.70 | module_segment |
| VOP Smash Seal Heat Alarm Low | `MASTER_RECIPE_GENERAL.VOP_SS_HEAT_ALARM_LOW` | °C | 0.70 | module_segment |
| VOP Water Trap Heat Alarm High | `MASTER_RECIPE_GENERAL.VOP_WT_HEAT_ALARM_HIGH` | °C | 0.70 | module_segment |
| VOP Water Trap Heat Alarm Low | `MASTER_RECIPE_GENERAL.VOP_WT_HEAT_ALARM_LOW` | °C | 0.70 | module_segment |
| VOP Cycle Counter | `L01S_VOP_DB_HMI_connect.Count.CycleCounter` | - | 0.70 | module_segment |
| VOP Smash Seal Heat Tolerance | `MASTER_RECIPE_GENERAL.VOP_SS_HEAT_TOL` | °C | 0.75 | module_segment |
| VOP Smash Seal Time | `MASTER_RECIPE_GENERAL.VOP_SS_SEAL_TIME` | ms | 0.75 | module_segment |
| VOP Water Trap Heat Tolerance | `MASTER_RECIPE_GENERAL.VOP_WT_HEAT_TOL` | °C | 0.75 | module_segment |
| VOP Water Trap Seal Time | `MASTER_RECIPE_GENERAL.VOP_WT_SEAL_TIME` | ms | 0.75 | module_segment |
| VOP Strip Distance Adjust Y LHS Offset Position | `L01S_VOP_DB_setpoint.LHS.StripDistance_Y.Offset_Pos` | mm | 0.75 | module_segment |
| VOP Strip Distance Adjust Y LHS Target Position | `L01S_VOP_DB_setpoint.LHS.StripDistance_Y.Target_Pos` | mm | 0.75 | module_segment |
| VOP Lower Clamp Feed Gearing Factor Sync | `L01S_VOP_DB_setpoint.LowerClampFeed.GearingFactorSync` | % | 0.75 | module_segment |
| VOP Strip Distance Adjust Y RHS Offset Position | `L01S_VOP_DB_setpoint.RHS.StripDistance_Y.Offset_Pos` | mm | 0.75 | module_segment |
| VOP Strip Distance Adjust Y RHS Target Position | `L01S_VOP_DB_setpoint.RHS.StripDistance_Y.Target_Pos` | mm | 0.75 | module_segment |
| VOP Cycle Time Setpoint (T01) | `L01S_VOP_DB_setpoint.Times.CycleTime` | ms | 0.75 | module_segment |
| VOP Smiley Cut Punch Time Setpoint (T04) | `L01S_VOP_DB_setpoint.Times.PunchSmileyCutTime` | ms | 0.75 | module_segment |
| VOP Smash Seal Welding Time LHS Setpoint (T02) | `L01S_VOP_DB_setpoint.Times.WeldingSmashSealTimeLHS` | ms | 0.75 | module_segment |
| VOP Smash Seal Welding Time RHS Setpoint (T03) | `L01S_VOP_DB_setpoint.Times.WeldingSmashSealTimeRHS` | ms | 0.75 | module_segment |
| VOP Water Trap Welding Time LHS Setpoint (T05) | `L01S_VOP_DB_setpoint.Times.WeldingWaterTrapTimeLHS` | ms | 0.75 | module_segment |
| VOP Water Trap Welding Time RHS Setpoint (T06) | `L01S_VOP_DB_setpoint.Times.WeldingWaterTrapTimeRHS` | ms | 0.75 | module_segment |
| VOP Actual Cycle Time (T01) | `L01S_VOP_DB_HMI_connect.HMIActualTimes.T01` | ms | 0.75 | module_segment |
| VOP Strip Distance Adjust Y LHS Actual Position | `L01S_VOP_DB_HMI_connect.LHS.StripDistance_Y.ActPos` | mm | 0.75 | module_segment |
| VOP Strip Distance Adjust Y RHS Actual Position | `L01S_VOP_DB_HMI_connect.RHS.StripDistance_Y.ActPos` | mm | 0.75 | module_segment |
| VOP Smash Seal Heat Setpoint | `MASTER_RECIPE_GENERAL.VOP_SS_HEAT_SP` | °C | 0.80 | module_segment |
| VOP Water Trap Heat Setpoint | `MASTER_RECIPE_GENERAL.VOP_WT_HEAT_SP` | °C | 0.80 | module_segment |
| VOP Fife Web1 Adjust Offset Position | `L01S_VOP_DB_setpoint.Adjust_VOP_Fife_Web_1.Offset_Pos` | mm | 0.80 | module_segment |
| VOP Fife Web1 Adjust Target Position | `L01S_VOP_DB_setpoint.Adjust_VOP_Fife_Web_1.Target_Pos` | mm | 0.80 | module_segment |
| VOP Smash Seal Heater LHS Correction Value | `L01S_VOP_DB_setpoint.HeaterSmashLHS.Correction_Value` | 1/10 °K | 0.80 | module_segment |
| VOP Smash Seal Heater RHS Correction Value | `L01S_VOP_DB_setpoint.HeaterSmashRHS.Correction_Value` | 1/10 °K | 0.80 | module_segment |
| VOP Water Trap Heater LHS Correction Value | `L01S_VOP_DB_setpoint.HeaterTrapLHS.Correction_Value` | 1/10 °K | 0.80 | module_segment |
| VOP Water Trap Heater RHS Correction Value | `L01S_VOP_DB_setpoint.HeaterTrapRHS.Correction_Value` | 1/10 °K | 0.80 | module_segment |
| VOP Smash Seal Adjust Y LHS Offset Position | `L01S_VOP_DB_setpoint.LHS.SmashSealAdjust_Y.Offset_Pos` | mm | 0.80 | module_segment |
| VOP Smash Seal Adjust Y LHS Target Position | `L01S_VOP_DB_setpoint.LHS.SmashSealAdjust_Y.Target_Pos` | mm | 0.80 | module_segment |
| VOP Smiley Cut Adjust Y LHS Offset Position | `L01S_VOP_DB_setpoint.LHS.SmileyCutAdjust_Y.Offset_Pos` | mm | 0.80 | module_segment |
| VOP Smiley Cut Adjust Y LHS Target Position | `L01S_VOP_DB_setpoint.LHS.SmileyCutAdjust_Y.Target_Pos` | mm | 0.80 | module_segment |
| VOP Water Trap Adjust Y LHS Offset Position | `L01S_VOP_DB_setpoint.LHS.WaterTrapAdjust_Y.Offset_Pos` | mm | 0.80 | module_segment |
| VOP Water Trap Adjust Y LHS Target Position | `L01S_VOP_DB_setpoint.LHS.WaterTrapAdjust_Y.Target_Pos` | mm | 0.80 | module_segment |
| VOP Welding Belt Adjust Y LHS Offset Position | `L01S_VOP_DB_setpoint.LHS.WeldingBeltAdjust_Y.Offset_Pos` | mm | 0.80 | module_segment |
| VOP Welding Belt Adjust Y LHS Target Position | `L01S_VOP_DB_setpoint.LHS.WeldingBeltAdjust_Y.Target_Pos` | mm | 0.80 | module_segment |
| VOP Lower Clamp Feed Backward Acceleration | `L01S_VOP_DB_setpoint.LowerClampFeed.Backward.Acc` | % | 0.80 | module_segment |
| VOP Lower Clamp Feed Backward Deceleration | `L01S_VOP_DB_setpoint.LowerClampFeed.Backward.Dec` | % | 0.80 | module_segment |
| VOP Lower Clamp Feed Backward Target Position | `L01S_VOP_DB_setpoint.LowerClampFeed.Backward.Position` | mm | 0.80 | module_segment |
| VOP Lower Clamp Feed Backward Velocity | `L01S_VOP_DB_setpoint.LowerClampFeed.Backward.Velocity` | % | 0.80 | module_segment |
| VOP Lower Clamp Feed Forward Target Position | `L01S_VOP_DB_setpoint.LowerClampFeed.Forward.Position` | mm | 0.80 | module_segment |
| VOP Smash Seal Adjust Y RHS Offset Position | `L01S_VOP_DB_setpoint.RHS.SmashSealAdjust_Y.Offset_Pos` | mm | 0.80 | module_segment |
| VOP Smash Seal Adjust Y RHS Target Position | `L01S_VOP_DB_setpoint.RHS.SmashSealAdjust_Y.Target_Pos` | mm | 0.80 | module_segment |
| VOP Smiley Cut Adjust Y RHS Offset Position | `L01S_VOP_DB_setpoint.RHS.SmileyCutAdjust_Y.Offset_Pos` | mm | 0.80 | module_segment |
| VOP Smiley Cut Adjust Y RHS Target Position | `L01S_VOP_DB_setpoint.RHS.SmileyCutAdjust_Y.Target_Pos` | mm | 0.80 | module_segment |
| VOP Water Trap Adjust Y RHS Offset Position | `L01S_VOP_DB_setpoint.RHS.WaterTrapAdjust_Y.Offset_Pos` | mm | 0.80 | module_segment |
| VOP Water Trap Adjust Y RHS Target Position | `L01S_VOP_DB_setpoint.RHS.WaterTrapAdjust_Y.Target_Pos` | mm | 0.80 | module_segment |
| VOP Welding Belt Adjust Y RHS Offset Position | `L01S_VOP_DB_setpoint.RHS.WeldingBeltAdjust_Y.Offset_Pos` | mm | 0.80 | module_segment |
| VOP Welding Belt Adjust Y RHS Target Position | `L01S_VOP_DB_setpoint.RHS.WeldingBeltAdjust_Y.Target_Pos` | mm | 0.80 | module_segment |
| VOP Smash Seal Adjust X Offset Position | `L01S_VOP_DB_setpoint.SmashSealAdjust_X.Offset_Pos` | mm | 0.80 | module_segment |
| VOP Smash Seal Adjust X Target Position | `L01S_VOP_DB_setpoint.SmashSealAdjust_X.Target_Pos` | mm | 0.80 | module_segment |
| VOP Smiley Cut Adjust X Offset Position | `L01S_VOP_DB_setpoint.SmileyCutAdjust_X.Offset_Pos` | mm | 0.80 | module_segment |
| VOP Smiley Cut Adjust X Target Position | `L01S_VOP_DB_setpoint.SmileyCutAdjust_X.Target_Pos` | mm | 0.80 | module_segment |
| VOP Water Trap Adjust X Offset Position | `L01S_VOP_DB_setpoint.WaterTrapAdjust_X.Offset_Pos` | mm | 0.80 | module_segment |
| VOP Water Trap Adjust X Target Position | `L01S_VOP_DB_setpoint.WaterTrapAdjust_X.Target_Pos` | mm | 0.80 | module_segment |
| VOP Fife Web1 Adjust Actual Position | `L01S_VOP_DB_HMI_connect.Adjust_VOP_Fife_Web_1.ActPos` | mm | 0.80 | module_segment |
| VOP Smash Seal Adjust Y LHS Actual Position | `L01S_VOP_DB_HMI_connect.LHS.SmashSealAdjust_Y.ActPos` | mm | 0.80 | module_segment |
| VOP Smiley Cut Adjust Y LHS Actual Position | `L01S_VOP_DB_HMI_connect.LHS.SmileyCutAdjust_Y.ActPos` | mm | 0.80 | module_segment |
| VOP Water Trap Adjust Y LHS Actual Position | `L01S_VOP_DB_HMI_connect.LHS.WaterTrapAdjust_Y.ActPos` | mm | 0.80 | module_segment |
| VOP Welding Belt Adjust Y LHS Actual Position | `L01S_VOP_DB_HMI_connect.LHS.WeldingBeltAdjust_Y.ActPos` | mm | 0.80 | module_segment |
| VOP Lower Clamp Feed Actual Position | `L01S_VOP_DB_HMI_connect.LowerClampFeed.ActPos` | mm | 0.80 | module_segment |
| VOP Lower Clamp Feed Target Position | `L01S_VOP_DB_HMI_connect.LowerClampFeed.TargetPos` | mm | 0.80 | module_segment |
| VOP Smash Seal Adjust Y RHS Actual Position | `L01S_VOP_DB_HMI_connect.RHS.SmashSealAdjust_Y.ActPos` | mm | 0.80 | module_segment |
| VOP Smiley Cut Adjust Y RHS Actual Position | `L01S_VOP_DB_HMI_connect.RHS.SmileyCutAdjust_Y.ActPos` | mm | 0.80 | module_segment |
| VOP Water Trap Adjust Y RHS Actual Position | `L01S_VOP_DB_HMI_connect.RHS.WaterTrapAdjust_Y.ActPos` | mm | 0.80 | module_segment |
| VOP Welding Belt Adjust Y RHS Actual Position | `L01S_VOP_DB_HMI_connect.RHS.WeldingBeltAdjust_Y.ActPos` | mm | 0.80 | module_segment |
| VOP Smash Seal Adjust X Actual Position | `L01S_VOP_DB_HMI_connect.SmashSealAdjust_X.ActPos` | mm | 0.80 | module_segment |
| VOP Smiley Cut Adjust X Actual Position | `L01S_VOP_DB_HMI_connect.SmileyCutAdjust_X.ActPos` | mm | 0.80 | module_segment |
| VOP Water Trap Adjust X Actual Position | `L01S_VOP_DB_HMI_connect.WaterTrapAdjust_X.ActPos` | mm | 0.80 | module_segment |
| VOP Smash Seal Heater LHS Lower Alarm Boundary | `L01S_VOP_DB_setpoint.HeaterSmashLHS.Alarm_Boundary_Down` | 1/10 °C | 0.85 | module_segment |
| VOP Smash Seal Heater LHS Upper Alarm Boundary | `L01S_VOP_DB_setpoint.HeaterSmashLHS.Alarm_Boundary_Up` | 1/10 °C | 0.85 | module_segment |
| VOP Smash Seal Heater RHS Lower Alarm Boundary | `L01S_VOP_DB_setpoint.HeaterSmashRHS.Alarm_Boundary_Down` | 1/10 °C | 0.85 | module_segment |
| VOP Smash Seal Heater RHS Upper Alarm Boundary | `L01S_VOP_DB_setpoint.HeaterSmashRHS.Alarm_Boundary_Up` | 1/10 °C | 0.85 | module_segment |
| VOP Water Trap Heater LHS Lower Alarm Boundary | `L01S_VOP_DB_setpoint.HeaterTrapLHS.Alarm_Boundary_Down` | 1/10 °C | 0.85 | module_segment |
| VOP Water Trap Heater LHS Upper Alarm Boundary | `L01S_VOP_DB_setpoint.HeaterTrapLHS.Alarm_Boundary_Up` | 1/10 °C | 0.85 | module_segment |
| VOP Water Trap Heater RHS Lower Alarm Boundary | `L01S_VOP_DB_setpoint.HeaterTrapRHS.Alarm_Boundary_Down` | 1/10 °C | 0.85 | module_segment |
| VOP Water Trap Heater RHS Upper Alarm Boundary | `L01S_VOP_DB_setpoint.HeaterTrapRHS.Alarm_Boundary_Up` | 1/10 °C | 0.85 | module_segment |
| VOP Smash Seal Heater LHS Temperature Setpoint | `L01S_VOP_DB_setpoint.HeaterSmashLHS.Temp_Set` | 1/10 °C | 0.90 | module_segment |
| VOP Smash Seal Heater RHS Temperature Setpoint | `L01S_VOP_DB_setpoint.HeaterSmashRHS.Temp_Set` | 1/10 °C | 0.90 | module_segment |
| VOP Water Trap Heater LHS Temperature Setpoint | `L01S_VOP_DB_setpoint.HeaterTrapLHS.Temp_Set` | 1/10 °C | 0.90 | module_segment |
| VOP Water Trap Heater RHS Temperature Setpoint | `L01S_VOP_DB_setpoint.HeaterTrapRHS.Temp_Set` | 1/10 °C | 0.90 | module_segment |
| VOP Smash Seal Heater LHS Actual Temperature | `L01S_VOP_DB_HMI_connect.HeaterSmashLHS.Status.Actual` | °C | 0.90 | module_segment |
| VOP Smash Seal Heater RHS Actual Temperature | `L01S_VOP_DB_HMI_connect.HeaterSmashRHS.Status.Actual` | °C | 0.90 | module_segment |
| VOP Water Trap Heater LHS Actual Temperature | `L01S_VOP_DB_HMI_connect.HeaterTrapLHS.Status.Actual` | °C | 0.90 | module_segment |
| VOP Water Trap Heater RHS Actual Temperature | `L01S_VOP_DB_HMI_connect.HeaterTrapRHS.Status.Actual` | °C | 0.90 | module_segment |

### PWC periphery welding station (MC007-PWC)

- 198 candidate tag(s) considered -> 44 kept as genuine parameters (22%).
- Kept tags found by: 44 via *module_segment* (the tag name contains this station's own PLC/module code as a literal segment - the strongest signal available).
- 4 kept parameter(s) below 0.5 confidence - flagged with ⚠ below.

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| PWC Lower Heater PID Output ⚠ | `L01S_PWC_DB_HMI_connect.HeaterLower.Status.LMN` | % | 0.40 | module_segment |
| PWC Upper Heater PID Output ⚠ | `L01S_PWC_DB_HMI_connect.HeaterUpper.Status.LMN` | % | 0.40 | module_segment |
| PWC Cycle Counter ⚠ | `L01S_PWC_DB_HMI_connect.Count.CycleCounter` | - | 0.45 | module_segment |
| PWC Cooling Fan On Delay (T22) ⚠ | `L01S_PWC_DB_HMI_connect.HMIActualTimes.T22` | ms | 0.45 | module_segment |
| PWC Gripper Feed Back Stroke Delay (T04) | `L01S_PWC_DB_setpoint.Times._04` | ms | 0.50 | module_segment |
| PWC Magnetic Clutch Close Delay (T05) | `L01S_PWC_DB_setpoint.Times._05` | ms | 0.50 | module_segment |
| PWC Actual Cycle Time (T01) | `L01S_PWC_DB_HMI_connect.HMIActualTimes.T01` | ms | 0.50 | module_segment |
| Gap: PT1 Station to PWC Station | `GE1_DB_setpoint.StationGaps.PT1_St_PWC_St` | mm | 0.55 | module_segment |
| Gap: PWC Station to AF Station | `GE1_DB_setpoint.StationGaps.PWC_St_AF_St` | mm | 0.55 | module_segment |
| Gap: PWC Station to FWC Inspection | `GE1_DB_setpoint.StationGaps.PWC_St_FWC_Insp` | mm | 0.55 | module_segment |
| Gap: PWC Station to VOP Water Trap | `GE1_DB_setpoint.StationGaps.PWC_St_VOP_WaTr` | mm | 0.55 | module_segment |
| PWC Cycle Time Setpoint (T01) | `L01S_PWC_DB_setpoint.Times.CycleTime` | ms | 0.55 | module_segment |
| PWC Welding Time (T02) | `L01S_PWC_DB_setpoint.Times.WeldingTime` | ms | 0.55 | module_segment |
| PWC Welding Top Relative Controller Range Position | `L01S_PWC_DB_setpoint.WeldingTop.Pos_RelController` | mm | 0.55 | module_segment |
| PWC Welding Top Relative Foil Release Position | `L01S_PWC_DB_setpoint.WeldingTop.Pos_RelFoil` | mm | 0.55 | module_segment |
| PWC Welding Top Tool Change Position | `L01S_PWC_DB_setpoint.WeldingTop.Pos_ToolChange` | mm | 0.55 | module_segment |
| PWC Weld Curve Force (Top Table) | `L01S_PWC_DB_weldcurves.Curves.Force` | N | 0.55 | module_segment |
| PWC Weld Curve Position (Top Table) | `L01S_PWC_DB_weldcurves.Curves.Position` | mm | 0.55 | module_segment |
| PWC Cooling Plate Temperature | `GE1_DB_interface.PWC_COMMUNICATION._FROM.TempCoolingPlate` | °C | 0.60 | module_segment |
| PWC Welding Top Maximum Position | `L01S_PWC_DB_setpoint.WeldingTop.Pos_Max` | mm | 0.60 | module_segment |
| PWC Welding Top Open Position | `L01S_PWC_DB_setpoint.WeldingTop.Pos_Open` | mm | 0.60 | module_segment |
| PWC Welding Top Actual Load Cell | `L01S_PWC_DB_HMI_connect.WeldingTop.LoadCell` | % | 0.60 | module_segment |
| PWC Lower Heater Correction Value | `L01S_PWC_DB_setpoint.HeaterLower.Correction_Value` | °C | 0.65 | module_segment |
| PWC Upper Heater Correction Value | `L01S_PWC_DB_setpoint.HeaterUpper.Correction_Value` | °C | 0.65 | module_segment |
| PWC Lower Heater Lower Alarm Boundary | `L01S_PWC_DB_setpoint.HeaterLower.Alarm_Boundary_Down` | °C | 0.70 | module_segment |
| PWC Lower Heater Upper Alarm Boundary | `L01S_PWC_DB_setpoint.HeaterLower.Alarm_Boundary_Up` | °C | 0.70 | module_segment |
| PWC Upper Heater Lower Alarm Boundary | `L01S_PWC_DB_setpoint.HeaterUpper.Alarm_Boundary_Down` | °C | 0.70 | module_segment |
| PWC Upper Heater Upper Alarm Boundary | `L01S_PWC_DB_setpoint.HeaterUpper.Alarm_Boundary_Up` | °C | 0.70 | module_segment |
| PWC Welding Top Lower Force Alarm Boundary | `L01S_PWC_DB_setpoint.WeldingTop.Alarm_Boundary_Down` | kN | 0.70 | module_segment |
| PWC Welding Top Upper Force Alarm Boundary | `L01S_PWC_DB_setpoint.WeldingTop.Alarm_Boundary_Up` | kN | 0.70 | module_segment |
| PWC X-Axis Adjust Actual Position | `L01S_PWC_DB_HMI_connect.Adjust_X.ActPos` | mm | 0.70 | module_segment |
| PWC Y-Axis Adjust Actual Position | `L01S_PWC_DB_HMI_connect.Adjust_Y.ActPos` | mm | 0.70 | module_segment |
| PWC X-Axis Adjust Offset Position | `L01S_PWC_DB_setpoint.Adjust_X.Offset_Pos` | mm | 0.75 | module_segment |
| PWC X-Axis Adjust Target Position | `L01S_PWC_DB_setpoint.Adjust_X.Target_Pos` | mm | 0.75 | module_segment |
| PWC Y-Axis Adjust Offset Position | `L01S_PWC_DB_setpoint.Adjust_Y.Offset_Pos` | mm | 0.75 | module_segment |
| PWC Y-Axis Adjust Target Position | `L01S_PWC_DB_setpoint.Adjust_Y.Target_Pos` | mm | 0.75 | module_segment |
| PWC Welding Top Actual Position | `L01S_PWC_DB_HMI_connect.WeldingTop.ActPos` | mm | 0.75 | module_segment |
| PWC Welding Top Target Position | `L01S_PWC_DB_HMI_connect.WeldingTop.TargetPos` | mm | 0.75 | module_segment |
| PWC Lower Heater Temperature Setpoint | `L01S_PWC_DB_setpoint.HeaterLower.Temp_Set` | °C | 0.85 | module_segment |
| PWC Upper Heater Temperature Setpoint | `L01S_PWC_DB_setpoint.HeaterUpper.Temp_Set` | °C | 0.85 | module_segment |
| PWC Welding Top Target Force | `L01S_PWC_DB_setpoint.WeldingTop.Force` | kN | 0.85 | module_segment |
| PWC Lower Heater Actual Temperature | `L01S_PWC_DB_HMI_connect.HeaterLower.Status.Actual` | °C | 0.85 | module_segment |
| PWC Upper Heater Actual Temperature | `L01S_PWC_DB_HMI_connect.HeaterUpper.Status.Actual` | °C | 0.85 | module_segment |
| PWC Welding Top Actual Force | `L01S_PWC_DB_HMI_connect.WeldingTop.ActForce` | N | 0.85 | module_segment |

### ASC labelling station, curved closure, post-heating (MC007-ASC)

- 526 candidate tag(s) considered -> 105 kept as genuine parameters (20%).
- Kept tags found by: 105 via *module_segment* (the tag name contains this station's own PLC/module code as a literal segment - the strongest signal available).
- 10 kept parameter(s) below 0.5 confidence - flagged with ⚠ below.

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| ASCL Bottom Heater PID Output ⚠ | `L01S_ASCL_DB_HMI_connect.HeaterBottom.Status.LMN` | % | 0.40 | module_segment |
| ASCL Top Heater PID Output ⚠ | `L01S_ASCL_DB_HMI_connect.HeaterTop.Status.LMN` | % | 0.40 | module_segment |
| ASCR Bottom Heater PID Output ⚠ | `L01S_ASCR_DB_HMI_connect.HeaterBottom.Status.LMN` | % | 0.40 | module_segment |
| ASCR Top Heater PID Output ⚠ | `L01S_ASCR_DB_HMI_connect.HeaterTop.Status.LMN` | % | 0.40 | module_segment |
| ASCL Coil Counter Actual (Down) ⚠ | `L01S_ASCL_DB_HMI_connect.CoilCounter.CoilCounter_Uown` | - | 0.45 | module_segment |
| ASCL Coil Counter Actual (Up) ⚠ | `L01S_ASCL_DB_HMI_connect.CoilCounter.CoilCounter_Up` | - | 0.45 | module_segment |
| ASCL Cycle Counter ⚠ | `L01S_ASCL_DB_HMI_connect.Count.CycleCounter` | - | 0.45 | module_segment |
| ASCR Coil Counter Actual (Down) ⚠ | `L01S_ASCR_DB_HMI_connect.CoilCounter.CoilCounter_Uown` | - | 0.45 | module_segment |
| ASCR Coil Counter Actual (Up) ⚠ | `L01S_ASCR_DB_HMI_connect.CoilCounter.CoilCounter_Up` | - | 0.45 | module_segment |
| ASCR Cycle Counter ⚠ | `L01S_ASCR_DB_HMI_connect.Count.CycleCounter` | - | 0.45 | module_segment |
| Gap: ASC Preheat to ASC Station | `GE1_DB_setpoint.StationGaps.ASC_Pht_ASC_St` | mm | 0.50 | module_segment |
| Gap: ASC Station to ASB Station | `GE1_DB_setpoint.StationGaps.ASC_St_ASB_St` | mm | 0.50 | module_segment |
| ASCL Coil Counter To End (Down) | `L01S_ASCL_DB_setpoint.CoilCounter.CounterToEnd_Down` | - | 0.50 | module_segment |
| ASCL Coil Counter To End (Up) | `L01S_ASCL_DB_setpoint.CoilCounter.CounterToEnd_Up` | - | 0.50 | module_segment |
| ASCL Labeler Type Selection | `L01S_ASCL_DB_setpoint.Labeler.LType` | - | 0.50 | module_segment |
| ASCL Heating Time (T02) | `L01S_ASCL_DB_setpoint.Times._02` | ms | 0.50 | module_segment |
| ASCL Actual Cycle Time (T01) | `L01S_ASCL_DB_HMI_connect.HMIActualTimes.T01` | ms | 0.50 | module_segment |
| ASCR Coil Counter To End (Down) | `L01S_ASCR_DB_setpoint.CoilCounter.CounterToEnd_Down` | - | 0.50 | module_segment |
| ASCR Coil Counter To End (Up) | `L01S_ASCR_DB_setpoint.CoilCounter.CounterToEnd_Up` | - | 0.50 | module_segment |
| ASCR Labeler Type Selection | `L01S_ASCR_DB_setpoint.Labeler.LType` | - | 0.50 | module_segment |
| ASCR Heating Time (T02) | `L01S_ASCR_DB_setpoint.Times._02` | ms | 0.50 | module_segment |
| ASCR Actual Cycle Time (T01) | `L01S_ASCR_DB_HMI_connect.HMIActualTimes.T01` | ms | 0.50 | module_segment |
| ASC Seal Time | `MASTER_RECIPE_GENERAL.ASC_SEAL_TIME` | ms | 0.55 | module_segment |
| ASCL Cycle Time Setpoint (T01) | `L01S_ASCL_DB_setpoint.Times.CycleTime` | ms | 0.55 | module_segment |
| ASCR Cycle Time Setpoint (T01) | `L01S_ASCR_DB_setpoint.Times.CycleTime` | ms | 0.55 | module_segment |
| ASC Heat Alarm High | `MASTER_RECIPE_GENERAL.ASC_HEAT_ALARM_HIGH` | °C | 0.60 | module_segment |
| ASC Heat Alarm Low | `MASTER_RECIPE_GENERAL.ASC_HEAT_ALARM_LOW` | °C | 0.60 | module_segment |
| ASC Heat Tolerance | `MASTER_RECIPE_GENERAL.ASC_HEAT_TOL` | °C | 0.60 | module_segment |
| ASCL Adjust X Bottom Actual Position | `SIKO_ASCL Adjust X Btm.Actual_Position_mm_unit` | mm | 0.60 | module_segment |
| ASCL Adjust X Bottom Target Position | `SIKO_ASCL Adjust X Btm.Target_Position_mm` | mm | 0.60 | module_segment |
| ASCL Adjust X Top Actual Position | `SIKO_ASCL Adjust X Top.Actual_Position_mm_unit` | mm | 0.60 | module_segment |
| ASCL Adjust X Top Target Position | `SIKO_ASCL Adjust X Top.Target_Position_mm` | mm | 0.60 | module_segment |
| ASCL Adjust Y Bottom Actual Position | `SIKO_ASCL Adjust Y Btm.Actual_Position_mm_unit` | mm | 0.60 | module_segment |
| ASCL Adjust Y Bottom Target Position | `SIKO_ASCL Adjust Y Btm.Target_Position_mm` | mm | 0.60 | module_segment |
| ASCL Adjust Y Top Actual Position | `SIKO_ASCL Adjust Y Top.Actual_Position_mm_unit` | mm | 0.60 | module_segment |
| ASCL Adjust Y Top Target Position | `SIKO_ASCL Adjust Y Top.Target_Position_mm` | mm | 0.60 | module_segment |
| ASCL Camera Adjust X Actual Position | `SIKO_ASCL Camera Adj X.Actual_Position_mm_unit` | mm | 0.60 | module_segment |
| ASCL Camera Adjust X Target Position | `SIKO_ASCL Camera Adj X.Target_Position_mm` | mm | 0.60 | module_segment |
| ASCL Camera Adjust Y Actual Position | `SIKO_ASCL Camera Adj Y.Actual_Position_mm_unit` | mm | 0.60 | module_segment |
| ASCL Camera Adjust Y Target Position | `SIKO_ASCL Camera Adj Y.Target_Position_mm` | mm | 0.60 | module_segment |
| ASCR Adjust X Bottom Actual Position | `SIKO_ASCR Adjust X Btm.Actual_Position_mm_unit` | mm | 0.60 | module_segment |
| ASCR Adjust X Bottom Target Position | `SIKO_ASCR Adjust X Btm.Target_Position_mm` | mm | 0.60 | module_segment |
| ASCR Adjust X Top Actual Position | `SIKO_ASCR Adjust X Top.Actual_Position_mm_unit` | mm | 0.60 | module_segment |
| ASCR Adjust X Top Target Position | `SIKO_ASCR Adjust X Top.Target_Position_mm` | mm | 0.60 | module_segment |
| ASCR Adjust Y Bottom Actual Position | `SIKO_ASCR Adjust Y Btm.Actual_Position_mm_unit` | mm | 0.60 | module_segment |
| ASCR Adjust Y Bottom Target Position | `SIKO_ASCR Adjust Y Btm.Target_Position_mm` | mm | 0.60 | module_segment |
| ASCR Adjust Y Top Actual Position | `SIKO_ASCR Adjust Y Top.Actual_Position_mm_unit` | mm | 0.60 | module_segment |
| ASCR Adjust Y Top Target Position | `SIKO_ASCR Adjust Y Top.Target_Position_mm` | mm | 0.60 | module_segment |
| ASCR Camera Adjust X Actual Position | `SIKO_ASCR Camera Adj X.Actual_Position_mm_unit` | mm | 0.60 | module_segment |
| ASCR Camera Adjust X Target Position | `SIKO_ASCR Camera Adj X.Target_Position_mm` | mm | 0.60 | module_segment |
| ASCR Camera Adjust Y Actual Position | `SIKO_ASCR Camera Adj Y.Actual_Position_mm_unit` | mm | 0.60 | module_segment |
| ASCR Camera Adjust Y Target Position | `SIKO_ASCR Camera Adj Y.Target_Position_mm` | mm | 0.60 | module_segment |
| ASCL X-Axis Lower Adjust Auto-Correct Setpoint Position | `L01S_ASCL_DB_HMI_connect.x_adjust_lwr.AutoCorrectSPPos` | mm | 0.60 | module_segment |
| ASCL X-Axis Upper Adjust Auto-Correct Setpoint Position | `L01S_ASCL_DB_HMI_connect.x_adjust_up.AutoCorrectSPPos` | mm | 0.60 | module_segment |
| ASCL Y-Axis Lower Adjust Auto-Correct Setpoint Position | `L01S_ASCL_DB_HMI_connect.y_adjust_lwr.AutoCorrectSPPos` | mm | 0.60 | module_segment |
| ASCL Y-Axis Upper Adjust Auto-Correct Setpoint Position | `L01S_ASCL_DB_HMI_connect.y_adjust_up.AutoCorrectSPPos` | mm | 0.60 | module_segment |
| ASCR X-Axis Lower Adjust Auto-Correct Setpoint Position | `L01S_ASCR_DB_HMI_connect.x_adjust_lwr.AutoCorrectSPPos` | mm | 0.60 | module_segment |
| ASCR X-Axis Upper Adjust Auto-Correct Setpoint Position | `L01S_ASCR_DB_HMI_connect.x_adjust_up.AutoCorrectSPPos` | mm | 0.60 | module_segment |
| ASCR Y-Axis Lower Adjust Auto-Correct Setpoint Position | `L01S_ASCR_DB_HMI_connect.y_adjust_lwr.AutoCorrectSPPos` | mm | 0.60 | module_segment |
| ASCR Y-Axis Upper Adjust Auto-Correct Setpoint Position | `L01S_ASCR_DB_HMI_connect.y_adjust_up.AutoCorrectSPPos` | mm | 0.60 | module_segment |
| ASC Heat Setpoint | `MASTER_RECIPE_GENERAL.ASC_HEAT_SP` | °C | 0.65 | module_segment |
| ASCL Bottom Heater Correction Value | `L01S_ASCL_DB_setpoint.HeaterBottom.Correction_Value` | °C | 0.65 | module_segment |
| ASCL Top Heater Correction Value | `L01S_ASCL_DB_setpoint.HeaterTop.Correction_Value` | °C | 0.65 | module_segment |
| ASCR Bottom Heater Correction Value | `L01S_ASCR_DB_setpoint.HeaterBottom.Correction_Value` | °C | 0.65 | module_segment |
| ASCR Top Heater Correction Value | `L01S_ASCR_DB_setpoint.HeaterTop.Correction_Value` | °C | 0.65 | module_segment |
| ASCL Bottom Heater Lower Alarm Boundary | `L01S_ASCL_DB_setpoint.HeaterBottom.Alarm_Boundary_Down` | °C | 0.70 | module_segment |
| ASCL Bottom Heater Upper Alarm Boundary | `L01S_ASCL_DB_setpoint.HeaterBottom.Alarm_Boundary_Up` | °C | 0.70 | module_segment |
| ASCL Top Heater Lower Alarm Boundary | `L01S_ASCL_DB_setpoint.HeaterTop.Alarm_Boundary_Down` | °C | 0.70 | module_segment |
| ASCL Top Heater Upper Alarm Boundary | `L01S_ASCL_DB_setpoint.HeaterTop.Alarm_Boundary_Up` | °C | 0.70 | module_segment |
| ASCL X-Axis Lower Adjust Offset Position | `L01S_ASCL_DB_setpoint.x_adjust_lwr.Offset_Pos` | mm | 0.70 | module_segment |
| ASCL X-Axis Lower Adjust Target Position | `L01S_ASCL_DB_setpoint.x_adjust_lwr.Target_Pos` | mm | 0.70 | module_segment |
| ASCL X-Axis Upper Adjust Offset Position | `L01S_ASCL_DB_setpoint.x_adjust_up.Offset_Pos` | mm | 0.70 | module_segment |
| ASCL X-Axis Upper Adjust Target Position | `L01S_ASCL_DB_setpoint.x_adjust_up.Target_Pos` | mm | 0.70 | module_segment |
| ASCL Y-Axis Lower Adjust Offset Position | `L01S_ASCL_DB_setpoint.y_adjust_lwr.Offset_Pos` | mm | 0.70 | module_segment |
| ASCL Y-Axis Lower Adjust Target Position | `L01S_ASCL_DB_setpoint.y_adjust_lwr.Target_Pos` | mm | 0.70 | module_segment |
| ASCL Y-Axis Upper Adjust Offset Position | `L01S_ASCL_DB_setpoint.y_adjust_up.Offset_Pos` | mm | 0.70 | module_segment |
| ASCL Y-Axis Upper Adjust Target Position | `L01S_ASCL_DB_setpoint.y_adjust_up.Target_Pos` | mm | 0.70 | module_segment |
| ASCL X-Axis Lower Adjust Actual Position | `L01S_ASCL_DB_HMI_connect.x_adjust_lwr.ActPos` | mm | 0.70 | module_segment |
| ASCL X-Axis Upper Adjust Actual Position | `L01S_ASCL_DB_HMI_connect.x_adjust_up.ActPos` | mm | 0.70 | module_segment |
| ASCL Y-Axis Lower Adjust Actual Position | `L01S_ASCL_DB_HMI_connect.y_adjust_lwr.ActPos` | mm | 0.70 | module_segment |
| ASCL Y-Axis Upper Adjust Actual Position | `L01S_ASCL_DB_HMI_connect.y_adjust_up.ActPos` | mm | 0.70 | module_segment |
| ASCR Bottom Heater Lower Alarm Boundary | `L01S_ASCR_DB_setpoint.HeaterBottom.Alarm_Boundary_Down` | °C | 0.70 | module_segment |
| ASCR Bottom Heater Upper Alarm Boundary | `L01S_ASCR_DB_setpoint.HeaterBottom.Alarm_Boundary_Up` | °C | 0.70 | module_segment |
| ASCR Top Heater Lower Alarm Boundary | `L01S_ASCR_DB_setpoint.HeaterTop.Alarm_Boundary_Down` | °C | 0.70 | module_segment |
| ASCR Top Heater Upper Alarm Boundary | `L01S_ASCR_DB_setpoint.HeaterTop.Alarm_Boundary_Up` | °C | 0.70 | module_segment |
| ASCR X-Axis Lower Adjust Offset Position | `L01S_ASCR_DB_setpoint.x_adjust_lwr.Offset_Pos` | mm | 0.70 | module_segment |
| ASCR X-Axis Lower Adjust Target Position | `L01S_ASCR_DB_setpoint.x_adjust_lwr.Target_Pos` | mm | 0.70 | module_segment |
| ASCR X-Axis Upper Adjust Offset Position | `L01S_ASCR_DB_setpoint.x_adjust_up.Offset_Pos` | mm | 0.70 | module_segment |
| ASCR X-Axis Upper Adjust Target Position | `L01S_ASCR_DB_setpoint.x_adjust_up.Target_Pos` | mm | 0.70 | module_segment |
| ASCR Y-Axis Lower Adjust Offset Position | `L01S_ASCR_DB_setpoint.y_adjust_lwr.Offset_Pos` | mm | 0.70 | module_segment |
| ASCR Y-Axis Lower Adjust Target Position | `L01S_ASCR_DB_setpoint.y_adjust_lwr.Target_Pos` | mm | 0.70 | module_segment |
| ASCR Y-Axis Upper Adjust Offset Position | `L01S_ASCR_DB_setpoint.y_adjust_up.Offset_Pos` | mm | 0.70 | module_segment |
| ASCR Y-Axis Upper Adjust Target Position | `L01S_ASCR_DB_setpoint.y_adjust_up.Target_Pos` | mm | 0.70 | module_segment |
| ASCR X-Axis Lower Adjust Actual Position | `L01S_ASCR_DB_HMI_connect.x_adjust_lwr.ActPos` | mm | 0.70 | module_segment |
| ASCR X-Axis Upper Adjust Actual Position | `L01S_ASCR_DB_HMI_connect.x_adjust_up.ActPos` | mm | 0.70 | module_segment |
| ASCR Y-Axis Lower Adjust Actual Position | `L01S_ASCR_DB_HMI_connect.y_adjust_lwr.ActPos` | mm | 0.70 | module_segment |
| ASCR Y-Axis Upper Adjust Actual Position | `L01S_ASCR_DB_HMI_connect.y_adjust_up.ActPos` | mm | 0.70 | module_segment |
| ASCL Bottom Heater Temperature Setpoint | `L01S_ASCL_DB_setpoint.HeaterBottom.Temp_Set` | °C | 0.85 | module_segment |
| ASCL Top Heater Temperature Setpoint | `L01S_ASCL_DB_setpoint.HeaterTop.Temp_Set` | °C | 0.85 | module_segment |
| ASCL Bottom Heater Actual Temperature | `L01S_ASCL_DB_HMI_connect.HeaterBottom.Status.Actual` | °C | 0.85 | module_segment |
| ASCL Top Heater Actual Temperature | `L01S_ASCL_DB_HMI_connect.HeaterTop.Status.Actual` | °C | 0.85 | module_segment |
| ASCR Bottom Heater Temperature Setpoint | `L01S_ASCR_DB_setpoint.HeaterBottom.Temp_Set` | °C | 0.85 | module_segment |
| ASCR Top Heater Temperature Setpoint | `L01S_ASCR_DB_setpoint.HeaterTop.Temp_Set` | °C | 0.85 | module_segment |
| ASCR Bottom Heater Actual Temperature | `L01S_ASCR_DB_HMI_connect.HeaterBottom.Status.Actual` | °C | 0.85 | module_segment |
| ASCR Top Heater Actual Temperature | `L01S_ASCR_DB_HMI_connect.HeaterTop.Status.Actual` | °C | 0.85 | module_segment |

### ASB labelling station, curved closure (MC007-ASB)

- 323 candidate tag(s) considered -> 77 kept as genuine parameters (24%).
- Kept tags found by: 77 via *module_segment* (the tag name contains this station's own PLC/module code as a literal segment - the strongest signal available).
- 12 kept parameter(s) below 0.5 confidence - flagged with ⚠ below.

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| ASBL Bottom Inspection Job Number ⚠ | `L01S_ASBL_DB_setpoint.Inspection_Bottom.JobNr` | - | 0.45 | module_segment |
| ASBL Top Inspection Job Number ⚠ | `L01S_ASBL_DB_setpoint.Inspection_Top.JobNr` | - | 0.45 | module_segment |
| ASBL Coil Counter Actual ⚠ | `L01S_ASBL_DB_HMI_connect.CoilCounter.CoilCounter` | - | 0.45 | module_segment |
| ASBL Cycle Counter ⚠ | `L01S_ASBL_DB_HMI_connect.Count.CycleCounter` | - | 0.45 | module_segment |
| ASBL Bottom Inspection Actual Job Number ⚠ | `L01S_ASBL_DB_HMI_connect.Inspection.Bottom.JobNr` | - | 0.45 | module_segment |
| ASBL Top Inspection Actual Job Number ⚠ | `L01S_ASBL_DB_HMI_connect.Inspection.Top.JobNr` | - | 0.45 | module_segment |
| ASBR Bottom Inspection Job Number ⚠ | `L01S_ASBR_DB_setpoint.Inspection_Bottom.JobNr` | - | 0.45 | module_segment |
| ASBR Top Inspection Job Number ⚠ | `L01S_ASBR_DB_setpoint.Inspection_Top.JobNr` | - | 0.45 | module_segment |
| ASBR Coil Counter Actual ⚠ | `L01S_ASBR_DB_HMI_connect.CoilCounter.CoilCounter` | - | 0.45 | module_segment |
| ASBR Cycle Counter ⚠ | `L01S_ASBR_DB_HMI_connect.Count.CycleCounter` | - | 0.45 | module_segment |
| ASBR Bottom Inspection Actual Job Number ⚠ | `L01S_ASBR_DB_HMI_connect.Inspection.Bottom.JobNr` | - | 0.45 | module_segment |
| ASBR Top Inspection Actual Job Number ⚠ | `L01S_ASBR_DB_HMI_connect.Inspection.Top.JobNr` | - | 0.45 | module_segment |
| Gap: ASB Inspection to ASC Preheat | `GE1_DB_setpoint.StationGaps.ASB_Insp_ASC_Pht` | mm | 0.50 | module_segment |
| Gap: ASB Station to PT1 Station | `GE1_DB_setpoint.StationGaps.ASB_St_PT1_St` | mm | 0.50 | module_segment |
| ASBL Averaging Result | `Averaging_ASBL_DB.Averaging_Result` | - | 0.50 | module_segment |
| ASBL Averaging Lower Limit | `Averaging_ASBL_DB.Lower_Limit` | - | 0.50 | module_segment |
| ASBL Averaging Upper Limit | `Averaging_ASBL_DB.Upper_Limit` | - | 0.50 | module_segment |
| ASBR Averaging Result | `Averaging_ASBR_DB.Averaging_Result` | - | 0.50 | module_segment |
| ASBR Averaging Lower Limit | `Averaging_ASBR_DB.Lower_Limit` | - | 0.50 | module_segment |
| ASBR Averaging Upper Limit | `Averaging_ASBR_DB.Upper_Limit` | - | 0.50 | module_segment |
| ASBL Coil Counter To End | `L01S_ASBL_DB_setpoint.CoilCounter.CounterToEnd` | - | 0.50 | module_segment |
| ASBL Labeler Type Selection | `L01S_ASBL_DB_setpoint.Labeler.LType` | - | 0.50 | module_segment |
| ASBL Actual Cycle Time (T01) | `L01S_ASBL_DB_HMI_connect.HMIActualTimes.T01` | ms | 0.50 | module_segment |
| ASBR Coil Counter To End | `L01S_ASBR_DB_setpoint.CoilCounter.CounterToEnd` | - | 0.50 | module_segment |
| ASBR Labeler Type Selection | `L01S_ASBR_DB_setpoint.Labeler.LType` | - | 0.50 | module_segment |
| ASBR Actual Cycle Time (T01) | `L01S_ASBR_DB_HMI_connect.HMIActualTimes.T01` | ms | 0.50 | module_segment |
| ASBL Vision Member 4 In Footprint LHS | `LO1S_ASBL_DB_Vision Valu.Mem_4_In_Fprint_L` | mm | 0.55 | module_segment |
| ASBL Vision Member 4 In Footprint RHS | `LO1S_ASBL_DB_Vision Valu.Mem_4_In_Fprint_R` | mm | 0.55 | module_segment |
| ASBL Label Adjustment X | `L01S_ASBL_DB_setpoint.LabelAdjust.X` | mm | 0.55 | module_segment |
| ASBL Label Adjustment Y | `L01S_ASBL_DB_setpoint.LabelAdjust.Y` | mm | 0.55 | module_segment |
| ASBL Cycle Time Setpoint | `L01S_ASBL_DB_setpoint.Times.CycleTime` | ms | 0.55 | module_segment |
| ASBR Label Adjustment X | `L01S_ASBR_DB_setpoint.LabelAdjust.X` | mm | 0.55 | module_segment |
| ASBR Label Adjustment Y | `L01S_ASBR_DB_setpoint.LabelAdjust.Y` | mm | 0.55 | module_segment |
| ASBR Cycle Time Setpoint | `L01S_ASBR_DB_setpoint.Times.CycleTime` | ms | 0.55 | module_segment |
| ASBL Vision Spreading Distance LHS | `LO1S_ASBL_DB_Vision Valu.Spreading_Dist_L` | mm | 0.60 | module_segment |
| ASBL Vision Spreading Distance RHS | `LO1S_ASBL_DB_Vision Valu.Spreading_Dist_R` | mm | 0.60 | module_segment |
| ASBR Vision Spreading Distance Left | `L01S_ASBR_DB_Vision_Value_Spreading_Distance_Left` | mm | 0.60 | module_segment |
| ASBR Vision Spreading Distance Right | `L01S_ASBR_DB_Vision_Value_Spreading_Distance_Right` | mm | 0.60 | module_segment |
| ASBL Adjust X Actual Position | `SIKO_ASBL Adjust X.Actual_Position_mm_unit` | mm | 0.60 | module_segment |
| ASBL Adjust X Target Position | `SIKO_ASBL Adjust X.Target_Position_mm` | mm | 0.60 | module_segment |
| ASBL Adjust Y Actual Position | `SIKO_ASBL Adjust Y.Actual_Position_mm_unit` | mm | 0.60 | module_segment |
| ASBL Adjust Y Target Position | `SIKO_ASBL Adjust Y.Target_Position_mm` | mm | 0.60 | module_segment |
| ASBR Adjust X Actual Position | `SIKO_ASBR Adjust X.Actual_Position_mm_unit` | mm | 0.60 | module_segment |
| ASBR Adjust X Target Position | `SIKO_ASBR Adjust X.Target_Position_mm` | mm | 0.60 | module_segment |
| ASBR Adjust Y Actual Position | `SIKO_ASBR Adjust Y.Actual_Position_mm_unit` | mm | 0.60 | module_segment |
| ASBR Adjust Y Target Position | `SIKO_ASBR Adjust Y.Target_Position_mm` | mm | 0.60 | module_segment |
| ASBL X-Axis Adjust Auto-Correct Setpoint Position | `L01S_ASBL_DB_HMI_connect.x_adjust.AutoCorrectSPPos` | mm | 0.60 | module_segment |
| ASBL Y-Axis Adjust Auto-Correct Setpoint Position | `L01S_ASBL_DB_HMI_connect.y_adjust.AutoCorrectSPPos` | mm | 0.60 | module_segment |
| ASBR X-Axis Adjust Auto-Correct Setpoint Position | `L01S_ASBR_DB_HMI_connect.x_adjust.AutoCorrectSPPos` | mm | 0.60 | module_segment |
| ASBR Y-Axis Adjust Auto-Correct Setpoint Position | `L01S_ASBR_DB_HMI_connect.y_adjust.AutoCorrectSPPos` | mm | 0.60 | module_segment |
| ASBL Vision Fastener Position LHS | `LO1S_ASBL_DB_Vision Valu.Fast_Pos_Left` | mm | 0.65 | module_segment |
| ASBL Vision Fastener Position RHS | `LO1S_ASBL_DB_Vision Valu.Fast_Pos_Right` | mm | 0.65 | module_segment |
| ASBL Vision Flap Height | `LO1S_ASBL_DB_Vision Valu.Flap_Height` | mm | 0.65 | module_segment |
| ASBL X-Axis Camera Adjust Actual Position | `L01S_ASBL_DB_HMI_connect.x_adjust_camera.ActPos` | mm | 0.65 | module_segment |
| ASBL Y-Axis Camera Adjust Actual Position | `L01S_ASBL_DB_HMI_connect.y_adjust_camera.ActPos` | mm | 0.65 | module_segment |
| ASBR X-Axis Camera Adjust Actual Position | `L01S_ASBR_DB_HMI_connect.x_adjust_camera.ActPos` | mm | 0.65 | module_segment |
| ASBR Y-Axis Camera Adjust Actual Position | `L01S_ASBR_DB_HMI_connect.y_adjust_camera.ActPos` | mm | 0.65 | module_segment |
| ASBL X-Axis Adjust Offset Position | `L01S_ASBL_DB_setpoint.x_adjust.Offset_Pos` | mm | 0.70 | module_segment |
| ASBL X-Axis Adjust Target Position | `L01S_ASBL_DB_setpoint.x_adjust.Target_Pos` | mm | 0.70 | module_segment |
| ASBL X-Axis Camera Adjust Offset Position | `L01S_ASBL_DB_setpoint.x_adjust_camera.Offset_Pos` | mm | 0.70 | module_segment |
| ASBL X-Axis Camera Adjust Target Position | `L01S_ASBL_DB_setpoint.x_adjust_camera.Target_Pos` | mm | 0.70 | module_segment |
| ASBL Y-Axis Adjust Offset Position | `L01S_ASBL_DB_setpoint.y_adjust.Offset_Pos` | mm | 0.70 | module_segment |
| ASBL Y-Axis Adjust Target Position | `L01S_ASBL_DB_setpoint.y_adjust.Target_Pos` | mm | 0.70 | module_segment |
| ASBL Y-Axis Camera Adjust Offset Position | `L01S_ASBL_DB_setpoint.y_adjust_camera.Offset_Pos` | mm | 0.70 | module_segment |
| ASBL Y-Axis Camera Adjust Target Position | `L01S_ASBL_DB_setpoint.y_adjust_camera.Target_Pos` | mm | 0.70 | module_segment |
| ASBL X-Axis Adjust Actual Position | `L01S_ASBL_DB_HMI_connect.x_adjust.ActPos` | mm | 0.70 | module_segment |
| ASBL Y-Axis Adjust Actual Position | `L01S_ASBL_DB_HMI_connect.y_adjust.ActPos` | mm | 0.70 | module_segment |
| ASBR X-Axis Adjust Offset Position | `L01S_ASBR_DB_setpoint.x_adjust.Offset_Pos` | mm | 0.70 | module_segment |
| ASBR X-Axis Adjust Target Position | `L01S_ASBR_DB_setpoint.x_adjust.Target_Pos` | mm | 0.70 | module_segment |
| ASBR X-Axis Camera Adjust Offset Position | `L01S_ASBR_DB_setpoint.x_adjust_camera.Offset_Pos` | mm | 0.70 | module_segment |
| ASBR X-Axis Camera Adjust Target Position | `L01S_ASBR_DB_setpoint.x_adjust_camera.Target_Pos` | mm | 0.70 | module_segment |
| ASBR Y-Axis Adjust Offset Position | `L01S_ASBR_DB_setpoint.y_adjust.Offset_Pos` | mm | 0.70 | module_segment |
| ASBR Y-Axis Adjust Target Position | `L01S_ASBR_DB_setpoint.y_adjust.Target_Pos` | mm | 0.70 | module_segment |
| ASBR Y-Axis Camera Adjust Offset Position | `L01S_ASBR_DB_setpoint.y_adjust_camera.Offset_Pos` | mm | 0.70 | module_segment |
| ASBR Y-Axis Camera Adjust Target Position | `L01S_ASBR_DB_setpoint.y_adjust_camera.Target_Pos` | mm | 0.70 | module_segment |
| ASBR X-Axis Adjust Actual Position | `L01S_ASBR_DB_HMI_connect.x_adjust.ActPos` | mm | 0.70 | module_segment |
| ASBR Y-Axis Adjust Actual Position | `L01S_ASBR_DB_HMI_connect.y_adjust.ActPos` | mm | 0.70 | module_segment |

### PPS periphery punching station (MC007-PPS)

- 65 candidate tag(s) considered -> 14 kept as genuine parameters (22%).
- Kept tags found by: 14 via *module_segment* (the tag name contains this station's own PLC/module code as a literal segment - the strongest signal available).

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| Gap 02: PPS to ASB/ASC inspection station gap | `GE1_DB_setpoint.StationGaps.PPS_St_ASB_Insp` | - | 0.50 | module_segment |
| Cycle counter | `L01S_PPS_DB_HMI_connect.Count.CycleCounter` | - | 0.55 | module_segment |
| T02: punching time | `L01S_PPS_DB_setpoint.Times._02` | ms | 0.75 | module_segment |
| T01: cycle time (actual) | `L01S_PPS_DB_HMI_connect.HMIActualTimes.T01` | ms | 0.80 | module_segment |
| T01: cycle time (setpoint) | `L01S_PPS_DB_setpoint.Times.CycleTime` | ms | 0.85 | module_segment |
| X-axis offset position | `L01S_PPS_DB_setpoint.Adujst_X.Offset_Pos` | mm | 0.90 | module_segment |
| X-axis target position | `L01S_PPS_DB_setpoint.Adujst_X.Target_Pos` | mm | 0.90 | module_segment |
| Y-axis offset position | `L01S_PPS_DB_setpoint.Adujst_Y.Offset_Pos` | mm | 0.90 | module_segment |
| Y-axis target position | `L01S_PPS_DB_setpoint.Adujst_Y.Target_Pos` | mm | 0.90 | module_segment |
| Z-axis offset position | `L01S_PPS_DB_setpoint.Adujst_Z.Offset_Pos` | mm | 0.90 | module_segment |
| Z-axis target position | `L01S_PPS_DB_setpoint.Adujst_Z.Target_Pos` | mm | 0.90 | module_segment |
| X-axis actual position | `L01S_PPS_DB_HMI_connect.Adujst_X.ActPos` | mm | 0.90 | module_segment |
| Y-axis actual position | `L01S_PPS_DB_HMI_connect.Adujst_Y.ActPos` | mm | 0.90 | module_segment |
| Z-axis actual position | `L01S_PPS_DB_HMI_connect.Adujst_Z.ActPos` | mm | 0.90 | module_segment |

### ULS unloading station (MC007-ULS)

- 161 candidate tag(s) considered -> 27 kept as genuine parameters (17%).
- Kept tags found by: 27 via *module_segment* (the tag name contains this station's own PLC/module code as a literal segment - the strongest signal available).

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| Gap 01: ULS to PPS station gap | `GE1_DB_setpoint.StationGaps.ULS_St_PPS_St` | - | 0.50 | module_segment |
| Stack counter, belt conveyor (setpoint) | `L01S_ULS_DB_setpoint.BeltConveyor.StackCounter` | - | 0.55 | module_segment |
| Stack counter, belt conveyor (actual) | `L01S_ULS_DB_HMI_connect.BeltConveyor.StackCounter` | - | 0.55 | module_segment |
| Cycle counter | `L01S_ULS_DB_HMI_connect.Count.CycleCounter` | - | 0.55 | module_segment |
| T02: belt running time in stack | `L01S_ULS_DB_setpoint.Times._02` | ms | 0.75 | module_segment |
| T03: belt running time between | `L01S_ULS_DB_setpoint.Times._03` | ms | 0.75 | module_segment |
| T04: pick and place suction time | `L01S_ULS_DB_setpoint.Times._04` | ms | 0.75 | module_segment |
| T05: pick and place blow-off time | `L01S_ULS_DB_setpoint.Times._05` | ms | 0.75 | module_segment |
| T01: cycle time (actual) | `L01S_ULS_DB_HMI_connect.HMIActualTimes.T01` | ms | 0.80 | module_segment |
| Extractor position 1 acceleration | `L01S_ULS_DB_setpoint.Extractor._Pos1.Acc` | % | 0.85 | module_segment |
| Extractor position 1 deceleration | `L01S_ULS_DB_setpoint.Extractor._Pos1.Dec` | % | 0.85 | module_segment |
| Extractor override velocity | `L01S_ULS_DB_setpoint.Extractor.OVR_Velocity` | % | 0.85 | module_segment |
| T01: cycle time (setpoint) | `L01S_ULS_DB_setpoint.Times.CycleTime` | ms | 0.85 | module_segment |
| X-axis offset position | `L01S_ULS_DB_setpoint.Adjust_X.Offset_Pos` | mm | 0.90 | module_segment |
| X-axis target position | `L01S_ULS_DB_setpoint.Adjust_X.Target_Pos` | mm | 0.90 | module_segment |
| X-axis expeller offset position | `L01S_ULS_DB_setpoint.Adjust_X_Expeller.Offset_Pos` | mm | 0.90 | module_segment |
| X-axis expeller target position | `L01S_ULS_DB_setpoint.Adjust_X_Expeller.Target_Pos` | mm | 0.90 | module_segment |
| Y-axis offset position | `L01S_ULS_DB_setpoint.Adjust_Y.Offset_Pos` | mm | 0.90 | module_segment |
| Y-axis target position | `L01S_ULS_DB_setpoint.Adjust_Y.Target_Pos` | mm | 0.90 | module_segment |
| Extractor position 1 target position | `L01S_ULS_DB_setpoint.Extractor._Pos1.Position` | mm | 0.90 | module_segment |
| Extractor position 2 target position | `L01S_ULS_DB_setpoint.Extractor._Pos2.Position` | mm | 0.90 | module_segment |
| Extractor position 3 target position | `L01S_ULS_DB_setpoint.Extractor._Pos3.Position` | mm | 0.90 | module_segment |
| X-axis actual position | `L01S_ULS_DB_HMI_connect.Adjust_X.ActPos` | mm | 0.90 | module_segment |
| X-axis expeller actual position | `L01S_ULS_DB_HMI_connect.Adjust_X_Expeller.ActPos` | mm | 0.90 | module_segment |
| Y-axis actual position | `L01S_ULS_DB_HMI_connect.Adjust_Y.ActPos` | mm | 0.90 | module_segment |
| Extractor actual position | `L01S_ULS_DB_HMI_connect.Extractor.ActPos` | mm | 0.90 | module_segment |
| Extractor target position | `L01S_ULS_DB_HMI_connect.Extractor.TargetPos` | mm | 0.90 | module_segment |

### FFT feeding station, flange (MC007-FFT)

- 204 candidate tag(s) considered -> 30 kept as genuine parameters (15%).
- Kept tags found by: 30 via *module_segment* (the tag name contains this station's own PLC/module code as a literal segment - the strongest signal available).

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| RobSORT_L vision process code | `L02_FFT_DB_setpoint.RobSORT_L.vison_process_code` | - | 0.55 | module_segment |
| RobSORT_L vision process number | `L02_FFT_DB_setpoint.RobSORT_L.vison_process_number` | - | 0.55 | module_segment |
| RobSORT_R vision process code | `L02_FFT_DB_setpoint.RobSORT_R.vison_process_code` | - | 0.55 | module_segment |
| RobSORT_R vision process number | `L02_FFT_DB_setpoint.RobSORT_R.vison_process_number` | - | 0.55 | module_segment |
| Cycle counter | `L02_FFT_DB_HMI_connect.Count.CycleCounter` | - | 0.55 | module_segment |
| RobFEED pick angle | `L02_FFT_DB_setpoint.RobFEED.PICK.Angle` | deg | 0.60 | module_segment |
| RobFEED pick X offset | `L02_FFT_DB_setpoint.RobFEED.PICK.X_offset` | mm | 0.60 | module_segment |
| RobFEED pick Z offset | `L02_FFT_DB_setpoint.RobFEED.PICK.Z_offset` | mm | 0.60 | module_segment |
| RobFEED place angle | `L02_FFT_DB_setpoint.RobFEED.PLACE.Angle` | deg | 0.60 | module_segment |
| RobFEED place X offset | `L02_FFT_DB_setpoint.RobFEED.PLACE.X_offset` | mm | 0.60 | module_segment |
| RobFEED place Y offset | `L02_FFT_DB_setpoint.RobFEED.PLACE.Y_offset` | mm | 0.60 | module_segment |
| RobFEED place Z offset | `L02_FFT_DB_setpoint.RobFEED.PLACE.Z_offset` | mm | 0.60 | module_segment |
| RobSORT_L pick Z offset | `L02_FFT_DB_setpoint.RobSORT_L.PICK.Z_offset` | mm | 0.60 | module_segment |
| RobSORT_L place angle | `L02_FFT_DB_setpoint.RobSORT_L.PLACE.Angle` | deg | 0.60 | module_segment |
| RobSORT_L place X offset | `L02_FFT_DB_setpoint.RobSORT_L.PLACE.X_offset` | mm | 0.60 | module_segment |
| RobSORT_L place Y offset | `L02_FFT_DB_setpoint.RobSORT_L.PLACE.Y_offset` | mm | 0.60 | module_segment |
| RobSORT_L place Z offset | `L02_FFT_DB_setpoint.RobSORT_L.PLACE.Z_offset` | mm | 0.60 | module_segment |
| RobSORT_R pick Z offset | `L02_FFT_DB_setpoint.RobSORT_R.PICK.Z_offset` | mm | 0.60 | module_segment |
| RobSORT_R place angle | `L02_FFT_DB_setpoint.RobSORT_R.PLACE.Angle` | deg | 0.60 | module_segment |
| RobSORT_R place X offset | `L02_FFT_DB_setpoint.RobSORT_R.PLACE.X_offset` | mm | 0.60 | module_segment |
| RobSORT_R place Y offset | `L02_FFT_DB_setpoint.RobSORT_R.PLACE.Y_offset` | mm | 0.60 | module_segment |
| RobSORT_R place Z offset | `L02_FFT_DB_setpoint.RobSORT_R.PLACE.Z_offset` | mm | 0.60 | module_segment |
| RobFEED velocity factor | `L02_FFT_DB_setpoint.RobFEED.velocity` | % | 0.75 | module_segment |
| RobSORT_L velocity factor | `L02_FFT_DB_setpoint.RobSORT_L.velocity` | % | 0.75 | module_segment |
| RobSORT_R velocity factor | `L02_FFT_DB_setpoint.RobSORT_R.velocity` | % | 0.75 | module_segment |
| Cycle time, robot FEED (line) | `L02_FFT_DB_HMI_connect.HMIActualTimes.T21` | ms | 0.75 | module_segment |
| Cycle time, robot SORT left (line) | `L02_FFT_DB_HMI_connect.HMIActualTimes.T22` | ms | 0.75 | module_segment |
| Cycle time, robot SORT right (line) | `L02_FFT_DB_HMI_connect.HMIActualTimes.T23` | ms | 0.75 | module_segment |
| T01: cycle time (actual) | `L02_FFT_DB_HMI_connect.HMIActualTimes.T01` | ms | 0.80 | module_segment |
| T01: cycle time (setpoint) | `L02_FFT_DB_setpoint.Times.CycleTime` | ms | 0.85 | module_segment |

### FFG feeding station, gasket (MC007-FFG)

- 131 candidate tag(s) considered -> 44 kept as genuine parameters (34%).
- Kept tags found by: 44 via *module_segment* (the tag name contains this station's own PLC/module code as a literal segment - the strongest signal available).
- 3 kept parameter(s) below 0.5 confidence - flagged with ⚠ below.

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| Actual time T04 ⚠ | `L02S_FFG_DB_HMI_connect.HMIActualTimes.T04` | ms | 0.40 | module_segment |
| Actual time T05 ⚠ | `L02S_FFG_DB_HMI_connect.HMIActualTimes.T05` | ms | 0.40 | module_segment |
| Actual time T06 ⚠ | `L02S_FFG_DB_HMI_connect.HMIActualTimes.T06` | ms | 0.40 | module_segment |
| Cycle counter | `L02S_FFG_DB_HMI_connect.Count.CycleCounter` | - | 0.55 | module_segment |
| Pusher left target position (readback) | `L02S_FFG_DB_HMI_connect.PusherLeft.TargetPos` | mm | 0.55 | module_segment |
| Pusher right target position (readback) | `L02S_FFG_DB_HMI_connect.PusherRight.TargetPos` | mm | 0.55 | module_segment |
| T07: delay stopper left up | `L02S_FFG_DB_setpoint.Times.DelayStopperLeftup` | ms | 0.75 | module_segment |
| T08: delay stopper right up | `L02S_FFG_DB_setpoint.Times.DelayStopperRightup` | ms | 0.75 | module_segment |
| T10: separating unit suction time LHS | `L02S_FFG_DB_setpoint.Times.SeparatingSuctionTimeLHS` | ms | 0.75 | module_segment |
| T09: separating unit suction time RHS | `L02S_FFG_DB_setpoint.Times.SeparatingSuctionTimeRHS` | ms | 0.75 | module_segment |
| Chain target position (readback) | `L02S_FFG_DB_HMI_connect.Chain.TargetPos` | mm | 0.75 | module_segment |
| Pusher left actual position | `L02S_FFG_DB_HMI_connect.PusherLeft.ActPos` | mm | 0.75 | module_segment |
| Pusher right actual position | `L02S_FFG_DB_HMI_connect.PusherRight.ActPos` | mm | 0.75 | module_segment |
| T01: cycle time (actual) | `L02S_FFG_DB_HMI_connect.HMIActualTimes.T01` | ms | 0.80 | module_segment |
| Chain position acceleration | `L02S_FFG_DB_setpoint.Chain._Pos.Acc` | % | 0.85 | module_segment |
| Chain position deceleration | `L02S_FFG_DB_setpoint.Chain._Pos.Dec` | % | 0.85 | module_segment |
| Chain override velocity | `L02S_FFG_DB_setpoint.Chain.OVR_Velocity` | % | 0.85 | module_segment |
| Pusher left, empty position acceleration | `L02S_FFG_DB_setpoint.PusherLeft._Empty.Acc` | % | 0.85 | module_segment |
| Pusher left, empty position deceleration | `L02S_FFG_DB_setpoint.PusherLeft._Empty.Dec` | % | 0.85 | module_segment |
| Pusher left, empty position velocity | `L02S_FFG_DB_setpoint.PusherLeft._Empty.Velocity` | % | 0.85 | module_segment |
| Pusher left, full position acceleration | `L02S_FFG_DB_setpoint.PusherLeft._Full.Acc` | % | 0.85 | module_segment |
| Pusher left, full position deceleration | `L02S_FFG_DB_setpoint.PusherLeft._Full.Dec` | % | 0.85 | module_segment |
| Pusher left, full position velocity | `L02S_FFG_DB_setpoint.PusherLeft._Full.Velocity` | % | 0.85 | module_segment |
| Pusher left, pick position acceleration | `L02S_FFG_DB_setpoint.PusherLeft._Pick.Acc` | % | 0.85 | module_segment |
| Pusher left, pick position deceleration | `L02S_FFG_DB_setpoint.PusherLeft._Pick.Dec` | % | 0.85 | module_segment |
| Pusher left, pick position velocity | `L02S_FFG_DB_setpoint.PusherLeft._Pick.Velocity` | % | 0.85 | module_segment |
| Pusher right, empty position acceleration | `L02S_FFG_DB_setpoint.PusherRight._Empty.Acc` | % | 0.85 | module_segment |
| Pusher right, empty position deceleration | `L02S_FFG_DB_setpoint.PusherRight._Empty.Dec` | % | 0.85 | module_segment |
| Pusher right, empty position velocity | `L02S_FFG_DB_setpoint.PusherRight._Empty.Velocity` | % | 0.85 | module_segment |
| Pusher right, full position acceleration | `L02S_FFG_DB_setpoint.PusherRight._Full.Acc` | % | 0.85 | module_segment |
| Pusher right, full position deceleration | `L02S_FFG_DB_setpoint.PusherRight._Full.Dec` | % | 0.85 | module_segment |
| Pusher right, full position velocity | `L02S_FFG_DB_setpoint.PusherRight._Full.Velocity` | % | 0.85 | module_segment |
| Pusher right, pick position acceleration | `L02S_FFG_DB_setpoint.PusherRight._Pick.Acc` | % | 0.85 | module_segment |
| Pusher right, pick position deceleration | `L02S_FFG_DB_setpoint.PusherRight._Pick.Dec` | % | 0.85 | module_segment |
| Pusher right, pick position velocity | `L02S_FFG_DB_setpoint.PusherRight._Pick.Velocity` | % | 0.85 | module_segment |
| T01: cycle time (setpoint) | `L02S_FFG_DB_setpoint.Times.CycleTime` | ms | 0.85 | module_segment |
| Chain target position | `L02S_FFG_DB_setpoint.Chain._Pos.Position` | mm | 0.90 | module_segment |
| Pusher left, empty target position | `L02S_FFG_DB_setpoint.PusherLeft._Empty.Position` | mm | 0.90 | module_segment |
| Pusher left, full target position | `L02S_FFG_DB_setpoint.PusherLeft._Full.Position` | mm | 0.90 | module_segment |
| Pusher left, pick target position | `L02S_FFG_DB_setpoint.PusherLeft._Pick.Position` | mm | 0.90 | module_segment |
| Pusher right, empty target position | `L02S_FFG_DB_setpoint.PusherRight._Empty.Position` | mm | 0.90 | module_segment |
| Pusher right, full target position | `L02S_FFG_DB_setpoint.PusherRight._Full.Position` | mm | 0.90 | module_segment |
| Pusher right, pick target position | `L02S_FFG_DB_setpoint.PusherRight._Pick.Position` | mm | 0.90 | module_segment |
| Chain actual position | `L02S_FFG_DB_HMI_connect.Chain.ActPos` | mm | 0.90 | module_segment |

### FFB feeding station, barrier (MC007-FFB)

- 108 candidate tag(s) considered -> 9 kept as genuine parameters (8%).
- Kept tags found by: 9 via *module_segment* (the tag name contains this station's own PLC/module code as a literal segment - the strongest signal available).

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| RobBARRIER vision process code | `L02S_FFB_DB_setpoint.RobBARRIER.vison_process_code` | - | 0.55 | module_segment |
| RobBARRIER vision process number | `L02S_FFB_DB_setpoint.RobBARRIER.vison_process_number` | - | 0.55 | module_segment |
| Cycle counter | `L02S_FFB_DB_HMI_connect.Count.CycleCounter` | - | 0.55 | module_segment |
| RobBARRIER X offset | `L02S_FFB_DB_setpoint.RobBARRIER.X_offset` | mm | 0.60 | module_segment |
| RobBARRIER Z offset | `L02S_FFB_DB_setpoint.RobBARRIER.Z_offset` | mm | 0.60 | module_segment |
| RobBARRIER Y offset (pick/place distance between barrier stacks) | `L02S_FFB_DB_setpoint.RobBARRIER.Y_offset` | mm | 0.65 | module_segment |
| RobBARRIER velocity factor | `L02S_FFB_DB_setpoint.RobBARRIER.velocity` | % | 0.75 | module_segment |
| T01: cycle time (actual) | `L02S_FFB_DB_HMI_connect.HMIActualTimes.T01` | ms | 0.80 | module_segment |
| T01: cycle time (setpoint) | `L02S_FFB_DB_setpoint.Times.CycleTime` | ms | 0.85 | module_segment |

### INS chain conveyor (MC007-INS)

- 265 candidate tag(s) considered -> 78 kept as genuine parameters (29%).
- Kept tags found by: 78 via *module_segment* (the tag name contains this station's own PLC/module code as a literal segment - the strongest signal available).

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| Welding belt FPW gearing factor LHS | `L01_INS_DB_setpoint.WeldingBeltFPW.GearingFactorLHS` | % | 0.55 | module_segment |
| Welding belt FPW gearing factor RHS | `L01_INS_DB_setpoint.WeldingBeltFPW.GearingFactorRHS` | % | 0.55 | module_segment |
| Cycle counter | `L01_INS_DB_HMI_connect.Count.CycleCounter` | - | 0.55 | module_segment |
| Film stretching, lower, station 1-2 | `L01_INS_DB_setpoint.Film_Stretching_Lower.Stretching_1_2` | % | 0.60 | module_segment |
| Film stretching, lower, station 2-3 | `L01_INS_DB_setpoint.Film_Stretching_Lower.Stretching_2_3` | % | 0.60 | module_segment |
| Film stretching, lower, station 3-4 | `L01_INS_DB_setpoint.Film_Stretching_Lower.Stretching_3_4` | % | 0.60 | module_segment |
| Film stretching, lower, station 4-5 | `L01_INS_DB_setpoint.Film_Stretching_Lower.Stretching_4_5` | % | 0.60 | module_segment |
| Film stretching, upper, station 1-2 | `L01_INS_DB_setpoint.Film_Stretching_Upper.Stretching_1_2` | % | 0.60 | module_segment |
| Film stretching, upper, station 2-3 | `L01_INS_DB_setpoint.Film_Stretching_Upper.Stretching_2_3` | % | 0.60 | module_segment |
| Film stretching, upper, station 3-4 | `L01_INS_DB_setpoint.Film_Stretching_Upper.Stretching_3_4` | % | 0.60 | module_segment |
| Film stretching, upper, station 4-5 | `L01_INS_DB_setpoint.Film_Stretching_Upper.Stretching_4_5` | % | 0.60 | module_segment |
| Film stretching, lower, station 1-2 - maximum limit | `L01_INS_DB_setpointMAX.Film_Stretching_Lower.Stretching_1_2` | % | 0.65 | module_segment |
| Film stretching, lower, station 2-3 - maximum limit | `L01_INS_DB_setpointMAX.Film_Stretching_Lower.Stretching_2_3` | % | 0.65 | module_segment |
| Film stretching, lower, station 3-4 - maximum limit | `L01_INS_DB_setpointMAX.Film_Stretching_Lower.Stretching_3_4` | % | 0.65 | module_segment |
| Film stretching, lower, station 4-5 - maximum limit | `L01_INS_DB_setpointMAX.Film_Stretching_Lower.Stretching_4_5` | % | 0.65 | module_segment |
| Film stretching, upper, station 1-2 - maximum limit | `L01_INS_DB_setpointMAX.Film_Stretching_Upper.Stretching_1_2` | % | 0.65 | module_segment |
| Film stretching, upper, station 2-3 - maximum limit | `L01_INS_DB_setpointMAX.Film_Stretching_Upper.Stretching_2_3` | % | 0.65 | module_segment |
| Film stretching, upper, station 3-4 - maximum limit | `L01_INS_DB_setpointMAX.Film_Stretching_Upper.Stretching_3_4` | % | 0.65 | module_segment |
| Film stretching, upper, station 4-5 - maximum limit | `L01_INS_DB_setpointMAX.Film_Stretching_Upper.Stretching_4_5` | % | 0.65 | module_segment |
| Film stretching, lower, station 1-2 - minimum limit | `L01_INS_DB_setpointMIN.Film_Stretching_Lower.Stretching_1_2` | % | 0.65 | module_segment |
| Film stretching, lower, station 2-3 - minimum limit | `L01_INS_DB_setpointMIN.Film_Stretching_Lower.Stretching_2_3` | % | 0.65 | module_segment |
| Film stretching, lower, station 3-4 - minimum limit | `L01_INS_DB_setpointMIN.Film_Stretching_Lower.Stretching_3_4` | % | 0.65 | module_segment |
| Film stretching, lower, station 4-5 - minimum limit | `L01_INS_DB_setpointMIN.Film_Stretching_Lower.Stretching_4_5` | % | 0.65 | module_segment |
| Film stretching, upper, station 1-2 - minimum limit | `L01_INS_DB_setpointMIN.Film_Stretching_Upper.Stretching_1_2` | % | 0.65 | module_segment |
| Film stretching, upper, station 2-3 - minimum limit | `L01_INS_DB_setpointMIN.Film_Stretching_Upper.Stretching_2_3` | % | 0.65 | module_segment |
| Film stretching, upper, station 3-4 - minimum limit | `L01_INS_DB_setpointMIN.Film_Stretching_Upper.Stretching_3_4` | % | 0.65 | module_segment |
| Film stretching, upper, station 4-5 - minimum limit | `L01_INS_DB_setpointMIN.Film_Stretching_Upper.Stretching_4_5` | % | 0.65 | module_segment |
| Lower chain 1 target position - maximum limit | `L01_INS_DB_setpointMAX.Adjust_LowerChain_1.Target_Pos` | mm | 0.80 | module_segment |
| Upper chain 1 target position - maximum limit | `L01_INS_DB_setpointMAX.Adjust_UpperChain_1.Target_Pos` | mm | 0.80 | module_segment |
| Lower chain 1 target position - minimum limit | `L01_INS_DB_setpointMIN.Adjust_LowerChain_1.Target_Pos` | mm | 0.80 | module_segment |
| Upper chain 1 target position - minimum limit | `L01_INS_DB_setpointMIN.Adjust_UpperChain_1.Target_Pos` | mm | 0.80 | module_segment |
| T01: cycle time (actual) | `L01_INS_DB_HMI_connect.HMIActualTimes.T01` | ms | 0.80 | module_segment |
| Lower chain 1 offset position | `L01_INS_DB_setpoint.Adjust_LowerChain_1.Offset_Pos` | mm | 0.85 | module_segment |
| Lower chain 1 target position | `L01_INS_DB_setpoint.Adjust_LowerChain_1.Target_Pos` | mm | 0.85 | module_segment |
| Lower chain 2 offset position | `L01_INS_DB_setpoint.Adjust_LowerChain_2.Offset_Pos` | mm | 0.85 | module_segment |
| Lower chain 2 target position | `L01_INS_DB_setpoint.Adjust_LowerChain_2.Target_Pos` | mm | 0.85 | module_segment |
| Lower chain 3 offset position | `L01_INS_DB_setpoint.Adjust_LowerChain_3.Offset_Pos` | mm | 0.85 | module_segment |
| Lower chain 3 target position | `L01_INS_DB_setpoint.Adjust_LowerChain_3.Target_Pos` | mm | 0.85 | module_segment |
| Lower chain 4 offset position | `L01_INS_DB_setpoint.Adjust_LowerChain_4.Offset_Pos` | mm | 0.85 | module_segment |
| Lower chain 4 target position | `L01_INS_DB_setpoint.Adjust_LowerChain_4.Target_Pos` | mm | 0.85 | module_segment |
| Upper chain 1 offset position | `L01_INS_DB_setpoint.Adjust_UpperChain_1.Offset_Pos` | mm | 0.85 | module_segment |
| Upper chain 1 target position | `L01_INS_DB_setpoint.Adjust_UpperChain_1.Target_Pos` | mm | 0.85 | module_segment |
| Upper chain 2 offset position | `L01_INS_DB_setpoint.Adjust_UpperChain_2.Offset_Pos` | mm | 0.85 | module_segment |
| Upper chain 2 target position | `L01_INS_DB_setpoint.Adjust_UpperChain_2.Target_Pos` | mm | 0.85 | module_segment |
| Upper chain 3 offset position | `L01_INS_DB_setpoint.Adjust_UpperChain_3.Offset_Pos` | mm | 0.85 | module_segment |
| Upper chain 3 target position | `L01_INS_DB_setpoint.Adjust_UpperChain_3.Target_Pos` | mm | 0.85 | module_segment |
| Upper chain 4 offset position | `L01_INS_DB_setpoint.Adjust_UpperChain_4.Offset_Pos` | mm | 0.85 | module_segment |
| Upper chain 4 target position | `L01_INS_DB_setpoint.Adjust_UpperChain_4.Target_Pos` | mm | 0.85 | module_segment |
| Upper chain 5 offset position | `L01_INS_DB_setpoint.Adjust_UpperChain_5.Offset_Pos` | mm | 0.85 | module_segment |
| Upper chain 5 target position | `L01_INS_DB_setpoint.Adjust_UpperChain_5.Target_Pos` | mm | 0.85 | module_segment |
| Chain position 1 acceleration | `L01_INS_DB_setpoint.Chain._Pos1.Acc` | % | 0.85 | module_segment |
| Chain position 1 deceleration | `L01_INS_DB_setpoint.Chain._Pos1.Dec` | % | 0.85 | module_segment |
| Chain position 1 jerk | `L01_INS_DB_setpoint.Chain._Pos1.Jerk` | % | 0.85 | module_segment |
| Chain position 1 velocity | `L01_INS_DB_setpoint.Chain._Pos1.Velocity` | % | 0.85 | module_segment |
| Chain gearing factor to upper chain | `L01_INS_DB_setpoint.Chain.GearingFactorSync` | % | 0.85 | module_segment |
| T01: cycle time (setpoint) | `L01_INS_DB_setpoint.Times.CycleTime` | ms | 0.85 | module_segment |
| Upper clamp feed backward acceleration | `L01_INS_DB_setpoint.UpperClampFeed.Backward.Acc` | % | 0.85 | module_segment |
| Upper clamp feed backward deceleration | `L01_INS_DB_setpoint.UpperClampFeed.Backward.Dec` | % | 0.85 | module_segment |
| Upper clamp feed backward velocity | `L01_INS_DB_setpoint.UpperClampFeed.Backward.Velocity` | % | 0.85 | module_segment |
| Upper clamp feed gearing factor to upper chain | `L01_INS_DB_setpoint.UpperClampFeed.GearingFactorSync` | % | 0.85 | module_segment |
| Lower chain 1 actual position | `L01_INS_DB_HMI_connect.Adjust_LowerChain_1.ActPos` | mm | 0.85 | module_segment |
| Lower chain 2 actual position | `L01_INS_DB_HMI_connect.Adjust_LowerChain_2.ActPos` | mm | 0.85 | module_segment |
| Lower chain 3 actual position | `L01_INS_DB_HMI_connect.Adjust_LowerChain_3.ActPos` | mm | 0.85 | module_segment |
| Lower chain 4 actual position | `L01_INS_DB_HMI_connect.Adjust_LowerChain_4.ActPos` | mm | 0.85 | module_segment |
| Upper chain 1 actual position | `L01_INS_DB_HMI_connect.Adjust_UpperChain_1.ActPos` | mm | 0.85 | module_segment |
| Upper chain 2 actual position | `L01_INS_DB_HMI_connect.Adjust_UpperChain_2.ActPos` | mm | 0.85 | module_segment |
| Upper chain 3 actual position | `L01_INS_DB_HMI_connect.Adjust_UpperChain_3.ActPos` | mm | 0.85 | module_segment |
| Upper chain 4 actual position | `L01_INS_DB_HMI_connect.Adjust_UpperChain_4.ActPos` | mm | 0.85 | module_segment |
| Upper chain 5 actual position | `L01_INS_DB_HMI_connect.Adjust_UpperChain_5.ActPos` | mm | 0.85 | module_segment |
| Chain target position (readback) | `L01_INS_DB_HMI_connect.Chain.TargetPos` | mm | 0.85 | module_segment |
| Lower chain drive actual position | `L01_INS_DB_HMI_connect.ChainLower.ActPos` | mm | 0.85 | module_segment |
| Upper chain drive actual position | `L01_INS_DB_HMI_connect.ChainUpper.ActPos` | mm | 0.85 | module_segment |
| Upper clamp feed actual position | `L01_INS_DB_HMI_connect.UpperClampFeed.ActPos` | mm | 0.85 | module_segment |
| Upper clamp feed target position (readback) | `L01_INS_DB_HMI_connect.UpperClampFeed.TargetPos` | mm | 0.85 | module_segment |
| Chain position 1 target position | `L01_INS_DB_setpoint.Chain._Pos1.Position` | mm | 0.90 | module_segment |
| Upper clamp feed backward target position | `L01_INS_DB_setpoint.UpperClampFeed.Backward.Position` | mm | 0.90 | module_segment |
| Upper clamp feed forward target position | `L01_INS_DB_setpoint.UpperClampFeed.Forward.Position` | mm | 0.90 | module_segment |
| Chain actual position | `L01_INS_DB_HMI_connect.Chain.ActPos` | mm | 0.90 | module_segment |
