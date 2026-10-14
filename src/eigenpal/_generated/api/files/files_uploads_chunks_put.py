from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.accept_http_chunked_upload_chunk_response import AcceptHttpChunkedUploadChunkResponse
from ...models.api_error_envelope import ApiErrorEnvelope
from ...types import File, FileTypes
from io import BytesIO
from typing import cast



def _get_kwargs(
    upload_id: str,
    chunk_index: str,
    *,
    body: File,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}






    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/files/uploads/{upload_id}/chunks/{chunk_index}".format(upload_id=quote(str(upload_id), safe=""),chunk_index=quote(str(chunk_index), safe=""),),
    }

    _kwargs["content"] = body.payload
    headers["Content-Type"] = "application/octet-stream"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AcceptHttpChunkedUploadChunkResponse | ApiErrorEnvelope | None:
    if response.status_code == 200:
        response_200 = AcceptHttpChunkedUploadChunkResponse.from_dict(response.json())



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

    if response.status_code == 409:
        response_409 = ApiErrorEnvelope.from_dict(response.json())



        return response_409

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AcceptHttpChunkedUploadChunkResponse | ApiErrorEnvelope]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    upload_id: str,
    chunk_index: str,
    *,
    client: AuthenticatedClient | Client,
    body: File,

) -> Response[AcceptHttpChunkedUploadChunkResponse | ApiErrorEnvelope]:
    """ Upload one file chunk

     Accept one raw body for an http-chunked session. Each chunk must match the negotiated size; chunks
    are accepted in order. Idempotent overwrite of the current index is allowed.

    Args:
        upload_id (str):
        chunk_index (str):
        body (File): Raw chunk bytes

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AcceptHttpChunkedUploadChunkResponse | ApiErrorEnvelope]
     """


    kwargs = _get_kwargs(
        upload_id=upload_id,
chunk_index=chunk_index,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    upload_id: str,
    chunk_index: str,
    *,
    client: AuthenticatedClient | Client,
    body: File,

) -> AcceptHttpChunkedUploadChunkResponse | ApiErrorEnvelope | None:
    """ Upload one file chunk

     Accept one raw body for an http-chunked session. Each chunk must match the negotiated size; chunks
    are accepted in order. Idempotent overwrite of the current index is allowed.

    Args:
        upload_id (str):
        chunk_index (str):
        body (File): Raw chunk bytes

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AcceptHttpChunkedUploadChunkResponse | ApiErrorEnvelope
     """


    return sync_detailed(
        upload_id=upload_id,
chunk_index=chunk_index,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    upload_id: str,
    chunk_index: str,
    *,
    client: AuthenticatedClient | Client,
    body: File,

) -> Response[AcceptHttpChunkedUploadChunkResponse | ApiErrorEnvelope]:
    """ Upload one file chunk

     Accept one raw body for an http-chunked session. Each chunk must match the negotiated size; chunks
    are accepted in order. Idempotent overwrite of the current index is allowed.

    Args:
        upload_id (str):
        chunk_index (str):
        body (File): Raw chunk bytes

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AcceptHttpChunkedUploadChunkResponse | ApiErrorEnvelope]
     """


    kwargs = _get_kwargs(
        upload_id=upload_id,
chunk_index=chunk_index,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    upload_id: str,
    chunk_index: str,
    *,
    client: AuthenticatedClient | Client,
    body: File,

) -> AcceptHttpChunkedUploadChunkResponse | ApiErrorEnvelope | None:
    """ Upload one file chunk

     Accept one raw body for an http-chunked session. Each chunk must match the negotiated size; chunks
    are accepted in order. Idempotent overwrite of the current index is allowed.

    Args:
        upload_id (str):
        chunk_index (str):
        body (File): Raw chunk bytes

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AcceptHttpChunkedUploadChunkResponse | ApiErrorEnvelope
     """


    return (await asyncio_detailed(
        upload_id=upload_id,
chunk_index=chunk_index,
client=client,
body=body,

    )).parsed
