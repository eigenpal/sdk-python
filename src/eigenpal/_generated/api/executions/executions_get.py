from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_error_envelope import ApiErrorEnvelope
from ...models.execution_status_response import ExecutionStatusResponse
from ...models.execution_summary import ExecutionSummary
from ...models.executions_get_include_steps import ExecutionsGetIncludeSteps
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    execution_id: str,
    *,
    include_steps: ExecutionsGetIncludeSteps | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_include_steps: str | Unset = UNSET
    if not isinstance(include_steps, Unset):
        json_include_steps = include_steps.value

    params["includeSteps"] = json_include_steps


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/executions/{execution_id}".format(execution_id=quote(str(execution_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ApiErrorEnvelope | ExecutionStatusResponse | ExecutionSummary | None:
    if response.status_code == 200:
        def _parse_response_200(data: object) -> ExecutionStatusResponse | ExecutionSummary:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = ExecutionStatusResponse.from_dict(data)



                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = ExecutionSummary.from_dict(data)



            return response_200_type_1

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ApiErrorEnvelope | ExecutionStatusResponse | ExecutionSummary]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    execution_id: str,
    *,
    client: AuthenticatedClient | Client,
    include_steps: ExecutionsGetIncludeSteps | Unset = UNSET,

) -> Response[ApiErrorEnvelope | ExecutionStatusResponse | ExecutionSummary]:
    """ Get execution status

     Returns the current status, completion timestamps, and (when terminal) the result or error for a
    single execution. Pass `includeSteps=true` for the per-step artifact payload (heavier; intended for
    debugging).

    Args:
        execution_id (str): Execution id (e.g. exec_xyz)
        include_steps (ExecutionsGetIncludeSteps | Unset): When "true", returns the full per-step
            execution payload instead of the summary

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | ExecutionStatusResponse | ExecutionSummary]
     """


    kwargs = _get_kwargs(
        execution_id=execution_id,
include_steps=include_steps,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    execution_id: str,
    *,
    client: AuthenticatedClient | Client,
    include_steps: ExecutionsGetIncludeSteps | Unset = UNSET,

) -> ApiErrorEnvelope | ExecutionStatusResponse | ExecutionSummary | None:
    """ Get execution status

     Returns the current status, completion timestamps, and (when terminal) the result or error for a
    single execution. Pass `includeSteps=true` for the per-step artifact payload (heavier; intended for
    debugging).

    Args:
        execution_id (str): Execution id (e.g. exec_xyz)
        include_steps (ExecutionsGetIncludeSteps | Unset): When "true", returns the full per-step
            execution payload instead of the summary

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | ExecutionStatusResponse | ExecutionSummary
     """


    return sync_detailed(
        execution_id=execution_id,
client=client,
include_steps=include_steps,

    ).parsed

async def asyncio_detailed(
    execution_id: str,
    *,
    client: AuthenticatedClient | Client,
    include_steps: ExecutionsGetIncludeSteps | Unset = UNSET,

) -> Response[ApiErrorEnvelope | ExecutionStatusResponse | ExecutionSummary]:
    """ Get execution status

     Returns the current status, completion timestamps, and (when terminal) the result or error for a
    single execution. Pass `includeSteps=true` for the per-step artifact payload (heavier; intended for
    debugging).

    Args:
        execution_id (str): Execution id (e.g. exec_xyz)
        include_steps (ExecutionsGetIncludeSteps | Unset): When "true", returns the full per-step
            execution payload instead of the summary

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | ExecutionStatusResponse | ExecutionSummary]
     """


    kwargs = _get_kwargs(
        execution_id=execution_id,
include_steps=include_steps,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    execution_id: str,
    *,
    client: AuthenticatedClient | Client,
    include_steps: ExecutionsGetIncludeSteps | Unset = UNSET,

) -> ApiErrorEnvelope | ExecutionStatusResponse | ExecutionSummary | None:
    """ Get execution status

     Returns the current status, completion timestamps, and (when terminal) the result or error for a
    single execution. Pass `includeSteps=true` for the per-step artifact payload (heavier; intended for
    debugging).

    Args:
        execution_id (str): Execution id (e.g. exec_xyz)
        include_steps (ExecutionsGetIncludeSteps | Unset): When "true", returns the full per-step
            execution payload instead of the summary

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | ExecutionStatusResponse | ExecutionSummary
     """


    return (await asyncio_detailed(
        execution_id=execution_id,
client=client,
include_steps=include_steps,

    )).parsed
