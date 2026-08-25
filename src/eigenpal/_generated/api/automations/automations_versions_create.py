from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_error_envelope import ApiErrorEnvelope
from ...models.automation_version import AutomationVersion
from ...models.create_automation_version_request_type_0 import CreateAutomationVersionRequestType0
from ...models.create_automation_version_request_type_1 import CreateAutomationVersionRequestType1
from typing import cast



def _get_kwargs(
    id: str,
    *,
    body: CreateAutomationVersionRequestType0 | CreateAutomationVersionRequestType1,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}






    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/automations/{id}/versions".format(id=quote(str(id), safe=""),),
    }


    if isinstance(body, CreateAutomationVersionRequestType0):
        _kwargs["json"] = body.to_dict()
    else:
        _kwargs["json"] = body.to_dict()



    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ApiErrorEnvelope | AutomationVersion | None:
    if response.status_code == 201:
        response_201 = AutomationVersion.from_dict(response.json())



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
    *,
    client: AuthenticatedClient | Client,
    body: CreateAutomationVersionRequestType0 | CreateAutomationVersionRequestType1,

) -> Response[ApiErrorEnvelope | AutomationVersion]:
    """ Create a workflow version

     Create a tagged YAML workflow candidate from validated YAML or by copying an existing snapshot
    (`historyId`). Provide exactly one of `yaml` or `historyId`. Copy creates a new tagged row and
    leaves the source tag unchanged; it does not retag the original. Defaults to making the new version
    current. Set `activate: false` to keep it off live traffic until promote — that path requires an
    existing current workflow version and returns 400 if HEAD is empty. Agent automations are Git-backed
    and return 400. Requires a Bearer API key or a dashboard session.

    Args:
        id (str): Workflow id, agent id, or typed alias like workflows.slug / agents.slug
        body (CreateAutomationVersionRequestType0 | CreateAutomationVersionRequestType1): Exactly
            one of `yaml` or `historyId`, plus a bare semver `version`. YAML is capped at 1 MiB.
            `historyId` copies the selected snapshot into a new tagged row and does not retag the
            source. Set `activate: false` to create a detached candidate that does not move live HEAD;
            that path requires an existing current version.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | AutomationVersion]
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
    body: CreateAutomationVersionRequestType0 | CreateAutomationVersionRequestType1,

) -> ApiErrorEnvelope | AutomationVersion | None:
    """ Create a workflow version

     Create a tagged YAML workflow candidate from validated YAML or by copying an existing snapshot
    (`historyId`). Provide exactly one of `yaml` or `historyId`. Copy creates a new tagged row and
    leaves the source tag unchanged; it does not retag the original. Defaults to making the new version
    current. Set `activate: false` to keep it off live traffic until promote — that path requires an
    existing current workflow version and returns 400 if HEAD is empty. Agent automations are Git-backed
    and return 400. Requires a Bearer API key or a dashboard session.

    Args:
        id (str): Workflow id, agent id, or typed alias like workflows.slug / agents.slug
        body (CreateAutomationVersionRequestType0 | CreateAutomationVersionRequestType1): Exactly
            one of `yaml` or `historyId`, plus a bare semver `version`. YAML is capped at 1 MiB.
            `historyId` copies the selected snapshot into a new tagged row and does not retag the
            source. Set `activate: false` to create a detached candidate that does not move live HEAD;
            that path requires an existing current version.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | AutomationVersion
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
    body: CreateAutomationVersionRequestType0 | CreateAutomationVersionRequestType1,

) -> Response[ApiErrorEnvelope | AutomationVersion]:
    """ Create a workflow version

     Create a tagged YAML workflow candidate from validated YAML or by copying an existing snapshot
    (`historyId`). Provide exactly one of `yaml` or `historyId`. Copy creates a new tagged row and
    leaves the source tag unchanged; it does not retag the original. Defaults to making the new version
    current. Set `activate: false` to keep it off live traffic until promote — that path requires an
    existing current workflow version and returns 400 if HEAD is empty. Agent automations are Git-backed
    and return 400. Requires a Bearer API key or a dashboard session.

    Args:
        id (str): Workflow id, agent id, or typed alias like workflows.slug / agents.slug
        body (CreateAutomationVersionRequestType0 | CreateAutomationVersionRequestType1): Exactly
            one of `yaml` or `historyId`, plus a bare semver `version`. YAML is capped at 1 MiB.
            `historyId` copies the selected snapshot into a new tagged row and does not retag the
            source. Set `activate: false` to create a detached candidate that does not move live HEAD;
            that path requires an existing current version.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | AutomationVersion]
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
    body: CreateAutomationVersionRequestType0 | CreateAutomationVersionRequestType1,

) -> ApiErrorEnvelope | AutomationVersion | None:
    """ Create a workflow version

     Create a tagged YAML workflow candidate from validated YAML or by copying an existing snapshot
    (`historyId`). Provide exactly one of `yaml` or `historyId`. Copy creates a new tagged row and
    leaves the source tag unchanged; it does not retag the original. Defaults to making the new version
    current. Set `activate: false` to keep it off live traffic until promote — that path requires an
    existing current workflow version and returns 400 if HEAD is empty. Agent automations are Git-backed
    and return 400. Requires a Bearer API key or a dashboard session.

    Args:
        id (str): Workflow id, agent id, or typed alias like workflows.slug / agents.slug
        body (CreateAutomationVersionRequestType0 | CreateAutomationVersionRequestType1): Exactly
            one of `yaml` or `historyId`, plus a bare semver `version`. YAML is capped at 1 MiB.
            `historyId` copies the selected snapshot into a new tagged row and does not retag the
            source. Set `activate: false` to create a detached candidate that does not move live HEAD;
            that path requires an existing current version.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | AutomationVersion
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
