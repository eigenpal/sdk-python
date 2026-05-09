"""Tests for multipart file uploads — exercises the ``-F``-style path the
SDK takes whenever ``workflows.run``'s input contains a Path / file-like /
explicit dict descriptor."""

from __future__ import annotations

import json
from io import BytesIO
from pathlib import Path

import httpx
import pytest
import respx

from eigenpal import EigenpalClient


@pytest.fixture
def client() -> EigenpalClient:
    return EigenpalClient(api_key="eg_test_key", base_url="http://localhost:3000")


@respx.mock
def test_path_input_uploads_as_multipart(tmp_path: Path, client: EigenpalClient) -> None:
    pdf = tmp_path / "contract.pdf"
    pdf.write_bytes(b"%PDF-1.4 fake content")

    route = respx.post("http://localhost:3000/api/v1/workflows/wf_xyz/run").mock(
        return_value=httpx.Response(201, json={"executionId": "exec_abc"})
    )

    result = client.workflows.run(
        "wf_xyz",
        input={"contract_document": pdf, "language": "en"},
    )

    assert result.execution_id == "exec_abc"
    request = route.calls.last.request
    content_type = request.headers["content-type"]
    assert content_type.startswith("multipart/form-data; boundary=")

    body = request.content.decode("utf-8", errors="replace")
    assert 'name="contract_document"' in body
    assert 'filename="contract.pdf"' in body
    # Scalar input rides in the _json sidecar
    assert 'name="_json"' in body
    assert '"language": "en"' in body or '"language":"en"' in body


@respx.mock
def test_explicit_descriptor_with_raw_bytes(client: EigenpalClient) -> None:
    route = respx.post("http://localhost:3000/api/v1/workflows/wf_xyz/run").mock(
        return_value=httpx.Response(201, json={"executionId": "exec_abc"})
    )

    client.workflows.run(
        "wf_xyz",
        input={
            "contract": {
                "content": b"%PDF",
                "filename": "contract.pdf",
                "mime_type": "application/pdf",
            },
        },
    )

    body = route.calls.last.request.content.decode("utf-8", errors="replace")
    assert 'filename="contract.pdf"' in body
    assert "application/pdf" in body


@respx.mock
def test_file_like_object_uploads(tmp_path: Path, client: EigenpalClient) -> None:
    fpath = tmp_path / "policy.txt"
    fpath.write_bytes(b"hello world")

    route = respx.post("http://localhost:3000/api/v1/workflows/wf_xyz/run").mock(
        return_value=httpx.Response(201, json={"executionId": "exec_abc"})
    )

    with fpath.open("rb") as f:
        client.workflows.run("wf_xyz", input={"policy": f})

    body = route.calls.last.request.content.decode("utf-8", errors="replace")
    assert 'name="policy"' in body
    assert 'filename="policy.txt"' in body


@respx.mock
def test_no_files_uses_json(client: EigenpalClient) -> None:
    route = respx.post("http://localhost:3000/api/v1/workflows/wf_xyz/run").mock(
        return_value=httpx.Response(201, json={"executionId": "exec_abc"})
    )

    client.workflows.run("wf_xyz", input={"language": "en"})

    request = route.calls.last.request
    assert request.headers["content-type"] == "application/json"
    assert json.loads(request.content) == {"input": {"language": "en"}}


@respx.mock
def test_multiple_files_all_present(tmp_path: Path, client: EigenpalClient) -> None:
    a = tmp_path / "a.pdf"
    a.write_bytes(b"a")
    b = tmp_path / "b.pdf"
    b.write_bytes(b"b")

    route = respx.post("http://localhost:3000/api/v1/workflows/wf_xyz/run").mock(
        return_value=httpx.Response(201, json={"executionId": "exec_abc"})
    )

    client.workflows.run("wf_xyz", input={"primary": a, "secondary": b})

    body = route.calls.last.request.content.decode("utf-8", errors="replace")
    assert 'filename="a.pdf"' in body
    assert 'filename="b.pdf"' in body


@respx.mock
def test_bytesio_uploads_with_default_filename(client: EigenpalClient) -> None:
    route = respx.post("http://localhost:3000/api/v1/workflows/wf_xyz/run").mock(
        return_value=httpx.Response(201, json={"executionId": "exec_abc"})
    )

    buf = BytesIO(b"data")
    # BytesIO has no .name → falls back to "file"
    client.workflows.run(
        "wf_xyz",
        input={"contract": {"content": buf.getvalue(), "filename": "named.bin"}},
    )

    body = route.calls.last.request.content.decode("utf-8", errors="replace")
    assert 'filename="named.bin"' in body
