from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_error_envelope import ApiErrorEnvelope
from ...models.run_review_expected_file_update_request import RunReviewExpectedFileUpdateRequest
from ...models.run_review_expected_file_update_response import RunReviewExpectedFileUpdateResponse
from typing import cast



def _get_kwargs(
    id: str,
    filename: str,
    *,
    body: RunReviewExpectedFileUpdateRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}






    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v1/runs/{id}/reviews/expected/{filename}".format(id=quote(str(id), safe=""),filename=quote(str(filename), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ApiErrorEnvelope | RunReviewExpectedFileUpdateResponse | None:
    if response.status_code == 200:
        response_200 = RunReviewExpectedFileUpdateResponse.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ApiErrorEnvelope | RunReviewExpectedFileUpdateResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    filename: str,
    *,
    client: AuthenticatedClient | Client,
    body: RunReviewExpectedFileUpdateRequest,

) -> Response[ApiErrorEnvelope | RunReviewExpectedFileUpdateResponse]:
    """ Rename corrected artifact file

     Renames one corrected artifact file attached to the run review.

    Args:
        id (str): Run id.
        filename (str): Corrected artifact file name or slash-delimited path, as returned by `GET
            /runs/{id}/reviews/expected`.
        body (RunReviewExpectedFileUpdateRequest): Rename one corrected file.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | RunReviewExpectedFileUpdateResponse]
     """


    kwargs = _get_kwargs(
        id=id,
filename=filename,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    filename: str,
    *,
    client: AuthenticatedClient | Client,
    body: RunReviewExpectedFileUpdateRequest,

) -> ApiErrorEnvelope | RunReviewExpectedFileUpdateResponse | None:
    """ Rename corrected artifact file

     Renames one corrected artifact file attached to the run review.

    Args:
        id (str): Run id.
        filename (str): Corrected artifact file name or slash-delimited path, as returned by `GET
            /runs/{id}/reviews/expected`.
        body (RunReviewExpectedFileUpdateRequest): Rename one corrected file.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | RunReviewExpectedFileUpdateResponse
     """


    return sync_detailed(
        id=id,
filename=filename,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    id: str,
    filename: str,
    *,
    client: AuthenticatedClient | Client,
    body: RunReviewExpectedFileUpdateRequest,

) -> Response[ApiErrorEnvelope | RunReviewExpectedFileUpdateResponse]:
    """ Rename corrected artifact file

     Renames one corrected artifact file attached to the run review.

    Args:
        id (str): Run id.
        filename (str): Corrected artifact file name or slash-delimited path, as returned by `GET
            /runs/{id}/reviews/expected`.
        body (RunReviewExpectedFileUpdateRequest): Rename one corrected file.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | RunReviewExpectedFileUpdateResponse]
     """


    kwargs = _get_kwargs(
        id=id,
filename=filename,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    filename: str,
    *,
    client: AuthenticatedClient | Client,
    body: RunReviewExpectedFileUpdateRequest,

) -> ApiErrorEnvelope | RunReviewExpectedFileUpdateResponse | None:
    """ Rename corrected artifact file

     Renames one corrected artifact file attached to the run review.

    Args:
        id (str): Run id.
        filename (str): Corrected artifact file name or slash-delimited path, as returned by `GET
            /runs/{id}/reviews/expected`.
        body (RunReviewExpectedFileUpdateRequest): Rename one corrected file.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | RunReviewExpectedFileUpdateResponse
     """


    return (await asyncio_detailed(
        id=id,
filename=filename,
client=client,
body=body,

    )).parsed
