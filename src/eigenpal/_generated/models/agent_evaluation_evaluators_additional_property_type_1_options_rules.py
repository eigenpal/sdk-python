from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.agent_evaluation_evaluators_additional_property_type_1_options_rules_additional_property import AgentEvaluationEvaluatorsAdditionalPropertyType1OptionsRulesAdditionalProperty





T = TypeVar("T", bound="AgentEvaluationEvaluatorsAdditionalPropertyType1OptionsRules")



@_attrs_define
class AgentEvaluationEvaluatorsAdditionalPropertyType1OptionsRules:


    additional_properties: dict[str, AgentEvaluationEvaluatorsAdditionalPropertyType1OptionsRulesAdditionalProperty] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.agent_evaluation_evaluators_additional_property_type_1_options_rules_additional_property import AgentEvaluationEvaluatorsAdditionalPropertyType1OptionsRulesAdditionalProperty # noqa: PLC0415

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()


        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_evaluation_evaluators_additional_property_type_1_options_rules_additional_property import AgentEvaluationEvaluatorsAdditionalPropertyType1OptionsRulesAdditionalProperty # noqa: PLC0415
        d = dict(src_dict)
        agent_evaluation_evaluators_additional_property_type_1_options_rules = cls(
        )


        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = AgentEvaluationEvaluatorsAdditionalPropertyType1OptionsRulesAdditionalProperty.from_dict(prop_dict)



            additional_properties[prop_name] = additional_property

        agent_evaluation_evaluators_additional_property_type_1_options_rules.additional_properties = additional_properties
        return agent_evaluation_evaluators_additional_property_type_1_options_rules

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> AgentEvaluationEvaluatorsAdditionalPropertyType1OptionsRulesAdditionalProperty:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: AgentEvaluationEvaluatorsAdditionalPropertyType1OptionsRulesAdditionalProperty) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
