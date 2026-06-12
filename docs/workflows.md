# Workflows

`client.workflows` is the entry point for listing and fetching workflows. Start workflow runs with root `client.run()`.

## List

```python
listing = client.workflows.list(limit=20, search="invoice")
for wf in listing.data:
    print(wf.id, wf.version)
```

Query options: `limit`, `offset`, `search` (substring), `name` (exact slug), `kind` (`"workflow" | "block"`).

## Get

```python
wf = client.workflows.get("extract-invoice")
#   WorkflowSummary(id, version, created_at, updated_at)
```

`version` is the current published release tag (e.g. `"1.2.4"`), or `None` if no version is published yet.

## Trigger a run

Three ways to run, depending on how long you want to wait.

### Async (returns immediately)

```python
from pathlib import Path

result = client.run("workflows.extract-invoice", input={
    "contract_document": Path("contract.pdf"),
})
print(result.id)
```

For webhooks and fire-and-forget jobs. Poll status via [`client.runs.get`](./executions.md).

### Sync (server holds up to 60s)

```python
result = client.run(
    "workflows.extract-invoice",
    input={"contract_document": Path("contract.pdf")},
    wait_for_completion=60,
)
print(result.finished, result.output)
```

If the run completes within `wait_for_completion` seconds, `finished` is true and `output` is populated. Either way the response carries the run `id`.

### Long-running (client polls)

```python
final = client.workflows.executions.run_and_wait(
    "extract-invoice",
    input={"contract_document": Path("contract.pdf")},
)
```

Default 5 min cap; tune with `poll_interval_seconds` and `timeout_seconds`. See [Executions](./executions.md#run-and-wait).

## Pin a version

```python
client.run("workflows.extract-invoice@1.2.3", input=input)
```

If omitted, the run picks up the workflow's current published version at trigger time.

## Override step output

```python
client.run("workflows.extract-invoice", input=input, overrides={
    "steps": {"parse-contract": {"text": "pre-extracted..."}},
})
```

Replaces a step's output for this one run. The step doesn't execute. Useful for testing downstream steps without re-running expensive parsing.

## List versions

```python
listing = client.workflows.versions("extract-invoice", limit=10)
for v in listing.data:
    print(v.id, v.version, v.is_current)
```

Returns published versions in reverse-chronological order.

## File inputs

See [File inputs](./files.md). In short: pass a `Path`, a file handle, or `{"content": bytes, "filename": str, "mime_type": str}` and the SDK uploads via `multipart/form-data` automatically.
