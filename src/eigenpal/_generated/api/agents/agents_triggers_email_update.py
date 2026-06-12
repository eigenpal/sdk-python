from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.agents_triggers_email_update_body import AgentsTriggersEmailUpdateBody
from ...models.agents_triggers_email_update_response_200 import AgentsTriggersEmailUpdateResponse200
from ...models.api_error_envelope import ApiErrorEnvelope
from typing import cast



def _get_kwargs(
    agent_id: str,
    *,
    body: AgentsTriggersEmailUpdateBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}






    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v1/agents/{agent_id}/triggers/email".format(agent_id=quote(str(agent_id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AgentsTriggersEmailUpdateResponse200 | ApiErrorEnvelope | None:
    if response.status_code == 200:
        response_200 = AgentsTriggersEmailUpdateResponse200.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AgentsTriggersEmailUpdateResponse200 | ApiErrorEnvelope]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    agent_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AgentsTriggersEmailUpdateBody,

) -> Response[AgentsTriggersEmailUpdateResponse200 | ApiErrorEnvelope]:
    """ Update an agent email trigger

     Enables or disables the email trigger for one agent.

    Args:
        agent_id (str): Agent id or slug
        body (AgentsTriggersEmailUpdateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentsTriggersEmailUpdateResponse200 | ApiErrorEnvelope]
     """


    kwargs = _get_kwargs(
        agent_id=agent_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    agent_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AgentsTriggersEmailUpdateBody,

) -> AgentsTriggersEmailUpdateResponse200 | ApiErrorEnvelope | None:
    """ Update an agent email trigger

     Enables or disables the email trigger for one agent.

    Args:
        agent_id (str): Agent id or slug
        body (AgentsTriggersEmailUpdateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentsTriggersEmailUpdateResponse200 | ApiErrorEnvelope
     """


    return sync_detailed(
        agent_id=agent_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    agent_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AgentsTriggersEmailUpdateBody,

) -> Response[AgentsTriggersEmailUpdateResponse200 | ApiErrorEnvelope]:
    """ Update an agent email trigger

     Enables or disables the email trigger for one agent.

    Args:
        agent_id (str): Agent id or slug
        body (AgentsTriggersEmailUpdateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentsTriggersEmailUpdateResponse200 | ApiErrorEnvelope]
     """


    kwargs = _get_kwargs(
        agent_id=agent_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    agent_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AgentsTriggersEmailUpdateBody,

) -> AgentsTriggersEmailUpdateResponse200 | ApiErrorEnvelope | None:
    """ Update an agent email trigger

     Enables or disables the email trigger for one agent.

    Args:
        agent_id (str): Agent id or slug
        body (AgentsTriggersEmailUpdateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentsTriggersEmailUpdateResponse200 | ApiErrorEnvelope
     """


    return (await asyncio_detailed(
        agent_id=agent_id,
client=client,
body=body,

    )).parsed
