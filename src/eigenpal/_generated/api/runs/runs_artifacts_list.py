from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_error_envelope import ApiErrorEnvelope
from ...models.run_artifacts_response import RunArtifactsResponse
from ...models.runs_artifacts_list_bundle import RunsArtifactsListBundle
from ...models.runs_artifacts_list_zip import RunsArtifactsListZip
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: str,
    *,
    zip_: RunsArtifactsListZip | Unset = UNSET,
    bundle: RunsArtifactsListBundle | Unset = UNSET,
    token: str | Unset = UNSET,

) -> dict[str, Any]:




    params: dict[str, Any] = {}

    json_zip_: str | Unset = UNSET
    if not isinstance(zip_, Unset):
        json_zip_ = zip_.value

    params["zip"] = json_zip_

    json_bundle: str | Unset = UNSET
    if not isinstance(bundle, Unset):
        json_bundle = bundle.value

    params["bundle"] = json_bundle

    params["token"] = token


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/runs/{id}/artifacts".format(id=quote(str(id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ApiErrorEnvelope | RunArtifactsResponse | bytes | None:
    if response.status_code == 200:
        if response.headers.get("content-type", "").split(";", 1)[0].strip() in {"application/zip", "application/octet-stream"}:
            return response.content
        response_200 = RunArtifactsResponse.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ApiErrorEnvelope | RunArtifactsResponse | bytes]:
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
    zip_: RunsArtifactsListZip | Unset = UNSET,
    bundle: RunsArtifactsListBundle | Unset = UNSET,
    token: str | Unset = UNSET,

) -> Response[ApiErrorEnvelope | RunArtifactsResponse | bytes]:
    """ List run artifacts

     Returns a JSON list of downloadable artifact paths for a run. Pass `zip=1` to switch the response to
    a ZIP download containing output files.

    Args:
        id (str): Run id
        zip_ (RunsArtifactsListZip | Unset): When `1`, download output files as a ZIP instead of
            listing paths. Does not include trace, scores, or input — use `GET /runs/{id}/scores` and
            `GET /runs/{id}/trace` for those.
        bundle (RunsArtifactsListBundle | Unset): With `zip=1`, use `review` to download a ZIP
            with `output/` and `expected/` folders (corrected review artifacts).
        token (str | Unset): Signed email download token (zip only; no Bearer required).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | RunArtifactsResponse | bytes]
     """


    kwargs = _get_kwargs(
        id=id,
zip_=zip_,
bundle=bundle,
token=token,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    zip_: RunsArtifactsListZip | Unset = UNSET,
    bundle: RunsArtifactsListBundle | Unset = UNSET,
    token: str | Unset = UNSET,

) -> ApiErrorEnvelope | RunArtifactsResponse | bytes | None:
    """ List run artifacts

     Returns a JSON list of downloadable artifact paths for a run. Pass `zip=1` to switch the response to
    a ZIP download containing output files.

    Args:
        id (str): Run id
        zip_ (RunsArtifactsListZip | Unset): When `1`, download output files as a ZIP instead of
            listing paths. Does not include trace, scores, or input — use `GET /runs/{id}/scores` and
            `GET /runs/{id}/trace` for those.
        bundle (RunsArtifactsListBundle | Unset): With `zip=1`, use `review` to download a ZIP
            with `output/` and `expected/` folders (corrected review artifacts).
        token (str | Unset): Signed email download token (zip only; no Bearer required).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | RunArtifactsResponse
     """


    return sync_detailed(
        id=id,
client=client,
zip_=zip_,
bundle=bundle,
token=token,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    zip_: RunsArtifactsListZip | Unset = UNSET,
    bundle: RunsArtifactsListBundle | Unset = UNSET,
    token: str | Unset = UNSET,

) -> Response[ApiErrorEnvelope | RunArtifactsResponse | bytes]:
    """ List run artifacts

     Returns a JSON list of downloadable artifact paths for a run. Pass `zip=1` to switch the response to
    a ZIP download containing output files.

    Args:
        id (str): Run id
        zip_ (RunsArtifactsListZip | Unset): When `1`, download output files as a ZIP instead of
            listing paths. Does not include trace, scores, or input — use `GET /runs/{id}/scores` and
            `GET /runs/{id}/trace` for those.
        bundle (RunsArtifactsListBundle | Unset): With `zip=1`, use `review` to download a ZIP
            with `output/` and `expected/` folders (corrected review artifacts).
        token (str | Unset): Signed email download token (zip only; no Bearer required).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | RunArtifactsResponse | bytes]
     """


    kwargs = _get_kwargs(
        id=id,
zip_=zip_,
bundle=bundle,
token=token,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    zip_: RunsArtifactsListZip | Unset = UNSET,
    bundle: RunsArtifactsListBundle | Unset = UNSET,
    token: str | Unset = UNSET,

) -> ApiErrorEnvelope | RunArtifactsResponse | bytes | None:
    """ List run artifacts

     Returns a JSON list of downloadable artifact paths for a run. Pass `zip=1` to switch the response to
    a ZIP download containing output files.

    Args:
        id (str): Run id
        zip_ (RunsArtifactsListZip | Unset): When `1`, download output files as a ZIP instead of
            listing paths. Does not include trace, scores, or input — use `GET /runs/{id}/scores` and
            `GET /runs/{id}/trace` for those.
        bundle (RunsArtifactsListBundle | Unset): With `zip=1`, use `review` to download a ZIP
            with `output/` and `expected/` folders (corrected review artifacts).
        token (str | Unset): Signed email download token (zip only; no Bearer required).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | RunArtifactsResponse
     """


    return (await asyncio_detailed(
        id=id,
client=client,
zip_=zip_,
bundle=bundle,
token=token,

    )).parsed
