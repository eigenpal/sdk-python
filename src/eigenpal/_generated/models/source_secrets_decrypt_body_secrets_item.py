from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.source_secrets_decrypt_body_secrets_item_encrypted import SourceSecretsDecryptBodySecretsItemEncrypted





T = TypeVar("T", bound="SourceSecretsDecryptBodySecretsItem")



@_attrs_define
class SourceSecretsDecryptBodySecretsItem:
    """
        Attributes:
            source_path (str):
            secret_name (str):
            encrypted (SourceSecretsDecryptBodySecretsItemEncrypted):
     """

    source_path: str
    secret_name: str
    encrypted: SourceSecretsDecryptBodySecretsItemEncrypted
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.source_secrets_decrypt_body_secrets_item_encrypted import SourceSecretsDecryptBodySecretsItemEncrypted
        source_path = self.source_path

        secret_name = self.secret_name

        encrypted = self.encrypted.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "sourcePath": source_path,
            "secretName": secret_name,
            "encrypted": encrypted,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.source_secrets_decrypt_body_secrets_item_encrypted import SourceSecretsDecryptBodySecretsItemEncrypted
        d = dict(src_dict)
        source_path = d.pop("sourcePath")

        secret_name = d.pop("secretName")

        encrypted = SourceSecretsDecryptBodySecretsItemEncrypted.from_dict(d.pop("encrypted"))




        source_secrets_decrypt_body_secrets_item = cls(
            source_path=source_path,
            secret_name=secret_name,
            encrypted=encrypted,
        )


        source_secrets_decrypt_body_secrets_item.additional_properties = d
        return source_secrets_decrypt_body_secrets_item

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
