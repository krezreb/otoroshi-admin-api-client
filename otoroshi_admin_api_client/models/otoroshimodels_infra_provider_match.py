from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.otoroshimodels_infra_provider_match_type import OtoroshimodelsInfraProviderMatchType
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshimodelsInfraProviderMatch")


@attr.s(auto_attribs=True)
class OtoroshimodelsInfraProviderMatch:
    """Match a target if in the same infrastructure"""

    provider: Union[Unset, str] = UNSET
    type: Union[Unset, OtoroshimodelsInfraProviderMatchType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        provider = self.provider
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if provider is not UNSET:
            field_dict["provider"] = provider
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        provider = d.pop("provider", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, OtoroshimodelsInfraProviderMatchType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = OtoroshimodelsInfraProviderMatchType(_type)

        otoroshimodels_infra_provider_match = cls(
            provider=provider,
            type=type,
        )

        otoroshimodels_infra_provider_match.additional_properties = d
        return otoroshimodels_infra_provider_match

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
