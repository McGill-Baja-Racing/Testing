# EXAMPLE equipment, calibration and installation

**Entirely fictional.** Capabilities, IDs, dates, readings and owners below are fabricated for training. They do not establish team inventory or readiness. [Operational inventory](../instrumentation/inventory.md).

## Model capability and physical units

| Model ID | Fabricated capability | Device ID | Serial/owner/location | Availability |
| --- | --- | --- | --- | --- |
| EXAMPLE-M-RPM | Digital pulse pickup; example 0–9000 rpm range; pulse count interpreted by example firmware | EXAMPLE-DEV-RPM-01 | EXAMPLE serial R01 / Electronics member A / bench | available in narrative only |
| EXAMPLE-M-P | Example 0–10 MPa pressure transducer; 0.5–4.5 V output | EXAMPLE-DEV-P-01 | EXAMPLE serial P01 / Electronics member B / bench | awaiting adaptation in narrative |
| EXAMPLE-M-S | Example strain bridge/conditioner; torque mapping not established | EXAMPLE-DEV-S-01 | EXAMPLE serial S01 / Electronics member C / bench | available hardware, not ready |

## Calibration/reference records

| Record/version | Device/scope | Method and fabricated observations | Validity/traceability and limitations | Contextual judgment |
| --- | --- | --- | --- | --- |
| EXAMPLE-CAL-RPM-01/v1 | EXAMPLE-DEV-RPM-01; EXAMPLE-config-A | Pulse-generator reference at equivalent 1500/3000/4500 rpm; fabricated displayed 1502/2998/4504 rpm | EXAMPLE reference PG-01, fictional certificate valid through 2099-02-01; estimated ±10 rpm at these points; review after firmware/wiring changes or before each campaign | Narrative reference check only; no real calibration |
| EXAMPLE-CAL-P-01/v1 | EXAMPLE-DEV-P-01; bench configuration | Fabricated reference checks at 0/2/4 MPa; reconstructed 0.00/2.01/3.99 MPa | EXAMPLE pressure reference PR-01, fictional certificate valid through 2099-02-01; estimated ±0.03 MPa in 0–4 MPa only; temperature/mounting applicability still required | Standalone example check does not authorize installed use |
| EXAMPLE-CAL-S-PROPOSED | EXAMPLE-DEV-S-01 | Proposed reversible reference-load fixture; no readings/calibration yet | Load mapping, traceability, temperature sensitivity and uncertainty unresolved | blocked; not a calibration certificate |

Dates refer to a hypothetical exercise beginning 2099-01-01. Reference traceability above is a fabricated chain, never a claimed accredited certificate. Real records use the [calibration template](../templates/calibration-record.md), link original readings, and justify validity for intended use.

## Installation and readiness

| Installation/version | Device/configuration/intended use | Checks and readiness in the narrative |
| --- | --- | --- |
| EXAMPLE-INST-RPM-01/v1 | EXAMPLE-DEV-RPM-01 / EXAMPLE-config-A / low-frequency speed trace | Existing validated configuration assumed only for the example; repeat installed pulse-to-file verification, units/timebase and reference check before any readiness decision |
| EXAMPLE-INST-P-01/v1 | EXAMPLE-DEV-P-01 / EXAMPLE-config-B / pressure trace | Adapter compatibility, mounting and installed scaling verification required; invalid sample run demonstrates how a mismatch can invalidate evidence |
| EXAMPLE-INST-S-01/proposed | EXAMPLE-DEV-S-01 / EXAMPLE-config-C / strain-to-torque assessment | Bonding/rotating interface/load mapping not established; no readiness until separate full preparation and successful installed verification |

No row is an actual owner sign-off. The [equipment template](../templates/sensor-record.md) links calibration and installed evidence. Changing wiring, settings, mounting or intended use can require new checks even if the unit remains available.
