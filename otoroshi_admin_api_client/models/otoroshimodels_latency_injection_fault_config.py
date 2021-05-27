from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshimodelsLatencyInjectionFaultConfig")


@attr.s(auto_attribs=True)
class OtoroshimodelsLatencyInjectionFaultConfig:
    """Settings for a latency injection fault (chaos engineering)"""

    ratio: Union[Unset, float] = UNSET
    from_: Union[Unset, float] = UNSET
    to: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ratio = self.ratio
        from_ = self.from_
        to = self.to

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ratio is not UNSET:
            field_dict["ratio"] = ratio
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ratio = d.pop("ratio", UNSET)

        from_ = d.pop("from", UNSET)

        to = d.pop("to", UNSET)

        otoroshimodels_latency_injection_fault_config = cls(
            ratio=ratio,
            from_=from_,
            to=to,
        )

        otoroshimodels_latency_injection_fault_config.additional_properties = d
        return otoroshimodels_latency_injection_fault_config

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
