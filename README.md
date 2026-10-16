# McGill Baja Racing — Testing Requests

## What is this repository?

A central place for McGill Baja Racing Subsystem Leads to request testing, communicate measurement needs and coordinate the preparation necessary to obtain useful results. This first release focuses on requests and review.

## How to request a test

**[Create a Test Request](https://github.com/McGill-Baja-Racing/Testing/issues/new?template=test-request.yml)**

Only **Subsystem Leads** submit formal requests. Other members should bring testing ideas to their Subsystem Lead.

Give the issue a clear title, such as “Measure engine speed during acceleration.” Explain what you want to determine, what to measure and why it matters. Include the vehicle, proposed method/location, known preparation and need-by date (`YYYY-MM-DD`). Link existing requirements where relevant; do not copy them into this repository.

You do not need exact sensor models, sampling rates or a finished procedure. Enter **Unknown** or **TBD** when a technical detail needs help from another team. The Electronics Manager can help clarify instrumentation needs.

## What happens next?

1. The Subsystem Lead submits a preliminary testing request.
2. The request is reviewed for clarity, feasibility and estimated effort; Electronics assesses instrumentation needs.
3. Managers review priorities and resources and decide whether to approve the request.
4. The requesting Subsystem Lead and relevant technical teams develop the detailed plan and complete preparation together.
5. The Testing Manager confirms testing only after required preparation and readiness checks are complete.

**Request approval does not mean the test is ready, scheduled or guaranteed for the requested date.** The requesting subsystem remains responsible for its engineering requirements and contributes to preparation. After approval, the Subsystem Lead may be contacted to clarify technical details, develop calibration or validation methods, complete preparation tasks and agree on responsibilities/deadlines. Relevant resource managers confirm capacity before substantial work is committed.

Keep follow-up discussions and preparation updates on the original issue; the Testing Manager coordinates them.

## Where to see testing requests

Follow requests on the **[Issues page](https://github.com/McGill-Baja-Racing/Testing/issues)**. We use five tracking labels:

- `testing:needs-review` — new request awaiting review.
- `testing:needs-clarification` — more information is needed.
- `testing:needs-preparation` — approved request still being planned or prepared; not confirmed.
- `testing:ready` — necessary preparation and readiness checks are complete.
- `testing:completed` — the request is resolved and its outcome is recorded.

See the short [request tracking guide](docs/request-tracking.md) for reviewer responsibilities. Labels summarize progress; they do not authorize vehicle operation.
