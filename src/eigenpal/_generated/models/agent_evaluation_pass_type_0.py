from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Literal, cast






T = TypeVar("T", bound="AgentEvaluationPassType0")



@_attrs_define
class AgentEvaluationPassType0:
    """
        Attributes:
            kind (Literal['callback']):
     """

    kind: Literal['callback']





    def to_dict(self) -> dict[str, Any]:
        kind = self.kind


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "kind": kind,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = cast(Literal['callback'] , d.pop("kind"))
        if kind != 'callback':
            raise ValueError(f"kind must match const 'callback', got '{kind}'")

        agent_evaluation_pass_type_0 = cls(
            kind=kind,
        )

        return agent_evaluation_pass_type_0
