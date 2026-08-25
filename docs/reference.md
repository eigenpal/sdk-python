# eigenpal reference

## Quick example

```python
import os
from pathlib import Path
from eigenpal import EigenpalClient

client = EigenpalClient(api_key=os.environ["EIGENPAL_API_KEY"])

# Small files use multipart; larger files are pre-uploaded automatically.
result = client.run_and_wait(
    "workflows.extract-invoice",
    input={"contract": Path("contract.pdf")},
)
print(result["finished"], result["output"])
```

Set `multipart_max_bytes=None` or `EIGENPAL_MULTIPART_MAX_BYTES=none` to keep every run file on multipart for a self-hosted deployment.

## Surface

```
client
├── run
├── rerun
├── automations
│   ├── list
│   ├── get
│   ├── versions
│   ├── sync
│   ├── create_version
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
│   │   ├── expected_file
│   │   │   ├── get
│   │   │   ├── delete
│   │   │   └── update
│   │   ├── expected_files
│   │   │   ├── list
│   │   │   └── create
│   │   ├── input_file
│   │   │   ├── get
│   │   │   ├── delete
│   │   │   └── update
│   │   ├── input_files
│   │   │   ├── list
│   │   │   └── create
│   │   ├── run
│   │   └── update
│   ├── experiments
│   │   ├── list
│   │   ├── get
│   │   ├── cancel
│   │   ├── create
│   │   ├── create_stream
│   │   ├── export
│   │   └── export_all
│   ├── promote_version
│   ├── restore_version
│   ├── reviews
│   │   └── health
│   └── triggers
├── runs
│   ├── list
│   ├── get
│   ├── artifacts
│   │   ├── list
│   │   └── download
│   ├── cancel
│   ├── events
│   ├── promote
│   ├── reviews
│   │   ├── get
│   │   ├── list_expected
│   │   ├── copy_output_to_expected / upload_expected
│   │   ├── download_expected
│   │   ├── rename_expected
│   │   ├── delete_expected
│   │   ├── clear
│   │   └── update
│   ├── scores
│   │   └── list
│   ├── steps
│   ├── trace
│   │   └── get
│   └── usage
├── files
│   ├── get
│   ├── abort_upload
│   ├── complete_upload
│   ├── create_upload
│   ├── delete
│   ├── download
│   └── upload
├── auth
│   └── check
└── experiments
    └── resolve
```

Start runs with `client.run(...)` and create a new run from a previous snapshot with `client.rerun(...)`.

Run inspection, artifacts, traces, usage, events, and reviews live under `client.runs.*`, which maps to `/api/v1/runs`.

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

| Option                | Type          | Default                                                               | Description                                                                                    |
| --------------------- | ------------- | --------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `api_key`             | `str`         | `os.environ["EIGENPAL_API_KEY"]`                                      | Bearer key from the dashboard.                                                                 |
| `base_url`            | `str`         | `os.environ.get("EIGENPAL_BASE_URL")` ?? `'https://api.eigenpal.com'` | API host. Set to your deployment for self-hosted.                                              |
| `timeout_seconds`     | `float`       | `60.0`                                                                | Per-request timeout.                                                                           |
| `multipart_max_bytes` | `int \| None` | `EIGENPAL_MULTIPART_MAX_BYTES` ?? 4.5 MiB                             | Pre-upload run files above the aggregate multipart limit. `None` keeps all files on multipart. |

## Metadata

### `client.auth.check`

**`GET /v1/auth/check`**

Check API key identity

Return the tenant, user, API key, and scope represented by the current API key.

**Response**

```python
// AuthCheckResponse
```

## Automations

### `client.automations.list`

**`GET /v1/automations`**

List automations

Returns workflows and agents through one runnable automation collection. Use `type` to narrow to workflows or agents, and `search` to find automations by slug, name, or description.

**Query parameters**

| Name     | Type                           | Description                                                  |
| -------- | ------------------------------ | ------------------------------------------------------------ |
| `search` | `str`                          | (optional)Substring match against slug, name, or description |
| `type`   | `Literal["workflow", "agent"]` | (optional)Filter by implementation type                      |
| `limit`  | `int`                          | (optional)Maximum number of automations to return.           |
| `offset` | `int`                          | (optional)Zero-based offset for paging through automations.  |

**Response**

```python
// ListAutomationsResponse
```

### `client.automations.get`

**`GET /v1/automations/:id`**

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

### `client.automations.sync`

**`POST /v1/automations/:id/sync`**

Sync automation from latest Git release

Reconciles automation registry metadata and trigger projections from the latest Git source release. This operation is idempotent for unchanged source state: repeated calls against the same latest release leave the same automation registry state and may repeat the same warnings. Requires a Bearer API token for the organization and a user-backed API key. It does not publish source; it reads the already-published latest release manifest. Versioned targets are rejected with 400, missing organization/source/release/manifest state returns 404, invalid manifests return 400, and provider or persistence failures return 5xx.

**Path parameters**

