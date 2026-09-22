from __future__ import annotations

import json

import httpx
import respx

from eigenpal import EigenpalClient

WORKFLOW_ID = "wf_01ABCDEFGHJKMNPQRSTVWXYZ"
REVIEW_ID = "dsr_01ABCDEFGHJKMNPQRSTVWXYZ"
ITEM_ID = "dsri_01ABCDEFGHJKMNPQRSTVWXYZ"
BASE = "http://localhost:3000"


@respx.mock
def test_list_encodes_status_filter_and_pagination() -> None:
    client = EigenpalClient(api_key="eg_test", base_url=BASE, max_retries=0)
    route = respx.get(
        f"{BASE}/v1/automations/{WORKFLOW_ID}/dataset-review-requests",
        params={"status": "open,paused", "limit": 20, "offset": 5},
    ).mock(return_value=httpx.Response(200, json={"data": [], "total": 0}))

    client.automations.dataset_review_requests.list(
        WORKFLOW_ID,
        status=["open", "paused"],
        limit=20,
        offset=5,
    )

    assert route.called
    assert route.calls.last.request.method == "GET"


@respx.mock
def test_create_posts_review_request_body() -> None:
    client = EigenpalClient(api_key="eg_test", base_url=BASE, max_retries=0)
    route = respx.post(f"{BASE}/v1/automations/{WORKFLOW_ID}/dataset-review-requests").mock(
        return_value=httpx.Response(201, json={"id": REVIEW_ID, "status": "open"})
    )

    client.automations.dataset_review_requests.create(
        WORKFLOW_ID,
        {
            "title": "Q1 GT review",
            "exampleNames": ["invoice-foo", "invoice-bar"],
            "instructions": "Check totals",
            "focusFields": [{"path": "vendor.iban", "reason": "OCR often mangles IBANs"}],
            "ignoredFields": ["currency"],
            "itemNotes": [
                {
                    "exampleName": "invoice-foo",
                    "comment": "Totals drifted",
                    "fields": [{"path": "total", "comment": "off by 0.01"}],
                }
            ],
            "status": "open",
        },
    )

    assert route.called
    body = json.loads(route.calls.last.request.content.decode())
    assert body == {
        "title": "Q1 GT review",
        "exampleNames": ["invoice-foo", "invoice-bar"],
        "instructions": "Check totals",
        "focusFields": [{"path": "vendor.iban", "reason": "OCR often mangles IBANs"}],
        "ignoredFields": ["currency"],
        "itemNotes": [
            {
                "exampleName": "invoice-foo",
                "comment": "Totals drifted",
                "fields": [{"path": "total", "comment": "off by 0.01"}],
            }
        ],
        "status": "open",
    }


@respx.mock
def test_update_patches_request_status() -> None:
    client = EigenpalClient(api_key="eg_test", base_url=BASE, max_retries=0)
    route = respx.patch(
        f"{BASE}/v1/automations/{WORKFLOW_ID}/dataset-review-requests/{REVIEW_ID}"
    ).mock(return_value=httpx.Response(200, json={"id": REVIEW_ID, "status": "closed"}))

    client.automations.dataset_review_requests.update(
        WORKFLOW_ID,
        REVIEW_ID,
        {"status": "closed"},
    )

    assert route.called
    body = json.loads(route.calls.last.request.content.decode())
    assert body == {"status": "closed"}


@respx.mock
def test_update_item_patches_action_payload() -> None:
    client = EigenpalClient(api_key="eg_test", base_url=BASE, max_retries=0)
    route = respx.patch(
        f"{BASE}/v1/automations/{WORKFLOW_ID}/dataset-review-requests/{REVIEW_ID}/items/{ITEM_ID}"
    ).mock(return_value=httpx.Response(200, json={"item": {"id": ITEM_ID, "status": "edited"}}))

    client.automations.dataset_review_requests.update_item(
        WORKFLOW_ID,
        REVIEW_ID,
        ITEM_ID,
        {
            "action": "edit",
            "expected": {"total": 42},
            "comment": "fixed total",
            "expectedUpdatedAt": "2026-01-01T00:00:00.000Z",
        },
    )

    assert route.called
    body = json.loads(route.calls.last.request.content.decode())
    assert body == {
        "action": "edit",
        "expected": {"total": 42},
        "comment": "fixed total",
        "expectedUpdatedAt": "2026-01-01T00:00:00.000Z",
    }


@respx.mock
def test_update_item_field_decision_and_clear() -> None:
    client = EigenpalClient(api_key="eg_test", base_url=BASE, max_retries=0)
    route = respx.patch(
        f"{BASE}/v1/automations/{WORKFLOW_ID}/dataset-review-requests/{REVIEW_ID}/items/{ITEM_ID}"
    ).mock(
        return_value=httpx.Response(
            200, json={"item": {"id": ITEM_ID, "status": "pending", "fieldDecisions": {}}}
        )
    )

    client.automations.dataset_review_requests.update_item(
        WORKFLOW_ID,
        REVIEW_ID,
        ITEM_ID,
        {
            "action": "field-decision",
            "fieldPath": "vendor.iban",
            "decision": "rejected",
            "expectedUpdatedAt": "2026-01-01T00:00:00.000Z",
        },
    )
    client.automations.dataset_review_requests.update_item(
        WORKFLOW_ID,
        REVIEW_ID,
        ITEM_ID,
        {
            "action": "field-decision",
            "fieldPath": "vendor.iban",
            "decision": None,
            "expectedUpdatedAt": "2026-01-01T00:00:01.000Z",
        },
    )

    assert route.call_count == 2
    assert json.loads(route.calls[0].request.content.decode())["decision"] == "rejected"
    assert json.loads(route.calls[1].request.content.decode())["decision"] is None


@respx.mock
def test_events_reads_events_subresource() -> None:
    client = EigenpalClient(api_key="eg_test", base_url=BASE, max_retries=0)
    route = respx.get(
        f"{BASE}/v1/automations/{WORKFLOW_ID}/dataset-review-requests/{REVIEW_ID}/events"
    ).mock(return_value=httpx.Response(200, json={"events": []}))

    client.automations.dataset_review_requests.events(WORKFLOW_ID, REVIEW_ID)

    assert route.called
    assert route.calls.last.request.method == "GET"
