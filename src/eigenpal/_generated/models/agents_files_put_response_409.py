from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="AgentsFilesPutResponse409")



@_attrs_define
class AgentsFilesPutResponse409:
    """ 
        Attributes:
            error (str):
     """

    error: str





    def to_dict(self) -> dict[str, Any]:
        error = self.error


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "error": error,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        error = d.pop("error")

        agents_files_put_response_409 = cls(
            error=error,
        )

        return agents_files_put_response_409

