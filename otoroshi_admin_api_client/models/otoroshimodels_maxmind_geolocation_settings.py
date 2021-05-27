from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.otoroshimodels_maxmind_geolocation_settings_type import OtoroshimodelsMaxmindGeolocationSettingsType
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshimodelsMaxmindGeolocationSettings")


@attr.s(auto_attribs=True)
class OtoroshimodelsMaxmindGeolocationSettings:
    """Settings for connection to a maxmind db"""

    path: Union[Unset, str] = UNSET
    type: Union[Unset, OtoroshimodelsMaxmindGeolocationSettingsType] = UNSET
    enabled: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        path = self.path
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        enabled = self.enabled

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if path is not UNSET:
            field_dict["path"] = path
        if type is not UNSET:
            field_dict["type"] = type
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        path = d.pop("path", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, OtoroshimodelsMaxmindGeolocationSettingsType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = OtoroshimodelsMaxmindGeolocationSettingsType(_type)

        enabled = d.pop("enabled", UNSET)

        otoroshimodels_maxmind_geolocation_settings = cls(
            path=path,
            type=type,
            enabled=enabled,
        )

        otoroshimodels_maxmind_geolocation_settings.additional_properties = d
        return otoroshimodels_maxmind_geolocation_settings

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
