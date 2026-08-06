from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.create_file_upload_session_request_purpose import CreateFileUploadSessionRequestPurpose
from ..types import UNSET, Unset






T = TypeVar("T", bound="CreateFileUploadSessionRequest")



@_attrs_define
class CreateFileUploadSessionRequest:
    """
        Attributes:
            filename (str):
            content_type (str):
            size (int):
            purpose (CreateFileUploadSessionRequestPurpose | Unset):
            idempotency_key (str | Unset):
     """

    filename: str
    content_type: str
    size: int
    purpose: CreateFileUploadSessionRequestPurpose | Unset = UNSET
    idempotency_key: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        filename = self.filename

        content_type = self.content_type

        size = self.size

        purpose: str | Unset = UNSET
        if not isinstance(self.purpose, Unset):
            purpose = self.purpose.value


        idempotency_key = self.idempotency_key


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "filename": filename,
            "contentType": content_type,
            "size": size,
        })
        if purpose is not UNSET:
            field_dict["purpose"] = purpose
        if idempotency_key is not UNSET:
            field_dict["idempotencyKey"] = idempotency_key

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        filename = d.pop("filename")

        content_type = d.pop("contentType")

        size = d.pop("size")

        _purpose = d.pop("purpose", UNSET)
        purpose: CreateFileUploadSessionRequestPurpose | Unset
        if isinstance(_purpose,  Unset):
            purpose = UNSET
        else:
            purpose = CreateFileUploadSessionRequestPurpose(_purpose)




        idempotency_key = d.pop("idempotencyKey", UNSET)

        create_file_upload_session_request = cls(
            filename=filename,
            content_type=content_type,
            size=size,
            purpose=purpose,
            idempotency_key=idempotency_key,
        )


        create_file_upload_session_request.additional_properties = d
        return create_file_upload_session_request

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
