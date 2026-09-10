# Automations

`client.automations` is the public entry point for both workflows and agents. Start runs with root `client.run()`.

## List

```python
listing = client.automations.list(limit=20, search="invoice", folder_id="fldr_…")
for automation in listing.data:
    print(automation.id, automation.type, automation.folderPath)
```

`folder_id="null"` lists unfiled YAML workflows at the tenant root. Combining `folder_id` with `type="agent"` is rejected. Agent automations always return `folderId` / `folderPath` as `null`.

## Get

```python
automation = client.automations.get("workflows.extract-invoice")
# { id, type, name, inputSchema, outputSchema, triggers, ... }
```

Use typed ids or aliases (`workflows.<slug>` / `agents.<slug>`) when a slug could exist in both systems.

## Move

Move YAML workflows between organizing folders. `folder_path` creates missing workflow folders; empty or `/` (and `folder_id=None`) files the workflow at root. Agent automations have no database folder model and are rejected.

```python
client.automations.move("workflows.extract-invoice", folder_path="billing/invoices")
client.automations.move("workflows.extract-invoice", folder_id=None)
```

## Delete

Delete uses the same cleanup as the dashboard. Workflows archive the automations registry parent and keep execution history. Agents delete the agent implementation and history, archive the registry parent, and best-effort-delete leftover agent storage. There is no uniform purge of every related artifact.

```python
client.automations.delete("workflows.extract-invoice")
client.automations.delete("agents.invoice-agent")
```

## Folders

`client.folders` manages workflow and template trees. Deleting a folder cascade-deletes child folders and unfiles contained workflows or templates; it does not delete those resources. Nested agent directories in Git are source organization only and are not folders.

```python
tree = client.folders.list(type="workflow", tree="true")
folder = client.folders.create(name="invoices", type="workflow")
client.folders.update(folder.id, parent_id=None)
client.folders.delete(folder.id)
```

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
