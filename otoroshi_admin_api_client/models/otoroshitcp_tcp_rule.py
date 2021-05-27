from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.otoroshitcp_tcp_target import OtoroshitcpTcpTarget
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshitcpTcpRule")


@attr.s(auto_attribs=True)
class OtoroshitcpTcpRule:
    """Associate targets for a domain (SNI)"""

    domain: Union[Unset, str] = UNSET
    targets: Union[Unset, List[OtoroshitcpTcpTarget]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        domain = self.domain
        targets: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.targets, Unset):
            targets = []
            for targets_item_data in self.targets:
                targets_item = targets_item_data.to_dict()

                targets.append(targets_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if domain is not UNSET:
            field_dict["domain"] = domain
        if targets is not UNSET:
            field_dict["targets"] = targets

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        domain = d.pop("domain", UNSET)

        targets = []
        _targets = d.pop("targets", UNSET)
        for targets_item_data in _targets or []:
            targets_item = OtoroshitcpTcpTarget.from_dict(targets_item_data)

            targets.append(targets_item)

        otoroshitcp_tcp_rule = cls(
            domain=domain,
            targets=targets,
        )

        otoroshitcp_tcp_rule.additional_properties = d
        return otoroshitcp_tcp_rule

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
