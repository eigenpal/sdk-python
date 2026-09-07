from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_error_envelope import ApiErrorEnvelope
from ...models.create_email_server_request_type_0 import CreateEmailServerRequestType0
from ...models.create_email_server_request_type_1 import CreateEmailServerRequestType1
from ...models.public_resend_email_server import PublicResendEmailServer
from ...models.public_smtp_email_server import PublicSmtpEmailServer
from typing import cast



def _get_kwargs(
    *,
    body: CreateEmailServerRequestType0 | CreateEmailServerRequestType1,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}






    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/email-servers",
    }


    if isinstance(body, CreateEmailServerRequestType0):
        _kwargs["json"] = body.to_dict()
    else:
        _kwargs["json"] = body.to_dict()



    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ApiErrorEnvelope | PublicResendEmailServer | PublicSmtpEmailServer | None:
    if response.status_code == 201:
        def _parse_response_201(data: object) -> PublicResendEmailServer | PublicSmtpEmailServer:
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

        response_201 = _parse_response_201(response.json())

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ApiErrorEnvelope | PublicResendEmailServer | PublicSmtpEmailServer]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateEmailServerRequestType0 | CreateEmailServerRequestType1,

) -> Response[ApiErrorEnvelope | PublicResendEmailServer | PublicSmtpEmailServer]:
    """ Create email server

     Create an outbound email server. Secrets are encrypted at rest and never returned. Names must be
    unique among live servers in the workspace.

    Args:
        body (CreateEmailServerRequestType0 | CreateEmailServerRequestType1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | PublicResendEmailServer | PublicSmtpEmailServer]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body: CreateEmailServerRequestType0 | CreateEmailServerRequestType1,

) -> ApiErrorEnvelope | PublicResendEmailServer | PublicSmtpEmailServer | None:
    """ Create email server

     Create an outbound email server. Secrets are encrypted at rest and never returned. Names must be
    unique among live servers in the workspace.

    Args:
        body (CreateEmailServerRequestType0 | CreateEmailServerRequestType1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | PublicResendEmailServer | PublicSmtpEmailServer
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateEmailServerRequestType0 | CreateEmailServerRequestType1,

) -> Response[ApiErrorEnvelope | PublicResendEmailServer | PublicSmtpEmailServer]:
    """ Create email server

     Create an outbound email server. Secrets are encrypted at rest and never returned. Names must be
    unique among live servers in the workspace.

    Args:
        body (CreateEmailServerRequestType0 | CreateEmailServerRequestType1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | PublicResendEmailServer | PublicSmtpEmailServer]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateEmailServerRequestType0 | CreateEmailServerRequestType1,

) -> ApiErrorEnvelope | PublicResendEmailServer | PublicSmtpEmailServer | None:
    """ Create email server

     Create an outbound email server. Secrets are encrypted at rest and never returned. Names must be
    unique among live servers in the workspace.

    Args:
        body (CreateEmailServerRequestType0 | CreateEmailServerRequestType1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | PublicResendEmailServer | PublicSmtpEmailServer
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
