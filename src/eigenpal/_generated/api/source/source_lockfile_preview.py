from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_error_envelope import ApiErrorEnvelope
from ...models.source_lockfile_response import SourceLockfileResponse
from typing import cast



def _get_kwargs(
    *,
    package_ref: str,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["packageRef"] = package_ref


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/source/lockfile",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ApiErrorEnvelope | SourceLockfileResponse | None:
    if response.status_code == 200:
        response_200 = SourceLockfileResponse.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ApiErrorEnvelope | SourceLockfileResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    package_ref: str,

) -> Response[ApiErrorEnvelope | SourceLockfileResponse]:
    """ Preview a source lockfile

     Resolves a package ref and returns the would-be eigenpal.lock without enqueueing or writing runtime
    artifacts.

    Args:
        package_ref (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | SourceLockfileResponse]
     """


    kwargs = _get_kwargs(
        package_ref=package_ref,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    package_ref: str,

) -> ApiErrorEnvelope | SourceLockfileResponse | None:
    """ Preview a source lockfile

     Resolves a package ref and returns the would-be eigenpal.lock without enqueueing or writing runtime
    artifacts.

    Args:
        package_ref (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | SourceLockfileResponse
     """


    return sync_detailed(
        client=client,
package_ref=package_ref,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    package_ref: str,

) -> Response[ApiErrorEnvelope | SourceLockfileResponse]:
    """ Preview a source lockfile

     Resolves a package ref and returns the would-be eigenpal.lock without enqueueing or writing runtime
    artifacts.

    Args:
        package_ref (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | SourceLockfileResponse]
     """


    kwargs = _get_kwargs(
        package_ref=package_ref,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    package_ref: str,

) -> ApiErrorEnvelope | SourceLockfileResponse | None:
    """ Preview a source lockfile

     Resolves a package ref and returns the would-be eigenpal.lock without enqueueing or writing runtime
    artifacts.

    Args:
        package_ref (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | SourceLockfileResponse
     """


    return (await asyncio_detailed(
        client=client,
package_ref=package_ref,

    )).parsed
