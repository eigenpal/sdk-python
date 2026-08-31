from pathlib import Path

import httpx
import respx

from eigenpal import EigenpalClient
from eigenpal._generated.api.templates.templates_content_get import _parse_response
from eigenpal._generated.client import Client


@respx.mock
def test_template_create_and_revision_download(tmp_path: Path) -> None:
    client = EigenpalClient(api_key="eg_test", base_url="http://localhost:3000")
    template_file = tmp_path / "contract.docx"
    template_file.write_bytes(b"docx")
    upload_prepare = respx.post("http://localhost:3000/v1/files/uploads").mock(
        return_value=httpx.Response(
            200,
            json={
                "transport": "multipart",
                "url": "/v1/files",
                "maxFileSizeBytes": 50_000_000,
            },
        )
    )
    upload_file = respx.post("http://localhost:3000/v1/files").mock(
        return_value=httpx.Response(200, json={"id": "file_123456789012345678901"})
    )
    respx.delete("http://localhost:3000/v1/files/file_123456789012345678901").mock(
        return_value=httpx.Response(200, json={"deleted": True})
    )
    created = respx.post("http://localhost:3000/v1/templates").mock(
        return_value=httpx.Response(201, json={"id": "tmpl_1"})
    )
    replaced = respx.put("http://localhost:3000/v1/templates/tmpl_1").mock(
        return_value=httpx.Response(200, json={"id": "tmpl_1"})
    )
    content = respx.get(
        "http://localhost:3000/v1/templates/tmpl_1/content",
        params={"revisionId": "tmpr_1"},
    ).mock(return_value=httpx.Response(200, content=b"stable-bytes"))

    assert client.templates.create(template_file, name="Contract")["id"] == "tmpl_1"
    assert created.calls.last.request.headers["content-type"] == "application/json"
    assert (
        created.calls.last.request.content
        == b'{"fileId":"file_123456789012345678901","name":"Contract"}'
    )
    client.templates.create_from_file_id("file_abcdefghijklmnopqrstu", name="Existing")
    client.templates.replace_from_file_id("tmpl_1", "file_abcdefghijklmnopqrstu")
    assert upload_prepare.call_count == 1
    assert upload_file.call_count == 1
    assert (
        created.calls.last.request.content
        == b'{"fileId":"file_abcdefghijklmnopqrstu","name":"Existing"}'
    )
    assert (
        replaced.calls.last.request.content
        == b'{"fileId":"file_abcdefghijklmnopqrstu"}'
    )
    downloaded = client.templates.download("tmpl_1", revision_id="tmpr_1")
    assert isinstance(downloaded, bytes)
    assert downloaded == b"stable-bytes"
    assert content.called


def test_public_facade_owns_file_upload_helpers_and_omits_staging() -> None:
    client = EigenpalClient(api_key="eg_test", base_url="http://localhost:3000")
    assert callable(client.templates.create)
    assert callable(client.templates.replace)
    assert callable(client.templates.create_from_file_id)
    assert callable(client.templates.replace_from_file_id)
    assert callable(client.templates.download)
    assert not hasattr(client.templates, "staging")

    docs = (Path(__file__).resolve().parents[1] / "docs" / "reference.md").read_text()
    assert "### `client.templates.create`" in docs
    assert "### `client.templates.replace`" in docs
    assert "create_from_file_id" in docs
    assert "replace_from_file_id" in docs
    assert "client.templates.staging" not in docs

    create_src = (
        Path(__file__).resolve().parents[1]
        / "src/eigenpal/_generated/api/templates/templates_create.py"
    ).read_text()
    replace_src = (
        Path(__file__).resolve().parents[1]
        / "src/eigenpal/_generated/api/templates/templates_replace.py"
    ).read_text()
    assert 'headers["Content-Type"] = "multipart/form-data"' not in create_src
    assert 'headers["Content-Type"] = "multipart/form-data"' not in replace_src
    assert "to_multipart" not in create_src
    assert "to_multipart" not in replace_src
    assert 'headers["Content-Type"] = "application/json"' in create_src
    assert 'headers["Content-Type"] = "application/json"' in replace_src


def test_generated_content_get_parses_bytes() -> None:
    parsed = _parse_response(
        client=Client(base_url="http://localhost"),
        response=httpx.Response(
            200,
            content=b"template-bytes",
            headers={"content-type": "application/octet-stream"},
        ),
    )
    assert parsed == b"template-bytes"
