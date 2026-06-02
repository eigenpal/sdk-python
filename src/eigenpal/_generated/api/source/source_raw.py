from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_error_envelope import ApiErrorEnvelope
from ...models.raw_source_response import RawSourceResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    ref: str | Unset = 'main',
    path: str,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["ref"] = ref

    params["path"] = path


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/source/raw",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ApiErrorEnvelope | RawSourceResponse | None:
    if response.status_code == 200:
        response_200 = RawSourceResponse.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ApiErrorEnvelope | RawSourceResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    ref: str | Unset = 'main',
    path: str,

) -> Response[ApiErrorEnvelope | RawSourceResponse]:
    """ Preview a raw Git source file

     Reads a raw file from the organization Git repository for metadata previews.

    Args:
        ref (str | Unset):  Default: 'main'.
        path (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | RawSourceResponse]
     """


    kwargs = _get_kwargs(
        ref=ref,
path=path,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    ref: str | Unset = 'main',
    path: str,

) -> ApiErrorEnvelope | RawSourceResponse | None:
    """ Preview a raw Git source file

     Reads a raw file from the organization Git repository for metadata previews.

    Args:
        ref (str | Unset):  Default: 'main'.
        path (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | RawSourceResponse
     """


    return sync_detailed(
        client=client,
ref=ref,
path=path,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    ref: str | Unset = 'main',
    path: str,

) -> Response[ApiErrorEnvelope | RawSourceResponse]:
    """ Preview a raw Git source file

     Reads a raw file from the organization Git repository for metadata previews.

    Args:
        ref (str | Unset):  Default: 'main'.
        path (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | RawSourceResponse]
     """


    kwargs = _get_kwargs(
        ref=ref,
path=path,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    ref: str | Unset = 'main',
    path: str,

) -> ApiErrorEnvelope | RawSourceResponse | None:
    """ Preview a raw Git source file

     Reads a raw file from the organization Git repository for metadata previews.

    Args:
        ref (str | Unset):  Default: 'main'.
        path (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | RawSourceResponse
     """


    return (await asyncio_detailed(
        client=client,
ref=ref,
path=path,

    )).parsed
