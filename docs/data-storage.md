# Data naming, retention and archive proposal

No Drive folders or permissions have been created. Proposed layout in the existing team Drive:

```text
Testing Data/<season>/<test-id>_<short-name>/
  raw/
  video/
  processed/
  supporting/
```

Testing Manager allocates IDs such as `TST-DEMO-001` in the pilot; production proposal is `TST-<season>-<sequence>` from one allocation register. Never reuse IDs. Run IDs append `-R001`, including failed/aborted attempts. An independently authorized retest uses a new test ID and links the prior attempt. Stable requirement IDs are independent of season/test numbering.

File convention: `<test-id>_<run-id>_<stream>_<UTC-timestamp>_<config-rev>.<ext>`. Timestamp format `YYYYMMDDTHHMMSSZ`; record local offset separately when useful. Avoid spaces and ambiguous local times. Every stream/video includes run and synchronization reference. [Run log](../templates/run-log.csv) uses ISO 8601 start/end timestamps with offsets, configuration/version reference, conditions, observations/deviations, raw-data reference and calibration reference. Record no-calibration-required with rationale where appropriate.

Retain original raw data without overwriting or deleting it during processing. Preserve invalid/aborted runs. New derivations go in processed with versioned parameters/code commits; supporting holds plans, installation/calibration records, metadata and reports. Keep a manifest of original filenames, sizes and checksums when importing; if names change at import, preserve mapping and originals. Preserve raw even when corrected metadata is added alongside it. Proposed retention is indefinite pending explicit team retention policy; no automatic cleanup.

Minimum supporting metadata: test/run IDs; actual conditions; configuration/firmware/analysis commits; physical device IDs; install/calibration versions and validity; units/scaling; sampling/timebase; operators; plan revision; deviations/data checks; manifest; processing instructions and result links. GitHub holds small metadata, procedures, calibration descriptions and code, with stable links to large data.

Use `<DRIVE_FOLDER_LINK_PENDING_AUTHORIZATION>` in local examples, never invented Drive URLs. After authorization, archive owner supplies stable folder/file links, confirms intended team access under existing policy, checks from a reader account and records custodian and backup arrangement. Do not expose private data by changing sharing without approval. Avoid moving folders after linking; if unavoidable keep a cross-reference and update issue index, logs and DVP&R. Testing Manager checks access at closure.

Existing [ProjectBoard](https://github.com/McGill-Baja-Racing/ProjectBoard) and [ESP32DataLogger](https://github.com/McGill-Baja-Racing/ESP32DataLogger) may be referenced by full issue/code links after actual references are known; no issues are moved or modified by this pilot.
