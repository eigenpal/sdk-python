from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="UpdateEmailServerRequestType2")



@_attrs_define
class UpdateEmailServerRequestType2:
    """
        Attributes:
            name (str | Unset):
            enabled (bool | Unset):
            transport (Any | Unset):
     """

    name: str | Unset = UNSET
    enabled: bool | Unset = UNSET
    transport: Any | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        enabled = self.enabled

        transport = self.transport


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if transport is not UNSET:
            field_dict["transport"] = transport

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        enabled = d.pop("enabled", UNSET)

        transport = d.pop("transport", UNSET)

        update_email_server_request_type_2 = cls(
            name=name,
            enabled=enabled,
            transport=transport,
        )

        return update_email_server_request_type_2
