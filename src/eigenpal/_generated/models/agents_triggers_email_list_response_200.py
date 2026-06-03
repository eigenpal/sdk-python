from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="AgentsTriggersEmailListResponse200")



@_attrs_define
class AgentsTriggersEmailListResponse200:
    """ 
        Attributes:
            emails (list[Any]):
     """

    emails: list[Any]





    def to_dict(self) -> dict[str, Any]:
        emails = self.emails




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "emails": emails,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        emails = cast(list[Any], d.pop("emails"))


        agents_triggers_email_list_response_200 = cls(
            emails=emails,
        )

        return agents_triggers_email_list_response_200

