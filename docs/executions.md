# Runs

`client.runs` is the shared run API for workflow, agent, manual, and eval runs.

## Start

```python
started = client.run("workflows.extract-invoice", input={})
```

For short jobs, ask the server to hold the request:

```python
result = client.run(
    "workflows.extract-invoice",
    input={},
    wait_for_completion=60,
)
```

For longer jobs, use `client.run_and_wait` or poll manually:

```python
final = client.run_and_wait("agents.invoice-agent", input={})
```

## Get

```python
run = client.runs.get(started.id)
# { id, type, finished, execution, output?, files?, error?, timing, ... }
```

Add heavier optional sections with `expand`:

```python
run = client.runs.get(started.id, expand=["usage", "execution"])
print(run.output, run.usage, run.execution)
```

## List

```python
listing = client.runs.list(
    type="workflow",
    status="failed,cancelled",
    limit=50,
)
```

## Subresources

```python
client.runs.usage(started.id)
client.runs.steps(started.id)
client.runs.events(started.id)
client.runs.trace.get(started.id)
client.runs.feedback.get(started.id)
client.runs.feedback.update(started.id, {"body": "Looks wrong", "status": "open"})
```

## Artifacts

```python
artifacts = client.runs.artifacts.list(started.id)
content = client.runs.artifacts.download(started.id, artifacts.artifacts[0].path)
```

Artifacts are run-scoped snapshots. Reusable uploaded files are managed separately through `client.files`.

## Cancel And Rerun

```python
client.runs.cancel(started.id)
rerun = client.rerun(started.id, wait_for_completion=60)
```

## Promote

Copy a completed run's input, output, feedback, and expected artifacts into a dataset example on the same automation:

```python
result = client.runs.promote(started.id, name="golden-invoice")
print(result.example_id, result.name)
```
