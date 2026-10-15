# Analysis and closure

During planning name analysis owner and agreed due date. Subsystem owns analysis; electronics supports processing and data-quality judgments. Proposed pilot reminder rule: Testing Manager reminds owner when overdue; if unresolved after the next agreed check-in (default seven calendar days), escalates to subsystem lead and leadership. Record actions in the issue; agree shorter intervals when urgency warrants. No reminder automation is installed.

Post [results summary](../../templates/results-summary.md) on the same test issue. Complex/critical tests link a [report](../../templates/test-report.md). Include actual procedure, deviations, raw/run/config/calibration references, processing/code versions, metrics, uncertainty/limitations and conclusions.

| Attempt validity | Meaning | Design/requirement handling |
| --- | --- | --- |
| valid | Evidence supports the stated evaluation within limitations | PASS or FAIL only against applicable justified criteria; exploratory findings may be not assessed |
| inconclusive | Evidence cannot resolve the question | Linked follow-up for unresolved objectives; requirements remain unverified |
| invalid | Method/data unsuitable | Preserve data and failure reasons; linked follow-up; requirements remain unverified |
| aborted | Stopped before intended completion | Record stop/clearance history and unresolved objectives; follow-up or explicit disposition |

Subsystem lead approves conclusions and updates DVP&R with evidence applicability. Testing Manager checks logs, data access, plan/configuration, outcome, analysis, sign-offs and linked follow-ups before closing the attempt. An unsuccessful attempt may close once documented; requirement status does not become verified through issue closure. A valid design failure is evidence, not an invalid test.

If analysis cannot be completed, explicitly record why, limitations, unresolved objectives and disposition with lead/Testing Manager acknowledgment; never claim validity or verification from missing analysis. Substantial follow-up scope changes return to screening and reauthorization. [DEMO invalid-run follow-up](../../examples/follow-up.md).
