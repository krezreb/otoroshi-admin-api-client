from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.otoroshimodels_region_match_type import OtoroshimodelsRegionMatchType
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshimodelsRegionMatch")


@attr.s(auto_attribs=True)
class OtoroshimodelsRegionMatch:
    """Match a target if in the same region"""

    type: Union[Unset, OtoroshimodelsRegionMatchType] = UNSET
    region: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        region = self.region

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if region is not UNSET:
            field_dict["region"] = region

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: Union[Unset, OtoroshimodelsRegionMatchType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = OtoroshimodelsRegionMatchType(_type)

        region = d.pop("region", UNSET)

        otoroshimodels_region_match = cls(
            type=type,
            region=region,
        )

        otoroshimodels_region_match.additional_properties = d
        return otoroshimodels_region_match

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
