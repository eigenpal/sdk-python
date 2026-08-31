from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Literal, cast






T = TypeVar("T", bound="PublicModelCost")



@_attrs_define
class PublicModelCost:
    """
        Attributes:
            unit (Literal['credits']):
            credits_per_page (float | Unset):
     """

    unit: Literal['credits']
    credits_per_page: float | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        unit = self.unit

        credits_per_page = self.credits_per_page


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "unit": unit,
        })
        if credits_per_page is not UNSET:
            field_dict["creditsPerPage"] = credits_per_page

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        unit = cast(Literal['credits'] , d.pop("unit"))
        if unit != 'credits':
            raise ValueError(f"unit must match const 'credits', got '{unit}'")

        credits_per_page = d.pop("creditsPerPage", UNSET)

        public_model_cost = cls(
            unit=unit,
            credits_per_page=credits_per_page,
        )

        return public_model_cost
