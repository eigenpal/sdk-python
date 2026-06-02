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
│   ├── runs.list
│   ├── runs.get
│   ├── runs.cancel
│   ├── runs.rerun
│   ├── runs.get_feedback
│   ├── runs.update_feedback
│   ├── runs.clear_feedback
│   ├── runs.list_expected
│   ├── runs.copy_output_to_expected / upload_expected
│   ├── runs.download_expected
│   ├── runs.rename_expected
│   ├── runs.delete_expected
│   └── runs.download_file
├── workflows
│   ├── list
│   ├── get
│   ├── run
│   ├── versions
│   ├── executions.list
│   ├── executions.get
│   ├── executions.cancel
│   └── executions.run_and_wait
├── source
│   ├── decrypt_secrets
│   ├── lockfile
│   ├── raw
│   ├── releases
│   └── repository
└── automations
    └── sync
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

### `client.agents.list_files`

**`GET /api/v1/agents/{agentId}/files`**

List or download agent source files

Lists or reads files from the agent Git package (`agents/{slug}/` on organization source). Runtime artifacts (runs, dataset) are not served here.

**Path parameters**

| Name       | Type  | Description      |
| ---------- | ----- | ---------------- |
| `agent_id` | `str` | Agent id or slug |

**Query parameters**

| Name     | Type  | Description                      |
| -------- | ----- | -------------------------------- |
| `path`   | `str` | (optional)                       |
| `prefix` | `str` | (optional)                       |
| `ref`    | `str` | (optional)Git ref (default main) |

**Response**

```python
// Any
```

### `client.agents.put_file`

**`PUT /api/v1/agents/{agentId}/files`**

Upload one agent file (deprecated)

Agent source is Git-backed. Use Git push or the builder instead.

**Path parameters**

| Name       | Type  | Description      |
| ---------- | ----- | ---------------- |
| `agent_id` | `str` | Agent id or slug |

**Query parameters**

| Name     | Type  | Description                      |
| -------- | ----- | -------------------------------- |
| `path`   | `str` | (optional)                       |
| `prefix` | `str` | (optional)                       |
| `ref`    | `str` | (optional)Git ref (default main) |

**Request body**

```python
// dict[str, Any]
```

### `client.agents.upload_files`

**`POST /api/v1/agents/{agentId}/files`**

Upload agent files (deprecated)

Agent source is Git-backed. Use Git push or the builder instead.

**Path parameters**

| Name       | Type  | Description      |
| ---------- | ----- | ---------------- |
| `agent_id` | `str` | Agent id or slug |

**Request body**

```python
// dict[str, Any]
```

### `client.agents.get`

**`GET /api/v1/agents/{agentId}`**

Get an agent

Returns one agent by id or slug.

**Path parameters**

| Name       | Type  | Description      |
| ---------- | ----- | ---------------- |
| `agent_id` | `str` | Agent id or slug |

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

| Name       | Type  | Description      |
| ---------- | ----- | ---------------- |
| `agent_id` | `str` | Agent id or slug |

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

Run an agent

Enqueues an agent run. Returns 202 with `{ runId }` by default. Pass `wait_for_completion=<seconds>` to hold the connection until the run reaches a terminal state. File inputs are uploaded as multipart/form-data.

**Path parameters**

| Name       | Type  | Description      |
| ---------- | ----- | ---------------- |
| `agent_id` | `str` | Agent id or slug |

**Query parameters**

| Name                  | Type  | Description                                                                                                                                                                                |
| --------------------- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `wait_for_completion` | `int` | (optional)Seconds to hold the connection waiting for completion (max 600). Omit for async.                                                                                                 |
| `source_ref`          | `str` | (optional)Git source ref to resolve for this run. Defaults to latest. Supports latest, main, exact versions/tags such as 1.2.3, semver ranges such as 1.2.x or 1.x, and exact commit SHAs. |

**Request body**

```python
// RunAgentBody
```

**Response**

```python
// RunAgentResponse
```

### `client.agents.runs.list`

**`GET /api/v1/agents/{agentId}/runs`**

List agent runs

Returns runs for an agent, optionally filtered by status or experiment batch.

**Path parameters**

| Name       | Type  | Description      |
| ---------- | ----- | ---------------- |
| `agent_id` | `str` | Agent id or slug |

**Query parameters**

