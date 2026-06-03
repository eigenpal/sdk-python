from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.agents_triggers_email_create_alias_body_reply_config import AgentsTriggersEmailCreateAliasBodyReplyConfig





T = TypeVar("T", bound="AgentsTriggersEmailCreateAliasBody")



@_attrs_define
class AgentsTriggersEmailCreateAliasBody:
    """ 
        Attributes:
            email (str | Unset):
            alias (str | Unset):
            label (str | Unset):
            allowlist (list[str] | Unset):
            allow (list[str] | Unset):
            reply_config (AgentsTriggersEmailCreateAliasBodyReplyConfig | Unset):
     """

    email: str | Unset = UNSET
    alias: str | Unset = UNSET
    label: str | Unset = UNSET
    allowlist: list[str] | Unset = UNSET
    allow: list[str] | Unset = UNSET
    reply_config: AgentsTriggersEmailCreateAliasBodyReplyConfig | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.agents_triggers_email_create_alias_body_reply_config import AgentsTriggersEmailCreateAliasBodyReplyConfig
        email = self.email

        alias = self.alias

        label = self.label

        allowlist: list[str] | Unset = UNSET
        if not isinstance(self.allowlist, Unset):
            allowlist = self.allowlist



        allow: list[str] | Unset = UNSET
        if not isinstance(self.allow, Unset):
            allow = self.allow



        reply_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.reply_config, Unset):
            reply_config = self.reply_config.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if email is not UNSET:
            field_dict["email"] = email
        if alias is not UNSET:
            field_dict["alias"] = alias
        if label is not UNSET:
            field_dict["label"] = label
        if allowlist is not UNSET:
            field_dict["allowlist"] = allowlist
        if allow is not UNSET:
            field_dict["allow"] = allow
        if reply_config is not UNSET:
            field_dict["replyConfig"] = reply_config

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agents_triggers_email_create_alias_body_reply_config import AgentsTriggersEmailCreateAliasBodyReplyConfig
        d = dict(src_dict)
        email = d.pop("email", UNSET)

        alias = d.pop("alias", UNSET)

        label = d.pop("label", UNSET)

        allowlist = cast(list[str], d.pop("allowlist", UNSET))


        allow = cast(list[str], d.pop("allow", UNSET))


        _reply_config = d.pop("replyConfig", UNSET)
        reply_config: AgentsTriggersEmailCreateAliasBodyReplyConfig | Unset
        if isinstance(_reply_config,  Unset):
            reply_config = UNSET
        else:
            reply_config = AgentsTriggersEmailCreateAliasBodyReplyConfig.from_dict(_reply_config)




        agents_triggers_email_create_alias_body = cls(
            email=email,
            alias=alias,
            label=label,
            allowlist=allowlist,
            allow=allow,
            reply_config=reply_config,
        )


        agents_triggers_email_create_alias_body.additional_properties = d
        return agents_triggers_email_create_alias_body

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
