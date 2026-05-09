from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_error_envelope import ApiErrorEnvelope
from ...models.cancel_workflow_execution_response import CancelWorkflowExecutionResponse
from typing import cast



def _get_kwargs(
    execution_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/workflows/executions/{execution_id}/cancel".format(execution_id=quote(str(execution_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ApiErrorEnvelope | CancelWorkflowExecutionResponse | None:
    if response.status_code == 200:
        response_200 = CancelWorkflowExecutionResponse.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ApiErrorEnvelope | CancelWorkflowExecutionResponse]:
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

) -> Response[ApiErrorEnvelope | CancelWorkflowExecutionResponse]:
    """ Cancel a workflow execution

     Idempotent. Created/pending executions transition immediately to `cancelled`; running/waiting
    executions receive a cancellation request for the worker to observe.

    Args:
        execution_id (str): Execution id to cancel

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | CancelWorkflowExecutionResponse]
     """


    kwargs = _get_kwargs(
        execution_id=execution_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    execution_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> ApiErrorEnvelope | CancelWorkflowExecutionResponse | None:
    """ Cancel a workflow execution

     Idempotent. Created/pending executions transition immediately to `cancelled`; running/waiting
    executions receive a cancellation request for the worker to observe.

    Args:
        execution_id (str): Execution id to cancel

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | CancelWorkflowExecutionResponse
     """


    return sync_detailed(
        execution_id=execution_id,
client=client,

    ).parsed

async def asyncio_detailed(
    execution_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[ApiErrorEnvelope | CancelWorkflowExecutionResponse]:
    """ Cancel a workflow execution

     Idempotent. Created/pending executions transition immediately to `cancelled`; running/waiting
    executions receive a cancellation request for the worker to observe.

    Args:
        execution_id (str): Execution id to cancel

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | CancelWorkflowExecutionResponse]
     """


    kwargs = _get_kwargs(
        execution_id=execution_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    execution_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> ApiErrorEnvelope | CancelWorkflowExecutionResponse | None:
    """ Cancel a workflow execution

     Idempotent. Created/pending executions transition immediately to `cancelled`; running/waiting
    executions receive a cancellation request for the worker to observe.

    Args:
        execution_id (str): Execution id to cancel

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | CancelWorkflowExecutionResponse
     """


    return (await asyncio_detailed(
        execution_id=execution_id,
client=client,

    )).parsed
