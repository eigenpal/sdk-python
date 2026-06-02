from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_error_envelope import ApiErrorEnvelope
from ...models.rename_expected_file_body import RenameExpectedFileBody
from ...models.rename_expected_file_response import RenameExpectedFileResponse
from typing import cast



def _get_kwargs(
    run_id: str,
    filename: str,
    *,
    body: RenameExpectedFileBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v1/agents/runs/{run_id}/expected/{filename}".format(run_id=quote(str(run_id), safe=""),filename=quote(str(filename), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ApiErrorEnvelope | RenameExpectedFileResponse | None:
    if response.status_code == 200:
        response_200 = RenameExpectedFileResponse.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ApiErrorEnvelope | RenameExpectedFileResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    run_id: str,
    filename: str,
    *,
    client: AuthenticatedClient | Client,
    body: RenameExpectedFileBody,

) -> Response[ApiErrorEnvelope | RenameExpectedFileResponse]:
    """ Rename an expected file

     Renames one expected file attached to an agent run.

    Args:
        run_id (str): Run id
        filename (str): Expected artifact path
        body (RenameExpectedFileBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | RenameExpectedFileResponse]
     """


    kwargs = _get_kwargs(
        run_id=run_id,
filename=filename,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    run_id: str,
    filename: str,
    *,
    client: AuthenticatedClient | Client,
    body: RenameExpectedFileBody,

) -> ApiErrorEnvelope | RenameExpectedFileResponse | None:
    """ Rename an expected file

     Renames one expected file attached to an agent run.

    Args:
        run_id (str): Run id
        filename (str): Expected artifact path
        body (RenameExpectedFileBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | RenameExpectedFileResponse
     """


    return sync_detailed(
        run_id=run_id,
filename=filename,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    run_id: str,
    filename: str,
    *,
    client: AuthenticatedClient | Client,
    body: RenameExpectedFileBody,

) -> Response[ApiErrorEnvelope | RenameExpectedFileResponse]:
    """ Rename an expected file

     Renames one expected file attached to an agent run.

    Args:
        run_id (str): Run id
        filename (str): Expected artifact path
        body (RenameExpectedFileBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | RenameExpectedFileResponse]
     """


    kwargs = _get_kwargs(
        run_id=run_id,
filename=filename,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    run_id: str,
    filename: str,
    *,
    client: AuthenticatedClient | Client,
    body: RenameExpectedFileBody,

) -> ApiErrorEnvelope | RenameExpectedFileResponse | None:
    """ Rename an expected file

     Renames one expected file attached to an agent run.

    Args:
        run_id (str): Run id
        filename (str): Expected artifact path
        body (RenameExpectedFileBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | RenameExpectedFileResponse
     """


    return (await asyncio_detailed(
        run_id=run_id,
filename=filename,
client=client,
body=body,

    )).parsed
