from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.run_usage_tokens import RunUsageTokens





T = TypeVar("T", bound="RunUsage")



@_attrs_define
class RunUsage:
    """
        Attributes:
            tokens (RunUsageTokens):
            credits_charged (float | None):
            duration_ms (float | None):
            llm_call_count (float | Unset): LLM call count (workflow runs only).
            ocr_pages_processed (float | Unset): OCR pages processed (workflow runs only).
            agent_turns (float | None | Unset): Agent conversation turns (agent runs only).
     """

    tokens: RunUsageTokens
    credits_charged: float | None
    duration_ms: float | None
    llm_call_count: float | Unset = UNSET
    ocr_pages_processed: float | Unset = UNSET
    agent_turns: float | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.run_usage_tokens import RunUsageTokens
        tokens = self.tokens.to_dict()

        credits_charged: float | None
        credits_charged = self.credits_charged

        duration_ms: float | None
        duration_ms = self.duration_ms

        llm_call_count = self.llm_call_count

        ocr_pages_processed = self.ocr_pages_processed

        agent_turns: float | None | Unset
        if isinstance(self.agent_turns, Unset):
            agent_turns = UNSET
        else:
            agent_turns = self.agent_turns


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "tokens": tokens,
            "creditsCharged": credits_charged,
            "durationMs": duration_ms,
        })
        if llm_call_count is not UNSET:
            field_dict["llmCallCount"] = llm_call_count
        if ocr_pages_processed is not UNSET:
            field_dict["ocrPagesProcessed"] = ocr_pages_processed
        if agent_turns is not UNSET:
            field_dict["agentTurns"] = agent_turns

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.run_usage_tokens import RunUsageTokens
        d = dict(src_dict)
        tokens = RunUsageTokens.from_dict(d.pop("tokens"))




        def _parse_credits_charged(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        credits_charged = _parse_credits_charged(d.pop("creditsCharged"))


        def _parse_duration_ms(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        duration_ms = _parse_duration_ms(d.pop("durationMs"))


        llm_call_count = d.pop("llmCallCount", UNSET)

        ocr_pages_processed = d.pop("ocrPagesProcessed", UNSET)

        def _parse_agent_turns(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        agent_turns = _parse_agent_turns(d.pop("agentTurns", UNSET))


        run_usage = cls(
            tokens=tokens,
            credits_charged=credits_charged,
            duration_ms=duration_ms,
            llm_call_count=llm_call_count,
            ocr_pages_processed=ocr_pages_processed,
            agent_turns=agent_turns,
        )

        return run_usage
