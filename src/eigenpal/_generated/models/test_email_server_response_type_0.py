from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.test_email_server_response_type_0_transport import TestEmailServerResponseType0Transport






T = TypeVar("T", bound="TestEmailServerResponseType0")



@_attrs_define
class TestEmailServerResponseType0:
    """
        Attributes:
            ok (bool):
            transport (TestEmailServerResponseType0Transport):
            message_id (str):
     """

    ok: bool
    transport: TestEmailServerResponseType0Transport
    message_id: str





    def to_dict(self) -> dict[str, Any]:
        ok = self.ok

        transport = self.transport.value

        message_id = self.message_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "ok": ok,
            "transport": transport,
            "messageId": message_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ok = d.pop("ok")

        transport = TestEmailServerResponseType0Transport(d.pop("transport"))




        message_id = d.pop("messageId")

        test_email_server_response_type_0 = cls(
            ok=ok,
            transport=transport,
            message_id=message_id,
        )

        return test_email_server_response_type_0
