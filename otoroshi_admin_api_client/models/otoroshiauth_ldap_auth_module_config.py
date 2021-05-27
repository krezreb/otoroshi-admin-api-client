from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.null import Null
from ..models.otoroshiauth_group_filter import OtoroshiauthGroupFilter
from ..models.otoroshiauth_ldap_auth_module_config_data_override import OtoroshiauthLdapAuthModuleConfigDataOverride
from ..models.otoroshiauth_ldap_auth_module_config_extra_metadata import OtoroshiauthLdapAuthModuleConfigExtraMetadata
from ..models.otoroshiauth_ldap_auth_module_config_group_rights import OtoroshiauthLdapAuthModuleConfigGroupRights
from ..models.otoroshiauth_ldap_auth_module_config_metadata import OtoroshiauthLdapAuthModuleConfigMetadata
from ..models.otoroshiauth_ldap_auth_module_config_rights_override import OtoroshiauthLdapAuthModuleConfigRightsOverride
from ..models.otoroshiauth_ldap_auth_module_config_type import OtoroshiauthLdapAuthModuleConfigType
from ..models.otoroshiauth_session_cookie_values import OtoroshiauthSessionCookieValues
from ..models.otoroshimodels_entity_location import OtoroshimodelsEntityLocation
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshiauthLdapAuthModuleConfig")


