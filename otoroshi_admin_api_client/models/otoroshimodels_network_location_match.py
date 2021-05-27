from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.otoroshimodels_network_location_match_type import OtoroshimodelsNetworkLocationMatchType
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshimodelsNetworkLocationMatch")


@attr.s(auto_attribs=True)
class OtoroshimodelsNetworkLocationMatch:
    """Match a target if in the same network location"""

    rack: Union[Unset, str] = UNSET
    provider: Union[Unset, str] = UNSET
    data_center: Union[Unset, str] = UNSET
    zone: Union[Unset, str] = UNSET
    type: Union[Unset, OtoroshimodelsNetworkLocationMatchType] = UNSET
    region: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        rack = self.rack
        provider = self.provider
        data_center = self.data_center
        zone = self.zone
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        region = self.region

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rack is not UNSET:
            field_dict["rack"] = rack
        if provider is not UNSET:
            field_dict["provider"] = provider
        if data_center is not UNSET:
            field_dict["dataCenter"] = data_center
        if zone is not UNSET:
            field_dict["zone"] = zone
        if type is not UNSET:
            field_dict["type"] = type
        if region is not UNSET:
            field_dict["region"] = region

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        rack = d.pop("rack", UNSET)

        provider = d.pop("provider", UNSET)

        data_center = d.pop("dataCenter", UNSET)

        zone = d.pop("zone", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, OtoroshimodelsNetworkLocationMatchType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = OtoroshimodelsNetworkLocationMatchType(_type)

        region = d.pop("region", UNSET)

        otoroshimodels_network_location_match = cls(
            rack=rack,
            provider=provider,
            data_center=data_center,
            zone=zone,
            type=type,
            region=region,
        )

        otoroshimodels_network_location_match.additional_properties = d
        return otoroshimodels_network_location_match

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
