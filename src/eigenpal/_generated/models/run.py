from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.run_type import RunType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.agent_run_execution import AgentRunExecution
  from ..models.run_artifact import RunArtifact
  from ..models.run_debug import RunDebug
  from ..models.run_eval import RunEval
  from ..models.run_execution_meta import RunExecutionMeta
  from ..models.run_input import RunInput
  from ..models.run_output_type_0 import RunOutputType0
  from ..models.run_source import RunSource
  from ..models.run_timing import RunTiming
  from ..models.run_trigger import RunTrigger
  from ..models.run_usage import RunUsage
  from ..models.workflow_run_execution import WorkflowRunExecution





T = TypeVar("T", bound="Run")



@_attrs_define
class Run:
    """
        Attributes:
            id (str):
            type_ (RunType):
            finished (bool): True when the run has reached a terminal status.
            timing (RunTiming):
            source (RunSource):
            trigger (RunTrigger):
            execution (AgentRunExecution | RunExecutionMeta | WorkflowRunExecution): Slim execution metadata always present.
                Pass `expand=execution` to replace with full RunExecution (WorkflowRunExecution or AgentRunExecution depending
                on run type).
            eval_ (RunEval | Unset):
            output (None | RunOutputType0 | Unset): Completed runs only.
            files (list[RunArtifact] | Unset): Completed runs only. Download with GET /api/v1/runs/:id/artifacts/:path.
            error (None | str | Unset):
            input_ (RunInput | Unset):
            usage (None | RunUsage | Unset): `expand=usage`. Null for old runs without telemetry.
            debug (RunDebug | Unset):
     """

    id: str
    type_: RunType
    finished: bool
    timing: RunTiming
    source: RunSource
    trigger: RunTrigger
    execution: AgentRunExecution | RunExecutionMeta | WorkflowRunExecution
    eval_: RunEval | Unset = UNSET
    output: None | RunOutputType0 | Unset = UNSET
    files: list[RunArtifact] | Unset = UNSET
    error: None | str | Unset = UNSET
    input_: RunInput | Unset = UNSET
    usage: None | RunUsage | Unset = UNSET
    debug: RunDebug | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.agent_run_execution import AgentRunExecution
        from ..models.run_artifact import RunArtifact
        from ..models.run_debug import RunDebug
        from ..models.run_eval import RunEval
        from ..models.run_execution_meta import RunExecutionMeta
        from ..models.run_input import RunInput
        from ..models.run_output_type_0 import RunOutputType0
        from ..models.run_source import RunSource
        from ..models.run_timing import RunTiming
        from ..models.run_trigger import RunTrigger
        from ..models.run_usage import RunUsage
        from ..models.workflow_run_execution import WorkflowRunExecution
        id = self.id

        type_ = self.type_.value

        finished = self.finished

        timing = self.timing.to_dict()

        source = self.source.to_dict()

        trigger = self.trigger.to_dict()

        execution: dict[str, Any]
        if isinstance(self.execution, RunExecutionMeta):
            execution = self.execution.to_dict()
        elif isinstance(self.execution, WorkflowRunExecution):
            execution = self.execution.to_dict()
        else:
            execution = self.execution.to_dict()


        eval_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.eval_, Unset):
            eval_ = self.eval_.to_dict()

        output: dict[str, Any] | None | Unset
        if isinstance(self.output, Unset):
            output = UNSET
        elif isinstance(self.output, RunOutputType0):
            output = self.output.to_dict()
        else:
            output = self.output

        files: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.files, Unset):
            files = []
            for files_item_data in self.files:
                files_item = files_item_data.to_dict()
                files.append(files_item)



        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        input_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.input_, Unset):
            input_ = self.input_.to_dict()

        usage: dict[str, Any] | None | Unset
        if isinstance(self.usage, Unset):
            usage = UNSET
        elif isinstance(self.usage, RunUsage):
            usage = self.usage.to_dict()
        else:
            usage = self.usage

        debug: dict[str, Any] | Unset = UNSET
        if not isinstance(self.debug, Unset):
            debug = self.debug.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "type": type_,
            "finished": finished,
            "timing": timing,
            "source": source,
            "trigger": trigger,
            "execution": execution,
        })
        if eval_ is not UNSET:
            field_dict["eval"] = eval_
        if output is not UNSET:
            field_dict["output"] = output
        if files is not UNSET:
            field_dict["files"] = files
        if error is not UNSET:
            field_dict["error"] = error
        if input_ is not UNSET:
            field_dict["input"] = input_
        if usage is not UNSET:
            field_dict["usage"] = usage
        if debug is not UNSET:
            field_dict["debug"] = debug

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_run_execution import AgentRunExecution
        from ..models.run_artifact import RunArtifact
        from ..models.run_debug import RunDebug
        from ..models.run_eval import RunEval
        from ..models.run_execution_meta import RunExecutionMeta
        from ..models.run_input import RunInput
        from ..models.run_output_type_0 import RunOutputType0
        from ..models.run_source import RunSource
        from ..models.run_timing import RunTiming
        from ..models.run_trigger import RunTrigger
        from ..models.run_usage import RunUsage
        from ..models.workflow_run_execution import WorkflowRunExecution
        d = dict(src_dict)
        id = d.pop("id")

        type_ = RunType(d.pop("type"))




        finished = d.pop("finished")

        timing = RunTiming.from_dict(d.pop("timing"))




        source = RunSource.from_dict(d.pop("source"))




        trigger = RunTrigger.from_dict(d.pop("trigger"))




        def _parse_execution(data: object) -> AgentRunExecution | RunExecutionMeta | WorkflowRunExecution:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                execution_type_0 = RunExecutionMeta.from_dict(data)



                return execution_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_run_execution_type_0 = WorkflowRunExecution.from_dict(data)



                return componentsschemas_run_execution_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_run_execution_type_1 = AgentRunExecution.from_dict(data)



            return componentsschemas_run_execution_type_1

        execution = _parse_execution(d.pop("execution"))


        _eval_ = d.pop("eval", UNSET)
        eval_: RunEval | Unset
        if isinstance(_eval_,  Unset):
            eval_ = UNSET
        else:
            eval_ = RunEval.from_dict(_eval_)




        def _parse_output(data: object) -> None | RunOutputType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                output_type_0 = RunOutputType0.from_dict(data)



                return output_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RunOutputType0 | Unset, data)

        output = _parse_output(d.pop("output", UNSET))


        _files = d.pop("files", UNSET)
        files: list[RunArtifact] | Unset = UNSET
        if _files is not UNSET:
            files = []
            for files_item_data in _files:
                files_item = RunArtifact.from_dict(files_item_data)



                files.append(files_item)


        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))


        _input_ = d.pop("input", UNSET)
        input_: RunInput | Unset
        if isinstance(_input_,  Unset):
            input_ = UNSET
        else:
            input_ = RunInput.from_dict(_input_)




        def _parse_usage(data: object) -> None | RunUsage | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                usage_type_0 = RunUsage.from_dict(data)



                return usage_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RunUsage | Unset, data)

        usage = _parse_usage(d.pop("usage", UNSET))


        _debug = d.pop("debug", UNSET)
        debug: RunDebug | Unset
        if isinstance(_debug,  Unset):
            debug = UNSET
        else:
            debug = RunDebug.from_dict(_debug)




        run = cls(
            id=id,
            type_=type_,
            finished=finished,
            timing=timing,
            source=source,
            trigger=trigger,
            execution=execution,
            eval_=eval_,
            output=output,
            files=files,
            error=error,
            input_=input_,
            usage=usage,
            debug=debug,
        )

        return run
