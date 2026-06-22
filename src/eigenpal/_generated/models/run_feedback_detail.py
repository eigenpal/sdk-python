from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.run_feedback import RunFeedback
  from ..models.run_file import RunFile





T = TypeVar("T", bound="RunFeedbackDetail")



@_attrs_define
class RunFeedbackDetail:
    """ Complete feedback state for a run: human feedback, expected JSON output, and expected files.

        Attributes:
            feedback (None | RunFeedback): Human feedback object for the run, or null when no feedback exists.
            expected (Any | None): Expected JSON output for the run, or null when none is set.
            expected_files (list[RunFile]): Expected output files attached to this run feedback record.
     """

    feedback: None | RunFeedback
    expected: Any | None
    expected_files: list[RunFile]





    def to_dict(self) -> dict[str, Any]:
        from ..models.run_feedback import RunFeedback
        from ..models.run_file import RunFile
        feedback: dict[str, Any] | None
        if isinstance(self.feedback, RunFeedback):
            feedback = self.feedback.to_dict()
        else:
            feedback = self.feedback

        expected: Any | None
        expected = self.expected

        expected_files = []
        for expected_files_item_data in self.expected_files:
            expected_files_item = expected_files_item_data.to_dict()
            expected_files.append(expected_files_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "feedback": feedback,
            "expected": expected,
            "expectedFiles": expected_files,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.run_feedback import RunFeedback
        from ..models.run_file import RunFile
        d = dict(src_dict)
        def _parse_feedback(data: object) -> None | RunFeedback:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                feedback_type_0 = RunFeedback.from_dict(data)



                return feedback_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RunFeedback, data)

        feedback = _parse_feedback(d.pop("feedback"))


        def _parse_expected(data: object) -> Any | None:
            if data is None:
                return data
            return cast(Any | None, data)

        expected = _parse_expected(d.pop("expected"))


        expected_files = []
        _expected_files = d.pop("expectedFiles")
        for expected_files_item_data in (_expected_files):
            expected_files_item = RunFile.from_dict(expected_files_item_data)



            expected_files.append(expected_files_item)


        run_feedback_detail = cls(
            feedback=feedback,
            expected=expected,
            expected_files=expected_files,
        )

        return run_feedback_detail