| Name | Type  | Description                                                                                                                                      |
| ---- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `id` | `str` | Automation target to sync, such as agents.invoice-agent or workflows.extract. Do not include a version; sync always uses the latest Git release. |

**Response**

```python
// dict[str, Any]
```

### `client.automations.triggers`

**`GET /v1/automations/:id/triggers`**

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

**`GET /v1/automations/:id/versions`**

List automation versions

List versions for a workflow or agent automation. YAML workflow lists include tagged releases plus the current untagged snapshot when HEAD is untagged (for example after restore), so the current version is always present. Agent lists remain Git release tags.

**Path parameters**

| Name | Type  | Description                                                             |
| ---- | ----- | ----------------------------------------------------------------------- |
| `id` | `str` | Workflow id, agent id, or typed alias like workflows.slug / agents.slug |

**Response**

```python
// ListAutomationVersionsResponse
```

### `client.automations.create_version`

**`POST /v1/automations/:id/versions`**

Create a workflow version

Create a tagged YAML workflow candidate from validated YAML or by copying an existing snapshot (`historyId`). Provide exactly one of `yaml` or `historyId`. Copy creates a new tagged row and leaves the source tag unchanged; it does not retag the original. Defaults to making the new version current. Set `activate: false` to keep it off live traffic until promote — that path requires an existing current workflow version and returns 400 if HEAD is empty. Agent automations are Git-backed and return 400. Requires a Bearer API key or a dashboard session.

**Example**

```python
client.automations.create_version(
    "workflows.extract-invoice",
    yaml="name: extract-invoice\n...",
    version="1.2.0",
    activate=False,  # requires an existing current version
)
# Copy without retagging the source snapshot:
client.automations.create_version(
    "workflows.extract-invoice",
    history_id="wfh_old",
    version="1.3.0",
    activate=False,
)
```

**Path parameters**

| Name | Type  | Description                                                             |
| ---- | ----- | ----------------------------------------------------------------------- |
| `id` | `str` | Workflow id, agent id, or typed alias like workflows.slug / agents.slug |

**Request body**

```python
// CreateAutomationVersionRequest
```

**Response**

```python
// AutomationVersion
```

### `client.automations.promote_version`

**`POST /v1/automations/:id/versions/:versionId/promote`**

Promote a workflow version

Make an existing tagged YAML workflow candidate current without creating another history row. Only tagged version rows can be promoted; untagged snapshots (including restore HEAD) and missing ids return 404. Agent automations return 400. Requires a Bearer API key or a dashboard session.

**Example**

```python
client.automations.promote_version("workflows.extract-invoice", "wfh_candidate")
# Untagged restore snapshots and unknown ids return 404.
```

**Path parameters**

| Name         | Type  | Description                                                                                                                       |
| ------------ | ----- | --------------------------------------------------------------------------------------------------------------------------------- |
| `id`         | `str` | Workflow id, agent id, or typed alias like workflows.slug / agents.slug                                                           |
| `version_id` | `str` | Tagged version id from GET /automations/{id}/versions. Untagged snapshots (for example after restore) and unknown ids return 404. |

**Response**

```python
// AutomationVersion
```

### `client.automations.restore_version`

**`POST /v1/automations/:id/versions/:versionId/restore`**

Restore a workflow version

Restore a YAML workflow automation by copying a previous snapshot into a new untagged current version. The source tag is left unchanged; the new HEAD appears in subsequent version lists as the untagged current row and cannot be promoted until you create a tagged copy. The JSON body may be `{}`; `message` is optional and defaults to a timestamped restore note. Agent automations return 400. Requires a Bearer API key or a dashboard session.

**Example**

```python
client.automations.restore_version("workflows.extract-invoice", "wfh_old")
client.automations.restore_version(
    "workflows.extract-invoice",
    "wfh_old",
    message="Roll back after failed candidate",
)
# Restore creates a new untagged current snapshot. Body may be {}.
```

**Path parameters**

| Name         | Type  | Description                                                             |
| ------------ | ----- | ----------------------------------------------------------------------- |
| `id`         | `str` | Workflow id, agent id, or typed alias like workflows.slug / agents.slug |
| `version_id` | `str` | Version id from GET /automations/{id}/versions (a workflow history id). |

**Request body**

```python
// RestoreAutomationVersionRequest
```

**Response**

```python
// AutomationVersion
```

## Evaluation

### `client.automations.dataset.export`

**`GET /v1/automations/:id/dataset/export`**

Export automation dataset

Download the automation dataset as a ZIP archive. The archive uses the examples/<name>/input and examples/<name>/expected folder convention, so it can be re-imported into another automation or environment. Cloud deployments may redirect large archives to a short-lived storage URL.

**Path parameters**

| Name | Type  | Description                   |
| ---- | ----- | ----------------------------- |
| `id` | `str` | Automation id or typed alias. |

**Query parameters**

