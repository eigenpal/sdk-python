from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.created_template_tokens_item_kind import CreatedTemplateTokensItemKind
from ..models.created_template_tokens_item_type import CreatedTemplateTokensItemType
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="CreatedTemplateTokensItem")



@_attrs_define
class CreatedTemplateTokensItem:
    """
        Attributes:
            name (str):
            path (list[str] | Unset):
            kind (CreatedTemplateTokensItemKind | Unset):
            type_ (CreatedTemplateTokensItemType | Unset):
            required (bool | Unset):
            description (str | Unset):
     """

    name: str
    path: list[str] | Unset = UNSET
    kind: CreatedTemplateTokensItemKind | Unset = UNSET
    type_: CreatedTemplateTokensItemType | Unset = UNSET
    required: bool | Unset = UNSET
    description: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        path: list[str] | Unset = UNSET
        if not isinstance(self.path, Unset):
            path = self.path



        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value


        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value


        required = self.required

        description = self.description


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "name": name,
        })
        if path is not UNSET:
            field_dict["path"] = path
        if kind is not UNSET:
            field_dict["kind"] = kind
        if type_ is not UNSET:
            field_dict["type"] = type_
        if required is not UNSET:
            field_dict["required"] = required
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        path = cast(list[str], d.pop("path", UNSET))


        _kind = d.pop("kind", UNSET)
        kind: CreatedTemplateTokensItemKind | Unset
        if isinstance(_kind,  Unset):
            kind = UNSET
        else:
            kind = CreatedTemplateTokensItemKind(_kind)




        _type_ = d.pop("type", UNSET)
        type_: CreatedTemplateTokensItemType | Unset
        if isinstance(_type_,  Unset):
            type_ = UNSET
        else:
            type_ = CreatedTemplateTokensItemType(_type_)




        required = d.pop("required", UNSET)

        description = d.pop("description", UNSET)

        created_template_tokens_item = cls(
            name=name,
            path=path,
            kind=kind,
            type_=type_,
            required=required,
            description=description,
        )

        return created_template_tokens_item
