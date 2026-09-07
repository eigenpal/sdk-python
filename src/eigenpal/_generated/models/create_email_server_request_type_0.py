from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Literal, cast






T = TypeVar("T", bound="CreateEmailServerRequestType0")



@_attrs_define
class CreateEmailServerRequestType0:
    """
        Attributes:
            name (str):
            transport (Literal['resend']):
            api_key (str):
            from_email (str):
            from_name (str):
            enabled (bool | Unset):  Default: True.
     """

    name: str
    transport: Literal['resend']
    api_key: str
    from_email: str
    from_name: str
    enabled: bool | Unset = True





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        transport = self.transport

        api_key = self.api_key

        from_email = self.from_email

        from_name = self.from_name

        enabled = self.enabled


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "name": name,
            "transport": transport,
            "apiKey": api_key,
            "fromEmail": from_email,
            "fromName": from_name,
        })
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        transport = cast(Literal['resend'] , d.pop("transport"))
        if transport != 'resend':
            raise ValueError(f"transport must match const 'resend', got '{transport}'")

        api_key = d.pop("apiKey")

        from_email = d.pop("fromEmail")

        from_name = d.pop("fromName")

        enabled = d.pop("enabled", UNSET)

        create_email_server_request_type_0 = cls(
            name=name,
            transport=transport,
            api_key=api_key,
            from_email=from_email,
            from_name=from_name,
            enabled=enabled,
        )

        return create_email_server_request_type_0