| Name          | Type  | Description                                                                                        |
| ------------- | ----- | -------------------------------------------------------------------------------------------------- |
| `example_ids` | `str` | (optional)Optional comma-separated dataset example ids to export. Omit to export the full dataset. |

**Response**

```python
// bytes
```

### `client.automations.dataset.import_`

**`POST /v1/automations/:id/dataset/import`**

Import automation dataset

Import a dataset ZIP archive using the examples/<name>/input and examples/<name>/expected folder convention. Use `mode=append` for additive imports or `mode=replace` to replace the dataset.

**Path parameters**

| Name | Type  | Description                   |
| ---- | ----- | ----------------------------- |
| `id` | `str` | Automation id or typed alias. |

**Response**

```python
// DatasetImportResponse
```

### `client.automations.evaluators.get`

**`GET /v1/automations/:id/evaluators`**

Get evaluators

Fetch the evaluator configuration for an automation. Evaluators produce automated `score` results, which are separate from human review verdicts.

**Path parameters**

| Name | Type  | Description                   |
| ---- | ----- | ----------------------------- |
| `id` | `str` | Automation id or typed alias. |

**Response**

```python
// EvaluatorConfigResponse
```

### `client.automations.evaluators.update`

**`PUT /v1/automations/:id/evaluators`**

Replace evaluators

Replace the evaluator YAML for an automation. The submitted YAML is validated before it becomes the source for future experiment scores.

**Path parameters**

| Name | Type  | Description                   |
| ---- | ----- | ----------------------------- |
| `id` | `str` | Automation id or typed alias. |

**Request body**

```python
// EvaluatorConfigUpdate
```

**Response**

```python
// EvaluatorConfigResponse
```

### `client.automations.examples.list`

**`GET /v1/automations/:id/examples`**

List dataset examples

List dataset examples for one automation. Examples contain input, expected output, expected files, metadata, and optional overrides used by evaluation runs. Pass `include=metadata` to return ids, names, metadata, and expected file refs without loading input or expected JSON.

**Path parameters**

| Name | Type  | Description                                                              |
| ---- | ----- | ------------------------------------------------------------------------ |
| `id` | `str` | Automation id or typed alias, such as `workflows.slug` or `agents.slug`. |

**Query parameters**

| Name      | Type                          | Description                                                                                                                               |
| --------- | ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `limit`   | `int`                         | (optional)Maximum number of examples to return.                                                                                           |
| `offset`  | `int`                         | (optional)Zero-based offset for paging through examples.                                                                                  |
| `include` | `Literal["full", "metadata"]` | (optional)Response payload scope. `metadata` returns ids, names, metadata, and expected file refs without loading input or expected JSON. |

**Response**

```python
// DatasetExampleList
```

### `client.automations.examples.create`

**`POST /v1/automations/:id/examples`**

Create dataset example

Create one dataset example from JSON fields. Use dataset import for archive-based uploads and file-bearing examples.

**Path parameters**

| Name | Type  | Description                                                              |
| ---- | ----- | ------------------------------------------------------------------------ |
| `id` | `str` | Automation id or typed alias, such as `workflows.slug` or `agents.slug`. |

**Request body**

```python
// DatasetExampleMutation
```

**Response**

```python
// DatasetExample
```

### `client.automations.examples.get`

**`GET /v1/automations/:id/examples/:exampleId`**

Get dataset example

Fetch one dataset example, including input, expected output, expected files, metadata, and overrides.

**Path parameters**

| Name         | Type  | Description                                                                                                  |
| ------------ | ----- | ------------------------------------------------------------------------------------------------------------ |
| `id`         | `str` | Automation id or typed alias.                                                                                |
| `example_id` | `str` | Dataset example id. Agent examples may use deterministic name-derived ids returned by list/create responses. |

**Response**

```python
// DatasetExample
```

### `client.automations.examples.update`

**`PATCH /v1/automations/:id/examples/:exampleId`**

Update dataset example

Partially update a dataset example. Omitted fields are preserved; pass null for nullable fields to clear them.

**Path parameters**

| Name         | Type  | Description                                                                                                  |
| ------------ | ----- | ------------------------------------------------------------------------------------------------------------ |
| `id`         | `str` | Automation id or typed alias.                                                                                |
| `example_id` | `str` | Dataset example id. Agent examples may use deterministic name-derived ids returned by list/create responses. |

**Request body**

```python
// DatasetExampleUpdate
```

**Response**

```python
// DatasetExample
```

### `client.automations.examples.delete`

**`DELETE /v1/automations/:id/examples/:exampleId`**

Delete dataset example

Delete one dataset example from the automation dataset. This removes the example from future experiments.

**Path parameters**

| Name         | Type  | Description                                                                                                  |
| ------------ | ----- | ------------------------------------------------------------------------------------------------------------ |
| `id`         | `str` | Automation id or typed alias.                                                                                |
| `example_id` | `str` | Dataset example id. Agent examples may use deterministic name-derived ids returned by list/create responses. |

**Response**

```python
// DatasetExample
```

### `client.automations.examples.expected_files.list`

