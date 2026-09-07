from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.public_smtp_email_server_security import PublicSmtpEmailServerSecurity
from typing import cast
from typing import Literal, cast






T = TypeVar("T", bound="PublicSmtpEmailServer")



@_attrs_define
class PublicSmtpEmailServer:
    """
        Attributes:
            id (str):
            name (str):
            enabled (bool):
            created_at (str):
            updated_at (str):
            transport (Literal['smtp']):
            from_email (str):
            from_name (str):
            host (str):
            port (int):
            security (PublicSmtpEmailServerSecurity):
            username (None | str):
            password_configured (bool):
            ca_pem_configured (bool):
     """

    id: str
    name: str
    enabled: bool
    created_at: str
    updated_at: str
    transport: Literal['smtp']
    from_email: str
    from_name: str
    host: str
    port: int
    security: PublicSmtpEmailServerSecurity
    username: None | str
    password_configured: bool
    ca_pem_configured: bool





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

        host = self.host

        port = self.port

        security = self.security.value

        username: None | str
        username = self.username

        password_configured = self.password_configured

        ca_pem_configured = self.ca_pem_configured


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
            "host": host,
            "port": port,
            "security": security,
            "username": username,
            "passwordConfigured": password_configured,
            "caPemConfigured": ca_pem_configured,
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


        transport = cast(Literal['smtp'] , d.pop("transport"))
        if transport != 'smtp':
            raise ValueError(f"transport must match const 'smtp', got '{transport}'")

        from_email = d.pop("fromEmail")

        from_name = d.pop("fromName")

        host = d.pop("host")

        port = d.pop("port")

        security = PublicSmtpEmailServerSecurity(d.pop("security"))




        def _parse_username(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        username = _parse_username(d.pop("username"))


        password_configured = d.pop("passwordConfigured")

        ca_pem_configured = d.pop("caPemConfigured")

        public_smtp_email_server = cls(
            id=id,
            name=name,
            enabled=enabled,
            created_at=created_at,
            updated_at=updated_at,
            transport=transport,
            from_email=from_email,
            from_name=from_name,
            host=host,
            port=port,
            security=security,
            username=username,
            password_configured=password_configured,
            ca_pem_configured=ca_pem_configured,
        )

        return public_smtp_email_server
