# Verification and validation — approved Stage 3

Start with a focused subsystem DVP&R for major requirements, safety/performance, important design assumptions and known failure risks; grow coverage over time. Subsystem leads maintain it at completed verification and after significant modifications/failures. Leadership reviews completeness and risks at major design milestones. Continuous mandatory Testing Manager audits are not required.

Each [DVP&R row](../../templates/dvp-r.md) keeps a stable requirement ID, description, owner, method (test/analysis/inspection/demonstration), acceptance criteria and rationale, target milestone, evidence and status. Allowed statuses: not planned; planned; in progress; verified; not verified-failed; insufficient evidence; reverification required; N/A with reason. N/A requires an explicit reason and owner decision.

One test can support many requirements and one requirement can need many tests. Issue closure never automatically verifies a requirement. Reuse prior evidence only with an explicit configuration, conditions and applicability justification. A modification/failure triggers owner review of affected evidence and reverification scope. Invalid/inconclusive evidence leaves requirements unverified, normally insufficient evidence; a valid failure becomes not verified-failed only when applicable criteria support that conclusion.

Leadership maintains the compact [vehicle validation overview](../../verification/vehicle.md): performance, reliability, integration, durability and safety. Subsystem leads still file individual requests for vehicle-level concerns.

Prioritize using safety/severity, uncertainty, historical failure, evidence gap, deadline and effort. Record the reasoning and resource constraints rather than collapsing subjective ratings into one misleading numerical score. Example requirements/limits are placeholders until owners establish engineering targets; no sample row claims actual verification.
