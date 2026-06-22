from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.run_file import RunFile





T = TypeVar("T", bound="RunExpectedArtifacts")



@_attrs_define
class RunExpectedArtifacts:
    """ Expected JSON output and expected files attached to run feedback.

        Attributes:
            expected (Any | None): Expected JSON output for the run, or null when none is set.
            files (list[RunFile]): Expected output files attached to this run feedback record.
     """

    expected: Any | None
    files: list[RunFile]





    def to_dict(self) -> dict[str, Any]:
        from ..models.run_file import RunFile
        expected: Any | None
        expected = self.expected

        files = []
        for files_item_data in self.files:
            files_item = files_item_data.to_dict()
            files.append(files_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "expected": expected,
            "files": files,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.run_file import RunFile
        d = dict(src_dict)
        def _parse_expected(data: object) -> Any | None:
            if data is None:
                return data
            return cast(Any | None, data)

        expected = _parse_expected(d.pop("expected"))


        files = []
        _files = d.pop("files")
        for files_item_data in (_files):
            files_item = RunFile.from_dict(files_item_data)



            files.append(files_item)


        run_expected_artifacts = cls(
            expected=expected,
            files=files,
        )

        return run_expected_artifacts
