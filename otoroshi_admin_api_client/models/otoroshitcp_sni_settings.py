from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.otoroshitcp_tcp_target import OtoroshitcpTcpTarget
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshitcpSniSettings")


@attr.s(auto_attribs=True)
class OtoroshitcpSniSettings:
    """SNI settings for a TCP proxy"""

    enabled: Union[Unset, bool] = UNSET
    forward_if_no_match: Union[Unset, bool] = UNSET
    forwards_to: Union[Unset, OtoroshitcpTcpTarget] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enabled = self.enabled
        forward_if_no_match = self.forward_if_no_match
        forwards_to: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.forwards_to, Unset):
            forwards_to = self.forwards_to.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if forward_if_no_match is not UNSET:
            field_dict["forwardIfNoMatch"] = forward_if_no_match
        if forwards_to is not UNSET:
            field_dict["forwardsTo"] = forwards_to

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        enabled = d.pop("enabled", UNSET)

        forward_if_no_match = d.pop("forwardIfNoMatch", UNSET)

        _forwards_to = d.pop("forwardsTo", UNSET)
        forwards_to: Union[Unset, OtoroshitcpTcpTarget]
        if isinstance(_forwards_to, Unset):
            forwards_to = UNSET
        else:
            forwards_to = OtoroshitcpTcpTarget.from_dict(_forwards_to)

        otoroshitcp_sni_settings = cls(
            enabled=enabled,
            forward_if_no_match=forward_if_no_match,
            forwards_to=forwards_to,
        )

        otoroshitcp_sni_settings.additional_properties = d
        return otoroshitcp_sni_settings

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
