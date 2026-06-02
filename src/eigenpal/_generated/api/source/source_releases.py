from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_error_envelope import ApiErrorEnvelope
from ...models.source_releases_response import SourceReleasesResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    package_path: str,
    version: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["packagePath"] = package_path

    params["version"] = version


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/source/releases",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ApiErrorEnvelope | SourceReleasesResponse | None:
    if response.status_code == 200:
        response_200 = SourceReleasesResponse.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ApiErrorEnvelope | SourceReleasesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    package_path: str,
    version: str | Unset = UNSET,

) -> Response[ApiErrorEnvelope | SourceReleasesResponse]:
    """ List Git source package releases

     Lists package-scoped Git release tags, or returns one exact version when requested.

    Args:
        package_path (str):
        version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | SourceReleasesResponse]
     """


    kwargs = _get_kwargs(
        package_path=package_path,
version=version,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    package_path: str,
    version: str | Unset = UNSET,

) -> ApiErrorEnvelope | SourceReleasesResponse | None:
    """ List Git source package releases

     Lists package-scoped Git release tags, or returns one exact version when requested.

    Args:
        package_path (str):
        version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | SourceReleasesResponse
     """


    return sync_detailed(
        client=client,
package_path=package_path,
version=version,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    package_path: str,
    version: str | Unset = UNSET,

) -> Response[ApiErrorEnvelope | SourceReleasesResponse]:
    """ List Git source package releases

     Lists package-scoped Git release tags, or returns one exact version when requested.

    Args:
        package_path (str):
        version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | SourceReleasesResponse]
     """


    kwargs = _get_kwargs(
        package_path=package_path,
version=version,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    package_path: str,
    version: str | Unset = UNSET,

) -> ApiErrorEnvelope | SourceReleasesResponse | None:
    """ List Git source package releases

     Lists package-scoped Git release tags, or returns one exact version when requested.

    Args:
        package_path (str):
        version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | SourceReleasesResponse
     """


    return (await asyncio_detailed(
        client=client,
package_path=package_path,
version=version,

    )).parsed
