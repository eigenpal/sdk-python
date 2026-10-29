# Errors

## API request errors

Every non-2xx response raises a typed subclass of `EigenpalError`.

| HTTP    | Class                     | Notes                                                                |
| ------- | ------------------------- | -------------------------------------------------------------------- |
| 400     | `EigenpalValidationError` | `.issues` carries per-field problems                                 |
| 401     | `EigenpalAuthError`       | Bad / missing API key                                                |
| 403     | `EigenpalForbiddenError`  | `api_trigger_disabled`, `manual_trigger_disabled`, or scope mismatch |
| 404     | `EigenpalNotFoundError`   | Automation / run does not exist                                      |
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

## Run failures are returned data

A successful API call can return a failed run. HTTP 200 means the request
succeeded, not that processing succeeded. `finished: true` means the run is
terminal, including failure and cancellation. Inspect `execution.status`.

A failed run's `error` is an object with `code`, `message`, and `retryable`.
A deliberate `control.fail` rejection also includes `statusCode` (for example 422) and `step`. That business code is not the HTTP response status.
`retryable` describes potential recovery; it does not schedule another run.
The SDK does not throw an HTTP exception or automatically rerun a workflow
because a successful response contains a failed run.

Run errors were previously strings. Display `error.message` after updating
clients. Historical failures without retained typed metadata have
`code: "unknown_error"` and no business `statusCode`.

See [Errors and recovery](https://docs.eigenpal.com/guides/errors) for the API
issue codes, run failure codes, examples, retry policies, and legacy endpoints.

```python
run = client.runs.get(run_id)
if run["execution"]["status"] == "failed" and run.get("error"):
    failure = run["error"]
    print(failure["code"], failure.get("statusCode"), failure["message"])
```
