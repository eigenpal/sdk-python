# eigenpal

Trigger and inspect Eigenpal automations from Python.

[![pypi](https://img.shields.io/pypi/v/eigenpal?color=3B5BDB&labelColor=555&label=pypi)](https://pypi.org/project/eigenpal/)
[![downloads](https://img.shields.io/pypi/dm/eigenpal?color=3B5BDB&labelColor=555&label=downloads)](https://pypi.org/project/eigenpal/)
[![license](https://img.shields.io/badge/license-Apache--2.0-3B5BDB?labelColor=555)](https://github.com/eigenpal/sdk-python/blob/main/LICENSE)

## Install

```bash
pip install eigenpal
```

Requires Python 3.9+. Get an API key at **studio.eigenpal.com -> Settings -> API Keys**.

## Quick Start

```python
import os
from pathlib import Path
from eigenpal import EigenpalClient

client = EigenpalClient(api_key=os.environ["EIGENPAL_API_KEY"])

result = client.run_and_wait(
    "workflows.extract-invoice",
    input={"contract_document": Path("contract.pdf")},
)

print(result.finished, result.output)
```

`target` is always typed: `workflows.<slug>` or `agents.<slug>`. That keeps workflow and agent slugs unambiguous.

## Automations

Workflows and agents are exposed as automations.

```python
listing = client.automations.list(search="invoice")
automation = client.automations.get("workflows.extract-invoice")
versions = client.automations.versions("workflows.extract-invoice")
triggers = client.automations.triggers("workflows.extract-invoice")
```

## Runs

```python
started = client.run("agents.invoice-agent", input={"invoice": Path("invoice.pdf")})

run = client.runs.get(started.id, expand=["usage", "execution"])
usage = client.runs.usage(started.id)
steps = client.runs.steps(started.id)
events = client.runs.events(started.id)
trace = client.runs.trace.get(started.id)

client.runs.cancel(started.id)
client.rerun(started.id, wait_for_completion=60)
```

List calls use the same run API for workflows, agents, manual runs, and eval runs:

```python
recent_failures = client.runs.list(
    type="workflow",
    status="failed,cancelled",
    limit=50,
)
```

## Files And Artifacts

Use `client.files` for reusable upload-first blobs. When referenced by a run input, Eigenpal snapshots the file into run-scoped artifacts.

```python
uploaded = client.files.upload(Path("contract.pdf"))

started = client.run(
    "workflows.extract-invoice",
    input={"contract_document": {"$fileId": uploaded.id}},
)

artifacts = client.runs.artifacts.list(started.id)
content = client.runs.artifacts.download(started.id, artifacts.artifacts[0].path)
```

You can also pass a `Path`, file handle, or `{"content": bytes, "filename": str, "mime_type": str}` directly to `client.run`; the SDK sends multipart form data automatically. Durable run inputs and dataset examples store scoped `{"$file": "input/..."}` artifact refs after ingestion.

## Errors

Every non-2xx response raises a typed subclass of `EigenpalError`:

| HTTP    | Class                     |
| ------- | ------------------------- |
| 400     | `EigenpalValidationError` |
| 401     | `EigenpalAuthError`       |
| 403     | `EigenpalForbiddenError`  |
| 404     | `EigenpalNotFoundError`   |
| 429     | `EigenpalRateLimitError`  |
| 5xx     | `EigenpalServerError`     |
| timeout | `EigenpalTimeoutError`    |

## Reference

| Topic                                     | What is in it                                                      |
| ----------------------------------------- | ------------------------------------------------------------------ |
| [Automations](./docs/workflows.md)        | List, inspect, versions, triggers.                                 |
| [Runs](./docs/executions.md)              | Start, poll, cancel, rerun, usage, steps, events, traces, reviews. |
| [File inputs](./docs/files.md)            | Multipart upload from Path, file handle, or bytes.                 |
| [Errors](./docs/errors.md)                | Typed exceptions, retries, request ids.                            |
| [Configuration](./docs/configuration.md)  | API key, base_url, timeouts, headers.                              |
| [Full API reference](./docs/reference.md) | Every method, generated from OpenAPI.                              |

## License

Apache-2.0.
