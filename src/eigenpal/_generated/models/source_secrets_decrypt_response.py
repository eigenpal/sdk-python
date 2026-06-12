from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.source_secrets_decrypt_response_secrets import SourceSecretsDecryptResponseSecrets





T = TypeVar("T", bound="SourceSecretsDecryptResponse")



@_attrs_define
class SourceSecretsDecryptResponse:
    """
        Attributes:
            plaintext (str | Unset):
            secrets (SourceSecretsDecryptResponseSecrets | Unset):
     """

    plaintext: str | Unset = UNSET
    secrets: SourceSecretsDecryptResponseSecrets | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.source_secrets_decrypt_response_secrets import SourceSecretsDecryptResponseSecrets
        plaintext = self.plaintext

        secrets: dict[str, Any] | Unset = UNSET
        if not isinstance(self.secrets, Unset):
            secrets = self.secrets.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if plaintext is not UNSET:
            field_dict["plaintext"] = plaintext
        if secrets is not UNSET:
            field_dict["secrets"] = secrets

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.source_secrets_decrypt_response_secrets import SourceSecretsDecryptResponseSecrets
        d = dict(src_dict)
        plaintext = d.pop("plaintext", UNSET)

        _secrets = d.pop("secrets", UNSET)
        secrets: SourceSecretsDecryptResponseSecrets | Unset
        if isinstance(_secrets,  Unset):
            secrets = UNSET
        else:
            secrets = SourceSecretsDecryptResponseSecrets.from_dict(_secrets)




        source_secrets_decrypt_response = cls(
            plaintext=plaintext,
            secrets=secrets,
        )

        return source_secrets_decrypt_response
