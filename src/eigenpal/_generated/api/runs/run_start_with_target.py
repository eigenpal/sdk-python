from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_error_envelope import ApiErrorEnvelope
from ...models.run_start_response import RunStartResponse
from ...models.run_start_with_target_files_body import RunStartWithTargetFilesBody
from ...models.run_target_input_body import RunTargetInputBody
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    target: str,
    *,
    body:    RunTargetInputBody  |     RunStartWithTargetFilesBody  | Unset = UNSET,
    version: str | Unset = UNSET,
    wait_for_completion: int | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["version"] = version

    params["wait_for_completion"] = wait_for_completion


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/run/{target}".format(target=quote(str(target), safe=""),),
        "params": params,
    }

    if isinstance(body, RunTargetInputBody):
        _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "application/json"
    if isinstance(body, RunStartWithTargetFilesBody):
        _kwargs["files"] = body.to_multipart()


        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ApiErrorEnvelope | RunStartResponse | None:
    if response.status_code == 200:
        response_200 = RunStartResponse.from_dict(response.json())



        return response_200

    if response.status_code == 201:
        response_201 = RunStartResponse.from_dict(response.json())



        return response_201

    if response.status_code == 202:
        response_202 = RunStartResponse.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ApiErrorEnvelope | RunStartResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    target: str,
    *,
    client: AuthenticatedClient | Client,
    body:    RunTargetInputBody  |     RunStartWithTargetFilesBody  | Unset = UNSET,
    version: str | Unset = UNSET,
    wait_for_completion: int | Unset = UNSET,

) -> Response[ApiErrorEnvelope | RunStartResponse]:
    """ Start a workflow or agent run

     Starts a run for a workflow or agent target. The target lives in the URL path; the optional
    `version` query parameter selects a release/ref and defaults to `latest`. The request body is the
    input object; a reserved `_overrides` key (workflow targets only) carries per-step output overrides
    for replay. Run provenance may be declared with the `X-Eigenpal-Trigger` header (`api` or `cli`).

    Args:
        target (str): Automation target without a version suffix.
        version (str | Unset): Optional version or source ref. Defaults to latest.
        wait_for_completion (int | Unset):
        body (RunTargetInputBody):
        body (RunStartWithTargetFilesBody): Multipart upload. `_json` carries scalar input fields
            only; file form fields become run inputs; an optional `_overrides` text field carries per-
            step output overrides as JSON.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | RunStartResponse]
     """


    kwargs = _get_kwargs(
        target=target,
body=body,
version=version,
wait_for_completion=wait_for_completion,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    target: str,
    *,
    client: AuthenticatedClient | Client,
    body:    RunTargetInputBody  |     RunStartWithTargetFilesBody  | Unset = UNSET,
    version: str | Unset = UNSET,
    wait_for_completion: int | Unset = UNSET,

) -> ApiErrorEnvelope | RunStartResponse | None:
    """ Start a workflow or agent run

     Starts a run for a workflow or agent target. The target lives in the URL path; the optional
    `version` query parameter selects a release/ref and defaults to `latest`. The request body is the
    input object; a reserved `_overrides` key (workflow targets only) carries per-step output overrides
    for replay. Run provenance may be declared with the `X-Eigenpal-Trigger` header (`api` or `cli`).

    Args:
        target (str): Automation target without a version suffix.
        version (str | Unset): Optional version or source ref. Defaults to latest.
        wait_for_completion (int | Unset):
        body (RunTargetInputBody):
        body (RunStartWithTargetFilesBody): Multipart upload. `_json` carries scalar input fields
            only; file form fields become run inputs; an optional `_overrides` text field carries per-
            step output overrides as JSON.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | RunStartResponse
     """


    return sync_detailed(
        target=target,
client=client,
body=body,
version=version,
wait_for_completion=wait_for_completion,

    ).parsed

async def asyncio_detailed(
    target: str,
    *,
    client: AuthenticatedClient | Client,
    body:    RunTargetInputBody  |     RunStartWithTargetFilesBody  | Unset = UNSET,
    version: str | Unset = UNSET,
    wait_for_completion: int | Unset = UNSET,

) -> Response[ApiErrorEnvelope | RunStartResponse]:
    """ Start a workflow or agent run

     Starts a run for a workflow or agent target. The target lives in the URL path; the optional
    `version` query parameter selects a release/ref and defaults to `latest`. The request body is the
    input object; a reserved `_overrides` key (workflow targets only) carries per-step output overrides
    for replay. Run provenance may be declared with the `X-Eigenpal-Trigger` header (`api` or `cli`).

    Args:
        target (str): Automation target without a version suffix.
        version (str | Unset): Optional version or source ref. Defaults to latest.
        wait_for_completion (int | Unset):
        body (RunTargetInputBody):
        body (RunStartWithTargetFilesBody): Multipart upload. `_json` carries scalar input fields
            only; file form fields become run inputs; an optional `_overrides` text field carries per-
            step output overrides as JSON.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | RunStartResponse]
     """


    kwargs = _get_kwargs(
        target=target,
body=body,
version=version,
wait_for_completion=wait_for_completion,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    target: str,
    *,
    client: AuthenticatedClient | Client,
    body:    RunTargetInputBody  |     RunStartWithTargetFilesBody  | Unset = UNSET,
    version: str | Unset = UNSET,
    wait_for_completion: int | Unset = UNSET,

) -> ApiErrorEnvelope | RunStartResponse | None:
    """ Start a workflow or agent run

     Starts a run for a workflow or agent target. The target lives in the URL path; the optional
    `version` query parameter selects a release/ref and defaults to `latest`. The request body is the
    input object; a reserved `_overrides` key (workflow targets only) carries per-step output overrides
    for replay. Run provenance may be declared with the `X-Eigenpal-Trigger` header (`api` or `cli`).

    Args:
        target (str): Automation target without a version suffix.
        version (str | Unset): Optional version or source ref. Defaults to latest.
        wait_for_completion (int | Unset):
        body (RunTargetInputBody):
        body (RunStartWithTargetFilesBody): Multipart upload. `_json` carries scalar input fields
            only; file form fields become run inputs; an optional `_overrides` text field carries per-
            step output overrides as JSON.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | RunStartResponse
     """


    return (await asyncio_detailed(
        target=target,
client=client,
body=body,
version=version,
wait_for_completion=wait_for_completion,

    )).parsed
