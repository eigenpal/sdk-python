from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="TemplateGrammar")



@_attrs_define
class TemplateGrammar:
    """
        Attributes:
            syntax (str):
            token_discovery (bool):
            capabilities (list[str]):
     """

    syntax: str
    token_discovery: bool
    capabilities: list[str]





    def to_dict(self) -> dict[str, Any]:
        syntax = self.syntax

        token_discovery = self.token_discovery

        capabilities = self.capabilities




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "syntax": syntax,
            "tokenDiscovery": token_discovery,
            "capabilities": capabilities,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        syntax = d.pop("syntax")

        token_discovery = d.pop("tokenDiscovery")

        capabilities = cast(list[str], d.pop("capabilities"))


        template_grammar = cls(
            syntax=syntax,
            token_discovery=token_discovery,
            capabilities=capabilities,
        )

        return template_grammar
