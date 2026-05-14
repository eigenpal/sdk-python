# eigenpal reference

## Quick example

```python
import os
from pathlib import Path
from eigenpal import EigenpalClient

client = EigenpalClient(api_key=os.environ["EIGENPAL_API_KEY"])

# Run a workflow with a file input (multipart upload, no base64).
result = client.workflows.executions.run_and_wait(
    "extract-invoice",
    input={"contract": Path("contract.pdf")},
)
print(result["status"], result["result"])
```

## Surface

```
client
├── agents
│   ├── list
│   ├── get
│   ├── create
│   ├── update
│   ├── run
│   ├── list_files
│   ├── put_file
│   ├── upload_files
│   ├── executions.list
│   ├── executions.get
│   ├── executions.cancel
│   ├── executions.rerun
│   ├── executions.get_feedback
│   ├── executions.update_feedback
│   ├── executions.clear_feedback
│   ├── executions.list_expected
│   ├── executions.copy_output_to_expected / upload_expected
│   ├── executions.download_expected
│   ├── executions.rename_expected
│   ├── executions.delete_expected
│   └── executions.download_file
└── workflows
    ├── list
    ├── get
    ├── run
    ├── versions
    ├── executions.list
    ├── executions.get
    ├── executions.cancel
    └── executions.run_and_wait
```

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
| `verify_ssl`      | `bool`  | `True`                                           | Disable for self-signed dev hosts.                |

## Agents

### `client.agents.executions.list`

**`GET /api/v1/agents/{agentId}/executions`**

List agent executions

Returns executions for an agent, optionally filtered by status or experiment batch.

**Path parameters**

| Name      | Type  | Description      |
| --------- | ----- | ---------------- |
| `agentId` | `str` | Agent id or slug |

**Query parameters**

| Name                     | Type                                                           | Description                                                      |
| ------------------------ | -------------------------------------------------------------- | ---------------------------------------------------------------- |
| `status`                 | `str`                                                          | (optional)Execution status filter                                |
| `batchId`                | `str`                                                          | (optional)Experiment batch id filter                             |
| `exampleName`            | `str`                                                          | (optional)Exact dataset example name filter                      |
| `exampleNameContains`    | `str`                                                          | (optional)Substring match on example name                        |
| `createdAfter`           | `str`                                                          | (optional)Only executions created at/after this ISO timestamp    |
| `createdBefore`          | `str`                                                          | (optional)Only executions created at/before this ISO timestamp   |
| `completedAfter`         | `str`                                                          | (optional)Only executions completed at/after this ISO timestamp  |
| `completedBefore`        | `str`                                                          | (optional)Only executions completed at/before this ISO timestamp |
| `feedbackStatus`         | `Literal["open", "resolved", "ignored"]`                       | (optional)                                                       |
| `feedbackRating`         | `Literal["pass", "fail", "partial", "none"]`                   | (optional)                                                       |
| `hasFeedback`            | `bool`                                                         | (optional)                                                       |
| `noFeedback`             | `bool`                                                         | (optional)                                                       |
| `hasExpected`            | `bool`                                                         | (optional)                                                       |
| `hasExpectedJson`        | `bool`                                                         | (optional)                                                       |
| `hasExpectedFiles`       | `bool`                                                         | (optional)                                                       |
| `feedbackBodyContains`   | `str`                                                          | (optional)                                                       |
| `feedbackCreatedAfter`   | `str`                                                          | (optional)                                                       |
| `feedbackCreatedBefore`  | `str`                                                          | (optional)                                                       |
| `feedbackUpdatedAfter`   | `str`                                                          | (optional)                                                       |
| `feedbackUpdatedBefore`  | `str`                                                          | (optional)                                                       |
| `feedbackResolvedAfter`  | `str`                                                          | (optional)                                                       |
| `feedbackResolvedBefore` | `str`                                                          | (optional)                                                       |
| `promotedToExample`      | `bool`                                                         | (optional)                                                       |
| `promotedExampleName`    | `str`                                                          | (optional)                                                       |
| `sinceLastResolved`      | `bool`                                                         | (optional)                                                       |
| `include`                | `str`                                                          | (optional)Comma-separated extra parts: feedback, expected, files |
| `sort`                   | `Literal["createdAt", "completedAt", "status", "exampleName"]` | (optional)                                                       |
| `order`                  | `Literal["asc", "desc"]`                                       | (optional)                                                       |
| `scanLimit`              | `int`                                                          | (optional)                                                       |
| `limit`                  | `int`                                                          | (optional)                                                       |
| `offset`                 | `int`                                                          | (optional)                                                       |

