from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_error_envelope import ApiErrorEnvelope
from ...models.human_review_list_response import HumanReviewListResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    automation_id: str | Unset = UNSET,
    waiting_before: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,

) -> dict[str, Any]:




    params: dict[str, Any] = {}

    params["automationId"] = automation_id

    params["waitingBefore"] = waiting_before

    params["cursor"] = cursor

    params["limit"] = limit


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/human-reviews",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ApiErrorEnvelope | HumanReviewListResponse | None:
    if response.status_code == 200:
        response_200 = HumanReviewListResponse.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ApiErrorEnvelope | HumanReviewListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    automation_id: str | Unset = UNSET,
    waiting_before: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,

) -> Response[ApiErrorEnvelope | HumanReviewListResponse]:
    """ List pending human review tasks

     Cursor-paginated queue of pending human-review tasks for the tenant, oldest first.

    Args:
        automation_id (str | Unset):
        waiting_before (str | Unset):
        cursor (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | HumanReviewListResponse]
     """


    kwargs = _get_kwargs(
        automation_id=automation_id,
waiting_before=waiting_before,
cursor=cursor,
limit=limit,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    automation_id: str | Unset = UNSET,
    waiting_before: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,

) -> ApiErrorEnvelope | HumanReviewListResponse | None:
    """ List pending human review tasks

     Cursor-paginated queue of pending human-review tasks for the tenant, oldest first.

    Args:
        automation_id (str | Unset):
        waiting_before (str | Unset):
        cursor (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | HumanReviewListResponse
     """


    return sync_detailed(
        client=client,
automation_id=automation_id,
waiting_before=waiting_before,
cursor=cursor,
limit=limit,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    automation_id: str | Unset = UNSET,
    waiting_before: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,

) -> Response[ApiErrorEnvelope | HumanReviewListResponse]:
    """ List pending human review tasks

     Cursor-paginated queue of pending human-review tasks for the tenant, oldest first.

    Args:
        automation_id (str | Unset):
        waiting_before (str | Unset):
        cursor (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | HumanReviewListResponse]
     """


    kwargs = _get_kwargs(
        automation_id=automation_id,
waiting_before=waiting_before,
cursor=cursor,
limit=limit,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    automation_id: str | Unset = UNSET,
    waiting_before: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,

) -> ApiErrorEnvelope | HumanReviewListResponse | None:
    """ List pending human review tasks

     Cursor-paginated queue of pending human-review tasks for the tenant, oldest first.

    Args:
        automation_id (str | Unset):
        waiting_before (str | Unset):
        cursor (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | HumanReviewListResponse
     """


    return (await asyncio_detailed(
        client=client,
automation_id=automation_id,
waiting_before=waiting_before,
cursor=cursor,
limit=limit,

    )).parsed
