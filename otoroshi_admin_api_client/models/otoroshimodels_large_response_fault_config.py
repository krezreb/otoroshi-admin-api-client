from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshimodelsLargeResponseFaultConfig")


@attr.s(auto_attribs=True)
class OtoroshimodelsLargeResponseFaultConfig:
    """Settings for a large response fault (chaos engineering)"""

    ratio: Union[Unset, float] = UNSET
    additional_response_size: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ratio = self.ratio
        additional_response_size = self.additional_response_size

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ratio is not UNSET:
            field_dict["ratio"] = ratio
        if additional_response_size is not UNSET:
            field_dict["additionalResponseSize"] = additional_response_size

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ratio = d.pop("ratio", UNSET)

        additional_response_size = d.pop("additionalResponseSize", UNSET)

        otoroshimodels_large_response_fault_config = cls(
            ratio=ratio,
            additional_response_size=additional_response_size,
        )

        otoroshimodels_large_response_fault_config.additional_properties = d
        return otoroshimodels_large_response_fault_config

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
