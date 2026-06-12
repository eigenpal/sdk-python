from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="RunExecutionRetryNextRunType0")



@_attrs_define
class RunExecutionRetryNextRunType0:
    """
        Attributes:
            id (str):
            status (str):
     """

    id: str
    status: str





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        status = self.status


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "status": status,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        status = d.pop("status")

        run_execution_retry_next_run_type_0 = cls(
            id=id,
            status=status,
        )

        return run_execution_retry_next_run_type_0
