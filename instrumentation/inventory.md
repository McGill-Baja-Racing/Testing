# Equipment inventory

**Production register:** no real equipment records have been supplied for this revision. The Instrumentation Owner maintains the tables below as equipment is entered. Do not infer team stock or capability from [fictional examples](../examples/instrumentation.md).

## Model capabilities

| Model ID | Manufacturer/model and datasheet revision | Quantity/range | Response/bandwidth | Accuracy/uncertainty basis | Interface/environment limits |
| --- | --- | --- | --- | --- | --- |

## Physical units and availability

| Device ID | Model ID | Serial/asset ID | Custodian/location | Availability and condition | Calibration record/version |
| --- | --- | --- | --- | --- | --- |

## Installation and readiness for intended use

| Installation ID/revision | Device ID | Test/configuration/intended use | Calibration validity/limits | Installed verification evidence | Readiness + technical owner/date |
| --- | --- | --- | --- | --- | --- |

Create one [equipment/install record](../templates/sensor-record.md) per unit/installation and link its [calibration record](../templates/calibration-record.md). Use unique stable device IDs, including separate units of the same model. Retain superseded versions and damage/maintenance history. Calibration needs method, original evidence, reference traceability/validity, uncertainty, limits and a justified validity interval or condition/use triggers.

**Available** means a unit can be allocated. **Ready for this test** means the actual unit, installed chain, configuration and intended use have the required evidence and technical sign-off. Neither model availability nor a calibration sticker proves readiness.

Changing mounting, wiring, bonding, firmware, scaling, range, sample settings, environment or intended use can invalidate installed readiness. The Testing Manager determines reassessment with relevant technical/safety owners and repeats affected checks. A damaged device or replacement unit cannot inherit another unit's sign-off.

Pending preparation: follow the linked tasks on each test or the [Preparation workload view](../docs/project-setup.md#views). Electronics Manager owns Electronics capacity commitments. [Instrumentation guide](../docs/guides/instrumentation.md).
