from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="AgentsFilesPutResponse200")



@_attrs_define
class AgentsFilesPutResponse200:
    """ 
        Attributes:
            ok (bool):
            path (str):
     """

    ok: bool
    path: str





    def to_dict(self) -> dict[str, Any]:
        ok = self.ok

        path = self.path


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "ok": ok,
            "path": path,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ok = d.pop("ok")

        path = d.pop("path")

        agents_files_put_response_200 = cls(
            ok=ok,
            path=path,
        )

        return agents_files_put_response_200