| Name                       | Type                                                         | Description                                                           |
| -------------------------- | ------------------------------------------------------------ | --------------------------------------------------------------------- |
| `status`                   | `str`                                                        | (optional)Run status filter                                           |
| `batch_id`                 | `str`                                                        | (optional)Experiment batch id filter                                  |
| `example_id`               | `str`                                                        | (optional)Exact dataset example id (folder name) filter               |
| `example_id_contains`      | `str`                                                        | (optional)Substring match on dataset example id                       |
| `created_after`            | `str`                                                        | (optional)Only runs created at/after this ISO timestamp               |
| `created_before`           | `str`                                                        | (optional)Only runs created at/before this ISO timestamp              |
| `completed_after`          | `str`                                                        | (optional)Only runs completed at/after this ISO timestamp             |
| `completed_before`         | `str`                                                        | (optional)Only runs completed at/before this ISO timestamp            |
| `source_ref`               | `str`                                                        | (optional)Filter by the source ref requested when the run was created |
| `feedback_status`          | `Literal["open", "resolved", "ignored"]`                     | (optional)                                                            |
| `feedback_rating`          | `Literal["pass", "fail", "partial", "none"]`                 | (optional)                                                            |
| `has_feedback`             | `bool`                                                       | (optional)                                                            |
| `no_feedback`              | `bool`                                                       | (optional)                                                            |
| `has_expected`             | `bool`                                                       | (optional)                                                            |
| `has_expected_json`        | `bool`                                                       | (optional)                                                            |
| `has_expected_files`       | `bool`                                                       | (optional)                                                            |
| `feedback_body_contains`   | `str`                                                        | (optional)                                                            |
| `feedback_created_after`   | `str`                                                        | (optional)                                                            |
| `feedback_created_before`  | `str`                                                        | (optional)                                                            |
| `feedback_updated_after`   | `str`                                                        | (optional)                                                            |
| `feedback_updated_before`  | `str`                                                        | (optional)                                                            |
| `feedback_resolved_after`  | `str`                                                        | (optional)                                                            |
| `feedback_resolved_before` | `str`                                                        | (optional)                                                            |
| `promoted_to_example`      | `bool`                                                       | (optional)                                                            |
| `promoted_example_name`    | `str`                                                        | (optional)                                                            |
| `since_last_resolved`      | `bool`                                                       | (optional)                                                            |
| `include`                  | `str`                                                        | (optional)Comma-separated extra parts: feedback, expected, files      |
| `sort`                     | `Literal["createdAt", "completedAt", "status", "exampleId"]` | (optional)                                                            |
| `order`                    | `Literal["asc", "desc"]`                                     | (optional)                                                            |
| `scan_limit`               | `int`                                                        | (optional)                                                            |
| `limit`                    | `int`                                                        | (optional)                                                            |
| `offset`                   | `int`                                                        | (optional)                                                            |

**Response**

```python
// ListAgentRunsResponse
```

### `client.agents.list`

**`GET /api/v1/agents`**

List agents

Returns agents the caller has access to, with pagination and basic execution stats. Accepts session cookies or API keys.

**Query parameters**

| Name               | Type   | Description                                    |
| ------------------ | ------ | ---------------------------------------------- |
| `search`           | `str`  | (optional)Substring match against agent fields |
| `slug`             | `str`  | (optional)Return a single agent by slug        |
| `limit`            | `int`  | (optional)                                     |
| `offset`           | `int`  | (optional)                                     |
| `include_archived` | `bool` | (optional)                                     |

**Response**

```python
// ListAgentsResponse
```

### `client.agents.create`

**`POST /api/v1/agents`**

Create an agent

Creates a new agent, registers it in the automation table, and scaffolds its Git source package. Accepts session cookies or API keys.

**Request body**

```python
// CreateAgentBody
```

**Response**

```python
// CreateAgentResponse
```

### `client.agents.runs.cancel`

**`POST /api/v1/agents/runs/{runId}/cancel`**

Cancel agent run

Requests cancellation for one agent run by id.

**Path parameters**

| Name     | Type  | Description |
| -------- | ----- | ----------- |
| `run_id` | `str` | Run id      |

**Response**

```python
// CancelAgentExecutionResponse
```

### `client.agents.runs.download_expected`

**`GET /api/v1/agents/runs/{runId}/expected/{filename}`**

Download an expected file

Downloads one expected file attached to an agent run.

**Path parameters**

| Name       | Type  | Description            |
| ---------- | ----- | ---------------------- |
| `run_id`   | `str` | Run id                 |
| `filename` | `str` | Expected artifact path |

