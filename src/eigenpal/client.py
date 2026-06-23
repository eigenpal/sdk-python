"""Hand-written Python facade for the public Eigenpal API."""

from __future__ import annotations

import json
import os
import time
from pathlib import Path
from typing import Any, BinaryIO, Iterator, Literal, Optional, Sequence, Union
from urllib.parse import quote

import httpx

from eigenpal._files import has_file_input, is_file_input, to_upload_tuple
from eigenpal._telemetry import build_telemetry_headers
from eigenpal.errors import EigenpalError, EigenpalTimeoutError, error_from_response

DEFAULT_BASE_URL = "https://studio.eigenpal.com"
DEFAULT_TIMEOUT_SECONDS = 60.0
DEFAULT_POLL_INTERVAL_SECONDS = 2.0
DEFAULT_RUN_AND_WAIT_TIMEOUT_SECONDS = 5 * 60.0
TERMINAL_STATUSES = frozenset({"completed", "failed", "cancelled", "rejected"})

RunTarget = Union[
    str,
    dict[str, Union[Literal["workflow", "agent"], str]],
]
RunExpandSection = Literal["input", "usage", "execution", "debug"]
RunExpand = Union[RunExpandSection, Sequence[RunExpandSection], str]


class AttrDict(dict[str, Any]):
    """Dict response that also supports attribute access."""

    def __getattr__(self, name: str) -> Any:
        try:
            return self[name]
        except KeyError as exc:
            raise AttributeError(name) from exc


def _to_attr(value: Any) -> Any:
    if isinstance(value, dict):
        return AttrDict({key: _to_attr(item) for key, item in value.items()})
    if isinstance(value, list):
        return [_to_attr(item) for item in value]
    return value


def _format_run_expand(expand: Optional[RunExpand]) -> Optional[str]:
    if expand is None or isinstance(expand, str):
        return expand
    return ",".join(expand)


def _headers(api_key: str, default_headers: Optional[dict[str, str]]) -> dict[str, str]:
    return {
        "Authorization": f"Bearer {api_key}",
        **build_telemetry_headers(),
        **(default_headers or {}),
    }


def _assert_json_response(response: httpx.Response) -> None:
    if response.status_code == 204:
        return
    content_type = (response.headers.get("content-type") or "").lower()
    if content_type == "" or "json" in content_type or "octet-stream" in content_type:
        return
    raise EigenpalError(
        f'Expected a JSON response from the API but got Content-Type "{content_type}". '
        "Set `base_url` to your Eigenpal instance root, "
        'e.g. "https://studio.eigenpal.com".',
        status=response.status_code,
    )


def _parse_json_error(response: httpx.Response) -> Optional[dict[str, Any]]:
    try:
        parsed = response.json()
    except Exception:
        return None
    return parsed if isinstance(parsed, dict) else None


def _check_response(response: httpx.Response) -> Any:
    _assert_json_response(response)
    if 200 <= response.status_code < 300:
        if response.status_code == 204 or not response.content:
            return None
        return _to_attr(response.json())

    retry_after: Optional[int] = None
    try:
        retry_after = int(response.headers.get("retry-after", ""))
    except ValueError:
        pass
    raise error_from_response(response.status_code, _parse_json_error(response), retry_after)


def _is_retriable(status: int) -> bool:
    return status >= 500 or status == 429


def _path_target(target: RunTarget) -> tuple[str, Optional[str]]:
    if isinstance(target, str):
        parts = target.split("@")
        if len(parts) > 2 or not parts[0] or (len(parts) == 2 and not parts[1]):
            raise EigenpalError(
                "Run target strings must be <target> or <target>@<version>.",
                status=0,
            )
        version = parts[1] if len(parts) == 2 and parts[1] != "latest" else None
        return parts[0], version

    kind = target.get("type")
    id_or_slug = target.get("slug") or target.get("id")
    if kind not in ("workflow", "agent") or not isinstance(id_or_slug, str):
        raise EigenpalError("Run target objects require `type` plus `slug` or `id`.", status=0)

    if kind == "agent":
        if "." in id_or_slug and not id_or_slug.startswith("agents."):
            raise EigenpalError(
                f'Agent target must be rooted at "agents.", got "{id_or_slug}".',
                status=0,
            )
        path_target = id_or_slug if id_or_slug.startswith("agents.") else f"agents.{id_or_slug}"
    else:
        path_target = f"workflows.{id_or_slug}"

    version = target.get("version")
    return path_target.replace("/", "."), version if isinstance(version, str) else None


def _quote_path(path: str) -> str:
    return "/".join(quote(part, safe="") for part in path.split("/"))


