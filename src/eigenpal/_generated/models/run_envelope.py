from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.run_envelope_run_type_1 import RunEnvelopeRunType1
  from ..models.run_summary import RunSummary





T = TypeVar("T", bound="RunEnvelope")



@_attrs_define
class RunEnvelope:
    """ 
        Attributes:
            run (RunEnvelopeRunType1 | RunSummary):
     """

    run: RunEnvelopeRunType1 | RunSummary





    def to_dict(self) -> dict[str, Any]:
        from ..models.run_envelope_run_type_1 import RunEnvelopeRunType1
        from ..models.run_summary import RunSummary
        run: dict[str, Any]
        if isinstance(self.run, RunSummary):
            run = self.run.to_dict()
        else:
            run = self.run.to_dict()



        field_dict: dict[str, Any] = {}

        field_dict.update({
            "run": run,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.run_envelope_run_type_1 import RunEnvelopeRunType1
        from ..models.run_summary import RunSummary
        d = dict(src_dict)
        def _parse_run(data: object) -> RunEnvelopeRunType1 | RunSummary:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                run_type_0 = RunSummary.from_dict(data)



                return run_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            run_type_1 = RunEnvelopeRunType1.from_dict(data)



            return run_type_1

        run = _parse_run(d.pop("run"))


        run_envelope = cls(
            run=run,
        )

        return run_envelope

