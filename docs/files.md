# File inputs

When a workflow input is a file, the SDK uploads it as `multipart/form-data` (the same shape as `curl -F`). No base64, no payload doubling.

## From a Path

```python
from pathlib import Path

client.run("workflows.extract-invoice", input={
    "contract_document": Path("contract.pdf"),
})
```

Filename and MIME type are inferred automatically.

## From a file handle

```python
with open("contract.pdf", "rb") as f:
    client.run("workflows.extract-invoice", input={"contract_document": f})
```

Filename inferred from `f.name`.

## From raw bytes

```python
client.run("workflows.extract-invoice", input={
    "contract_document": {
        "content": data,
        "filename": "contract.pdf",
        "mime_type": "application/pdf",
    },
})
```

## Multiple files

```python
client.run("workflows.compare-versions", input={
    "original": Path("v1.pdf"),
    "revised": Path("v2.pdf"),
    "reference": Path("ref.pdf"),
})
```

Each file becomes a top-level form field. Mix files and scalar inputs freely; scalars ride along in a single `_json` text field automatically.

## Nested files aren't extracted

Only top-level file values become multipart fields. Files inside lists or nested dicts stay in the JSON sidecar and the server won't see them as uploads:

```python
# DON'T — `documents` becomes a JSON list, no upload.
client.run("workflows.compare", input={"documents": [Path("a.pdf"), Path("b.pdf")]})

# DO — flatten to top-level keys, your workflow accepts them by name.
client.run("workflows.compare", input={"document_0": Path("a.pdf"), "document_1": Path("b.pdf")})
```

## Don't base64 yourself

```python
# Don't do this. Doubles the payload size and skips the optimised path.
import base64
client.run("workflows.extract-invoice", input={
    "contract_document": base64.b64encode(data).decode(),
})
```

The SDK picks multipart whenever it sees a `Path`, file-like object, or `{"content": ..., "filename": ..., "mime_type": ...}` dict. Plain strings pass through as scalar inputs.