**`GET /v1/automations/:id/examples/:exampleId/expected`**

List expected files

List files stored under the expected folder for one automation dataset example.

**Path parameters**

| Name         | Type  | Description                   |
| ------------ | ----- | ----------------------------- |
| `id`         | `str` | Automation id or typed alias. |
| `example_id` | `str` | Dataset example id.           |

**Response**

```python
// DatasetExampleExpectedFileList
```

### `client.automations.examples.expected_files.create`

**`POST /v1/automations/:id/examples/:exampleId/expected`**

Upload expected files

Upload one or more files into the expected folder for an automation dataset example. Use `$file` references such as `expected/result.pdf` from expected JSON to compare file outputs.

**Path parameters**

| Name         | Type  | Description                   |
| ------------ | ----- | ----------------------------- |
| `id`         | `str` | Automation id or typed alias. |
| `example_id` | `str` | Dataset example id.           |

**Response**

```python
// DatasetExampleExpectedFileUploadResponse
```

### `client.automations.examples.expected_file.get`

**`GET /v1/automations/:id/examples/:exampleId/expected/:path`**

Download expected dataset file

Download one expected file attached to an automation dataset example.

**Path parameters**

| Name         | Type  | Description                             |
| ------------ | ----- | --------------------------------------- |
| `id`         | `str` | Automation id or typed alias.           |
| `example_id` | `str` | Dataset example id.                     |
| `path`       | `str` | Path under the example expected folder. |

**Response**

```python
// bytes
```

### `client.automations.examples.expected_file.update`

**`PATCH /v1/automations/:id/examples/:exampleId/expected/:path`**

Rename expected file

Rename one expected file attached to an automation dataset example. The parent folder is preserved.

**Path parameters**

| Name         | Type  | Description                             |
| ------------ | ----- | --------------------------------------- |
| `id`         | `str` | Automation id or typed alias.           |
| `example_id` | `str` | Dataset example id.                     |
| `path`       | `str` | Path under the example expected folder. |

**Request body**

```python
// DatasetExampleExpectedFileRenameRequest
```

**Response**

```python
// DatasetExampleExpectedFileRenameResponse
```

### `client.automations.examples.expected_file.delete`

**`DELETE /v1/automations/:id/examples/:exampleId/expected/:path`**

Delete expected file

Delete one file from an automation dataset example expected folder.

**Path parameters**

| Name         | Type  | Description                             |
| ------------ | ----- | --------------------------------------- |
| `id`         | `str` | Automation id or typed alias.           |
| `example_id` | `str` | Dataset example id.                     |
| `path`       | `str` | Path under the example expected folder. |

### `client.automations.examples.input_files.list`

**`GET /v1/automations/:id/examples/:exampleId/input`**

List input files

List files stored under the input folder for one automation dataset example.

**Path parameters**

| Name         | Type  | Description                   |
| ------------ | ----- | ----------------------------- |
| `id`         | `str` | Automation id or typed alias. |
| `example_id` | `str` | Dataset example id.           |

**Response**

```python
// DatasetExampleInputFileList
```

### `client.automations.examples.input_files.create`

**`POST /v1/automations/:id/examples/:exampleId/input`**

Upload input files

Upload one or more files into the input folder for an automation dataset example. Use `$file` references such as `input/invoice.pdf` from the example input JSON to consume them.

**Path parameters**

| Name         | Type  | Description                   |
| ------------ | ----- | ----------------------------- |
| `id`         | `str` | Automation id or typed alias. |
| `example_id` | `str` | Dataset example id.           |

**Response**

```python
// DatasetExampleInputFileUploadResponse
```

### `client.automations.examples.input_file.get`

**`GET /v1/automations/:id/examples/:exampleId/input/:path`**

Download input file

Download one file from an automation dataset example input folder.

**Path parameters**

| Name         | Type  | Description                                          |
| ------------ | ----- | ---------------------------------------------------- |
| `id`         | `str` | Automation id or typed alias.                        |
| `example_id` | `str` | Dataset example id.                                  |
| `path`       | `str` | Slash-delimited path under the example input folder. |

**Response**

```python
// bytes
```

### `client.automations.examples.input_file.update`

**`PATCH /v1/automations/:id/examples/:exampleId/input/:path`**

Rename input file

Rename one input file attached to an automation dataset example. The parent folder is preserved.

**Path parameters**

| Name         | Type  | Description                                          |
| ------------ | ----- | ---------------------------------------------------- |
| `id`         | `str` | Automation id or typed alias.                        |
| `example_id` | `str` | Dataset example id.                                  |
| `path`       | `str` | Slash-delimited path under the example input folder. |

**Request body**

```python
// DatasetExampleInputFileRenameRequest
```

**Response**

```python
// DatasetExampleInputFileRenameResponse
```

### `client.automations.examples.input_file.delete`

**`DELETE /v1/automations/:id/examples/:exampleId/input/:path`**

Delete input file

Delete one file from an automation dataset example input folder.

