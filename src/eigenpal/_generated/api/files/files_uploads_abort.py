from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.abort_file_upload_response import AbortFileUploadResponse
from ...models.api_error_envelope import ApiErrorEnvelope
from typing import cast



def _get_kwargs(
    upload_id: str,

) -> dict[str, Any]:






    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/files/uploads/{upload_id}".format(upload_id=quote(str(upload_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AbortFileUploadResponse | ApiErrorEnvelope | None:
    if response.status_code == 200:
        response_200 = AbortFileUploadResponse.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AbortFileUploadResponse | ApiErrorEnvelope]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    upload_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[AbortFileUploadResponse | ApiErrorEnvelope]:
    """ Abort file upload

     Abort a pending storage-direct upload and remove its pending object.

    Args:
        upload_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AbortFileUploadResponse | ApiErrorEnvelope]
     """


    kwargs = _get_kwargs(
        upload_id=upload_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    upload_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> AbortFileUploadResponse | ApiErrorEnvelope | None:
    """ Abort file upload

     Abort a pending storage-direct upload and remove its pending object.

    Args:
        upload_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AbortFileUploadResponse | ApiErrorEnvelope
     """


    return sync_detailed(
        upload_id=upload_id,
client=client,

    ).parsed

async def asyncio_detailed(
    upload_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[AbortFileUploadResponse | ApiErrorEnvelope]:
    """ Abort file upload

     Abort a pending storage-direct upload and remove its pending object.

    Args:
        upload_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AbortFileUploadResponse | ApiErrorEnvelope]
     """


    kwargs = _get_kwargs(
        upload_id=upload_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    upload_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> AbortFileUploadResponse | ApiErrorEnvelope | None:
    """ Abort file upload

     Abort a pending storage-direct upload and remove its pending object.

    Args:
        upload_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AbortFileUploadResponse | ApiErrorEnvelope
     """


    return (await asyncio_detailed(
        upload_id=upload_id,
client=client,

    )).parsed
