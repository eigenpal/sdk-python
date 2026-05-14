from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.agent_execution_feedback import AgentExecutionFeedback
  from ..models.agent_execution_feedback_detail_expected_files_item import AgentExecutionFeedbackDetailExpectedFilesItem





T = TypeVar("T", bound="AgentExecutionFeedbackDetail")



@_attrs_define
class AgentExecutionFeedbackDetail:
    """ 
        Attributes:
            feedback (AgentExecutionFeedback | None):
            expected (Any | None):
            expected_files (list[AgentExecutionFeedbackDetailExpectedFilesItem]):
     """

    feedback: AgentExecutionFeedback | None
    expected: Any | None
    expected_files: list[AgentExecutionFeedbackDetailExpectedFilesItem]





    def to_dict(self) -> dict[str, Any]:
        from ..models.agent_execution_feedback import AgentExecutionFeedback
        from ..models.agent_execution_feedback_detail_expected_files_item import AgentExecutionFeedbackDetailExpectedFilesItem
        feedback: dict[str, Any] | None
        if isinstance(self.feedback, AgentExecutionFeedback):
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
        from ..models.agent_execution_feedback import AgentExecutionFeedback
        from ..models.agent_execution_feedback_detail_expected_files_item import AgentExecutionFeedbackDetailExpectedFilesItem
        d = dict(src_dict)
        def _parse_feedback(data: object) -> AgentExecutionFeedback | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                feedback_type_0 = AgentExecutionFeedback.from_dict(data)



                return feedback_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AgentExecutionFeedback | None, data)

        feedback = _parse_feedback(d.pop("feedback"))


        def _parse_expected(data: object) -> Any | None:
            if data is None:
                return data
            return cast(Any | None, data)

        expected = _parse_expected(d.pop("expected"))


        expected_files = []
        _expected_files = d.pop("expectedFiles")
        for expected_files_item_data in (_expected_files):
            expected_files_item = AgentExecutionFeedbackDetailExpectedFilesItem.from_dict(expected_files_item_data)



            expected_files.append(expected_files_item)


        agent_execution_feedback_detail = cls(
            feedback=feedback,
            expected=expected,
            expected_files=expected_files,
        )

        return agent_execution_feedback_detail

