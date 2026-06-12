from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="RunDebug")



@_attrs_define
class RunDebug:
    """
        Attributes:
            observability (Any): Execution phase timeline and structured failure.
            trace_id (None | str | Unset): Workflow trace id for span lookup (workflow runs only).
     """

    observability: Any
    trace_id: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        observability = self.observability

        trace_id: None | str | Unset
        if isinstance(self.trace_id, Unset):
            trace_id = UNSET
        else:
            trace_id = self.trace_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "observability": observability,
        })
        if trace_id is not UNSET:
            field_dict["traceId"] = trace_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        observability = d.pop("observability")

        def _parse_trace_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        trace_id = _parse_trace_id(d.pop("traceId", UNSET))


        run_debug = cls(
            observability=observability,
            trace_id=trace_id,
        )

        return run_debug
