from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_error_envelope import ApiErrorEnvelope
from ...models.automations_list_type import AutomationsListType
from ...models.list_automations_response import ListAutomationsResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    search: str | Unset = UNSET,
    type_: AutomationsListType | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,

) -> dict[str, Any]:




    params: dict[str, Any] = {}

    params["search"] = search

    json_type_: str | Unset = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_.value

    params["type"] = json_type_

    params["limit"] = limit

    params["offset"] = offset


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/automations",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ApiErrorEnvelope | ListAutomationsResponse | None:
    if response.status_code == 200:
        response_200 = ListAutomationsResponse.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ApiErrorEnvelope | ListAutomationsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    search: str | Unset = UNSET,
    type_: AutomationsListType | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,

) -> Response[ApiErrorEnvelope | ListAutomationsResponse]:
    """ List automations

     List runnable workflow and agent automations in one collection.

    Args:
        search (str | Unset): Substring match against slug, name, or description
        type_ (AutomationsListType | Unset): Filter by implementation type
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | ListAutomationsResponse]
     """


    kwargs = _get_kwargs(
        search=search,
type_=type_,
limit=limit,
offset=offset,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    search: str | Unset = UNSET,
    type_: AutomationsListType | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,

) -> ApiErrorEnvelope | ListAutomationsResponse | None:
    """ List automations

     List runnable workflow and agent automations in one collection.

    Args:
        search (str | Unset): Substring match against slug, name, or description
        type_ (AutomationsListType | Unset): Filter by implementation type
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | ListAutomationsResponse
     """


    return sync_detailed(
        client=client,
search=search,
type_=type_,
limit=limit,
offset=offset,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    search: str | Unset = UNSET,
    type_: AutomationsListType | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,

) -> Response[ApiErrorEnvelope | ListAutomationsResponse]:
    """ List automations

     List runnable workflow and agent automations in one collection.

    Args:
        search (str | Unset): Substring match against slug, name, or description
        type_ (AutomationsListType | Unset): Filter by implementation type
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | ListAutomationsResponse]
     """


    kwargs = _get_kwargs(
        search=search,
type_=type_,
limit=limit,
offset=offset,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    search: str | Unset = UNSET,
    type_: AutomationsListType | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,

) -> ApiErrorEnvelope | ListAutomationsResponse | None:
    """ List automations

     List runnable workflow and agent automations in one collection.

    Args:
        search (str | Unset): Substring match against slug, name, or description
        type_ (AutomationsListType | Unset): Filter by implementation type
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | ListAutomationsResponse
     """


    return (await asyncio_detailed(
        client=client,
search=search,
type_=type_,
limit=limit,
offset=offset,

    )).parsed
