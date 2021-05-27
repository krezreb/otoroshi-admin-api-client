from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.otoroshiutilsmailer_console_mailer_settings_type import OtoroshiutilsmailerConsoleMailerSettingsType
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshiutilsmailerConsoleMailerSettings")


@attr.s(auto_attribs=True)
class OtoroshiutilsmailerConsoleMailerSettings:
    """Settings for the console mailer"""

    type: Union[Unset, OtoroshiutilsmailerConsoleMailerSettingsType] = UNSET
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
        type: Union[Unset, OtoroshiutilsmailerConsoleMailerSettingsType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = OtoroshiutilsmailerConsoleMailerSettingsType(_type)

        otoroshiutilsmailer_console_mailer_settings = cls(
            type=type,
        )

        otoroshiutilsmailer_console_mailer_settings.additional_properties = d
        return otoroshiutilsmailer_console_mailer_settings

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
