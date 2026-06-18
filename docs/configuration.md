# Configuration

```python
EigenpalClient(
    api_key="eig_live_...",                       # or EIGENPAL_API_KEY env var
    base_url="https://studio.eigenpal.com",    # or EIGENPAL_BASE_URL env var
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

`base_url` overrides `EIGENPAL_BASE_URL`. Defaults to `https://studio.eigenpal.com`.

## Timeouts

`timeout_seconds` applies per-request via `httpx.Timeout`. For runs longer than the timeout, use `client.run_and_wait(...)` or start asynchronously with `client.run(...)` and poll `client.runs.get(id)`.

## Connection lifetime

The client owns an httpx connection pool. Use as a context manager so the pool is closed deterministically:

```python
with EigenpalClient() as client:
    client.run("workflows.extract-invoice", input=input)
```

Outside a `with`, the pool is closed when the client is garbage-collected.
