from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from typing import Literal, cast






T = TypeVar("T", bound="PublicResendEmailServer")



@_attrs_define
class PublicResendEmailServer:
    """
        Attributes:
            id (str):
            name (str):
            enabled (bool):
            created_at (str):
            updated_at (str):
            transport (Literal['resend']):
            from_email (str):
            from_name (str):
            api_key_configured (bool):
     """

    id: str
    name: str
    enabled: bool
    created_at: str
    updated_at: str
    transport: Literal['resend']
    from_email: str
    from_name: str
    api_key_configured: bool





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        enabled = self.enabled

        created_at: str
        created_at = self.created_at

        updated_at: str
        updated_at = self.updated_at

        transport = self.transport

        from_email = self.from_email

        from_name = self.from_name

        api_key_configured = self.api_key_configured


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "name": name,
            "enabled": enabled,
            "createdAt": created_at,
            "updatedAt": updated_at,
            "transport": transport,
            "fromEmail": from_email,
            "fromName": from_name,
            "apiKeyConfigured": api_key_configured,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        enabled = d.pop("enabled")

        def _parse_created_at(data: object) -> str:
            return cast(str, data)

        created_at = _parse_created_at(d.pop("createdAt"))


        def _parse_updated_at(data: object) -> str:
            return cast(str, data)

        updated_at = _parse_updated_at(d.pop("updatedAt"))


        transport = cast(Literal['resend'] , d.pop("transport"))
        if transport != 'resend':
            raise ValueError(f"transport must match const 'resend', got '{transport}'")

        from_email = d.pop("fromEmail")

        from_name = d.pop("fromName")

        api_key_configured = d.pop("apiKeyConfigured")

        public_resend_email_server = cls(
            id=id,
            name=name,
            enabled=enabled,
            created_at=created_at,
            updated_at=updated_at,
            transport=transport,
            from_email=from_email,
            from_name=from_name,
            api_key_configured=api_key_configured,
        )

        return public_resend_email_server
