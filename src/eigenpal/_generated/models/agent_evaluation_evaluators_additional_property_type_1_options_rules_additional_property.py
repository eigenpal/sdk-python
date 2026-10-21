from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.agent_evaluation_evaluators_additional_property_type_1_options_rules_additional_property_items import AgentEvaluationEvaluatorsAdditionalPropertyType1OptionsRulesAdditionalPropertyItems
from ..models.agent_evaluation_evaluators_additional_property_type_1_options_rules_additional_property_order import AgentEvaluationEvaluatorsAdditionalPropertyType1OptionsRulesAdditionalPropertyOrder
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="AgentEvaluationEvaluatorsAdditionalPropertyType1OptionsRulesAdditionalProperty")



@_attrs_define
class AgentEvaluationEvaluatorsAdditionalPropertyType1OptionsRulesAdditionalProperty:
    """
        Attributes:
            ignore (bool | Unset):
            order (AgentEvaluationEvaluatorsAdditionalPropertyType1OptionsRulesAdditionalPropertyOrder | Unset):
            items (AgentEvaluationEvaluatorsAdditionalPropertyType1OptionsRulesAdditionalPropertyItems | Unset):
            match_by (list[str] | str | Unset):
            allow_extra_fields (bool | Unset):
            numeric_tolerance (float | Unset):
     """

    ignore: bool | Unset = UNSET
    order: AgentEvaluationEvaluatorsAdditionalPropertyType1OptionsRulesAdditionalPropertyOrder | Unset = UNSET
    items: AgentEvaluationEvaluatorsAdditionalPropertyType1OptionsRulesAdditionalPropertyItems | Unset = UNSET
    match_by: list[str] | str | Unset = UNSET
    allow_extra_fields: bool | Unset = UNSET
    numeric_tolerance: float | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        ignore = self.ignore

        order: str | Unset = UNSET
        if not isinstance(self.order, Unset):
            order = self.order.value


        items: str | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = self.items.value


        match_by: list[str] | str | Unset
        if isinstance(self.match_by, Unset):
            match_by = UNSET
        elif isinstance(self.match_by, list):
            match_by = self.match_by


        else:
            match_by = self.match_by

        allow_extra_fields = self.allow_extra_fields

        numeric_tolerance = self.numeric_tolerance


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if ignore is not UNSET:
            field_dict["ignore"] = ignore
        if order is not UNSET:
            field_dict["order"] = order
        if items is not UNSET:
            field_dict["items"] = items
        if match_by is not UNSET:
            field_dict["matchBy"] = match_by
        if allow_extra_fields is not UNSET:
            field_dict["allowExtraFields"] = allow_extra_fields
        if numeric_tolerance is not UNSET:
            field_dict["numericTolerance"] = numeric_tolerance

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ignore = d.pop("ignore", UNSET)

        _order = d.pop("order", UNSET)
        order: AgentEvaluationEvaluatorsAdditionalPropertyType1OptionsRulesAdditionalPropertyOrder | Unset
        if isinstance(_order,  Unset):
            order = UNSET
        else:
            order = AgentEvaluationEvaluatorsAdditionalPropertyType1OptionsRulesAdditionalPropertyOrder(_order)




        _items = d.pop("items", UNSET)
        items: AgentEvaluationEvaluatorsAdditionalPropertyType1OptionsRulesAdditionalPropertyItems | Unset
        if isinstance(_items,  Unset):
            items = UNSET
        else:
            items = AgentEvaluationEvaluatorsAdditionalPropertyType1OptionsRulesAdditionalPropertyItems(_items)




        def _parse_match_by(data: object) -> list[str] | str | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                match_by_type_1 = cast(list[str], data)

                return match_by_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | str | Unset, data)

        match_by = _parse_match_by(d.pop("matchBy", UNSET))


        allow_extra_fields = d.pop("allowExtraFields", UNSET)

        numeric_tolerance = d.pop("numericTolerance", UNSET)

        agent_evaluation_evaluators_additional_property_type_1_options_rules_additional_property = cls(
            ignore=ignore,
            order=order,
            items=items,
            match_by=match_by,
            allow_extra_fields=allow_extra_fields,
            numeric_tolerance=numeric_tolerance,
        )

        return agent_evaluation_evaluators_additional_property_type_1_options_rules_additional_property
