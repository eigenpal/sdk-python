# eigenpal reference

## Quick example

```python
import os
from pathlib import Path
from eigenpal import Eigenpal

client = Eigenpal(api_key=os.environ["EIGENPAL_API_KEY"])

# Run a workflow with a file input (multipart upload, no base64).
result = client.executions.run_and_wait(
    "extract-invoice",
    input={"contract": Path("contract.pdf")},
)
print(result["status"], result["result"])
```

## Surface

```
client
├── executions
│   ├── cancel
│   ├── get
│   ├── list
│   └── runAndWait
└── workflows
    ├── get
    ├── run
    ├── versions
    └── list
```

## Client construction

```python
import os
from eigenpal import Eigenpal

client = Eigenpal(
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
| `verify_ssl`      | `bool`  | `True`                                           | Disable for self-signed dev hosts.                |

## Executions

### `client.executions.cancel`

**`POST /v1/executions/{executionId}/cancel`**

Cancel an execution

Idempotent. For executions not yet picked up by a worker (status=created/pending), transitions immediately to `cancelled`. For running/waiting executions, stamps `cancelRequestedAt` so the worker observes cancellation between step transitions. Terminal executions are a no-op.

**Path parameters**

| Name          | Type  | Description            |
| ------------- | ----- | ---------------------- |
| `executionId` | `str` | Execution id to cancel |

**Response**

```python
// CancelExecutionResponse
```

### `client.executions.get`

**`GET /v1/executions/{executionId}`**

Get execution status

Returns the current status, completion timestamps, and (when terminal) the result or error for a single execution. Pass `includeSteps=true` for the per-step artifact payload (heavier; intended for debugging).

**Path parameters**

| Name          | Type  | Description                  |
| ------------- | ----- | ---------------------------- |
| `executionId` | `str` | Execution id (e.g. exec_xyz) |

**Query parameters**

| Name           | Type                       | Description                                                                               |
| -------------- | -------------------------- | ----------------------------------------------------------------------------------------- |
| `includeSteps` | `Literal["true", "false"]` | (optional)When "true", returns the full per-step execution payload instead of the summary |

**Response**

```python
// Union[ExecutionStatusResponse, ExecutionSummary]
```

### `client.executions.list`

**`GET /v1/executions`**

List executions

Returns executions across the tenant, optionally filtered by workflow, status, date range, or eval example. Paginated.

**Query parameters**

| Name         | Type  | Description                                                                                              |
| ------------ | ----- | -------------------------------------------------------------------------------------------------------- |
| `workflowId` | `str` | (optional)Comma-separated list of workflow ids to filter by                                              |
| `status`     | `str` | (optional)Comma-separated list of execution statuses to filter by                                        |
| `fromDate`   | `str` | (optional)ISO-8601 timestamp or relative expression (e.g. "now()-7d") for the lower bound on `createdAt` |
| `toDate`     | `str` | (optional)Upper bound on `createdAt`                                                                     |
| `exampleId`  | `str` | (optional)Filter to executions launched from a specific eval example                                     |
| `limit`      | `int` | (optional)                                                                                               |
| `offset`     | `int` | (optional)                                                                                               |

**Response**

```python
// ListExecutionsResponse
```

## Workflows

### `client.workflows.get`

**`GET /v1/workflows/{id}`**

Get a workflow by id

Returns the workflow with its current version (definition + YAML content).

**Path parameters**

| Name | Type  | Description                  |
| ---- | ----- | ---------------------------- |
| `id` | `str` | Workflow id (e.g. wf_abc123) |

**Response**

```python
// WorkflowSummary
```

### `client.workflows.run`

**`POST /v1/workflows/{id}/run`**

Execute a workflow (async or sync)

Enqueues a workflow execution. Returns 201 with `{ executionId }` by default. Pass `wait_for_completion=<seconds>` (max 60) to hold the connection until the run reaches a terminal state; the body then also includes `status`, `result`, and `error`. File inputs are uploaded as `multipart/form-data` (each file as a top-level form field; `_json` field carries scalar inputs).

**Path parameters**

| Name | Type  | Description                                                                           |
| ---- | ----- | ------------------------------------------------------------------------------------- |
| `id` | `str` | Workflow id (e.g. `wf_abc123`) or slug (e.g. `extract-invoice`, the workflow `name`). |

**Query parameters**

| Name                  | Type  | Description                                                                               |
| --------------------- | ----- | ----------------------------------------------------------------------------------------- |
| `version`             | `str` | (optional)Version id, or "latest" (default)                                               |
| `wait_for_completion` | `int` | (optional)Seconds to hold the connection waiting for completion (max 60). Omit for async. |

**Request body**

```python
// RunWorkflowBody
```

**Response**

```python
// RunWorkflowResponse
```

### `client.workflows.versions`

**`GET /v1/workflows/{id}/versions`**

List tagged versions for a workflow

Returns released versions in reverse-chronological order, paginated.

**Path parameters**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | `str` | Workflow id |

**Query parameters**

| Name     | Type  | Description                               |
| -------- | ----- | ----------------------------------------- |
| `limit`  | `int` | (optional)Page size (max 100, default 50) |
| `offset` | `int` | (optional)Page offset                     |

**Response**

```python
// ListVersionsResponse
```

### `client.workflows.list`

**`GET /v1/workflows`**

List workflows

Returns workflows the API key has access to, with pagination. Use `name` for exact-match slug lookup, `search` for substring match.

**Query parameters**

| Name     | Type                           | Description                                          |
| -------- | ------------------------------ | ---------------------------------------------------- |
| `search` | `str`                          | (optional)Substring match against workflow name      |
| `name`   | `str`                          | (optional)Exact-match lookup by workflow name (slug) |
| `kind`   | `Literal["workflow", "block"]` | (optional)Filter by workflow kind                    |
| `limit`  | `int`                          | (optional)Page size (max 100, default 50)            |
| `offset` | `int`                          | (optional)Page offset                                |

**Response**

```python
// ListWorkflowsResponse
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
