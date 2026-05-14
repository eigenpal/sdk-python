from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET, Unset
from ... import errors

from ...models.agents_executions_expected_create_files_body import AgentsExecutionsExpectedCreateFilesBody
from ...models.agents_executions_expected_create_response_201 import AgentsExecutionsExpectedCreateResponse201
from ...models.api_error_envelope import ApiErrorEnvelope
from ...models.copy_agent_execution_output_to_expected_body import CopyAgentExecutionOutputToExpectedBody
from typing import cast



def _get_kwargs(
    execution_id: str,
    *,
    body:    CopyAgentExecutionOutputToExpectedBody  |     AgentsExecutionsExpectedCreateFilesBody  | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/agents/executions/{execution_id}/expected".format(execution_id=quote(str(execution_id), safe=""),),
    }

    if isinstance(body, CopyAgentExecutionOutputToExpectedBody):
        _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "application/json"
    if isinstance(body, AgentsExecutionsExpectedCreateFilesBody):
        _kwargs["files"] = body.to_multipart()


        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AgentsExecutionsExpectedCreateResponse201 | ApiErrorEnvelope | None:
    if response.status_code == 201:
        response_201 = AgentsExecutionsExpectedCreateResponse201.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AgentsExecutionsExpectedCreateResponse201 | ApiErrorEnvelope]:
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
    body:    CopyAgentExecutionOutputToExpectedBody  |     AgentsExecutionsExpectedCreateFilesBody  | Unset = UNSET,

) -> Response[AgentsExecutionsExpectedCreateResponse201 | ApiErrorEnvelope]:
    """ Create an expected file

     Uploads an expected file with multipart/form-data, or copies a generated output file into expected
    artifacts with JSON.

    Args:
        execution_id (str): Execution id
        body (CopyAgentExecutionOutputToExpectedBody):
        body (AgentsExecutionsExpectedCreateFilesBody): Form fields: file=<binary>, optional
            name=<expected artifact path>

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentsExecutionsExpectedCreateResponse201 | ApiErrorEnvelope]
     """


    kwargs = _get_kwargs(
        execution_id=execution_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    execution_id: str,
    *,
    client: AuthenticatedClient | Client,
    body:    CopyAgentExecutionOutputToExpectedBody  |     AgentsExecutionsExpectedCreateFilesBody  | Unset = UNSET,

) -> AgentsExecutionsExpectedCreateResponse201 | ApiErrorEnvelope | None:
    """ Create an expected file

     Uploads an expected file with multipart/form-data, or copies a generated output file into expected
    artifacts with JSON.

    Args:
        execution_id (str): Execution id
        body (CopyAgentExecutionOutputToExpectedBody):
        body (AgentsExecutionsExpectedCreateFilesBody): Form fields: file=<binary>, optional
            name=<expected artifact path>

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentsExecutionsExpectedCreateResponse201 | ApiErrorEnvelope
     """


    return sync_detailed(
        execution_id=execution_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    execution_id: str,
    *,
    client: AuthenticatedClient | Client,
    body:    CopyAgentExecutionOutputToExpectedBody  |     AgentsExecutionsExpectedCreateFilesBody  | Unset = UNSET,

) -> Response[AgentsExecutionsExpectedCreateResponse201 | ApiErrorEnvelope]:
    """ Create an expected file

     Uploads an expected file with multipart/form-data, or copies a generated output file into expected
    artifacts with JSON.

    Args:
        execution_id (str): Execution id
        body (CopyAgentExecutionOutputToExpectedBody):
        body (AgentsExecutionsExpectedCreateFilesBody): Form fields: file=<binary>, optional
            name=<expected artifact path>

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentsExecutionsExpectedCreateResponse201 | ApiErrorEnvelope]
     """


    kwargs = _get_kwargs(
        execution_id=execution_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    execution_id: str,
    *,
    client: AuthenticatedClient | Client,
    body:    CopyAgentExecutionOutputToExpectedBody  |     AgentsExecutionsExpectedCreateFilesBody  | Unset = UNSET,

) -> AgentsExecutionsExpectedCreateResponse201 | ApiErrorEnvelope | None:
    """ Create an expected file

     Uploads an expected file with multipart/form-data, or copies a generated output file into expected
    artifacts with JSON.

    Args:
        execution_id (str): Execution id
        body (CopyAgentExecutionOutputToExpectedBody):
        body (AgentsExecutionsExpectedCreateFilesBody): Form fields: file=<binary>, optional
            name=<expected artifact path>

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentsExecutionsExpectedCreateResponse201 | ApiErrorEnvelope
     """


    return (await asyncio_detailed(
        execution_id=execution_id,
client=client,
body=body,

    )).parsed
