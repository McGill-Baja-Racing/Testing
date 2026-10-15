# Sensor inventory — DEMO only

Models describe capability; device records track physical units; installation/calibration records establish contextual readiness. All capabilities, IDs and evidence below are hypothetical placeholders. No hardware specification or actual readiness is asserted.

## Model/capability register

| Model ID | Manufacturer/model | Quantity | Range | Dynamic response/bandwidth | Accuracy/uncertainty basis | Interface/environment | Datasheet/version |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MODEL-DEMO-RPM | TBD by owner | Engine speed | TBD | TBD | TBD for intended use | TBD | Not supplied |
| MODEL-DEMO-PRESSURE | TBD by owner | Brake pressure | TBD | TBD | TBD | Compatibility/pressure/environment TBD | Not supplied |
| MODEL-DEMO-STRAIN | TBD by owner | Half-shaft strain | TBD | TBD | TBD incl. torque conversion | Bonding/bridge/telemetry TBD | Not supplied |

## Individual physical devices

| Device ID | Model ID | Serial/asset ID | Custodian/location | Condition | Calibration record | Installation record |
| --- | --- | --- | --- | --- | --- | --- |
| DEV-DEMO-RPM-001 | MODEL-DEMO-RPM | DEMO-not-real | DEMO electronics | Unknown in reality | CAL-DEMO-001 | INST-DEMO-001 |
| DEV-DEMO-P-001 | MODEL-DEMO-PRESSURE | DEMO-not-real | DEMO electronics | Unknown | Pending | Pending |
| DEV-DEMO-S-001 | MODEL-DEMO-STRAIN | DEMO-not-real | DEMO electronics | Unknown | Pending | Pending |

## Installation/calibration/readiness records

Use [record template](../templates/sensor-record.md) per device/install and link immutable record versions. Required calibration content: method/procedure version; date/operator; reference ID and traceability chain; reference validity; points/conditions and raw evidence; coefficients/units; uncertainty and limits; validity interval or usage/condition triggers with rationale. Do not assume a universal expiry period.

| Record ID | Device/configuration | Method/evidence | Validity/traceability | Contextual readiness |
| --- | --- | --- | --- | --- |
| CAL-DEMO-001 | DEV-DEMO-RPM-001; DEMO historical configuration A | Hypothetical reference comparison; no real evidence | Reference ID/validity, date, uncertainty and limits all TBD; unusable as real calibration | Not established |
| INST-DEMO-001 | DEV-DEMO-RPM-001; configuration A / intended engine-speed use | Hypothetical wiring, mounting and DAQ revision; all TBD | Must link calibration and installed signal-chain check | Not established in reality; example A assumes prior validated configuration solely for walkthrough |

Changing mounting, wiring, bridge bonding, firmware, scaling, sample settings, range, environment or intended use may invalidate integration readiness even if a device calibration remains valid. Testing Manager determines reassessment with instrumentation/technical/safety owners. A spare of the same model has a different device ID and requires its own records. Failed/damaged devices retain history and cannot inherit another unit's sign-off.
