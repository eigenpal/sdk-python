from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.run_file import RunFile





T = TypeVar("T", bound="RunReviewExpectedArtifacts")



@_attrs_define
class RunReviewExpectedArtifacts:
    """
        Attributes:
            files (list[RunFile]): Corrected artifact files attached to the run review. Corrected JSON output lives on the
                review object at GET /runs/{id}/reviews.
     """

    files: list[RunFile]





    def to_dict(self) -> dict[str, Any]:
        from ..models.run_file import RunFile
        files = []
        for files_item_data in self.files:
            files_item = files_item_data.to_dict()
            files.append(files_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "files": files,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.run_file import RunFile
        d = dict(src_dict)
        files = []
        _files = d.pop("files")
        for files_item_data in (_files):
            files_item = RunFile.from_dict(files_item_data)



            files.append(files_item)


        run_review_expected_artifacts = cls(
            files=files,
        )

        return run_review_expected_artifacts
