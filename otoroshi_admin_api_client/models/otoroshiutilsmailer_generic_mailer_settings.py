from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.otoroshiutilsmailer_email_location import OtoroshiutilsmailerEmailLocation
from ..models.otoroshiutilsmailer_generic_mailer_settings_headers import OtoroshiutilsmailerGenericMailerSettingsHeaders
from ..models.otoroshiutilsmailer_generic_mailer_settings_type import OtoroshiutilsmailerGenericMailerSettingsType
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshiutilsmailerGenericMailerSettings")


@attr.s(auto_attribs=True)
class OtoroshiutilsmailerGenericMailerSettings:
    """Settings for the generic mailer (http requests)"""

    headers: Union[Unset, OtoroshiutilsmailerGenericMailerSettingsHeaders] = UNSET
    to: Union[Unset, List[OtoroshiutilsmailerEmailLocation]] = UNSET
    type: Union[Unset, OtoroshiutilsmailerGenericMailerSettingsType] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        headers: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        to: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.to, Unset):
            to = []
            for to_item_data in self.to:
                to_item = to_item_data.to_dict()

                to.append(to_item)

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if headers is not UNSET:
            field_dict["headers"] = headers
        if to is not UNSET:
            field_dict["to"] = to
        if type is not UNSET:
            field_dict["type"] = type
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _headers = d.pop("headers", UNSET)
        headers: Union[Unset, OtoroshiutilsmailerGenericMailerSettingsHeaders]
        if isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = OtoroshiutilsmailerGenericMailerSettingsHeaders.from_dict(_headers)

        to = []
        _to = d.pop("to", UNSET)
        for to_item_data in _to or []:
            to_item = OtoroshiutilsmailerEmailLocation.from_dict(to_item_data)

            to.append(to_item)

        _type = d.pop("type", UNSET)
        type: Union[Unset, OtoroshiutilsmailerGenericMailerSettingsType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = OtoroshiutilsmailerGenericMailerSettingsType(_type)

        url = d.pop("url", UNSET)

        otoroshiutilsmailer_generic_mailer_settings = cls(
            headers=headers,
            to=to,
            type=type,
            url=url,
        )

        otoroshiutilsmailer_generic_mailer_settings.additional_properties = d
        return otoroshiutilsmailer_generic_mailer_settings

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