@attr.s(auto_attribs=True)
class OtoroshiauthLdapAuthModuleConfig:
    """Authentication module that works with LDAP"""

    group_filters: Union[Unset, List[OtoroshiauthGroupFilter]] = UNSET
    metadata: Union[Unset, OtoroshiauthLdapAuthModuleConfigMetadata] = UNSET
    allow_empty_password: Union[Unset, bool] = UNSET
    basic_auth: Union[Unset, bool] = UNSET
    search_base: Union[Unset, str] = UNSET
    name_field: Union[Unset, str] = UNSET
    email_field: Union[Unset, str] = UNSET
    type: Union[Unset, OtoroshiauthLdapAuthModuleConfigType] = UNSET
    metadata_field: Union[Null, Unset, str] = UNSET
    rights_override: Union[Unset, OtoroshiauthLdapAuthModuleConfigRightsOverride] = UNSET
    group_rights: Union[Unset, OtoroshiauthLdapAuthModuleConfigGroupRights] = UNSET
    id: Union[Unset, str] = UNSET
    extra_metadata: Union[Unset, OtoroshiauthLdapAuthModuleConfigExtraMetadata] = UNSET
    search_filter: Union[Unset, str] = UNSET
    admin_password: Union[Null, Unset, str] = UNSET
    session_cookie_values: Union[Unset, OtoroshiauthSessionCookieValues] = UNSET
    data_override: Union[Unset, OtoroshiauthLdapAuthModuleConfigDataOverride] = UNSET
    super_admins: Union[Unset, bool] = UNSET
    user_base: Union[Null, Unset, str] = UNSET
    server_urls: Union[Unset, List[str]] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    session_max_age: Union[Unset, int] = UNSET
    admin_username: Union[Null, Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    location: Union[Unset, OtoroshimodelsEntityLocation] = UNSET
    desc: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        group_filters: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.group_filters, Unset):
            group_filters = []
            for group_filters_item_data in self.group_filters:
                group_filters_item = group_filters_item_data.to_dict()

                group_filters.append(group_filters_item)

        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        allow_empty_password = self.allow_empty_password
        basic_auth = self.basic_auth
        search_base = self.search_base
        name_field = self.name_field
        email_field = self.email_field
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        metadata_field: Union[Dict[str, Any], Unset, str]
        if isinstance(self.metadata_field, Unset):
            metadata_field = UNSET
        elif isinstance(self.metadata_field, Null):
            metadata_field = UNSET
            if not isinstance(self.metadata_field, Unset):
                metadata_field = self.metadata_field.to_dict()

        else:
            metadata_field = self.metadata_field

        rights_override: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.rights_override, Unset):
            rights_override = self.rights_override.to_dict()

        group_rights: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.group_rights, Unset):
            group_rights = self.group_rights.to_dict()

        id = self.id
        extra_metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.extra_metadata, Unset):
            extra_metadata = self.extra_metadata.to_dict()

        search_filter = self.search_filter
        admin_password: Union[Dict[str, Any], Unset, str]
        if isinstance(self.admin_password, Unset):
            admin_password = UNSET
        elif isinstance(self.admin_password, Null):
            admin_password = UNSET
            if not isinstance(self.admin_password, Unset):
                admin_password = self.admin_password.to_dict()

        else:
            admin_password = self.admin_password

        session_cookie_values: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.session_cookie_values, Unset):
            session_cookie_values = self.session_cookie_values.to_dict()

        data_override: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data_override, Unset):
            data_override = self.data_override.to_dict()

        super_admins = self.super_admins
        user_base: Union[Dict[str, Any], Unset, str]
        if isinstance(self.user_base, Unset):
            user_base = UNSET
        elif isinstance(self.user_base, Null):
            user_base = UNSET
            if not isinstance(self.user_base, Unset):
                user_base = self.user_base.to_dict()

        else:
            user_base = self.user_base

        server_urls: Union[Unset, List[str]] = UNSET
        if not isinstance(self.server_urls, Unset):
            server_urls = self.server_urls

        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        session_max_age = self.session_max_age
        admin_username: Union[Dict[str, Any], Unset, str]
        if isinstance(self.admin_username, Unset):
            admin_username = UNSET
        elif isinstance(self.admin_username, Null):
            admin_username = UNSET
            if not isinstance(self.admin_username, Unset):
                admin_username = self.admin_username.to_dict()

        else:
            admin_username = self.admin_username

        name = self.name
        location: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict()

        desc = self.desc

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if group_filters is not UNSET:
            field_dict["groupFilters"] = group_filters
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if allow_empty_password is not UNSET:
            field_dict["allowEmptyPassword"] = allow_empty_password
        if basic_auth is not UNSET:
            field_dict["basicAuth"] = basic_auth
        if search_base is not UNSET:
            field_dict["searchBase"] = search_base
        if name_field is not UNSET:
            field_dict["nameField"] = name_field
        if email_field is not UNSET:
            field_dict["emailField"] = email_field
        if type is not UNSET:
            field_dict["type"] = type
        if metadata_field is not UNSET:
            field_dict["metadataField"] = metadata_field
        if rights_override is not UNSET:
            field_dict["rightsOverride"] = rights_override
        if group_rights is not UNSET:
            field_dict["groupRights"] = group_rights
        if id is not UNSET:
            field_dict["id"] = id
        if extra_metadata is not UNSET:
            field_dict["extraMetadata"] = extra_metadata
        if search_filter is not UNSET:
            field_dict["searchFilter"] = search_filter
        if admin_password is not UNSET:
            field_dict["adminPassword"] = admin_password
        if session_cookie_values is not UNSET:
            field_dict["sessionCookieValues"] = session_cookie_values
        if data_override is not UNSET:
            field_dict["dataOverride"] = data_override
        if super_admins is not UNSET:
            field_dict["superAdmins"] = super_admins
        if user_base is not UNSET:
            field_dict["userBase"] = user_base
        if server_urls is not UNSET:
            field_dict["serverUrls"] = server_urls
        if tags is not UNSET:
            field_dict["tags"] = tags
        if session_max_age is not UNSET:
            field_dict["sessionMaxAge"] = session_max_age
        if admin_username is not UNSET:
            field_dict["adminUsername"] = admin_username
        if name is not UNSET:
            field_dict["name"] = name
        if location is not UNSET:
            field_dict["location"] = location
        if desc is not UNSET:
            field_dict["desc"] = desc

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        group_filters = []
        _group_filters = d.pop("groupFilters", UNSET)
        for group_filters_item_data in _group_filters or []:
            group_filters_item = OtoroshiauthGroupFilter.from_dict(group_filters_item_data)

            group_filters.append(group_filters_item)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, OtoroshiauthLdapAuthModuleConfigMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = OtoroshiauthLdapAuthModuleConfigMetadata.from_dict(_metadata)

        allow_empty_password = d.pop("allowEmptyPassword", UNSET)

        basic_auth = d.pop("basicAuth", UNSET)

        search_base = d.pop("searchBase", UNSET)

        name_field = d.pop("nameField", UNSET)

        email_field = d.pop("emailField", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, OtoroshiauthLdapAuthModuleConfigType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = OtoroshiauthLdapAuthModuleConfigType(_type)

        def _parse_metadata_field(data: object) -> Union[Null, Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _metadata_field_type_0 = data
                metadata_field_type_0: Union[Unset, Null]
                if isinstance(_metadata_field_type_0, Unset):
                    metadata_field_type_0 = UNSET
                else:
                    metadata_field_type_0 = Null.from_dict(_metadata_field_type_0)

                return metadata_field_type_0
            except:  # noqa: E722
                pass
            return cast(Union[Null, Unset, str], data)

        metadata_field = _parse_metadata_field(d.pop("metadataField", UNSET))

        _rights_override = d.pop("rightsOverride", UNSET)
        rights_override: Union[Unset, OtoroshiauthLdapAuthModuleConfigRightsOverride]
        if isinstance(_rights_override, Unset):
            rights_override = UNSET
        else:
            rights_override = OtoroshiauthLdapAuthModuleConfigRightsOverride.from_dict(_rights_override)

        _group_rights = d.pop("groupRights", UNSET)
        group_rights: Union[Unset, OtoroshiauthLdapAuthModuleConfigGroupRights]
        if isinstance(_group_rights, Unset):
            group_rights = UNSET
        else:
            group_rights = OtoroshiauthLdapAuthModuleConfigGroupRights.from_dict(_group_rights)

        id = d.pop("id", UNSET)

        _extra_metadata = d.pop("extraMetadata", UNSET)
        extra_metadata: Union[Unset, OtoroshiauthLdapAuthModuleConfigExtraMetadata]
        if isinstance(_extra_metadata, Unset):
            extra_metadata = UNSET
        else:
            extra_metadata = OtoroshiauthLdapAuthModuleConfigExtraMetadata.from_dict(_extra_metadata)

        search_filter = d.pop("searchFilter", UNSET)

        def _parse_admin_password(data: object) -> Union[Null, Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _admin_password_type_0 = data
                admin_password_type_0: Union[Unset, Null]
                if isinstance(_admin_password_type_0, Unset):
                    admin_password_type_0 = UNSET
                else:
                    admin_password_type_0 = Null.from_dict(_admin_password_type_0)

                return admin_password_type_0
            except:  # noqa: E722
                pass
            return cast(Union[Null, Unset, str], data)

        admin_password = _parse_admin_password(d.pop("adminPassword", UNSET))

        _session_cookie_values = d.pop("sessionCookieValues", UNSET)
        session_cookie_values: Union[Unset, OtoroshiauthSessionCookieValues]
        if isinstance(_session_cookie_values, Unset):
            session_cookie_values = UNSET
        else:
            session_cookie_values = OtoroshiauthSessionCookieValues.from_dict(_session_cookie_values)

        _data_override = d.pop("dataOverride", UNSET)
        data_override: Union[Unset, OtoroshiauthLdapAuthModuleConfigDataOverride]
        if isinstance(_data_override, Unset):
            data_override = UNSET
        else:
            data_override = OtoroshiauthLdapAuthModuleConfigDataOverride.from_dict(_data_override)

        super_admins = d.pop("superAdmins", UNSET)

        def _parse_user_base(data: object) -> Union[Null, Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _user_base_type_0 = data
                user_base_type_0: Union[Unset, Null]
                if isinstance(_user_base_type_0, Unset):
                    user_base_type_0 = UNSET
                else:
                    user_base_type_0 = Null.from_dict(_user_base_type_0)

                return user_base_type_0
            except:  # noqa: E722
                pass
            return cast(Union[Null, Unset, str], data)

        user_base = _parse_user_base(d.pop("userBase", UNSET))

        server_urls = cast(List[str], d.pop("serverUrls", UNSET))

        tags = cast(List[str], d.pop("tags", UNSET))

        session_max_age = d.pop("sessionMaxAge", UNSET)

        def _parse_admin_username(data: object) -> Union[Null, Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _admin_username_type_0 = data
                admin_username_type_0: Union[Unset, Null]
                if isinstance(_admin_username_type_0, Unset):
                    admin_username_type_0 = UNSET
                else:
                    admin_username_type_0 = Null.from_dict(_admin_username_type_0)

                return admin_username_type_0
            except:  # noqa: E722
                pass
            return cast(Union[Null, Unset, str], data)

        admin_username = _parse_admin_username(d.pop("adminUsername", UNSET))

        name = d.pop("name", UNSET)

        _location = d.pop("location", UNSET)
        location: Union[Unset, OtoroshimodelsEntityLocation]
        if isinstance(_location, Unset):
            location = UNSET
        else:
            location = OtoroshimodelsEntityLocation.from_dict(_location)

        desc = d.pop("desc", UNSET)

        otoroshiauth_ldap_auth_module_config = cls(
            group_filters=group_filters,
            metadata=metadata,
            allow_empty_password=allow_empty_password,
            basic_auth=basic_auth,
            search_base=search_base,
            name_field=name_field,
            email_field=email_field,
            type=type,
            metadata_field=metadata_field,
            rights_override=rights_override,
            group_rights=group_rights,
            id=id,
            extra_metadata=extra_metadata,
            search_filter=search_filter,
            admin_password=admin_password,
            session_cookie_values=session_cookie_values,
            data_override=data_override,
            super_admins=super_admins,
            user_base=user_base,
            server_urls=server_urls,
            tags=tags,
            session_max_age=session_max_age,
            admin_username=admin_username,
            name=name,
            location=location,
            desc=desc,
        )

        otoroshiauth_ldap_auth_module_config.additional_properties = d
        return otoroshiauth_ldap_auth_module_config

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
