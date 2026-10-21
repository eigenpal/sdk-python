from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="AgentEvaluatorConfigResponseSource")



@_attrs_define
class AgentEvaluatorConfigResponseSource:
    """
        Attributes:
            path (str):
            ref (str):
            commit (str):
     """

    path: str
    ref: str
    commit: str





    def to_dict(self) -> dict[str, Any]:
        path = self.path

        ref = self.ref

        commit = self.commit


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "path": path,
            "ref": ref,
            "commit": commit,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        path = d.pop("path")

        ref = d.pop("ref")

        commit = d.pop("commit")

        agent_evaluator_config_response_source = cls(
            path=path,
            ref=ref,
            commit=commit,
        )

        return agent_evaluator_config_response_source
