from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import httpx
import pytest
import respx

from eigenpal import (
    CreateFolderRequest,
    DeleteFolderResponse,
    EigenpalClient,
    EigenpalNotFoundError,
    EigenpalValidationError,
    Folder,
    FolderType,
    UpdateFolderRequest,
)

FOLDER_ID = "fldr_01ABCDEFGHJKMNPQRSTVWXYZ"
PARENT_ID = "fldr_01PARENT0000000000000000"
BASE = "http://localhost:3000"


def public_folder(**overrides: Any) -> dict[str, Any]:
    return {
        "id": FOLDER_ID,
        "parentId": None,
        "type": "workflow",
        "name": "invoices",
        "createdAt": "2026-09-10T00:00:00.000Z",
        **overrides,
    }


@respx.mock
def test_list_uses_required_type_and_optional_query() -> None:
    client = EigenpalClient(api_key="eg_test", base_url=BASE, max_retries=0)
    listing = [public_folder(childCount=1, workflowCount=2)]
    route = respx.get(
        f"{BASE}/v1/folders",
        params={"type": "workflow", "parentId": "null", "tree": "true"},
    ).mock(return_value=httpx.Response(200, json=listing))

    page = client.folders.list(type="workflow", parent_id="null", tree="true")

    assert route.called
    assert route.calls.last.request.method == "GET"
    parsed = Folder.from_dict(dict(page[0]))
    assert parsed.type_ is FolderType.WORKFLOW
    assert parsed.name == "invoices"
    assert parsed.child_count == 1


@respx.mock
def test_create_get_update_delete_match_contract() -> None:
    client = EigenpalClient(api_key="eg_test", base_url=BASE, max_retries=0)
    created = respx.post(f"{BASE}/v1/folders").mock(
        return_value=httpx.Response(201, json=public_folder(parentId=PARENT_ID))
    )
    fetched = respx.get(f"{BASE}/v1/folders/{FOLDER_ID}").mock(
        return_value=httpx.Response(200, json=public_folder())
    )
    updated = respx.patch(f"{BASE}/v1/folders/{FOLDER_ID}").mock(
        return_value=httpx.Response(200, json=public_folder(name="billing", parentId=None))
    )
    deleted = respx.delete(f"{BASE}/v1/folders/{FOLDER_ID}").mock(
        return_value=httpx.Response(200, json={"deleted": True, "id": FOLDER_ID})
    )

    create_result = client.folders.create(
        name="invoices", type="workflow", parent_id=PARENT_ID
    )
    get_result = client.folders.get(FOLDER_ID)
    update_result = client.folders.update(FOLDER_ID, name="billing", parent_id=None)
    delete_result = client.folders.delete(FOLDER_ID)

    parsed_create = CreateFolderRequest.from_dict(
        json.loads(created.calls.last.request.content.decode())
    )
    assert parsed_create.name == "invoices"
    assert parsed_create.type_ is FolderType.WORKFLOW
    assert parsed_create.parent_id == PARENT_ID
    parsed_update = UpdateFolderRequest.from_dict(
        json.loads(updated.calls.last.request.content.decode())
    )
    assert parsed_update.name == "billing"
    assert parsed_update.parent_id is None

    assert fetched.called
    assert deleted.called
    assert create_result["parentId"] == PARENT_ID
    assert get_result["id"] == FOLDER_ID
    assert update_result["name"] == "billing"
    parsed_delete = DeleteFolderResponse.from_dict(dict(delete_result))
    assert parsed_delete.deleted is True
    assert parsed_delete.id == FOLDER_ID


@respx.mock
def test_maps_404_and_400_to_typed_errors() -> None:
    client = EigenpalClient(api_key="eg_test", base_url=BASE, max_retries=0)
    respx.get(f"{BASE}/v1/folders/{FOLDER_ID}").mock(
        return_value=httpx.Response(
            404,
            json={"issues": [{"field": "id", "message": "Folder not found", "code": "not_found"}]},
        )
    )
    respx.patch(f"{BASE}/v1/folders/{FOLDER_ID}").mock(
        return_value=httpx.Response(
            400,
            json={
                "issues": [
                    {
                        "field": "parentId",
                        "message": "Cannot move a folder into itself",
                        "code": "invalid_value",
                    }
                ]
            },
        )
    )

    with pytest.raises(EigenpalNotFoundError):
        client.folders.get(FOLDER_ID)
    with pytest.raises(EigenpalValidationError):
        client.folders.update(FOLDER_ID, parent_id=FOLDER_ID)


def test_public_facade_and_docs_cover_folder_methods() -> None:
    client = EigenpalClient(api_key="eg_test", base_url=BASE, max_retries=0)
    assert callable(client.folders.list)
    assert callable(client.folders.get)
    assert callable(client.folders.create)
    assert callable(client.folders.update)
    assert callable(client.folders.delete)

    docs = (Path(__file__).resolve().parents[1] / "docs" / "reference.md").read_text()
    assert "### `client.folders.list`" in docs
    assert "### `client.folders.create`" in docs
    assert "### `client.folders.get`" in docs
    assert "### `client.folders.update`" in docs
    assert "### `client.folders.delete`" in docs
    assert 'type="workflow"' in docs
    assert "agent folders" not in docs
