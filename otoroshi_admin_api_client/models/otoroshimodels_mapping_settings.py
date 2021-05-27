from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.otoroshimodels_mapping_settings_map import OtoroshimodelsMappingSettingsMap
from ..models.otoroshimodels_mapping_settings_values import OtoroshimodelsMappingSettingsValues
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshimodelsMappingSettings")


@attr.s(auto_attribs=True)
class OtoroshimodelsMappingSettings:
    """Settings to transform a jwt token"""

    map_: Union[Unset, OtoroshimodelsMappingSettingsMap] = UNSET
    values: Union[Unset, OtoroshimodelsMappingSettingsValues] = UNSET
    remove: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        map_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.map_, Unset):
            map_ = self.map_.to_dict()

        values: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.values, Unset):
            values = self.values.to_dict()

        remove: Union[Unset, List[str]] = UNSET
        if not isinstance(self.remove, Unset):
            remove = self.remove

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if map_ is not UNSET:
            field_dict["map"] = map_
        if values is not UNSET:
            field_dict["values"] = values
        if remove is not UNSET:
            field_dict["remove"] = remove

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _map_ = d.pop("map", UNSET)
        map_: Union[Unset, OtoroshimodelsMappingSettingsMap]
        if isinstance(_map_, Unset):
            map_ = UNSET
        else:
            map_ = OtoroshimodelsMappingSettingsMap.from_dict(_map_)

        _values = d.pop("values", UNSET)
        values: Union[Unset, OtoroshimodelsMappingSettingsValues]
        if isinstance(_values, Unset):
            values = UNSET
        else:
            values = OtoroshimodelsMappingSettingsValues.from_dict(_values)

        remove = cast(List[str], d.pop("remove", UNSET))

        otoroshimodels_mapping_settings = cls(
            map_=map_,
            values=values,
            remove=remove,
        )

        otoroshimodels_mapping_settings.additional_properties = d
        return otoroshimodels_mapping_settings

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
