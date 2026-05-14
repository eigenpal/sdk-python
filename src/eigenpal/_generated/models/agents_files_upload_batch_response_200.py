from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="AgentsFilesUploadBatchResponse200")



@_attrs_define
class AgentsFilesUploadBatchResponse200:
    """ 
        Attributes:
            ok (bool):
            files (list[str]):
     """

    ok: bool
    files: list[str]





    def to_dict(self) -> dict[str, Any]:
        ok = self.ok

        files = self.files




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "ok": ok,
            "files": files,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ok = d.pop("ok")

        files = cast(list[str], d.pop("files"))


        agents_files_upload_batch_response_200 = cls(
            ok=ok,
            files=files,
        )

        return agents_files_upload_batch_response_200

