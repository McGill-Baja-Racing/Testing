# McGill Baja Racing — Testing Requests

## What is this repository?

A central place for McGill Baja Racing Subsystem Leads to request testing, communicate measurement needs and coordinate the preparation necessary to obtain useful results. This first release focuses on requests and review.

## How to request a test

**[Create a Test Request](https://github.com/McGill-Baja-Racing/Testing/issues/new?template=test-request.yml)**

Only **Subsystem Leads** submit formal requests. Other members should bring testing ideas to their Subsystem Lead.

Give the issue a clear title, such as “Measure engine speed during acceleration.” Explain what you want to determine, what to measure and why it matters. Include the vehicle, proposed method/location, known preparation and need-by date (`YYYY-MM-DD`). Link existing requirements where relevant; do not copy them into this repository.

You do not need exact sensor models, sampling rates or a finished procedure. Enter **Unknown** or **TBD** when a technical detail needs help from another team. The Electronics Manager can help clarify instrumentation needs.

## What happens next?

1. The request is reviewed for clarity and instrumentation requirements.
2. Preparation effort and feasibility are assessed.
3. Managers review priorities and resources.
4. The test is confirmed only when the necessary preparation and readiness checks are completed.

The Testing Manager coordinates follow-up. **Submitting an issue does not guarantee testing on the requested date.**

## Where to see testing requests

Follow requests on the **[Issues page](https://github.com/McGill-Baja-Racing/Testing/issues)**. We use five tracking labels:

- `testing:needs-review` — new request awaiting review.
- `testing:needs-clarification` — more information is needed.
- `testing:needs-preparation` — preparation remains before confirmation.
- `testing:ready` — necessary preparation and readiness checks are complete.
- `testing:completed` — the request is resolved and its outcome is recorded.

See the short [request tracking guide](docs/request-tracking.md) for reviewer responsibilities. Labels summarize progress; they do not authorize vehicle operation.