**Response**

```python
// ListAgentExecutionsResponse
```

### `client.agents.list_files`

**`GET /api/v1/agents/{agentId}/files`**

List or download agent files

Lists live agent files, or returns one file when `path` is provided.

**Path parameters**

| Name      | Type  | Description      |
| --------- | ----- | ---------------- |
| `agentId` | `str` | Agent id or slug |

**Query parameters**

| Name     | Type  | Description |
| -------- | ----- | ----------- |
| `path`   | `str` | (optional)  |
| `prefix` | `str` | (optional)  |

**Response**

```python
// Any
```

### `client.agents.put_file`

**`PUT /api/v1/agents/{agentId}/files`**

Upload one agent file

Uploads one file into the live agent namespace at the safe relative `path` query parameter.

**Path parameters**

| Name      | Type  | Description      |
| --------- | ----- | ---------------- |
| `agentId` | `str` | Agent id or slug |

**Query parameters**

| Name     | Type  | Description |
| -------- | ----- | ----------- |
| `path`   | `str` | (optional)  |
| `prefix` | `str` | (optional)  |

**Request body**

```python
// AgentFileBody
```

**Response**

```python
// dict[str, Any]
```

### `client.agents.upload_files`

**`POST /api/v1/agents/{agentId}/files`**

Upload agent files

Uploads multiple files into the live agent namespace.

**Path parameters**

| Name      | Type  | Description      |
| --------- | ----- | ---------------- |
| `agentId` | `str` | Agent id or slug |

**Request body**

```python
// AgentFilesBody
```

**Response**

```python
// dict[str, Any]
```

### `client.agents.get`

**`GET /api/v1/agents/{agentId}`**

Get an agent

Returns one agent by id or slug.

**Path parameters**

| Name      | Type  | Description      |
| --------- | ----- | ---------------- |
| `agentId` | `str` | Agent id or slug |

**Query parameters**

| Name      | Type  | Description                                                     |
| --------- | ----- | --------------------------------------------------------------- |
| `include` | `str` | (optional)Comma-separated optional sections, e.g. files,dataset |

**Response**

```python
// GetAgentResponse
```

### `client.agents.update`

**`PATCH /api/v1/agents/{agentId}`**

Update an agent

Updates mutable agent metadata and configuration.

**Path parameters**

| Name      | Type  | Description      |
| --------- | ----- | ---------------- |
| `agentId` | `str` | Agent id or slug |

**Request body**

```python
// PatchAgentBody
```

**Response**

```python
// PatchAgentResponse
```

### `client.agents.run`

**`POST /api/v1/agents/{agentId}/run`**

Execute an agent

Enqueues an agent execution. Returns 202 with `{ executionId }` by default. Pass `wait_for_completion=<seconds>` to hold the connection until the execution reaches a terminal state. File inputs are uploaded as multipart/form-data.

**Path parameters**

| Name      | Type  | Description      |
| --------- | ----- | ---------------- |
| `agentId` | `str` | Agent id or slug |

**Query parameters**

| Name                  | Type  | Description                                                                                |
| --------------------- | ----- | ------------------------------------------------------------------------------------------ |
| `wait_for_completion` | `int` | (optional)Seconds to hold the connection waiting for completion (max 600). Omit for async. |

**Request body**

```python
// RunAgentBody
```

**Response**

```python
// RunAgentResponse
```

### `client.agents.executions.cancel`

**`POST /api/v1/agents/executions/{executionId}/cancel`**

Cancel agent execution

Requests cancellation for one agent execution by id.

