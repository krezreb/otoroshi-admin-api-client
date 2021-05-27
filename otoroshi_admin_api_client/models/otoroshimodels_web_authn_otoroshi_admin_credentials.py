from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.otoroshimodels_web_authn_otoroshi_admin_credentials_additional_property import (
    OtoroshimodelsWebAuthnOtoroshiAdminCredentialsAdditionalProperty,
)

T = TypeVar("T", bound="OtoroshimodelsWebAuthnOtoroshiAdminCredentials")


@attr.s(auto_attribs=True)
class OtoroshimodelsWebAuthnOtoroshiAdminCredentials:
    """User webauthn credentials"""

    additional_properties: Dict[str, OtoroshimodelsWebAuthnOtoroshiAdminCredentialsAdditionalProperty] = attr.ib(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        otoroshimodels_web_authn_otoroshi_admin_credentials = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = OtoroshimodelsWebAuthnOtoroshiAdminCredentialsAdditionalProperty.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        otoroshimodels_web_authn_otoroshi_admin_credentials.additional_properties = additional_properties
        return otoroshimodels_web_authn_otoroshi_admin_credentials

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> OtoroshimodelsWebAuthnOtoroshiAdminCredentialsAdditionalProperty:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: OtoroshimodelsWebAuthnOtoroshiAdminCredentialsAdditionalProperty) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
