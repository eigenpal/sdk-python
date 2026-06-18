# eigenpal reference

## Quick example

```python
import os
from pathlib import Path
from eigenpal import EigenpalClient

client = EigenpalClient(api_key=os.environ["EIGENPAL_API_KEY"])

# Run a workflow with a file input (multipart upload, no base64).
result = client.run_and_wait(
    "workflows.extract-invoice",
    input={"contract": Path("contract.pdf")},
)
print(result["finished"], result["output"])
```

## Surface

```
client
├── run
├── rerun
├── automations
│   ├── list
│   ├── get
│   ├── versions
│   ├── dataset
│   │   ├── export
│   │   └── import_
│   ├── evaluators
│   │   ├── get
│   │   └── update
│   ├── examples
│   │   ├── list
│   │   ├── get
│   │   ├── create
│   │   ├── delete
│   │   ├── run
│   │   └── update
│   ├── experiments
│   │   ├── list
│   │   ├── get
│   │   ├── cancel
│   │   └── create
│   └── triggers
├── runs
│   ├── list
│   ├── get
│   ├── artifacts
│   │   ├── list
│   │   └── download
│   ├── cancel
│   ├── eval_results
│   │   └── list
│   ├── events
│   ├── feedback
│   │   ├── get
│   │   ├── clear
│   │   └── update
│   ├── promote
│   ├── steps
│   ├── trace
│   │   └── get
│   └── usage
├── files
│   ├── get
│   ├── delete
│   ├── download
│   └── upload
└── auth
    └── check
```

Start runs with `client.run(...)` and create a new run from a previous snapshot with `client.rerun(...)`.

Run inspection, artifacts, traces, usage, events, and feedback live under `client.runs.*`, which maps to `/api/v1/runs`.

Reusable upload-first files live under `client.files.*`; once a file is referenced by a run, Eigenpal snapshots it into run-scoped artifacts.

## Client construction

```python
import os
from eigenpal import EigenpalClient

client = EigenpalClient(
    api_key=os.environ["EIGENPAL_API_KEY"],
    # For self-hosted deployments:
    base_url=os.environ.get("EIGENPAL_BASE_URL"),
)
```

The constructor argument always wins; the env var is a fallback so scripts don't have to write `api_key=os.environ["EIGENPAL_API_KEY"]` explicitly.

| Option            | Type    | Default                                          | Description                                       |
| ----------------- | ------- | ------------------------------------------------ | ------------------------------------------------- |
| `api_key`         | `str`   | `os.environ["EIGENPAL_API_KEY"]`                 | Bearer key from the dashboard.                    |
| `base_url`        | `str`   | `os.environ.get("EIGENPAL_BASE_URL")` or default | API host. Set to your deployment for self-hosted. |
| `timeout_seconds` | `float` | `60.0`                                           | Per-request timeout.                              |

## Metadata

### `client.auth.check`

**`GET /api/v1/auth/check`**

Check API key identity

Return the tenant, user, API key, and scope represented by the current API key.

**Response**

```python
// AuthCheckResponse
```

## Evaluation

### `client.automations.dataset.export`

**`GET /api/v1/automations/:id/dataset/export`**

Export automation dataset

**Path parameters**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | `str` |             |

**Query parameters**

| Name          | Type  | Description |
| ------------- | ----- | ----------- |
| `example_ids` | `str` | (optional)  |

**Response**

```python
// str
```

### `client.automations.dataset.import_`

**`POST /api/v1/automations/:id/dataset/import`**

Import automation dataset

**Path parameters**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | `str` |             |

**Response**

```python
// DatasetImportResponse
```

### `client.automations.evaluators.get`

**`GET /api/v1/automations/:id/evaluators`**

Get automation evaluators

**Path parameters**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | `str` |             |

**Response**

```python
// EvaluatorConfigResponse
```

### `client.automations.evaluators.update`

**`PUT /api/v1/automations/:id/evaluators`**

Replace automation evaluators

**Path parameters**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | `str` |             |

**Request body**

```python
// EvaluatorConfigUpdate
```

**Response**

```python
// EvaluatorConfigResponse
```

### `client.automations.examples.get`

**`GET /api/v1/automations/:id/examples/:exampleId`**