class EigenpalClient:
    """Top-level public API client."""

    def __init__(
        self,
        *,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        timeout_seconds: float = DEFAULT_TIMEOUT_SECONDS,
        max_retries: int = 3,
        default_headers: Optional[dict[str, str]] = None,
        httpx_args: Optional[dict[str, Any]] = None,
    ) -> None:
        resolved_key = api_key or os.getenv("EIGENPAL_API_KEY")
        if not resolved_key:
            raise EigenpalError(
                "Missing API key. Pass `EigenpalClient(api_key=...)` or set EIGENPAL_API_KEY.",
                status=0,
            )

        self.base_url = (base_url or os.getenv("EIGENPAL_BASE_URL") or DEFAULT_BASE_URL).rstrip("/")
        self.timeout_seconds = timeout_seconds
        self.max_retries = max_retries
        self._http = httpx.Client(
            base_url=self.base_url,
            timeout=timeout_seconds,
            headers=_headers(resolved_key, default_headers),
            **(httpx_args or {}),
        )

        self.auth = AuthResource(self)
        self.automations = AutomationsResource(self)
        self.runs = RunsResource(self)
        self.files = FilesResource(self)

    def close(self) -> None:
        self._http.close()

    def __enter__(self) -> "EigenpalClient":
        return self

    def __exit__(self, *_: object) -> None:
        self.close()

    def _request(self, method: str, url: str, **kwargs: Any) -> Any:
        for attempt in range(self.max_retries + 1):
            try:
                response = self._http.request(method, url, **kwargs)
                if _is_retriable(response.status_code) and attempt < self.max_retries:
                    time.sleep(0.25 * (2**attempt))
                    continue
                return _check_response(response)
            except httpx.TimeoutException as exc:
                if attempt < self.max_retries:
                    time.sleep(0.25 * (2**attempt))
                    continue
                raise EigenpalTimeoutError() from exc
            except httpx.TransportError:
                if attempt < self.max_retries:
                    time.sleep(0.25 * (2**attempt))
                    continue
                raise

        raise AssertionError("unreachable")

    def run(
        self,
        target: RunTarget,
        input: Optional[dict[str, Any]] = None,
        *,
        wait_for_completion: Optional[int] = None,
        overrides: Optional[dict[str, Any]] = None,
        metadata: Optional[dict[str, Any]] = None,
    ) -> Any:
        path_target, version = _path_target(target)
        params: dict[str, Any] = {}
        if wait_for_completion is not None:
            params["wait_for_completion"] = wait_for_completion
        if version:
            params["version"] = version

        if has_file_input(input):
            fields: dict[str, Any] = {"target": (None, path_target)}
            if input:
                scalar_input: dict[str, Any] = {}
                for key, value in input.items():
                    if is_file_input(value):
                        fields[f"files.{key}"] = to_upload_tuple(value)
                    else:
                        scalar_input[key] = value
                fields["input"] = (None, json.dumps(scalar_input), "application/json")
            if overrides:
                fields["overrides"] = (None, json.dumps(overrides), "application/json")
            if metadata:
                fields["metadata"] = (None, json.dumps(metadata), "application/json")
            return self._request("POST", "/api/v1/runs", params=params or None, files=fields)

        body: dict[str, Any] = {"target": path_target}
        if input is not None:
            body["input"] = input
        if overrides:
            body["overrides"] = overrides
        if metadata:
            body["metadata"] = metadata
        return self._request("POST", "/api/v1/runs", params=params or None, json=body)

    def rerun(
        self,
        run_id: str,
        *,
        version: Optional[str] = None,
        wait_for_completion: Optional[int] = None,
    ) -> Any:
        params: dict[str, Any] = {}
        if version and version != "latest":
            params["version"] = version
        if wait_for_completion is not None:
            params["wait_for_completion"] = wait_for_completion
        return self._request("POST", f"/api/v1/runs/{quote(run_id, safe='')}/rerun", params=params or None)

    def run_and_wait(
        self,
        target: RunTarget,
        input: Optional[dict[str, Any]] = None,
        *,
        timeout_seconds: float = DEFAULT_RUN_AND_WAIT_TIMEOUT_SECONDS,
        poll_interval_seconds: float = DEFAULT_POLL_INTERVAL_SECONDS,
        overrides: Optional[dict[str, Any]] = None,
        metadata: Optional[dict[str, Any]] = None,
    ) -> Any:
        started = self.run(target, input=input, overrides=overrides, metadata=metadata)
        run_id = started["id"]
        deadline = time.monotonic() + timeout_seconds
        while time.monotonic() < deadline:
            current = self.runs.get(run_id)
            status = (((current.get("execution") or {}) if isinstance(current, dict) else {}).get("status"))
            if status in TERMINAL_STATUSES or current.get("finished") is True:
                return current
            time.sleep(poll_interval_seconds)
        raise EigenpalTimeoutError(f"Run {run_id} did not finish within {timeout_seconds:g}s")


