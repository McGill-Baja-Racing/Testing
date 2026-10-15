# Technical testing — approved Stage 2

Every test states its engineering question, measured quantities, intended outputs and sufficient evidence. Quantitative pass/fail limits are used where appropriate, with a traceable requirement, calculation, simulation, reference or reasoned engineering basis. Exploratory/diagnostic work needs a definite question but no invented threshold. Subsystem leads own criteria; the Testing Manager reviews clarity/testability without changing objectives unilaterally.

The subsystem defines physical need and operating conditions. Electronics/specialists translate that into sensor location, range, bandwidth/dynamic response, sampling, acceptable uncertainty, calibration/reference verification, environment, DAQ/timebase/logging and known limitations. There is no universal sampling rate, accuracy, repeat count or calibration recipe. Justify these for the intended use.

Use one [modular plan](../../templates/test-plan.md). Core sections apply to all tests; add complexity, safety and design-of-experiments detail as justified. Technical complexity and operational safety risk are independent assessments. Required records scale with the test, not with a fixed paperwork quota.

[Readiness](../../templates/readiness-checklist.md) covers installation, calibration/reference validity, signal chain, units, timebase/logging and installed integrated verification where practical. Technical owners sign the particular configuration/intended use. If an integrated check is unsafe or inapplicable, record why, alternate evidence and responsible owner clearance; do not silently mark it done. Configuration changes can invalidate readiness.

Retain original raw data without overwriting. Unique test/run IDs connect logs, configuration versions, analysis code, reports and calibration/equipment records. Check data after runs where feasible and at least before leaving when practical. Log deviations, missing data and limitations explicitly. Default results are an issue summary; complex/critical tests need a detailed report linked from that same issue. Reports describe actual method, deviations, metrics, uncertainty, conclusion and follow-up.

[Inventory](../../instrumentation/inventory.md) distinguishes model capability, unique physical devices, installation and calibration evidence. Model availability or a calibration sticker alone never proves readiness of an integrated system.
