# eigenpal

Trigger EigenPal workflows from Python.

[![pypi](https://img.shields.io/pypi/v/eigenpal?color=3B5BDB&labelColor=555&label=pypi)](https://pypi.org/project/eigenpal/)
[![downloads](https://img.shields.io/pypi/dm/eigenpal?color=3B5BDB&labelColor=555&label=downloads)](https://pypi.org/project/eigenpal/)
[![license](https://img.shields.io/badge/license-Apache--2.0-3B5BDB?labelColor=555)](https://github.com/eigenpal/sdk-python/blob/main/LICENSE)
[![docs](https://img.shields.io/badge/docs-eigenpal-3B5BDB?labelColor=555)](https://github.com/eigenpal/sdk-python)

## Install

```bash
pip install eigenpal
```

Requires Python 3.9+. Get an API key at **app.eigenpal.com → Settings → API Keys**.

## Quick start

```python
import os
from pathlib import Path
from eigenpal import EigenpalClient, EigenpalValidationError

client = EigenpalClient(api_key=os.environ["EIGENPAL_API_KEY"])

# Pass a Path / file handle / { content, filename, mime_type }. The SDK
# uploads the request as multipart/form-data, no base64 needed.
result = client.workflows.executions.run_and_wait(
    "extract-invoice",
    input={"contract_document": Path("contract.pdf")},
)
print(result["status"], result["result"])
```

## Authentication

Generate an API key from the dashboard under **Settings → API Keys**, then pass it explicitly:

```python
client = EigenpalClient(api_key=os.environ["EIGENPAL_API_KEY"])
```

The `api_key` argument always wins. If you omit it, the SDK falls back to `EIGENPAL_API_KEY` for convenience, handy in scripts where you'd be writing exactly the line above.

## Self-hosted

Point the SDK at your own deployment via `base_url`:

```python
client = EigenpalClient(
    api_key=os.environ["EIGENPAL_API_KEY"],
    base_url=os.environ.get("EIGENPAL_BASE_URL", "https://eigenpal.acme.internal"),
)
```

`base_url` likewise wins over the `EIGENPAL_BASE_URL` env fallback. Defaults to `https://app.eigenpal.com` (the hosted cloud).

## Starting runs

`client.run(target, input=None, **options)` starts a workflow or agent run. Targets can be strings like `"workflows.extract-invoice"` / `"agents.invoice-agent"` or structured objects like `{"type": "workflow", "slug": "extract-invoice"}`.

```python
from pathlib import Path

# Async: returns immediately with { run_id }.
result = client.run(
    "workflows.extract-invoice",
    input={"contract_document": Path("contract.pdf")},
)
print(result.run_id)

# Sync: server holds the connection up to 60 seconds.
result = client.run(
    "workflows.extract-invoice",
    input={"contract_document": Path("contract.pdf")},
    wait_for_completion=60,
)
print(result.status, result.output)

# Long-running: client-side polling (default 5min cap).
final = client.workflows.executions.run_and_wait(
    "extract-invoice",
    input={"contract_document": Path("contract.pdf")},
)
print(final["status"])
```

The `input` argument is the input map keyed by input name. Omit it for inputs-less runs. Put the workflow version or agent source ref in the target; other keyword args include `overrides` and `wait_for_completion`.

## File inputs

Pass a `pathlib.Path`, an open file handle, or an explicit `{"content": bytes, "filename": str, "mime_type": str}` descriptor. The SDK auto-detects files and uploads as `multipart/form-data` (the same shape as `curl -F`):

```python
from pathlib import Path

# Path: filename + mime type inferred.
client.run("workflows.extract-invoice", input={
    "contract_document": Path("contract.pdf"),
})

# File handle: filename inferred from .name.
with open("contract.pdf", "rb") as f:
    client.run("workflows.extract-invoice", input={"contract_document": f})

# Explicit dict: required for raw bytes.
client.run("workflows.extract-invoice", input={
    "contract_document": {
        "content": data,
        "filename": "contract.pdf",
        "mime_type": "application/pdf",
    },
})
```

> **Don't** base64-encode files yourself. The SDK is multipart-first; base64 doubles the payload size and skips the optimised upload path.

## Execution polling

```python
summaries = client.runs.list(
    type="workflow",
    source="extract-invoice",
    status="failed,cancelled",
)

run = client.runs.get(run_id, include="detail")
client.runs.cancel(run_id)

status = client.runs.get(run_id)
#   RunEnvelope(run=...)

executions = client.runs.list(
    type="workflow",
    source="extract-invoice",
    status="failed",
    from_date="now()-7d",
    limit=50,
)

client.runs.cancel(run_id)
```

`/api/v1/runs` is the shared run API for workflow, agent, and eval runs. Use
`type="workflow"|"agent"` and `source="<workflowId-or-agentId>"` to scope list
calls.

## Workflows

```python
client.workflows.list(search="invoice", limit=20)
client.workflows.get("extract-invoice")
client.workflows.versions("extract-invoice")
```

## Agents

```python
client.agents.list(search="invoice")
client.agents.get("invoice-agent")

result = client.run("agents.invoice-agent", input={
    "invoice": Path("invoice.pdf"),
})

client.runs.get(result.run_id)
client.runs.cancel(result.run_id)
```

Agent run listing uses the same shared runs API with `type_="agent"` and the
agent id or slug as `source`.

## Errors

Every non-2xx response raises a typed subclass of `EigenpalError`:

| HTTP    | Class                     | Notes                                                 |
| ------- | ------------------------- | ----------------------------------------------------- |
| 400     | `EigenpalValidationError` | `.issues` carries the per-field problems              |
| 401     | `EigenpalAuthError`       | Bad / missing API key                                 |
| 403     | `EigenpalForbiddenError`  | API trigger disabled, scope mismatch                  |
| 404     | `EigenpalNotFoundError`   | Workflow / execution doesn't exist                    |
| 429     | `EigenpalRateLimitError`  | `.retry_after` is the server-suggested wait (seconds) |
| 5xx     | `EigenpalServerError`     |                                                       |
| timeout | `EigenpalTimeoutError`    |                                                       |

```python
from eigenpal import EigenpalClient, EigenpalValidationError

client = EigenpalClient(api_key=os.environ["EIGENPAL_API_KEY"])

try:
    # First arg accepts the workflow slug ("extract-invoice") or id ("wf_abc123").
    result = client.workflows.executions.run_and_wait(
        "extract-invoice",
        input={"language": "en"},
    )
    print(result["status"], result["result"])
except EigenpalValidationError as err:
    for issue in err.issues:
        print(f"{issue['field']}: {issue['message']}")
    raise
```

For file inputs, see [docs/files.md](./docs/files.md).

## Reference

| Topic                                     | What's in it                                       |
| ----------------------------------------- | -------------------------------------------------- |
| [Workflows](./docs/workflows.md)          | List, get, trigger runs, pin versions.             |
| [Executions](./docs/executions.md)        | Status, polling, cancel, run-and-wait.             |
| [File inputs](./docs/files.md)            | Multipart upload from Path, file handle, or bytes. |
| [Errors](./docs/errors.md)                | Typed exceptions, retries, request ids.            |
| [Configuration](./docs/configuration.md)  | API key, base_url, timeouts, headers.              |
| [Full API reference](./docs/reference.md) | Every method, generated from the OpenAPI spec.     |

## License

Apache-2.0.
