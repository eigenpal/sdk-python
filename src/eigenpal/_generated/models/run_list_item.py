from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.run_list_item_type import RunListItemType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.run_eval import RunEval
  from ..models.run_execution_meta import RunExecutionMeta
  from ..models.run_source import RunSource
  from ..models.run_timing import RunTiming
  from ..models.run_trigger import RunTrigger





T = TypeVar("T", bound="RunListItem")



@_attrs_define
class RunListItem:
    """
        Attributes:
            id (str):
            type_ (RunListItemType):
            finished (bool): True when the run has reached a terminal status.
            sample_rank (float): Deterministic pseudo-random rank in [0, 1) for this run within the tenant. Use with a
                sample rate threshold to review a stable subset.
            timing (RunTiming):
            source (RunSource):
            trigger (RunTrigger):
            execution (RunExecutionMeta):
            eval_ (RunEval | Unset):
            error (None | str | Unset):
     """

    id: str
    type_: RunListItemType
    finished: bool
    sample_rank: float
    timing: RunTiming
    source: RunSource
    trigger: RunTrigger
    execution: RunExecutionMeta
    eval_: RunEval | Unset = UNSET
    error: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.run_eval import RunEval
        from ..models.run_execution_meta import RunExecutionMeta
        from ..models.run_source import RunSource
        from ..models.run_timing import RunTiming
        from ..models.run_trigger import RunTrigger
        id = self.id

        type_ = self.type_.value

        finished = self.finished

        sample_rank = self.sample_rank

        timing = self.timing.to_dict()

        source = self.source.to_dict()

        trigger = self.trigger.to_dict()

        execution = self.execution.to_dict()

        eval_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.eval_, Unset):
            eval_ = self.eval_.to_dict()

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "type": type_,
            "finished": finished,
            "sampleRank": sample_rank,
            "timing": timing,
            "source": source,
            "trigger": trigger,
            "execution": execution,
        })
        if eval_ is not UNSET:
            field_dict["eval"] = eval_
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.run_eval import RunEval
        from ..models.run_execution_meta import RunExecutionMeta
        from ..models.run_source import RunSource
        from ..models.run_timing import RunTiming
        from ..models.run_trigger import RunTrigger
        d = dict(src_dict)
        id = d.pop("id")

        type_ = RunListItemType(d.pop("type"))




        finished = d.pop("finished")

        sample_rank = d.pop("sampleRank")

        timing = RunTiming.from_dict(d.pop("timing"))




        source = RunSource.from_dict(d.pop("source"))




        trigger = RunTrigger.from_dict(d.pop("trigger"))




        execution = RunExecutionMeta.from_dict(d.pop("execution"))




        _eval_ = d.pop("eval", UNSET)
        eval_: RunEval | Unset
        if isinstance(_eval_,  Unset):
            eval_ = UNSET
        else:
            eval_ = RunEval.from_dict(_eval_)




        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))


        run_list_item = cls(
            id=id,
            type_=type_,
            finished=finished,
            sample_rank=sample_rank,
            timing=timing,
            source=source,
            trigger=trigger,
            execution=execution,
            eval_=eval_,
            error=error,
        )

        return run_list_item
