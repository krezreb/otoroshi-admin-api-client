from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.null import Null
from ..models.otoroshimodels_entity_location import OtoroshimodelsEntityLocation
from ..models.otoroshimodels_private_apps_user_metadata import OtoroshimodelsPrivateAppsUserMetadata
from ..models.otoroshimodels_private_apps_user_otoroshi_data_type_1 import (
    OtoroshimodelsPrivateAppsUserOtoroshiDataType1,
)
from ..models.otoroshimodels_private_apps_user_profile import OtoroshimodelsPrivateAppsUserProfile
from ..models.otoroshimodels_private_apps_user_token import OtoroshimodelsPrivateAppsUserToken
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshimodelsPrivateAppsUser")


@attr.s(auto_attribs=True)
class OtoroshimodelsPrivateAppsUser:
    """User session for private apps"""

    realm: Union[Unset, str] = UNSET
    token: Union[Unset, OtoroshimodelsPrivateAppsUserToken] = UNSET
    expired_at: Union[Unset, float] = UNSET
    profile: Union[Unset, OtoroshimodelsPrivateAppsUserProfile] = UNSET
    last_refresh: Union[Unset, float] = UNSET
    random_id: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    created_at: Union[Unset, float] = UNSET
    location: Union[Unset, OtoroshimodelsEntityLocation] = UNSET
    auth_config_id: Union[Unset, str] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    name: Union[Unset, str] = UNSET
    otoroshi_data: Union[Null, OtoroshimodelsPrivateAppsUserOtoroshiDataType1, Unset] = UNSET
    metadata: Union[Unset, OtoroshimodelsPrivateAppsUserMetadata] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        realm = self.realm
        token: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.token, Unset):
            token = self.token.to_dict()

        expired_at = self.expired_at
        profile: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.profile, Unset):
            profile = self.profile.to_dict()

        last_refresh = self.last_refresh
        random_id = self.random_id
        email = self.email
        created_at = self.created_at
        location: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict()

        auth_config_id = self.auth_config_id
        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        name = self.name
        otoroshi_data: Union[Dict[str, Any], Unset]
        if isinstance(self.otoroshi_data, Unset):
            otoroshi_data = UNSET
        elif isinstance(self.otoroshi_data, Null):
            otoroshi_data = UNSET
            if not isinstance(self.otoroshi_data, Unset):
                otoroshi_data = self.otoroshi_data.to_dict()

        else:
            otoroshi_data = UNSET
            if not isinstance(self.otoroshi_data, Unset):
                otoroshi_data = self.otoroshi_data.to_dict()

        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if realm is not UNSET:
            field_dict["realm"] = realm
        if token is not UNSET:
            field_dict["token"] = token
        if expired_at is not UNSET:
            field_dict["expiredAt"] = expired_at
        if profile is not UNSET:
            field_dict["profile"] = profile
        if last_refresh is not UNSET:
            field_dict["lastRefresh"] = last_refresh
        if random_id is not UNSET:
            field_dict["randomId"] = random_id
        if email is not UNSET:
            field_dict["email"] = email
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if location is not UNSET:
            field_dict["location"] = location
        if auth_config_id is not UNSET:
            field_dict["authConfigId"] = auth_config_id
        if tags is not UNSET:
            field_dict["tags"] = tags
        if name is not UNSET:
            field_dict["name"] = name
        if otoroshi_data is not UNSET:
            field_dict["otoroshiData"] = otoroshi_data
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        realm = d.pop("realm", UNSET)

        _token = d.pop("token", UNSET)
        token: Union[Unset, OtoroshimodelsPrivateAppsUserToken]
        if isinstance(_token, Unset):
            token = UNSET
        else:
            token = OtoroshimodelsPrivateAppsUserToken.from_dict(_token)

        expired_at = d.pop("expiredAt", UNSET)

        _profile = d.pop("profile", UNSET)
        profile: Union[Unset, OtoroshimodelsPrivateAppsUserProfile]
        if isinstance(_profile, Unset):
            profile = UNSET
        else:
            profile = OtoroshimodelsPrivateAppsUserProfile.from_dict(_profile)

        last_refresh = d.pop("lastRefresh", UNSET)

        random_id = d.pop("randomId", UNSET)

        email = d.pop("email", UNSET)

        created_at = d.pop("createdAt", UNSET)

        _location = d.pop("location", UNSET)
        location: Union[Unset, OtoroshimodelsEntityLocation]
        if isinstance(_location, Unset):
            location = UNSET
        else:
            location = OtoroshimodelsEntityLocation.from_dict(_location)

        auth_config_id = d.pop("authConfigId", UNSET)

        tags = cast(List[str], d.pop("tags", UNSET))

        name = d.pop("name", UNSET)

        def _parse_otoroshi_data(data: object) -> Union[Null, OtoroshimodelsPrivateAppsUserOtoroshiDataType1, Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _otoroshi_data_type_0 = data
                otoroshi_data_type_0: Union[Unset, Null]
                if isinstance(_otoroshi_data_type_0, Unset):
                    otoroshi_data_type_0 = UNSET
                else:
                    otoroshi_data_type_0 = Null.from_dict(_otoroshi_data_type_0)

                return otoroshi_data_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            _otoroshi_data_type_1 = data
            otoroshi_data_type_1: Union[Unset, OtoroshimodelsPrivateAppsUserOtoroshiDataType1]
            if isinstance(_otoroshi_data_type_1, Unset):
                otoroshi_data_type_1 = UNSET
            else:
                otoroshi_data_type_1 = OtoroshimodelsPrivateAppsUserOtoroshiDataType1.from_dict(_otoroshi_data_type_1)

            return otoroshi_data_type_1

        otoroshi_data = _parse_otoroshi_data(d.pop("otoroshiData", UNSET))

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, OtoroshimodelsPrivateAppsUserMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = OtoroshimodelsPrivateAppsUserMetadata.from_dict(_metadata)

        otoroshimodels_private_apps_user = cls(
            realm=realm,
            token=token,
            expired_at=expired_at,
            profile=profile,
            last_refresh=last_refresh,
            random_id=random_id,
            email=email,
            created_at=created_at,
            location=location,
            auth_config_id=auth_config_id,
            tags=tags,
            name=name,
            otoroshi_data=otoroshi_data,
            metadata=metadata,
        )

        otoroshimodels_private_apps_user.additional_properties = d
        return otoroshimodels_private_apps_user

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
