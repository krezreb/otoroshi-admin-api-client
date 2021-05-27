from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshimodelsIpFiltering")


@attr.s(auto_attribs=True)
class OtoroshimodelsIpFiltering:
    """Settings for ip address filtering for a service or globally"""

    whitelist: Union[Unset, List[str]] = UNSET
    blacklist: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        whitelist: Union[Unset, List[str]] = UNSET
        if not isinstance(self.whitelist, Unset):
            whitelist = self.whitelist

        blacklist: Union[Unset, List[str]] = UNSET
        if not isinstance(self.blacklist, Unset):
            blacklist = self.blacklist

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if whitelist is not UNSET:
            field_dict["whitelist"] = whitelist
        if blacklist is not UNSET:
            field_dict["blacklist"] = blacklist

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        whitelist = cast(List[str], d.pop("whitelist", UNSET))

        blacklist = cast(List[str], d.pop("blacklist", UNSET))

        otoroshimodels_ip_filtering = cls(
            whitelist=whitelist,
            blacklist=blacklist,
        )

        otoroshimodels_ip_filtering.additional_properties = d
        return otoroshimodels_ip_filtering

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
