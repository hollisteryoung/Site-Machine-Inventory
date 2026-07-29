# Tag Matching Report - Line K13

This summarizes, for every station found on this line, which historian tags were kept as genuine process parameters and why. Parameters marked with a low match strategy (keyword/keyword_stem/legend_code/folder_match) or below 0.5 confidence are the ones most worth a second look from someone who knows the physical machine.

## Summary

- 19 station(s) processed.
- 4399 candidate tag(s) considered across all stations -> 1309 kept as genuine parameters (30% of candidates).
- 1309 of this line's 5411 total historian tags (24.2%) ended up mapped to a genuine parameter - this is the actual coverage of the raw tag export, as opposed to the conversion rate above, which only measures the pre-filtered candidate pool.
- 130 kept parameter(s) below 0.5 confidence overall - worth a second look.

## Machine: Inline System KIT 70/20

### UWS unwinding station (MC006-UWS)

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

### FPW filter welding station (MC006-FPW)

- 650 candidate tag(s) considered -> 188 kept as genuine parameters (29%).
- Kept tags found by: 188 via *module_segment* (the tag name contains this station's own PLC/module code as a literal segment - the strongest signal available).
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
| Gap 25: FPWL Station Hole Punch to COR Station Low (Web2) | `GE1_DB_setpoint.StationGaps.FPWL_StHp_COR_StDn` | mm | 0.50 | module_segment |
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
| FPW Left Revolver Blow-Off Delay Preset Time | `FPWL_TIMERS_NEW.Blowoff_delay_Time` | s | 0.55 | module_segment |
| FPW Right Revolver Blow-Off Delay Preset Time | `FPWR_TIMERS_NEW.Blowoff_delay_Time` | s | 0.55 | module_segment |
| FPW Left Filter Coil Counter To End | `L01S_FPWL_DB_setpoint.FilterCoil.CounterToEnd` | - | 0.55 | module_segment |
| FPW Right Filter Coil Counter To End | `L01S_FPWR_DB_setpoint.FilterCoil.CounterToEnd` | - | 0.55 | module_segment |
| FPW Left Filter Register Coil Counter at End (Actual) | `L01S_FPWL_DB_HMI_connect.FilterRegister.States.CoilCounter` | - | 0.55 | module_segment |
| FPW Right Filter Register Coil Counter at End (Actual) | `L01S_FPWR_DB_HMI_connect.FilterRegister.States.CoilCounter` | - | 0.55 | module_segment |
| FPW Left Cycle Time (Actual, T01) | `L01S_FPWL_DB_HMI_connect.HMIActualTimes.T01` | ms | 0.55 | module_segment |
| FPW Right Cycle Time (Actual, T01) | `L01S_FPWR_DB_HMI_connect.HMIActualTimes.T01` | ms | 0.55 | module_segment |
| FPW Left Cooling Plate Temperature | `GE1_DB_interface.FPWL_COMMUNICATION._FROM.TempCoolingPlate` | °C | 0.60 | module_segment |
| FPW Right Filter Transport Override Velocity | `L01S_FPWR_DB_setpoint.FilterTransport.OVR_Velocity` | % | 0.60 | module_segment |
| FPW Left Heater Correction Value | `L01S_FPWL_DB_setpoint.Heater.Correction_Value` | °K | 0.60 | module_segment |
| FPW Right Heater Correction Value | `L01S_FPWR_DB_setpoint.Heater.Correction_Value` | °K | 0.60 | module_segment |
| FPW Right Revolver Override Velocity | `L01S_FPWR_DB_setpoint.Revolver.OVR_Velocity` | % | 0.60 | module_segment |
| FPW Left Cycle Counter | `L01S_FPWL_DB_HMI_connect.Count.CycleCounter` | - | 0.60 | module_segment |
| FPW Right Cycle Counter | `L01S_FPWR_DB_HMI_connect.Count.CycleCounter` | - | 0.60 | module_segment |
| FPW Left Heater1 PID Output | `L01S_FPWL_DB_HMI_connect.Heater1.Status.LMN` | % | 0.60 | module_segment |
| FPW Right Heater1 PID Output | `L01S_FPWR_DB_HMI_connect.Heater1.Status.LMN` | % | 0.60 | module_segment |
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
| FPW Left Heater Temperature Setpoint | `L01S_FPWL_DB_setpoint.Heater.Temp_Set` | °C | 0.90 | module_segment |
| FPW Right Heater Temperature Setpoint | `L01S_FPWR_DB_setpoint.Heater.Temp_Set` | °C | 0.90 | module_segment |
| FPW Left Heater1 Actual Temperature | `L01S_FPWL_DB_HMI_connect.Heater1.Status.Actual` | °C | 0.90 | module_segment |
| FPW Right Heater1 Actual Temperature | `L01S_FPWR_DB_HMI_connect.Heater1.Status.Actual` | °C | 0.90 | module_segment |

### PRI printing unit (Corona printer control module) (MC006-PRI)

- 327 candidate tag(s) considered -> 107 kept as genuine parameters (33%).
- Kept tags found by: 107 via *module_segment* (the tag name contains this station's own PLC/module code as a literal segment - the strongest signal available).
- 11 kept parameter(s) below 0.5 confidence - flagged with ⚠ below.

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| PRIH Cycles After Film Finished, Actual (Left) ⚠ | `L01S_PRIH_DB_HMI_connect.CyclesAfterFilmFinished._left` | - | 0.40 | module_segment |
| PRIH Cycles After Film Finished, Actual (Right) ⚠ | `L01S_PRIH_DB_HMI_connect.CyclesAfterFilmFinished._right` | - | 0.40 | module_segment |
| PRIH Heater 1 Self-Tuning Excitation Delta ⚠ | `L01S_PRIH_DB_HMI_connect.Heater1.Control.TUN_DLMN` | % | 0.40 | module_segment |
| PRIH Heater 2 Self-Tuning Excitation Delta ⚠ | `L01S_PRIH_DB_HMI_connect.Heater2.Control.TUN_DLMN` | % | 0.40 | module_segment |
| PRIH Tack Seal Heater Self-Tuning Excitation Delta ⚠ | `L01S_PRIH_DB_HMI_connect.HeaterTackSeal.Control.TUN_DLMN` | % | 0.40 | module_segment |
| PRIH Print Inspection Actual Job (LHS) ⚠ | `L01S_PRIH_DB_HMI_connect.Inspection._LHS.JobNr` | - | 0.40 | module_segment |
| PRIH Print Inspection Actual Job (RHS) ⚠ | `L01S_PRIH_DB_HMI_connect.Inspection._RHS.JobNr` | - | 0.40 | module_segment |
| PRIT Print Inspection Actual Job (LHS) ⚠ | `L01S_PRIT_DB_HMI_connect.Inspection._LHS.JobNr` | - | 0.40 | module_segment |
| PRIT Print Inspection Actual Job (RHS) ⚠ | `L01S_PRIT_DB_HMI_connect.Inspection._RHS.JobNr` | - | 0.40 | module_segment |
| PRIT Left Printer Active Job Name ⚠ | `L01S_PRIT_PM_L.JobName` | - | 0.40 | module_segment |
| PRIT Right Printer Active Job Name ⚠ | `L01S_PRIT_PM_R.JobName` | - | 0.40 | module_segment |
| Gap 30: PRIH Inspection to PRIH Station (Web12) | `GE1_DB_setpoint.StationGaps.PRIH_Insp_PRIH_St` | mm | 0.50 | module_segment |
| Gap 35: PRIH Station to Splice Web 1 | `GE1_DB_setpoint.StationGaps.PRIH_St_SPLICE_W1` | mm | 0.50 | module_segment |
| Gap 31: PRIH Station to Splice Web 2 | `GE1_DB_setpoint.StationGaps.PRIH_St_SPLICE_W2` | mm | 0.50 | module_segment |
| Gap 29: PRIH Tack Seal to PRIH Inspection (Web12) | `GE1_DB_setpoint.StationGaps.PRIH_TS_PRIH_Insp` | mm | 0.50 | module_segment |
| Gap 12: PRIT Inspection to COR Station Upper (Web3) | `GE1_DB_setpoint.StationGaps.PRIT_Insp_COR_StUp` | mm | 0.50 | module_segment |
| Gap 14: PRIT Station to Splice Web 3 | `GE1_DB_setpoint.StationGaps.PRIT_St_SPLICE_W3` | mm | 0.50 | module_segment |
| PRIH Cycles After Film Finished (Left) | `L01S_PRIH_DB_setpoint.CyclesAfterFilmFinished._left` | - | 0.50 | module_segment |
| PRIH Cycles After Film Finished (Right) | `L01S_PRIH_DB_setpoint.CyclesAfterFilmFinished._right` | - | 0.50 | module_segment |
| PRIH Print Inspection Job Number (LHS) | `L01S_PRIH_DB_setpoint.Inspection_LHS.JobNr` | - | 0.50 | module_segment |
| PRIH Print Inspection Job Number (RHS) | `L01S_PRIH_DB_setpoint.Inspection_RHS.JobNr` | - | 0.50 | module_segment |
| PRIH Heater 1 PID Proportional Gain | `L01S_PRIH_DB_HMI_connect.Heater1.Control.GAIN` | - | 0.50 | module_segment |
| PRIH Heater 1 Manipulated Variable High Limit | `L01S_PRIH_DB_HMI_connect.Heater1.Control.LMN_HLM` | % | 0.50 | module_segment |
| PRIH Heater 1 Manipulated Variable Low Limit | `L01S_PRIH_DB_HMI_connect.Heater1.Control.LMN_LLM` | % | 0.50 | module_segment |
| PRIH Heater 1 Manual Output Value | `L01S_PRIH_DB_HMI_connect.Heater1.Control.MAN` | % | 0.50 | module_segment |
| PRIH Heater 1 Manual-Switch Temperature Deviation | `L01S_PRIH_DB_HMI_connect.Heater1.Control.MAN_ON_VALUE` | °C | 0.50 | module_segment |
| PRIH Heater 1 PID Derivative Time | `L01S_PRIH_DB_HMI_connect.Heater1.Control.TD` | s | 0.50 | module_segment |
| PRIH Heater 1 PID Integration Time | `L01S_PRIH_DB_HMI_connect.Heater1.Control.TI` | s | 0.50 | module_segment |
| PRIH Heater 2 PID Proportional Gain | `L01S_PRIH_DB_HMI_connect.Heater2.Control.GAIN` | - | 0.50 | module_segment |
| PRIH Heater 2 Manipulated Variable High Limit | `L01S_PRIH_DB_HMI_connect.Heater2.Control.LMN_HLM` | % | 0.50 | module_segment |
| PRIH Heater 2 Manipulated Variable Low Limit | `L01S_PRIH_DB_HMI_connect.Heater2.Control.LMN_LLM` | % | 0.50 | module_segment |
| PRIH Heater 2 Manual Output Value | `L01S_PRIH_DB_HMI_connect.Heater2.Control.MAN` | % | 0.50 | module_segment |
| PRIH Heater 2 Manual-Switch Temperature Deviation | `L01S_PRIH_DB_HMI_connect.Heater2.Control.MAN_ON_VALUE` | °C | 0.50 | module_segment |
| PRIH Heater 2 PID Derivative Time | `L01S_PRIH_DB_HMI_connect.Heater2.Control.TD` | s | 0.50 | module_segment |
| PRIH Heater 2 PID Integration Time | `L01S_PRIH_DB_HMI_connect.Heater2.Control.TI` | s | 0.50 | module_segment |
| PRIH Tack Seal Heater PID Proportional Gain | `L01S_PRIH_DB_HMI_connect.HeaterTackSeal.Control.GAIN` | - | 0.50 | module_segment |
| PRIH Tack Seal Heater Manipulated Variable High Limit | `L01S_PRIH_DB_HMI_connect.HeaterTackSeal.Control.LMN_HLM` | % | 0.50 | module_segment |
| PRIH Tack Seal Heater Manipulated Variable Low Limit | `L01S_PRIH_DB_HMI_connect.HeaterTackSeal.Control.LMN_LLM` | % | 0.50 | module_segment |
| PRIH Tack Seal Heater Manual Output Value | `L01S_PRIH_DB_HMI_connect.HeaterTackSeal.Control.MAN` | % | 0.50 | module_segment |
| PRIH Tack Seal Heater Manual-Switch Temperature Deviation | `L01S_PRIH_DB_HMI_connect.HeaterTackSeal.Control.MAN_ON_VALUE` | °C | 0.50 | module_segment |
| PRIH Tack Seal Heater PID Derivative Time | `L01S_PRIH_DB_HMI_connect.HeaterTackSeal.Control.TD` | s | 0.50 | module_segment |
| PRIH Tack Seal Heater PID Integration Time | `L01S_PRIH_DB_HMI_connect.HeaterTackSeal.Control.TI` | s | 0.50 | module_segment |
| PRIH Actual Cycle Time | `L01S_PRIH_DB_HMI_connect.HMIActualTimes.T01` | ms | 0.50 | module_segment |
| PRIH FP03: Print Inspection LHS Enable | `L01S_PRIH_DB_HMI_connect.Selections.FP02` | - | 0.50 | module_segment |
| PRIH FP04: Print Inspection RHS Enable | `L01S_PRIH_DB_HMI_connect.Selections.FP03` | - | 0.50 | module_segment |
| PRIH FP01: Operation Mode Semiautomatic | `L01S_PRIH_DB_HMI_connect.Selections.SemiAuto` | - | 0.50 | module_segment |
| PRIT Print Inspection Job Number (LHS) | `L01S_PRIT_DB_setpoint.Inspection_LHS.JobNr` | - | 0.50 | module_segment |
| PRIT Print Inspection Job Number (RHS) | `L01S_PRIT_DB_setpoint.Inspection_RHS.JobNr` | - | 0.50 | module_segment |
| PRIT Actual Cycle Time | `L01S_PRIT_DB_HMI_connect.HMIActualTimes.T01` | ms | 0.50 | module_segment |
| PRIT FP03: Print Inspection LHS Enable | `L01S_PRIT_DB_HMI_connect.Selections.FP02` | - | 0.50 | module_segment |
| PRIT FP04: Print Inspection RHS Enable | `L01S_PRIT_DB_HMI_connect.Selections.FP03` | - | 0.50 | module_segment |
| PRIT FP01: Operation Mode Semiautomatic | `L01S_PRIT_DB_HMI_connect.Selections.SemiAuto` | - | 0.50 | module_segment |
| PRIH FP01: Hot Stamp Station Enable | `L01S_PRIH_DB_setpoint.Selections.HotStamp` | - | 0.55 | module_segment |
| PRIH FP06: Tack Sealer Enable | `L01S_PRIH_DB_setpoint.Selections.TackSealer` | - | 0.55 | module_segment |
| PRIH Heater 1 Controller Proportional Gain | `L01S_PRIH_IDB_Heater1.DI_TCONT_CP.GAIN` | - | 0.55 | module_segment |
| PRIH Heater 1 Controller Derivative Time | `L01S_PRIH_IDB_Heater1.DI_TCONT_CP.TD` | s | 0.55 | module_segment |
| PRIH Heater 1 Controller Reset Time | `L01S_PRIH_IDB_Heater1.DI_TCONT_CP.TI` | s | 0.55 | module_segment |
| PRIH Heater 2 Controller Proportional Gain | `L01S_PRIH_IDB_Heater2.DI_TCONT_CP.GAIN` | - | 0.55 | module_segment |
| PRIH Heater 2 Controller Derivative Time | `L01S_PRIH_IDB_Heater2.DI_TCONT_CP.TD` | s | 0.55 | module_segment |
| PRIH Heater 2 Controller Reset Time | `L01S_PRIH_IDB_Heater2.DI_TCONT_CP.TI` | s | 0.55 | module_segment |
| PRIH Tack Seal Heater Controller Proportional Gain | `L01S_PRIH_IDB_HeaterTS.DI_TCONT_CP.GAIN` | - | 0.55 | module_segment |
| PRIH Tack Seal Heater Controller Derivative Time | `L01S_PRIH_IDB_HeaterTS.DI_TCONT_CP.TD` | s | 0.55 | module_segment |
| PRIH Tack Seal Heater Controller Reset Time | `L01S_PRIH_IDB_HeaterTS.DI_TCONT_CP.TI` | s | 0.55 | module_segment |
| PRIT FP01: Station Enable | `L01S_PRIT_DB_setpoint.Selections.StationEnabled` | - | 0.55 | module_segment |
| PRIH Heater 1 (Left) Correction Value | `L01S_PRIH_DB_setpoint.Heater1.Correction_Value` | °K | 0.60 | module_segment |
| PRIH Heater 2 (Right) Correction Value | `L01S_PRIH_DB_setpoint.Heater2.Correction_Value` | °K | 0.60 | module_segment |
| PRIH Tack Seal Heater Correction Value | `L01S_PRIH_DB_setpoint.HeaterTackSeal.Correction_Value` | °K | 0.60 | module_segment |
| PRIH T01: Cycle Time | `L01S_PRIH_DB_setpoint.Times.CycleTime` | ms | 0.60 | module_segment |
| PRIH T02: Printing Time (Left) | `L01S_PRIH_DB_setpoint.Times.PrintingTimeLeft` | ms | 0.60 | module_segment |
| PRIH T03: Printing Time (Right) | `L01S_PRIH_DB_setpoint.Times.PrintingTimeRight` | ms | 0.60 | module_segment |
| PRIH T04: Tack Seal Time | `L01S_PRIH_DB_setpoint.Times.TackSealTime` | ms | 0.60 | module_segment |
| PRIH Cycle Counter (Left) | `L01S_PRIH_DB_HMI_connect.Count.CycleCounterLeft` | - | 0.60 | module_segment |
| PRIH Cycle Counter (Right) | `L01S_PRIH_DB_HMI_connect.Count.CycleCounterRight` | - | 0.60 | module_segment |
| PRIH Heater 1 PID Output | `L01S_PRIH_DB_HMI_connect.Heater1.Status.LMN` | % | 0.60 | module_segment |
| PRIH Heater 2 PID Output | `L01S_PRIH_DB_HMI_connect.Heater2.Status.LMN` | % | 0.60 | module_segment |
| PRIH Tack Seal Heater PID Output | `L01S_PRIH_DB_HMI_connect.HeaterTackSeal.Status.LMN` | % | 0.60 | module_segment |
| PRIT T01: Cycle Time | `L01S_PRIT_DB_setpoint.Times.CycleTime` | ms | 0.60 | module_segment |
| PRIT T02: Printing Delay | `L01S_PRIT_DB_setpoint.Times.PrintDelay` | ms | 0.60 | module_segment |
| PRIT Cycle Counter (Left) | `L01S_PRIT_DB_HMI_connect.Count.CycleCounterLeft` | - | 0.60 | module_segment |
| PRIT Cycle Counter (Right) | `L01S_PRIT_DB_HMI_connect.Count.CycleCounterRight` | - | 0.60 | module_segment |
| PRIH Hot Stamp Camera X-Adjust Offset Position | `L01S_PRIH_DB_setpoint.Adjust_X_C.Offset_Pos` | mm | 0.70 | module_segment |
| PRIH Hot Stamp Camera X-Adjust Target Position | `L01S_PRIH_DB_setpoint.Adjust_X_C.Target_Pos` | mm | 0.70 | module_segment |
| PRIH Hot Stamp X-Adjust Offset Position | `L01S_PRIH_DB_setpoint.Adjust_X_HS.Offset_Pos` | mm | 0.70 | module_segment |
| PRIH Hot Stamp X-Adjust Target Position | `L01S_PRIH_DB_setpoint.Adjust_X_HS.Target_Pos` | mm | 0.70 | module_segment |
| PRIH Tack Sealer X-Adjust Offset Position | `L01S_PRIH_DB_setpoint.Adjust_X_TS.Offset_Pos` | mm | 0.70 | module_segment |
| PRIH Tack Sealer X-Adjust Target Position | `L01S_PRIH_DB_setpoint.Adjust_X_TS.Target_Pos` | mm | 0.70 | module_segment |
| PRIH Heater 1 (Left) Lower Alarm Boundary | `L01S_PRIH_DB_setpoint.Heater1.Alarm_Boundary_Down` | °C | 0.70 | module_segment |
| PRIH Heater 1 (Left) Upper Alarm Boundary | `L01S_PRIH_DB_setpoint.Heater1.Alarm_Boundary_Up` | °C | 0.70 | module_segment |
| PRIH Heater 2 (Right) Lower Alarm Boundary | `L01S_PRIH_DB_setpoint.Heater2.Alarm_Boundary_Down` | °C | 0.70 | module_segment |
| PRIH Heater 2 (Right) Upper Alarm Boundary | `L01S_PRIH_DB_setpoint.Heater2.Alarm_Boundary_Up` | °C | 0.70 | module_segment |
| PRIH Tack Seal Heater Lower Alarm Boundary | `L01S_PRIH_DB_setpoint.HeaterTackSeal.Alarm_Boundary_Down` | °C | 0.70 | module_segment |
| PRIH Tack Seal Heater Upper Alarm Boundary | `L01S_PRIH_DB_setpoint.HeaterTackSeal.Alarm_Boundary_Up` | °C | 0.70 | module_segment |
| PRIH Hot Stamp Camera X-Adjust Actual Position | `L01S_PRIH_DB_HMI_connect.Adjust_X_C.ActPos` | mm | 0.70 | module_segment |
| PRIH Hot Stamp X-Adjust Actual Position | `L01S_PRIH_DB_HMI_connect.Adjust_X_HS.ActPos` | mm | 0.70 | module_segment |
| PRIH Tack Sealer X-Adjust Actual Position | `L01S_PRIH_DB_HMI_connect.Adjust_X_TS.ActPos` | mm | 0.70 | module_segment |
| PRIT Camera X-Adjust Offset Position | `L01S_PRIT_DB_setpoint.Adjust_X_C.Offset_Pos` | mm | 0.70 | module_segment |
| PRIT Camera X-Adjust Target Position | `L01S_PRIT_DB_setpoint.Adjust_X_C.Target_Pos` | mm | 0.70 | module_segment |
| PRIT Thermotransfer Head X-Adjust Offset Position | `L01S_PRIT_DB_setpoint.Adjust_X_TH.Offset_Pos` | mm | 0.70 | module_segment |
| PRIT Thermotransfer Head X-Adjust Target Position | `L01S_PRIT_DB_setpoint.Adjust_X_TH.Target_Pos` | mm | 0.70 | module_segment |
| PRIT Camera X-Adjust Actual Position | `L01S_PRIT_DB_HMI_connect.Adjust_X_C.ActPos` | mm | 0.70 | module_segment |
| PRIT Thermotransfer Head X-Adjust Actual Position | `L01S_PRIT_DB_HMI_connect.Adjust_X_TH.ActPos` | mm | 0.70 | module_segment |
| PRIH Heater 1 (Left) Temperature Setpoint | `L01S_PRIH_DB_setpoint.Heater1.Temp_Set` | °C | 0.90 | module_segment |
| PRIH Heater 2 (Right) Temperature Setpoint | `L01S_PRIH_DB_setpoint.Heater2.Temp_Set` | °C | 0.90 | module_segment |
| PRIH Tack Seal Heater Temperature Setpoint | `L01S_PRIH_DB_setpoint.HeaterTackSeal.Temp_Set` | °C | 0.90 | module_segment |
| PRIH Heater 1 (Left) Actual Temperature | `L01S_PRIH_DB_HMI_connect.Heater1.Status.Actual` | °C | 0.90 | module_segment |
| PRIH Heater 2 (Right) Actual Temperature | `L01S_PRIH_DB_HMI_connect.Heater2.Status.Actual` | °C | 0.90 | module_segment |
| PRIH Tack Seal Heater Actual Temperature | `L01S_PRIH_DB_HMI_connect.HeaterTackSeal.Status.Actual` | °C | 0.90 | module_segment |

### FOR filter welding station (Corona printer control module) (MC006-FOR)

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

### COR corona surface-treatment station (printer control module) (MC006-COR)

- 142 candidate tag(s) considered -> 33 kept as genuine parameters (23%).
- Kept tags found by: 33 via *module_segment* (the tag name contains this station's own PLC/module code as a literal segment - the strongest signal available).
- 3 kept parameter(s) below 0.5 confidence - flagged with ⚠ below.

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| COR Station Present in Machine Configuration ⚠ | `GE1_DB_Info.MachineConfiguration.COR` | - | 0.35 | module_segment |
| COR FP02: Disable ASB/ASC Watchdog ⚠ | `L01S_COR_DB_HMI_connect.Selections.FP02` | - | 0.40 | module_segment |
| COR FP01: Operation Mode Semi-Automatic ⚠ | `L01S_COR_DB_HMI_connect.Selections.SemiAuto` | - | 0.45 | module_segment |
| Gap 26: COR Station Low to Splice Web 2 | `GE1_DB_setpoint.StationGaps.COR_StDn_SPLICE_W2` | mm | 0.50 | module_segment |
| Gap 13: COR Station Upper to PRIT Station (Web3) | `GE1_DB_setpoint.StationGaps.COR_StUp_PRIT_St` | mm | 0.50 | module_segment |
| COR FP01: Station Enabled | `L01S_COR_DB_setpoint.Selections.StationEnabled` | - | 0.50 | module_segment |
| COR Delay Start Corona Test | `L01S_COR_DB_HMI_connect.DelayStartTest` | ms | 0.50 | module_segment |
| COR Cycle Time (Actual, T01) | `L01S_COR_DB_HMI_connect.HMIActualTimes.T01` | ms | 0.55 | module_segment |
| COR Cycle Counter | `L01S_COR_DB_HMI_connect.Count.CycleCounter` | - | 0.60 | module_segment |
| COR T02: Corona Suction Time | `L01S_COR_DB_setpoint.Times._02` | ms | 0.65 | module_segment |
| COR T01: Cycle Time Setpoint | `L01S_COR_DB_setpoint.Times.CycleTime` | ms | 0.65 | module_segment |
| COR X-Adjust Down Offset Position | `L01S_COR_DB_setpoint.Adjust_X_D.Offset_Pos` | mm | 0.70 | module_segment |
| COR X-Adjust Down Target Position | `L01S_COR_DB_setpoint.Adjust_X_D.Target_Pos` | mm | 0.70 | module_segment |
| COR X-Adjust Top Offset Position | `L01S_COR_DB_setpoint.Adjust_X_T.Offset_Pos` | mm | 0.70 | module_segment |
| COR X-Adjust Top Target Position | `L01S_COR_DB_setpoint.Adjust_X_T.Target_Pos` | mm | 0.70 | module_segment |
| COR Y-Adjust Down Left Offset Position | `L01S_COR_DB_setpoint.Adjust_Y_D_L.Offset_Pos` | mm | 0.70 | module_segment |
| COR Y-Adjust Down Left Target Position | `L01S_COR_DB_setpoint.Adjust_Y_D_L.Target_Pos` | mm | 0.70 | module_segment |
| COR Y-Adjust Down Right Offset Position | `L01S_COR_DB_setpoint.Adjust_Y_D_R.Offset_Pos` | mm | 0.70 | module_segment |
| COR Y-Adjust Down Right Target Position | `L01S_COR_DB_setpoint.Adjust_Y_D_R.Target_Pos` | mm | 0.70 | module_segment |
| COR Y-Adjust Top Left Offset Position | `L01S_COR_DB_setpoint.Adjust_Y_T_L.Offset_Pos` | mm | 0.70 | module_segment |
| COR Y-Adjust Top Left Target Position | `L01S_COR_DB_setpoint.Adjust_Y_T_L.Target_Pos` | mm | 0.70 | module_segment |
| COR Y-Adjust Top Right Offset Position | `L01S_COR_DB_setpoint.Adjust_Y_T_R.Offset_Pos` | mm | 0.70 | module_segment |
| COR Y-Adjust Top Right Target Position | `L01S_COR_DB_setpoint.Adjust_Y_T_R.Target_Pos` | mm | 0.70 | module_segment |
| COR T03: Corona Process Time 1 | `L01S_COR_DB_setpoint.Times._03` | ms | 0.70 | module_segment |
| COR T04: Corona Delay Time | `L01S_COR_DB_setpoint.Times._04` | ms | 0.70 | module_segment |
| COR T05: Corona Process Time 2 | `L01S_COR_DB_setpoint.Times._05` | ms | 0.70 | module_segment |
| COR T06: Corona Blow-Off Time | `L01S_COR_DB_setpoint.Times._06` | ms | 0.70 | module_segment |
| COR X-Adjust Down Actual Position | `L01S_COR_DB_HMI_connect.Adjust_X_D.ActPos` | mm | 0.70 | module_segment |
| COR X-Adjust Top Actual Position | `L01S_COR_DB_HMI_connect.Adjust_X_T.ActPos` | mm | 0.70 | module_segment |
| COR Y-Adjust Down Left Actual Position | `L01S_COR_DB_HMI_connect.Adjust_Y_D_L.ActPos` | mm | 0.70 | module_segment |
| COR Y-Adjust Down Right Actual Position | `L01S_COR_DB_HMI_connect.Adjust_Y_D_R.ActPos` | mm | 0.70 | module_segment |
| COR Y-Adjust Top Left Actual Position | `L01S_COR_DB_HMI_connect.Adjust_Y_T_L.ActPos` | mm | 0.70 | module_segment |
| COR Y-Adjust Top Right Actual Position | `L01S_COR_DB_HMI_connect.Adjust_Y_T_R.ActPos` | mm | 0.70 | module_segment |

### FHP flange hole-punch station (MC006-FHP)

- 118 candidate tag(s) considered -> 20 kept as genuine parameters (17%).
- Kept tags found by: 20 via *module_segment* (the tag name contains this station's own PLC/module code as a literal segment - the strongest signal available).
- 2 kept parameter(s) below 0.5 confidence - flagged with ⚠ below.

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| FHP Selection: Upper Hole Punches (Non-Woven) ⚠ | `FHP_SelUpperPunch` | - | 0.45 | module_segment |
| FHP FP01: Operation Mode Semi-Automatic ⚠ | `L01S_FHP_DB_HMI_connect.Selections.SemiAuto` | - | 0.45 | module_segment |
| Gap 11: FHP Station to PRIT Inspection (Web3) | `GE1_DB_setpoint.StationGaps.FHP_St_PRIT_Insp` | mm | 0.50 | module_segment |
| Gap 15: FHP Station to Splice Web 3 | `GE1_DB_setpoint.StationGaps.FHP_St_SPLICE_W3` | mm | 0.50 | module_segment |
| Gap 16: FHP Station to Splice Web 4 | `GE1_DB_setpoint.StationGaps.FHP_St_SPLICE_W4` | mm | 0.50 | module_segment |
| FHP FP01: Station Enabled | `L01S_FHP_DB_setpoint.Selections.StationEnabled` | - | 0.50 | module_segment |
| FHP Cycle Time (Actual, T01) | `L01S_FHP_DB_HMI_connect.HMIActualTimes.T01` | ms | 0.55 | module_segment |
| FHP Cycle Counter | `L01S_FHP_DB_HMI_connect.Count.CycleCounter` | - | 0.60 | module_segment |
| FHP T03: Delay of Press Out | `L01S_FHP_DB_setpoint.Times._03` | ms | 0.65 | module_segment |
| FHP T01: Cycle Time Setpoint | `L01S_FHP_DB_setpoint.Times.CycleTime` | ms | 0.65 | module_segment |
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

### BSW backing-seal welding station (MC006-BSW)

- 110 candidate tag(s) considered -> 32 kept as genuine parameters (29%).
- Kept tags found by: 32 via *module_segment* (the tag name contains this station's own PLC/module code as a literal segment - the strongest signal available).
- 1 kept parameter(s) below 0.5 confidence - flagged with ⚠ below.

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| BSW Heater Self-Tuning Excitation Delta ⚠ | `L01S_BSW_DB_HMI_connect.Heater1.Control.TUN_DLMN` | % | 0.40 | module_segment |
| Gap 10: BSW Station to FHP Station (Web34) | `GE1_DB_setpoint.StationGaps.BSW_St_FHP_St` | mm | 0.50 | module_segment |
| BSW Heater PID Proportional Gain | `L01S_BSW_DB_HMI_connect.Heater1.Control.GAIN` | - | 0.50 | module_segment |
| BSW Heater Manipulated Variable High Limit | `L01S_BSW_DB_HMI_connect.Heater1.Control.LMN_HLM` | % | 0.50 | module_segment |
| BSW Heater Manipulated Variable Low Limit | `L01S_BSW_DB_HMI_connect.Heater1.Control.LMN_LLM` | % | 0.50 | module_segment |
| BSW Heater Manual Output Value | `L01S_BSW_DB_HMI_connect.Heater1.Control.MAN` | % | 0.50 | module_segment |
| BSW Heater Manual-Switch Temperature Deviation | `L01S_BSW_DB_HMI_connect.Heater1.Control.MAN_ON_VALUE` | °C | 0.50 | module_segment |
| BSW Heater PID Derivative Time | `L01S_BSW_DB_HMI_connect.Heater1.Control.TD` | s | 0.50 | module_segment |
| BSW Heater PID Integration Time | `L01S_BSW_DB_HMI_connect.Heater1.Control.TI` | s | 0.50 | module_segment |
| BSW Actual Cycle Time | `L01S_BSW_DB_HMI_connect.HMIActualTimes.T01` | ms | 0.50 | module_segment |
| BSW FP02: Stretching Clamp Enable | `L01S_BSW_DB_HMI_connect.Selections.FP02` | - | 0.50 | module_segment |
| BSW FP01: Operation Mode Semiautomatic | `L01S_BSW_DB_HMI_connect.Selections.SemiAuto` | - | 0.50 | module_segment |
| BSW FP01: Station Enable | `L01S_BSW_DB_setpoint.Selections.StationEnabled` | - | 0.55 | module_segment |
| BSW Cooling Fan On Delay | `L01S_BSW_DB_HMI_connect.HMIActualTimes.T22` | ms | 0.55 | module_segment |
| BSW Heater Controller Proportional Gain | `L01S_BSW_IDB_Heater.DI_TCONT_CP.GAIN` | - | 0.55 | module_segment |
| BSW Heater Controller Derivative Time | `L01S_BSW_IDB_Heater.DI_TCONT_CP.TD` | s | 0.55 | module_segment |
| BSW Heater Controller Reset Time | `L01S_BSW_IDB_Heater.DI_TCONT_CP.TI` | s | 0.55 | module_segment |
| BSW Heater Correction Value | `L01S_BSW_DB_setpoint.Heater.Correction_Value` | °K | 0.60 | module_segment |
| BSW T02: Welding Time | `L01S_BSW_DB_setpoint.Times._02` | ms | 0.60 | module_segment |
| BSW T01: Cycle Time | `L01S_BSW_DB_setpoint.Times.CycleTime` | ms | 0.60 | module_segment |
| BSW Cycle Counter | `L01S_BSW_DB_HMI_connect.Count.CycleCounter` | - | 0.60 | module_segment |
| BSW Heater PID Output | `L01S_BSW_DB_HMI_connect.Heater1.Status.LMN` | % | 0.60 | module_segment |
| BSW X-Adjust Offset Position | `L01S_BSW_DB_setpoint.Adujst_X.Offset_Pos` | mm | 0.70 | module_segment |
| BSW X-Adjust Target Position | `L01S_BSW_DB_setpoint.Adujst_X.Target_Pos` | mm | 0.70 | module_segment |
| BSW Y-Adjust Offset Position | `L01S_BSW_DB_setpoint.Adujst_Y.Offset_Pos` | mm | 0.70 | module_segment |
| BSW Y-Adjust Target Position | `L01S_BSW_DB_setpoint.Adujst_Y.Target_Pos` | mm | 0.70 | module_segment |
| BSW Heater Lower Alarm Boundary | `L01S_BSW_DB_setpoint.Heater.Alarm_Boundary_Down` | °C | 0.70 | module_segment |
| BSW Heater Upper Alarm Boundary | `L01S_BSW_DB_setpoint.Heater.Alarm_Boundary_Up` | °C | 0.70 | module_segment |
| BSW X-Adjust Actual Position | `L01S_BSW_DB_HMI_connect.Adujst_X.ActPos` | mm | 0.70 | module_segment |
| BSW Y-Adjust Actual Position | `L01S_BSW_DB_HMI_connect.Adujst_Y.ActPos` | mm | 0.70 | module_segment |
| BSW Heater Temperature Setpoint | `L01S_BSW_DB_setpoint.Heater.Temp_Set` | °C | 0.90 | module_segment |
| BSW Heater Actual Temperature | `L01S_BSW_DB_HMI_connect.Heater1.Status.Actual` | °C | 0.90 | module_segment |

### FWC flange welding station (MC006-FWC)

- 124 candidate tag(s) considered -> 51 kept as genuine parameters (41%).
- Kept tags found by: 51 via *module_segment* (the tag name contains this station's own PLC/module code as a literal segment - the strongest signal available).
- 3 kept parameter(s) below 0.5 confidence - flagged with ⚠ below.

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| FWC Lower Heater Self-Tuning Excitation Delta ⚠ | `L01S_FWC_DB_HMI_connect.HeaterLower.Control.TUN_DLMN` | % | 0.40 | module_segment |
| FWC Flange Inspection Actual Job (LHS) ⚠ | `L01S_FWC_DB_HMI_connect.Inspection._LHS.JobNr` | - | 0.40 | module_segment |
| FWC Flange Inspection Actual Job (RHS) ⚠ | `L01S_FWC_DB_HMI_connect.Inspection._RHS.JobNr` | - | 0.40 | module_segment |
| Gap 08: FWC Inspection to FWC Station (Web34) | `GE1_DB_setpoint.StationGaps.FWC_Insp_FWC_St` | mm | 0.50 | module_segment |
| Gap 09: FWC Station to BSW Station (Web34) | `GE1_DB_setpoint.StationGaps.FWC_St_BSW_St` | mm | 0.50 | module_segment |
| FWC Print Inspection Job Number (LHS) | `L01S_FWC_DB_setpoint.Inspection_LHS.JobNr` | - | 0.50 | module_segment |
| FWC Print Inspection Job Number (RHS) | `L01S_FWC_DB_setpoint.Inspection_RHS.JobNr` | - | 0.50 | module_segment |
| FWC Lower Heater PID Proportional Gain | `L01S_FWC_DB_HMI_connect.HeaterLower.Control.GAIN` | - | 0.50 | module_segment |
| FWC Lower Heater Manipulated Variable High Limit | `L01S_FWC_DB_HMI_connect.HeaterLower.Control.LMN_HLM` | % | 0.50 | module_segment |
| FWC Lower Heater Manipulated Variable Low Limit | `L01S_FWC_DB_HMI_connect.HeaterLower.Control.LMN_LLM` | % | 0.50 | module_segment |
| FWC Lower Heater Manual Output Value | `L01S_FWC_DB_HMI_connect.HeaterLower.Control.MAN` | % | 0.50 | module_segment |
| FWC Lower Heater Manual-Switch Temperature Deviation | `L01S_FWC_DB_HMI_connect.HeaterLower.Control.MAN_ON_VALUE` | °C | 0.50 | module_segment |
| FWC Lower Heater PID Derivative Time | `L01S_FWC_DB_HMI_connect.HeaterLower.Control.TD` | s | 0.50 | module_segment |
| FWC Lower Heater PID Integration Time | `L01S_FWC_DB_HMI_connect.HeaterLower.Control.TI` | s | 0.50 | module_segment |
| FWC Actual Cycle Time | `L01S_FWC_DB_HMI_connect.HMIActualTimes.T01` | ms | 0.50 | module_segment |
| FWC FP03: Flange Inspection LHS Enable | `L01S_FWC_DB_HMI_connect.Selections.FP02` | - | 0.50 | module_segment |
| FWC FP04: Flange Inspection RHS Enable | `L01S_FWC_DB_HMI_connect.Selections.FP03` | - | 0.50 | module_segment |
| FWC FP01: Operation Mode Semiautomatic | `L01S_FWC_DB_HMI_connect.Selections.SemiAuto` | - | 0.50 | module_segment |
| FWC FP01: Station Enable | `L01S_FWC_DB_setpoint.Selections.StationEnabled` | - | 0.55 | module_segment |
| FWC FP04: Welding Belt Selection | `L01S_FWC_DB_setpoint.Selections.WeldingBelt` | - | 0.55 | module_segment |
| FWC Welding Top Jerk (Close) | `L01S_FWC_DB_setpoint.WeldingTop.Jerk_Close` | % | 0.55 | module_segment |
| FWC Welding Top Jerk (Open) | `L01S_FWC_DB_setpoint.WeldingTop.Jerk_Open` | % | 0.55 | module_segment |
| FWC Cooling Fan On Delay | `L01S_FWC_DB_HMI_connect.HMIActualTimes.T22` | ms | 0.55 | module_segment |
| FWC Lower Heater Controller Proportional Gain | `L01S_FWC_IDB_HeaterLower.DI_TCONT_CP.GAIN` | - | 0.55 | module_segment |
| FWC Lower Heater Controller Derivative Time | `L01S_FWC_IDB_HeaterLower.DI_TCONT_CP.TD` | s | 0.55 | module_segment |
| FWC Lower Heater Controller Reset Time | `L01S_FWC_IDB_HeaterLower.DI_TCONT_CP.TI` | s | 0.55 | module_segment |
| FWC Lower Heater Correction Value | `L01S_FWC_DB_setpoint.HeaterLower.Correction_Value` | °K | 0.60 | module_segment |
| FWC T01: Cycle Time | `L01S_FWC_DB_setpoint.Times.CycleTime` | ms | 0.60 | module_segment |
| FWC T02: Welding Time | `L01S_FWC_DB_setpoint.Times.WeldingTime` | ms | 0.60 | module_segment |
| FWC Welding Top Acceleration (Close) | `L01S_FWC_DB_setpoint.WeldingTop.Acc_Close` | % | 0.60 | module_segment |
| FWC Welding Top Acceleration (Open) | `L01S_FWC_DB_setpoint.WeldingTop.Acc_Open` | % | 0.60 | module_segment |
| FWC Welding Top Deceleration (Close) | `L01S_FWC_DB_setpoint.WeldingTop.Dec_Close` | % | 0.60 | module_segment |
| FWC Welding Top Deceleration (Open) | `L01S_FWC_DB_setpoint.WeldingTop.Dec_Open` | % | 0.60 | module_segment |
| FWC Welding Top Position Relative to Close (Load) | `L01S_FWC_DB_setpoint.WeldingTop.Pos_RelLoad` | mm | 0.60 | module_segment |
| FWC Welding Top Velocity (Close) | `L01S_FWC_DB_setpoint.WeldingTop.Velocity_Close` | % | 0.60 | module_segment |
| FWC Welding Top Velocity (Open) | `L01S_FWC_DB_setpoint.WeldingTop.Velocity_Open` | % | 0.60 | module_segment |
| FWC Cycle Counter | `L01S_FWC_DB_HMI_connect.Count.CycleCounter` | - | 0.60 | module_segment |
| FWC Lower Heater PID Output | `L01S_FWC_DB_HMI_connect.HeaterLower.Status.LMN` | % | 0.60 | module_segment |
| FWC Welding Top Maximum Position | `L01S_FWC_DB_HMI_connect.WeldingTop.MaxPos` | mm | 0.60 | module_segment |
| FWC Welding Top Position (Close) | `L01S_FWC_DB_setpoint.WeldingTop.Pos_Close` | mm | 0.65 | module_segment |
| FWC Welding Top Position (Die Change) | `L01S_FWC_DB_setpoint.WeldingTop.Pos_DieChange` | mm | 0.65 | module_segment |
| FWC Welding Top Position (Open) | `L01S_FWC_DB_setpoint.WeldingTop.Pos_Open` | mm | 0.65 | module_segment |
| FWC X-Adjust Offset Position | `L01S_FWC_DB_setpoint.Adjust_X.Offset_Pos` | mm | 0.70 | module_segment |
| FWC X-Adjust Target Position | `L01S_FWC_DB_setpoint.Adjust_X.Target_Pos` | mm | 0.70 | module_segment |
| FWC Lower Heater Lower Alarm Boundary | `L01S_FWC_DB_setpoint.HeaterLower.Alarm_Boundary_Down` | °C | 0.70 | module_segment |
| FWC Lower Heater Upper Alarm Boundary | `L01S_FWC_DB_setpoint.HeaterLower.Alarm_Boundary_Up` | °C | 0.70 | module_segment |
| FWC X-Adjust Actual Position | `L01S_FWC_DB_HMI_connect.Adjust_X.ActPos` | mm | 0.70 | module_segment |
| FWC Welding Top Actual Position | `L01S_FWC_DB_HMI_connect.WeldingTop.ActPos` | mm | 0.70 | module_segment |
| FWC Welding Top Target Position | `L01S_FWC_DB_HMI_connect.WeldingTop.TargetPos` | mm | 0.70 | module_segment |
| FWC Lower Heater Temperature Setpoint | `L01S_FWC_DB_setpoint.HeaterLower.Temp_Set` | °C | 0.90 | module_segment |
| FWC Lower Heater Actual Temperature | `L01S_FWC_DB_HMI_connect.HeaterLower.Status.Actual` | °C | 0.90 | module_segment |

### AF binder-flap welding station (MC006-AF)

- 424 candidate tag(s) considered -> 105 kept as genuine parameters (25%).
- Kept tags found by: 105 via *module_segment* (the tag name contains this station's own PLC/module code as a literal segment - the strongest signal available).
- 2 kept parameter(s) below 0.5 confidence - flagged with ⚠ below.

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| AFL Upper Heater Self-Tuning Excitation Delta ⚠ | `L01S_AFL_DB_HMI_connect.HeaterUpper.Control.TUN_DLMN` | % | 0.40 | module_segment |
| AFR Upper Heater Self-Tuning Excitation Delta ⚠ | `L01S_AFR_DB_HMI_connect.HeaterUpper.Control.TUN_DLMN` | % | 0.40 | module_segment |
| Gap 19: AF Station to FPWR Inspection (Web2) | `GE1_DB_setpoint.StationGaps.AF_St_FPWR_Insp` | mm | 0.50 | module_segment |
| AFL Flap Feed Register Invert Position | `L01S_AFL_DB_HMI_connect.FlapFeedRegister.CMD.InvertPosition` | - | 0.50 | module_segment |
| AFL Upper Heater PID Proportional Gain | `L01S_AFL_DB_HMI_connect.HeaterUpper.Control.GAIN` | - | 0.50 | module_segment |
| AFL Upper Heater Manipulated Variable High Limit | `L01S_AFL_DB_HMI_connect.HeaterUpper.Control.LMN_HLM` | % | 0.50 | module_segment |
| AFL Upper Heater Manipulated Variable Low Limit | `L01S_AFL_DB_HMI_connect.HeaterUpper.Control.LMN_LLM` | % | 0.50 | module_segment |
| AFL Upper Heater Manual Output Value | `L01S_AFL_DB_HMI_connect.HeaterUpper.Control.MAN` | % | 0.50 | module_segment |
| AFL Upper Heater Manual-Switch Temperature Deviation | `L01S_AFL_DB_HMI_connect.HeaterUpper.Control.MAN_ON_VALUE` | °C | 0.50 | module_segment |
| AFL Upper Heater PID Derivative Time | `L01S_AFL_DB_HMI_connect.HeaterUpper.Control.TD` | s | 0.50 | module_segment |
| AFL Upper Heater PID Integration Time | `L01S_AFL_DB_HMI_connect.HeaterUpper.Control.TI` | s | 0.50 | module_segment |
| AFL Actual Cycle Time | `L01S_AFL_DB_HMI_connect.HMIActualTimes.T01` | ms | 0.50 | module_segment |
| AFL FP03: Auto-Correct Enable | `L01S_AFL_DB_HMI_connect.Selections.FP03` | - | 0.50 | module_segment |
| AFL FP02: Invert Unwinder Direction | `L01S_AFL_DB_HMI_connect.Selections.InvDirUw` | - | 0.50 | module_segment |
| AFL FP01: Operation Mode Semiautomatic | `L01S_AFL_DB_HMI_connect.Selections.SemiAuto` | - | 0.50 | module_segment |
| AFR Flap Feed Register Invert Position | `L01S_AFR_DB_HMI_connect.FlapFeedRegister.CMD.InvertPosition` | - | 0.50 | module_segment |
| AFR Upper Heater PID Proportional Gain | `L01S_AFR_DB_HMI_connect.HeaterUpper.Control.GAIN` | - | 0.50 | module_segment |
| AFR Upper Heater Manipulated Variable High Limit | `L01S_AFR_DB_HMI_connect.HeaterUpper.Control.LMN_HLM` | % | 0.50 | module_segment |
| AFR Upper Heater Manipulated Variable Low Limit | `L01S_AFR_DB_HMI_connect.HeaterUpper.Control.LMN_LLM` | % | 0.50 | module_segment |
| AFR Upper Heater Manual Output Value | `L01S_AFR_DB_HMI_connect.HeaterUpper.Control.MAN` | % | 0.50 | module_segment |
| AFR Upper Heater Manual-Switch Temperature Deviation | `L01S_AFR_DB_HMI_connect.HeaterUpper.Control.MAN_ON_VALUE` | °C | 0.50 | module_segment |
| AFR Upper Heater PID Derivative Time | `L01S_AFR_DB_HMI_connect.HeaterUpper.Control.TD` | s | 0.50 | module_segment |
| AFR Upper Heater PID Integration Time | `L01S_AFR_DB_HMI_connect.HeaterUpper.Control.TI` | s | 0.50 | module_segment |
| AFR Actual Cycle Time | `L01S_AFR_DB_HMI_connect.HMIActualTimes.T01` | ms | 0.50 | module_segment |
| AFR FP03: Auto-Correct Enable | `L01S_AFR_DB_HMI_connect.Selections.FP03` | - | 0.50 | module_segment |
| AFR FP02: Invert Unwinder Direction | `L01S_AFR_DB_HMI_connect.Selections.InvDirUw` | - | 0.50 | module_segment |
| AFR FP01: Operation Mode Semiautomatic | `L01S_AFR_DB_HMI_connect.Selections.SemiAuto` | - | 0.50 | module_segment |
| AFL Flap Coil Parts-to-End Counter | `L01S_AFL_DB_setpoint.FlapCoil.CounterToEnd` | - | 0.55 | module_segment |
| AFL FP01: Station Enable | `L01S_AFL_DB_setpoint.Selections.StationEnabled` | - | 0.55 | module_segment |
| AFL Unwinder Low Speed | `L01S_AFL_DB_setpoint.Unwinder.LowSpeed` | - | 0.55 | module_segment |
| AFL Turntable Position 1 Acceleration | `L01S_AFL_DB_setpoint.Turntable._Pos1.Acc` | - | 0.55 | module_segment |
| AFL Turntable Position 1 Deceleration | `L01S_AFL_DB_setpoint.Turntable._Pos1.Dec` | - | 0.55 | module_segment |
| AFL Turntable Position 1 Setpoint | `L01S_AFL_DB_setpoint.Turntable._Pos1.Position` | ° | 0.55 | module_segment |
| AFL Turntable Position 1 Velocity | `L01S_AFL_DB_setpoint.Turntable._Pos1.Velocity` | - | 0.55 | module_segment |
| AFL Turntable Position 2 Acceleration | `L01S_AFL_DB_setpoint.Turntable._Pos2.Acc` | - | 0.55 | module_segment |
| AFL Turntable Position 2 Deceleration | `L01S_AFL_DB_setpoint.Turntable._Pos2.Dec` | - | 0.55 | module_segment |
| AFL Turntable Position 2 Setpoint | `L01S_AFL_DB_setpoint.Turntable._Pos2.Position` | ° | 0.55 | module_segment |
| AFL Turntable Position 2 Velocity | `L01S_AFL_DB_setpoint.Turntable._Pos2.Velocity` | - | 0.55 | module_segment |
| AFL Flap Feed Register Punch Position | `L01S_AFL_DB_HMI_connect.FlapFeedRegister.Set.PosPunch` | - | 0.55 | module_segment |
| AFL Flap Coil Actual Counter | `L01S_AFL_DB_HMI_connect.FlapFeedRegister.States.CoilCounter` | - | 0.55 | module_segment |
| AFL Turntable Actual Position | `L01S_AFL_DB_HMI_connect.Turntable.ActPos` | ° | 0.55 | module_segment |
| AFL Turntable Target Position | `L01S_AFL_DB_HMI_connect.Turntable.TargetPos` | ° | 0.55 | module_segment |
| AFL Upper Heater Controller Proportional Gain | `L01S_AFL_IDB_HeaterUpper.DI_TCONT_CP.GAIN` | - | 0.55 | module_segment |
| AFL Upper Heater Controller Derivative Time | `L01S_AFL_IDB_HeaterUpper.DI_TCONT_CP.TD` | s | 0.55 | module_segment |
| AFL Upper Heater Controller Reset Time | `L01S_AFL_IDB_HeaterUpper.DI_TCONT_CP.TI` | s | 0.55 | module_segment |
| AFR Flap Coil Parts-to-End Counter | `L01S_AFR_DB_setpoint.FlapCoil.CounterToEnd` | - | 0.55 | module_segment |
| AFR FP01: Station Enable | `L01S_AFR_DB_setpoint.Selections.StationEnabled` | - | 0.55 | module_segment |
| AFR Unwinder Low Speed | `L01S_AFR_DB_setpoint.Unwinder.LowSpeed` | - | 0.55 | module_segment |
| AFR Turntable Position 1 Acceleration | `L01S_AFR_DB_setpoint.Turntable._Pos1.Acc` | - | 0.55 | module_segment |
| AFR Turntable Position 1 Deceleration | `L01S_AFR_DB_setpoint.Turntable._Pos1.Dec` | - | 0.55 | module_segment |
| AFR Turntable Position 1 Setpoint | `L01S_AFR_DB_setpoint.Turntable._Pos1.Position` | ° | 0.55 | module_segment |
| AFR Turntable Position 1 Velocity | `L01S_AFR_DB_setpoint.Turntable._Pos1.Velocity` | - | 0.55 | module_segment |
| AFR Turntable Position 2 Acceleration | `L01S_AFR_DB_setpoint.Turntable._Pos2.Acc` | - | 0.55 | module_segment |
| AFR Turntable Position 2 Deceleration | `L01S_AFR_DB_setpoint.Turntable._Pos2.Dec` | - | 0.55 | module_segment |
| AFR Turntable Position 2 Setpoint | `L01S_AFR_DB_setpoint.Turntable._Pos2.Position` | ° | 0.55 | module_segment |
| AFR Turntable Position 2 Velocity | `L01S_AFR_DB_setpoint.Turntable._Pos2.Velocity` | - | 0.55 | module_segment |
| AFR Flap Feed Register Punch Position | `L01S_AFR_DB_HMI_connect.FlapFeedRegister.Set.PosPunch` | - | 0.55 | module_segment |
| AFR Flap Coil Actual Counter | `L01S_AFR_DB_HMI_connect.FlapFeedRegister.States.CoilCounter` | - | 0.55 | module_segment |
| AFR Turntable Actual Position | `L01S_AFR_DB_HMI_connect.Turntable.ActPos` | ° | 0.55 | module_segment |
| AFR Turntable Target Position | `L01S_AFR_DB_HMI_connect.Turntable.TargetPos` | ° | 0.55 | module_segment |
| AFR Upper Heater Controller Proportional Gain | `L01S_AFR_IDB_HeaterUpper.DI_TCONT_CP.GAIN` | - | 0.55 | module_segment |
| AFR Upper Heater Controller Derivative Time | `L01S_AFR_IDB_HeaterUpper.DI_TCONT_CP.TD` | s | 0.55 | module_segment |
| AFR Upper Heater Controller Reset Time | `L01S_AFR_IDB_HeaterUpper.DI_TCONT_CP.TI` | s | 0.55 | module_segment |
| AFL Upper Heater Correction Value | `L01S_AFL_DB_setpoint.HeaterUpper.Correction_Value` | °K | 0.60 | module_segment |
| AFL T05: Blow-Off Time, Punch Loading | `L01S_AFL_DB_setpoint.Times.BlowOffPunchTime` | ms | 0.60 | module_segment |
| AFL T01: Cycle Time | `L01S_AFL_DB_setpoint.Times.CycleTime` | ms | 0.60 | module_segment |
| AFL T06: Feed Clamp Closing Delay | `L01S_AFL_DB_setpoint.Times.FeedClampDelay` | ms | 0.60 | module_segment |
| AFL T03: Punch Time | `L01S_AFL_DB_setpoint.Times.PunchTime` | ms | 0.60 | module_segment |
| AFL T04: Vacuum Time, Loading on Turntable | `L01S_AFL_DB_setpoint.Times.VacLoadTime` | ms | 0.60 | module_segment |
| AFL T02: Welding Time | `L01S_AFL_DB_setpoint.Times.WeldingTime` | ms | 0.60 | module_segment |
| AFL X-Adjust Auto-Correct Setpoint Position | `L01S_AFL_DB_HMI_connect.Adjust_X.AutoCorrectSPPos` | mm | 0.60 | module_segment |
| AFL Y-Adjust Auto-Correct Setpoint Position | `L01S_AFL_DB_HMI_connect.Adjust_Y.AutoCorrectSPPos` | mm | 0.60 | module_segment |
| AFL Cycle Counter | `L01S_AFL_DB_HMI_connect.Count.CycleCounter` | - | 0.60 | module_segment |
| AFL Upper Heater PID Output | `L01S_AFL_DB_HMI_connect.HeaterUpper.Status.LMN` | % | 0.60 | module_segment |
| AFR Upper Heater Correction Value | `L01S_AFR_DB_setpoint.HeaterUpper.Correction_Value` | °K | 0.60 | module_segment |
| AFR T05: Blow-Off Time, Punch Loading | `L01S_AFR_DB_setpoint.Times.BlowOffPunchTime` | ms | 0.60 | module_segment |
| AFR T01: Cycle Time | `L01S_AFR_DB_setpoint.Times.CycleTime` | ms | 0.60 | module_segment |
| AFR T06: Feed Clamp Closing Delay | `L01S_AFR_DB_setpoint.Times.FeedClampDelay` | ms | 0.60 | module_segment |
| AFR T03: Punch Time | `L01S_AFR_DB_setpoint.Times.PunchTime` | ms | 0.60 | module_segment |
| AFR T04: Vacuum Time, Loading on Turntable | `L01S_AFR_DB_setpoint.Times.VacLoadTime` | ms | 0.60 | module_segment |
| AFR T02: Welding Time | `L01S_AFR_DB_setpoint.Times.WeldingTime` | ms | 0.60 | module_segment |
| AFR X-Adjust Auto-Correct Setpoint Position | `L01S_AFR_DB_HMI_connect.Adjust_X.AutoCorrectSPPos` | mm | 0.60 | module_segment |
| AFR Y-Adjust Auto-Correct Setpoint Position | `L01S_AFR_DB_HMI_connect.Adjust_Y.AutoCorrectSPPos` | mm | 0.60 | module_segment |
| AFR Cycle Counter | `L01S_AFR_DB_HMI_connect.Count.CycleCounter` | - | 0.60 | module_segment |
| AFR Upper Heater PID Output | `L01S_AFR_DB_HMI_connect.HeaterUpper.Status.LMN` | % | 0.60 | module_segment |
| AFL X-Adjust Offset Position | `L01S_AFL_DB_setpoint.Adujst_X.Offset_Pos` | mm | 0.70 | module_segment |
| AFL X-Adjust Target Position | `L01S_AFL_DB_setpoint.Adujst_X.Target_Pos` | mm | 0.70 | module_segment |
| AFL Y-Adjust Offset Position | `L01S_AFL_DB_setpoint.Adujst_Y.Offset_Pos` | mm | 0.70 | module_segment |
| AFL Y-Adjust Target Position | `L01S_AFL_DB_setpoint.Adujst_Y.Target_Pos` | mm | 0.70 | module_segment |
| AFL Upper Heater Lower Alarm Boundary | `L01S_AFL_DB_setpoint.HeaterUpper.Alarm_Boundary_Down` | °C | 0.70 | module_segment |
| AFL Upper Heater Upper Alarm Boundary | `L01S_AFL_DB_setpoint.HeaterUpper.Alarm_Boundary_Up` | °C | 0.70 | module_segment |
| AFL X-Adjust Actual Position | `L01S_AFL_DB_HMI_connect.Adjust_X.ActPos` | mm | 0.70 | module_segment |
| AFL Y-Adjust Actual Position | `L01S_AFL_DB_HMI_connect.Adjust_Y.ActPos` | mm | 0.70 | module_segment |
| AFR X-Adjust Offset Position | `L01S_AFR_DB_setpoint.Adujst_X.Offset_Pos` | mm | 0.70 | module_segment |
| AFR X-Adjust Target Position | `L01S_AFR_DB_setpoint.Adujst_X.Target_Pos` | mm | 0.70 | module_segment |
| AFR Y-Adjust Offset Position | `L01S_AFR_DB_setpoint.Adujst_Y.Offset_Pos` | mm | 0.70 | module_segment |
| AFR Y-Adjust Target Position | `L01S_AFR_DB_setpoint.Adujst_Y.Target_Pos` | mm | 0.70 | module_segment |
| AFR Upper Heater Lower Alarm Boundary | `L01S_AFR_DB_setpoint.HeaterUpper.Alarm_Boundary_Down` | °C | 0.70 | module_segment |
| AFR Upper Heater Upper Alarm Boundary | `L01S_AFR_DB_setpoint.HeaterUpper.Alarm_Boundary_Up` | °C | 0.70 | module_segment |
| AFR X-Adjust Actual Position | `L01S_AFR_DB_HMI_connect.Adjust_X.ActPos` | mm | 0.70 | module_segment |
| AFR Y-Adjust Actual Position | `L01S_AFR_DB_HMI_connect.Adjust_Y.ActPos` | mm | 0.70 | module_segment |
| AFL Upper Heater Temperature Setpoint | `L01S_AFL_DB_setpoint.HeaterUpper.Temp_Set` | °C | 0.90 | module_segment |
| AFL Upper Heater Actual Temperature | `L01S_AFL_DB_HMI_connect.HeaterUpper.Status.Actual` | °C | 0.90 | module_segment |
| AFR Upper Heater Temperature Setpoint | `L01S_AFR_DB_setpoint.HeaterUpper.Temp_Set` | °C | 0.90 | module_segment |
| AFR Upper Heater Actual Temperature | `L01S_AFR_DB_HMI_connect.HeaterUpper.Status.Actual` | °C | 0.90 | module_segment |

### VOP viewing-option (vision inspection) station (MC006-VOP)

- 464 candidate tag(s) considered -> 145 kept as genuine parameters (31%).
- Kept tags found by: 145 via *module_segment* (the tag name contains this station's own PLC/module code as a literal segment - the strongest signal available).
- 13 kept parameter(s) below 0.5 confidence - flagged with ⚠ below.

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| Heater Smash Seal LHS y-scaling groundpoint boundary ⚠ | `L01S_VOP_DB_setpoint.HeaterSmashLHS.Y_Scaling_groundpoint` | - | 0.40 | module_segment |
| Heater Smash Seal LHS y-scaling toppoint boundary ⚠ | `L01S_VOP_DB_setpoint.HeaterSmashLHS.Y_Scaling_toppoint` | - | 0.40 | module_segment |
| Heater Smash Seal RHS y-scaling groundpoint boundary ⚠ | `L01S_VOP_DB_setpoint.HeaterSmashRHS.Y_Scaling_groundpoint` | - | 0.40 | module_segment |
| Heater Smash Seal RHS y-scaling toppoint boundary ⚠ | `L01S_VOP_DB_setpoint.HeaterSmashRHS.Y_Scaling_toppoint` | - | 0.40 | module_segment |
| Heater Water Trap LHS y-scaling groundpoint boundary ⚠ | `L01S_VOP_DB_setpoint.HeaterTrapLHS.Y_Scaling_groundpoint` | - | 0.40 | module_segment |
| Heater Water Trap LHS y-scaling toppoint boundary ⚠ | `L01S_VOP_DB_setpoint.HeaterTrapLHS.Y_Scaling_toppoint` | - | 0.40 | module_segment |
| Heater Water Trap RHS y-scaling groundpoint boundary ⚠ | `L01S_VOP_DB_setpoint.HeaterTrapRHS.Y_Scaling_groundpoint` | - | 0.40 | module_segment |
| Heater Water Trap RHS y-scaling toppoint boundary ⚠ | `L01S_VOP_DB_setpoint.HeaterTrapRHS.Y_Scaling_toppoint` | - | 0.40 | module_segment |
| Gap 18: VOP Water Trap to AF Station distance (Web2) ⚠ | `GE1_DB_setpoint.StationGaps.VOP_WaTr_AF_St` | mm | 0.45 | module_segment |
| Heater Smash Seal LHS delta manipulated variable for process excitation (self-tuning) ⚠ | `L01S_VOP_DB_HMI_connect.HeaterSmashLHS.Control.TUN_DLMN` | % | 0.45 | module_segment |
| Heater Smash Seal RHS delta manipulated variable for process excitation (self-tuning) ⚠ | `L01S_VOP_DB_HMI_connect.HeaterSmashRHS.Control.TUN_DLMN` | % | 0.45 | module_segment |
| Heater Water Trap LHS delta manipulated variable for process excitation (self-tuning) ⚠ | `L01S_VOP_DB_HMI_connect.HeaterTrapLHS.Control.TUN_DLMN` | % | 0.45 | module_segment |
| Heater Water Trap RHS delta manipulated variable for process excitation (self-tuning) ⚠ | `L01S_VOP_DB_HMI_connect.HeaterTrapRHS.Control.TUN_DLMN` | % | 0.45 | module_segment |
| Gap 34: VOP Smash Seal to Splice Web 1 distance | `GE1_DB_setpoint.StationGaps.VOP_SmSe_SPLICE_W1` | mm | 0.50 | module_segment |
| Heater Smash Seal LHS manual output value | `L01S_VOP_DB_HMI_connect.HeaterSmashLHS.Control.MAN` | % | 0.50 | module_segment |
| Heater Smash Seal LHS temperature deviation threshold to switch PID to manual | `L01S_VOP_DB_HMI_connect.HeaterSmashLHS.Control.MAN_ON_VALUE` | °C | 0.50 | module_segment |
| Heater Smash Seal RHS manual output value | `L01S_VOP_DB_HMI_connect.HeaterSmashRHS.Control.MAN` | % | 0.50 | module_segment |
| Heater Smash Seal RHS temperature deviation threshold to switch PID to manual | `L01S_VOP_DB_HMI_connect.HeaterSmashRHS.Control.MAN_ON_VALUE` | °C | 0.50 | module_segment |
| Heater Water Trap LHS manual output value | `L01S_VOP_DB_HMI_connect.HeaterTrapLHS.Control.MAN` | % | 0.50 | module_segment |
| Heater Water Trap LHS temperature deviation threshold to switch PID to manual | `L01S_VOP_DB_HMI_connect.HeaterTrapLHS.Control.MAN_ON_VALUE` | °C | 0.50 | module_segment |
| Heater Water Trap RHS manual output value | `L01S_VOP_DB_HMI_connect.HeaterTrapRHS.Control.MAN` | % | 0.50 | module_segment |
| Heater Water Trap RHS temperature deviation threshold to switch PID to manual | `L01S_VOP_DB_HMI_connect.HeaterTrapRHS.Control.MAN_ON_VALUE` | °C | 0.50 | module_segment |
| Cooling fan on delay time (actual) | `L01S_VOP_DB_HMI_connect.HMIActualTimes.T22` | - | 0.50 | module_segment |
| FP04: Unwinder top active LHS (0 = unwinder bottom active LHS) | `L01S_VOP_DB_HMI_connect.Selections.FP04` | - | 0.50 | module_segment |
| FP05: Unwinder top active RHS (0 = unwinder bottom active RHS) | `L01S_VOP_DB_HMI_connect.Selections.FP05` | - | 0.50 | module_segment |
| FP02: Unwinder turning direction LHS (1 = right turn) | `L01S_VOP_DB_HMI_connect.Selections.InvDirUw_LHS` | - | 0.50 | module_segment |
| FP03: Unwinder turning direction RHS (1 = right turn) | `L01S_VOP_DB_HMI_connect.Selections.InvDirUw_RHS` | - | 0.50 | module_segment |
| Splice detected sensor LHS | `L01S_VOP_DB_HMI_connect.SpliceRegister.SpliceDet_LHS` | - | 0.50 | module_segment |
| Splice detected sensor RHS | `L01S_VOP_DB_HMI_connect.SpliceRegister.SpliceDet_RHS` | - | 0.50 | module_segment |
| Gap 33: VOP Smiley Cut to VOP Smash Seal distance (Web1) | `GE1_DB_setpoint.StationGaps.VOP_SmCt_VOP_SmSe` | mm | 0.55 | module_segment |
| Gap 32: VOP Water Trap to VOP Smiley Cut distance (Web1) | `GE1_DB_setpoint.StationGaps.VOP_WaTr_VOP_SmCt` | mm | 0.55 | module_segment |
| Step distance from splice to welding point, LHS | `L01S_VOP_DB_setpoint.SpliceRegister.DistToWeld_LHS` | - | 0.55 | module_segment |
| Step distance from splice to welding point, RHS | `L01S_VOP_DB_setpoint.SpliceRegister.DistToWeld_RHS` | - | 0.55 | module_segment |
| Unwinder LHS low speed setpoint | `L01S_VOP_DB_setpoint.Unwinder_LHS.LowSpeed` | - | 0.55 | module_segment |
| Unwinder RHS low speed setpoint | `L01S_VOP_DB_setpoint.Unwinder_RHS.LowSpeed` | - | 0.55 | module_segment |
| Film low sensor, unwinder bottom LHS | `L01S_VOP_DB_HMI_connect.CoilCounter.FilmLow_Bottom_LHS` | - | 0.55 | module_segment |
| Film low sensor, unwinder bottom RHS | `L01S_VOP_DB_HMI_connect.CoilCounter.FilmLow_Bottom_RHS` | - | 0.55 | module_segment |
| Film low sensor, unwinder top LHS | `L01S_VOP_DB_HMI_connect.CoilCounter.FilmLow_Top_LHS` | - | 0.55 | module_segment |
| Film low sensor, unwinder top RHS | `L01S_VOP_DB_HMI_connect.CoilCounter.FilmLow_Top_RHS` | - | 0.55 | module_segment |
| Heater Smash Seal LHS P - proportional factor | `L01S_VOP_DB_HMI_connect.HeaterSmashLHS.Control.GAIN` | - | 0.55 | module_segment |
| Heater Smash Seal LHS manipulated variable high limit | `L01S_VOP_DB_HMI_connect.HeaterSmashLHS.Control.LMN_HLM` | % | 0.55 | module_segment |
| Heater Smash Seal LHS manipulated variable low limit | `L01S_VOP_DB_HMI_connect.HeaterSmashLHS.Control.LMN_LLM` | % | 0.55 | module_segment |
| Heater Smash Seal LHS D - derivative time | `L01S_VOP_DB_HMI_connect.HeaterSmashLHS.Control.TD` | s | 0.55 | module_segment |
| Heater Smash Seal LHS I - integration time | `L01S_VOP_DB_HMI_connect.HeaterSmashLHS.Control.TI` | s | 0.55 | module_segment |
| Heater Smash Seal RHS P - proportional factor | `L01S_VOP_DB_HMI_connect.HeaterSmashRHS.Control.GAIN` | - | 0.55 | module_segment |
| Heater Smash Seal RHS manipulated variable high limit | `L01S_VOP_DB_HMI_connect.HeaterSmashRHS.Control.LMN_HLM` | % | 0.55 | module_segment |
| Heater Smash Seal RHS manipulated variable low limit | `L01S_VOP_DB_HMI_connect.HeaterSmashRHS.Control.LMN_LLM` | % | 0.55 | module_segment |
| Heater Smash Seal RHS D - derivative time | `L01S_VOP_DB_HMI_connect.HeaterSmashRHS.Control.TD` | s | 0.55 | module_segment |
| Heater Smash Seal RHS I - integration time | `L01S_VOP_DB_HMI_connect.HeaterSmashRHS.Control.TI` | s | 0.55 | module_segment |
| Heater Water Trap LHS P - proportional factor | `L01S_VOP_DB_HMI_connect.HeaterTrapLHS.Control.GAIN` | - | 0.55 | module_segment |
| Heater Water Trap LHS manipulated variable high limit | `L01S_VOP_DB_HMI_connect.HeaterTrapLHS.Control.LMN_HLM` | % | 0.55 | module_segment |
| Heater Water Trap LHS manipulated variable low limit | `L01S_VOP_DB_HMI_connect.HeaterTrapLHS.Control.LMN_LLM` | % | 0.55 | module_segment |
| Heater Water Trap LHS D - derivative time | `L01S_VOP_DB_HMI_connect.HeaterTrapLHS.Control.TD` | s | 0.55 | module_segment |
| Heater Water Trap LHS I - integration time | `L01S_VOP_DB_HMI_connect.HeaterTrapLHS.Control.TI` | s | 0.55 | module_segment |
| Heater Water Trap RHS P - proportional factor | `L01S_VOP_DB_HMI_connect.HeaterTrapRHS.Control.GAIN` | - | 0.55 | module_segment |
| Heater Water Trap RHS manipulated variable high limit | `L01S_VOP_DB_HMI_connect.HeaterTrapRHS.Control.LMN_HLM` | % | 0.55 | module_segment |
| Heater Water Trap RHS manipulated variable low limit | `L01S_VOP_DB_HMI_connect.HeaterTrapRHS.Control.LMN_LLM` | % | 0.55 | module_segment |
| Heater Water Trap RHS D - derivative time | `L01S_VOP_DB_HMI_connect.HeaterTrapRHS.Control.TD` | s | 0.55 | module_segment |
| Heater Water Trap RHS I - integration time | `L01S_VOP_DB_HMI_connect.HeaterTrapRHS.Control.TI` | s | 0.55 | module_segment |
| Cycle time (actual) | `L01S_VOP_DB_HMI_connect.HMIActualTimes.T01` | - | 0.55 | module_segment |
| Counter to film end, unwinder bottom LHS (setpoint) | `L01S_VOP_DB_setpoint.CounterToEnd.Unwinder_Bottom_LHS` | - | 0.60 | module_segment |
| Counter to film end, unwinder bottom RHS (setpoint) | `L01S_VOP_DB_setpoint.CounterToEnd.Unwinder_Bottom_RHS` | - | 0.60 | module_segment |
| Counter to film end, unwinder top LHS (setpoint) | `L01S_VOP_DB_setpoint.CounterToEnd.Unwinder_Top_LHS` | - | 0.60 | module_segment |
| Counter to film end, unwinder top RHS (setpoint) | `L01S_VOP_DB_setpoint.CounterToEnd.Unwinder_Top_RHS` | - | 0.60 | module_segment |
| Heater Smash Seal LHS correction value for controller | `L01S_VOP_DB_setpoint.HeaterSmashLHS.Correction_Value` | °C | 0.60 | module_segment |
| Heater Smash Seal RHS correction value for controller | `L01S_VOP_DB_setpoint.HeaterSmashRHS.Correction_Value` | °C | 0.60 | module_segment |
| Heater Water Trap LHS correction value for controller | `L01S_VOP_DB_setpoint.HeaterTrapLHS.Correction_Value` | °C | 0.60 | module_segment |
| Heater Water Trap RHS correction value for controller | `L01S_VOP_DB_setpoint.HeaterTrapRHS.Correction_Value` | °C | 0.60 | module_segment |
| Counter to film end (actual), unwinder bottom LHS | `L01S_VOP_DB_HMI_connect.CoilCounter.Unwinder_Bottom_LHS` | - | 0.60 | module_segment |
| Counter to film end (actual), unwinder bottom RHS | `L01S_VOP_DB_HMI_connect.CoilCounter.Unwinder_Bottom_RHS` | - | 0.60 | module_segment |
| Counter to film end (actual), unwinder top LHS | `L01S_VOP_DB_HMI_connect.CoilCounter.Unwinder_Top_LHS` | - | 0.60 | module_segment |
| Counter to film end (actual), unwinder top RHS | `L01S_VOP_DB_HMI_connect.CoilCounter.Unwinder_Top_RHS` | - | 0.60 | module_segment |
| Lower Clamp Feed gearing factor from lower chain | `L01S_VOP_DB_setpoint.LowerClampFeed.GearingFactorSync` | % | 0.65 | module_segment |
| FP04: Smash Seal function enabled | `L01S_VOP_DB_setpoint.Selections.SmashSealEnabled` | - | 0.65 | module_segment |
| FP05: Smiley Cut function enabled | `L01S_VOP_DB_setpoint.Selections.SmileyCutEnabled` | - | 0.65 | module_segment |
| FP06: Water Trap function enabled | `L01S_VOP_DB_setpoint.Selections.WaterTrapEnabled` | - | 0.65 | module_segment |
| Heater Smash Seal LHS PID output | `L01S_VOP_DB_HMI_connect.HeaterSmashLHS.Status.LMN` | % | 0.65 | module_segment |
| Heater Smash Seal RHS PID output | `L01S_VOP_DB_HMI_connect.HeaterSmashRHS.Status.LMN` | % | 0.65 | module_segment |
| Heater Water Trap LHS PID output | `L01S_VOP_DB_HMI_connect.HeaterTrapLHS.Status.LMN` | % | 0.65 | module_segment |
| Heater Water Trap RHS PID output | `L01S_VOP_DB_HMI_connect.HeaterTrapRHS.Status.LMN` | % | 0.65 | module_segment |
| Cycle counter (production count) | `L01S_VOP_DB_HMI_connect.Count.CycleCounter` | - | 0.70 | module_segment |
| Heater Smash Seal LHS proportional gain | `L01S_VOP_IDB_HeaterSS_LH.DI_TCONT_CP.GAIN` | - | 0.70 | module_segment |
| Heater Smash Seal RHS proportional gain | `L01S_VOP_IDB_HeaterSS_RH.DI_TCONT_CP.GAIN` | - | 0.70 | module_segment |
| Heater Water Trap LHS proportional gain | `L01S_VOP_IDB_HeaterWT_LH.DI_TCONT_CP.GAIN` | - | 0.70 | module_segment |
| Heater Water Trap RHS proportional gain | `L01S_VOP_IDB_HeaterWT_RH.DI_TCONT_CP.GAIN` | - | 0.70 | module_segment |
| Heater Smash Seal LHS lower alarm boundary | `L01S_VOP_DB_setpoint.HeaterSmashLHS.Alarm_Boundary_Down` | °C | 0.75 | module_segment |
| Heater Smash Seal LHS upper alarm boundary | `L01S_VOP_DB_setpoint.HeaterSmashLHS.Alarm_Boundary_Up` | °C | 0.75 | module_segment |
| Heater Smash Seal RHS lower alarm boundary | `L01S_VOP_DB_setpoint.HeaterSmashRHS.Alarm_Boundary_Down` | °C | 0.75 | module_segment |
| Heater Smash Seal RHS upper alarm boundary | `L01S_VOP_DB_setpoint.HeaterSmashRHS.Alarm_Boundary_Up` | °C | 0.75 | module_segment |
| Heater Water Trap LHS lower alarm boundary | `L01S_VOP_DB_setpoint.HeaterTrapLHS.Alarm_Boundary_Down` | °C | 0.75 | module_segment |
| Heater Water Trap LHS upper alarm boundary | `L01S_VOP_DB_setpoint.HeaterTrapLHS.Alarm_Boundary_Up` | °C | 0.75 | module_segment |
| Heater Water Trap RHS lower alarm boundary | `L01S_VOP_DB_setpoint.HeaterTrapRHS.Alarm_Boundary_Down` | °C | 0.75 | module_segment |
| Heater Water Trap RHS upper alarm boundary | `L01S_VOP_DB_setpoint.HeaterTrapRHS.Alarm_Boundary_Up` | °C | 0.75 | module_segment |
| Lower Clamp Feed backward acceleration | `L01S_VOP_DB_setpoint.LowerClampFeed.Backward.Acc` | % | 0.75 | module_segment |
| Lower Clamp Feed backward deceleration | `L01S_VOP_DB_setpoint.LowerClampFeed.Backward.Dec` | % | 0.75 | module_segment |
| Lower Clamp Feed backward velocity | `L01S_VOP_DB_setpoint.LowerClampFeed.Backward.Velocity` | % | 0.75 | module_segment |
| T01: cycle time setpoint | `L01S_VOP_DB_setpoint.Times.CycleTime` | - | 0.75 | module_segment |
| T04: Smiley Cut punch time setpoint | `L01S_VOP_DB_setpoint.Times.PunchSmileyCutTime` | - | 0.75 | module_segment |
| Welding Belt Y-adjust offset position | `L01S_VOP_DB_setpoint.WeldingBeltAdjust_Y.Offset_Pos` | mm | 0.75 | module_segment |
| Heater Smash Seal LHS derivative time | `L01S_VOP_IDB_HeaterSS_LH.DI_TCONT_CP.TD` | s | 0.75 | module_segment |
| Heater Smash Seal LHS reset time | `L01S_VOP_IDB_HeaterSS_LH.DI_TCONT_CP.TI` | s | 0.75 | module_segment |
| Heater Smash Seal RHS derivative time | `L01S_VOP_IDB_HeaterSS_RH.DI_TCONT_CP.TD` | s | 0.75 | module_segment |
| Heater Smash Seal RHS reset time | `L01S_VOP_IDB_HeaterSS_RH.DI_TCONT_CP.TI` | s | 0.75 | module_segment |
| Heater Water Trap LHS derivative time | `L01S_VOP_IDB_HeaterWT_LH.DI_TCONT_CP.TD` | s | 0.75 | module_segment |
| Heater Water Trap LHS reset time | `L01S_VOP_IDB_HeaterWT_LH.DI_TCONT_CP.TI` | s | 0.75 | module_segment |
| Heater Water Trap RHS derivative time | `L01S_VOP_IDB_HeaterWT_RH.DI_TCONT_CP.TD` | s | 0.75 | module_segment |
| Heater Water Trap RHS reset time | `L01S_VOP_IDB_HeaterWT_RH.DI_TCONT_CP.TI` | s | 0.75 | module_segment |
| VOP Fife web guide offset position | `L01S_VOP_DB_setpoint.Adjust_VOP_Fife_Web_1.Offset_Pos` | mm | 0.80 | module_segment |
| VOP Fife web guide target position | `L01S_VOP_DB_setpoint.Adjust_VOP_Fife_Web_1.Target_Pos` | mm | 0.80 | module_segment |
| Lower Clamp Feed backward target position | `L01S_VOP_DB_setpoint.LowerClampFeed.Backward.Position` | mm | 0.80 | module_segment |
| Lower Clamp Feed forward target position | `L01S_VOP_DB_setpoint.LowerClampFeed.Forward.Position` | mm | 0.80 | module_segment |
| Smash Seal X-adjust offset position | `L01S_VOP_DB_setpoint.SmashSealAdjust_X.Offset_Pos` | mm | 0.80 | module_segment |
| Smash Seal X-adjust target position | `L01S_VOP_DB_setpoint.SmashSealAdjust_X.Target_Pos` | mm | 0.80 | module_segment |
| Smash Seal Y-adjust offset position | `L01S_VOP_DB_setpoint.SmashSealAdjust_Y.Offset_Pos` | mm | 0.80 | module_segment |
| Smash Seal Y-adjust target position | `L01S_VOP_DB_setpoint.SmashSealAdjust_Y.Target_Pos` | mm | 0.80 | module_segment |
| Smiley Cut X-adjust offset position | `L01S_VOP_DB_setpoint.SmileyCutAdjust_X.Offset_Pos` | mm | 0.80 | module_segment |
| Smiley Cut X-adjust target position | `L01S_VOP_DB_setpoint.SmileyCutAdjust_X.Target_Pos` | mm | 0.80 | module_segment |
| Strip Distance Y-adjust offset position | `L01S_VOP_DB_setpoint.StripDistance_Y.Offset_Pos` | mm | 0.80 | module_segment |
| Strip Distance Y-adjust target position | `L01S_VOP_DB_setpoint.StripDistance_Y.Target_Pos` | mm | 0.80 | module_segment |
| T02: Smash Seal welding time setpoint, LHS | `L01S_VOP_DB_setpoint.Times.WeldingSmashSealTimeLHS` | - | 0.80 | module_segment |
| T03: Smash Seal welding time setpoint, RHS | `L01S_VOP_DB_setpoint.Times.WeldingSmashSealTimeRHS` | - | 0.80 | module_segment |
| T05: Water Trap welding time setpoint, LHS | `L01S_VOP_DB_setpoint.Times.WeldingWaterTrapTimeLHS` | - | 0.80 | module_segment |
| T06: Water Trap welding time setpoint, RHS | `L01S_VOP_DB_setpoint.Times.WeldingWaterTrapTimeRHS` | - | 0.80 | module_segment |
| Water Trap X-adjust offset position | `L01S_VOP_DB_setpoint.WaterTrapAdjust_X.Offset_Pos` | mm | 0.80 | module_segment |
| Water Trap X-adjust target position | `L01S_VOP_DB_setpoint.WaterTrapAdjust_X.Target_Pos` | mm | 0.80 | module_segment |
| Water Trap Y-adjust offset position | `L01S_VOP_DB_setpoint.WaterTrapAdjust_Y.Offset_Pos` | mm | 0.80 | module_segment |
| Water Trap Y-adjust target position | `L01S_VOP_DB_setpoint.WaterTrapAdjust_Y.Target_Pos` | mm | 0.80 | module_segment |
| VOP Fife web guide actual position | `L01S_VOP_DB_HMI_connect.Adjust_VOP_Fife_Web_1.ActPos` | mm | 0.80 | module_segment |
| Lower Clamp Feed actual position | `L01S_VOP_DB_HMI_connect.LowerClampFeed.ActPos` | mm | 0.80 | module_segment |
| Lower Clamp Feed target position (actual) | `L01S_VOP_DB_HMI_connect.LowerClampFeed.TargetPos` | mm | 0.80 | module_segment |
| Smash Seal X-adjust actual position | `L01S_VOP_DB_HMI_connect.SmashSealAdjust_X.ActPos` | mm | 0.80 | module_segment |
| Smash Seal Y-adjust actual position | `L01S_VOP_DB_HMI_connect.SmashSealAdjust_Y.ActPos` | mm | 0.80 | module_segment |
| Smiley Cut X-adjust actual position | `L01S_VOP_DB_HMI_connect.SmileyCutAdjust_X.ActPos` | mm | 0.80 | module_segment |
| Strip Distance Y-adjust actual position | `L01S_VOP_DB_HMI_connect.StripDistance_Y.ActPos` | mm | 0.80 | module_segment |
| Water Trap X-adjust actual position | `L01S_VOP_DB_HMI_connect.WaterTrapAdjust_X.ActPos` | mm | 0.80 | module_segment |
| Water Trap Y-adjust actual position | `L01S_VOP_DB_HMI_connect.WaterTrapAdjust_Y.ActPos` | mm | 0.80 | module_segment |
| Welding Belt Y-adjust actual position | `L01S_VOP_DB_HMI_connect.WeldingBeltAdjust_Y.ActPos` | mm | 0.80 | module_segment |
| Heater Smash Seal LHS temperature setpoint | `L01S_VOP_DB_setpoint.HeaterSmashLHS.Temp_Set` | °C | 0.90 | module_segment |
| Heater Smash Seal RHS temperature setpoint | `L01S_VOP_DB_setpoint.HeaterSmashRHS.Temp_Set` | °C | 0.90 | module_segment |
| Heater Water Trap LHS temperature setpoint | `L01S_VOP_DB_setpoint.HeaterTrapLHS.Temp_Set` | °C | 0.90 | module_segment |
| Heater Water Trap RHS temperature setpoint | `L01S_VOP_DB_setpoint.HeaterTrapRHS.Temp_Set` | °C | 0.90 | module_segment |
| Heater Smash Seal LHS actual temperature | `L01S_VOP_DB_HMI_connect.HeaterSmashLHS.Status.Actual` | °C | 0.90 | module_segment |
| Heater Smash Seal RHS actual temperature | `L01S_VOP_DB_HMI_connect.HeaterSmashRHS.Status.Actual` | °C | 0.90 | module_segment |
| Heater Water Trap LHS actual temperature | `L01S_VOP_DB_HMI_connect.HeaterTrapLHS.Status.Actual` | °C | 0.90 | module_segment |
| Heater Water Trap RHS actual temperature | `L01S_VOP_DB_HMI_connect.HeaterTrapRHS.Status.Actual` | °C | 0.90 | module_segment |

### PWC periphery welding station (MC006-PWC)

- 196 candidate tag(s) considered -> 81 kept as genuine parameters (41%).
- Kept tags found by: 81 via *module_segment* (the tag name contains this station's own PLC/module code as a literal segment - the strongest signal available).
- 4 kept parameter(s) below 0.5 confidence - flagged with ⚠ below.

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| Gripper Feed Selection Enabled ⚠ | `L01S_PWC_DB_setpoint.Selections.GripperFeed` | - | 0.40 | module_segment |
| Station Enabled Selection ⚠ | `L01S_PWC_DB_setpoint.Selections.StationEnabled` | - | 0.40 | module_segment |
| Lower Heater Controller Heating Active ⚠ | `L01S_PWC_DB_HMI_connect.HeaterLower.Status.Heater_ControllerHeating` | - | 0.40 | module_segment |
| Upper Heater Controller Heating Active ⚠ | `L01S_PWC_DB_HMI_connect.HeaterUpper.Status.Heater_ControllerHeating` | - | 0.40 | module_segment |
| Welding Top Force Curve (Servo Table) | `L01S_PWC_DB_weldcurves.Curves.Force` | N | 0.50 | module_segment |
| Welding Top Position Curve (Servo Table) | `L01S_PWC_DB_weldcurves.Curves.Position` | mm | 0.50 | module_segment |
| Station Gap: PWC Station to AF Station (Gap 27, PRIH selected) | `GE1_DB_setpoint.StationGaps.PWC_St_AF_St` | - | 0.55 | module_segment |
| Station Gap: PWC Station to FWC Inspection (Gap 07) | `GE1_DB_setpoint.StationGaps.PWC_St_FWC_Insp` | - | 0.55 | module_segment |
| Station Gap: PWC Station to VOP Water Trap (Gap 17, PRIT/COR/VOP selected) | `GE1_DB_setpoint.StationGaps.PWC_St_VOP_WaTr` | - | 0.55 | module_segment |
| Cooling Plate Temperature (from PWC) | `GE1_DB_interface.PWC_COMMUNICATION._FROM.TempCoolingPlate` | °C | 0.55 | module_segment |
| Delay: Gripper Feed Back Stroke In Position | `L01S_PWC_DB_setpoint.Times._04` | - | 0.55 | module_segment |
| Delay: Magnetic Clutch Close | `L01S_PWC_DB_setpoint.Times._05` | - | 0.55 | module_segment |
| Lower Heater Self-Tuning Excitation Delta | `L01S_PWC_DB_HMI_connect.HeaterLower.Control.TUN_DLMN` | % | 0.55 | module_segment |
| Upper Heater Self-Tuning Excitation Delta | `L01S_PWC_DB_HMI_connect.HeaterUpper.Control.TUN_DLMN` | % | 0.55 | module_segment |
| Delay: Cooling Fan On | `L01S_PWC_DB_HMI_connect.HMIActualTimes.T22` | - | 0.55 | module_segment |
| Lower Heater Manual Output Value | `L01S_PWC_DB_HMI_connect.HeaterLower.Control.MAN` | % | 0.60 | module_segment |
| Upper Heater Manual Output Value | `L01S_PWC_DB_HMI_connect.HeaterUpper.Control.MAN` | % | 0.60 | module_segment |
| Actual Cycle Time | `L01S_PWC_DB_HMI_connect.HMIActualTimes.T01` | - | 0.60 | module_segment |
| Cycle Time Setpoint | `L01S_PWC_DB_setpoint.Times.CycleTime` | - | 0.65 | module_segment |
| Cycle Counter | `L01S_PWC_DB_HMI_connect.Count.CycleCounter` | - | 0.65 | module_segment |
| Lower Heater Manipulated Variable High Limit | `L01S_PWC_DB_HMI_connect.HeaterLower.Control.LMN_HLM` | % | 0.65 | module_segment |
| Lower Heater Manipulated Variable Low Limit | `L01S_PWC_DB_HMI_connect.HeaterLower.Control.LMN_LLM` | % | 0.65 | module_segment |
| Lower Heater Temperature Deviation Threshold for Manual Switchover | `L01S_PWC_DB_HMI_connect.HeaterLower.Control.MAN_ON_VALUE` | °C | 0.65 | module_segment |
| Upper Heater Manipulated Variable High Limit | `L01S_PWC_DB_HMI_connect.HeaterUpper.Control.LMN_HLM` | % | 0.65 | module_segment |
| Upper Heater Manipulated Variable Low Limit | `L01S_PWC_DB_HMI_connect.HeaterUpper.Control.LMN_LLM` | % | 0.65 | module_segment |
| Upper Heater Temperature Deviation Threshold for Manual Switchover | `L01S_PWC_DB_HMI_connect.HeaterUpper.Control.MAN_ON_VALUE` | °C | 0.65 | module_segment |
| Lower Heater Controller Proportional Gain (Raw) | `L01S_PWC_IDB_HeaterLower.DI_TCONT_CP.GAIN` | - | 0.65 | module_segment |
| Upper Heater Controller Proportional Gain (Raw) | `L01S_PWC_IDB_HeaterUpper.DI_TCONT_CP.GAIN` | - | 0.65 | module_segment |
| Welding Top External Force Calibration Value 1 | `L01S_PWC_DB_setpoint.WeldingTop.Calibration.ExternalForce1` | kN | 0.70 | module_segment |
| Welding Top External Force Calibration Value 2 | `L01S_PWC_DB_setpoint.WeldingTop.Calibration.ExternalForce2` | kN | 0.70 | module_segment |
| Welding Top Load Cell Calibration Point 1 | `L01S_PWC_DB_setpoint.WeldingTop.Calibration.LoadCellPoint1` | % | 0.70 | module_segment |
| Welding Top Load Cell Calibration Point 2 | `L01S_PWC_DB_setpoint.WeldingTop.Calibration.LoadCellPoint2` | % | 0.70 | module_segment |
| Welding Top Relative Position Controller Range | `L01S_PWC_DB_setpoint.WeldingTop.Pos_RelController` | mm | 0.70 | module_segment |
| Welding Top Relative Position Release Foil | `L01S_PWC_DB_setpoint.WeldingTop.Pos_RelFoil` | mm | 0.70 | module_segment |
| Lower Heater PID Proportional Gain | `L01S_PWC_DB_HMI_connect.HeaterLower.Control.GAIN` | - | 0.70 | module_segment |
| Lower Heater PID Derivative Time | `L01S_PWC_DB_HMI_connect.HeaterLower.Control.TD` | s | 0.70 | module_segment |
| Lower Heater PID Integral Time | `L01S_PWC_DB_HMI_connect.HeaterLower.Control.TI` | s | 0.70 | module_segment |
| Upper Heater PID Proportional Gain | `L01S_PWC_DB_HMI_connect.HeaterUpper.Control.GAIN` | - | 0.70 | module_segment |
| Upper Heater PID Derivative Time | `L01S_PWC_DB_HMI_connect.HeaterUpper.Control.TD` | s | 0.70 | module_segment |
| Upper Heater PID Integral Time | `L01S_PWC_DB_HMI_connect.HeaterUpper.Control.TI` | s | 0.70 | module_segment |
| Lower Heater Controller Derivative Time (Raw) | `L01S_PWC_IDB_HeaterLower.DI_TCONT_CP.TD` | s | 0.70 | module_segment |
| Lower Heater Controller Reset (Integral) Time (Raw) | `L01S_PWC_IDB_HeaterLower.DI_TCONT_CP.TI` | s | 0.70 | module_segment |
| Upper Heater Controller Derivative Time (Raw) | `L01S_PWC_IDB_HeaterUpper.DI_TCONT_CP.TD` | s | 0.70 | module_segment |
| Upper Heater Controller Reset (Integral) Time (Raw) | `L01S_PWC_IDB_HeaterUpper.DI_TCONT_CP.TI` | s | 0.70 | module_segment |
| Welding Top Closing Jerk | `L01S_PWC_DB_setpoint.WeldingTop.Jerk_Close` | % | 0.75 | module_segment |
| Welding Top Opening Jerk | `L01S_PWC_DB_setpoint.WeldingTop.Jerk_Open` | % | 0.75 | module_segment |
| Welding Top Die Change Position | `L01S_PWC_DB_setpoint.WeldingTop.Pos_DieChange` | mm | 0.75 | module_segment |
| Lower Heater PID Output | `L01S_PWC_DB_HMI_connect.HeaterLower.Status.LMN` | % | 0.75 | module_segment |
| Upper Heater PID Output | `L01S_PWC_DB_HMI_connect.HeaterUpper.Status.LMN` | % | 0.75 | module_segment |
| Lower Heater Controller Correction Value | `L01S_PWC_DB_setpoint.HeaterLower.Correction_Value` | °K | 0.80 | module_segment |
| Upper Heater Controller Correction Value | `L01S_PWC_DB_setpoint.HeaterUpper.Correction_Value` | °K | 0.80 | module_segment |
| Welding Top Closing Acceleration | `L01S_PWC_DB_setpoint.WeldingTop.Acc_Close` | % | 0.80 | module_segment |
| Welding Top Opening Acceleration | `L01S_PWC_DB_setpoint.WeldingTop.Acc_Open` | % | 0.80 | module_segment |
| Welding Top Closing Deceleration | `L01S_PWC_DB_setpoint.WeldingTop.Dec_Close` | % | 0.80 | module_segment |
| Welding Top Opening Deceleration | `L01S_PWC_DB_setpoint.WeldingTop.Dec_Open` | % | 0.80 | module_segment |
| Welding Top Maximum Position | `L01S_PWC_DB_setpoint.WeldingTop.Pos_Max` | mm | 0.80 | module_segment |
| Welding Top Open Position | `L01S_PWC_DB_setpoint.WeldingTop.Pos_Open` | mm | 0.80 | module_segment |
| Welding Top Closing Velocity | `L01S_PWC_DB_setpoint.WeldingTop.Velocity_Close` | % | 0.80 | module_segment |
| Welding Top Opening Velocity | `L01S_PWC_DB_setpoint.WeldingTop.Velocity_Open` | % | 0.80 | module_segment |
| X-Axis Adjustment Offset Position | `L01S_PWC_DB_setpoint.Adjust_X.Offset_Pos` | mm | 0.85 | module_segment |
| X-Axis Adjustment Target Position | `L01S_PWC_DB_setpoint.Adjust_X.Target_Pos` | mm | 0.85 | module_segment |
| Y-Axis Adjustment Offset Position | `L01S_PWC_DB_setpoint.Adjust_Y.Offset_Pos` | mm | 0.85 | module_segment |
| Y-Axis Adjustment Target Position | `L01S_PWC_DB_setpoint.Adjust_Y.Target_Pos` | mm | 0.85 | module_segment |
| Lower Heater Temperature Alarm Lower Boundary | `L01S_PWC_DB_setpoint.HeaterLower.Alarm_Boundary_Down` | °C | 0.85 | module_segment |
| Lower Heater Temperature Alarm Upper Boundary | `L01S_PWC_DB_setpoint.HeaterLower.Alarm_Boundary_Up` | °C | 0.85 | module_segment |
| Upper Heater Temperature Alarm Lower Boundary | `L01S_PWC_DB_setpoint.HeaterUpper.Alarm_Boundary_Down` | °C | 0.85 | module_segment |
| Upper Heater Temperature Alarm Upper Boundary | `L01S_PWC_DB_setpoint.HeaterUpper.Alarm_Boundary_Up` | °C | 0.85 | module_segment |
| Welding Top Force Alarm Lower Boundary | `L01S_PWC_DB_setpoint.WeldingTop.Alarm_Boundary_Down` | kN | 0.85 | module_segment |
| Welding Top Force Alarm Upper Boundary | `L01S_PWC_DB_setpoint.WeldingTop.Alarm_Boundary_Up` | kN | 0.85 | module_segment |
| X-Axis Adjustment Actual Position | `L01S_PWC_DB_HMI_connect.Adjust_X.ActPos` | mm | 0.85 | module_segment |
| Y-Axis Adjustment Actual Position | `L01S_PWC_DB_HMI_connect.Adjust_Y.ActPos` | mm | 0.85 | module_segment |
| Welding Top Actual Load Cell Value | `L01S_PWC_DB_HMI_connect.WeldingTop.LoadCell` | % | 0.85 | module_segment |
| Welding Top Target Position | `L01S_PWC_DB_HMI_connect.WeldingTop.TargetPos` | mm | 0.85 | module_segment |
| Lower Heater Temperature Setpoint | `L01S_PWC_DB_setpoint.HeaterLower.Temp_Set` | °C | 0.90 | module_segment |
| Upper Heater Temperature Setpoint | `L01S_PWC_DB_setpoint.HeaterUpper.Temp_Set` | °C | 0.90 | module_segment |
| Welding Time Setpoint | `L01S_PWC_DB_setpoint.Times.WeldingTime` | - | 0.90 | module_segment |
| Welding Top Target Force | `L01S_PWC_DB_setpoint.WeldingTop.Force` | kN | 0.90 | module_segment |
| Lower Heater Actual Temperature | `L01S_PWC_DB_HMI_connect.HeaterLower.Status.Actual` | °C | 0.90 | module_segment |
| Upper Heater Actual Temperature | `L01S_PWC_DB_HMI_connect.HeaterUpper.Status.Actual` | °C | 0.90 | module_segment |
| Welding Top Actual Force | `L01S_PWC_DB_HMI_connect.WeldingTop.ActForce` | N | 0.90 | module_segment |
| Welding Top Actual Position | `L01S_PWC_DB_HMI_connect.WeldingTop.ActPos` | mm | 0.90 | module_segment |

### ASC labelling station, curved closure, post-heating (MC006-ASC)

- 390 candidate tag(s) considered -> 136 kept as genuine parameters (35%).
- Kept tags found by: 136 via *module_segment* (the tag name contains this station's own PLC/module code as a literal segment - the strongest signal available).
- 26 kept parameter(s) below 0.5 confidence - flagged with ⚠ below.

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| Heater Bottom delta manipulated variable for process excitation (200=20.0%) ⚠ | `L01S_ASCL_DB_HMI_connect.HeaterBottom.Control.TUN_DLMN` | % | 0.30 | module_segment |
| Heater Top delta manipulated variable for process excitation (200=20.0%) ⚠ | `L01S_ASCL_DB_HMI_connect.HeaterTop.Control.TUN_DLMN` | % | 0.30 | module_segment |
| Heater Bottom delta manipulated variable for process excitation (200=20.0%) ⚠ | `L01S_ASCR_DB_HMI_connect.HeaterBottom.Control.TUN_DLMN` | % | 0.30 | module_segment |
| Heater Top delta manipulated variable for process excitation (200=20.0%) ⚠ | `L01S_ASCR_DB_HMI_connect.HeaterTop.Control.TUN_DLMN` | % | 0.30 | module_segment |
| Labeler lower: operating mode automatic (only automatic functions) ⚠ | `L01S_ASCL_DB_HMI_connect.Labeler_lwr.Command.OpModeAutomatic` | - | 0.35 | module_segment |
| Labeler lower: operating mode service (only service functions) ⚠ | `L01S_ASCL_DB_HMI_connect.Labeler_lwr.Command.OpModeService` | - | 0.35 | module_segment |
| Labeler upper: operating mode automatic (only automatic functions) ⚠ | `L01S_ASCL_DB_HMI_connect.Labeler_up.Command.OpModeAutomatic` | - | 0.35 | module_segment |
| Labeler upper: operating mode service (only service functions) ⚠ | `L01S_ASCL_DB_HMI_connect.Labeler_up.Command.OpModeService` | - | 0.35 | module_segment |
| Labeler lower: operating mode automatic (only automatic functions) ⚠ | `L01S_ASCR_DB_HMI_connect.Labeler_lwr.Command.OpModeAutomatic` | - | 0.35 | module_segment |
| Labeler lower: operating mode service (only service functions) ⚠ | `L01S_ASCR_DB_HMI_connect.Labeler_lwr.Command.OpModeService` | - | 0.35 | module_segment |
| Labeler upper: operating mode automatic (only automatic functions) ⚠ | `L01S_ASCR_DB_HMI_connect.Labeler_up.Command.OpModeAutomatic` | - | 0.35 | module_segment |
| Labeler upper: operating mode service (only service functions) ⚠ | `L01S_ASCR_DB_HMI_connect.Labeler_up.Command.OpModeService` | - | 0.35 | module_segment |
| Type of labeler lower (1 = Member single, 2 = Member 3, 3 = Member3 spread wide) ⚠ | `L01S_ASCL_DB_setpoint.Labeler.LType` | - | 0.40 | module_segment |
| Type of labeler lower (1 = Member single, 2 = Member 3, 3 = Member3 spread wide) ⚠ | `L01S_ASCR_DB_setpoint.Labeler.LType` | - | 0.40 | module_segment |
| FP03: autocorrect enabled top ⚠ | `L01S_ASCL_DB_HMI_connect.Selections.FP03` | - | 0.40 | module_segment |
| FP04: autocorrect enabled bottom ⚠ | `L01S_ASCL_DB_HMI_connect.Selections.FP04` | - | 0.40 | module_segment |
| FP01: operation mode semiautomatic ⚠ | `L01S_ASCL_DB_HMI_connect.Selections.SemiAuto` | - | 0.40 | module_segment |
| FP03: autocorrect enabled top ⚠ | `L01S_ASCR_DB_HMI_connect.Selections.FP03` | - | 0.40 | module_segment |
| FP04: autocorrect enabled bottom ⚠ | `L01S_ASCR_DB_HMI_connect.Selections.FP04` | - | 0.40 | module_segment |
| FP01: operation mode semiautomatic ⚠ | `L01S_ASCR_DB_HMI_connect.Selections.SemiAuto` | - | 0.40 | module_segment |
| FP01: station enabled ⚠ | `L01S_ASCL_DB_setpoint.Selections.StationEnabled` | - | 0.45 | module_segment |
| FP01: station enabled ⚠ | `L01S_ASCR_DB_setpoint.Selections.StationEnabled` | - | 0.45 | module_segment |
| Heater Bottom manual value (0-100%) ⚠ | `L01S_ASCL_DB_HMI_connect.HeaterBottom.Control.MAN` | % | 0.45 | module_segment |
| Heater Top manual value (0-100%) ⚠ | `L01S_ASCL_DB_HMI_connect.HeaterTop.Control.MAN` | % | 0.45 | module_segment |
| Heater Bottom manual value (0-100%) ⚠ | `L01S_ASCR_DB_HMI_connect.HeaterBottom.Control.MAN` | % | 0.45 | module_segment |
| Heater Top manual value (0-100%) ⚠ | `L01S_ASCR_DB_HMI_connect.HeaterTop.Control.MAN` | % | 0.45 | module_segment |
| Actual Counter at End (down) | `L01S_ASCL_DB_HMI_connect.CoilCounter.CoilCounter_Uown` | - | 0.50 | module_segment |
| Actual Counter at End (up) | `L01S_ASCL_DB_HMI_connect.CoilCounter.CoilCounter_Up` | - | 0.50 | module_segment |
| Actual Counter at End (down) | `L01S_ASCR_DB_HMI_connect.CoilCounter.CoilCounter_Uown` | - | 0.50 | module_segment |
| Actual Counter at End (up) | `L01S_ASCR_DB_HMI_connect.CoilCounter.CoilCounter_Up` | - | 0.50 | module_segment |
| Heater Bottom: temperature difference to switch PID to manual (200=20.0 °C) | `L01S_ASCL_DB_HMI_connect.HeaterBottom.Control.MAN_ON_VALUE` | °C | 0.50 | module_segment |
| Heater Top: temperature difference to switch PID to manual (200=20.0 °C) | `L01S_ASCL_DB_HMI_connect.HeaterTop.Control.MAN_ON_VALUE` | °C | 0.50 | module_segment |
| Heater Bottom: temperature difference to switch PID to manual (200=20.0 °C) | `L01S_ASCR_DB_HMI_connect.HeaterBottom.Control.MAN_ON_VALUE` | °C | 0.50 | module_segment |
| Heater Top: temperature difference to switch PID to manual (200=20.0 °C) | `L01S_ASCR_DB_HMI_connect.HeaterTop.Control.MAN_ON_VALUE` | °C | 0.50 | module_segment |
| Number how many Parts are on Coil to End when Sensor detact (down count) | `L01S_ASCL_DB_setpoint.CoilCounter.CounterToEnd_Down` | - | 0.55 | module_segment |
| Number how many Parts are on Coil to End when Sensor detact (up count) | `L01S_ASCL_DB_setpoint.CoilCounter.CounterToEnd_Up` | - | 0.55 | module_segment |
| Number how many Parts are on Coil to End when Sensor detact (down count) | `L01S_ASCR_DB_setpoint.CoilCounter.CounterToEnd_Down` | - | 0.55 | module_segment |
| Number how many Parts are on Coil to End when Sensor detact (up count) | `L01S_ASCR_DB_setpoint.CoilCounter.CounterToEnd_Up` | - | 0.55 | module_segment |
| T02: heating time | `L01S_ASCL_DB_setpoint.Times._02` | s | 0.55 | module_segment |
| T02: heating time | `L01S_ASCR_DB_setpoint.Times._02` | s | 0.55 | module_segment |
| Cycle time (actual, HMI) | `L01S_ASCL_DB_HMI_connect.HMIActualTimes.T01` | s | 0.55 | module_segment |
| Cycle time (actual, HMI) | `L01S_ASCR_DB_HMI_connect.HMIActualTimes.T01` | s | 0.55 | module_segment |
| Gap 04: ASC Preheat to ASC Station (Web1234) | `GE1_DB_setpoint.StationGaps.ASC_Pht_ASC_St` | mm | 0.60 | module_segment |
| Gap 05: ASC Station to ASB Station (Web1234) | `GE1_DB_setpoint.StationGaps.ASC_St_ASB_St` | mm | 0.60 | module_segment |
| T01: cycle time (setpoint) | `L01S_ASCL_DB_setpoint.Times.CycleTime` | s | 0.60 | module_segment |
| T01: cycle time (setpoint) | `L01S_ASCR_DB_setpoint.Times.CycleTime` | s | 0.60 | module_segment |
| Cycle counter | `L01S_ASCL_DB_HMI_connect.Count.CycleCounter` | - | 0.60 | module_segment |
| Cycle counter | `L01S_ASCR_DB_HMI_connect.Count.CycleCounter` | - | 0.60 | module_segment |
| Heater Bottom PID output (0-100%) | `L01S_ASCL_DB_HMI_connect.HeaterBottom.Status.LMN` | % | 0.60 | module_segment |
| Heater Top PID output (0-100%) | `L01S_ASCL_DB_HMI_connect.HeaterTop.Status.LMN` | % | 0.60 | module_segment |
| Heater Bottom PID output (0-100%) | `L01S_ASCR_DB_HMI_connect.HeaterBottom.Status.LMN` | % | 0.60 | module_segment |
| Heater Top PID output (0-100%) | `L01S_ASCR_DB_HMI_connect.HeaterTop.Status.LMN` | % | 0.60 | module_segment |
| Heater Bottom manipulated variable high limit (0-100%) | `L01S_ASCL_DB_HMI_connect.HeaterBottom.Control.LMN_HLM` | % | 0.65 | module_segment |
| Heater Bottom manipulated variable low limit (0-100%) | `L01S_ASCL_DB_HMI_connect.HeaterBottom.Control.LMN_LLM` | % | 0.65 | module_segment |
| Heater Top manipulated variable high limit (0-100%) | `L01S_ASCL_DB_HMI_connect.HeaterTop.Control.LMN_HLM` | % | 0.65 | module_segment |
| Heater Top manipulated variable low limit (0-100%) | `L01S_ASCL_DB_HMI_connect.HeaterTop.Control.LMN_LLM` | % | 0.65 | module_segment |
| Heater Bottom manipulated variable high limit (0-100%) | `L01S_ASCR_DB_HMI_connect.HeaterBottom.Control.LMN_HLM` | % | 0.65 | module_segment |
| Heater Bottom manipulated variable low limit (0-100%) | `L01S_ASCR_DB_HMI_connect.HeaterBottom.Control.LMN_LLM` | % | 0.65 | module_segment |
| Heater Top manipulated variable high limit (0-100%) | `L01S_ASCR_DB_HMI_connect.HeaterTop.Control.LMN_HLM` | % | 0.65 | module_segment |
| Heater Top manipulated variable low limit (0-100%) | `L01S_ASCR_DB_HMI_connect.HeaterTop.Control.LMN_LLM` | % | 0.65 | module_segment |
| Heater Bottom P - proportional factor (100 = 10.0) | `L01S_ASCL_DB_HMI_connect.HeaterBottom.Control.GAIN` | - | 0.70 | module_segment |
| Heater Top P - proportional factor (100 = 10.0) | `L01S_ASCL_DB_HMI_connect.HeaterTop.Control.GAIN` | - | 0.70 | module_segment |
| Heater Bottom P - proportional factor (100 = 10.0) | `L01S_ASCR_DB_HMI_connect.HeaterBottom.Control.GAIN` | - | 0.70 | module_segment |
| Heater Top P - proportional factor (100 = 10.0) | `L01S_ASCR_DB_HMI_connect.HeaterTop.Control.GAIN` | - | 0.70 | module_segment |
| X-adjust lower: auto correct setpoint position [mm] | `L01S_ASCL_DB_HMI_connect.x_adjust_lwr.AutoCorrectSPPos` | mm | 0.70 | module_segment |
| X-adjust upper: auto correct setpoint position [mm] | `L01S_ASCL_DB_HMI_connect.x_adjust_up.AutoCorrectSPPos` | mm | 0.70 | module_segment |
| Y-adjust lower: auto correct setpoint position [mm] | `L01S_ASCL_DB_HMI_connect.y_adjust_lwr.AutoCorrectSPPos` | mm | 0.70 | module_segment |
| Y-adjust upper: auto correct setpoint position [mm] | `L01S_ASCL_DB_HMI_connect.y_adjust_up.AutoCorrectSPPos` | mm | 0.70 | module_segment |
| X-adjust lower: auto correct setpoint position [mm] | `L01S_ASCR_DB_HMI_connect.x_adjust_lwr.AutoCorrectSPPos` | mm | 0.70 | module_segment |
| X-adjust upper: auto correct setpoint position [mm] | `L01S_ASCR_DB_HMI_connect.x_adjust_up.AutoCorrectSPPos` | mm | 0.70 | module_segment |
| Y-adjust lower: auto correct setpoint position [mm] | `L01S_ASCR_DB_HMI_connect.y_adjust_lwr.AutoCorrectSPPos` | mm | 0.70 | module_segment |
| Y-adjust upper: auto correct setpoint position [mm] | `L01S_ASCR_DB_HMI_connect.y_adjust_up.AutoCorrectSPPos` | mm | 0.70 | module_segment |
| Heater Bottom D - derivative time (100 = 10.0s) | `L01S_ASCL_DB_HMI_connect.HeaterBottom.Control.TD` | s | 0.75 | module_segment |
| Heater Bottom I - integration time (1000 = 100.0s) | `L01S_ASCL_DB_HMI_connect.HeaterBottom.Control.TI` | s | 0.75 | module_segment |
| Heater Top D - derivative time (100 = 10.0s) | `L01S_ASCL_DB_HMI_connect.HeaterTop.Control.TD` | s | 0.75 | module_segment |
| Heater Top I - integration time (1000 = 100.0s) | `L01S_ASCL_DB_HMI_connect.HeaterTop.Control.TI` | s | 0.75 | module_segment |
| Heater Bottom D - derivative time (100 = 10.0s) | `L01S_ASCR_DB_HMI_connect.HeaterBottom.Control.TD` | s | 0.75 | module_segment |
| Heater Bottom I - integration time (1000 = 100.0s) | `L01S_ASCR_DB_HMI_connect.HeaterBottom.Control.TI` | s | 0.75 | module_segment |
| Heater Top D - derivative time (100 = 10.0s) | `L01S_ASCR_DB_HMI_connect.HeaterTop.Control.TD` | s | 0.75 | module_segment |
| Heater Top I - integration time (1000 = 100.0s) | `L01S_ASCR_DB_HMI_connect.HeaterTop.Control.TI` | s | 0.75 | module_segment |
| Heater lower: proportional gain | `L01S_ASCL_IDB_Heater_lwr.DI_TCONT_CP.GAIN` | - | 0.75 | module_segment |
| Heater upper: proportional gain | `L01S_ASCL_IDB_Heater_up.DI_TCONT_CP.GAIN` | - | 0.75 | module_segment |
| Heater lower: proportional gain | `L01S_ASCR_IDB_Heater_lwr.DI_TCONT_CP.GAIN` | - | 0.75 | module_segment |
| Heater upper: proportional gain | `L01S_ASCR_IDB_Heater_up.DI_TCONT_CP.GAIN` | - | 0.75 | module_segment |
| X-adjust lower: offset position [mm] | `L01S_ASCL_DB_setpoint.x_adjust_lwr.Offset_Pos` | mm | 0.80 | module_segment |
| X-adjust lower: target position [mm] | `L01S_ASCL_DB_setpoint.x_adjust_lwr.Target_Pos` | mm | 0.80 | module_segment |
| X-adjust upper: offset position [mm] | `L01S_ASCL_DB_setpoint.x_adjust_up.Offset_Pos` | mm | 0.80 | module_segment |
| X-adjust upper: target position [mm] | `L01S_ASCL_DB_setpoint.x_adjust_up.Target_Pos` | mm | 0.80 | module_segment |
| Y-adjust lower: offset position [mm] | `L01S_ASCL_DB_setpoint.y_adjust_lwr.Offset_Pos` | mm | 0.80 | module_segment |
| Y-adjust lower: target position [mm] | `L01S_ASCL_DB_setpoint.y_adjust_lwr.Target_Pos` | mm | 0.80 | module_segment |
| Y-adjust upper: offset position [mm] | `L01S_ASCL_DB_setpoint.y_adjust_up.Offset_Pos` | mm | 0.80 | module_segment |
| Y-adjust upper: target position [mm] | `L01S_ASCL_DB_setpoint.y_adjust_up.Target_Pos` | mm | 0.80 | module_segment |
| X-adjust lower: offset position [mm] | `L01S_ASCR_DB_setpoint.x_adjust_lwr.Offset_Pos` | mm | 0.80 | module_segment |
| X-adjust lower: target position [mm] | `L01S_ASCR_DB_setpoint.x_adjust_lwr.Target_Pos` | mm | 0.80 | module_segment |
| X-adjust upper: offset position [mm] | `L01S_ASCR_DB_setpoint.x_adjust_up.Offset_Pos` | mm | 0.80 | module_segment |
| X-adjust upper: target position [mm] | `L01S_ASCR_DB_setpoint.x_adjust_up.Target_Pos` | mm | 0.80 | module_segment |
| Y-adjust lower: offset position [mm] | `L01S_ASCR_DB_setpoint.y_adjust_lwr.Offset_Pos` | mm | 0.80 | module_segment |
| Y-adjust lower: target position [mm] | `L01S_ASCR_DB_setpoint.y_adjust_lwr.Target_Pos` | mm | 0.80 | module_segment |
| Y-adjust upper: offset position [mm] | `L01S_ASCR_DB_setpoint.y_adjust_up.Offset_Pos` | mm | 0.80 | module_segment |
| Y-adjust upper: target position [mm] | `L01S_ASCR_DB_setpoint.y_adjust_up.Target_Pos` | mm | 0.80 | module_segment |
| X-adjust lower: actual position [mm] | `L01S_ASCL_DB_HMI_connect.x_adjust_lwr.ActPos` | mm | 0.80 | module_segment |
| X-adjust upper: actual position [mm] | `L01S_ASCL_DB_HMI_connect.x_adjust_up.ActPos` | mm | 0.80 | module_segment |
| Y-adjust lower: actual position [mm] | `L01S_ASCL_DB_HMI_connect.y_adjust_lwr.ActPos` | mm | 0.80 | module_segment |
| Y-adjust upper: actual position [mm] | `L01S_ASCL_DB_HMI_connect.y_adjust_up.ActPos` | mm | 0.80 | module_segment |
| X-adjust lower: actual position [mm] | `L01S_ASCR_DB_HMI_connect.x_adjust_lwr.ActPos` | mm | 0.80 | module_segment |
| X-adjust upper: actual position [mm] | `L01S_ASCR_DB_HMI_connect.x_adjust_up.ActPos` | mm | 0.80 | module_segment |
| Y-adjust lower: actual position [mm] | `L01S_ASCR_DB_HMI_connect.y_adjust_lwr.ActPos` | mm | 0.80 | module_segment |
| Y-adjust upper: actual position [mm] | `L01S_ASCR_DB_HMI_connect.y_adjust_up.ActPos` | mm | 0.80 | module_segment |
| Heater lower: derivative time [s] | `L01S_ASCL_IDB_Heater_lwr.DI_TCONT_CP.TD` | s | 0.80 | module_segment |
| Heater lower: reset time [s] | `L01S_ASCL_IDB_Heater_lwr.DI_TCONT_CP.TI` | s | 0.80 | module_segment |
| Heater upper: derivative time [s] | `L01S_ASCL_IDB_Heater_up.DI_TCONT_CP.TD` | s | 0.80 | module_segment |
| Heater upper: reset time [s] | `L01S_ASCL_IDB_Heater_up.DI_TCONT_CP.TI` | s | 0.80 | module_segment |
| Heater lower: derivative time [s] | `L01S_ASCR_IDB_Heater_lwr.DI_TCONT_CP.TD` | s | 0.80 | module_segment |
| Heater lower: reset time [s] | `L01S_ASCR_IDB_Heater_lwr.DI_TCONT_CP.TI` | s | 0.80 | module_segment |
| Heater upper: derivative time [s] | `L01S_ASCR_IDB_Heater_up.DI_TCONT_CP.TD` | s | 0.80 | module_segment |
| Heater upper: reset time [s] | `L01S_ASCR_IDB_Heater_up.DI_TCONT_CP.TI` | s | 0.80 | module_segment |
| Heater Bottom lower alarm boundary [°C] | `L01S_ASCL_DB_setpoint.HeaterBottom.Alarm_Boundary_Down` | °C | 0.85 | module_segment |
| Heater Bottom upper alarm boundary [°C] | `L01S_ASCL_DB_setpoint.HeaterBottom.Alarm_Boundary_Up` | °C | 0.85 | module_segment |
| Hot stamp heater right correction value for controller [°K] | `L01S_ASCL_DB_setpoint.HeaterBottom.Correction_Value` | °K | 0.85 | module_segment |
| Heater Top lower alarm boundary [°C] | `L01S_ASCL_DB_setpoint.HeaterTop.Alarm_Boundary_Down` | °C | 0.85 | module_segment |
| Heater Top upper alarm boundary [°C] | `L01S_ASCL_DB_setpoint.HeaterTop.Alarm_Boundary_Up` | °C | 0.85 | module_segment |
| Hot stamp heater left correction value for controller [°K] | `L01S_ASCL_DB_setpoint.HeaterTop.Correction_Value` | °K | 0.85 | module_segment |
| Heater Bottom lower alarm boundary [°C] | `L01S_ASCR_DB_setpoint.HeaterBottom.Alarm_Boundary_Down` | °C | 0.85 | module_segment |
| Heater Bottom upper alarm boundary [°C] | `L01S_ASCR_DB_setpoint.HeaterBottom.Alarm_Boundary_Up` | °C | 0.85 | module_segment |
| Hot stamp heater right correction value for controller [°K] | `L01S_ASCR_DB_setpoint.HeaterBottom.Correction_Value` | °K | 0.85 | module_segment |
| Heater Top lower alarm boundary [°C] | `L01S_ASCR_DB_setpoint.HeaterTop.Alarm_Boundary_Down` | °C | 0.85 | module_segment |
| Heater Top upper alarm boundary [°C] | `L01S_ASCR_DB_setpoint.HeaterTop.Alarm_Boundary_Up` | °C | 0.85 | module_segment |
| Hot stamp heater left correction value for controller [°K] | `L01S_ASCR_DB_setpoint.HeaterTop.Correction_Value` | °K | 0.85 | module_segment |
| Heater Bottom actual temperature for HMI (1000 = 100.0 °C) | `L01S_ASCL_DB_HMI_connect.HeaterBottom.Status.Actual` | °C | 0.85 | module_segment |
| Heater Top actual temperature for HMI (1000 = 100.0 °C) | `L01S_ASCL_DB_HMI_connect.HeaterTop.Status.Actual` | °C | 0.85 | module_segment |
| Heater Bottom actual temperature for HMI (1000 = 100.0 °C) | `L01S_ASCR_DB_HMI_connect.HeaterBottom.Status.Actual` | °C | 0.85 | module_segment |
| Heater Top actual temperature for HMI (1000 = 100.0 °C) | `L01S_ASCR_DB_HMI_connect.HeaterTop.Status.Actual` | °C | 0.85 | module_segment |
| Hot stamp heater right temperature setpoint [°C] | `L01S_ASCL_DB_setpoint.HeaterBottom.Temp_Set` | °C | 0.90 | module_segment |
| Hot stamp heater left temperature setpoint [°C] | `L01S_ASCL_DB_setpoint.HeaterTop.Temp_Set` | °C | 0.90 | module_segment |
| Hot stamp heater right temperature setpoint [°C] | `L01S_ASCR_DB_setpoint.HeaterBottom.Temp_Set` | °C | 0.90 | module_segment |
| Hot stamp heater left temperature setpoint [°C] | `L01S_ASCR_DB_setpoint.HeaterTop.Temp_Set` | °C | 0.90 | module_segment |

### ASB labelling station, curved closure (MC006-ASB)

- 237 candidate tag(s) considered -> 66 kept as genuine parameters (28%).
- Kept tags found by: 66 via *module_segment* (the tag name contains this station's own PLC/module code as a literal segment - the strongest signal available).
- 4 kept parameter(s) below 0.5 confidence - flagged with ⚠ below.

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| Operating mode: automatic, automatic functions only (ASBL) ⚠ | `L01S_ASBL_DB_HMI_connect.Labeler.Command.OpModeAutomatic` | - | 0.35 | module_segment |
| Operating mode: service, service functions only (ASBL) ⚠ | `L01S_ASBL_DB_HMI_connect.Labeler.Command.OpModeService` | - | 0.35 | module_segment |
| Operating mode: automatic, automatic functions only (ASBR) ⚠ | `L01S_ASBR_DB_HMI_connect.Labeler.Command.OpModeAutomatic` | - | 0.35 | module_segment |
| Operating mode: service, service functions only (ASBR) ⚠ | `L01S_ASBR_DB_HMI_connect.Labeler.Command.OpModeService` | - | 0.35 | module_segment |
| Labeler type (1 = Binder, 2 = Binder 90°) (ASBL) | `L01S_ASBL_DB_setpoint.Labeler.LType` | - | 0.50 | module_segment |
| Actual inspection job number, bottom (ASBL) | `L01S_ASBL_DB_HMI_connect.Inspection.Bottom.JobNr` | - | 0.50 | module_segment |
| Actual inspection job number, top (ASBL) | `L01S_ASBL_DB_HMI_connect.Inspection.Top.JobNr` | - | 0.50 | module_segment |
| Labeler type (1 = Binder, 2 = Binder 90°) (ASBR) | `L01S_ASBR_DB_setpoint.Labeler.LType` | - | 0.50 | module_segment |
| Actual inspection job number, bottom (ASBR) | `L01S_ASBR_DB_HMI_connect.Inspection.Bottom.JobNr` | - | 0.50 | module_segment |
| Actual inspection job number, top (ASBR) | `L01S_ASBR_DB_HMI_connect.Inspection.Top.JobNr` | - | 0.50 | module_segment |
| Inspection job number, bottom - setpoint (ASBL) | `L01S_ASBL_DB_setpoint.Inspection_Bottom.JobNr` | - | 0.55 | module_segment |
| Inspection job number, top - setpoint (ASBL) | `L01S_ASBL_DB_setpoint.Inspection_Top.JobNr` | - | 0.55 | module_segment |
| Label inspection enabled, LHS (FP02) (ASBL) | `L01S_ASBL_DB_HMI_connect.Selections.FP02` | - | 0.55 | module_segment |
| Autocorrect enabled (FP03) (ASBL) | `L01S_ASBL_DB_HMI_connect.Selections.FP03` | - | 0.55 | module_segment |
| Operation mode: semiautomatic (FP01) (ASBL) | `L01S_ASBL_DB_HMI_connect.Selections.SemiAuto` | - | 0.55 | module_segment |
| Inspection job number, bottom - setpoint (ASBR) | `L01S_ASBR_DB_setpoint.Inspection_Bottom.JobNr` | - | 0.55 | module_segment |
| Inspection job number, top - setpoint (ASBR) | `L01S_ASBR_DB_setpoint.Inspection_Top.JobNr` | - | 0.55 | module_segment |
| Label inspection enabled, RHS (FP02) (ASBR) | `L01S_ASBR_DB_HMI_connect.Selections.FP02` | - | 0.55 | module_segment |
| Autocorrect enabled (FP03) (ASBR) | `L01S_ASBR_DB_HMI_connect.Selections.FP03` | - | 0.55 | module_segment |
| Operation mode: semiautomatic (FP01) (ASBR) | `L01S_ASBR_DB_HMI_connect.Selections.SemiAuto` | - | 0.55 | module_segment |
| Station enabled (FP01) (ASBL) | `L01S_ASBL_DB_setpoint.Selections.StationEnabled` | - | 0.60 | module_segment |
| Station enabled (FP01) (ASBR) | `L01S_ASBR_DB_setpoint.Selections.StationEnabled` | - | 0.60 | module_segment |
| Gap 03: ASC Inspection to ASC Preheat (Web1234) | `GE1_DB_setpoint.StationGaps.ASB_Insp_ASC_Pht` | mm | 0.70 | module_segment |
| Gap 06: ASB Station to PWC Station (Web1234) | `GE1_DB_setpoint.StationGaps.ASB_St_PWC_St` | mm | 0.70 | module_segment |
| Label adjustment in X (ASBL) | `L01S_ASBL_DB_setpoint.LabelAdjust.X` | mm | 0.75 | module_segment |
| Label adjustment in Y (ASBL) | `L01S_ASBL_DB_setpoint.LabelAdjust.Y` | mm | 0.75 | module_segment |
| Label adjustment in X (ASBR) | `L01S_ASBR_DB_setpoint.LabelAdjust.X` | mm | 0.75 | module_segment |
| Label adjustment in Y (ASBR) | `L01S_ASBR_DB_setpoint.LabelAdjust.Y` | mm | 0.75 | module_segment |
| Number of parts on coil to end when sensor detected (ASBL) | `L01S_ASBL_DB_setpoint.CoilCounter.CounterToEnd` | count | 0.80 | module_segment |
| Actual coil counter at end (ASBL) | `L01S_ASBL_DB_HMI_connect.CoilCounter.CoilCounter` | count | 0.80 | module_segment |
| Cycle counter (ASBL) | `L01S_ASBL_DB_HMI_connect.Count.CycleCounter` | count | 0.80 | module_segment |
| X-adjust auto-correct setpoint position [mm] (ASBL) | `L01S_ASBL_DB_HMI_connect.x_adjust.AutoCorrectSPPos` | mm | 0.80 | module_segment |
| Y-adjust auto-correct setpoint position [mm] (ASBL) | `L01S_ASBL_DB_HMI_connect.y_adjust.AutoCorrectSPPos` | mm | 0.80 | module_segment |
| Number of parts on coil to end when sensor detected (ASBR) | `L01S_ASBR_DB_setpoint.CoilCounter.CounterToEnd` | count | 0.80 | module_segment |
| Actual coil counter at end (ASBR) | `L01S_ASBR_DB_HMI_connect.CoilCounter.CoilCounter` | count | 0.80 | module_segment |
| Cycle counter (ASBR) | `L01S_ASBR_DB_HMI_connect.Count.CycleCounter` | count | 0.80 | module_segment |
| X-adjust auto-correct setpoint position [mm] (ASBR) | `L01S_ASBR_DB_HMI_connect.x_adjust.AutoCorrectSPPos` | mm | 0.80 | module_segment |
| Y-adjust auto-correct setpoint position [mm] (ASBR) | `L01S_ASBR_DB_HMI_connect.y_adjust.AutoCorrectSPPos` | mm | 0.80 | module_segment |
| Cycle time setpoint (T01) (ASBL) | `L01S_ASBL_DB_setpoint.Times.CycleTime` | ms | 0.85 | module_segment |
| X-adjust offset position [mm] (ASBL) | `L01S_ASBL_DB_setpoint.x_adjust.Offset_Pos` | mm | 0.85 | module_segment |
| X-adjust target position [mm] (ASBL) | `L01S_ASBL_DB_setpoint.x_adjust.Target_Pos` | mm | 0.85 | module_segment |
| X-adjust camera offset position [mm] (ASBL) | `L01S_ASBL_DB_setpoint.x_adjust_camera.Offset_Pos` | mm | 0.85 | module_segment |
| X-adjust camera target position [mm] (ASBL) | `L01S_ASBL_DB_setpoint.x_adjust_camera.Target_Pos` | mm | 0.85 | module_segment |
| Y-adjust offset position [mm] (ASBL) | `L01S_ASBL_DB_setpoint.y_adjust.Offset_Pos` | mm | 0.85 | module_segment |
| Y-adjust target position [mm] (ASBL) | `L01S_ASBL_DB_setpoint.y_adjust.Target_Pos` | mm | 0.85 | module_segment |
| Y-adjust camera offset position [mm] (ASBL) | `L01S_ASBL_DB_setpoint.y_adjust_camera.Offset_Pos` | mm | 0.85 | module_segment |
| Y-adjust camera target position [mm] (ASBL) | `L01S_ASBL_DB_setpoint.y_adjust_camera.Target_Pos` | mm | 0.85 | module_segment |
| Actual cycle time (T01) (ASBL) | `L01S_ASBL_DB_HMI_connect.HMIActualTimes.T01` | ms | 0.85 | module_segment |
| X-adjust actual position [mm] (ASBL) | `L01S_ASBL_DB_HMI_connect.x_adjust.ActPos` | mm | 0.85 | module_segment |
| X-adjust camera actual position [mm] (ASBL) | `L01S_ASBL_DB_HMI_connect.x_adjust_camera.ActPos` | mm | 0.85 | module_segment |
| Y-adjust actual position [mm] (ASBL) | `L01S_ASBL_DB_HMI_connect.y_adjust.ActPos` | mm | 0.85 | module_segment |
| Y-adjust camera actual position [mm] (ASBL) | `L01S_ASBL_DB_HMI_connect.y_adjust_camera.ActPos` | mm | 0.85 | module_segment |
| Cycle time setpoint (T01) (ASBR) | `L01S_ASBR_DB_setpoint.Times.CycleTime` | ms | 0.85 | module_segment |
| X-adjust offset position [mm] (ASBR) | `L01S_ASBR_DB_setpoint.x_adjust.Offset_Pos` | mm | 0.85 | module_segment |
| X-adjust target position [mm] (ASBR) | `L01S_ASBR_DB_setpoint.x_adjust.Target_Pos` | mm | 0.85 | module_segment |
| X-adjust camera offset position [mm] (ASBR) | `L01S_ASBR_DB_setpoint.x_adjust_camera.Offset_Pos` | mm | 0.85 | module_segment |
| X-adjust camera target position [mm] (ASBR) | `L01S_ASBR_DB_setpoint.x_adjust_camera.Target_Pos` | mm | 0.85 | module_segment |
| Y-adjust offset position [mm] (ASBR) | `L01S_ASBR_DB_setpoint.y_adjust.Offset_Pos` | mm | 0.85 | module_segment |
| Y-adjust target position [mm] (ASBR) | `L01S_ASBR_DB_setpoint.y_adjust.Target_Pos` | mm | 0.85 | module_segment |
| Y-adjust camera offset position [mm] (ASBR) | `L01S_ASBR_DB_setpoint.y_adjust_camera.Offset_Pos` | mm | 0.85 | module_segment |
| Y-adjust camera target position [mm] (ASBR) | `L01S_ASBR_DB_setpoint.y_adjust_camera.Target_Pos` | mm | 0.85 | module_segment |
| Actual cycle time (T01) (ASBR) | `L01S_ASBR_DB_HMI_connect.HMIActualTimes.T01` | ms | 0.85 | module_segment |
| X-adjust actual position [mm] (ASBR) | `L01S_ASBR_DB_HMI_connect.x_adjust.ActPos` | mm | 0.85 | module_segment |
| X-adjust camera actual position [mm] (ASBR) | `L01S_ASBR_DB_HMI_connect.x_adjust_camera.ActPos` | mm | 0.85 | module_segment |
| Y-adjust actual position [mm] (ASBR) | `L01S_ASBR_DB_HMI_connect.y_adjust.ActPos` | mm | 0.85 | module_segment |
| Y-adjust camera actual position [mm] (ASBR) | `L01S_ASBR_DB_HMI_connect.y_adjust_camera.ActPos` | mm | 0.85 | module_segment |

### PPS periphery punching station (MC006-PPS)

- 74 candidate tag(s) considered -> 17 kept as genuine parameters (23%).
- Kept tags found by: 17 via *module_segment* (the tag name contains this station's own PLC/module code as a literal segment - the strongest signal available).
- 1 kept parameter(s) below 0.5 confidence - flagged with ⚠ below.

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| Part Status ⚠ | `L01S_PPS_DB_HMI_connect.Status.PartStatus` | - | 0.35 | module_segment |
| FP01: Station Enabled | `L01S_PPS_DB_setpoint.Selections.StationEnabled` | - | 0.50 | module_segment |
| FP01: Operation Mode - Semi-Automatic | `L01S_PPS_DB_HMI_connect.Selections.SemiAuto` | - | 0.50 | module_segment |
| T02: Punching Time | `L01S_PPS_DB_setpoint.Times._02` | ms | 0.65 | module_segment |
| T01: Cycle Time (Setpoint) | `L01S_PPS_DB_setpoint.Times.CycleTime` | ms | 0.65 | module_segment |
| T01: Cycle Time (Actual) | `L01S_PPS_DB_HMI_connect.HMIActualTimes.T01` | ms | 0.65 | module_segment |
| Gap 02: FPPS to ASB/ASC Inspection (Web1234) | `GE1_DB_setpoint.StationGaps.PPS_St_ASB_Insp` | mm | 0.75 | module_segment |
| Cycle Counter | `L01S_PPS_DB_HMI_connect.Count.CycleCounter` | cycles | 0.75 | module_segment |
| X-Axis Offset Position [mm] | `L01S_PPS_DB_setpoint.Adujst_X.Offset_Pos` | mm | 0.90 | module_segment |
| X-Axis Target Position [mm] | `L01S_PPS_DB_setpoint.Adujst_X.Target_Pos` | mm | 0.90 | module_segment |
| Y-Axis Offset Position [mm] | `L01S_PPS_DB_setpoint.Adujst_Y.Offset_Pos` | mm | 0.90 | module_segment |
| Y-Axis Target Position [mm] | `L01S_PPS_DB_setpoint.Adujst_Y.Target_Pos` | mm | 0.90 | module_segment |
| Z-Axis Offset Position [mm] | `L01S_PPS_DB_setpoint.Adujst_Z.Offset_Pos` | mm | 0.90 | module_segment |
| Z-Axis Target Position [mm] | `L01S_PPS_DB_setpoint.Adujst_Z.Target_Pos` | mm | 0.90 | module_segment |
| X-Axis Actual Position [mm] | `L01S_PPS_DB_HMI_connect.Adujst_X.ActPos` | mm | 0.90 | module_segment |
| Y-Axis Actual Position [mm] | `L01S_PPS_DB_HMI_connect.Adujst_Y.ActPos` | mm | 0.90 | module_segment |
| Z-Axis Actual Position [mm] | `L01S_PPS_DB_HMI_connect.Adujst_Z.ActPos` | mm | 0.90 | module_segment |

### ULS unloading station (MC006-ULS)

- 170 candidate tag(s) considered -> 30 kept as genuine parameters (18%).
- Kept tags found by: 30 via *module_segment* (the tag name contains this station's own PLC/module code as a literal segment - the strongest signal available).

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| FP02: Preselection - Suction Basket Down on Belt | `L01S_ULS_DB_setpoint.Selections.BasketDownOnBelt` | - | 0.50 | module_segment |
| FP01: Operation Mode - Semiautomatic | `L01S_ULS_DB_HMI_connect.Selections.SemiAuto` | - | 0.50 | module_segment |
| FP01: Station Enabled | `L01S_ULS_DB_setpoint.Selections.StationEnabled` | - | 0.60 | module_segment |
| Stack Counter, Belt Conveyor (Actual) | `L01S_ULS_DB_HMI_connect.BeltConveyor.StackCounter` | - | 0.70 | module_segment |
| Stack Counter, Belt Conveyor (Setpoint) | `L01S_ULS_DB_setpoint.BeltConveyor.StackCounter` | - | 0.75 | module_segment |
| T02: Belt Running Time in Stack | `L01S_ULS_DB_setpoint.Times._02` | ms | 0.80 | module_segment |
| T03: Belt Running Time Between | `L01S_ULS_DB_setpoint.Times._03` | ms | 0.80 | module_segment |
| T04: Pick and Place - Suction Time | `L01S_ULS_DB_setpoint.Times._04` | ms | 0.80 | module_segment |
| T05: Pick and Place - Blow-off Time | `L01S_ULS_DB_setpoint.Times._05` | ms | 0.80 | module_segment |
| Cycle Counter | `L01S_ULS_DB_HMI_connect.Count.CycleCounter` | - | 0.80 | module_segment |
| T01: Cycle Time (Actual) | `L01S_ULS_DB_HMI_connect.HMIActualTimes.T01` | ms | 0.80 | module_segment |
| Gap 01: ULS to PPS (Web1234) | `GE1_DB_setpoint.StationGaps.ULS_St_PPS_St` | mm | 0.85 | module_segment |
| Extractor Position 1 - Acceleration [%] | `L01S_ULS_DB_setpoint.Extractor._Pos1.Acc` | % | 0.85 | module_segment |
| Extractor Position 1 - Deceleration [%] | `L01S_ULS_DB_setpoint.Extractor._Pos1.Dec` | % | 0.85 | module_segment |
| Extractor - Override Velocity [%] | `L01S_ULS_DB_setpoint.Extractor.OVR_Velocity` | % | 0.85 | module_segment |
| T01: Cycle Time (Setpoint) | `L01S_ULS_DB_setpoint.Times.CycleTime` | ms | 0.85 | module_segment |
| Extractor - Target Position [mm] | `L01S_ULS_DB_HMI_connect.Extractor.TargetPos` | mm | 0.85 | module_segment |
| Adjust X - Offset Position [mm] | `L01S_ULS_DB_setpoint.Adjust_X.Offset_Pos` | mm | 0.90 | module_segment |
| Adjust X - Target Position [mm] | `L01S_ULS_DB_setpoint.Adjust_X.Target_Pos` | mm | 0.90 | module_segment |
| Adjust X Expeller - Offset Position [mm] | `L01S_ULS_DB_setpoint.Adjust_X_Expeller.Offset_Pos` | mm | 0.90 | module_segment |
| Adjust X Expeller - Target Position [mm] | `L01S_ULS_DB_setpoint.Adjust_X_Expeller.Target_Pos` | mm | 0.90 | module_segment |
| Adjust Y - Offset Position [mm] | `L01S_ULS_DB_setpoint.Adjust_Y.Offset_Pos` | mm | 0.90 | module_segment |
| Adjust Y - Target Position [mm] | `L01S_ULS_DB_setpoint.Adjust_Y.Target_Pos` | mm | 0.90 | module_segment |
| Extractor Position 1 - Target Position [mm] | `L01S_ULS_DB_setpoint.Extractor._Pos1.Position` | mm | 0.90 | module_segment |
| Extractor Position 2 - Target Position [mm] | `L01S_ULS_DB_setpoint.Extractor._Pos2.Position` | mm | 0.90 | module_segment |
| Extractor Position 3 - Target Position [mm] | `L01S_ULS_DB_setpoint.Extractor._Pos3.Position` | mm | 0.90 | module_segment |
| Adjust X - Actual Position [mm] | `L01S_ULS_DB_HMI_connect.Adjust_X.ActPos` | mm | 0.90 | module_segment |
| Adjust X Expeller - Actual Position [mm] | `L01S_ULS_DB_HMI_connect.Adjust_X_Expeller.ActPos` | mm | 0.90 | module_segment |
| Adjust Y - Actual Position [mm] | `L01S_ULS_DB_HMI_connect.Adjust_Y.ActPos` | mm | 0.90 | module_segment |
| Extractor - Actual Position [mm] | `L01S_ULS_DB_HMI_connect.Extractor.ActPos` | mm | 0.90 | module_segment |

### FFT feeding station, flange (MC006-FFT)

- 200 candidate tag(s) considered -> 45 kept as genuine parameters (22%).
- Kept tags found by: 45 via *module_segment* (the tag name contains this station's own PLC/module code as a literal segment - the strongest signal available).

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| Robot SORT Left - Vision Process Code | `L02_FFT_DB_setpoint.RobSORT_L.vison_process_code` | - | 0.55 | module_segment |
| Robot SORT Left - Vision Process Number | `L02_FFT_DB_setpoint.RobSORT_L.vison_process_number` | - | 0.55 | module_segment |
| Robot SORT Right - Vision Process Code | `L02_FFT_DB_setpoint.RobSORT_R.vison_process_code` | - | 0.55 | module_segment |
| Robot SORT Right - Vision Process Number | `L02_FFT_DB_setpoint.RobSORT_R.vison_process_number` | - | 0.55 | module_segment |
| Station Enabled (FP01) | `L02_FFT_DB_setpoint.Selections.StationEnabled` | - | 0.60 | module_segment |
| Operation Mode: Semi-Automatic (FP01) | `L02_FFT_DB_HMI_connect.Selections.SemiAuto` | - | 0.60 | module_segment |
| Robot FEED - Pick X Offset Negative (Sign) | `L02_FFT_DB_setpoint.RobFEED.PICK.X_negativ` | - | 0.75 | module_segment |
| Robot FEED - Pick Z Offset Negative (Sign) | `L02_FFT_DB_setpoint.RobFEED.PICK.Z_negativ` | - | 0.75 | module_segment |
| Robot FEED - Place X Offset Negative (Sign) | `L02_FFT_DB_setpoint.RobFEED.PLACE.X_negativ` | - | 0.75 | module_segment |
| Robot FEED - Place Y Offset Negative (Sign) | `L02_FFT_DB_setpoint.RobFEED.PLACE.Y_negativ` | - | 0.75 | module_segment |
| Robot FEED - Place Z Offset Negative (Sign) | `L02_FFT_DB_setpoint.RobFEED.PLACE.Z_negativ` | - | 0.75 | module_segment |
| Robot SORT Left - Pick Z Offset Negative (Sign) | `L02_FFT_DB_setpoint.RobSORT_L.PICK.Z_negativ` | - | 0.75 | module_segment |
| Robot SORT Left - Place Angle Negative (Sign) | `L02_FFT_DB_setpoint.RobSORT_L.PLACE.Angle_negativ` | - | 0.75 | module_segment |
| Robot SORT Left - Place X Offset Negative (Sign) | `L02_FFT_DB_setpoint.RobSORT_L.PLACE.X_negativ` | - | 0.75 | module_segment |
| Robot SORT Left - Place Y Offset Negative (Sign) | `L02_FFT_DB_setpoint.RobSORT_L.PLACE.Y_negativ` | - | 0.75 | module_segment |
| Robot SORT Left - Place Z Offset Negative (Sign) | `L02_FFT_DB_setpoint.RobSORT_L.PLACE.Z_negativ` | - | 0.75 | module_segment |
| Robot SORT Right - Pick Z Offset Negative (Sign) | `L02_FFT_DB_setpoint.RobSORT_R.PICK.Z_negativ` | - | 0.75 | module_segment |
| Robot SORT Right - Place Angle Negative (Sign) | `L02_FFT_DB_setpoint.RobSORT_R.PLACE.Angle_negativ` | - | 0.75 | module_segment |
| Robot SORT Right - Place X Offset Negative (Sign) | `L02_FFT_DB_setpoint.RobSORT_R.PLACE.X_negativ` | - | 0.75 | module_segment |
| Robot SORT Right - Place Y Offset Negative (Sign) | `L02_FFT_DB_setpoint.RobSORT_R.PLACE.Y_negativ` | - | 0.75 | module_segment |
| Robot SORT Right - Place Z Offset Negative (Sign) | `L02_FFT_DB_setpoint.RobSORT_R.PLACE.Z_negativ` | - | 0.75 | module_segment |
| Actual Cycle Time - Robot FEED (T21, Line) | `L02_FFT_DB_HMI_connect.HMIActualTimes.T21` | ms | 0.80 | module_segment |
| Actual Cycle Time - Robot SORT Left (T22) | `L02_FFT_DB_HMI_connect.HMIActualTimes.T22` | ms | 0.80 | module_segment |
| Actual Cycle Time - Robot SORT Right (T23) | `L02_FFT_DB_HMI_connect.HMIActualTimes.T23` | ms | 0.80 | module_segment |
| Robot FEED - Pick X Offset | `L02_FFT_DB_setpoint.RobFEED.PICK.X_offset` | mm | 0.85 | module_segment |
| Robot FEED - Pick Z Offset | `L02_FFT_DB_setpoint.RobFEED.PICK.Z_offset` | mm | 0.85 | module_segment |
| Robot FEED - Place X Offset | `L02_FFT_DB_setpoint.RobFEED.PLACE.X_offset` | mm | 0.85 | module_segment |
| Robot FEED - Place Y Offset | `L02_FFT_DB_setpoint.RobFEED.PLACE.Y_offset` | mm | 0.85 | module_segment |
| Robot FEED - Place Z Offset | `L02_FFT_DB_setpoint.RobFEED.PLACE.Z_offset` | mm | 0.85 | module_segment |
| Robot FEED - Velocity Factor (0-100%) | `L02_FFT_DB_setpoint.RobFEED.velocity` | % | 0.85 | module_segment |
| Robot SORT Left - Pick Z Offset | `L02_FFT_DB_setpoint.RobSORT_L.PICK.Z_offset` | mm | 0.85 | module_segment |
| Robot SORT Left - Place Angle | `L02_FFT_DB_setpoint.RobSORT_L.PLACE.Angle` | ° | 0.85 | module_segment |
| Robot SORT Left - Place X Offset | `L02_FFT_DB_setpoint.RobSORT_L.PLACE.X_offset` | mm | 0.85 | module_segment |
| Robot SORT Left - Place Y Offset | `L02_FFT_DB_setpoint.RobSORT_L.PLACE.Y_offset` | mm | 0.85 | module_segment |
| Robot SORT Left - Place Z Offset | `L02_FFT_DB_setpoint.RobSORT_L.PLACE.Z_offset` | mm | 0.85 | module_segment |
| Robot SORT Left - Velocity Factor (0-100%) | `L02_FFT_DB_setpoint.RobSORT_L.velocity` | % | 0.85 | module_segment |
| Robot SORT Right - Pick Z Offset | `L02_FFT_DB_setpoint.RobSORT_R.PICK.Z_offset` | mm | 0.85 | module_segment |
| Robot SORT Right - Place Angle | `L02_FFT_DB_setpoint.RobSORT_R.PLACE.Angle` | ° | 0.85 | module_segment |
| Robot SORT Right - Place X Offset | `L02_FFT_DB_setpoint.RobSORT_R.PLACE.X_offset` | mm | 0.85 | module_segment |
| Robot SORT Right - Place Y Offset | `L02_FFT_DB_setpoint.RobSORT_R.PLACE.Y_offset` | mm | 0.85 | module_segment |
| Robot SORT Right - Place Z Offset | `L02_FFT_DB_setpoint.RobSORT_R.PLACE.Z_offset` | mm | 0.85 | module_segment |
| Robot SORT Right - Velocity Factor (0-100%) | `L02_FFT_DB_setpoint.RobSORT_R.velocity` | % | 0.85 | module_segment |
| Cycle Time Setpoint (T01) | `L02_FFT_DB_setpoint.Times.CycleTime` | ms | 0.85 | module_segment |
| Cycle Counter | `L02_FFT_DB_HMI_connect.Count.CycleCounter` | count | 0.85 | module_segment |
| Actual Cycle Time (T01) | `L02_FFT_DB_HMI_connect.HMIActualTimes.T01` | ms | 0.85 | module_segment |

### FFG feeding station, gasket (MC006-FFG)

- 124 candidate tag(s) considered -> 47 kept as genuine parameters (38%).
- Kept tags found by: 47 via *module_segment* (the tag name contains this station's own PLC/module code as a literal segment - the strongest signal available).

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| Air duct enabled (FP02) | `L02S_FFG_DB_setpoint.Selections.FP02` | - | 0.50 | module_segment |
| Operation mode: semiautomatic (FP01) | `L02S_FFG_DB_HMI_connect.Selections.SemiAuto` | - | 0.50 | module_segment |
| Actual time T04 | `L02S_FFG_DB_HMI_connect.HMIActualTimes.T04` | ms | 0.55 | module_segment |
| Actual time T05 | `L02S_FFG_DB_HMI_connect.HMIActualTimes.T05` | ms | 0.55 | module_segment |
| Actual time T06 | `L02S_FFG_DB_HMI_connect.HMIActualTimes.T06` | ms | 0.55 | module_segment |
| Station enabled (FP01) | `L02S_FFG_DB_setpoint.Selections.StationEnabled` | - | 0.60 | module_segment |
| Pusher left target position (HMI readback) | `L02S_FFG_DB_HMI_connect.PusherLeft.TargetPos` | mm | 0.75 | module_segment |
| Pusher right target position (HMI readback) | `L02S_FFG_DB_HMI_connect.PusherRight.TargetPos` | mm | 0.75 | module_segment |
| Delay stopper left up setpoint (T07) | `L02S_FFG_DB_setpoint.Times.DelayStopperLeftup` | ms | 0.80 | module_segment |
| Delay stopper right up setpoint (T08) | `L02S_FFG_DB_setpoint.Times.DelayStopperRightup` | ms | 0.80 | module_segment |
| Separating unit suction time LHS setpoint (T10) | `L02S_FFG_DB_setpoint.Times.SeparatingSuctionTimeLHS` | ms | 0.80 | module_segment |
| Separating unit suction time RHS setpoint (T09) | `L02S_FFG_DB_setpoint.Times.SeparatingSuctionTimeRHS` | ms | 0.80 | module_segment |
| Cycle time actual (T01) | `L02S_FFG_DB_HMI_connect.HMIActualTimes.T01` | ms | 0.80 | module_segment |
| Pusher left actual position | `L02S_FFG_DB_HMI_connect.PusherLeft.ActPos` | mm | 0.80 | module_segment |
| Pusher right actual position | `L02S_FFG_DB_HMI_connect.PusherRight.ActPos` | mm | 0.80 | module_segment |
| Chain override velocity | `L02S_FFG_DB_setpoint.Chain.OVR_Velocity` | % | 0.85 | module_segment |
| Cycle time setpoint (T01) | `L02S_FFG_DB_setpoint.Times.CycleTime` | ms | 0.85 | module_segment |
| Chain target position (HMI readback) | `L02S_FFG_DB_HMI_connect.Chain.TargetPos` | mm | 0.85 | module_segment |
| Cycle counter | `L02S_FFG_DB_HMI_connect.Count.CycleCounter` | - | 0.85 | module_segment |
| Chain position setpoint acceleration | `L02S_FFG_DB_setpoint.Chain._Pos.Acc` | % | 0.90 | module_segment |
| Chain position setpoint deceleration | `L02S_FFG_DB_setpoint.Chain._Pos.Dec` | % | 0.90 | module_segment |
| Chain position setpoint | `L02S_FFG_DB_setpoint.Chain._Pos.Position` | mm | 0.90 | module_segment |
| Pusher left (empty position) acceleration | `L02S_FFG_DB_setpoint.PusherLeft._Empty.Acc` | % | 0.90 | module_segment |
| Pusher left (empty position) deceleration | `L02S_FFG_DB_setpoint.PusherLeft._Empty.Dec` | % | 0.90 | module_segment |
| Pusher left (empty position) target position | `L02S_FFG_DB_setpoint.PusherLeft._Empty.Position` | mm | 0.90 | module_segment |
| Pusher left (empty position) velocity | `L02S_FFG_DB_setpoint.PusherLeft._Empty.Velocity` | % | 0.90 | module_segment |
| Pusher left (full position) acceleration | `L02S_FFG_DB_setpoint.PusherLeft._Full.Acc` | % | 0.90 | module_segment |
| Pusher left (full position) deceleration | `L02S_FFG_DB_setpoint.PusherLeft._Full.Dec` | % | 0.90 | module_segment |
| Pusher left (full position) target position | `L02S_FFG_DB_setpoint.PusherLeft._Full.Position` | mm | 0.90 | module_segment |
| Pusher left (full position) velocity | `L02S_FFG_DB_setpoint.PusherLeft._Full.Velocity` | % | 0.90 | module_segment |
| Pusher left (pick position) acceleration | `L02S_FFG_DB_setpoint.PusherLeft._Pick.Acc` | % | 0.90 | module_segment |
| Pusher left (pick position) deceleration | `L02S_FFG_DB_setpoint.PusherLeft._Pick.Dec` | % | 0.90 | module_segment |
| Pusher left (pick position) target position | `L02S_FFG_DB_setpoint.PusherLeft._Pick.Position` | mm | 0.90 | module_segment |
| Pusher left (pick position) velocity | `L02S_FFG_DB_setpoint.PusherLeft._Pick.Velocity` | % | 0.90 | module_segment |
| Pusher right (empty position) acceleration | `L02S_FFG_DB_setpoint.PusherRight._Empty.Acc` | % | 0.90 | module_segment |
| Pusher right (empty position) deceleration | `L02S_FFG_DB_setpoint.PusherRight._Empty.Dec` | % | 0.90 | module_segment |
| Pusher right (empty position) target position | `L02S_FFG_DB_setpoint.PusherRight._Empty.Position` | mm | 0.90 | module_segment |
| Pusher right (empty position) velocity | `L02S_FFG_DB_setpoint.PusherRight._Empty.Velocity` | % | 0.90 | module_segment |
| Pusher right (full position) acceleration | `L02S_FFG_DB_setpoint.PusherRight._Full.Acc` | % | 0.90 | module_segment |
| Pusher right (full position) deceleration | `L02S_FFG_DB_setpoint.PusherRight._Full.Dec` | % | 0.90 | module_segment |
| Pusher right (full position) target position | `L02S_FFG_DB_setpoint.PusherRight._Full.Position` | mm | 0.90 | module_segment |
| Pusher right (full position) velocity | `L02S_FFG_DB_setpoint.PusherRight._Full.Velocity` | % | 0.90 | module_segment |
| Pusher right (pick position) acceleration | `L02S_FFG_DB_setpoint.PusherRight._Pick.Acc` | % | 0.90 | module_segment |
| Pusher right (pick position) deceleration | `L02S_FFG_DB_setpoint.PusherRight._Pick.Dec` | % | 0.90 | module_segment |
| Pusher right (pick position) target position | `L02S_FFG_DB_setpoint.PusherRight._Pick.Position` | mm | 0.90 | module_segment |
| Pusher right (pick position) velocity | `L02S_FFG_DB_setpoint.PusherRight._Pick.Velocity` | % | 0.90 | module_segment |
| Chain actual position | `L02S_FFG_DB_HMI_connect.Chain.ActPos` | mm | 0.90 | module_segment |

### FFB feeding station, barrier (MC006-FFB)

- 105 candidate tag(s) considered -> 14 kept as genuine parameters (13%).
- Kept tags found by: 14 via *module_segment* (the tag name contains this station's own PLC/module code as a literal segment - the strongest signal available).

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| Vision process file code (e.g. VPH1) | `L02S_FFB_DB_setpoint.RobBARRIER.vison_process_code` | - | 0.50 | module_segment |
| Vision process file number (e.g. VPH1) | `L02S_FFB_DB_setpoint.RobBARRIER.vison_process_number` | - | 0.50 | module_segment |
| Station enabled (FP01) | `L02S_FFB_DB_setpoint.Selections.StationEnabled` | - | 0.50 | module_segment |
| Operation mode: semiautomatic (FP01) | `L02S_FFB_DB_HMI_connect.Selections.SemiAuto` | - | 0.50 | module_segment |
| Negative X offset (direction flag) | `L02S_FFB_DB_setpoint.RobBARRIER.X_negativ` | - | 0.55 | module_segment |
| Negative Y offset (direction flag) | `L02S_FFB_DB_setpoint.RobBARRIER.Y_negativ` | - | 0.55 | module_segment |
| Negative Z offset (direction flag) | `L02S_FFB_DB_setpoint.RobBARRIER.Z_negativ` | - | 0.55 | module_segment |
| X offset | `L02S_FFB_DB_setpoint.RobBARRIER.X_offset` | mm | 0.75 | module_segment |
| Z offset | `L02S_FFB_DB_setpoint.RobBARRIER.Z_offset` | mm | 0.75 | module_segment |
| Y offset (pick/place gap distance to barrier stacks) | `L02S_FFB_DB_setpoint.RobBARRIER.Y_offset` | mm | 0.80 | module_segment |
| Cycle time setpoint (T01) | `L02S_FFB_DB_setpoint.Times.CycleTime` | ms | 0.80 | module_segment |
| Cycle time (actual) | `L02S_FFB_DB_HMI_connect.HMIActualTimes.T01` | ms | 0.80 | module_segment |
| Velocity factor (0-100%) | `L02S_FFB_DB_setpoint.RobBARRIER.velocity` | % | 0.85 | module_segment |
| Cycle counter | `L02S_FFB_DB_HMI_connect.Count.CycleCounter` | count | 0.85 | module_segment |

### INS chain conveyor (MC006-INS)

- 226 candidate tag(s) considered -> 81 kept as genuine parameters (36%).
- Kept tags found by: 81 via *module_segment* (the tag name contains this station's own PLC/module code as a literal segment - the strongest signal available).
- 1 kept parameter(s) below 0.5 confidence - flagged with ⚠ below.

| Parameter | Historian Tag | Unit | Confidence | Found via |
|---|---|---|---|---|
| FP03: disable fault cycle time too high ⚠ | `L01_INS_DB_HMI_connect.Selections.FP03` | - | 0.45 | module_segment |
| FP02: enable chain adjustment | `L01_INS_DB_HMI_connect.Selections.FP02` | - | 0.55 | module_segment |
| FP01: operation mode semiautomatic | `L01_INS_DB_HMI_connect.Selections.SemiAuto` | - | 0.55 | module_segment |
| Film stretching MAX limit between station 1 and 2 (Lower) | `L01_INS_DB_setpointMAX.Film_Stretching_Lower.Stretching_1_2` | % | 0.70 | module_segment |
| Film stretching MAX limit between station 2 and 3 (Lower) | `L01_INS_DB_setpointMAX.Film_Stretching_Lower.Stretching_2_3` | % | 0.70 | module_segment |
| Film stretching MAX limit between station 3 and 4 (Lower) | `L01_INS_DB_setpointMAX.Film_Stretching_Lower.Stretching_3_4` | % | 0.70 | module_segment |
| Film stretching MAX limit between station 4 and 5 (Lower) | `L01_INS_DB_setpointMAX.Film_Stretching_Lower.Stretching_4_5` | % | 0.70 | module_segment |
| Film stretching MAX limit between station 1 and 2 (Upper) | `L01_INS_DB_setpointMAX.Film_Stretching_Upper.Stretching_1_2` | % | 0.70 | module_segment |
| Film stretching MAX limit between station 2 and 3 (Upper) | `L01_INS_DB_setpointMAX.Film_Stretching_Upper.Stretching_2_3` | % | 0.70 | module_segment |
| Film stretching MAX limit between station 3 and 4 (Upper) | `L01_INS_DB_setpointMAX.Film_Stretching_Upper.Stretching_3_4` | % | 0.70 | module_segment |
| Film stretching MAX limit between station 4 and 5 (Upper) | `L01_INS_DB_setpointMAX.Film_Stretching_Upper.Stretching_4_5` | % | 0.70 | module_segment |
| Film stretching MIN limit between station 1 and 2 (Lower) | `L01_INS_DB_setpointMIN.Film_Stretching_Lower.Stretching_1_2` | % | 0.70 | module_segment |
| Film stretching MIN limit between station 2 and 3 (Lower) | `L01_INS_DB_setpointMIN.Film_Stretching_Lower.Stretching_2_3` | % | 0.70 | module_segment |
| Film stretching MIN limit between station 3 and 4 (Lower) | `L01_INS_DB_setpointMIN.Film_Stretching_Lower.Stretching_3_4` | % | 0.70 | module_segment |
| Film stretching MIN limit between station 4 and 5 (Lower) | `L01_INS_DB_setpointMIN.Film_Stretching_Lower.Stretching_4_5` | % | 0.70 | module_segment |
| Film stretching MIN limit between station 1 and 2 (Upper) | `L01_INS_DB_setpointMIN.Film_Stretching_Upper.Stretching_1_2` | % | 0.70 | module_segment |
| Film stretching MIN limit between station 2 and 3 (Upper) | `L01_INS_DB_setpointMIN.Film_Stretching_Upper.Stretching_2_3` | % | 0.70 | module_segment |
| Film stretching MIN limit between station 3 and 4 (Upper) | `L01_INS_DB_setpointMIN.Film_Stretching_Upper.Stretching_3_4` | % | 0.70 | module_segment |
| Film stretching MIN limit between station 4 and 5 (Upper) | `L01_INS_DB_setpointMIN.Film_Stretching_Upper.Stretching_4_5` | % | 0.70 | module_segment |
| Welding belt FPW gearing factor LHS [%] | `L01_INS_DB_setpoint.WeldingBeltFPW.GearingFactorLHS` | % | 0.70 | module_segment |
| Welding belt FPW gearing factor RHS [%] | `L01_INS_DB_setpoint.WeldingBeltFPW.GearingFactorRHS` | % | 0.70 | module_segment |
| Film stretching between station 1 and 2 (Lower) | `L01_INS_DB_setpoint.Film_Stretching_Lower.Stretching_1_2` | % | 0.75 | module_segment |
| Film stretching between station 2 and 3 (Lower) | `L01_INS_DB_setpoint.Film_Stretching_Lower.Stretching_2_3` | % | 0.75 | module_segment |
| Film stretching between station 3 and 4 (Lower) | `L01_INS_DB_setpoint.Film_Stretching_Lower.Stretching_3_4` | % | 0.75 | module_segment |
| Film stretching between station 4 and 5 (Lower) | `L01_INS_DB_setpoint.Film_Stretching_Lower.Stretching_4_5` | % | 0.75 | module_segment |
| Film stretching between station 1 and 2 (Upper) | `L01_INS_DB_setpoint.Film_Stretching_Upper.Stretching_1_2` | % | 0.75 | module_segment |
| Film stretching between station 2 and 3 (Upper) | `L01_INS_DB_setpoint.Film_Stretching_Upper.Stretching_2_3` | % | 0.75 | module_segment |
| Film stretching between station 3 and 4 (Upper) | `L01_INS_DB_setpoint.Film_Stretching_Upper.Stretching_3_4` | % | 0.75 | module_segment |
| Film stretching between station 4 and 5 (Upper) | `L01_INS_DB_setpoint.Film_Stretching_Upper.Stretching_4_5` | % | 0.75 | module_segment |
| Target position MAX limit [mm] - Adjust Lower Chain 1 | `L01_INS_DB_setpointMAX.Adjust_LowerChain_1.Target_Pos` | mm | 0.80 | module_segment |
| Target position MAX limit [mm] - Adjust Upper Chain 1 | `L01_INS_DB_setpointMAX.Adjust_UpperChain_1.Target_Pos` | mm | 0.80 | module_segment |
| Target position MIN limit [mm] - Adjust Lower Chain 1 | `L01_INS_DB_setpointMIN.Adjust_LowerChain_1.Target_Pos` | mm | 0.80 | module_segment |
| Target position MIN limit [mm] - Adjust Upper Chain 1 | `L01_INS_DB_setpointMIN.Adjust_UpperChain_1.Target_Pos` | mm | 0.80 | module_segment |
| Chain position 1 acceleration [%] | `L01_INS_DB_setpoint.Chain._Pos1.Acc` | % | 0.85 | module_segment |
| Chain position 1 deceleration [%] | `L01_INS_DB_setpoint.Chain._Pos1.Dec` | % | 0.85 | module_segment |
| Chain position 1 jerk [%] | `L01_INS_DB_setpoint.Chain._Pos1.Jerk` | % | 0.85 | module_segment |
| Chain position 1 target position [mm] | `L01_INS_DB_setpoint.Chain._Pos1.Position` | mm | 0.85 | module_segment |
| Chain position 1 velocity [%] | `L01_INS_DB_setpoint.Chain._Pos1.Velocity` | % | 0.85 | module_segment |
| Chain gearing factor to lower chain [%] | `L01_INS_DB_setpoint.Chain.GearingFactorSync` | % | 0.85 | module_segment |
| Chain actual position [mm] | `L01_INS_DB_HMI_connect.Chain.ActPos` | mm | 0.85 | module_segment |
| Chain target position [mm] | `L01_INS_DB_HMI_connect.Chain.TargetPos` | mm | 0.85 | module_segment |
| Lower chain actual position [mm] | `L01_INS_DB_HMI_connect.ChainLower.ActPos` | mm | 0.85 | module_segment |
| Upper chain actual position [mm] | `L01_INS_DB_HMI_connect.ChainUpper.ActPos` | mm | 0.85 | module_segment |
| Cycle time setpoint (T01) | `L01_INS_DB_setpoint.Times.CycleTime` | ms | 0.85 | module_segment |
| Cycle time actual (T01) | `L01_INS_DB_HMI_connect.HMIActualTimes.T01` | ms | 0.85 | module_segment |
| Upper clamp feed backward acceleration [%] | `L01_INS_DB_setpoint.UpperClampFeed.Backward.Acc` | % | 0.85 | module_segment |
| Upper clamp feed backward deceleration [%] | `L01_INS_DB_setpoint.UpperClampFeed.Backward.Dec` | % | 0.85 | module_segment |
| Upper clamp feed backward target position [mm] | `L01_INS_DB_setpoint.UpperClampFeed.Backward.Position` | mm | 0.85 | module_segment |
| Upper clamp feed backward velocity [%] | `L01_INS_DB_setpoint.UpperClampFeed.Backward.Velocity` | % | 0.85 | module_segment |
| Upper clamp feed forward target position [mm] | `L01_INS_DB_setpoint.UpperClampFeed.Forward.Position` | mm | 0.85 | module_segment |
| Upper clamp feed gearing factor to upper chain [%] | `L01_INS_DB_setpoint.UpperClampFeed.GearingFactorSync` | % | 0.85 | module_segment |
| Upper clamp feed actual position [mm] | `L01_INS_DB_HMI_connect.UpperClampFeed.ActPos` | mm | 0.85 | module_segment |
| Upper clamp feed target position [mm] | `L01_INS_DB_HMI_connect.UpperClampFeed.TargetPos` | mm | 0.85 | module_segment |
| Cycle counter | `L01_INS_DB_HMI_connect.Count.CycleCounter` | count | 0.85 | module_segment |
| Offset position [mm] - Adjust Lower Chain 1 | `L01_INS_DB_setpoint.Adjust_LowerChain_1.Offset_Pos` | mm | 0.90 | module_segment |
| Target position [mm] - Adjust Lower Chain 1 | `L01_INS_DB_setpoint.Adjust_LowerChain_1.Target_Pos` | mm | 0.90 | module_segment |
| Actual position [mm] - Adjust Lower Chain 1 | `L01_INS_DB_HMI_connect.Adjust_LowerChain_1.ActPos` | mm | 0.90 | module_segment |
| Offset position [mm] - Adjust Lower Chain 2 | `L01_INS_DB_setpoint.Adjust_LowerChain_2.Offset_Pos` | mm | 0.90 | module_segment |
| Target position [mm] - Adjust Lower Chain 2 | `L01_INS_DB_setpoint.Adjust_LowerChain_2.Target_Pos` | mm | 0.90 | module_segment |
| Actual position [mm] - Adjust Lower Chain 2 | `L01_INS_DB_HMI_connect.Adjust_LowerChain_2.ActPos` | mm | 0.90 | module_segment |
| Offset position [mm] - Adjust Lower Chain 3 | `L01_INS_DB_setpoint.Adjust_LowerChain_3.Offset_Pos` | mm | 0.90 | module_segment |
| Target position [mm] - Adjust Lower Chain 3 | `L01_INS_DB_setpoint.Adjust_LowerChain_3.Target_Pos` | mm | 0.90 | module_segment |
| Actual position [mm] - Adjust Lower Chain 3 | `L01_INS_DB_HMI_connect.Adjust_LowerChain_3.ActPos` | mm | 0.90 | module_segment |
| Offset position [mm] - Adjust Lower Chain 4 | `L01_INS_DB_setpoint.Adjust_LowerChain_4.Offset_Pos` | mm | 0.90 | module_segment |
| Target position [mm] - Adjust Lower Chain 4 | `L01_INS_DB_setpoint.Adjust_LowerChain_4.Target_Pos` | mm | 0.90 | module_segment |
| Actual position [mm] - Adjust Lower Chain 4 | `L01_INS_DB_HMI_connect.Adjust_LowerChain_4.ActPos` | mm | 0.90 | module_segment |
| Offset position [mm] - Adjust Upper Chain 1 | `L01_INS_DB_setpoint.Adjust_UpperChain_1.Offset_Pos` | mm | 0.90 | module_segment |
| Target position [mm] - Adjust Upper Chain 1 | `L01_INS_DB_setpoint.Adjust_UpperChain_1.Target_Pos` | mm | 0.90 | module_segment |
| Actual position [mm] - Adjust Upper Chain 1 | `L01_INS_DB_HMI_connect.Adjust_UpperChain_1.ActPos` | mm | 0.90 | module_segment |
| Offset position [mm] - Adjust Upper Chain 2 | `L01_INS_DB_setpoint.Adjust_UpperChain_2.Offset_Pos` | mm | 0.90 | module_segment |
| Target position [mm] - Adjust Upper Chain 2 | `L01_INS_DB_setpoint.Adjust_UpperChain_2.Target_Pos` | mm | 0.90 | module_segment |
| Actual position [mm] - Adjust Upper Chain 2 | `L01_INS_DB_HMI_connect.Adjust_UpperChain_2.ActPos` | mm | 0.90 | module_segment |
| Offset position [mm] - Adjust Upper Chain 3 | `L01_INS_DB_setpoint.Adjust_UpperChain_3.Offset_Pos` | mm | 0.90 | module_segment |
| Target position [mm] - Adjust Upper Chain 3 | `L01_INS_DB_setpoint.Adjust_UpperChain_3.Target_Pos` | mm | 0.90 | module_segment |
| Actual position [mm] - Adjust Upper Chain 3 | `L01_INS_DB_HMI_connect.Adjust_UpperChain_3.ActPos` | mm | 0.90 | module_segment |
| Offset position [mm] - Adjust Upper Chain 4 | `L01_INS_DB_setpoint.Adjust_UpperChain_4.Offset_Pos` | mm | 0.90 | module_segment |
| Target position [mm] - Adjust Upper Chain 4 | `L01_INS_DB_setpoint.Adjust_UpperChain_4.Target_Pos` | mm | 0.90 | module_segment |
| Actual position [mm] - Adjust Upper Chain 4 | `L01_INS_DB_HMI_connect.Adjust_UpperChain_4.ActPos` | mm | 0.90 | module_segment |
| Offset position [mm] - Adjust Upper Chain 5 | `L01_INS_DB_setpoint.Adjust_UpperChain_5.Offset_Pos` | mm | 0.90 | module_segment |
| Target position [mm] - Adjust Upper Chain 5 | `L01_INS_DB_setpoint.Adjust_UpperChain_5.Target_Pos` | mm | 0.90 | module_segment |
| Actual position [mm] - Adjust Upper Chain 5 | `L01_INS_DB_HMI_connect.Adjust_UpperChain_5.ActPos` | mm | 0.90 | module_segment |
