from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.run_start_body_files_additional_property_type_0_type_1_inline import RunStartBodyFilesAdditionalPropertyType0Type1Inline





T = TypeVar("T", bound="RunStartBodyFilesAdditionalPropertyType0Type1")



@_attrs_define
class RunStartBodyFilesAdditionalPropertyType0Type1:
    """
        Attributes:
            inline (RunStartBodyFilesAdditionalPropertyType0Type1Inline):
     """

    inline: RunStartBodyFilesAdditionalPropertyType0Type1Inline





    def to_dict(self) -> dict[str, Any]:
        from ..models.run_start_body_files_additional_property_type_0_type_1_inline import RunStartBodyFilesAdditionalPropertyType0Type1Inline
        inline = self.inline.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "$inline": inline,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.run_start_body_files_additional_property_type_0_type_1_inline import RunStartBodyFilesAdditionalPropertyType0Type1Inline
        d = dict(src_dict)
        inline = RunStartBodyFilesAdditionalPropertyType0Type1Inline.from_dict(d.pop("$inline"))




        run_start_body_files_additional_property_type_0_type_1 = cls(
            inline=inline,
        )

        return run_start_body_files_additional_property_type_0_type_1
