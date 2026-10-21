from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Literal, cast

if TYPE_CHECKING:
  from ..models.agent_evaluation_evaluators_additional_property_type_1_options import AgentEvaluationEvaluatorsAdditionalPropertyType1Options





T = TypeVar("T", bound="AgentEvaluationEvaluatorsAdditionalPropertyType1")



@_attrs_define
class AgentEvaluationEvaluatorsAdditionalPropertyType1:
    """
        Attributes:
            kind (Literal['exact-diff']):
            options (AgentEvaluationEvaluatorsAdditionalPropertyType1Options | Unset):
     """

    kind: Literal['exact-diff']
    options: AgentEvaluationEvaluatorsAdditionalPropertyType1Options | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.agent_evaluation_evaluators_additional_property_type_1_options import AgentEvaluationEvaluatorsAdditionalPropertyType1Options # noqa: PLC0415
        kind = self.kind

        options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "kind": kind,
        })
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_evaluation_evaluators_additional_property_type_1_options import AgentEvaluationEvaluatorsAdditionalPropertyType1Options # noqa: PLC0415
        d = dict(src_dict)
        kind = cast(Literal['exact-diff'] , d.pop("kind"))
        if kind != 'exact-diff':
            raise ValueError(f"kind must match const 'exact-diff', got '{kind}'")

        _options = d.pop("options", UNSET)
        options: AgentEvaluationEvaluatorsAdditionalPropertyType1Options | Unset
        if isinstance(_options,  Unset):
            options = UNSET
        else:
            options = AgentEvaluationEvaluatorsAdditionalPropertyType1Options.from_dict(_options)




        agent_evaluation_evaluators_additional_property_type_1 = cls(
            kind=kind,
            options=options,
        )

        return agent_evaluation_evaluators_additional_property_type_1
