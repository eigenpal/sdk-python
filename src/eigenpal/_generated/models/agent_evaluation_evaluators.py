from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.agent_evaluation_evaluators_additional_property_type_0 import AgentEvaluationEvaluatorsAdditionalPropertyType0
  from ..models.agent_evaluation_evaluators_additional_property_type_1 import AgentEvaluationEvaluatorsAdditionalPropertyType1
  from ..models.agent_evaluation_evaluators_additional_property_type_2 import AgentEvaluationEvaluatorsAdditionalPropertyType2





T = TypeVar("T", bound="AgentEvaluationEvaluators")



@_attrs_define
class AgentEvaluationEvaluators:


    additional_properties: dict[str, AgentEvaluationEvaluatorsAdditionalPropertyType0 | AgentEvaluationEvaluatorsAdditionalPropertyType1 | AgentEvaluationEvaluatorsAdditionalPropertyType2] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.agent_evaluation_evaluators_additional_property_type_0 import AgentEvaluationEvaluatorsAdditionalPropertyType0 # noqa: PLC0415
        from ..models.agent_evaluation_evaluators_additional_property_type_1 import AgentEvaluationEvaluatorsAdditionalPropertyType1 # noqa: PLC0415
        from ..models.agent_evaluation_evaluators_additional_property_type_2 import AgentEvaluationEvaluatorsAdditionalPropertyType2 # noqa: PLC0415

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():

            if isinstance(prop, AgentEvaluationEvaluatorsAdditionalPropertyType0):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, AgentEvaluationEvaluatorsAdditionalPropertyType1):
                field_dict[prop_name] = prop.to_dict()
            else:
                field_dict[prop_name] = prop.to_dict()



        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_evaluation_evaluators_additional_property_type_0 import AgentEvaluationEvaluatorsAdditionalPropertyType0 # noqa: PLC0415
        from ..models.agent_evaluation_evaluators_additional_property_type_1 import AgentEvaluationEvaluatorsAdditionalPropertyType1 # noqa: PLC0415
        from ..models.agent_evaluation_evaluators_additional_property_type_2 import AgentEvaluationEvaluatorsAdditionalPropertyType2 # noqa: PLC0415
        d = dict(src_dict)
        agent_evaluation_evaluators = cls(
        )


        additional_properties = {}
        for prop_name, prop_dict in d.items():
            def _parse_additional_property(data: object) -> AgentEvaluationEvaluatorsAdditionalPropertyType0 | AgentEvaluationEvaluatorsAdditionalPropertyType1 | AgentEvaluationEvaluatorsAdditionalPropertyType2:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_0 = AgentEvaluationEvaluatorsAdditionalPropertyType0.from_dict(data)



                    return additional_property_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_1 = AgentEvaluationEvaluatorsAdditionalPropertyType1.from_dict(data)



                    return additional_property_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                additional_property_type_2 = AgentEvaluationEvaluatorsAdditionalPropertyType2.from_dict(data)



                return additional_property_type_2

            additional_property = _parse_additional_property(prop_dict)

            additional_properties[prop_name] = additional_property

        agent_evaluation_evaluators.additional_properties = additional_properties
        return agent_evaluation_evaluators

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> AgentEvaluationEvaluatorsAdditionalPropertyType0 | AgentEvaluationEvaluatorsAdditionalPropertyType1 | AgentEvaluationEvaluatorsAdditionalPropertyType2:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: AgentEvaluationEvaluatorsAdditionalPropertyType0 | AgentEvaluationEvaluatorsAdditionalPropertyType1 | AgentEvaluationEvaluatorsAdditionalPropertyType2) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
