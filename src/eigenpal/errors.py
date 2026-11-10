"""Typed exceptions raised by the EigenPal SDK.

Every non-2xx HTTP response is mapped to one of these subclasses based on
the status code. The original API error envelope (`{ issues, requestId, hint?, docsUrl?, conflictingWorkflowId? }`)
is preserved on the exception's `envelope` attribute when present.
"""

from __future__ import annotations

from typing import Any, List, Optional


class EigenpalError(Exception):
    """Base class for every error the SDK raises."""

    def __init__(
        self,
        message: str,
        *,
        status: int,
        envelope: Optional[dict[str, Any]] = None,
    ) -> None:
        super().__init__(message)
        self.status = status
        self.envelope = envelope
        self.request_id: Optional[str] = (envelope or {}).get("requestId")


class EigenpalAuthError(EigenpalError):
    def __init__(self, envelope: Optional[dict[str, Any]] = None) -> None:
        msg = _first_issue_message(envelope) or (
            "Invalid or missing API key. Generate one at studio.eigenpal.com → "
            "Settings → API Keys; pass it as EigenpalClient(api_key=...) or "
            "set EIGENPAL_API_KEY."
        )
        super().__init__(msg, status=401, envelope=envelope)


class EigenpalForbiddenError(EigenpalError):
    def __init__(self, envelope: Optional[dict[str, Any]] = None) -> None:
        msg = _first_issue_message(envelope) or "forbidden"
        super().__init__(msg, status=403, envelope=envelope)


class EigenpalNotFoundError(EigenpalError):
    def __init__(self, envelope: Optional[dict[str, Any]] = None) -> None:
        msg = _first_issue_message(envelope) or "not found"
        super().__init__(msg, status=404, envelope=envelope)


class EigenpalValidationError(EigenpalError):
    def __init__(self, envelope: dict[str, Any]) -> None:
        issues: List[dict[str, Any]] = list(envelope.get("issues") or [])
        if issues:
            first = issues[0]
            msg = f"{first.get('field', '<root>')}: {first.get('message', 'invalid')}"
        else:
            msg = "validation error"
        super().__init__(msg, status=400, envelope=envelope)
        self.issues = issues


class EigenpalConflictError(EigenpalError):
    """409: the resource changed or already exists (e.g. a stale ``expectedUpdatedAt``)."""

    def __init__(self, envelope: Optional[dict[str, Any]] = None) -> None:
        msg = _first_issue_message(envelope) or "conflict"
        super().__init__(msg, status=409, envelope=envelope)


class EigenpalPayloadTooLargeError(EigenpalError):
    """413: the request body or uploaded file is larger than the server accepts."""

    def __init__(self, envelope: Optional[dict[str, Any]] = None) -> None:
        msg = _first_issue_message(envelope) or "payload too large"
        super().__init__(msg, status=413, envelope=envelope)


class EigenpalRateLimitError(EigenpalError):
    def __init__(
        self,
        envelope: Optional[dict[str, Any]] = None,
        retry_after: Optional[int] = None,
    ) -> None:
        super().__init__("rate limit exceeded", status=429, envelope=envelope)
        self.retry_after = retry_after


class EigenpalServerError(EigenpalError):
    def __init__(self, status: int, envelope: Optional[dict[str, Any]] = None) -> None:
        msg = _first_issue_message(envelope) or "internal server error"
        super().__init__(msg, status=status, envelope=envelope)


class EigenpalTimeoutError(EigenpalError):
    def __init__(self, message: str = "operation timed out") -> None:
        super().__init__(message, status=0)


def _first_issue_message(envelope: Optional[dict[str, Any]]) -> Optional[str]:
    if not envelope:
        return None
    issues = envelope.get("issues")
    if isinstance(issues, list) and issues:
        first = issues[0]
        if isinstance(first, dict):
            return first.get("message")
    return None


def error_from_response(
    status: int,
    envelope: Optional[dict[str, Any]],
    retry_after: Optional[int] = None,
) -> EigenpalError:
    """Map an HTTP status code into the appropriate typed exception."""
    if status == 400:
        return EigenpalValidationError(envelope or {"issues": [], "requestId": ""})
    if status == 401:
        return EigenpalAuthError(envelope)
    if status == 403:
        return EigenpalForbiddenError(envelope)
    if status == 404:
        return EigenpalNotFoundError(envelope)
    if status == 409:
        return EigenpalConflictError(envelope)
    if status == 413:
        return EigenpalPayloadTooLargeError(envelope)
    if status == 429:
        return EigenpalRateLimitError(envelope, retry_after)
    if status >= 500:
        return EigenpalServerError(status, envelope)
    message = _first_issue_message(envelope) or f"unexpected status {status}"
    return EigenpalError(message, status=status, envelope=envelope)
