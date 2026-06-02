from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.source_secrets_encrypt_body_secrets_item import SourceSecretsEncryptBodySecretsItem





T = TypeVar("T", bound="SourceSecretsEncryptBody")



@_attrs_define
class SourceSecretsEncryptBody:
    """ 
        Attributes:
            organization_id (str | Unset):
            source_path (str | Unset):
            secret_name (str | Unset):
            plaintext (str | Unset):
            secrets (list[SourceSecretsEncryptBodySecretsItem] | Unset):
     """

    organization_id: str | Unset = UNSET
    source_path: str | Unset = UNSET
    secret_name: str | Unset = UNSET
    plaintext: str | Unset = UNSET
    secrets: list[SourceSecretsEncryptBodySecretsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.source_secrets_encrypt_body_secrets_item import SourceSecretsEncryptBodySecretsItem
        organization_id = self.organization_id

        source_path = self.source_path

        secret_name = self.secret_name

        plaintext = self.plaintext

        secrets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.secrets, Unset):
            secrets = []
            for secrets_item_data in self.secrets:
                secrets_item = secrets_item_data.to_dict()
                secrets.append(secrets_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if source_path is not UNSET:
            field_dict["sourcePath"] = source_path
        if secret_name is not UNSET:
            field_dict["secretName"] = secret_name
        if plaintext is not UNSET:
            field_dict["plaintext"] = plaintext
        if secrets is not UNSET:
            field_dict["secrets"] = secrets

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.source_secrets_encrypt_body_secrets_item import SourceSecretsEncryptBodySecretsItem
        d = dict(src_dict)
        organization_id = d.pop("organizationId", UNSET)

        source_path = d.pop("sourcePath", UNSET)

        secret_name = d.pop("secretName", UNSET)

        plaintext = d.pop("plaintext", UNSET)

        _secrets = d.pop("secrets", UNSET)
        secrets: list[SourceSecretsEncryptBodySecretsItem] | Unset = UNSET
        if _secrets is not UNSET:
            secrets = []
            for secrets_item_data in _secrets:
                secrets_item = SourceSecretsEncryptBodySecretsItem.from_dict(secrets_item_data)



                secrets.append(secrets_item)


        source_secrets_encrypt_body = cls(
            organization_id=organization_id,
            source_path=source_path,
            secret_name=secret_name,
            plaintext=plaintext,
            secrets=secrets,
        )


        source_secrets_encrypt_body.additional_properties = d
        return source_secrets_encrypt_body

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