### `client.agents.runs.rename_expected`

**`PATCH /api/v1/agents/runs/{runId}/expected/{filename}`**

Rename an expected file

Renames one expected file attached to an agent run.

**Path parameters**

| Name       | Type  | Description            |
| ---------- | ----- | ---------------------- |
| `run_id`   | `str` | Run id                 |
| `filename` | `str` | Expected artifact path |

**Request body**

```python
// RenameExpectedFileBody
```

**Response**

```python
// RenameExpectedFileResponse
```

### `client.agents.runs.delete_expected`

**`DELETE /api/v1/agents/runs/{runId}/expected/{filename}`**

Delete an expected file

Deletes one expected file attached to an agent run.

**Path parameters**

| Name       | Type  | Description            |
| ---------- | ----- | ---------------------- |
| `run_id`   | `str` | Run id                 |
| `filename` | `str` | Expected artifact path |

### `client.agents.runs.list_expected`

**`GET /api/v1/agents/runs/{runId}/expected`**

List run expected artifacts

Returns structured expected JSON and expected file names for one run.

**Path parameters**

| Name     | Type  | Description |
| -------- | ----- | ----------- |
| `run_id` | `str` | Run id      |

**Response**

```python
// AgentExecutionExpectedArtifacts
```

### `client.agents.runs.copy_output_to_expected / upload_expected`

**`POST /api/v1/agents/runs/{runId}/expected`**

Create an expected file

Uploads an expected file with multipart/form-data, or copies a generated output file into expected artifacts with JSON.

**Path parameters**

| Name     | Type  | Description |
| -------- | ----- | ----------- |
| `run_id` | `str` | Run id      |

**Request body**

```python
// CopyAgentExecutionOutputToExpectedBody
```

**Response**

```python
// dict[str, Any]
```

### `client.agents.runs.get_feedback`

**`GET /api/v1/agents/runs/{runId}/feedback`**

Get run feedback

Returns feedback and expected artifacts attached to one agent run.

**Path parameters**

| Name     | Type  | Description |
| -------- | ----- | ----------- |
| `run_id` | `str` | Run id      |

**Response**

```python
// AgentExecutionFeedbackDetail
```

### `client.agents.runs.update_feedback`

**`PATCH /api/v1/agents/runs/{runId}/feedback`**

Update run feedback

Updates the feedback body, rating, status, or structured expected JSON attached to one run.

**Path parameters**

| Name     | Type  | Description |
| -------- | ----- | ----------- |
| `run_id` | `str` | Run id      |

**Request body**

```python
// UpdateAgentExecutionFeedbackBody
```

**Response**

```python
// AgentExecutionFeedbackDetail
```

### `client.agents.runs.clear_feedback`

**`DELETE /api/v1/agents/runs/{runId}/feedback`**

Clear run feedback

Deletes feedback, structured expected JSON, and expected files from one run.

**Path parameters**

| Name     | Type  | Description |
| -------- | ----- | ----------- |
| `run_id` | `str` | Run id      |

**Response**

```python
// AgentExecutionFeedbackDetail
```

### `client.agents.runs.download_file`

**`GET /api/v1/agents/runs/{runId}/files/{kind}/{filename}`**

Download a run file

Downloads an input file, output file, issues.md, trace.jsonl, or eigenpal.lock attached to an agent run.

**Path parameters**

| Name       | Type                                                        | Description |
| ---------- | ----------------------------------------------------------- | ----------- |
| `run_id`   | `str`                                                       |             |
| `kind`     | `Literal["input", "output", "issues", "trace", "lockfile"]` |             |
| `filename` | `str`                                                       |             |

### `client.agents.runs.rerun`

**`POST /api/v1/agents/runs/{runId}/rerun`**

Rerun agent run

Creates a new run for the same agent using a previous run's stored input snapshot.

**Path parameters**

| Name     | Type  | Description   |
| -------- | ----- | ------------- |
| `run_id` | `str` | Source run id |

**Response**

```python
// RerunAgentRunResponse
```

### `client.agents.runs.get`

**`GET /api/v1/agents/runs/{runId}`**

Get agent run

Returns one agent run by id.

**Path parameters**

| Name     | Type  | Description |
| -------- | ----- | ----------- |
| `run_id` | `str` | Run id      |

**Query parameters**

