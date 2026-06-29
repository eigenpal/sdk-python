from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="RunStartBodyFilesAdditionalPropertyType0Type0")



@_attrs_define
class RunStartBodyFilesAdditionalPropertyType0Type0:
    """
        Attributes:
            file_id (str): Reusable file-pool id to materialize
     """

    file_id: str





    def to_dict(self) -> dict[str, Any]:
        file_id = self.file_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "$fileId": file_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file_id = d.pop("$fileId")

        run_start_body_files_additional_property_type_0_type_0 = cls(
            file_id=file_id,
        )

        return run_start_body_files_additional_property_type_0_type_0
