from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.otoroshiutilsmailer_email_location import OtoroshiutilsmailerEmailLocation
from ..models.otoroshiutilsmailer_mailjet_settings_type import OtoroshiutilsmailerMailjetSettingsType
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshiutilsmailerMailjetSettings")


@attr.s(auto_attribs=True)
class OtoroshiutilsmailerMailjetSettings:
    """Settings for the mailjet mailer"""

    api_key_private: Union[Unset, str] = UNSET
    api_key_public: Union[Unset, str] = UNSET
    to: Union[Unset, List[OtoroshiutilsmailerEmailLocation]] = UNSET
    type: Union[Unset, OtoroshiutilsmailerMailjetSettingsType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        api_key_private = self.api_key_private
        api_key_public = self.api_key_public
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
        if api_key_private is not UNSET:
            field_dict["apiKeyPrivate"] = api_key_private
        if api_key_public is not UNSET:
            field_dict["apiKeyPublic"] = api_key_public
        if to is not UNSET:
            field_dict["to"] = to
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        api_key_private = d.pop("apiKeyPrivate", UNSET)

        api_key_public = d.pop("apiKeyPublic", UNSET)

        to = []
        _to = d.pop("to", UNSET)
        for to_item_data in _to or []:
            to_item = OtoroshiutilsmailerEmailLocation.from_dict(to_item_data)

            to.append(to_item)

        _type = d.pop("type", UNSET)
        type: Union[Unset, OtoroshiutilsmailerMailjetSettingsType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = OtoroshiutilsmailerMailjetSettingsType(_type)

        otoroshiutilsmailer_mailjet_settings = cls(
            api_key_private=api_key_private,
            api_key_public=api_key_public,
            to=to,
            type=type,
        )

        otoroshiutilsmailer_mailjet_settings.additional_properties = d
        return otoroshiutilsmailer_mailjet_settings

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
