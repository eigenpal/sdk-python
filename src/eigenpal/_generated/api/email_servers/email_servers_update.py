from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_error_envelope import ApiErrorEnvelope
from ...models.public_resend_email_server import PublicResendEmailServer
from ...models.public_smtp_email_server import PublicSmtpEmailServer
from ...models.update_email_server_request_type_0 import UpdateEmailServerRequestType0
from ...models.update_email_server_request_type_1 import UpdateEmailServerRequestType1
from ...models.update_email_server_request_type_2 import UpdateEmailServerRequestType2
from typing import cast



def _get_kwargs(
    id: str,
    *,
    body: UpdateEmailServerRequestType0 | UpdateEmailServerRequestType1 | UpdateEmailServerRequestType2,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}






    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/email-servers/{id}".format(id=quote(str(id), safe=""),),
    }


    if isinstance(body, UpdateEmailServerRequestType0):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, UpdateEmailServerRequestType1):
        _kwargs["json"] = body.to_dict()
    else:
        _kwargs["json"] = body.to_dict()



    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ApiErrorEnvelope | PublicResendEmailServer | PublicSmtpEmailServer | None:
    if response.status_code == 200:
        def _parse_response_200(data: object) -> PublicResendEmailServer | PublicSmtpEmailServer:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_email_server_type_0 = PublicResendEmailServer.from_dict(data)



                return componentsschemas_email_server_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_email_server_type_1 = PublicSmtpEmailServer.from_dict(data)



            return componentsschemas_email_server_type_1

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ApiErrorEnvelope | PublicResendEmailServer | PublicSmtpEmailServer]:
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
    body: UpdateEmailServerRequestType0 | UpdateEmailServerRequestType1 | UpdateEmailServerRequestType2,

) -> Response[ApiErrorEnvelope | PublicResendEmailServer | PublicSmtpEmailServer]:
    """ Update email server

     Rename, enable/disable, or replace transport configuration. Omitted secrets are retained only when
    the existing transport is compatible and, for SMTP, the host and username are unchanged. Changing
    transport or SMTP destination requires a complete valid target; a new password or explicit auth
    clearing is required when host or username changes.

    Args:
        id (str): Email server id (`ems_…`).
        body (UpdateEmailServerRequestType0 | UpdateEmailServerRequestType1 |
            UpdateEmailServerRequestType2):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | PublicResendEmailServer | PublicSmtpEmailServer]
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
    body: UpdateEmailServerRequestType0 | UpdateEmailServerRequestType1 | UpdateEmailServerRequestType2,

) -> ApiErrorEnvelope | PublicResendEmailServer | PublicSmtpEmailServer | None:
    """ Update email server

     Rename, enable/disable, or replace transport configuration. Omitted secrets are retained only when
    the existing transport is compatible and, for SMTP, the host and username are unchanged. Changing
    transport or SMTP destination requires a complete valid target; a new password or explicit auth
    clearing is required when host or username changes.

    Args:
        id (str): Email server id (`ems_…`).
        body (UpdateEmailServerRequestType0 | UpdateEmailServerRequestType1 |
            UpdateEmailServerRequestType2):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | PublicResendEmailServer | PublicSmtpEmailServer
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
    body: UpdateEmailServerRequestType0 | UpdateEmailServerRequestType1 | UpdateEmailServerRequestType2,

) -> Response[ApiErrorEnvelope | PublicResendEmailServer | PublicSmtpEmailServer]:
    """ Update email server

     Rename, enable/disable, or replace transport configuration. Omitted secrets are retained only when
    the existing transport is compatible and, for SMTP, the host and username are unchanged. Changing
    transport or SMTP destination requires a complete valid target; a new password or explicit auth
    clearing is required when host or username changes.

    Args:
        id (str): Email server id (`ems_…`).
        body (UpdateEmailServerRequestType0 | UpdateEmailServerRequestType1 |
            UpdateEmailServerRequestType2):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | PublicResendEmailServer | PublicSmtpEmailServer]
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
    body: UpdateEmailServerRequestType0 | UpdateEmailServerRequestType1 | UpdateEmailServerRequestType2,

) -> ApiErrorEnvelope | PublicResendEmailServer | PublicSmtpEmailServer | None:
    """ Update email server

     Rename, enable/disable, or replace transport configuration. Omitted secrets are retained only when
    the existing transport is compatible and, for SMTP, the host and username are unchanged. Changing
    transport or SMTP destination requires a complete valid target; a new password or explicit auth
    clearing is required when host or username changes.

    Args:
        id (str): Email server id (`ems_…`).
        body (UpdateEmailServerRequestType0 | UpdateEmailServerRequestType1 |
            UpdateEmailServerRequestType2):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | PublicResendEmailServer | PublicSmtpEmailServer
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