Get automation example

**Path parameters**

| Name         | Type  | Description |
| ------------ | ----- | ----------- |
| `id`         | `str` |             |
| `example_id` | `str` |             |

**Response**

```python
// DatasetExample
```

### `client.automations.examples.update`

**`PATCH /api/v1/automations/:id/examples/:exampleId`**

Update automation example

**Path parameters**

| Name         | Type  | Description |
| ------------ | ----- | ----------- |
| `id`         | `str` |             |
| `example_id` | `str` |             |

**Request body**

```python
// DatasetExampleUpdate
```

**Response**

```python
// DatasetExample
```

### `client.automations.examples.delete`

**`DELETE /api/v1/automations/:id/examples/:exampleId`**

Delete automation example

**Path parameters**

| Name         | Type  | Description |
| ------------ | ----- | ----------- |
| `id`         | `str` |             |
| `example_id` | `str` |             |

**Response**

```python
// DatasetExample
```

### `client.automations.examples.run`

**`POST /api/v1/automations/:id/examples/:exampleId/run`**

Run automation example

**Path parameters**

| Name         | Type  | Description |
| ------------ | ----- | ----------- |
| `id`         | `str` |             |
| `example_id` | `str` |             |

**Response**

```python
// ExampleRunResponse
```

### `client.automations.examples.list`

**`GET /api/v1/automations/:id/examples`**

List automation examples

**Path parameters**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | `str` |             |

**Query parameters**

| Name     | Type  | Description |
| -------- | ----- | ----------- |
| `limit`  | `int` | (optional)  |
| `offset` | `int` | (optional)  |

**Response**

```python
// DatasetExampleList
```

### `client.automations.examples.create`

**`POST /api/v1/automations/:id/examples`**

Create automation example

**Path parameters**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | `str` |             |

**Request body**

```python
// DatasetExampleMutation
```

**Response**

```python
// DatasetExample
```

### `client.automations.experiments.list`

**`GET /api/v1/automations/:id/experiments`**

List automation experiments

**Path parameters**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | `str` |             |

**Query parameters**

| Name     | Type  | Description |
| -------- | ----- | ----------- |
| `limit`  | `int` | (optional)  |
| `offset` | `int` | (optional)  |

**Response**

```python
// dict[str, Any]
```

### `client.automations.experiments.create`

**`POST /api/v1/automations/:id/experiments`**

Create automation experiment

**Path parameters**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | `str` |             |

**Request body**

```python
// ExperimentCreate
```

**Response**

```python
// ExperimentCreateResponse
```

### `client.automations.experiments.cancel`

**`POST /api/v1/automations/:id/experiments/:experimentId/cancel`**

Cancel automation experiment

**Path parameters**

| Name            | Type  | Description |
| --------------- | ----- | ----------- |
| `id`            | `str` |             |
| `experiment_id` | `str` |             |

**Response**

```python
// ExperimentDetail
```

### `client.automations.experiments.get`

**`GET /api/v1/automations/:id/experiments/:experimentId`**

Get automation experiment

**Path parameters**

| Name            | Type  | Description |
| --------------- | ----- | ----------- |
| `id`            | `str` |             |
| `experiment_id` | `str` |             |

**Response**

```python
// ExperimentDetail
```

### `client.runs.eval_results.list`

**`GET /api/v1/runs/:id/eval-results`**

List run eval results

**Path parameters**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | `str` |             |

**Response**

```python
// EvalResultsResponse
```

## Automations

### `client.automations.get`

**`GET /api/v1/automations/:id`**

Get automation

Get one runnable workflow or agent automation by id or typed alias.

**Path parameters**

| Name | Type  | Description                                                             |
| ---- | ----- | ----------------------------------------------------------------------- |
| `id` | `str` | Workflow id, agent id, or typed alias like workflows.slug / agents.slug |

**Response**

```python
// AutomationDetail
```

### `client.automations.triggers`

**`GET /api/v1/automations/:id/triggers`**

Get automation triggers

Read trigger state for a workflow or agent automation. Trigger mutation is not public v1.

**Path parameters**

| Name | Type  | Description                                                             |
| ---- | ----- | ----------------------------------------------------------------------- |
| `id` | `str` | Workflow id, agent id, or typed alias like workflows.slug / agents.slug |