**Path parameters**

| Name          | Type  | Description  |
| ------------- | ----- | ------------ |
| `executionId` | `str` | Execution id |

**Response**

```python
// CancelAgentExecutionResponse
```

### `client.agents.executions.download_expected`

**`GET /api/v1/agents/executions/{executionId}/expected/{filename}`**

Download an expected file

Downloads one expected file attached to an agent execution.

**Path parameters**

| Name          | Type  | Description            |
| ------------- | ----- | ---------------------- |
| `executionId` | `str` | Execution id           |
| `filename`    | `str` | Expected artifact path |

### `client.agents.executions.rename_expected`

**`PATCH /api/v1/agents/executions/{executionId}/expected/{filename}`**

Rename an expected file

Renames one expected file attached to an agent execution.

**Path parameters**

| Name          | Type  | Description            |
| ------------- | ----- | ---------------------- |
| `executionId` | `str` | Execution id           |
| `filename`    | `str` | Expected artifact path |

**Request body**

```python
// RenameExpectedFileBody
```

**Response**

```python
// RenameExpectedFileResponse
```

### `client.agents.executions.delete_expected`

**`DELETE /api/v1/agents/executions/{executionId}/expected/{filename}`**

Delete an expected file

Deletes one expected file attached to an agent execution.

**Path parameters**

| Name          | Type  | Description            |
| ------------- | ----- | ---------------------- |
| `executionId` | `str` | Execution id           |
| `filename`    | `str` | Expected artifact path |

### `client.agents.executions.list_expected`

**`GET /api/v1/agents/executions/{executionId}/expected`**

List execution expected artifacts

Returns structured expected JSON and expected file names for one execution.

**Path parameters**

| Name          | Type  | Description  |
| ------------- | ----- | ------------ |
| `executionId` | `str` | Execution id |

**Response**

```python
// AgentExecutionExpectedArtifacts
```

### `client.agents.executions.copy_output_to_expected / upload_expected`

**`POST /api/v1/agents/executions/{executionId}/expected`**

Create an expected file

Uploads an expected file with multipart/form-data, or copies a generated output file into expected artifacts with JSON.

**Path parameters**

| Name          | Type  | Description  |
| ------------- | ----- | ------------ |
| `executionId` | `str` | Execution id |

**Request body**

```python
// CopyAgentExecutionOutputToExpectedBody
```

**Response**

```python
// dict[str, Any]
```

### `client.agents.executions.get_feedback`

**`GET /api/v1/agents/executions/{executionId}/feedback`**

Get execution feedback

Returns feedback and expected artifacts attached to one agent execution.

**Path parameters**

| Name          | Type  | Description  |
| ------------- | ----- | ------------ |
| `executionId` | `str` | Execution id |

**Response**

```python
// AgentExecutionFeedbackDetail
```

### `client.agents.executions.update_feedback`

**`PATCH /api/v1/agents/executions/{executionId}/feedback`**

Update execution feedback

Updates the feedback body, rating, status, or structured expected JSON attached to one execution.

**Path parameters**

| Name          | Type  | Description  |
| ------------- | ----- | ------------ |
| `executionId` | `str` | Execution id |

**Request body**

```python
// UpdateAgentExecutionFeedbackBody
```

**Response**

```python
// AgentExecutionFeedbackDetail
```

### `client.agents.executions.clear_feedback`

**`DELETE /api/v1/agents/executions/{executionId}/feedback`**

Clear execution feedback

Deletes feedback, structured expected JSON, and expected files from one execution.

**Path parameters**

| Name          | Type  | Description  |
| ------------- | ----- | ------------ |
| `executionId` | `str` | Execution id |

**Response**

```python
// AgentExecutionFeedbackDetail
```

### `client.agents.executions.download_file`

**`GET /api/v1/agents/executions/{executionId}/files/{kind}/{filename}`**

Download an execution file

Downloads an input file, output file, issues.md, or trace.jsonl attached to an agent execution.

**Path parameters**

