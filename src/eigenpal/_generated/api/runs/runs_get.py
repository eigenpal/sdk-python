from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_error_envelope import ApiErrorEnvelope
from ...models.run import Run
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: str,
    *,
    expand: str | Unset = UNSET,

) -> dict[str, Any]:




    params: dict[str, Any] = {}

    params["expand"] = expand


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/runs/{id}".format(id=quote(str(id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ApiErrorEnvelope | Run | None:
    if response.status_code == 200:
        response_200 = Run.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ApiErrorEnvelope | Run]:
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
    expand: str | Unset = UNSET,

) -> Response[ApiErrorEnvelope | Run]:
    """ Get run

     Returns the grouped run object — identity, `finished`, slim `execution`, `timing`, `source`,
    `trigger`, optional `eval`, and terminal `output`/`files`/`error` at the top level once `finished`
    is true. Pass `expand` (`input`, `usage`, `execution`, `debug`) to add nested detail objects;
    `expand=execution` adds steps (workflow) or files, feedback, and expected (agent). Download
    artifacts through `GET /api/v1/runs/:id/artifacts/:path`. Workflow definition snapshot: `GET
    /api/v1/runs/:id/definition`.

    Args:
        id (str): Run id
        expand (str | Unset): Comma-separated expand sections: `input`, `usage`, `execution`,
            `debug`. Each adds one nested object onto the run. `finished` and slim `execution`
            (status, schemaValid, batch, retry, annotation) are always present; `output`, `files`, and
            `error` appear at the top level once the run is terminal. Use `expand=execution` for steps
            (workflow) or files, feedback, and expected (agent). Unknown tokens return 400 with a
            migration hint.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | Run]
     """


    kwargs = _get_kwargs(
        id=id,
expand=expand,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    expand: str | Unset = UNSET,

) -> ApiErrorEnvelope | Run | None:
    """ Get run

     Returns the grouped run object — identity, `finished`, slim `execution`, `timing`, `source`,
    `trigger`, optional `eval`, and terminal `output`/`files`/`error` at the top level once `finished`
    is true. Pass `expand` (`input`, `usage`, `execution`, `debug`) to add nested detail objects;
    `expand=execution` adds steps (workflow) or files, feedback, and expected (agent). Download
    artifacts through `GET /api/v1/runs/:id/artifacts/:path`. Workflow definition snapshot: `GET
    /api/v1/runs/:id/definition`.

    Args:
        id (str): Run id
        expand (str | Unset): Comma-separated expand sections: `input`, `usage`, `execution`,
            `debug`. Each adds one nested object onto the run. `finished` and slim `execution`
            (status, schemaValid, batch, retry, annotation) are always present; `output`, `files`, and
            `error` appear at the top level once the run is terminal. Use `expand=execution` for steps
            (workflow) or files, feedback, and expected (agent). Unknown tokens return 400 with a
            migration hint.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | Run
     """


    return sync_detailed(
        id=id,
client=client,
expand=expand,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    expand: str | Unset = UNSET,

) -> Response[ApiErrorEnvelope | Run]:
    """ Get run

     Returns the grouped run object — identity, `finished`, slim `execution`, `timing`, `source`,
    `trigger`, optional `eval`, and terminal `output`/`files`/`error` at the top level once `finished`
    is true. Pass `expand` (`input`, `usage`, `execution`, `debug`) to add nested detail objects;
    `expand=execution` adds steps (workflow) or files, feedback, and expected (agent). Download
    artifacts through `GET /api/v1/runs/:id/artifacts/:path`. Workflow definition snapshot: `GET
    /api/v1/runs/:id/definition`.

    Args:
        id (str): Run id
        expand (str | Unset): Comma-separated expand sections: `input`, `usage`, `execution`,
            `debug`. Each adds one nested object onto the run. `finished` and slim `execution`
            (status, schemaValid, batch, retry, annotation) are always present; `output`, `files`, and
            `error` appear at the top level once the run is terminal. Use `expand=execution` for steps
            (workflow) or files, feedback, and expected (agent). Unknown tokens return 400 with a
            migration hint.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | Run]
     """


    kwargs = _get_kwargs(
        id=id,
expand=expand,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    expand: str | Unset = UNSET,

) -> ApiErrorEnvelope | Run | None:
    """ Get run

     Returns the grouped run object — identity, `finished`, slim `execution`, `timing`, `source`,
    `trigger`, optional `eval`, and terminal `output`/`files`/`error` at the top level once `finished`
    is true. Pass `expand` (`input`, `usage`, `execution`, `debug`) to add nested detail objects;
    `expand=execution` adds steps (workflow) or files, feedback, and expected (agent). Download
    artifacts through `GET /api/v1/runs/:id/artifacts/:path`. Workflow definition snapshot: `GET
    /api/v1/runs/:id/definition`.

    Args:
        id (str): Run id
        expand (str | Unset): Comma-separated expand sections: `input`, `usage`, `execution`,
            `debug`. Each adds one nested object onto the run. `finished` and slim `execution`
            (status, schemaValid, batch, retry, annotation) are always present; `output`, `files`, and
            `error` appear at the top level once the run is terminal. Use `expand=execution` for steps
            (workflow) or files, feedback, and expected (agent). Unknown tokens return 400 with a
            migration hint.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | Run
     """


    return (await asyncio_detailed(
        id=id,
client=client,
expand=expand,

    )).parsed