**Response**

```python
// AutomationTriggersResponse
```

### `client.automations.versions`

**`GET /api/v1/automations/:id/versions`**

List automation versions

List versions for a workflow or agent automation through one read-only route.

**Path parameters**

| Name | Type  | Description                                                             |
| ---- | ----- | ----------------------------------------------------------------------- |
| `id` | `str` | Workflow id, agent id, or typed alias like workflows.slug / agents.slug |

**Response**

```python
// ListAutomationVersionsResponse
```

### `client.automations.list`

**`GET /api/v1/automations`**

List automations

List runnable workflow and agent automations in one collection.

**Query parameters**

| Name     | Type                           | Description                                                  |
| -------- | ------------------------------ | ------------------------------------------------------------ |
| `search` | `str`                          | (optional)Substring match against slug, name, or description |
| `type`   | `Literal["workflow", "agent"]` | (optional)Filter by implementation type                      |
| `limit`  | `int`                          | (optional)                                                   |
| `offset` | `int`                          | (optional)                                                   |

**Response**

```python
// ListAutomationsResponse
```

## Files

### `client.files.download`

**`GET /api/v1/files/:id/content`**

Download file content

Download bytes for a reusable uploaded file.

**Path parameters**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | `str` | File id     |

### `client.files.get`

**`GET /api/v1/files/:id`**

Get file metadata

Get metadata for a reusable uploaded file.

**Path parameters**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | `str` | File id     |

**Response**

```python
// File
```

### `client.files.delete`

**`DELETE /api/v1/files/:id`**

Delete file

Delete a reusable uploaded file. Historical run and dataset snapshots are separate artifacts.

**Path parameters**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | `str` | File id     |

**Response**

```python
// DeleteFileResponse
```

### `client.files.upload`

**`POST /api/v1/files`**

Upload file

Upload a reusable file that can later be referenced by run inputs or dataset examples.

**Response**

```python
// File
```

## Runs

### `client.run`

**`POST /api/v1/runs`**

Start a run

Start a run. Send JSON or multipart/form-data.

**Query parameters**

| Name                  | Type  | Description                                                           |
| --------------------- | ----- | --------------------------------------------------------------------- |
| `version`             | `str` | (optional)Release or git ref. Defaults to latest.                     |
| `wait_for_completion` | `int` | (optional)Seconds to wait before returning (max 600). Omit for async. |

**Request body**

```python
// RunStartBody
```

**Response**

```python
// RunStartResponse
```

### `client.runs.list`

**`GET /api/v1/runs`**

List runs

List workflow and agent runs with cursor pagination.

**Query parameters**

| Name                  | Type  | Description |
| --------------------- | ----- | ----------- |
| `type`                | `str` | (optional)  |
| `source`              | `str` | (optional)  |
| `status`              | `str` | (optional)  |
| `trigger`             | `str` | (optional)  |
| `triggered_by`        | `str` | (optional)  |
| `source_ref`          | `str` | (optional)  |
| `batch_id`            | `str` | (optional)  |
| `example_id`          | `str` | (optional)  |
| `example_id_contains` | `str` | (optional)  |
| `from`                | `str` | (optional)  |
| `to`                  | `str` | (optional)  |
| `created_after`       | `str` | (optional)  |
| `created_before`      | `str` | (optional)  |
| `completed_after`     | `str` | (optional)  |
| `completed_before`    | `str` | (optional)  |
| `cursor`              | `str` | (optional)  |
| `offset`              | `int` | (optional)  |
| `limit`               | `int` | (optional)  |
| `ids`                 | `str` | (optional)  |

**Response**

```python
// RunsListResponse
```

### `client.runs.artifacts.download`

**`GET /api/v1/runs/:id/artifacts/:path`**

Download run artifact

Download one artifact by path.

**Path parameters**

| Name   | Type  | Description |
| ------ | ----- | ----------- |
| `id`   | `str` |             |
| `path` | `str` |             |

### `client.runs.artifacts.list`

**`GET /api/v1/runs/:id/artifacts`**

List run artifacts

List downloadable artifact paths for a run.

**Path parameters**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | `str` | Run id      |

