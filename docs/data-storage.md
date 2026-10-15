# Data storage and traceability

GitHub holds requests, small metadata, procedures, calibration descriptions, reports and analysis code. The existing team Google Drive holds large raw recordings/videos. No folders or permissions are created by these files; an authorized archive owner must confirm locations and access before the first real test.

## Test and run IDs

**Proposed collision-safe convention:** derive test IDs from the GitHub owner/repository and issue number: `McGill-Baja-Racing-Testing-123` for test issue #123. Issue numbers are unique within that repository; preparation issues use their parent's test ID. Reserve the `EXAMPLE` namespace for documentation only. Existing `TST-DEMO-001`–`004` IDs remain historical example IDs and are not reused for real work.

Run IDs append `-R001`, `-R002`, etc.; include rejected and aborted runs and never recycle an index. An independently authorized retest gets a new test issue/ID with a link to its predecessor. If a test issue must move between repositories, retain its original stable ID and record the old/new URLs; do not rename historic data. Requirement and device IDs are independent of issue numbers.

## Folders and filenames

Proposed layout under the team's existing archive:

```text
Testing Data/<season>/<test-id>_<short-name>/
  raw/
  video/
  processed/
  supporting/
```

Use `<run-id>_<stream>_<UTC-timestamp>_<configuration-revision>.<ext>`; the run ID already includes the test ID. UTC timestamps use `YYYYMMDDTHHMMSSZ`; run logs use ISO 8601 with an explicit offset. For example, `EXAMPLE-002-R001_pressure_20990101T140000Z_cfg-B.csv` is fictional naming, not a real recording.

The [run log](../templates/run-log.csv) records test/run IDs, start/end, configuration, conditions, observations/deviations, raw link, calibration reference, operator and data quality. Every video/stream has a run ID and synchronization reference. Original logger filenames may be retained: record their run mapping rather than rename/overwrite originals.

## Preserve and link evidence

- Never overwrite original raw files, including invalid/aborted attempts. Keep new processing versions in `processed/`, with analysis code commit/settings. Corrections go in separate metadata/derivations, not replacement raw files.
- At import retain a manifest of original names, sizes and checksums plus any import-name mapping. `supporting/` holds the plan/configuration, equipment/calibration versions, units/scaling, sampling/timebase, operators, conditions, deviations, logs and reports.
- Link stable folder/file references from the parent issue and run log; link relevant evidence/applicability from DVP&R. Check intended reader access before leaving where practicable and at closure. Record archive custodian and backup arrangement.
- Do not invent Drive URLs. Blank templates collect the real link; fictional examples use the local [archive example](../examples/data/README.md). Avoid moving linked folders; if necessary preserve cross-references and update the evidence index.
- Sharing follows existing team policy. Permission changes, folder creation or reorganization require explicit authorization. Proposed retention is indefinite until Managers approve a retention policy; no automatic cleanup is installed.

Related code/issues may be linked in [ESP32DataLogger](https://github.com/McGill-Baja-Racing/ESP32DataLogger) or [ProjectBoard](https://github.com/McGill-Baja-Racing/ProjectBoard). This repository does not move or alter those records.
