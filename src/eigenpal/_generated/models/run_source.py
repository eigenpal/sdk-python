from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.run_source_git import RunSourceGit





T = TypeVar("T", bound="RunSource")



@_attrs_define
class RunSource:
    """
        Attributes:
            id (str): Owning workflow id or agent id.
            name (None | str):
            version (None | str): Workflow version label (workflow runs only).
            version_id (None | str | Unset): Captured workflow version id (workflow runs only).
            slug (None | str | Unset): Agent slug (agent runs only).
            model (None | str | Unset): LLM model used (agent runs only).
            git (None | RunSourceGit | Unset): Git provenance (agent runs only).
            implementation_available (bool | Unset): Whether the live workflow/agent implementation still exists (`GET
                /api/v1/runs/:id` detail only).
            automation_found (bool | Unset): Whether the owning automation registry row still exists (`GET /api/v1/runs/:id`
                detail only).
            current_version (None | str | Unset): Current released workflow version label when the source is live (`GET
                /api/v1/runs/:id` detail only).
     """

    id: str
    name: None | str
    version: None | str
    version_id: None | str | Unset = UNSET
    slug: None | str | Unset = UNSET
    model: None | str | Unset = UNSET
    git: None | RunSourceGit | Unset = UNSET
    implementation_available: bool | Unset = UNSET
    automation_found: bool | Unset = UNSET
    current_version: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.run_source_git import RunSourceGit
        id = self.id

        name: None | str
        name = self.name

        version: None | str
        version = self.version

        version_id: None | str | Unset
        if isinstance(self.version_id, Unset):
            version_id = UNSET
        else:
            version_id = self.version_id

        slug: None | str | Unset
        if isinstance(self.slug, Unset):
            slug = UNSET
        else:
            slug = self.slug

        model: None | str | Unset
        if isinstance(self.model, Unset):
            model = UNSET
        else:
            model = self.model

        git: dict[str, Any] | None | Unset
        if isinstance(self.git, Unset):
            git = UNSET
        elif isinstance(self.git, RunSourceGit):
            git = self.git.to_dict()
        else:
            git = self.git

        implementation_available = self.implementation_available

        automation_found = self.automation_found

        current_version: None | str | Unset
        if isinstance(self.current_version, Unset):
            current_version = UNSET
        else:
            current_version = self.current_version


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "name": name,
            "version": version,
        })
        if version_id is not UNSET:
            field_dict["versionId"] = version_id
        if slug is not UNSET:
            field_dict["slug"] = slug
        if model is not UNSET:
            field_dict["model"] = model
        if git is not UNSET:
            field_dict["git"] = git
        if implementation_available is not UNSET:
            field_dict["implementationAvailable"] = implementation_available
        if automation_found is not UNSET:
            field_dict["automationFound"] = automation_found
        if current_version is not UNSET:
            field_dict["currentVersion"] = current_version

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.run_source_git import RunSourceGit
        d = dict(src_dict)
        id = d.pop("id")

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))


        def _parse_version(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        version = _parse_version(d.pop("version"))


        def _parse_version_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        version_id = _parse_version_id(d.pop("versionId", UNSET))


        def _parse_slug(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        slug = _parse_slug(d.pop("slug", UNSET))


        def _parse_model(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        model = _parse_model(d.pop("model", UNSET))


        def _parse_git(data: object) -> None | RunSourceGit | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                git_type_0 = RunSourceGit.from_dict(data)



                return git_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RunSourceGit | Unset, data)

        git = _parse_git(d.pop("git", UNSET))


        implementation_available = d.pop("implementationAvailable", UNSET)

        automation_found = d.pop("automationFound", UNSET)

        def _parse_current_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        current_version = _parse_current_version(d.pop("currentVersion", UNSET))


        run_source = cls(
            id=id,
            name=name,
            version=version,
            version_id=version_id,
            slug=slug,
            model=model,
            git=git,
            implementation_available=implementation_available,
            automation_found=automation_found,
            current_version=current_version,
        )

        return run_source
