from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.otoroshiauth_o_auth_1_provider import OtoroshiauthOAuth1Provider
from ..models.otoroshiauth_oauth_1_module_config_metadata import OtoroshiauthOauth1ModuleConfigMetadata
from ..models.otoroshiauth_oauth_1_module_config_rights_override import OtoroshiauthOauth1ModuleConfigRightsOverride
from ..models.otoroshiauth_oauth_1_module_config_type import OtoroshiauthOauth1ModuleConfigType
from ..models.otoroshiauth_session_cookie_values import OtoroshiauthSessionCookieValues
from ..models.otoroshimodels_entity_location import OtoroshimodelsEntityLocation
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshiauthOauth1ModuleConfig")


@attr.s(auto_attribs=True)
class OtoroshiauthOauth1ModuleConfig:
    """Configuration of OAuth 1.0 module"""

    profile_url: Union[Unset, str] = UNSET
    metadata: Union[Unset, OtoroshiauthOauth1ModuleConfigMetadata] = UNSET
    authorize_url: Union[Unset, str] = UNSET
    request_token_url: Union[Unset, str] = UNSET
    session_cookie_values: Union[Unset, OtoroshiauthSessionCookieValues] = UNSET
    type: Union[Unset, OtoroshiauthOauth1ModuleConfigType] = UNSET
    http_method: Union[Unset, OtoroshiauthOAuth1Provider] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    session_max_age: Union[Unset, int] = UNSET
    consumer_secret: Union[Unset, str] = UNSET
    access_token_url: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    rights_override: Union[Unset, OtoroshiauthOauth1ModuleConfigRightsOverride] = UNSET
    callback_url: Union[Unset, str] = UNSET
    location: Union[Unset, OtoroshimodelsEntityLocation] = UNSET
    id: Union[Unset, str] = UNSET
    consumer_key: Union[Unset, str] = UNSET
    desc: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        profile_url = self.profile_url
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        authorize_url = self.authorize_url
        request_token_url = self.request_token_url
        session_cookie_values: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.session_cookie_values, Unset):
            session_cookie_values = self.session_cookie_values.to_dict()

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        http_method: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.http_method, Unset):
            http_method = self.http_method.to_dict()

        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        session_max_age = self.session_max_age
        consumer_secret = self.consumer_secret
        access_token_url = self.access_token_url
        name = self.name
        rights_override: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.rights_override, Unset):
            rights_override = self.rights_override.to_dict()

        callback_url = self.callback_url
        location: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict()

        id = self.id
        consumer_key = self.consumer_key
        desc = self.desc

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if profile_url is not UNSET:
            field_dict["profileURL"] = profile_url
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if authorize_url is not UNSET:
            field_dict["authorizeURL"] = authorize_url
        if request_token_url is not UNSET:
            field_dict["requestTokenURL"] = request_token_url
        if session_cookie_values is not UNSET:
            field_dict["sessionCookieValues"] = session_cookie_values
        if type is not UNSET:
            field_dict["type"] = type
        if http_method is not UNSET:
            field_dict["httpMethod"] = http_method
        if tags is not UNSET:
            field_dict["tags"] = tags
        if session_max_age is not UNSET:
            field_dict["sessionMaxAge"] = session_max_age
        if consumer_secret is not UNSET:
            field_dict["consumerSecret"] = consumer_secret
        if access_token_url is not UNSET:
            field_dict["accessTokenURL"] = access_token_url
        if name is not UNSET:
            field_dict["name"] = name
        if rights_override is not UNSET:
            field_dict["rightsOverride"] = rights_override
        if callback_url is not UNSET:
            field_dict["callbackURL"] = callback_url
        if location is not UNSET:
            field_dict["location"] = location
        if id is not UNSET:
            field_dict["id"] = id
        if consumer_key is not UNSET:
            field_dict["consumerKey"] = consumer_key
        if desc is not UNSET:
            field_dict["desc"] = desc

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        profile_url = d.pop("profileURL", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, OtoroshiauthOauth1ModuleConfigMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = OtoroshiauthOauth1ModuleConfigMetadata.from_dict(_metadata)

        authorize_url = d.pop("authorizeURL", UNSET)

        request_token_url = d.pop("requestTokenURL", UNSET)

        _session_cookie_values = d.pop("sessionCookieValues", UNSET)
        session_cookie_values: Union[Unset, OtoroshiauthSessionCookieValues]
        if isinstance(_session_cookie_values, Unset):
            session_cookie_values = UNSET
        else:
            session_cookie_values = OtoroshiauthSessionCookieValues.from_dict(_session_cookie_values)

        _type = d.pop("type", UNSET)
        type: Union[Unset, OtoroshiauthOauth1ModuleConfigType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = OtoroshiauthOauth1ModuleConfigType(_type)

        _http_method = d.pop("httpMethod", UNSET)
        http_method: Union[Unset, OtoroshiauthOAuth1Provider]
        if isinstance(_http_method, Unset):
            http_method = UNSET
        else:
            http_method = OtoroshiauthOAuth1Provider.from_dict(_http_method)

        tags = cast(List[str], d.pop("tags", UNSET))

        session_max_age = d.pop("sessionMaxAge", UNSET)

        consumer_secret = d.pop("consumerSecret", UNSET)

        access_token_url = d.pop("accessTokenURL", UNSET)

        name = d.pop("name", UNSET)

        _rights_override = d.pop("rightsOverride", UNSET)
        rights_override: Union[Unset, OtoroshiauthOauth1ModuleConfigRightsOverride]
        if isinstance(_rights_override, Unset):
            rights_override = UNSET
        else:
            rights_override = OtoroshiauthOauth1ModuleConfigRightsOverride.from_dict(_rights_override)

        callback_url = d.pop("callbackURL", UNSET)

        _location = d.pop("location", UNSET)
        location: Union[Unset, OtoroshimodelsEntityLocation]
        if isinstance(_location, Unset):
            location = UNSET
        else:
            location = OtoroshimodelsEntityLocation.from_dict(_location)

        id = d.pop("id", UNSET)

        consumer_key = d.pop("consumerKey", UNSET)

        desc = d.pop("desc", UNSET)

        otoroshiauth_oauth_1_module_config = cls(
            profile_url=profile_url,
            metadata=metadata,
            authorize_url=authorize_url,
            request_token_url=request_token_url,
            session_cookie_values=session_cookie_values,
            type=type,
            http_method=http_method,
            tags=tags,
            session_max_age=session_max_age,
            consumer_secret=consumer_secret,
            access_token_url=access_token_url,
            name=name,
            rights_override=rights_override,
            callback_url=callback_url,
            location=location,
            id=id,
            consumer_key=consumer_key,
            desc=desc,
        )

        otoroshiauth_oauth_1_module_config.additional_properties = d
        return otoroshiauth_oauth_1_module_config

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