**Response**

```python
// RunArtifactsResponse
```

### `client.runs.cancel`

**`POST /api/v1/runs/:id/cancel`**

Cancel run

Cancel a queued run or request cancellation of an in-flight run.

**Path parameters**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | `str` |             |

**Response**

```python
// RunCancelResponse
```

### `client.runs.events`

**`GET /api/v1/runs/:id/events`**

List run events

List a stable chronological lifecycle timeline for a run.

**Path parameters**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | `str` | Run id      |

**Response**

```python
// RunEventsResponse
```

### `client.runs.feedback.get`

**`GET /api/v1/runs/:id/feedback`**

Get run feedback

**Path parameters**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | `str` |             |

**Response**

```python
// RunFeedbackDetail
```

### `client.runs.feedback.update`

**`PUT /api/v1/runs/:id/feedback`**

Update run feedback

**Path parameters**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | `str` |             |

**Request body**

```python
// RunFeedbackRequest
```

**Response**

```python
// RunFeedbackDetail
```

### `client.runs.feedback.clear`

**`DELETE /api/v1/runs/:id/feedback`**

Clear run feedback

**Path parameters**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | `str` |             |

**Response**

```python
// RunFeedbackDetail
```

### `client.runs.promote`

**`POST /api/v1/runs/:id/promote`**

Promote a run to a dataset example

**Path parameters**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | `str` |             |

**Request body**

```python
// PromoteRunRequest
```

**Response**

```python
// PromoteRunResponse
```

### `client.rerun`

**`POST /api/v1/runs/:id/rerun`**

Rerun run

Start a new run from an existing run id.

**Path parameters**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | `str` |             |

**Query parameters**

| Name                  | Type  | Description                                                                            |
| --------------------- | ----- | -------------------------------------------------------------------------------------- |
| `version`             | `str` | (optional)Version for the new run. `original` pins the source run. Defaults to latest. |
| `wait_for_completion` | `int` | (optional)Seconds to wait before returning (max 600). Omit for async.                  |

**Response**

```python
// RunRerunResponse
```

### `client.runs.get`

**`GET /api/v1/runs/:id`**

Get run

Fetch one run by id. Use `expand` for input, usage, execution, and debug detail.

**Path parameters**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | `str` | Run id      |

**Query parameters**

| Name     | Type  | Description                                                                                                                           |
| -------- | ----- | ------------------------------------------------------------------------------------------------------------------------------------- |
| `expand` | `str` | (optional)Optional sections: `input`, `usage`, `execution`, `debug`. Terminal runs always include top-level output, files, and error. |

**Response**

```python
// Run
```

### `client.runs.steps`

**`GET /api/v1/runs/:id/steps`**

List run steps

List workflow steps or an agent-compatible execution step summary for a run.

**Path parameters**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | `str` | Run id      |

**Response**

```python
// RunStepsResponse
```

### `client.runs.trace.get`

**`GET /api/v1/runs/:id/trace`**

Get run trace

**Path parameters**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | `str` |             |

**Response**

```python
// dict[str, Any]
```

### `client.runs.usage`

**`GET /api/v1/runs/:id/usage`**

Get run usage

Get token, credit, duration, and execution usage for a run.

**Path parameters**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | `str` | Run id      |

**Response**

```python
// RunUsageResponse
```

## Errors

Every non-2xx response throws a typed exception:

| HTTP    | TypeScript                | Python                    |
| ------- | ------------------------- | ------------------------- |
| 400     | `EigenpalValidationError` | `EigenpalValidationError` |
| 401     | `EigenpalAuthError`       | `EigenpalAuthError`       |
| 403     | `EigenpalForbiddenError`  | `EigenpalForbiddenError`  |
| 404     | `EigenpalNotFoundError`   | `EigenpalNotFoundError`   |
| 429     | `EigenpalRateLimitError`  | `EigenpalRateLimitError`  |
| 5xx     | `EigenpalServerError`     | `EigenpalServerError`     |
| timeout | `EigenpalTimeoutError`    | `EigenpalTimeoutError`    |

The thrown exception carries `status`, `requestId`, `envelope` (raw `ApiErrorEnvelope`), and (for 429) `retryAfter`.
