from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="SourceSecretsEncryptBodySecretsItem")



@_attrs_define
class SourceSecretsEncryptBodySecretsItem:
    """ 
        Attributes:
            source_path (str):
            secret_name (str):
            plaintext (str):
     """

    source_path: str
    secret_name: str
    plaintext: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        source_path = self.source_path

        secret_name = self.secret_name

        plaintext = self.plaintext


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "sourcePath": source_path,
            "secretName": secret_name,
            "plaintext": plaintext,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        source_path = d.pop("sourcePath")

        secret_name = d.pop("secretName")

        plaintext = d.pop("plaintext")

        source_secrets_encrypt_body_secrets_item = cls(
            source_path=source_path,
            secret_name=secret_name,
            plaintext=plaintext,
        )


        source_secrets_encrypt_body_secrets_item.additional_properties = d
        return source_secrets_encrypt_body_secrets_item

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
