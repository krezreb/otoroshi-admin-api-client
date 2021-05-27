from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.otoroshiauth_ldap_auth_module_config_data_override_additional_property import (
    OtoroshiauthLdapAuthModuleConfigDataOverrideAdditionalProperty,
)

T = TypeVar("T", bound="OtoroshiauthLdapAuthModuleConfigDataOverride")


@attr.s(auto_attribs=True)
class OtoroshiauthLdapAuthModuleConfigDataOverride:
    """Overiddes user data. Object with email as key"""

    additional_properties: Dict[str, OtoroshiauthLdapAuthModuleConfigDataOverrideAdditionalProperty] = attr.ib(
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
        otoroshiauth_ldap_auth_module_config_data_override = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = OtoroshiauthLdapAuthModuleConfigDataOverrideAdditionalProperty.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        otoroshiauth_ldap_auth_module_config_data_override.additional_properties = additional_properties
        return otoroshiauth_ldap_auth_module_config_data_override

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> OtoroshiauthLdapAuthModuleConfigDataOverrideAdditionalProperty:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: OtoroshiauthLdapAuthModuleConfigDataOverrideAdditionalProperty) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
