from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.create_email_server_request_type_1_security import CreateEmailServerRequestType1Security
from ..types import UNSET, Unset
from typing import Literal, cast






T = TypeVar("T", bound="CreateEmailServerRequestType1")



@_attrs_define
class CreateEmailServerRequestType1:
    """
        Attributes:
            name (str):
            transport (Literal['smtp']):
            host (str):
            from_email (str):
            from_name (str):
            enabled (bool | Unset):  Default: True.
            port (int | Unset):
            security (CreateEmailServerRequestType1Security | Unset):  Default:
                CreateEmailServerRequestType1Security.STARTTLS.
            username (str | Unset):
            password (str | Unset):
            ca_pem (str | Unset):
     """

    name: str
    transport: Literal['smtp']
    host: str
    from_email: str
    from_name: str
    enabled: bool | Unset = True
    port: int | Unset = UNSET
    security: CreateEmailServerRequestType1Security | Unset = CreateEmailServerRequestType1Security.STARTTLS
    username: str | Unset = UNSET
    password: str | Unset = UNSET
    ca_pem: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        transport = self.transport

        host = self.host

        from_email = self.from_email

        from_name = self.from_name

        enabled = self.enabled

        port = self.port

        security: str | Unset = UNSET
        if not isinstance(self.security, Unset):
            security = self.security.value


        username = self.username

        password = self.password

        ca_pem = self.ca_pem


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "name": name,
            "transport": transport,
            "host": host,
            "fromEmail": from_email,
            "fromName": from_name,
        })
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if port is not UNSET:
            field_dict["port"] = port
        if security is not UNSET:
            field_dict["security"] = security
        if username is not UNSET:
            field_dict["username"] = username
        if password is not UNSET:
            field_dict["password"] = password
        if ca_pem is not UNSET:
            field_dict["caPem"] = ca_pem

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        transport = cast(Literal['smtp'] , d.pop("transport"))
        if transport != 'smtp':
            raise ValueError(f"transport must match const 'smtp', got '{transport}'")

        host = d.pop("host")

        from_email = d.pop("fromEmail")

        from_name = d.pop("fromName")

        enabled = d.pop("enabled", UNSET)

        port = d.pop("port", UNSET)

        _security = d.pop("security", UNSET)
        security: CreateEmailServerRequestType1Security | Unset
        if isinstance(_security,  Unset):
            security = UNSET
        else:
            security = CreateEmailServerRequestType1Security(_security)




        username = d.pop("username", UNSET)

        password = d.pop("password", UNSET)

        ca_pem = d.pop("caPem", UNSET)

        create_email_server_request_type_1 = cls(
            name=name,
            transport=transport,
            host=host,
            from_email=from_email,
            from_name=from_name,
            enabled=enabled,
            port=port,
            security=security,
            username=username,
            password=password,
            ca_pem=ca_pem,
        )

        return create_email_server_request_type_1
