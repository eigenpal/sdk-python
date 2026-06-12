from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET, Unset
from ... import errors

from ...models.api_error_envelope import ApiErrorEnvelope
from ...models.runs_expected_create_files_body import RunsExpectedCreateFilesBody
from ...models.runs_expected_create_json_body import RunsExpectedCreateJsonBody
from ...models.runs_expected_create_response_201 import RunsExpectedCreateResponse201
from typing import cast



def _get_kwargs(
    id: str,
    *,
    body:    RunsExpectedCreateJsonBody  |     RunsExpectedCreateFilesBody  | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}






    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/runs/{id}/expected".format(id=quote(str(id), safe=""),),
    }

    if isinstance(body, RunsExpectedCreateJsonBody):
        _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "application/json"
    if isinstance(body, RunsExpectedCreateFilesBody):
        _kwargs["files"] = body.to_multipart()


        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ApiErrorEnvelope | RunsExpectedCreateResponse201 | None:
    if response.status_code == 201:
        response_201 = RunsExpectedCreateResponse201.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ApiErrorEnvelope | RunsExpectedCreateResponse201]:
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
    body:    RunsExpectedCreateJsonBody  |     RunsExpectedCreateFilesBody  | Unset = UNSET,

) -> Response[ApiErrorEnvelope | RunsExpectedCreateResponse201]:
    """ Create or update expected artifacts

    Args:
        id (str):
        body (RunsExpectedCreateJsonBody):
        body (RunsExpectedCreateFilesBody): multipart/form-data

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | RunsExpectedCreateResponse201]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body:    RunsExpectedCreateJsonBody  |     RunsExpectedCreateFilesBody  | Unset = UNSET,

) -> ApiErrorEnvelope | RunsExpectedCreateResponse201 | None:
    """ Create or update expected artifacts

    Args:
        id (str):
        body (RunsExpectedCreateJsonBody):
        body (RunsExpectedCreateFilesBody): multipart/form-data

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | RunsExpectedCreateResponse201
     """


    return sync_detailed(
        id=id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body:    RunsExpectedCreateJsonBody  |     RunsExpectedCreateFilesBody  | Unset = UNSET,

) -> Response[ApiErrorEnvelope | RunsExpectedCreateResponse201]:
    """ Create or update expected artifacts

    Args:
        id (str):
        body (RunsExpectedCreateJsonBody):
        body (RunsExpectedCreateFilesBody): multipart/form-data

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | RunsExpectedCreateResponse201]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body:    RunsExpectedCreateJsonBody  |     RunsExpectedCreateFilesBody  | Unset = UNSET,

) -> ApiErrorEnvelope | RunsExpectedCreateResponse201 | None:
    """ Create or update expected artifacts

    Args:
        id (str):
        body (RunsExpectedCreateJsonBody):
        body (RunsExpectedCreateFilesBody): multipart/form-data

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | RunsExpectedCreateResponse201
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
