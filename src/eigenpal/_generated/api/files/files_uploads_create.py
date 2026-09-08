from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_error_envelope import ApiErrorEnvelope
from ...models.create_file_upload_session_request import CreateFileUploadSessionRequest
from ...models.multipart_file_upload_fallback import MultipartFileUploadFallback
from ...models.presigned_file_upload_session import PresignedFileUploadSession
from ...models.presigned_multipart_file_upload_session import PresignedMultipartFileUploadSession
from typing import cast



def _get_kwargs(
    *,
    body: CreateFileUploadSessionRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}






    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/files/uploads",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ApiErrorEnvelope | MultipartFileUploadFallback | PresignedFileUploadSession | PresignedMultipartFileUploadSession | None:
    if response.status_code == 200:
        def _parse_response_200(data: object) -> MultipartFileUploadFallback | PresignedFileUploadSession | PresignedMultipartFileUploadSession:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = PresignedFileUploadSession.from_dict(data)



                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_1 = PresignedMultipartFileUploadSession.from_dict(data)



                return response_200_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_2 = MultipartFileUploadFallback.from_dict(data)



            return response_200_type_2

        response_200 = _parse_response_200(response.json())

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ApiErrorEnvelope | MultipartFileUploadFallback | PresignedFileUploadSession | PresignedMultipartFileUploadSession]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateFileUploadSessionRequest,

) -> Response[ApiErrorEnvelope | MultipartFileUploadFallback | PresignedFileUploadSession | PresignedMultipartFileUploadSession]:
    """ Prepare file upload

     Negotiate HTTP multipart for small bodies, a short-lived signed PUT under the single-object ceiling,
    or storage-direct multipart (presigned-multipart) for larger files when storage supports MPU. The
    response transport is authoritative; clients must not guess from file size alone.

    Args:
        body (CreateFileUploadSessionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | MultipartFileUploadFallback | PresignedFileUploadSession | PresignedMultipartFileUploadSession]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body: CreateFileUploadSessionRequest,

) -> ApiErrorEnvelope | MultipartFileUploadFallback | PresignedFileUploadSession | PresignedMultipartFileUploadSession | None:
    """ Prepare file upload

     Negotiate HTTP multipart for small bodies, a short-lived signed PUT under the single-object ceiling,
    or storage-direct multipart (presigned-multipart) for larger files when storage supports MPU. The
    response transport is authoritative; clients must not guess from file size alone.

    Args:
        body (CreateFileUploadSessionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | MultipartFileUploadFallback | PresignedFileUploadSession | PresignedMultipartFileUploadSession
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateFileUploadSessionRequest,

) -> Response[ApiErrorEnvelope | MultipartFileUploadFallback | PresignedFileUploadSession | PresignedMultipartFileUploadSession]:
    """ Prepare file upload

     Negotiate HTTP multipart for small bodies, a short-lived signed PUT under the single-object ceiling,
    or storage-direct multipart (presigned-multipart) for larger files when storage supports MPU. The
    response transport is authoritative; clients must not guess from file size alone.

    Args:
        body (CreateFileUploadSessionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | MultipartFileUploadFallback | PresignedFileUploadSession | PresignedMultipartFileUploadSession]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateFileUploadSessionRequest,

) -> ApiErrorEnvelope | MultipartFileUploadFallback | PresignedFileUploadSession | PresignedMultipartFileUploadSession | None:
    """ Prepare file upload

     Negotiate HTTP multipart for small bodies, a short-lived signed PUT under the single-object ceiling,
    or storage-direct multipart (presigned-multipart) for larger files when storage supports MPU. The
    response transport is authoritative; clients must not guess from file size alone.

    Args:
        body (CreateFileUploadSessionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | MultipartFileUploadFallback | PresignedFileUploadSession | PresignedMultipartFileUploadSession
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
