from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="TestEmailServerRequest")



@_attrs_define
class TestEmailServerRequest:
    """
        Attributes:
            to (str):
     """

    to: str





    def to_dict(self) -> dict[str, Any]:
        to = self.to


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "to": to,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        to = d.pop("to")

        test_email_server_request = cls(
            to=to,
        )

        return test_email_server_request
