from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="ListAgentVersionsResponseVersionsItemCreatedByUserType0")



@_attrs_define
class ListAgentVersionsResponseVersionsItemCreatedByUserType0:
    """ 
        Attributes:
            id (str):
            email (str):
            name (None | str):
            image (None | str):
     """

    id: str
    email: str
    name: None | str
    image: None | str





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        email = self.email

        name: None | str
        name = self.name

        image: None | str
        image = self.image


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "email": email,
            "name": name,
            "image": image,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        email = d.pop("email")

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))


        def _parse_image(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        image = _parse_image(d.pop("image"))


        list_agent_versions_response_versions_item_created_by_user_type_0 = cls(
            id=id,
            email=email,
            name=name,
            image=image,
        )

        return list_agent_versions_response_versions_item_created_by_user_type_0

