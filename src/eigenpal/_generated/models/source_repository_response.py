from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="SourceRepositoryResponse")



@_attrs_define
class SourceRepositoryResponse:
    """
        Attributes:
            git_repository_path (str):
            remote_url (str):
     """

    git_repository_path: str
    remote_url: str





    def to_dict(self) -> dict[str, Any]:
        git_repository_path = self.git_repository_path

        remote_url = self.remote_url


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "gitRepositoryPath": git_repository_path,
            "remoteUrl": remote_url,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        git_repository_path = d.pop("gitRepositoryPath")

        remote_url = d.pop("remoteUrl")

        source_repository_response = cls(
            git_repository_path=git_repository_path,
            remote_url=remote_url,
        )

        return source_repository_response
