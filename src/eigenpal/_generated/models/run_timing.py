from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="RunTiming")



@_attrs_define
class RunTiming:
    """
        Attributes:
            created_at (str):
            started_at (None | str):
            completed_at (None | str):
            duration_ms (float | None):
            cancel_requested_at (None | str): When the user requested cancel; status may still be `running` until the worker
                stops.
     """

    created_at: str
    started_at: None | str
    completed_at: None | str
    duration_ms: float | None
    cancel_requested_at: None | str





    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        started_at: None | str
        started_at = self.started_at

        completed_at: None | str
        completed_at = self.completed_at

        duration_ms: float | None
        duration_ms = self.duration_ms

        cancel_requested_at: None | str
        cancel_requested_at = self.cancel_requested_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "createdAt": created_at,
            "startedAt": started_at,
            "completedAt": completed_at,
            "durationMs": duration_ms,
            "cancelRequestedAt": cancel_requested_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = d.pop("createdAt")

        def _parse_started_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        started_at = _parse_started_at(d.pop("startedAt"))


        def _parse_completed_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        completed_at = _parse_completed_at(d.pop("completedAt"))


        def _parse_duration_ms(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        duration_ms = _parse_duration_ms(d.pop("durationMs"))


        def _parse_cancel_requested_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        cancel_requested_at = _parse_cancel_requested_at(d.pop("cancelRequestedAt"))


        run_timing = cls(
            created_at=created_at,
            started_at=started_at,
            completed_at=completed_at,
            duration_ms=duration_ms,
            cancel_requested_at=cancel_requested_at,
        )

        return run_timing
