# EigenPal Python SDK

Official Python SDK for the [EigenPal](https://eigenpal.com) API.

```bash
pip install eigenpal
```

```python
import os
from pathlib import Path
from eigenpal import Eigenpal

client = Eigenpal(api_key=os.environ["EIGENPAL_API_KEY"])

# Pass a Path / file handle / { content, filename, mime_type }. The SDK
# uploads the request as multipart/form-data, no base64 needed.
result = client.executions.run_and_wait(
    "extract-invoice",
    input={"contract_document": Path("contract.pdf")},
)
print(result["status"], result["result"])
```

## Authentication

Generate an API key from the dashboard under **Settings → API Keys**, then pass it explicitly:

```python
client = Eigenpal(api_key=os.environ["EIGENPAL_API_KEY"])
```

The `api_key` argument always wins. If you omit it, the SDK falls back to `EIGENPAL_API_KEY` for convenience, handy in scripts where you'd be writing exactly the line above.

## Self-hosted

Point the SDK at your own deployment via `base_url`:

```python
client = Eigenpal(
    api_key=os.environ["EIGENPAL_API_KEY"],
    base_url=os.environ.get("EIGENPAL_BASE_URL", "https://eigenpal.acme.internal"),
)
```

`base_url` likewise wins over the `EIGENPAL_BASE_URL` env fallback. Defaults to `https://app.eigenpal.com` (the hosted cloud).

## Triggering workflows

`client.workflows.run(workflow_id, input=None, **options)` enqueues a workflow execution.

```python
from pathlib import Path

# Async: returns immediately with { execution_id }.
result = client.workflows.run(
    "extract-invoice",
    input={"contract_document": Path("contract.pdf")},
)
print(result.execution_id)

# Sync: server holds the connection up to 60 seconds.
result = client.workflows.run(
    "extract-invoice",
    input={"contract_document": Path("contract.pdf")},
    wait_for_completion=60,
)
print(result.status, result.result)

# Long-running: client-side polling (default 5min cap).
final = client.executions.run_and_wait(
    "extract-invoice",
    input={"contract_document": Path("contract.pdf")},
)
print(final["status"])
```

The `input` argument is the workflow input map keyed by input name (as declared in the workflow). Omit it for inputs-less workflows. Other keyword args: `version`, `overrides`, `wait_for_completion`.

## File inputs

Pass a `pathlib.Path`, an open file handle, or an explicit `{"content": bytes, "filename": str, "mime_type": str}` descriptor. The SDK auto-detects files and uploads as `multipart/form-data` (the same shape as `curl -F`):

```python
from pathlib import Path

# Path: filename + mime type inferred.
client.workflows.run("extract-invoice", input={
    "contract_document": Path("contract.pdf"),
})

# File handle: filename inferred from .name.
with open("contract.pdf", "rb") as f:
    client.workflows.run("extract-invoice", input={"contract_document": f})

# Explicit dict: required for raw bytes.
client.workflows.run("extract-invoice", input={
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
status = client.executions.get(execution_id)
#   ExecutionStatusResponse(execution_id=..., status=..., result=..., ...)

executions = client.executions.list(
    workflow_id="extract-invoice",
    status="failed",
    from_date="now()-7d",
    limit=50,
)

client.executions.cancel(execution_id)
```

## Workflows

```python
client.workflows.list(search="invoice", limit=20)
client.workflows.get("extract-invoice")
client.workflows.versions("extract-invoice")
```

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
from eigenpal import Eigenpal, EigenpalValidationError

try:
    client.workflows.run("extract-invoice")
except EigenpalValidationError as e:
    for issue in e.issues:
        print(f"{issue['field']}: {issue['message']}")
    raise
```

## Configuration

```python
client = Eigenpal(
    api_key="eg_…",                 # or EIGENPAL_API_KEY
    base_url="https://app.eigenpal.com",  # or EIGENPAL_BASE_URL
    timeout_seconds=60.0,           # per-request timeout
    verify_ssl=True,
)
```

Use as a context manager to ensure the underlying HTTP connection pool is closed:

```python
with Eigenpal() as client:
    client.workflows.run("extract-invoice")
```

## License

Apache-2.0.
