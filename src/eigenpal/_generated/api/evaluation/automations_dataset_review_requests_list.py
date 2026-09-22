from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_error_envelope import ApiErrorEnvelope
from ...models.dataset_review_request_list import DatasetReviewRequestList
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: str,
    *,
    status: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,

) -> dict[str, Any]:




    params: dict[str, Any] = {}

    params["status"] = status

    params["limit"] = limit

    params["offset"] = offset


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/automations/{id}/dataset-review-requests".format(id=quote(str(id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ApiErrorEnvelope | DatasetReviewRequestList | None:
    if response.status_code == 200:
        response_200 = DatasetReviewRequestList.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ApiErrorEnvelope | DatasetReviewRequestList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    status: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,

) -> Response[ApiErrorEnvelope | DatasetReviewRequestList]:
    """ List dataset review requests

     List dataset review requests for one automation, including per-request progress.

    Args:
        id (str): Automation id or typed alias, such as `workflows.slug` or `agents.slug`.
        status (str | Unset): Optional comma-separated review statuses to filter by.
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | DatasetReviewRequestList]
     """


    kwargs = _get_kwargs(
        id=id,
status=status,
limit=limit,
offset=offset,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    status: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,

) -> ApiErrorEnvelope | DatasetReviewRequestList | None:
    """ List dataset review requests

     List dataset review requests for one automation, including per-request progress.

    Args:
        id (str): Automation id or typed alias, such as `workflows.slug` or `agents.slug`.
        status (str | Unset): Optional comma-separated review statuses to filter by.
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | DatasetReviewRequestList
     """


    return sync_detailed(
        id=id,
client=client,
status=status,
limit=limit,
offset=offset,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    status: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,

) -> Response[ApiErrorEnvelope | DatasetReviewRequestList]:
    """ List dataset review requests

     List dataset review requests for one automation, including per-request progress.

    Args:
        id (str): Automation id or typed alias, such as `workflows.slug` or `agents.slug`.
        status (str | Unset): Optional comma-separated review statuses to filter by.
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | DatasetReviewRequestList]
     """


    kwargs = _get_kwargs(
        id=id,
status=status,
limit=limit,
offset=offset,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    status: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,

) -> ApiErrorEnvelope | DatasetReviewRequestList | None:
    """ List dataset review requests

     List dataset review requests for one automation, including per-request progress.

    Args:
        id (str): Automation id or typed alias, such as `workflows.slug` or `agents.slug`.
        status (str | Unset): Optional comma-separated review statuses to filter by.
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | DatasetReviewRequestList
     """


    return (await asyncio_detailed(
        id=id,
client=client,
status=status,
limit=limit,
offset=offset,

    )).parsed
