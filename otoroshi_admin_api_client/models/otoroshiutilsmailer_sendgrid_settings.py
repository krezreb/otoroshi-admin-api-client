from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.otoroshiutilsmailer_email_location import OtoroshiutilsmailerEmailLocation
from ..models.otoroshiutilsmailer_sendgrid_settings_type import OtoroshiutilsmailerSendgridSettingsType
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshiutilsmailerSendgridSettings")


@attr.s(auto_attribs=True)
class OtoroshiutilsmailerSendgridSettings:
    """Settings for the sendgrid mailer"""

    api_key: Union[Unset, str] = UNSET
    to: Union[Unset, List[OtoroshiutilsmailerEmailLocation]] = UNSET
    type: Union[Unset, OtoroshiutilsmailerSendgridSettingsType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        api_key = self.api_key
        to: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.to, Unset):
            to = []
            for to_item_data in self.to:
                to_item = to_item_data.to_dict()

                to.append(to_item)

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if api_key is not UNSET:
            field_dict["apiKey"] = api_key
        if to is not UNSET:
            field_dict["to"] = to
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        api_key = d.pop("apiKey", UNSET)

        to = []
        _to = d.pop("to", UNSET)
        for to_item_data in _to or []:
            to_item = OtoroshiutilsmailerEmailLocation.from_dict(to_item_data)

            to.append(to_item)

        _type = d.pop("type", UNSET)
        type: Union[Unset, OtoroshiutilsmailerSendgridSettingsType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = OtoroshiutilsmailerSendgridSettingsType(_type)

        otoroshiutilsmailer_sendgrid_settings = cls(
            api_key=api_key,
            to=to,
            type=type,
        )

        otoroshiutilsmailer_sendgrid_settings.additional_properties = d
        return otoroshiutilsmailer_sendgrid_settings

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
