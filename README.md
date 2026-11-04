# McGill Baja Racing — Testing Requests

## What is this repository?

A central place for McGill Baja Racing to request testing, communicate measurement needs and coordinate the preparation necessary to obtain useful results. Testing collects the agreed data and delivers it to the requesting subsystem; that subsystem owns processing, analysis and interpretation.

## How to request a test

**[Create a Test Request](https://github.com/McGill-Baja-Racing/Testing/issues/new?template=test-request.yml)**

Give the issue a clear title, such as “Measure engine speed during acceleration.” Explain what you want to determine, what to measure and why it matters. Identify essential measurements and why they are needed, the planned analysis and output, and who in your subsystem will own analysis. Include the vehicle/setup, proposed method/location and known preparation. Name existing requirements if applicable.

Plan backward from the engineering milestone: give your analysis completion date and its justification, estimate how long analysis will take, then state when Testing must deliver the raw/unprocessed data (`YYYY-MM-DD`, or No fixed deadline). Indicate whether that delivery deadline can move. The next testing day alone does not justify an engineering deadline.

You do not need exact sensor models, sampling rates or a finished procedure. Enter **Unknown** or **TBD** when a technical detail needs help from another team. Required questions need an answer, but you can explain where you need help; requirement references and event-timing estimates are optional. Complete, well-supported answers reduce follow-up and improve the chance of earlier testing, subject to priorities, resources and readiness. The Electronics Manager can help clarify instrumentation needs; planning guidance does not transfer analysis responsibility to Testing.

## What happens next?

1. Submit a preliminary testing request.
2. The request is reviewed for clarity, feasibility and estimated effort; Electronics assesses instrumentation needs.
3. Managers review priorities and resources and decide whether to approve the request.
4. The requesting Subsystem Lead and relevant technical teams develop the detailed plan and complete preparation together.
5. The Testing Manager confirms testing only after required preparation and readiness checks are complete.
6. After testing, Testing delivers the recorded data and relevant run context/limitations on the original issue. The requesting subsystem then performs its analysis.

**Request approval does not mean the test is ready, scheduled or guaranteed for the requested date.** The requesting subsystem remains responsible for its engineering requirements and contributes to preparation. After approval, the Subsystem Lead may be contacted to clarify technical details, develop calibration or validation methods, complete preparation tasks and agree on responsibilities/deadlines. Relevant resource managers confirm capacity before substantial work is committed.

Keep follow-up discussions and preparation updates on the original issue; the Testing Manager coordinates them.

## Where to see testing requests

Follow requests on the **[Issues page](https://github.com/McGill-Baja-Racing/Testing/issues)**. The tracking labels are:

- `testing:needs-review` — new request awaiting review.
- `testing:needs-clarification` — more information is needed.
- `testing:needs-preparation` — approved request still being planned or prepared; not confirmed.
- `testing:ready` — necessary preparation and readiness checks are complete.
- `testing:completed` — testing is complete or the request has been resolved without testing; record the outcome.
- `testing:needs-data` — testing is done but data has not yet been delivered. It can accompany `testing:completed`; keep the issue open until handoff is recorded.

See the short [request tracking guide](docs/request-tracking.md) for reviewer responsibilities. Labels summarize progress; they do not authorize vehicle operation.
