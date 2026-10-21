from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.agent_evaluation_evaluators_additional_property_type_1_options_rules import AgentEvaluationEvaluatorsAdditionalPropertyType1OptionsRules





T = TypeVar("T", bound="AgentEvaluationEvaluatorsAdditionalPropertyType1Options")



@_attrs_define
class AgentEvaluationEvaluatorsAdditionalPropertyType1Options:
    """
        Attributes:
            rules (AgentEvaluationEvaluatorsAdditionalPropertyType1OptionsRules | Unset):
            paths (list[str] | Unset):
            unordered_paths (list[str] | Unset):
            numeric_tolerance (float | Unset):
            allow_extra_fields (bool | Unset):
     """

    rules: AgentEvaluationEvaluatorsAdditionalPropertyType1OptionsRules | Unset = UNSET
    paths: list[str] | Unset = UNSET
    unordered_paths: list[str] | Unset = UNSET
    numeric_tolerance: float | Unset = UNSET
    allow_extra_fields: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.agent_evaluation_evaluators_additional_property_type_1_options_rules import AgentEvaluationEvaluatorsAdditionalPropertyType1OptionsRules # noqa: PLC0415
        rules: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rules, Unset):
            rules = self.rules.to_dict()

        paths: list[str] | Unset = UNSET
        if not isinstance(self.paths, Unset):
            paths = self.paths



        unordered_paths: list[str] | Unset = UNSET
        if not isinstance(self.unordered_paths, Unset):
            unordered_paths = self.unordered_paths



        numeric_tolerance = self.numeric_tolerance

        allow_extra_fields = self.allow_extra_fields


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if rules is not UNSET:
            field_dict["rules"] = rules
        if paths is not UNSET:
            field_dict["paths"] = paths
        if unordered_paths is not UNSET:
            field_dict["unorderedPaths"] = unordered_paths
        if numeric_tolerance is not UNSET:
            field_dict["numericTolerance"] = numeric_tolerance
        if allow_extra_fields is not UNSET:
            field_dict["allowExtraFields"] = allow_extra_fields

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_evaluation_evaluators_additional_property_type_1_options_rules import AgentEvaluationEvaluatorsAdditionalPropertyType1OptionsRules # noqa: PLC0415
        d = dict(src_dict)
        _rules = d.pop("rules", UNSET)
        rules: AgentEvaluationEvaluatorsAdditionalPropertyType1OptionsRules | Unset
        if isinstance(_rules,  Unset):
            rules = UNSET
        else:
            rules = AgentEvaluationEvaluatorsAdditionalPropertyType1OptionsRules.from_dict(_rules)




        paths = cast(list[str], d.pop("paths", UNSET))


        unordered_paths = cast(list[str], d.pop("unorderedPaths", UNSET))


        numeric_tolerance = d.pop("numericTolerance", UNSET)

        allow_extra_fields = d.pop("allowExtraFields", UNSET)

        agent_evaluation_evaluators_additional_property_type_1_options = cls(
            rules=rules,
            paths=paths,
            unordered_paths=unordered_paths,
            numeric_tolerance=numeric_tolerance,
            allow_extra_fields=allow_extra_fields,
        )

        return agent_evaluation_evaluators_additional_property_type_1_options
