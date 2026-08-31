from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="TemplateStagingResponse")



@_attrs_define
class TemplateStagingResponse:
    """
        Attributes:
            cleaned (bool | Unset):
            finalized (bool | Unset):
     """

    cleaned: bool | Unset = UNSET
    finalized: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        cleaned = self.cleaned

        finalized = self.finalized


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if cleaned is not UNSET:
            field_dict["cleaned"] = cleaned
        if finalized is not UNSET:
            field_dict["finalized"] = finalized

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cleaned = d.pop("cleaned", UNSET)

        finalized = d.pop("finalized", UNSET)

        template_staging_response = cls(
            cleaned=cleaned,
            finalized=finalized,
        )

        return template_staging_response
