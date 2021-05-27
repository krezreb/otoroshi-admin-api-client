from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.otoroshimodels_load_balancing_type import OtoroshimodelsLoadBalancingType
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshimodelsLoadBalancing")


@attr.s(auto_attribs=True)
class OtoroshimodelsLoadBalancing:
    """Loadbalancing strategy"""

    type: Union[Unset, OtoroshimodelsLoadBalancingType] = UNSET
    ratio: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        ratio = self.ratio

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if ratio is not UNSET:
            field_dict["ratio"] = ratio

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: Union[Unset, OtoroshimodelsLoadBalancingType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = OtoroshimodelsLoadBalancingType(_type)

        ratio = d.pop("ratio", UNSET)

        otoroshimodels_load_balancing = cls(
            type=type,
            ratio=ratio,
        )

        otoroshimodels_load_balancing.additional_properties = d
        return otoroshimodels_load_balancing

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
