from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="RunStartBodyFilesAdditionalPropertyType0Type1Inline")



@_attrs_define
class RunStartBodyFilesAdditionalPropertyType0Type1Inline:
    """
        Attributes:
            filename (str): Original filename for the materialized artifact
            mime_type (str): MIME type for the materialized artifact
            base64 (str): Base64-encoded file bytes
     """

    filename: str
    mime_type: str
    base64: str





    def to_dict(self) -> dict[str, Any]:
        filename = self.filename

        mime_type = self.mime_type

        base64 = self.base64


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "filename": filename,
            "mimeType": mime_type,
            "base64": base64,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        filename = d.pop("filename")

        mime_type = d.pop("mimeType")

        base64 = d.pop("base64")

        run_start_body_files_additional_property_type_0_type_1_inline = cls(
            filename=filename,
            mime_type=mime_type,
            base64=base64,
        )

        return run_start_body_files_additional_property_type_0_type_1_inline