**Path parameters**

| Name         | Type  | Description                                          |
| ------------ | ----- | ---------------------------------------------------- |
| `id`         | `str` | Automation id or typed alias.                        |
| `example_id` | `str` | Dataset example id.                                  |
| `path`       | `str` | Slash-delimited path under the example input folder. |

### `client.automations.examples.run`

**`POST /v1/automations/:id/examples/:exampleId/run`**

Run dataset example

Start an asynchronous run using the input from one dataset example. Poll `GET /api/v1/runs/:id` for completion and use run scores or review endpoints to review the result.

**Path parameters**

| Name         | Type  | Description                   |
| ------------ | ----- | ----------------------------- |
| `id`         | `str` | Automation id or typed alias. |
| `example_id` | `str` | Dataset example id to run.    |

**Response**

```python
// ExampleRunResponse
```

### `client.automations.experiments.list`

**`GET /v1/automations/:id/experiments`**

List experiments

List experiment batches for one automation. Each experiment runs selected dataset examples and records automated evaluator scores.

**Path parameters**

| Name | Type  | Description                   |
| ---- | ----- | ----------------------------- |
| `id` | `str` | Automation id or typed alias. |

**Query parameters**

| Name        | Type  | Description                                                                             |
| ----------- | ----- | --------------------------------------------------------------------------------------- |
| `limit`     | `int` | (optional)Maximum number of experiment batches to return.                               |
| `offset`    | `int` | (optional)Zero-based offset for paging through experiment batches.                      |
| `from_date` | `str` | (optional)Filter to experiment batches created at or after this date or relative date.  |
| `to_date`   | `str` | (optional)Filter to experiment batches created at or before this date or relative date. |

**Response**

```python
// dict[str, Any]
```

### `client.automations.experiments.create`

**`POST /v1/automations/:id/experiments`**

Create experiment

Start an asynchronous experiment batch for one automation. Omit `examples` to run the full dataset, or pass specific example ids to run a subset.

**Path parameters**

| Name | Type  | Description                   |
| ---- | ----- | ----------------------------- |
| `id` | `str` | Automation id or typed alias. |

**Request body**

```python
// ExperimentCreate
```

**Response**

```python
// ExperimentCreateResponse
```

### `client.automations.experiments.get`

**`GET /v1/automations/:id/experiments/:experimentId`**

Get experiment

Fetch one experiment batch with its run summaries and evaluator results grouped by run id.

**Path parameters**

| Name            | Type  | Description                   |
| --------------- | ----- | ----------------------------- |
| `id`            | `str` | Automation id or typed alias. |
| `experiment_id` | `str` | Experiment batch id.          |

**Response**

```python
// ExperimentDetail
```

### `client.automations.experiments.cancel`

**`POST /v1/automations/:id/experiments/:experimentId/cancel`**

Cancel experiment

Request cancellation for an experiment batch. Already-completed runs remain recorded; queued or running work is cancelled when possible.

**Path parameters**

| Name            | Type  | Description                   |
| --------------- | ----- | ----------------------------- |
| `id`            | `str` | Automation id or typed alias. |
| `experiment_id` | `str` | Experiment batch id.          |

**Response**

```python
// ExperimentDetail
```

### `client.automations.experiments.export`

**`GET /v1/automations/:id/experiments/:experimentId/export`**

Export experiment eval results

Download eval result rows for a single experiment batch as CSV or JSON.

**Path parameters**

| Name            | Type  | Description |
| --------------- | ----- | ----------- |
| `id`            | `str` |             |
| `experiment_id` | `str` |             |

**Query parameters**

| Name            | Type                                 | Description |
| --------------- | ------------------------------------ | ----------- |
| `format`        | `Literal["csv", "json"]`             |             |
| `include_trace` | `Literal["0", "1", "true", "false"]` | (optional)  |

**Response**

```python
// str
```

### `client.automations.experiments.export_all`

**`GET /v1/automations/:id/experiments/export`**

Export all experiment eval results

Download every eval result row for an automation as CSV or JSON.

**Path parameters**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | `str` |             |

**Query parameters**

| Name     | Type                     | Description |
| -------- | ------------------------ | ----------- |
| `format` | `Literal["csv", "json"]` |             |

**Response**

```python
// str
```

### `client.automations.experiments.create_stream`

**`POST /v1/automations/:id/experiments/stream`**

Create automation experiment with NDJSON progress