| Name      | Type  | Description                                                               |
| --------- | ----- | ------------------------------------------------------------------------- |
| `include` | `str` | (optional)Comma-separated optional sections, e.g. feedback,expected,files |

**Response**

```python
// AgentRunResponse
```

## Automations

### `client.automations.sync`

**`POST /api/v1/automations/{automation}/sync`**

Sync an automation from latest source

Reconciles lightweight automation metadata from the latest released Git source package. This does not enqueue executions.

**Path parameters**

| Name         | Type  | Description |
| ------------ | ----- | ----------- |
| `automation` | `str` |             |

**Response**

```python
// AutomationSyncResponse
```

## Source

### `client.source.lockfile`

**`GET /api/v1/source/lockfile`**

Preview a source lockfile

Resolves a package ref and returns the would-be eigenpal.lock without enqueueing or writing runtime artifacts.

**Query parameters**

| Name          | Type  | Description |
| ------------- | ----- | ----------- |
| `package_ref` | `str` |             |

**Response**

```python
// SourceLockfileResponse
```

### `client.source.raw`

**`GET /api/v1/source/raw`**

Preview a raw Git source file

Reads a raw file from the organization Git repository for metadata previews.

**Query parameters**

| Name   | Type  | Description |
| ------ | ----- | ----------- |
| `ref`  | `str` | (optional)  |
| `path` | `str` |             |

**Response**

```python
// RawSourceResponse
```

### `client.source.releases`

**`GET /api/v1/source/releases`**

List Git source package releases

Lists package-scoped Git release tags, or returns one exact version when requested.

**Query parameters**

| Name           | Type  | Description |
| -------------- | ----- | ----------- |
| `package_path` | `str` |             |
| `version`      | `str` | (optional)  |

**Response**

```python
// SourceReleasesResponse
```

### `client.source.repository`

**`GET /api/v1/source/repository`**

Get organization Git source repository

Returns the authenticated organization Git remote used by hidden source CLI commands.

**Response**

```python
// SourceRepositoryResponse
```

### `client.source.decrypt_secrets`

**`POST /api/v1/source/secrets/decrypt`**

Decrypt a Git-backed source secret

Decrypts one or more encrypted source secret values for the authenticated tenant. Single-secret requests require an execution id and are checked against that execution lockfile graph; batch `secrets[]` requests are tenant-scoped for local CLI use.

**Request body**

```python
// SourceSecretsDecryptBody
```

**Response**

```python
// SourceSecretsDecryptResponse
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

| Name         | Type  | Description                                                                                              |
| ------------ | ----- | -------------------------------------------------------------------------------------------------------- |
| `status`     | `str` | (optional)Comma-separated list of execution statuses to filter by                                        |
| `from_date`  | `str` | (optional)ISO-8601 timestamp or relative expression (e.g. "now()-7d") for the lower bound on `createdAt` |
| `to_date`    | `str` | (optional)Upper bound on `createdAt`                                                                     |
| `example_id` | `str` | (optional)Filter to executions launched from a specific eval example                                     |
| `limit`      | `int` | (optional)                                                                                               |
| `offset`     | `int` | (optional)                                                                                               |

**Response**

```python
// ListWorkflowExecutionsResponse
```

### `client.workflows.get`

**`GET /api/v1/workflows/{id}`**

Get a workflow by id

Returns the workflow summary plus the current version YAML. Use `versions list` for historical YAML.

**Path parameters**

| Name | Type  | Description                  |
| ---- | ----- | ---------------------------- |
| `id` | `str` | Workflow id (e.g. wf_abc123) |

**Response**

```python
// WorkflowDetail
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

| Name           | Type  | Description            |
| -------------- | ----- | ---------------------- |
| `execution_id` | `str` | Execution id to cancel |

**Response**

```python
// CancelWorkflowExecutionResponse
```

### `client.workflows.executions.get`

**`GET /api/v1/workflows/executions/{executionId}`**

Get workflow execution status

Returns the current status, completion timestamps, and result or error for a workflow execution. Pass `includeSteps=true` for the per-step artifact payload.

**Path parameters**

| Name           | Type  | Description                  |
| -------------- | ----- | ---------------------------- |
| `execution_id` | `str` | Execution id (e.g. exec_xyz) |

**Query parameters**

| Name            | Type                       | Description                                                                               |
| --------------- | -------------------------- | ----------------------------------------------------------------------------------------- |
| `include_steps` | `Literal["true", "false"]` | (optional)When "true", returns the full per-step execution payload instead of the summary |

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
