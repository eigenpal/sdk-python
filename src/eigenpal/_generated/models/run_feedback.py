from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="RunFeedback")



@_attrs_define
class RunFeedback:
    """ Canonical human feedback object for a run. Use feedback endpoints to read, update, clear, or promote it to a dataset
    example.

        Attributes:
            rating (None | str): Human verdict for the run: `pass`, `fail`, or `partial`. This is separate from evaluator
                `score` values.
            status (None | str): Review lifecycle status: `open` needs attention, `resolved` was addressed, and `ignored`
                was acknowledged but intentionally not acted on.
            body (str): Human feedback text written for this run.
            created_at (None | str): When feedback was first created.
            created_by (None | str): User id that created the feedback.
            created_by_email (None | str): Email of the user that created the feedback.
            updated_at (None | str): When feedback was last changed.
            resolved_at (None | str): When feedback was marked resolved or ignored.
            resolved_by (None | str): User id that resolved or ignored the feedback.
            resolved_by_email (None | str): Email of the user that resolved or ignored the feedback.
            resolved_by_session_id (None | str): Agent session id that resolved the feedback, when applicable.
            promoted_example_name (None | str): Dataset example name created from this feedback, if promoted.
     """

    rating: None | str
    status: None | str
    body: str
    created_at: None | str
    created_by: None | str
    created_by_email: None | str
    updated_at: None | str
    resolved_at: None | str
    resolved_by: None | str
    resolved_by_email: None | str
    resolved_by_session_id: None | str
    promoted_example_name: None | str





    def to_dict(self) -> dict[str, Any]:
        rating: None | str
        rating = self.rating

        status: None | str
        status = self.status

        body = self.body

        created_at: None | str
        created_at = self.created_at

        created_by: None | str
        created_by = self.created_by

        created_by_email: None | str
        created_by_email = self.created_by_email

        updated_at: None | str
        updated_at = self.updated_at

        resolved_at: None | str
        resolved_at = self.resolved_at

        resolved_by: None | str
        resolved_by = self.resolved_by

        resolved_by_email: None | str
        resolved_by_email = self.resolved_by_email

        resolved_by_session_id: None | str
        resolved_by_session_id = self.resolved_by_session_id

        promoted_example_name: None | str
        promoted_example_name = self.promoted_example_name


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "rating": rating,
            "status": status,
            "body": body,
            "createdAt": created_at,
            "createdBy": created_by,
            "createdByEmail": created_by_email,
            "updatedAt": updated_at,
            "resolvedAt": resolved_at,
            "resolvedBy": resolved_by,
            "resolvedByEmail": resolved_by_email,
            "resolvedBySessionId": resolved_by_session_id,
            "promotedExampleName": promoted_example_name,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_rating(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        rating = _parse_rating(d.pop("rating"))


        def _parse_status(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        status = _parse_status(d.pop("status"))


        body = d.pop("body")

        def _parse_created_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        created_at = _parse_created_at(d.pop("createdAt"))


        def _parse_created_by(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        created_by = _parse_created_by(d.pop("createdBy"))


        def _parse_created_by_email(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        created_by_email = _parse_created_by_email(d.pop("createdByEmail"))


        def _parse_updated_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        updated_at = _parse_updated_at(d.pop("updatedAt"))


        def _parse_resolved_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        resolved_at = _parse_resolved_at(d.pop("resolvedAt"))


        def _parse_resolved_by(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        resolved_by = _parse_resolved_by(d.pop("resolvedBy"))


        def _parse_resolved_by_email(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        resolved_by_email = _parse_resolved_by_email(d.pop("resolvedByEmail"))


        def _parse_resolved_by_session_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        resolved_by_session_id = _parse_resolved_by_session_id(d.pop("resolvedBySessionId"))


        def _parse_promoted_example_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        promoted_example_name = _parse_promoted_example_name(d.pop("promotedExampleName"))


        run_feedback = cls(
            rating=rating,
            status=status,
            body=body,
            created_at=created_at,
            created_by=created_by,
            created_by_email=created_by_email,
            updated_at=updated_at,
            resolved_at=resolved_at,
            resolved_by=resolved_by,
            resolved_by_email=resolved_by_email,
            resolved_by_session_id=resolved_by_session_id,
            promoted_example_name=promoted_example_name,
        )

        return run_feedback
