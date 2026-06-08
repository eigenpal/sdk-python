from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_error_envelope import ApiErrorEnvelope
from ...models.run_envelope import RunEnvelope
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: str,
    *,
    include: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["include"] = include


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/runs/{id}".format(id=quote(str(id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ApiErrorEnvelope | RunEnvelope | None:
    if response.status_code == 200:
        response_200 = RunEnvelope.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ApiErrorEnvelope | RunEnvelope]:
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
    include: str | Unset = UNSET,

) -> Response[ApiErrorEnvelope | RunEnvelope]:
    """ Get run

     Returns a run summary by default. Pass include=detail for the rich type-specific workflow or agent
    run payload.

    Args:
        id (str): Run id
        include (str | Unset): Comma-separated sections. Include `detail` for rich payload.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | RunEnvelope]
     """


    kwargs = _get_kwargs(
        id=id,
include=include,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    include: str | Unset = UNSET,

) -> ApiErrorEnvelope | RunEnvelope | None:
    """ Get run

     Returns a run summary by default. Pass include=detail for the rich type-specific workflow or agent
    run payload.

    Args:
        id (str): Run id
        include (str | Unset): Comma-separated sections. Include `detail` for rich payload.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | RunEnvelope
     """


    return sync_detailed(
        id=id,
client=client,
include=include,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    include: str | Unset = UNSET,

) -> Response[ApiErrorEnvelope | RunEnvelope]:
    """ Get run

     Returns a run summary by default. Pass include=detail for the rich type-specific workflow or agent
    run payload.

    Args:
        id (str): Run id
        include (str | Unset): Comma-separated sections. Include `detail` for rich payload.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | RunEnvelope]
     """


    kwargs = _get_kwargs(
        id=id,
include=include,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    include: str | Unset = UNSET,

) -> ApiErrorEnvelope | RunEnvelope | None:
    """ Get run

     Returns a run summary by default. Pass include=detail for the rich type-specific workflow or agent
    run payload.

    Args:
        id (str): Run id
        include (str | Unset): Comma-separated sections. Include `detail` for rich payload.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | RunEnvelope
     """


    return (await asyncio_detailed(
        id=id,
client=client,
include=include,

    )).parsed
