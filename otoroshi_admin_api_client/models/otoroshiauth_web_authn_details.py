from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.otoroshiauth_web_authn_details_credentials import OtoroshiauthWebAuthnDetailsCredentials
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshiauthWebAuthnDetails")


@attr.s(auto_attribs=True)
class OtoroshiauthWebAuthnDetails:
    """Handle and credentials for a webauthn user"""

    handle: Union[Unset, str] = UNSET
    credentials: Union[Unset, OtoroshiauthWebAuthnDetailsCredentials] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        handle = self.handle
        credentials: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.credentials, Unset):
            credentials = self.credentials.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if handle is not UNSET:
            field_dict["handle"] = handle
        if credentials is not UNSET:
            field_dict["credentials"] = credentials

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        handle = d.pop("handle", UNSET)

        _credentials = d.pop("credentials", UNSET)
        credentials: Union[Unset, OtoroshiauthWebAuthnDetailsCredentials]
        if isinstance(_credentials, Unset):
            credentials = UNSET
        else:
            credentials = OtoroshiauthWebAuthnDetailsCredentials.from_dict(_credentials)

        otoroshiauth_web_authn_details = cls(
            handle=handle,
            credentials=credentials,
        )

        otoroshiauth_web_authn_details.additional_properties = d
        return otoroshiauth_web_authn_details

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
