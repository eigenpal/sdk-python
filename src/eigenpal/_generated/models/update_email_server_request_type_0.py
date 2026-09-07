from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Literal, cast






T = TypeVar("T", bound="UpdateEmailServerRequestType0")



@_attrs_define
class UpdateEmailServerRequestType0:
    """
        Attributes:
            transport (Literal['resend']):
            from_email (str):
            from_name (str):
            name (str | Unset):
            enabled (bool | Unset):
            api_key (str | Unset):
     """

    transport: Literal['resend']
    from_email: str
    from_name: str
    name: str | Unset = UNSET
    enabled: bool | Unset = UNSET
    api_key: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        transport = self.transport

        from_email = self.from_email

        from_name = self.from_name

        name = self.name

        enabled = self.enabled

        api_key = self.api_key


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "transport": transport,
            "fromEmail": from_email,
            "fromName": from_name,
        })
        if name is not UNSET:
            field_dict["name"] = name
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if api_key is not UNSET:
            field_dict["apiKey"] = api_key

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        transport = cast(Literal['resend'] , d.pop("transport"))
        if transport != 'resend':
            raise ValueError(f"transport must match const 'resend', got '{transport}'")

        from_email = d.pop("fromEmail")

        from_name = d.pop("fromName")

        name = d.pop("name", UNSET)

        enabled = d.pop("enabled", UNSET)

        api_key = d.pop("apiKey", UNSET)

        update_email_server_request_type_0 = cls(
            transport=transport,
            from_email=from_email,
            from_name=from_name,
            name=name,
            enabled=enabled,
            api_key=api_key,
        )

        return update_email_server_request_type_0