Starts a batch eval experiment for workflow or agent automations and streams per-run completion events as NDJSON.

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
// str
```

### `client.experiments.resolve`

**`GET /v1/experiments/:experimentId`**

Resolve experiment by id

Returns the owning automation for an experiment batch id. Used when callers only know the experiment id.

**Path parameters**

| Name            | Type  | Description |
| --------------- | ----- | ----------- |
| `experiment_id` | `str` |             |

**Response**

```python
// ExperimentRef
```

### `client.runs.scores.list`

**`GET /v1/runs/:id/scores`**

List run evaluator scores

List automated evaluator results for one run. Use `score` for evaluator output and run reviews for human verdicts.

**Path parameters**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | `str` | Run id.     |

**Response**

```python
// RunScoresResponse
```

## Reviews

### `client.automations.reviews.health`

**`GET /v1/automations/:id/reviews/health`**

Get automation review health

Aggregates reviewed correctness, review coverage, bucketed counts, and rolling-window confidence for one automation. Prefer this endpoint for single-automation monitoring dashboards.

**Path parameters**

| Name | Type  | Description                                                              |
| ---- | ----- | ------------------------------------------------------------------------ |
| `id` | `str` | Workflow id, agent id, or typed alias like workflows.slug / agents.slug. |

**Query parameters**

| Name                  | Type                              | Description                                                                             |
| --------------------- | --------------------------------- | --------------------------------------------------------------------------------------- |
| `type`                | `str`                             | (optional)Comma-separated: workflow,agent.                                              |
| `status`              | `str`                             | (optional)Comma-separated execution statuses.                                           |
| `trigger`             | `str`                             | (optional)Comma-separated trigger types.                                                |
| `triggered_by`        | `str`                             | (optional)Comma-separated user ids, or **system** for system-triggered runs.            |
| `source_ref`          | `str`                             | (optional)                                                                              |
| `batch_id`            | `str`                             | (optional)                                                                              |
| `example_id`          | `str`                             | (optional)                                                                              |
| `example_id_contains` | `str`                             | (optional)                                                                              |
| `from`                | `str`                             | (optional)Start of the run-created time range. Defaults to now-30d.                     |
| `to`                  | `str`                             | (optional)End of the run-created time range.                                            |
| `completed_after`     | `str`                             | (optional)                                                                              |
| `completed_before`    | `str`                             | (optional)                                                                              |
| `experiments`         | `str`                             | (optional)Set to false to exclude experiment batch runs.                                |
| `bucket`              | `Literal["day", "week", "month"]` | (optional)Calendar bucket size for the bar chart series. Defaults to day.               |
| `rolling_window`      | `int`                             | (optional)Number of reviewed runs per rolling correctness point. Defaults to 100.       |
| `min_rolling_reviews` | `int`                             | (optional)Minimum reviewed runs required before emitting rolling points. Defaults to 1. |

**Response**

```python
// RunReviewHealthResponse
```

### `client.runs.promote`

**`POST /v1/runs/:id/promote`**

Promote run to example

Turn a reviewed run into a dataset example. The new example uses the run input and any corrected output/files stored through the review endpoints.

**Path parameters**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | `str` | Run id.     |

**Request body**

```python
// PromoteRunRequest
```

**Response**

```python
// PromoteRunResponse
```

### `client.runs.reviews.get`

**`GET /v1/runs/:id/reviews`**

Get run review

Returns review metadata and corrections for a run. Corrected files are listed at GET /runs/{id}/reviews/expected; embed review + expected artifacts with GET /runs/{id}?expand=execution.

**Path parameters**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | `str` | Run id.     |

**Response**

```python
// RunReviewDetail
```

### `client.runs.reviews.update`

**`PUT /v1/runs/:id/reviews`**

Update run review

Create or replace review metadata for a run.

**Path parameters**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | `str` | Run id.     |

**Request body**

```python
// RunReviewRequest
```

**Response**

```python
// RunReviewDetail
```

### `client.runs.reviews.clear`

**`DELETE /v1/runs/:id/reviews`**

Clear run review

Deletes review metadata, corrections, and corrected files for the run.

**Path parameters**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | `str` | Run id.     |

**Response**

```python
// RunReviewDetail
```

### `client.runs.reviews.list_expected`

**`GET /v1/runs/:id/reviews/expected`**

List corrected files

Returns corrected artifact files attached to the run review. Review metadata and corrected JSON output live at GET /runs/{id}/reviews.

**Path parameters**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | `str` | Run id.     |

**Response**

```python
// RunReviewExpectedArtifacts
```

### `client.runs.reviews.copy_output_to_expected / upload_expected`

**`POST /v1/runs/:id/reviews/expected`**

Add corrected file

Attach one corrected file to a run review. Send multipart/form-data with `file` and optional `name` to upload a local file, or JSON with `outputFileName` and optional `expectedName` to copy an existing run output file.

**Path parameters**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | `str` | Run id.     |

**Request body**

```python
// RunReviewExpectedFileCopyRequest
```

**Response**

```python
// RunReviewExpectedFileMutationResponse
```

### `client.runs.reviews.download_expected`

**`GET /v1/runs/:id/reviews/expected/:filename`**

Download corrected artifact file

Downloads one corrected artifact file attached to the run review. Use the `filename` returned by the corrected-output collection endpoint.

**Path parameters**

| Name       | Type  | Description                                                                                             |
| ---------- | ----- | ------------------------------------------------------------------------------------------------------- |
| `id`       | `str` | Run id.                                                                                                 |
| `filename` | `str` | Corrected artifact file name or slash-delimited path, as returned by `GET /runs/{id}/reviews/expected`. |

**Response**

```python
// bytes
```

### `client.runs.reviews.rename_expected`

**`PATCH /v1/runs/:id/reviews/expected/:filename`**

Rename corrected artifact file

Renames one corrected artifact file attached to the run review.

**Path parameters**

| Name       | Type  | Description                                                                                             |
| ---------- | ----- | ------------------------------------------------------------------------------------------------------- |
| `id`       | `str` | Run id.                                                                                                 |
| `filename` | `str` | Corrected artifact file name or slash-delimited path, as returned by `GET /runs/{id}/reviews/expected`. |

**Request body**

```python
// RunReviewExpectedFileUpdateRequest
```

**Response**

```python
// RunReviewExpectedFileUpdateResponse
```

### `client.runs.reviews.delete_expected`

**`DELETE /v1/runs/:id/reviews/expected/:filename`**

Delete corrected artifact file

Deletes one corrected artifact file attached to the run review.

**Path parameters**

| Name       | Type  | Description                                                                                             |
| ---------- | ----- | ------------------------------------------------------------------------------------------------------- |
| `id`       | `str` | Run id.                                                                                                 |
| `filename` | `str` | Corrected artifact file name or slash-delimited path, as returned by `GET /runs/{id}/reviews/expected`. |

## Files

### `client.files.upload`

**`POST /v1/files`**

Upload file

Upload a reusable file that can later be referenced by run inputs or dataset examples.

**Response**

```python
// File
```

### `client.files.get`

**`GET /v1/files/:id`**

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

**`DELETE /v1/files/:id`**

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

### `client.files.download`

**`GET /v1/files/:id/content`**

Download file content

Download bytes for a reusable uploaded file. Direct-enabled deployments redirect responses above their configured body limit to a short-lived signed storage URL; multipart-only/on-prem deployments stream through the API.

**Path parameters**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | `str` | File id     |

### `client.files.create_upload`

**`POST /v1/files/uploads`**

Prepare file upload

Negotiate multipart when the file fits the deployment body limit (or direct storage is disabled), otherwise return a short-lived signed storage PUT. The response transport is authoritative; clients must not guess from file size alone.

**Request body**

```python
// CreateFileUploadSessionRequest
```

**Response**

```python
// Union[PresignedFileUploadSession, MultipartFileUploadFallback]
```

### `client.files.abort_upload`

**`DELETE /v1/files/uploads/:uploadId`**

Abort file upload

Abort a pending storage-direct upload and remove its pending object.

**Path parameters**

| Name        | Type  | Description |
| ----------- | ----- | ----------- |
| `upload_id` | `str` |             |

**Response**

```python
// AbortFileUploadResponse
```

### `client.files.complete_upload`

**`POST /v1/files/uploads/:uploadId/complete`**

Complete file upload

Verify a storage-direct pending object and promote it into a reusable file. Safe to retry.

**Path parameters**

| Name        | Type  | Description |
| ----------- | ----- | ----------- |
| `upload_id` | `str` |             |

**Response**

```python
// File
```

## Runs

### `client.runs.list`

**`GET /v1/runs`**

List runs

List workflow and agent runs with cursor pagination.

**Query parameters**

| Name                    | Type  | Description                                                                                                                   |
| ----------------------- | ----- | ----------------------------------------------------------------------------------------------------------------------------- |
| `type`                  | `str` | (optional)                                                                                                                    |
| `source`                | `str` | (optional)                                                                                                                    |
| `status`                | `str` | (optional)                                                                                                                    |
| `trigger`               | `str` | (optional)                                                                                                                    |
| `triggered_by`          | `str` | (optional)                                                                                                                    |
| `source_ref`            | `str` | (optional)                                                                                                                    |
| `batch_id`              | `str` | (optional)                                                                                                                    |
| `example_id`            | `str` | (optional)                                                                                                                    |
| `example_id_contains`   | `str` | (optional)                                                                                                                    |
| `from`                  | `str` | (optional)                                                                                                                    |
| `to`                    | `str` | (optional)                                                                                                                    |
| `created_after`         | `str` | (optional)                                                                                                                    |
| `created_before`        | `str` | (optional)                                                                                                                    |
| `completed_after`       | `str` | (optional)                                                                                                                    |
| `completed_before`      | `str` | (optional)                                                                                                                    |
| `cursor`                | `str` | (optional)                                                                                                                    |
| `offset`                | `int` | (optional)                                                                                                                    |
| `limit`                 | `int` | (optional)                                                                                                                    |
| `ids`                   | `str` | (optional)                                                                                                                    |
| `experiments`           | `str` | (optional)                                                                                                                    |
| `sort`                  | `str` | (optional)                                                                                                                    |
| `order`                 | `str` | (optional)                                                                                                                    |
| `review_status`         | `str` | (optional)                                                                                                                    |
| `review_verdict`        | `str` | (optional)                                                                                                                    |
| `has_review`            | `str` | (optional)                                                                                                                    |
| `no_review`             | `str` | (optional)                                                                                                                    |
| `has_corrections`       | `str` | (optional)                                                                                                                    |
| `review_note_contains`  | `str` | (optional)                                                                                                                    |
| `review_created_after`  | `str` | (optional)                                                                                                                    |
| `review_created_before` | `str` | (optional)                                                                                                                    |
| `review_updated_after`  | `str` | (optional)                                                                                                                    |
| `review_updated_before` | `str` | (optional)                                                                                                                    |
| `review_closed_after`   | `str` | (optional)                                                                                                                    |
| `review_closed_before`  | `str` | (optional)                                                                                                                    |
| `since_last_closed`     | `str` | (optional)                                                                                                                    |
| `sample_rate`           | `str` | (optional)Keep runs whose `sampleRank` is below this threshold (0–1). Pages may return fewer than `limit` rows when filtered. |

**Response**

```python
// RunsListResponse
```

### `client.run`

**`POST /v1/runs`**

Start a run

Start a run. Send JSON or multipart/form-data.

How to read a run: the envelope is at the root. The automation business result is in `output` (per-automation, not this generic schema). Status is `execution.status` (`execution.retry.nextRun.status` is a later retry). `input`, `usage`, and `debug` appear only with `?expand=`. `eval` is present only on eval-scoped runs.

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
// Run
```

