from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="RerunAgentRunBody")



@_attrs_define
class RerunAgentRunBody:
    """ 
        Attributes:
            source_ref (str | Unset): Git source ref to use for the rerun. Defaults to latest. Pass the source run version
                to reproduce the previous version. Example: latest.
     """

    source_ref: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        source_ref = self.source_ref


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if source_ref is not UNSET:
            field_dict["sourceRef"] = source_ref

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        source_ref = d.pop("sourceRef", UNSET)

        rerun_agent_run_body = cls(
            source_ref=source_ref,
        )

        return rerun_agent_run_body

