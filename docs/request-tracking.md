# Reviewing testing requests

The Testing Manager coordinates review with the Subsystem Lead and Electronics Manager. Managers decide priorities and resources.

## Review the request

- Check the objective, measurements/outputs, vehicle readiness, proposed method/location, need-by date, justification and consequences. Accept Unknown/TBD for technical details that require specialist help; ask specific follow-up questions.
- Check the need-by date is a real calendar date in `YYYY-MM-DD` format, including the year. GitHub's required input cannot validate the date format or prove completeness; reviewers must check it.
- Electronics assesses instrumentation feasibility and preparation needs with the requesting Subsystem Lead and relevant teams; estimate effort and dependencies. A screen or an assigned person is not a resource commitment.
- Record Managers' individual test decision and priority/resource reasoning in a dated issue comment. Uncertain methods may need a bounded feasibility check before further preparation; a test-value approval is not unlimited authorization.

## After approval: plan and prepare together

Managers' request approval recognizes test value and priority; it does not mean ready or scheduled. Use the **original issue** for follow-up discussions, decisions and preparation updates.

The requesting Subsystem Lead remains responsible for engineering requirements and the subsystem's contribution to preparation. Electronics and other technical owners work with the lead to define the measurement system and appropriate methods. For significant work, clarify together and record a short checklist covering:

- What must be defined or done: sensor installation, calibration/validation methods, procedures, fixtures or vehicle modifications, as applicable.
- Who owns each task, what capacity relevant resource managers have confirmed, and agreed preparation deadlines. Capacity must be confirmed before Managers authorize substantial preparation work.
- Required readiness checks and their completion evidence for the intended test/configuration.

The Testing Manager coordinates follow-up. Keep approved requests in `testing:needs-preparation` while planning, preparation or capacity remains unresolved. Record Managers' approval in a dated comment; a tracking label is not proof of approval. The label table below distinguishes preparation, readiness and date confirmation.

## Use one current tracking label

| Label | When to use it |
| --- | --- |
| `testing:needs-review` | New request; the form selects this existing label. |
| `testing:needs-clarification` | A specific question needs an answer; write it in the issue. |
| `testing:needs-preparation` | Approved request still being planned or prepared, including unresolved capacity; do not imply readiness or a confirmed date. |
| `testing:ready` | Relevant owners have recorded completed preparation/readiness checks for this test/configuration. A date still needs separate confirmation by the Testing Manager. |
| `testing:completed` | Record the result or why testing did not proceed, then close the request. Completion does not imply a design passed. |

Replace the previous tracking label as progress changes; keep unrelated subsystem labels if useful. If configuration or scope changes affect readiness, reassess with relevant owners and return to preparation/clarification as needed. Record deferrals or declined requests in comments rather than adding more workflow states.

A Ready label or confirmed date is not permission to operate. The Subsystem Lead and Testing Manager still jointly decide final go/no-go, subject to required technical/safety clearance. Anyone can stop unsafe work; making safe never waits for an issue.

[Return to the README](../README.md).
