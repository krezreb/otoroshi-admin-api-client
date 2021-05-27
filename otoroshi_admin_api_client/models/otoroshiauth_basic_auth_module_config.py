from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.otoroshiauth_basic_auth_module_config_metadata import OtoroshiauthBasicAuthModuleConfigMetadata
from ..models.otoroshiauth_basic_auth_module_config_type import OtoroshiauthBasicAuthModuleConfigType
from ..models.otoroshiauth_basic_auth_user import OtoroshiauthBasicAuthUser
from ..models.otoroshiauth_session_cookie_values import OtoroshiauthSessionCookieValues
from ..models.otoroshimodels_entity_location import OtoroshimodelsEntityLocation
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshiauthBasicAuthModuleConfig")


@attr.s(auto_attribs=True)
class OtoroshiauthBasicAuthModuleConfig:
    """Authentication module that let you use otoroshi as the identity provider"""

    session_max_age: Union[Unset, int] = UNSET
    metadata: Union[Unset, OtoroshiauthBasicAuthModuleConfigMetadata] = UNSET
    session_cookie_values: Union[Unset, OtoroshiauthSessionCookieValues] = UNSET
    basic_auth: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    webauthn: Union[Unset, bool] = UNSET
    location: Union[Unset, OtoroshimodelsEntityLocation] = UNSET
    id: Union[Unset, str] = UNSET
    type: Union[Unset, OtoroshiauthBasicAuthModuleConfigType] = UNSET
    users: Union[Unset, List[OtoroshiauthBasicAuthUser]] = UNSET
    desc: Union[Unset, str] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        session_max_age = self.session_max_age
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        session_cookie_values: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.session_cookie_values, Unset):
            session_cookie_values = self.session_cookie_values.to_dict()

        basic_auth = self.basic_auth
        name = self.name
        webauthn = self.webauthn
        location: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict()

        id = self.id
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        users: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.users, Unset):
            users = []
            for users_item_data in self.users:
                users_item = users_item_data.to_dict()

                users.append(users_item)

        desc = self.desc
        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if session_max_age is not UNSET:
            field_dict["sessionMaxAge"] = session_max_age
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if session_cookie_values is not UNSET:
            field_dict["sessionCookieValues"] = session_cookie_values
        if basic_auth is not UNSET:
            field_dict["basicAuth"] = basic_auth
        if name is not UNSET:
            field_dict["name"] = name
        if webauthn is not UNSET:
            field_dict["webauthn"] = webauthn
        if location is not UNSET:
            field_dict["location"] = location
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["type"] = type
        if users is not UNSET:
            field_dict["users"] = users
        if desc is not UNSET:
            field_dict["desc"] = desc
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        session_max_age = d.pop("sessionMaxAge", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, OtoroshiauthBasicAuthModuleConfigMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = OtoroshiauthBasicAuthModuleConfigMetadata.from_dict(_metadata)

        _session_cookie_values = d.pop("sessionCookieValues", UNSET)
        session_cookie_values: Union[Unset, OtoroshiauthSessionCookieValues]
        if isinstance(_session_cookie_values, Unset):
            session_cookie_values = UNSET
        else:
            session_cookie_values = OtoroshiauthSessionCookieValues.from_dict(_session_cookie_values)

        basic_auth = d.pop("basicAuth", UNSET)

        name = d.pop("name", UNSET)

        webauthn = d.pop("webauthn", UNSET)

        _location = d.pop("location", UNSET)
        location: Union[Unset, OtoroshimodelsEntityLocation]
        if isinstance(_location, Unset):
            location = UNSET
        else:
            location = OtoroshimodelsEntityLocation.from_dict(_location)

        id = d.pop("id", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, OtoroshiauthBasicAuthModuleConfigType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = OtoroshiauthBasicAuthModuleConfigType(_type)

        users = []
        _users = d.pop("users", UNSET)
        for users_item_data in _users or []:
            users_item = OtoroshiauthBasicAuthUser.from_dict(users_item_data)

            users.append(users_item)

        desc = d.pop("desc", UNSET)

        tags = cast(List[str], d.pop("tags", UNSET))

        otoroshiauth_basic_auth_module_config = cls(
            session_max_age=session_max_age,
            metadata=metadata,
            session_cookie_values=session_cookie_values,
            basic_auth=basic_auth,
            name=name,
            webauthn=webauthn,
            location=location,
            id=id,
            type=type,
            users=users,
            desc=desc,
            tags=tags,
        )

        otoroshiauth_basic_auth_module_config.additional_properties = d
        return otoroshiauth_basic_auth_module_config

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
