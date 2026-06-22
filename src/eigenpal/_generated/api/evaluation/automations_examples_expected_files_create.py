from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_error_envelope import ApiErrorEnvelope
from ...models.dataset_example_expected_file_upload_request import DatasetExampleExpectedFileUploadRequest
from ...models.dataset_example_expected_file_upload_response import DatasetExampleExpectedFileUploadResponse
from typing import cast



def _get_kwargs(
    id: str,
    example_id: str,
    *,
    body: DatasetExampleExpectedFileUploadRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}






    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/automations/{id}/examples/{example_id}/expected".format(id=quote(str(id), safe=""),example_id=quote(str(example_id), safe=""),),
    }

    _kwargs["files"] = body.to_multipart()



    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ApiErrorEnvelope | DatasetExampleExpectedFileUploadResponse | None:
    if response.status_code == 201:
        response_201 = DatasetExampleExpectedFileUploadResponse.from_dict(response.json())



        return response_201

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ApiErrorEnvelope | DatasetExampleExpectedFileUploadResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    example_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DatasetExampleExpectedFileUploadRequest,

) -> Response[ApiErrorEnvelope | DatasetExampleExpectedFileUploadResponse]:
    """ Upload expected files

     Upload one or more files into the expected folder for an automation dataset example. Use `$file`
    references such as `expected/result.pdf` from expected JSON to compare file outputs.

    Args:
        id (str): Automation id or typed alias.
        example_id (str): Dataset example id.
        body (DatasetExampleExpectedFileUploadRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | DatasetExampleExpectedFileUploadResponse]
     """


    kwargs = _get_kwargs(
        id=id,
example_id=example_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    example_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DatasetExampleExpectedFileUploadRequest,

) -> ApiErrorEnvelope | DatasetExampleExpectedFileUploadResponse | None:
    """ Upload expected files

     Upload one or more files into the expected folder for an automation dataset example. Use `$file`
    references such as `expected/result.pdf` from expected JSON to compare file outputs.

    Args:
        id (str): Automation id or typed alias.
        example_id (str): Dataset example id.
        body (DatasetExampleExpectedFileUploadRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | DatasetExampleExpectedFileUploadResponse
     """


    return sync_detailed(
        id=id,
example_id=example_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    id: str,
    example_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DatasetExampleExpectedFileUploadRequest,

) -> Response[ApiErrorEnvelope | DatasetExampleExpectedFileUploadResponse]:
    """ Upload expected files

     Upload one or more files into the expected folder for an automation dataset example. Use `$file`
    references such as `expected/result.pdf` from expected JSON to compare file outputs.

    Args:
        id (str): Automation id or typed alias.
        example_id (str): Dataset example id.
        body (DatasetExampleExpectedFileUploadRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | DatasetExampleExpectedFileUploadResponse]
     """


    kwargs = _get_kwargs(
        id=id,
example_id=example_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    example_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DatasetExampleExpectedFileUploadRequest,

) -> ApiErrorEnvelope | DatasetExampleExpectedFileUploadResponse | None:
    """ Upload expected files

     Upload one or more files into the expected folder for an automation dataset example. Use `$file`
    references such as `expected/result.pdf` from expected JSON to compare file outputs.

    Args:
        id (str): Automation id or typed alias.
        example_id (str): Dataset example id.
        body (DatasetExampleExpectedFileUploadRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | DatasetExampleExpectedFileUploadResponse
     """


    return (await asyncio_detailed(
        id=id,
example_id=example_id,
client=client,
body=body,

    )).parsed
