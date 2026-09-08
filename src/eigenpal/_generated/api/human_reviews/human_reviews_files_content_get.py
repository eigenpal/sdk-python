from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_error_envelope import ApiErrorEnvelope
from typing import cast



def _get_kwargs(
    task_id: str,
    file_id: str,

) -> dict[str, Any]:






    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/human-reviews/{task_id}/files/{file_id}/content".format(task_id=quote(str(task_id), safe=""),file_id=quote(str(file_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | ApiErrorEnvelope | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 302:
        response_302 = cast(Any, None)
        return response_302

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | ApiErrorEnvelope]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    task_id: str,
    file_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[Any | ApiErrorEnvelope]:
    """ Download human review task file

     Download one file attached to a human-review task after strict tenant, task, and run ownership
    checks. Large cloud deployments may redirect to a short-lived signed storage URL.

    Args:
        task_id (str): Human review task id
        file_id (str): File id listed on the review task

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApiErrorEnvelope]
     """


    kwargs = _get_kwargs(
        task_id=task_id,
file_id=file_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    task_id: str,
    file_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Any | ApiErrorEnvelope | None:
    """ Download human review task file

     Download one file attached to a human-review task after strict tenant, task, and run ownership
    checks. Large cloud deployments may redirect to a short-lived signed storage URL.

    Args:
        task_id (str): Human review task id
        file_id (str): File id listed on the review task

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApiErrorEnvelope
     """


    return sync_detailed(
        task_id=task_id,
file_id=file_id,
client=client,

    ).parsed

async def asyncio_detailed(
    task_id: str,
    file_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[Any | ApiErrorEnvelope]:
    """ Download human review task file

     Download one file attached to a human-review task after strict tenant, task, and run ownership
    checks. Large cloud deployments may redirect to a short-lived signed storage URL.

    Args:
        task_id (str): Human review task id
        file_id (str): File id listed on the review task

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApiErrorEnvelope]
     """


    kwargs = _get_kwargs(
        task_id=task_id,
file_id=file_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    task_id: str,
    file_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Any | ApiErrorEnvelope | None:
    """ Download human review task file

     Download one file attached to a human-review task after strict tenant, task, and run ownership
    checks. Large cloud deployments may redirect to a short-lived signed storage URL.

    Args:
        task_id (str): Human review task id
        file_id (str): File id listed on the review task

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApiErrorEnvelope
     """


    return (await asyncio_detailed(
        task_id=task_id,
file_id=file_id,
client=client,

    )).parsed
