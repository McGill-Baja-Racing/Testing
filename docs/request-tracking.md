# Reviewing testing requests

The Testing Manager coordinates review with the Subsystem Lead and Electronics Manager. Managers decide priorities and resources.

## Review the request

- Check the engineering objective, essential measurements and their justification, planned subsystem analysis/output, analysis owner, vehicle/setup, preparation and proposed method/location. Accept explained Unknown/need-help responses for unresolved technical details; ask specific follow-up questions. Each essential measurement should have a clear use in the planned analysis.
- Check the analysis deadline and its engineering milestone, estimated analysis duration, raw-data delivery deadline and flexibility. Dates should include the year in `YYYY-MM-DD` format, or explicitly state No fixed deadline. Verify that the handoff date allows the subsystem enough analysis time and margin. Next testing day alone does not justify urgency. GitHub required fields cannot validate dates or answer quality; reviewers must check them.
- Electronics assesses instrumentation feasibility and preparation needs with the requesting Subsystem Lead and relevant teams; estimate effort and dependencies. A screen or an assigned person is not a resource commitment.
- Record Managers' individual test decision and priority/resource reasoning in a dated issue comment. Uncertain methods may need a bounded feasibility check before further preparation; a test-value approval is not unlimited authorization.

## After approval: plan and prepare together

Managers' request approval recognizes test value and priority; it does not mean ready or scheduled. Use the **original issue** for follow-up discussions, decisions and preparation updates.

The requesting Subsystem Lead remains responsible for engineering requirements, the subsystem's contribution to preparation, and arranging processing, analysis and interpretation. Testing is responsible for collecting the agreed data and delivering it; analysis-planning guidance does not make Testing responsible for subsystem analysis. Electronics and other technical owners work with the lead to define the measurement system and appropriate methods. For significant work, clarify together and record a short checklist covering:

- What must be defined or done: sensor installation, calibration/validation methods, procedures, fixtures or vehicle modifications, as applicable.
- Who owns each task, what capacity relevant resource managers have confirmed, and agreed preparation deadlines. Capacity must be confirmed before Managers authorize substantial preparation work.
- Required readiness checks and their completion evidence for the intended test/configuration.

The Testing Manager coordinates follow-up. Keep approved requests in `testing:needs-preparation` while planning, preparation or capacity remains unresolved. Record Managers' approval in a dated comment; a tracking label is not proof of approval. The label table below distinguishes preparation, readiness and date confirmation.

## Tracking labels and data handoff

| Label | When to use it |
| --- | --- |
| `testing:needs-review` | New request; the form selects this existing label. |
| `testing:needs-clarification` | A specific question needs an answer; write it in the issue. |
| `testing:needs-preparation` | Approved request still being planned or prepared, including unresolved capacity; do not imply readiness or a confirmed date. |
| `testing:ready` | Relevant owners have recorded completed preparation/readiness checks for this test/configuration. A date still needs separate confirmation by the Testing Manager. |
| `testing:completed` | Testing is complete, or the request was resolved without testing. Record the outcome; if data delivery is pending, also use `testing:needs-data` and keep the issue open. Completion does not imply a design passed. |
| `testing:needs-data` | Testing is done but data has not been delivered to the requesting subsystem. This supplementary label can accompany `testing:completed`; remove it after recording the handoff. |

Use one main progress label, replacing it as progress changes; `testing:needs-data` is the supplementary exception described above. Keep unrelated subsystem labels if useful. If configuration or scope changes affect readiness, reassess with relevant owners and return to preparation/clarification as needed. Record deferrals or declined requests in comments rather than adding more workflow states.

After testing, record the collected data or an accessible link on the original issue, identifying runs/configurations, units/timing information and known missing or unreliable measurements as applicable. Record who received the data and when. Remove `testing:needs-data` and close the completed request once handoff is recorded and no collection/delivery work remains. Subsystem analysis does not need to be finished before closing; a cancelled or declined request can close with its reason recorded and no data expected.

A Ready label or confirmed date is not permission to operate. The Subsystem Lead and Testing Manager still jointly decide final go/no-go, subject to required technical/safety clearance. Anyone can stop unsafe work; making safe never waits for an issue.

[Return to the README](../README.md).
