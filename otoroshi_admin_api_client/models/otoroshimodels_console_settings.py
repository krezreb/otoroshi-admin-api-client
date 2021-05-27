from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.otoroshimodels_console_settings_type import OtoroshimodelsConsoleSettingsType
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshimodelsConsoleSettings")


@attr.s(auto_attribs=True)
class OtoroshimodelsConsoleSettings:
    """Data exporter that will log everything to the console"""

    type: Union[Unset, OtoroshimodelsConsoleSettingsType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: Union[Unset, OtoroshimodelsConsoleSettingsType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = OtoroshimodelsConsoleSettingsType(_type)

        otoroshimodels_console_settings = cls(
            type=type,
        )

        otoroshimodels_console_settings.additional_properties = d
        return otoroshimodels_console_settings

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