from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.template_format import TemplateFormat
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.template_grammar import TemplateGrammar
  from ..models.template_revision import TemplateRevision
  from ..models.template_tokens_item import TemplateTokensItem





T = TypeVar("T", bound="Template")



@_attrs_define
class Template:
    """
        Attributes:
            id (str): Stable logical template id (tmpl_…).
            name (str):
            filename (str):
            format_ (TemplateFormat):
            mime_type (str):
            tokens (list[TemplateTokensItem]):
            grammar (TemplateGrammar):
            created_at (str):
            description (None | str | Unset):
            size (int | None | Unset):
            sha256 (None | str | Unset):
            current_revision (None | TemplateRevision | Unset):
            updated_at (None | str | Unset):
     """

    id: str
    name: str
    filename: str
    format_: TemplateFormat
    mime_type: str
    tokens: list[TemplateTokensItem]
    grammar: TemplateGrammar
    created_at: str
    description: None | str | Unset = UNSET
    size: int | None | Unset = UNSET
    sha256: None | str | Unset = UNSET
    current_revision: None | TemplateRevision | Unset = UNSET
    updated_at: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.template_grammar import TemplateGrammar
        from ..models.template_revision import TemplateRevision
        from ..models.template_tokens_item import TemplateTokensItem
        id = self.id

        name = self.name

        filename = self.filename

        format_ = self.format_.value

        mime_type = self.mime_type

        tokens = []
        for tokens_item_data in self.tokens:
            tokens_item = tokens_item_data.to_dict()
            tokens.append(tokens_item)



        grammar = self.grammar.to_dict()

        created_at: str
        created_at = self.created_at

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        size: int | None | Unset
        if isinstance(self.size, Unset):
            size = UNSET
        else:
            size = self.size

        sha256: None | str | Unset
        if isinstance(self.sha256, Unset):
            sha256 = UNSET
        else:
            sha256 = self.sha256

        current_revision: dict[str, Any] | None | Unset
        if isinstance(self.current_revision, Unset):
            current_revision = UNSET
        elif isinstance(self.current_revision, TemplateRevision):
            current_revision = self.current_revision.to_dict()
        else:
            current_revision = self.current_revision

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = self.updated_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "name": name,
            "filename": filename,
            "format": format_,
            "mimeType": mime_type,
            "tokens": tokens,
            "grammar": grammar,
            "createdAt": created_at,
        })
        if description is not UNSET:
            field_dict["description"] = description
        if size is not UNSET:
            field_dict["size"] = size
        if sha256 is not UNSET:
            field_dict["sha256"] = sha256
        if current_revision is not UNSET:
            field_dict["currentRevision"] = current_revision
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.template_grammar import TemplateGrammar
        from ..models.template_revision import TemplateRevision
        from ..models.template_tokens_item import TemplateTokensItem
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        filename = d.pop("filename")

        format_ = TemplateFormat(d.pop("format"))




        mime_type = d.pop("mimeType")

        tokens = []
        _tokens = d.pop("tokens")
        for tokens_item_data in (_tokens):
            tokens_item = TemplateTokensItem.from_dict(tokens_item_data)



            tokens.append(tokens_item)


        grammar = TemplateGrammar.from_dict(d.pop("grammar"))




        def _parse_created_at(data: object) -> str:
            return cast(str, data)

        created_at = _parse_created_at(d.pop("createdAt"))


        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        def _parse_size(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        size = _parse_size(d.pop("size", UNSET))


        def _parse_sha256(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sha256 = _parse_sha256(d.pop("sha256", UNSET))


        def _parse_current_revision(data: object) -> None | TemplateRevision | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                current_revision_type_0 = TemplateRevision.from_dict(data)



                return current_revision_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TemplateRevision | Unset, data)

        current_revision = _parse_current_revision(d.pop("currentRevision", UNSET))


        def _parse_updated_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        updated_at = _parse_updated_at(d.pop("updatedAt", UNSET))


        template = cls(
            id=id,
            name=name,
            filename=filename,
            format_=format_,
            mime_type=mime_type,
            tokens=tokens,
            grammar=grammar,
            created_at=created_at,
            description=description,
            size=size,
            sha256=sha256,
            current_revision=current_revision,
            updated_at=updated_at,
        )

        return template
