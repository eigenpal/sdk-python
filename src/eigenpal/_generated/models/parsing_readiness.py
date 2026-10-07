from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.parsing_readiness_image_reading import ParsingReadinessImageReading
from typing import cast
from typing import Literal, cast

if TYPE_CHECKING:
  from ..models.parsing_readiness_providers import ParsingReadinessProviders





T = TypeVar("T", bound="ParsingReadiness")



@_attrs_define
class ParsingReadiness:
    """
        Attributes:
            step_type (Literal['ai.parse-v2']):
            image_reading (ParsingReadinessImageReading):
            providers (ParsingReadinessProviders):
            native_extraction (Literal['requires-worker-probe']):
            live_probe (bool):
            warnings (list[str]):
     """

    step_type: Literal['ai.parse-v2']
    image_reading: ParsingReadinessImageReading
    providers: ParsingReadinessProviders
    native_extraction: Literal['requires-worker-probe']
    live_probe: bool
    warnings: list[str]





    def to_dict(self) -> dict[str, Any]:
        from ..models.parsing_readiness_providers import ParsingReadinessProviders # noqa: PLC0415
        step_type = self.step_type

        image_reading = self.image_reading.value

        providers = self.providers.to_dict()

        native_extraction = self.native_extraction

        live_probe = self.live_probe

        warnings = self.warnings




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "stepType": step_type,
            "imageReading": image_reading,
            "providers": providers,
            "nativeExtraction": native_extraction,
            "liveProbe": live_probe,
            "warnings": warnings,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.parsing_readiness_providers import ParsingReadinessProviders # noqa: PLC0415
        d = dict(src_dict)
        step_type = cast(Literal['ai.parse-v2'] , d.pop("stepType"))
        if step_type != 'ai.parse-v2':
            raise ValueError(f"stepType must match const 'ai.parse-v2', got '{step_type}'")

        image_reading = ParsingReadinessImageReading(d.pop("imageReading"))




        providers = ParsingReadinessProviders.from_dict(d.pop("providers"))




        native_extraction = cast(Literal['requires-worker-probe'] , d.pop("nativeExtraction"))
        if native_extraction != 'requires-worker-probe':
            raise ValueError(f"nativeExtraction must match const 'requires-worker-probe', got '{native_extraction}'")

        live_probe = d.pop("liveProbe")

        warnings = cast(list[str], d.pop("warnings"))


        parsing_readiness = cls(
            step_type=step_type,
            image_reading=image_reading,
            providers=providers,
            native_extraction=native_extraction,
            live_probe=live_probe,
            warnings=warnings,
        )

        return parsing_readiness
