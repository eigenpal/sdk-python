from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import httpx
import pytest
import respx

from eigenpal import (
    DeleteAutomationResponse,
    EigenpalClient,
    EigenpalNotFoundError,
    EigenpalValidationError,
    UpdateAutomationRequest,
)

WORKFLOW_ID = "wf_01ABCDEFGHJKMNPQRSTVWXYZ"
FOLDER_ID = "fldr_01ABCDEFGHJKMNPQRSTVWXYZ"
BASE = "http://localhost:3000"


def workflow_automation(**overrides: Any) -> dict[str, Any]:
    return {
        "id": WORKFLOW_ID,
        "type": "workflow",
        "slug": "extract-invoice",
        "name": "extract-invoice",
        "folderId": FOLDER_ID,
        "folderPath": "billing/invoices",
        "createdAt": "2026-09-10T00:00:00.000Z",
        **overrides,
    }


@respx.mock
def test_list_omits_folder_id_query_when_unset() -> None:
    client = EigenpalClient(api_key="eg_test", base_url=BASE, max_retries=0)
    listing = {
        "data": [workflow_automation()],
        "total": 1,
        "limit": 20,
        "offset": 0,
    }
    route = respx.get(
        f"{BASE}/v1/automations",
        params={"type": "workflow", "limit": 20},
    ).mock(return_value=httpx.Response(200, json=listing))

    page = client.automations.list(type="workflow", limit=20)

    assert route.called
    assert "folderId" not in str(route.calls.last.request.url)
    assert page["data"][0]["folderId"] == FOLDER_ID


@respx.mock
def test_list_encodes_folder_id_none_as_root_sentinel() -> None:
    client = EigenpalClient(api_key="eg_test", base_url=BASE, max_retries=0)
    listing = {
        "data": [workflow_automation(folderId=None, folderPath=None)],
        "total": 1,
        "limit": 20,
        "offset": 0,
    }
    route = respx.get(
        f"{BASE}/v1/automations",
        params={"type": "workflow", "folderId": "null", "limit": 20},
    ).mock(return_value=httpx.Response(200, json=listing))

    page = client.automations.list(type="workflow", folder_id=None, limit=20)

    assert route.called
    assert route.calls.last.request.method == "GET"
    assert page["data"][0]["folderId"] is None
    assert page["data"][0]["folderPath"] is None


@respx.mock
def test_move_sends_patch_body_for_folder_id_and_folder_path() -> None:
    client = EigenpalClient(api_key="eg_test", base_url=BASE, max_retries=0)
    by_path = respx.patch(f"{BASE}/v1/automations/workflows.extract-invoice").mock(
        return_value=httpx.Response(200, json=workflow_automation())
    )
    by_id = respx.patch(f"{BASE}/v1/automations/{WORKFLOW_ID}").mock(
        return_value=httpx.Response(
            200, json=workflow_automation(folderId=None, folderPath=None)
        )
    )

    moved = client.automations.move(
        "workflows.extract-invoice", folder_path="billing/invoices"
    )
    to_root = client.automations.move(WORKFLOW_ID, folder_id=None)

    parsed_path = UpdateAutomationRequest.from_dict(
        json.loads(by_path.calls.last.request.content.decode())
    )
    assert parsed_path.folder_path == "billing/invoices"
    parsed_root = UpdateAutomationRequest.from_dict(
        json.loads(by_id.calls.last.request.content.decode())
    )
    assert parsed_root.folder_id is None
    assert moved["folderPath"] == "billing/invoices"
    assert to_root["folderId"] is None


@respx.mock
def test_delete_sends_delete_and_returns_deleted_envelope() -> None:
    client = EigenpalClient(api_key="eg_test", base_url=BASE, max_retries=0)
    route = respx.delete(f"{BASE}/v1/automations/workflows.extract-invoice").mock(
        return_value=httpx.Response(200, json={"deleted": True, "id": WORKFLOW_ID})
    )

    deleted = client.automations.delete("workflows.extract-invoice")

    assert route.called
    parsed = DeleteAutomationResponse.from_dict(dict(deleted))
    assert parsed.deleted is True
    assert parsed.id == WORKFLOW_ID


@respx.mock
def test_maps_move_and_delete_errors_to_typed_exceptions() -> None:
    client = EigenpalClient(api_key="eg_test", base_url=BASE, max_retries=0)
    respx.patch(f"{BASE}/v1/automations/agents.invoice-agent").mock(
        return_value=httpx.Response(
            400,
            json={
                "issues": [
                    {
                        "field": "id",
                        "message": "Agent automations cannot be moved; they have no folder model",
                        "code": "invalid_value",
                    }
                ]
            },
        )
    )
    respx.delete(f"{BASE}/v1/automations/missing").mock(
        return_value=httpx.Response(
            404,
            json={
                "issues": [{"field": "id", "message": "Automation not found", "code": "not_found"}]
            },
        )
    )

    with pytest.raises(EigenpalValidationError):
        client.automations.move("agents.invoice-agent", folder_path="billing")
    with pytest.raises(EigenpalNotFoundError):
        client.automations.delete("missing")


def test_public_facade_and_docs_cover_move_delete_and_folder_id_list() -> None:
    client = EigenpalClient(api_key="eg_test", base_url=BASE, max_retries=0)
    assert callable(client.automations.list)
    assert callable(client.automations.move)
    assert callable(client.automations.delete)
    assert callable(client.folders.list)

    docs = (Path(__file__).resolve().parents[1] / "docs" / "reference.md").read_text()
    assert "### `client.automations.move`" in docs
    assert "### `client.automations.delete`" in docs
    assert "`folderId`" in docs or "folderId" in docs
    assert "`folderPath`" in docs or "folderPath" in docs
    assert "keep execution history" in docs
    assert "best-effort-delete agent storage" in docs
