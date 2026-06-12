from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.source_secrets_encrypt_response_encrypted import SourceSecretsEncryptResponseEncrypted
  from ..models.source_secrets_encrypt_response_secrets import SourceSecretsEncryptResponseSecrets





T = TypeVar("T", bound="SourceSecretsEncryptResponse")



@_attrs_define
class SourceSecretsEncryptResponse:
    """
        Attributes:
            encrypted (SourceSecretsEncryptResponseEncrypted | Unset):
            secrets (SourceSecretsEncryptResponseSecrets | Unset):
     """

    encrypted: SourceSecretsEncryptResponseEncrypted | Unset = UNSET
    secrets: SourceSecretsEncryptResponseSecrets | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.source_secrets_encrypt_response_encrypted import SourceSecretsEncryptResponseEncrypted
        from ..models.source_secrets_encrypt_response_secrets import SourceSecretsEncryptResponseSecrets
        encrypted: dict[str, Any] | Unset = UNSET
        if not isinstance(self.encrypted, Unset):
            encrypted = self.encrypted.to_dict()

        secrets: dict[str, Any] | Unset = UNSET
        if not isinstance(self.secrets, Unset):
            secrets = self.secrets.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if encrypted is not UNSET:
            field_dict["encrypted"] = encrypted
        if secrets is not UNSET:
            field_dict["secrets"] = secrets

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.source_secrets_encrypt_response_encrypted import SourceSecretsEncryptResponseEncrypted
        from ..models.source_secrets_encrypt_response_secrets import SourceSecretsEncryptResponseSecrets
        d = dict(src_dict)
        _encrypted = d.pop("encrypted", UNSET)
        encrypted: SourceSecretsEncryptResponseEncrypted | Unset
        if isinstance(_encrypted,  Unset):
            encrypted = UNSET
        else:
            encrypted = SourceSecretsEncryptResponseEncrypted.from_dict(_encrypted)




        _secrets = d.pop("secrets", UNSET)
        secrets: SourceSecretsEncryptResponseSecrets | Unset
        if isinstance(_secrets,  Unset):
            secrets = UNSET
        else:
            secrets = SourceSecretsEncryptResponseSecrets.from_dict(_secrets)




        source_secrets_encrypt_response = cls(
            encrypted=encrypted,
            secrets=secrets,
        )

        return source_secrets_encrypt_response
