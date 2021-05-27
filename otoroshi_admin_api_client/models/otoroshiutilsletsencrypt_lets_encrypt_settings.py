from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshiutilsletsencryptLetsEncryptSettings")


@attr.s(auto_attribs=True)
class OtoroshiutilsletsencryptLetsEncryptSettings:
    """Settings for connection to a let's encrypt (or ACME) server"""

    private_key: Union[Unset, str] = UNSET
    contacts: Union[Unset, List[str]] = UNSET
    emails: Union[Unset, List[str]] = UNSET
    enabled: Union[Unset, bool] = UNSET
    public_key: Union[Unset, str] = UNSET
    server: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        private_key = self.private_key
        contacts: Union[Unset, List[str]] = UNSET
        if not isinstance(self.contacts, Unset):
            contacts = self.contacts

        emails: Union[Unset, List[str]] = UNSET
        if not isinstance(self.emails, Unset):
            emails = self.emails

        enabled = self.enabled
        public_key = self.public_key
        server = self.server

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if private_key is not UNSET:
            field_dict["privateKey"] = private_key
        if contacts is not UNSET:
            field_dict["contacts"] = contacts
        if emails is not UNSET:
            field_dict["emails"] = emails
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if public_key is not UNSET:
            field_dict["publicKey"] = public_key
        if server is not UNSET:
            field_dict["server"] = server

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        private_key = d.pop("privateKey", UNSET)

        contacts = cast(List[str], d.pop("contacts", UNSET))

        emails = cast(List[str], d.pop("emails", UNSET))

        enabled = d.pop("enabled", UNSET)

        public_key = d.pop("publicKey", UNSET)

        server = d.pop("server", UNSET)

        otoroshiutilsletsencrypt_lets_encrypt_settings = cls(
            private_key=private_key,
            contacts=contacts,
            emails=emails,
            enabled=enabled,
            public_key=public_key,
            server=server,
        )

        otoroshiutilsletsencrypt_lets_encrypt_settings.additional_properties = d
        return otoroshiutilsletsencrypt_lets_encrypt_settings

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