| Name          | Type                                            | Description |
| ------------- | ----------------------------------------------- | ----------- |
| `executionId` | `str`                                           |             |
| `kind`        | `Literal["input", "output", "issues", "trace"]` |             |
| `filename`    | `str`                                           |             |

### `client.agents.executions.rerun`

**`POST /api/v1/agents/executions/{executionId}/rerun`**

Rerun agent execution

Creates a new execution for the same agent using a previous execution's stored input snapshot.

**Path parameters**

| Name          | Type  | Description         |
| ------------- | ----- | ------------------- |
| `executionId` | `str` | Source execution id |

**Response**

```python
// RerunAgentExecutionResponse
```

### `client.agents.executions.get`

**`GET /api/v1/agents/executions/{executionId}`**

Get agent execution

Returns one agent execution by id.

**Path parameters**

| Name          | Type  | Description  |
| ------------- | ----- | ------------ |
| `executionId` | `str` | Execution id |

**Query parameters**

| Name      | Type  | Description                                                               |
| --------- | ----- | ------------------------------------------------------------------------- |
| `include` | `str` | (optional)Comma-separated optional sections, e.g. feedback,expected,files |

**Response**

```python
// AgentExecutionResponse
```

### `client.agents.list`

**`GET /api/v1/agents`**

List agents

Returns agents the API key has access to, with pagination and basic execution stats.

**Query parameters**

| Name     | Type  | Description                                    |
| -------- | ----- | ---------------------------------------------- |
| `search` | `str` | (optional)Substring match against agent fields |
| `limit`  | `int` | (optional)                                     |
| `offset` | `int` | (optional)                                     |

**Response**

```python
// ListAgentsResponse
```

### `client.agents.create`

**`POST /api/v1/agents`**

Create an agent

Creates a new agent and initializes its workspace files.

**Request body**

```python
// CreateAgentBody
```

**Response**

```python
// CreateAgentResponse
```

## Workflows

### `client.workflows.executions.list`

**`GET /api/v1/workflows/{id}/executions`**

List workflow executions

Returns executions for a workflow, optionally filtered by status, date range, or eval example. Paginated.

**Path parameters**

| Name | Type  | Description                  |
| ---- | ----- | ---------------------------- |
| `id` | `str` | Workflow id (e.g. wf_abc123) |

**Query parameters**

| Name        | Type  | Description                                                                                              |
| ----------- | ----- | -------------------------------------------------------------------------------------------------------- |
| `status`    | `str` | (optional)Comma-separated list of execution statuses to filter by                                        |
| `fromDate`  | `str` | (optional)ISO-8601 timestamp or relative expression (e.g. "now()-7d") for the lower bound on `createdAt` |
| `toDate`    | `str` | (optional)Upper bound on `createdAt`                                                                     |
| `exampleId` | `str` | (optional)Filter to executions launched from a specific eval example                                     |
| `limit`     | `int` | (optional)                                                                                               |
| `offset`    | `int` | (optional)                                                                                               |

**Response**

```python
// ListWorkflowExecutionsResponse
```

### `client.workflows.get`

**`GET /api/v1/workflows/{id}`**

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

**`POST /api/v1/workflows/{id}/run`**

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

**`GET /api/v1/workflows/{id}/versions`**

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

### `client.workflows.executions.cancel`

**`POST /api/v1/workflows/executions/{executionId}/cancel`**

Cancel a workflow execution

Idempotent. Created/pending executions transition immediately to `cancelled`; running/waiting executions receive a cancellation request for the worker to observe.

**Path parameters**

| Name          | Type  | Description            |
| ------------- | ----- | ---------------------- |
| `executionId` | `str` | Execution id to cancel |

**Response**

```python
// CancelWorkflowExecutionResponse
```

### `client.workflows.executions.get`

**`GET /api/v1/workflows/executions/{executionId}`**

Get workflow execution status

Returns the current status, completion timestamps, and result or error for a workflow execution. Pass `includeSteps=true` for the per-step artifact payload.

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
// Union[WorkflowExecutionStatusResponse, ExecutionSummary]
```

### `client.workflows.list`

**`GET /api/v1/workflows`**

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
