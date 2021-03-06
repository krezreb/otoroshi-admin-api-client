from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.otoroshimodels_data_center_match_type import OtoroshimodelsDataCenterMatchType
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshimodelsDataCenterMatch")


@attr.s(auto_attribs=True)
class OtoroshimodelsDataCenterMatch:
    """Match a target if in the same datacenter"""

    type: Union[Unset, OtoroshimodelsDataCenterMatchType] = UNSET
    dc: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        dc = self.dc

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if dc is not UNSET:
            field_dict["dc"] = dc

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: Union[Unset, OtoroshimodelsDataCenterMatchType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = OtoroshimodelsDataCenterMatchType(_type)

        dc = d.pop("dc", UNSET)

        otoroshimodels_data_center_match = cls(
            type=type,
            dc=dc,
        )

        otoroshimodels_data_center_match.additional_properties = d
        return otoroshimodels_data_center_match

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
