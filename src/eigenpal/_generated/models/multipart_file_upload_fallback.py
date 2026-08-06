from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Literal, cast






T = TypeVar("T", bound="MultipartFileUploadFallback")



@_attrs_define
class MultipartFileUploadFallback:
    """
        Attributes:
            transport (Literal['multipart']):
            url (str):
            max_file_size_bytes (int):
     """

    transport: Literal['multipart']
    url: str
    max_file_size_bytes: int





    def to_dict(self) -> dict[str, Any]:
        transport = self.transport

        url = self.url

        max_file_size_bytes = self.max_file_size_bytes


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "transport": transport,
            "url": url,
            "maxFileSizeBytes": max_file_size_bytes,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        transport = cast(Literal['multipart'] , d.pop("transport"))
        if transport != 'multipart':
            raise ValueError(f"transport must match const 'multipart', got '{transport}'")

        url = d.pop("url")

        max_file_size_bytes = d.pop("maxFileSizeBytes")

        multipart_file_upload_fallback = cls(
            transport=transport,
            url=url,
            max_file_size_bytes=max_file_size_bytes,
        )

        return multipart_file_upload_fallback
