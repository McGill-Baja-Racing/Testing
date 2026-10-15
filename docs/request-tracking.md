# Reviewing testing requests

The Testing Manager coordinates review with the Subsystem Lead and Electronics Manager. Managers decide priorities and resources. Formal requests come from Subsystem Leads; the form cannot technically verify that role, so confirm it during review.

## Review the request

- Check the objective, measurements/outputs, vehicle readiness, proposed method/location, need-by date, justification and consequences. Accept Unknown/TBD for technical details that require specialist help; ask specific follow-up questions.
- Check the need-by date is a real calendar date in `YYYY-MM-DD` format, including the year. GitHub's required input cannot validate the date format or prove completeness; reviewers must check it.
- Assess preparation tasks, feasibility, dependencies and effort with the relevant teams. A screen or an assigned person is not a resource commitment. Resource managers, including the Electronics Manager, confirm capacity before Managers authorize defined preparation.
- Record Managers' individual test decision and priority/resource reasoning in a dated issue comment. Uncertain methods may need a bounded feasibility check before further preparation; a test-value approval is not unlimited authorization.

## Use one current tracking label

| Label | When to use it |
| --- | --- |
| `testing:needs-review` | New request; the form selects this label once it exists in GitHub. |
| `testing:needs-clarification` | A specific question needs an answer; write it in the issue. |
| `testing:needs-preparation` | Required preparation or capacity remains unresolved; do not imply a confirmed date. |
| `testing:ready` | The relevant owners have recorded that necessary preparation and readiness checks are complete for this test/configuration. The Testing Manager can then coordinate confirmation. |
| `testing:completed` | Record the result or why testing did not proceed, then close the request. Completion does not imply a design passed. |

Replace the previous tracking label as progress changes; keep unrelated subsystem labels if useful. If configuration or scope changes affect readiness, reassess with relevant owners and return to preparation/clarification as needed. Record deferrals or declined requests in comments rather than adding more workflow states.

A Ready label or confirmed date is not permission to operate. The Subsystem Lead and Testing Manager still jointly decide final go/no-go, subject to required technical/safety clearance. Anyone can stop unsafe work; making safe never waits for an issue.

[Return to the README](../README.md).
