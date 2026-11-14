# DR — Powertrain Load Spectrum Generation

MB26 · ENA · November 8, 2026 · [Testing request #14](https://github.com/McGill-Baja-Racing/Testing/issues/14)

- [RPM / GPS workbook](DR_RPM_GPS_by_session.xlsx?raw=true): one sheet per daytime session, approximately 20 Hz.
- [Half-shaft workbook](DR_halfshafts_by_session.xlsx?raw=true): one sheet per session, including night, with all native samples.
- [Original files and inventory](../source/README.md).

Both workbooks use Session, Original files, Absolute time (Montreal), Session time (s), then sensor columns. The half-shaft workbook retains 1,671,961 samples, including 568,116 night samples. Blank sensor cells mean no sample on that row.

Half-shaft units remain provisional: imperial wrench scale, lb·ft versus lb·in to confirm. Night LHS from night_ack_run_2.csv is unreliable; night_ack_run_3.csv has sparse LHS coverage. No night DAQ recording. Gearbox-bearing RPM ends around 14:54:40 Montreal time.

[Session plots](plots/) show the actual recorded coverage. The video link will be added after sharing through Teams.

Graph shading: **yellow** on RPM/GPS panels means clock time is estimated after the last recorded GPS time; sensor values remain recorded. **Red** on the night LHS plot marks file 2 for review because its near-flat section is unreliable. **Grey** marks the end of gearbox-bearing coverage.