### `client.runs.get`

**`GET /v1/runs/:id`**

Get a run

Fetch one run by id. By default this returns core metadata plus terminal output/error fields. Pass `?expand=input,usage,execution,debug` to include detailed sub-objects; `expand=execution` is also where embedded review and expected artifacts appear.

How to read a run: the envelope is at the root. The automation business result is in `output` (per-automation, not this generic schema). Status is `execution.status` (`execution.retry.nextRun.status` is a later retry). `input`, `usage`, and `debug` appear only with `?expand=`. `eval` is present only on eval-scoped runs.

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

### `client.runs.artifacts.list`

**`GET /v1/runs/:id/artifacts`**

List run artifacts

Returns a JSON list of downloadable artifact paths for a run. Pass `zip=1` to switch the response to a ZIP download containing output files.

**Path parameters**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | `str` | Run id      |

**Query parameters**

| Name     | Type                | Description                                                                                                                                                                                                                                                                                                                                                         |
| -------- | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `zip`    | `Literal["1"]`      | (optional)When `1`, download output files as a ZIP instead of listing paths. Does not include trace, scores, or input — use `GET /runs/{id}/scores` and `GET /runs/{id}/trace` for those. Cloud deployments reject archives whose uncompressed inputs exceed 32 MiB (`413 artifacts_zip_too_large`); download files individually or pass a smaller `files=` subset. |
| `bundle` | `Literal["review"]` | (optional)With `zip=1`, use `review` to download a ZIP with `output/` and `expected/` folders (corrected review artifacts).                                                                                                                                                                                                                                         |
| `token`  | `str`               | (optional)Signed email download token (zip only; no Bearer required).                                                                                                                                                                                                                                                                                               |

