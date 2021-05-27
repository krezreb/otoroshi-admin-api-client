from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.otoroshimodels_ip_stack_geolocation_settings_type import OtoroshimodelsIpStackGeolocationSettingsType
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshimodelsIpStackGeolocationSettings")


@attr.s(auto_attribs=True)
class OtoroshimodelsIpStackGeolocationSettings:
    """Settings for connection to IpStack"""

    apikey: Union[Unset, str] = UNSET
    type: Union[Unset, OtoroshimodelsIpStackGeolocationSettingsType] = UNSET
    enabled: Union[Unset, bool] = UNSET
    timeout: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        apikey = self.apikey
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        enabled = self.enabled
        timeout = self.timeout

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if apikey is not UNSET:
            field_dict["apikey"] = apikey
        if type is not UNSET:
            field_dict["type"] = type
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if timeout is not UNSET:
            field_dict["timeout"] = timeout

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        apikey = d.pop("apikey", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, OtoroshimodelsIpStackGeolocationSettingsType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = OtoroshimodelsIpStackGeolocationSettingsType(_type)

        enabled = d.pop("enabled", UNSET)

        timeout = d.pop("timeout", UNSET)

        otoroshimodels_ip_stack_geolocation_settings = cls(
            apikey=apikey,
            type=type,
            enabled=enabled,
            timeout=timeout,
        )

        otoroshimodels_ip_stack_geolocation_settings.additional_properties = d
        return otoroshimodels_ip_stack_geolocation_settings

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
