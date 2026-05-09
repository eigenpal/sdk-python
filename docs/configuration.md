# Configuration

```python
EigenpalClient(
    api_key="eg_...",                       # or EIGENPAL_API_KEY env var
    base_url="https://app.eigenpal.com",    # or EIGENPAL_BASE_URL env var
    timeout_seconds=60.0,                   # per-request timeout
    verify_ssl=True,                        # set False only for testing
)
```

## API key

`api_key` always wins. If omitted, the SDK reads `EIGENPAL_API_KEY` from the environment. If neither is set, the constructor raises `ValueError`.

Issue keys from the dashboard under **Settings → API Keys**. Keep them in env vars or a secret manager; never check them into git.

## Self-hosted

Point at your own deployment via `base_url`:

```python
import os

EigenpalClient(
    base_url=os.environ.get("EIGENPAL_BASE_URL", "https://eigenpal.acme.internal"),
)
```

`base_url` overrides `EIGENPAL_BASE_URL`. Defaults to `https://app.eigenpal.com`.

## Timeouts

`timeout_seconds` applies per-request via `httpx.Timeout`. For workflow runs longer than the timeout, prefer `workflows.executions.run_and_wait` (client-side polling) over `workflows.run(wait_for_completion=...)` (server-side hold).

## Connection lifetime

The client owns an httpx connection pool. Use as a context manager so the pool is closed deterministically:

```python
with EigenpalClient() as client:
    client.workflows.run("extract-invoice", input=input)
```

Outside a `with`, the pool is closed when the client is garbage-collected.
