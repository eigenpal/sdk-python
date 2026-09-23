from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET, Unset
from ... import errors

from ...models.api_error_envelope import ApiErrorEnvelope
from ...models.dataset_review_item_response import DatasetReviewItemResponse
from ...models.edit_dataset_review_item_file import EditDatasetReviewItemFile
from ...models.update_dataset_review_item import UpdateDatasetReviewItem
from typing import cast



def _get_kwargs(
    id: str,
    review_id: str,
    item_id: str,
    *,
    body:    UpdateDatasetReviewItem  |     EditDatasetReviewItemFile  | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}






    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/automations/{id}/dataset-review-requests/{review_id}/items/{item_id}".format(id=quote(str(id), safe=""),review_id=quote(str(review_id), safe=""),item_id=quote(str(item_id), safe=""),),
    }

    if isinstance(body, UpdateDatasetReviewItem):
        _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "application/json"
    if isinstance(body, EditDatasetReviewItemFile):
        _kwargs["files"] = body.to_multipart()


        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ApiErrorEnvelope | DatasetReviewItemResponse | None:
    if response.status_code == 200:
        response_200 = DatasetReviewItemResponse.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = ApiErrorEnvelope.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = ApiErrorEnvelope.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = ApiErrorEnvelope.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = ApiErrorEnvelope.from_dict(response.json())



        return response_404

    if response.status_code == 413:
        response_413 = ApiErrorEnvelope.from_dict(response.json())



        return response_413

    if response.status_code == 429:
        response_429 = ApiErrorEnvelope.from_dict(response.json())



        return response_429

    if response.status_code == 500:
        response_500 = ApiErrorEnvelope.from_dict(response.json())



        return response_500

    if response.status_code == 503:
        response_503 = ApiErrorEnvelope.from_dict(response.json())



        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ApiErrorEnvelope | DatasetReviewItemResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    review_id: str,
    item_id: str,
    *,
    client: AuthenticatedClient | Client,
    body:    UpdateDatasetReviewItem  |     EditDatasetReviewItemFile  | Unset = UNSET,

) -> Response[ApiErrorEnvelope | DatasetReviewItemResponse]:
    """ Update dataset review item

     Approve, edit, reject, reopen, comment, or record a field-decision or file-decision on one review
    item while the parent request is draft, open, or paused. Pass `expectedUpdatedAt` from the item the
    client last observed. Pass `fieldPath` with `action: comment` or `action: field-decision`,
    `filePath` with `action: file-decision`. `action: edit-file` is multipart-only: send `file` bytes
    with `filePath` (correct an existing expected file) or `newPath` (upload a brand-new expected file)
    plus `expectedUpdatedAt`.

    Args:
        id (str): Automation id or typed alias.
        review_id (str): Dataset review request id.
        item_id (str): Dataset review item id.
        body (UpdateDatasetReviewItem):
        body (EditDatasetReviewItemFile):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | DatasetReviewItemResponse]
     """


    kwargs = _get_kwargs(
        id=id,
review_id=review_id,
item_id=item_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    review_id: str,
    item_id: str,
    *,
    client: AuthenticatedClient | Client,
    body:    UpdateDatasetReviewItem  |     EditDatasetReviewItemFile  | Unset = UNSET,

) -> ApiErrorEnvelope | DatasetReviewItemResponse | None:
    """ Update dataset review item

     Approve, edit, reject, reopen, comment, or record a field-decision or file-decision on one review
    item while the parent request is draft, open, or paused. Pass `expectedUpdatedAt` from the item the
    client last observed. Pass `fieldPath` with `action: comment` or `action: field-decision`,
    `filePath` with `action: file-decision`. `action: edit-file` is multipart-only: send `file` bytes
    with `filePath` (correct an existing expected file) or `newPath` (upload a brand-new expected file)
    plus `expectedUpdatedAt`.

    Args:
        id (str): Automation id or typed alias.
        review_id (str): Dataset review request id.
        item_id (str): Dataset review item id.
        body (UpdateDatasetReviewItem):
        body (EditDatasetReviewItemFile):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | DatasetReviewItemResponse
     """


    return sync_detailed(
        id=id,
review_id=review_id,
item_id=item_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    id: str,
    review_id: str,
    item_id: str,
    *,
    client: AuthenticatedClient | Client,
    body:    UpdateDatasetReviewItem  |     EditDatasetReviewItemFile  | Unset = UNSET,

) -> Response[ApiErrorEnvelope | DatasetReviewItemResponse]:
    """ Update dataset review item

     Approve, edit, reject, reopen, comment, or record a field-decision or file-decision on one review
    item while the parent request is draft, open, or paused. Pass `expectedUpdatedAt` from the item the
    client last observed. Pass `fieldPath` with `action: comment` or `action: field-decision`,
    `filePath` with `action: file-decision`. `action: edit-file` is multipart-only: send `file` bytes
    with `filePath` (correct an existing expected file) or `newPath` (upload a brand-new expected file)
    plus `expectedUpdatedAt`.

    Args:
        id (str): Automation id or typed alias.
        review_id (str): Dataset review request id.
        item_id (str): Dataset review item id.
        body (UpdateDatasetReviewItem):
        body (EditDatasetReviewItemFile):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | DatasetReviewItemResponse]
     """


    kwargs = _get_kwargs(
        id=id,
review_id=review_id,
item_id=item_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    review_id: str,
    item_id: str,
    *,
    client: AuthenticatedClient | Client,
    body:    UpdateDatasetReviewItem  |     EditDatasetReviewItemFile  | Unset = UNSET,

) -> ApiErrorEnvelope | DatasetReviewItemResponse | None:
    """ Update dataset review item

     Approve, edit, reject, reopen, comment, or record a field-decision or file-decision on one review
    item while the parent request is draft, open, or paused. Pass `expectedUpdatedAt` from the item the
    client last observed. Pass `fieldPath` with `action: comment` or `action: field-decision`,
    `filePath` with `action: file-decision`. `action: edit-file` is multipart-only: send `file` bytes
    with `filePath` (correct an existing expected file) or `newPath` (upload a brand-new expected file)
    plus `expectedUpdatedAt`.

    Args:
        id (str): Automation id or typed alias.
        review_id (str): Dataset review request id.
        item_id (str): Dataset review item id.
        body (UpdateDatasetReviewItem):
        body (EditDatasetReviewItemFile):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | DatasetReviewItemResponse
     """


    return (await asyncio_detailed(
        id=id,
review_id=review_id,
item_id=item_id,
client=client,
body=body,

    )).parsed
