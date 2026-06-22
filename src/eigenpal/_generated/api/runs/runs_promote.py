from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_error_envelope import ApiErrorEnvelope
from ...models.promote_run_request import PromoteRunRequest
from ...models.promote_run_response import PromoteRunResponse
from typing import cast



def _get_kwargs(
    id: str,
    *,
    body: PromoteRunRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}






    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/runs/{id}/promote".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ApiErrorEnvelope | PromoteRunResponse | None:
    if response.status_code == 200:
        response_200 = PromoteRunResponse.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ApiErrorEnvelope | PromoteRunResponse]:
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
    body: PromoteRunRequest,

) -> Response[ApiErrorEnvelope | PromoteRunResponse]:
    """ Promote run to example

     Turn a reviewed run into a dataset example. The new example uses the run input, the run output, and
    any expected output/files stored through the feedback endpoints. Use this after adding feedback or
    expected artifacts to capture a regression test.

    Args:
        id (str): Run id.
        body (PromoteRunRequest): Create or update a dataset example from the run input, actual
            output, and feedback expected artifacts.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | PromoteRunResponse]
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
    body: PromoteRunRequest,

) -> ApiErrorEnvelope | PromoteRunResponse | None:
    """ Promote run to example

     Turn a reviewed run into a dataset example. The new example uses the run input, the run output, and
    any expected output/files stored through the feedback endpoints. Use this after adding feedback or
    expected artifacts to capture a regression test.

    Args:
        id (str): Run id.
        body (PromoteRunRequest): Create or update a dataset example from the run input, actual
            output, and feedback expected artifacts.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | PromoteRunResponse
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
    body: PromoteRunRequest,

) -> Response[ApiErrorEnvelope | PromoteRunResponse]:
    """ Promote run to example

     Turn a reviewed run into a dataset example. The new example uses the run input, the run output, and
    any expected output/files stored through the feedback endpoints. Use this after adding feedback or
    expected artifacts to capture a regression test.

    Args:
        id (str): Run id.
        body (PromoteRunRequest): Create or update a dataset example from the run input, actual
            output, and feedback expected artifacts.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | PromoteRunResponse]
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
    body: PromoteRunRequest,

) -> ApiErrorEnvelope | PromoteRunResponse | None:
    """ Promote run to example

     Turn a reviewed run into a dataset example. The new example uses the run input, the run output, and
    any expected output/files stored through the feedback endpoints. Use this after adding feedback or
    expected artifacts to capture a regression test.

    Args:
        id (str): Run id.
        body (PromoteRunRequest): Create or update a dataset example from the run input, actual
            output, and feedback expected artifacts.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | PromoteRunResponse
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
