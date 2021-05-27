from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.otoroshimodels_back_office_user_metadata import OtoroshimodelsBackOfficeUserMetadata
from ..models.otoroshimodels_back_office_user_profile import OtoroshimodelsBackOfficeUserProfile
from ..models.otoroshimodels_back_office_user_token import OtoroshimodelsBackOfficeUserToken
from ..models.otoroshimodels_entity_location import OtoroshimodelsEntityLocation
from ..models.otoroshimodels_user_rights import OtoroshimodelsUserRights
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshimodelsBackOfficeUser")


@attr.s(auto_attribs=True)
class OtoroshimodelsBackOfficeUser:
    """User session for otoroshi-ui admins"""

    random_id: Union[Unset, str] = UNSET
    profile: Union[Unset, OtoroshimodelsBackOfficeUserProfile] = UNSET
    auth_config_id: Union[Unset, str] = UNSET
    rights: Union[Unset, OtoroshimodelsUserRights] = UNSET
    created_at: Union[Unset, float] = UNSET
    token: Union[Unset, OtoroshimodelsBackOfficeUserToken] = UNSET
    name: Union[Unset, str] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    metadata: Union[Unset, OtoroshimodelsBackOfficeUserMetadata] = UNSET
    email: Union[Unset, str] = UNSET
    simple_login: Union[Unset, bool] = UNSET
    expired_at: Union[Unset, float] = UNSET
    location: Union[Unset, OtoroshimodelsEntityLocation] = UNSET
    last_refresh: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        random_id = self.random_id
        profile: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.profile, Unset):
            profile = self.profile.to_dict()

        auth_config_id = self.auth_config_id
        rights: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.rights, Unset):
            rights = self.rights.to_dict()

        created_at = self.created_at
        token: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.token, Unset):
            token = self.token.to_dict()

        name = self.name
        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        email = self.email
        simple_login = self.simple_login
        expired_at = self.expired_at
        location: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict()

        last_refresh = self.last_refresh

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if random_id is not UNSET:
            field_dict["randomId"] = random_id
        if profile is not UNSET:
            field_dict["profile"] = profile
        if auth_config_id is not UNSET:
            field_dict["authConfigId"] = auth_config_id
        if rights is not UNSET:
            field_dict["rights"] = rights
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if token is not UNSET:
            field_dict["token"] = token
        if name is not UNSET:
            field_dict["name"] = name
        if tags is not UNSET:
            field_dict["tags"] = tags
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if email is not UNSET:
            field_dict["email"] = email
        if simple_login is not UNSET:
            field_dict["simpleLogin"] = simple_login
        if expired_at is not UNSET:
            field_dict["expiredAt"] = expired_at
        if location is not UNSET:
            field_dict["location"] = location
        if last_refresh is not UNSET:
            field_dict["lastRefresh"] = last_refresh

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        random_id = d.pop("randomId", UNSET)

        _profile = d.pop("profile", UNSET)
        profile: Union[Unset, OtoroshimodelsBackOfficeUserProfile]
        if isinstance(_profile, Unset):
            profile = UNSET
        else:
            profile = OtoroshimodelsBackOfficeUserProfile.from_dict(_profile)

        auth_config_id = d.pop("authConfigId", UNSET)

        _rights = d.pop("rights", UNSET)
        rights: Union[Unset, OtoroshimodelsUserRights]
        if isinstance(_rights, Unset):
            rights = UNSET
        else:
            rights = OtoroshimodelsUserRights.from_dict(_rights)

        created_at = d.pop("createdAt", UNSET)

        _token = d.pop("token", UNSET)
        token: Union[Unset, OtoroshimodelsBackOfficeUserToken]
        if isinstance(_token, Unset):
            token = UNSET
        else:
            token = OtoroshimodelsBackOfficeUserToken.from_dict(_token)

        name = d.pop("name", UNSET)

        tags = cast(List[str], d.pop("tags", UNSET))

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, OtoroshimodelsBackOfficeUserMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = OtoroshimodelsBackOfficeUserMetadata.from_dict(_metadata)

        email = d.pop("email", UNSET)

        simple_login = d.pop("simpleLogin", UNSET)

        expired_at = d.pop("expiredAt", UNSET)

        _location = d.pop("location", UNSET)
        location: Union[Unset, OtoroshimodelsEntityLocation]
        if isinstance(_location, Unset):
            location = UNSET
        else:
            location = OtoroshimodelsEntityLocation.from_dict(_location)

        last_refresh = d.pop("lastRefresh", UNSET)

        otoroshimodels_back_office_user = cls(
            random_id=random_id,
            profile=profile,
            auth_config_id=auth_config_id,
            rights=rights,
            created_at=created_at,
            token=token,
            name=name,
            tags=tags,
            metadata=metadata,
            email=email,
            simple_login=simple_login,
            expired_at=expired_at,
            location=location,
            last_refresh=last_refresh,
        )

        otoroshimodels_back_office_user.additional_properties = d
        return otoroshimodels_back_office_user

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
