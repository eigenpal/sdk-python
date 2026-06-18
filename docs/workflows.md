# Automations

`client.automations` is the public entry point for both workflows and agents. Start runs with root `client.run()`.

## List

```python
listing = client.automations.list(limit=20, search="invoice")
for automation in listing.data:
    print(automation.id, automation.type, automation.name)
```

## Get

```python
automation = client.automations.get("workflows.extract-invoice")
# { id, type, name, inputSchema, outputSchema, triggers, ... }
```

Use typed ids or aliases (`workflows.<slug>` / `agents.<slug>`) when a slug could exist in both systems.

## Versions

```python
listing = client.automations.versions("workflows.extract-invoice")
for version in listing.data:
    print(version.id, version.version, version.isCurrent)
```

## Triggers

```python
state = client.automations.triggers("agents.invoice-agent")
for trigger in state.triggers:
    print(trigger.type, trigger.enabled)
```

Trigger mutation and source management are intentionally not part of the public SDK surface.

## Start A Run

```python
started = client.run(
    "workflows.extract-invoice",
    input={"contract_document": Path("contract.pdf")},
)
```

Pin a version or agent source ref by suffixing the target:

```python
client.run("workflows.extract-invoice@1.2.3", input={})
client.run("agents.invoice-agent@main", input={})
```

## File Inputs

See [File inputs](./files.md). Pass a `Path`, file handle, or `{"content": bytes, "filename": str, "mime_type": str}` and the SDK uploads via `multipart/form-data` automatically.
