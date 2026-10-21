from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Literal, cast






T = TypeVar("T", bound="AgentEvaluationEvaluatorsAdditionalPropertyType2")



@_attrs_define
class AgentEvaluationEvaluatorsAdditionalPropertyType2:
    """
        Attributes:
            kind (Literal['llm-judge']):
            prompt (str):
            model (str | Unset):
     """

    kind: Literal['llm-judge']
    prompt: str
    model: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        kind = self.kind

        prompt = self.prompt

        model = self.model


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "kind": kind,
            "prompt": prompt,
        })
        if model is not UNSET:
            field_dict["model"] = model

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = cast(Literal['llm-judge'] , d.pop("kind"))
        if kind != 'llm-judge':
            raise ValueError(f"kind must match const 'llm-judge', got '{kind}'")

        prompt = d.pop("prompt")

        model = d.pop("model", UNSET)

        agent_evaluation_evaluators_additional_property_type_2 = cls(
            kind=kind,
            prompt=prompt,
            model=model,
        )

        return agent_evaluation_evaluators_additional_property_type_2
