from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Literal, cast






T = TypeVar("T", bound="SourceSecretsEncryptResponseEncrypted")



@_attrs_define
class SourceSecretsEncryptResponseEncrypted:
    """ 
        Attributes:
            algorithm (Literal['aes-256-gcm']):
            key_id (str):
            nonce (str):
            ciphertext (str):
            tag (str):
     """

    algorithm: Literal['aes-256-gcm']
    key_id: str
    nonce: str
    ciphertext: str
    tag: str





    def to_dict(self) -> dict[str, Any]:
        algorithm = self.algorithm

        key_id = self.key_id

        nonce = self.nonce

        ciphertext = self.ciphertext

        tag = self.tag


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "algorithm": algorithm,
            "keyId": key_id,
            "nonce": nonce,
            "ciphertext": ciphertext,
            "tag": tag,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        algorithm = cast(Literal['aes-256-gcm'] , d.pop("algorithm"))
        if algorithm != 'aes-256-gcm':
            raise ValueError(f"algorithm must match const 'aes-256-gcm', got '{algorithm}'")

        key_id = d.pop("keyId")

        nonce = d.pop("nonce")

        ciphertext = d.pop("ciphertext")

        tag = d.pop("tag")

        source_secrets_encrypt_response_encrypted = cls(
            algorithm=algorithm,
            key_id=key_id,
            nonce=nonce,
            ciphertext=ciphertext,
            tag=tag,
        )

        return source_secrets_encrypt_response_encrypted

