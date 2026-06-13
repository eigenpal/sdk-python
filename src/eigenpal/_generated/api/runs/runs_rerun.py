from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_error_envelope import ApiErrorEnvelope
from ...models.run import Run
from ...models.run_accepted import RunAccepted
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: str,
    *,
    version: str | Unset = UNSET,
    wait_for_completion: int | Unset = UNSET,

) -> dict[str, Any]:




    params: dict[str, Any] = {}

    params["version"] = version

    params["wait_for_completion"] = wait_for_completion


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/runs/{id}/rerun".format(id=quote(str(id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ApiErrorEnvelope | Run | RunAccepted | None:
    if response.status_code == 200:
        def _parse_response_200(data: object) -> Run | RunAccepted:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_run_rerun_response_type_0 = RunAccepted.from_dict(data)



                return componentsschemas_run_rerun_response_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_run_rerun_response_type_1 = Run.from_dict(data)



            return componentsschemas_run_rerun_response_type_1

        response_200 = _parse_response_200(response.json())

        return response_200

    if response.status_code == 201:
        def _parse_response_201(data: object) -> Run | RunAccepted:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_run_rerun_response_type_0 = RunAccepted.from_dict(data)



                return componentsschemas_run_rerun_response_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_run_rerun_response_type_1 = Run.from_dict(data)



            return componentsschemas_run_rerun_response_type_1

        response_201 = _parse_response_201(response.json())

        return response_201

    if response.status_code == 202:
        def _parse_response_202(data: object) -> Run | RunAccepted:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_run_rerun_response_type_0 = RunAccepted.from_dict(data)



                return componentsschemas_run_rerun_response_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_run_rerun_response_type_1 = Run.from_dict(data)



            return componentsschemas_run_rerun_response_type_1

        response_202 = _parse_response_202(response.json())

        return response_202

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ApiErrorEnvelope | Run | RunAccepted]:
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
    version: str | Unset = UNSET,
    wait_for_completion: int | Unset = UNSET,

) -> Response[ApiErrorEnvelope | Run | RunAccepted]:
    """ Rerun run

     Start a new run from an existing run id.

    Args:
        id (str):
        version (str | Unset): Version for the new run. `original` pins the source run. Defaults
            to latest.
        wait_for_completion (int | Unset): Seconds to wait before returning (max 600). Omit for
            async.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | Run | RunAccepted]
     """


    kwargs = _get_kwargs(
        id=id,
version=version,
wait_for_completion=wait_for_completion,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    version: str | Unset = UNSET,
    wait_for_completion: int | Unset = UNSET,

) -> ApiErrorEnvelope | Run | RunAccepted | None:
    """ Rerun run

     Start a new run from an existing run id.

    Args:
        id (str):
        version (str | Unset): Version for the new run. `original` pins the source run. Defaults
            to latest.
        wait_for_completion (int | Unset): Seconds to wait before returning (max 600). Omit for
            async.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | Run | RunAccepted
     """


    return sync_detailed(
        id=id,
client=client,
version=version,
wait_for_completion=wait_for_completion,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    version: str | Unset = UNSET,
    wait_for_completion: int | Unset = UNSET,

) -> Response[ApiErrorEnvelope | Run | RunAccepted]:
    """ Rerun run

     Start a new run from an existing run id.

    Args:
        id (str):
        version (str | Unset): Version for the new run. `original` pins the source run. Defaults
            to latest.
        wait_for_completion (int | Unset): Seconds to wait before returning (max 600). Omit for
            async.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | Run | RunAccepted]
     """


    kwargs = _get_kwargs(
        id=id,
version=version,
wait_for_completion=wait_for_completion,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    version: str | Unset = UNSET,
    wait_for_completion: int | Unset = UNSET,

) -> ApiErrorEnvelope | Run | RunAccepted | None:
    """ Rerun run

     Start a new run from an existing run id.

    Args:
        id (str):
        version (str | Unset): Version for the new run. `original` pins the source run. Defaults
            to latest.
        wait_for_completion (int | Unset): Seconds to wait before returning (max 600). Omit for
            async.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | Run | RunAccepted
     """


    return (await asyncio_detailed(
        id=id,
client=client,
version=version,
wait_for_completion=wait_for_completion,

    )).parsed