**Response**

```python
// RunArtifactsResponse
```

### `client.runs.artifacts.download`

**`GET /v1/runs/:id/artifacts/:path`**

Download run artifact

Download one artifact by path. Cloud deployments may redirect to a short-lived storage URL for large files.

**Path parameters**

| Name   | Type  | Description |
| ------ | ----- | ----------- |
| `id`   | `str` |             |
| `path` | `str` |             |

### `client.runs.cancel`

**`POST /v1/runs/:id/cancel`**

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

**`GET /v1/runs/:id/events`**

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

### `client.rerun`

**`POST /v1/runs/:id/rerun`**

Retry run

Start a new run using the source run input. By default the retry uses the latest automation version; pass `version=original` to pin the same source version as the original run.

**Path parameters**

| Name | Type  | Description             |
| ---- | ----- | ----------------------- |
| `id` | `str` | Source run id to retry. |

**Query parameters**

| Name                  | Type  | Description                                                                            |
| --------------------- | ----- | -------------------------------------------------------------------------------------- |
| `version`             | `str` | (optional)Version for the new run. `original` pins the source run. Defaults to latest. |
| `wait_for_completion` | `int` | (optional)Seconds to wait before returning (max 600). Omit for async.                  |

**Response**

```python
// Run
```

### `client.runs.steps`

**`GET /v1/runs/:id/steps`**

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

**`GET /v1/runs/:id/trace`**

Get run trace

Return low-level execution trace events for debugging one run. Workflow runs expose observability phases or step records; agent runs expose parsed trace.jsonl events. The shape is intentionally extensible, but common fields are documented.

**Path parameters**

| Name | Type  | Description |
| ---- | ----- | ----------- |
| `id` | `str` | Run id.     |

**Response**

```python
// RunTraceResponse
```

### `client.runs.usage`

**`GET /v1/runs/:id/usage`**

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
