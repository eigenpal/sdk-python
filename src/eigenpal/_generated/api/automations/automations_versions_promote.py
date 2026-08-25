from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_error_envelope import ApiErrorEnvelope
from ...models.automation_version import AutomationVersion
from typing import cast



def _get_kwargs(
    id: str,
    version_id: str,

) -> dict[str, Any]:






    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/automations/{id}/versions/{version_id}/promote".format(id=quote(str(id), safe=""),version_id=quote(str(version_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ApiErrorEnvelope | AutomationVersion | None:
    if response.status_code == 200:
        response_200 = AutomationVersion.from_dict(response.json())



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

    if response.status_code == 409:
        response_409 = ApiErrorEnvelope.from_dict(response.json())



        return response_409

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ApiErrorEnvelope | AutomationVersion]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    version_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[ApiErrorEnvelope | AutomationVersion]:
    """ Promote a workflow version

     Make an existing tagged YAML workflow candidate current without creating another history row. Only
    tagged version rows can be promoted; untagged snapshots (including restore HEAD) and missing ids
    return 404. Agent automations return 400. Requires a Bearer API key or a dashboard session.

    Args:
        id (str): Workflow id, agent id, or typed alias like workflows.slug / agents.slug
        version_id (str): Tagged version id from GET /automations/{id}/versions. Untagged
            snapshots (for example after restore) and unknown ids return 404.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | AutomationVersion]
     """


    kwargs = _get_kwargs(
        id=id,
version_id=version_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    version_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> ApiErrorEnvelope | AutomationVersion | None:
    """ Promote a workflow version

     Make an existing tagged YAML workflow candidate current without creating another history row. Only
    tagged version rows can be promoted; untagged snapshots (including restore HEAD) and missing ids
    return 404. Agent automations return 400. Requires a Bearer API key or a dashboard session.

    Args:
        id (str): Workflow id, agent id, or typed alias like workflows.slug / agents.slug
        version_id (str): Tagged version id from GET /automations/{id}/versions. Untagged
            snapshots (for example after restore) and unknown ids return 404.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | AutomationVersion
     """


    return sync_detailed(
        id=id,
version_id=version_id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: str,
    version_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[ApiErrorEnvelope | AutomationVersion]:
    """ Promote a workflow version

     Make an existing tagged YAML workflow candidate current without creating another history row. Only
    tagged version rows can be promoted; untagged snapshots (including restore HEAD) and missing ids
    return 404. Agent automations return 400. Requires a Bearer API key or a dashboard session.

    Args:
        id (str): Workflow id, agent id, or typed alias like workflows.slug / agents.slug
        version_id (str): Tagged version id from GET /automations/{id}/versions. Untagged
            snapshots (for example after restore) and unknown ids return 404.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | AutomationVersion]
     """


    kwargs = _get_kwargs(
        id=id,
version_id=version_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    version_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> ApiErrorEnvelope | AutomationVersion | None:
    """ Promote a workflow version

     Make an existing tagged YAML workflow candidate current without creating another history row. Only
    tagged version rows can be promoted; untagged snapshots (including restore HEAD) and missing ids
    return 404. Agent automations return 400. Requires a Bearer API key or a dashboard session.

    Args:
        id (str): Workflow id, agent id, or typed alias like workflows.slug / agents.slug
        version_id (str): Tagged version id from GET /automations/{id}/versions. Untagged
            snapshots (for example after restore) and unknown ids return 404.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | AutomationVersion
     """


    return (await asyncio_detailed(
        id=id,
version_id=version_id,
client=client,

    )).parsed
