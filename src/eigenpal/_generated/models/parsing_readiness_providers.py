from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="ParsingReadinessProviders")



@_attrs_define
class ParsingReadinessProviders:
    """
        Attributes:
            ocr (None | str):
            vision (None | str):
     """

    ocr: None | str
    vision: None | str





    def to_dict(self) -> dict[str, Any]:
        ocr: None | str
        ocr = self.ocr

        vision: None | str
        vision = self.vision


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "ocr": ocr,
            "vision": vision,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_ocr(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        ocr = _parse_ocr(d.pop("ocr"))


        def _parse_vision(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        vision = _parse_vision(d.pop("vision"))


        parsing_readiness_providers = cls(
            ocr=ocr,
            vision=vision,
        )

        return parsing_readiness_providers
