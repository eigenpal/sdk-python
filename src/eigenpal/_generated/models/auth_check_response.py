from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="AuthCheckResponse")



@_attrs_define
class AuthCheckResponse:
    """
        Attributes:
            ok (bool):
            tenant_id (str):
            tenant_slug (str):
            tenant_name (None | str):
            user_id (None | str):
            key_id (str):
            email (None | str):
            name (None | str):
            scope (list[str]):
            wildcard_granted (bool):
     """

    ok: bool
    tenant_id: str
    tenant_slug: str
    tenant_name: None | str
    user_id: None | str
    key_id: str
    email: None | str
    name: None | str
    scope: list[str]
    wildcard_granted: bool





    def to_dict(self) -> dict[str, Any]:
        ok = self.ok

        tenant_id = self.tenant_id

        tenant_slug = self.tenant_slug

        tenant_name: None | str
        tenant_name = self.tenant_name

        user_id: None | str
        user_id = self.user_id

        key_id = self.key_id

        email: None | str
        email = self.email

        name: None | str
        name = self.name

        scope = self.scope



        wildcard_granted = self.wildcard_granted


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "ok": ok,
            "tenantId": tenant_id,
            "tenantSlug": tenant_slug,
            "tenantName": tenant_name,
            "userId": user_id,
            "keyId": key_id,
            "email": email,
            "name": name,
            "scope": scope,
            "wildcardGranted": wildcard_granted,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ok = d.pop("ok")

        tenant_id = d.pop("tenantId")

        tenant_slug = d.pop("tenantSlug")

        def _parse_tenant_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        tenant_name = _parse_tenant_name(d.pop("tenantName"))


        def _parse_user_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        user_id = _parse_user_id(d.pop("userId"))


        key_id = d.pop("keyId")

        def _parse_email(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        email = _parse_email(d.pop("email"))


        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))


        scope = cast(list[str], d.pop("scope"))


        wildcard_granted = d.pop("wildcardGranted")

        auth_check_response = cls(
            ok=ok,
            tenant_id=tenant_id,
            tenant_slug=tenant_slug,
            tenant_name=tenant_name,
            user_id=user_id,
            key_id=key_id,
            email=email,
            name=name,
            scope=scope,
            wildcard_granted=wildcard_granted,
        )

        return auth_check_response
