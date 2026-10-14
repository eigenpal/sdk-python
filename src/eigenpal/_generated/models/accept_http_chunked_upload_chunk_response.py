from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="AcceptHttpChunkedUploadChunkResponse")



@_attrs_define
class AcceptHttpChunkedUploadChunkResponse:
    """
        Attributes:
            accepted (bool):
            chunk_index (int):
            size (int):
     """

    accepted: bool
    chunk_index: int
    size: int





    def to_dict(self) -> dict[str, Any]:
        accepted = self.accepted

        chunk_index = self.chunk_index

        size = self.size


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "accepted": accepted,
            "chunkIndex": chunk_index,
            "size": size,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        accepted = d.pop("accepted")

        chunk_index = d.pop("chunkIndex")

        size = d.pop("size")

        accept_http_chunked_upload_chunk_response = cls(
            accepted=accepted,
            chunk_index=chunk_index,
            size=size,
        )

        return accept_http_chunked_upload_chunk_response
