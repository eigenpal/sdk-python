# Executions

`client.workflows.executions` only exposes `run_and_wait`. Inspect and manage existing workflow runs through `client.runs`.

## Which polling option do I pick?

| Run length   | Use                                                                            |
| ------------ | ------------------------------------------------------------------------------ |
| 0–60s        | `client.run("workflows.<slug>", input, wait_for_completion=60)` — server hold. |
| 60s–5min     | `client.workflows.executions.run_and_wait(id, input)` — client polls every 2s. |
| Driving a UI | `client.run(...)` then poll `client.runs.get(id)` yourself.                    |

## Statuses

```
created → pending → running → waiting → finalizing → completed
                                                     ↘ failed
                                                     ↘ cancelled
                                                     ↘ rejected
```

The first five are non-terminal; the last four are terminal. Always check `status` before reading `result`.

## Get

```python
run = client.runs.get(run_id)
#   RunEnvelope(run=...)
```

`result` is set on `status == "completed"`. `error` is set on `status == "failed"`.

### Per-step detail

```python
detail = client.runs.get(run_id, include="detail")
```

Returns the full per-step execution payload (heavier; intended for debugging, not happy-path UI).

## Run and wait

The convenience helper that wraps trigger + poll:

```python
final = client.workflows.executions.run_and_wait(
    "extract-invoice",
    input={"contract_document": Path("contract.pdf")},
    poll_interval_seconds=2.0,    # default 2.0
    timeout_seconds=5 * 60.0,     # default 300.0
)
```

Triggers async, then polls `client.runs.get` until terminal or timeout. Raises `EigenpalTimeoutError` on timeout.

## List

```python
executions = client.runs.list(
    type="workflow",
    source="wf_abc123",
    status=["failed", "cancelled"],                # str or list[str]
    from_date="now()-7d",                          # ISO-8601 or relative expression
    to_date="now()",
    limit=50,
)
```

Item shape: `{ id, workflow_id, status, trigger_type, trigger_input, result, error, created_at, started_at, completed_at, workflow }`.

`workflow` is `{ id, name }` of the owning workflow, or `None` if it has been deleted.

## Cancel

```python
client.runs.cancel(run_id)
```

Idempotent. For runs not yet picked up by a worker (`created`/`pending`), transitions immediately to `cancelled`. For `running` executions, stamps `cancel_requested_at` so the worker honors the cancel at the next checkpoint.

## Polling pattern

If `run_and_wait` doesn't fit (e.g. you're driving a UI progress bar), poll manually:

```python
import time

TERMINAL = {"completed", "failed", "cancelled", "rejected"}

triggered = client.run("workflows.extract-invoice", input=input)
status = None
while True:
    status = client.runs.get(triggered.run_id)
    if status.status in TERMINAL:
        break
    time.sleep(2)

print(status.status, status.output, status.error)
```

## Context manager

The client owns an httpx connection pool. Use a `with` block to close it deterministically:

```python
with EigenpalClient(api_key=api_key) as client:
    client.run("workflows.extract-invoice", input=input)
```
