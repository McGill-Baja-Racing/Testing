# Managers quick start

**Managers decide test value, priority and authorization.** The Testing Manager coordinates the work; resource managers commit their own teams' capacity.

## At regular management meetings

1. Review complete requests after quick specialist screening. Consider safety relevance/severity, performance impact, urgency, uncertainty, historical failures, evidence gaps, preparation effort, dependencies and capacity. Record a reasoned priority; do not combine subjective ratings into a misleading numerical score.
2. Decide each test individually: approve its value, defer with a review trigger, decline with a reason, or request clarification. The designated test-approval Manager records identity/date/scope and rationale in GitHub; any Manager may substitute. [Decision record](../../templates/approval-record.md).
3. For unknown measurement feasibility, obtain the resource manager's bounded capacity commitment, then authorize an investigation with a cap, deliverable and stop/review point. Review its outcome before considering full development.
4. For preparation, resource managers first confirm available capacity, owners, defined work, estimates and dates, and limits on simultaneous work. **Managers then authorize that defined preparation.** Value approval does not authorize unlimited effort. Uncommitted work stays Awaiting Capacity.
5. Resolve testing-time conflicts. Review blockers and analysis deadlines with the Testing Manager; use the [Project views or issue fallback](../project-setup.md). Only technically prepared tests can enter the confirmed schedule.

Urgent new tests still need an individual Manager approval. The Testing Manager and affected leads may rearrange already approved work. Stopping, inspection and making safe never wait for request paperwork.

## At major design milestones

Review subsystem [DVP&R coverage and gaps](../../verification/README.md) and maintain the [vehicle validation overview](../../verification/vehicle.md). Direct missing test needs to the appropriate Subsystem Lead for formal submission. Reuse earlier evidence only when configuration and conditions remain applicable.

[Five gates](approvals.md) · [Lifecycle](../standards/testing-lifecycle.md) · [Start here](../../README.md#start-here)
