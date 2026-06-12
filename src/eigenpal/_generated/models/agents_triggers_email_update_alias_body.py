from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.agents_triggers_email_update_alias_body_status import AgentsTriggersEmailUpdateAliasBodyStatus
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.agents_triggers_email_update_alias_body_reply_config import AgentsTriggersEmailUpdateAliasBodyReplyConfig





T = TypeVar("T", bound="AgentsTriggersEmailUpdateAliasBody")



@_attrs_define
class AgentsTriggersEmailUpdateAliasBody:
    """
        Attributes:
            label (None | str | Unset):
            allowlist (list[str] | Unset):
            allow (list[str] | Unset):
            status (AgentsTriggersEmailUpdateAliasBodyStatus | Unset):
            reply_config (AgentsTriggersEmailUpdateAliasBodyReplyConfig | Unset):
            require_sender_auth (bool | Unset):
     """

    label: None | str | Unset = UNSET
    allowlist: list[str] | Unset = UNSET
    allow: list[str] | Unset = UNSET
    status: AgentsTriggersEmailUpdateAliasBodyStatus | Unset = UNSET
    reply_config: AgentsTriggersEmailUpdateAliasBodyReplyConfig | Unset = UNSET
    require_sender_auth: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.agents_triggers_email_update_alias_body_reply_config import AgentsTriggersEmailUpdateAliasBodyReplyConfig
        label: None | str | Unset
        if isinstance(self.label, Unset):
            label = UNSET
        else:
            label = self.label

        allowlist: list[str] | Unset = UNSET
        if not isinstance(self.allowlist, Unset):
            allowlist = self.allowlist



        allow: list[str] | Unset = UNSET
        if not isinstance(self.allow, Unset):
            allow = self.allow



        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        reply_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.reply_config, Unset):
            reply_config = self.reply_config.to_dict()

        require_sender_auth = self.require_sender_auth


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if label is not UNSET:
            field_dict["label"] = label
        if allowlist is not UNSET:
            field_dict["allowlist"] = allowlist
        if allow is not UNSET:
            field_dict["allow"] = allow
        if status is not UNSET:
            field_dict["status"] = status
        if reply_config is not UNSET:
            field_dict["replyConfig"] = reply_config
        if require_sender_auth is not UNSET:
            field_dict["requireSenderAuth"] = require_sender_auth

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agents_triggers_email_update_alias_body_reply_config import AgentsTriggersEmailUpdateAliasBodyReplyConfig
        d = dict(src_dict)
        def _parse_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        label = _parse_label(d.pop("label", UNSET))


        allowlist = cast(list[str], d.pop("allowlist", UNSET))


        allow = cast(list[str], d.pop("allow", UNSET))


        _status = d.pop("status", UNSET)
        status: AgentsTriggersEmailUpdateAliasBodyStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = AgentsTriggersEmailUpdateAliasBodyStatus(_status)




        _reply_config = d.pop("replyConfig", UNSET)
        reply_config: AgentsTriggersEmailUpdateAliasBodyReplyConfig | Unset
        if isinstance(_reply_config,  Unset):
            reply_config = UNSET
        else:
            reply_config = AgentsTriggersEmailUpdateAliasBodyReplyConfig.from_dict(_reply_config)




        require_sender_auth = d.pop("requireSenderAuth", UNSET)

        agents_triggers_email_update_alias_body = cls(
            label=label,
            allowlist=allowlist,
            allow=allow,
            status=status,
            reply_config=reply_config,
            require_sender_auth=require_sender_auth,
        )


        agents_triggers_email_update_alias_body.additional_properties = d
        return agents_triggers_email_update_alias_body

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
