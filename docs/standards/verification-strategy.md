# Verification and validation

**Verification** asks whether a requirement is met. **Validation** asks whether the vehicle meets its intended use. A Design Verification Plan and Report (**DVP&R**) links requirements, methods, criteria and evidence; it is not a list of test issues alone.

Each **Subsystem Lead** maintains a focused, evolving DVP&R for important requirements, safety/performance goals, critical assumptions, failure risks and known historical failures. Start with a useful subset. Do not require exhaustive cataloguing on day one. **Managers** review coverage and gaps at major design milestones and maintain the [vehicle overview](../../verification/vehicle.md); continuous Testing Manager audits are not required.

## What a row records

Stable requirement ID, description, owner, method (analysis, inspection, demonstration, test or combination), acceptance criteria and engineering rationale, target milestone, planned work/evidence links, applicable configuration/conditions and status. One test can support several requirements; one requirement can need several kinds of evidence. [Template](../../templates/dvp-r.md) · [examples/index](../../verification/README.md).

| Status | Meaning |
| --- | --- |
| not planned | Requirement identified; verification work not planned |
| planned | Method, owner and evidence plan identified |
| in progress | Evidence work underway; not verified |
| verified | Applicable evidence meets the criteria; owner records judgment |
| not verified-failed | Applicable valid evidence fails the criteria |
| insufficient evidence | Evidence cannot support the judgment |
| reverification required | Changes/failures invalidate or question prior applicability |
| N/A with reason | Owner records a justified non-applicability decision |

Update after evidence, significant design changes or failures. Reuse prior evidence only with a recorded configuration/conditions/applicability justification. Issue closure never automatically verifies a requirement. Invalid/inconclusive attempts leave relevant requirements unverified and require linked follow-ups for unresolved objectives. A valid design failure is not an invalid experiment.

Prioritize safety/severity, uncertainty, historical failures, evidence gaps, deadlines and effort—not only easy measurements or a misleading combined score. Managers' vehicle-level concerns become formal requests through the appropriate Subsystem Lead. No fictional example establishes actual verification or competition compliance.
