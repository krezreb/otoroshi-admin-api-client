from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.otoroshimodels_target import OtoroshimodelsTarget
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshimodelsCanary")


@attr.s(auto_attribs=True)
class OtoroshimodelsCanary:
    """Settings for canary routing"""

    enabled: Union[Unset, bool] = UNSET
    traffic: Union[Unset, float] = UNSET
    targets: Union[Unset, List[OtoroshimodelsTarget]] = UNSET
    root: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enabled = self.enabled
        traffic = self.traffic
        targets: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.targets, Unset):
            targets = []
            for targets_item_data in self.targets:
                targets_item = targets_item_data.to_dict()

                targets.append(targets_item)

        root = self.root

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if traffic is not UNSET:
            field_dict["traffic"] = traffic
        if targets is not UNSET:
            field_dict["targets"] = targets
        if root is not UNSET:
            field_dict["root"] = root

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        enabled = d.pop("enabled", UNSET)

        traffic = d.pop("traffic", UNSET)

        targets = []
        _targets = d.pop("targets", UNSET)
        for targets_item_data in _targets or []:
            targets_item = OtoroshimodelsTarget.from_dict(targets_item_data)

            targets.append(targets_item)

        root = d.pop("root", UNSET)

        otoroshimodels_canary = cls(
            enabled=enabled,
            traffic=traffic,
            targets=targets,
            root=root,
        )

        otoroshimodels_canary.additional_properties = d
        return otoroshimodels_canary

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
