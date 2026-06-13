# Errors

Every non-2xx response raises a typed subclass of `EigenpalError`.

| HTTP    | Class                     | Notes                                                                |
| ------- | ------------------------- | -------------------------------------------------------------------- |
| 400     | `EigenpalValidationError` | `.issues` carries per-field problems                                 |
| 401     | `EigenpalAuthError`       | Bad / missing API key                                                |
| 403     | `EigenpalForbiddenError`  | `api_trigger_disabled`, `manual_trigger_disabled`, or scope mismatch |
| 404     | `EigenpalNotFoundError`   | Workflow / execution doesn't exist                                   |
| 429     | `EigenpalRateLimitError`  | `.retry_after` is the server-suggested wait (seconds)                |
| 5xx     | `EigenpalServerError`     |                                                                      |
| timeout | `EigenpalTimeoutError`    |                                                                      |

```python
from eigenpal import EigenpalClient, EigenpalValidationError

try:
    client.run("workflows.extract-invoice")
except EigenpalValidationError as e:
    for issue in e.issues:
        print(f"{issue['field']}: {issue['message']}")
    raise
```

## Request id

Every error carries `request_id` from the server's response header. Forward it to support for fastest triage:

```python
from eigenpal import EigenpalError

try:
    client.run("workflows.extract-invoice", input=input)
except EigenpalError as e:
    log.error("eigenpal call failed", extra={"request_id": e.request_id, "status": e.status})
    raise
```

## Bad base_url

If `base_url` points at a non-API host (the marketing site, a misconfigured proxy), the SDK raises `EigenpalError` with a clear message instead of surfacing a raw `JSONDecodeError`. Set `base_url` to your EigenPal instance root.
