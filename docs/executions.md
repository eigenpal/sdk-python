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

The first five are non-terminal; the last four are terminal. Check `finished` (or `execution.status` with `expand`) before reading `output`/`files`/`error`.

## Get

```python
run = client.runs.get(run_id)
#   Run(id=..., type=..., finished=..., execution=..., output=..., files=..., ...)
```

Terminal runs expose `output`, `files`, and `error` at the top level. Completed runs include `output` and `files`; failed or cancelled runs include `error`.
Downloadable output files are listed in `files` on completed runs; pass each entry's `path`
to `client.runs.artifacts.download`.

### Expanding heavier fields

```python
run = client.runs.get(run_id, expand=["usage", "execution"])
print(run.output, run.usage, run.execution)
```

`expand` adds optional nested sections in-place onto the run object. Pass a list of valid tokens: `input`, `usage`, `execution`, and `debug`; `execution` adds the heavier workflow step details or agent artifact summary.

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

Item shape: `{ id, type, finished, timing, source, trigger, execution, error?, eval? }`.

`source` identifies the owning workflow or agent. List rows always include slim
`execution` but omit completed-only `output`/`files`; fetch the detail with
`client.runs.get(id)` when you need output artifacts.

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
run = None
while True:
    run = client.runs.get(triggered.id)
    if run.finished:
        break
    time.sleep(2)

print(run.execution.status, run.output, run.error)
```

## Context manager

The client owns an httpx connection pool. Use a `with` block to close it deterministically:

```python
with EigenpalClient(api_key=api_key) as client:
    client.run("workflows.extract-invoice", input=input)
```