class AuthResource:
    def __init__(self, root: EigenpalClient) -> None:
        self._root = root

    def check(self) -> Any:
        return self._root._request("GET", "/api/v1/auth/check")


class AutomationsResource:
    def __init__(self, root: EigenpalClient) -> None:
        self._root = root
        self.dataset = AutomationDatasetResource(root)
        self.examples = AutomationExamplesResource(root)
        self.evaluators = AutomationEvaluatorsResource(root)
        self.experiments = AutomationExperimentsResource(root)
        self.reviews = AutomationReviewsResource(root)

    def list(
        self,
        *,
        search: Optional[str] = None,
        type: Optional[Literal["workflow", "agent"]] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> Any:
        params = {"search": search, "type": type, "limit": limit, "offset": offset}
        return self._root._request(
            "GET",
            "/api/v1/automations",
            params={k: v for k, v in params.items() if v is not None} or None,
        )

    def get(self, automation_id: str) -> Any:
        return self._root._request("GET", f"/api/v1/automations/{quote(automation_id, safe='')}")

    def versions(self, automation_id: str) -> Any:
        return self._root._request(
            "GET",
            f"/api/v1/automations/{quote(automation_id, safe='')}/versions",
        )

    def triggers(self, automation_id: str) -> Any:
        return self._root._request(
            "GET",
            f"/api/v1/automations/{quote(automation_id, safe='')}/triggers",
        )

    def sync(self, automation_id: str) -> Any:
        return self._root._request(
            "POST",
            f"/api/v1/automations/{quote(automation_id, safe='')}/sync",
        )


class AutomationReviewsResource:
    def __init__(self, root: EigenpalClient) -> None:
        self._root = root

    def health(self, automation_id: str, **query: Any) -> Any:
        return self._root._request(
            "GET",
            f"/api/v1/automations/{quote(automation_id, safe='')}/reviews/health",
            params=query or None,
        )


class AutomationDatasetResource:
    def __init__(self, root: EigenpalClient) -> None:
        self._root = root

    def export(self, automation_id: str, *, example_ids: Optional[Sequence[str]] = None) -> bytes:
        params = {"exampleIds": ",".join(example_ids)} if example_ids else None
        response = self._root._http.get(
            f"/api/v1/automations/{quote(automation_id, safe='')}/dataset/export",
            params=params,
        )
        if response.status_code >= 400:
            _check_response(response)
        return response.content

    def import_(
        self,
        automation_id: str,
        file: Path | dict[str, Any] | BinaryIO,
        *,
        mode: Literal["append", "replace"] = "append",
    ) -> Any:
        return self._root._request(
            "POST",
            f"/api/v1/automations/{quote(automation_id, safe='')}/dataset/import",
            files={"file": to_upload_tuple(file)},
            data={"mode": mode},
        )


class AutomationExamplesResource:
    def __init__(self, root: EigenpalClient) -> None:
        self._root = root

    def list(
        self,
        automation_id: str,
        *,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> Any:
        params = {"limit": limit, "offset": offset}
        return self._root._request(
            "GET",
            f"/api/v1/automations/{quote(automation_id, safe='')}/examples",
            params={k: v for k, v in params.items() if v is not None} or None,
        )

    def create(self, automation_id: str, body: dict[str, Any]) -> Any:
        return self._root._request(
            "POST",
            f"/api/v1/automations/{quote(automation_id, safe='')}/examples",
            json=body,
        )

    def get(self, automation_id: str, example_id: str) -> Any:
        return self._root._request(
            "GET",
            f"/api/v1/automations/{quote(automation_id, safe='')}/examples/{quote(example_id, safe='')}",
        )

    def update(self, automation_id: str, example_id: str, body: dict[str, Any]) -> Any:
        return self._root._request(
            "PATCH",
            f"/api/v1/automations/{quote(automation_id, safe='')}/examples/{quote(example_id, safe='')}",
            json=body,
        )

    def delete(self, automation_id: str, example_id: str) -> Any:
        return self._root._request(
            "DELETE",
            f"/api/v1/automations/{quote(automation_id, safe='')}/examples/{quote(example_id, safe='')}",
        )

    def run(self, automation_id: str, example_id: str) -> Any:
        return self._root._request(
            "POST",
            f"/api/v1/automations/{quote(automation_id, safe='')}/examples/{quote(example_id, safe='')}/run",
        )


class AutomationEvaluatorsResource:
    def __init__(self, root: EigenpalClient) -> None:
        self._root = root

    def get(self, automation_id: str) -> Any:
        return self._root._request(
            "GET",
            f"/api/v1/automations/{quote(automation_id, safe='')}/evaluators",
        )

    def update(self, automation_id: str, yaml: str) -> Any:
        return self._root._request(
            "PUT",
            f"/api/v1/automations/{quote(automation_id, safe='')}/evaluators",
            json={"yaml": yaml},
        )


class AutomationExperimentsResource:
    def __init__(self, root: EigenpalClient) -> None:
        self._root = root

    def list(
        self,
        automation_id: str,
        *,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> Any:
        params = {"limit": limit, "offset": offset}
        return self._root._request(
            "GET",
            f"/api/v1/automations/{quote(automation_id, safe='')}/experiments",
            params={k: v for k, v in params.items() if v is not None} or None,
        )

    def create(self, automation_id: str, body: Optional[dict[str, Any]] = None) -> Any:
        return self._root._request(
            "POST",
            f"/api/v1/automations/{quote(automation_id, safe='')}/experiments",
            json=body or {},
        )

    def get(self, automation_id: str, experiment_id: str) -> Any:
        return self._root._request(
            "GET",
            f"/api/v1/automations/{quote(automation_id, safe='')}/experiments/{quote(experiment_id, safe='')}",
        )

    def cancel(self, automation_id: str, experiment_id: str) -> Any:
        return self._root._request(
            "POST",
            f"/api/v1/automations/{quote(automation_id, safe='')}/experiments/{quote(experiment_id, safe='')}/cancel",
        )

    def export(
        self,
        automation_id: str,
        experiment_id: str,
        *,
        format: Literal["csv", "json"] = "csv",
    ) -> str:
        response = self._root._http.get(
            f"/api/v1/automations/{quote(automation_id, safe='')}/experiments/{quote(experiment_id, safe='')}/export",
            params={"format": format},
        )
        if response.status_code >= 400:
            _check_response(response)
        return response.text

    def export_all(
        self,
        automation_id: str,
        *,
        format: Literal["csv", "json"] = "csv",
    ) -> str:
        response = self._root._http.get(
            f"/api/v1/automations/{quote(automation_id, safe='')}/experiments/export",
            params={"format": format},
        )
        if response.status_code >= 400:
            _check_response(response)
        return response.text

    def create_stream(
        self,
        automation_id: str,
        body: Optional[dict[str, Any]] = None,
    ) -> Iterator[str]:
        def lines() -> Iterator[str]:
            with self._root._http.stream(
                "POST",
                f"/api/v1/automations/{quote(automation_id, safe='')}/experiments/stream",
                json=body or {},
            ) as response:
                if response.status_code >= 400:
                    response.read()
                    _check_response(response)
                for line in response.iter_lines():
                    if line:
                        yield line

        return lines()


class RunsResource:
    def __init__(self, root: EigenpalClient) -> None:
        self._root = root
        self.artifacts = RunsArtifactsResource(root)
        self.scores = RunsScoresResource(root)
        self.reviews = RunsReviewsResource(root)
        self.trace = RunsTraceResource(root)

    def list(self, **query: Any) -> Any:
        return self._root._request("GET", "/api/v1/runs", params=query or None)

    def get(self, run_id: str, *, expand: Optional[RunExpand] = None) -> Any:
        params = {"expand": _format_run_expand(expand)} if expand is not None else None
        return self._root._request("GET", f"/api/v1/runs/{quote(run_id, safe='')}", params=params)

    def cancel(self, run_id: str) -> Any:
        return self._root._request("POST", f"/api/v1/runs/{quote(run_id, safe='')}/cancel")

    def promote(self, run_id: str, body: Optional[dict[str, Any]] = None) -> Any:
        return self._root._request(
            "POST",
            f"/api/v1/runs/{quote(run_id, safe='')}/promote",
            json=body or {},
        )

    def rerun(
        self,
        run_id: str,
        *,
        version: Optional[str] = None,
        wait_for_completion: Optional[int] = None,
    ) -> Any:
        return self._root.rerun(run_id, version=version, wait_for_completion=wait_for_completion)

    def usage(self, run_id: str) -> Any:
        return self._root._request("GET", f"/api/v1/runs/{quote(run_id, safe='')}/usage")

    def steps(self, run_id: str) -> Any:
        return self._root._request("GET", f"/api/v1/runs/{quote(run_id, safe='')}/steps")

    def events(self, run_id: str) -> Any:
        return self._root._request("GET", f"/api/v1/runs/{quote(run_id, safe='')}/events")


class RunsScoresResource:
    def __init__(self, root: EigenpalClient) -> None:
        self._root = root

    def list(self, run_id: str) -> Any:
        return self._root._request("GET", f"/api/v1/runs/{quote(run_id, safe='')}/scores")


class RunsArtifactsResource:
    def __init__(self, root: EigenpalClient) -> None:
        self._root = root

    def list(self, run_id: str) -> Any:
        return self._root._request("GET", f"/api/v1/runs/{quote(run_id, safe='')}/artifacts")

    def download(self, run_id: str, path: str) -> BinaryIO | bytes:
        response = self._root._http.get(
            f"/api/v1/runs/{quote(run_id, safe='')}/artifacts/{_quote_path(path)}"
        )
        _assert_json_response(response) if response.status_code >= 400 else None
        if response.status_code >= 400:
            _check_response(response)
        return response.content


class RunsReviewsResource:
    def __init__(self, root: EigenpalClient) -> None:
        self._root = root

    def get(self, run_id: str) -> Any:
        return self._root._request("GET", f"/api/v1/runs/{quote(run_id, safe='')}/reviews")

    def update(self, run_id: str, body: dict[str, Any]) -> Any:
        return self._root._request(
            "PUT",
            f"/api/v1/runs/{quote(run_id, safe='')}/reviews",
            json=body,
        )

    def close(self, run_id: str, body: Optional[dict[str, Any]] = None) -> Any:
        return self._root._request(
            "PATCH",
            f"/api/v1/runs/{quote(run_id, safe='')}/reviews",
            json=body or {},
        )

    def clear(self, run_id: str) -> Any:
        return self._root._request("DELETE", f"/api/v1/runs/{quote(run_id, safe='')}/reviews")

    def list_expected(self, run_id: str) -> Any:
        return self._root._request(
            "GET",
            f"/api/v1/runs/{quote(run_id, safe='')}/reviews/expected",
        )

    def copy_output_to_expected(
        self,
        run_id: str,
        output_file_name: str,
        *,
        expected_name: Optional[str] = None,
    ) -> Any:
        body = {"outputFileName": output_file_name}
        if expected_name is not None:
            body["expectedName"] = expected_name
        return self._root._request(
            "POST",
            f"/api/v1/runs/{quote(run_id, safe='')}/reviews/expected",
            json=body,
        )

    def upload_expected(
        self,
        run_id: str,
        file: Path | dict[str, Any] | BinaryIO,
        *,
        name: Optional[str] = None,
    ) -> Any:
        data = {"name": name} if name is not None else None
        return self._root._request(
            "POST",
            f"/api/v1/runs/{quote(run_id, safe='')}/reviews/expected",
            files={"file": to_upload_tuple(file)},
            data=data,
        )

    def download_expected(self, run_id: str, filename: str) -> bytes:
        response = self._root._http.get(
            f"/api/v1/runs/{quote(run_id, safe='')}/reviews/expected/{_quote_path(filename)}"
        )
        if response.status_code >= 400:
            _check_response(response)
        return response.content

    def rename_expected(self, run_id: str, filename: str, new_filename: str) -> Any:
        return self._root._request(
            "PATCH",
            f"/api/v1/runs/{quote(run_id, safe='')}/reviews/expected/{_quote_path(filename)}",
            json={"name": new_filename},
        )

    def delete_expected(self, run_id: str, filename: str) -> Any:
        return self._root._request(
            "DELETE",
            f"/api/v1/runs/{quote(run_id, safe='')}/reviews/expected/{_quote_path(filename)}",
        )


class RunsTraceResource:
    def __init__(self, root: EigenpalClient) -> None:
        self._root = root

    def get(self, run_id: str) -> Any:
        return self._root._request("GET", f"/api/v1/runs/{quote(run_id, safe='')}/trace")


class FilesResource:
    def __init__(self, root: EigenpalClient) -> None:
        self._root = root

    def upload(self, file: Path | dict[str, Any] | BinaryIO) -> Any:
        return self._root._request("POST", "/api/v1/files", files={"file": to_upload_tuple(file)})

    def get(self, file_id: str) -> Any:
        return self._root._request("GET", f"/api/v1/files/{quote(file_id, safe='')}")

    def download(self, file_id: str) -> bytes:
        response = self._root._http.get(f"/api/v1/files/{quote(file_id, safe='')}/content")
        if response.status_code >= 400:
            _check_response(response)
        return response.content

    def delete(self, file_id: str) -> Any:
        return self._root._request("DELETE", f"/api/v1/files/{quote(file_id, safe='')}")
