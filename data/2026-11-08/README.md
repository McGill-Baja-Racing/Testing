# ENA — November 8, 2026

Shared measurements for MB26 testing. Each workbook is stored once here; testing requests link to the relevant files.

| Workbook | Contents |
| --- | --- |
| [RPM / GPS](RPM_GPS.xlsx?raw=true) | Engine RPM, gearbox-bearing RPM and DAQ GPS; one sheet per daytime session. |
| [Half-shafts](Half_shafts.xlsx?raw=true) | Native LHS/RHS samples; one sheet per session, including night. |
| [Front-left suspension](Front_left_suspension.xlsx?raw=true) | Native lower-arm bending and knuckle responses. |
| [Tie rod](Tie_rod.xlsx?raw=true) | Native parallel and night Ackermann readings; on-site offset/reliability note in [tie-rod review](Tie_rod.md). |
| [Body response](Body_response.xlsx?raw=true) | Separate AiM motion and native DAQ left-rear shock/GPS sheets. |
| [Maneuverability motion / GPS](Motion_GPS.xlsx?raw=true) | Retained post-night slalom windows; one sheet per window. |
| [Maneuverability activity index](Activity_index.xlsx?raw=true) | Matching source recordings and elapsed-time windows. |

[Powertrain load spectrum — #14](https://github.com/McGill-Baja-Racing/Testing/issues/14) · [Suspension/chassis response — #15](https://github.com/McGill-Baja-Racing/Testing/issues/15) · [Plots](plots/) · [Original files](source/README.md) · [Video](https://mcgill.sharepoint.com/:f:/r/sites/McGill_Baja_Group/Shared%20Documents/Drivers/MB26_Trainning/ENA%20Testing/Nov%208?d=w86e5a5a1d0dc4dd38bc664b2aefacb35&csf=1&web=1&e=pThiBI)

Times use Montreal time. AiM header-based time is nominal; precise synchronization across instruments is unverified. Angular rates are not roll/pitch angles; recorded axes are retained.

The front-left lower-arm gauge measured bending. Its and the front-left knuckle's calibration weights were entered directly in pounds; saved kg labels are stale. Their values retain the applied-pound calibration scale. The DAQ shock sensor was left rear.

Half-shaft units remain provisional: lb·ft versus lb·in to confirm. Night LHS file 2 requires review; final-file LHS reception is sparse. Grey plot shading marks missing channels; yellow marks estimated clock time; red marks the night LHS review interval.

[Request #17 — combined GPS circuit and motion figures](Maneuverability.md): all 13 retained post-night slalom windows. These windows do not overlap the daytime shock/front-left suspension recordings.
