from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.update_email_server_request_type_1_security import UpdateEmailServerRequestType1Security
from ..types import UNSET, Unset
from typing import cast
from typing import Literal, cast






T = TypeVar("T", bound="UpdateEmailServerRequestType1")



@_attrs_define
class UpdateEmailServerRequestType1:
    """
        Attributes:
            transport (Literal['smtp']):
            host (str):
            port (int):
            security (UpdateEmailServerRequestType1Security):
            from_email (str):
            from_name (str):
            name (str | Unset):
            enabled (bool | Unset):
            username (None | str | Unset):
            password (str | Unset):
            ca_pem (None | str | Unset):
     """

    transport: Literal['smtp']
    host: str
    port: int
    security: UpdateEmailServerRequestType1Security
    from_email: str
    from_name: str
    name: str | Unset = UNSET
    enabled: bool | Unset = UNSET
    username: None | str | Unset = UNSET
    password: str | Unset = UNSET
    ca_pem: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        transport = self.transport

        host = self.host

        port = self.port

        security = self.security.value

        from_email = self.from_email

        from_name = self.from_name

        name = self.name

        enabled = self.enabled

        username: None | str | Unset
        if isinstance(self.username, Unset):
            username = UNSET
        else:
            username = self.username

        password = self.password

        ca_pem: None | str | Unset
        if isinstance(self.ca_pem, Unset):
            ca_pem = UNSET
        else:
            ca_pem = self.ca_pem


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "transport": transport,
            "host": host,
            "port": port,
            "security": security,
            "fromEmail": from_email,
            "fromName": from_name,
        })
        if name is not UNSET:
            field_dict["name"] = name
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
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
        transport = cast(Literal['smtp'] , d.pop("transport"))
        if transport != 'smtp':
            raise ValueError(f"transport must match const 'smtp', got '{transport}'")

        host = d.pop("host")

        port = d.pop("port")

        security = UpdateEmailServerRequestType1Security(d.pop("security"))




        from_email = d.pop("fromEmail")

        from_name = d.pop("fromName")

        name = d.pop("name", UNSET)

        enabled = d.pop("enabled", UNSET)

        def _parse_username(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        username = _parse_username(d.pop("username", UNSET))


        password = d.pop("password", UNSET)

        def _parse_ca_pem(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ca_pem = _parse_ca_pem(d.pop("caPem", UNSET))


        update_email_server_request_type_1 = cls(
            transport=transport,
            host=host,
            port=port,
            security=security,
            from_email=from_email,
            from_name=from_name,
            name=name,
            enabled=enabled,
            username=username,
            password=password,
            ca_pem=ca_pem,
        )

        return update_email_server_request_type_1
