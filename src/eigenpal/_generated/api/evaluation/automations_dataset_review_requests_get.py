from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_error_envelope import ApiErrorEnvelope
from ...models.dataset_review_detail import DatasetReviewDetail
from typing import cast



def _get_kwargs(
    id: str,
    review_id: str,

) -> dict[str, Any]:






    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/automations/{id}/dataset-review-requests/{review_id}".format(id=quote(str(id), safe=""),review_id=quote(str(review_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ApiErrorEnvelope | DatasetReviewDetail | None:
    if response.status_code == 200:
        response_200 = DatasetReviewDetail.from_dict(response.json())



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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ApiErrorEnvelope | DatasetReviewDetail]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    review_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[ApiErrorEnvelope | DatasetReviewDetail]:
    """ Get dataset review request

     Fetch one dataset review request with snapshotted items, progress, focus fields, ignored fields, and
    events.

    Args:
        id (str): Automation id or typed alias.
        review_id (str): Dataset review request id.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | DatasetReviewDetail]
     """


    kwargs = _get_kwargs(
        id=id,
review_id=review_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    review_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> ApiErrorEnvelope | DatasetReviewDetail | None:
    """ Get dataset review request

     Fetch one dataset review request with snapshotted items, progress, focus fields, ignored fields, and
    events.

    Args:
        id (str): Automation id or typed alias.
        review_id (str): Dataset review request id.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | DatasetReviewDetail
     """


    return sync_detailed(
        id=id,
review_id=review_id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: str,
    review_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[ApiErrorEnvelope | DatasetReviewDetail]:
    """ Get dataset review request

     Fetch one dataset review request with snapshotted items, progress, focus fields, ignored fields, and
    events.

    Args:
        id (str): Automation id or typed alias.
        review_id (str): Dataset review request id.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | DatasetReviewDetail]
     """


    kwargs = _get_kwargs(
        id=id,
review_id=review_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    review_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> ApiErrorEnvelope | DatasetReviewDetail | None:
    """ Get dataset review request

     Fetch one dataset review request with snapshotted items, progress, focus fields, ignored fields, and
    events.

    Args:
        id (str): Automation id or typed alias.
        review_id (str): Dataset review request id.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | DatasetReviewDetail
     """


    return (await asyncio_detailed(
        id=id,
review_id=review_id,
client=client,

    )).parsed
