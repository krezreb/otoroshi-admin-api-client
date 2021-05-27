from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.otoroshimodels_user_rights import OtoroshimodelsUserRights

T = TypeVar("T", bound="OtoroshiauthOauth1ModuleConfigRightsOverride")


@attr.s(auto_attribs=True)
class OtoroshiauthOauth1ModuleConfigRightsOverride:
    """Overrides user rights of users connected by OAuth1 module"""

    additional_properties: Dict[str, OtoroshimodelsUserRights] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        otoroshiauth_oauth_1_module_config_rights_override = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = OtoroshimodelsUserRights.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        otoroshiauth_oauth_1_module_config_rights_override.additional_properties = additional_properties
        return otoroshiauth_oauth_1_module_config_rights_override

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> OtoroshimodelsUserRights:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: OtoroshimodelsUserRights) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
