from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.null import Null
from ..models.otoroshiauth_generic_oauth_2_module_config_data_override import (
    OtoroshiauthGenericOauth2ModuleConfigDataOverride,
)
from ..models.otoroshiauth_generic_oauth_2_module_config_extra_metadata import (
    OtoroshiauthGenericOauth2ModuleConfigExtraMetadata,
)
from ..models.otoroshiauth_generic_oauth_2_module_config_metadata import OtoroshiauthGenericOauth2ModuleConfigMetadata
from ..models.otoroshiauth_generic_oauth_2_module_config_rights_override import (
    OtoroshiauthGenericOauth2ModuleConfigRightsOverride,
)
from ..models.otoroshiauth_generic_oauth_2_module_config_type import OtoroshiauthGenericOauth2ModuleConfigType
from ..models.otoroshiauth_session_cookie_values import OtoroshiauthSessionCookieValues
from ..models.otoroshimodels_entity_location import OtoroshimodelsEntityLocation
from ..models.otoroshimodels_es_algo_settings import OtoroshimodelsESAlgoSettings
from ..models.otoroshimodels_eskp_algo_settings import OtoroshimodelsESKPAlgoSettings
from ..models.otoroshimodels_hs_algo_settings import OtoroshimodelsHSAlgoSettings
from ..models.otoroshimodels_jwks_algo_settings import OtoroshimodelsJWKSAlgoSettings
from ..models.otoroshimodels_kid_algo_settings import OtoroshimodelsKidAlgoSettings
from ..models.otoroshimodels_rs_algo_settings import OtoroshimodelsRSAlgoSettings
from ..models.otoroshimodels_rsakp_algo_settings import OtoroshimodelsRSAKPAlgoSettings
from ..models.otoroshiutilshttp_mtls_config import OtoroshiutilshttpMtlsConfig
from ..models.playapilibsws_ws_proxy_server import PlayapilibswsWSProxyServer
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshiauthGenericOauth2ModuleConfig")


@attr.s(auto_attribs=True)
class OtoroshiauthGenericOauth2ModuleConfig:
    """Authentication module that works with OAuth2/OIDC"""

    refresh_tokens: Union[Unset, bool] = UNSET
    metadata: Union[Unset, OtoroshiauthGenericOauth2ModuleConfigMetadata] = UNSET
    token_url: Union[Unset, str] = UNSET
    mtls_config: Union[Unset, OtoroshiutilshttpMtlsConfig] = UNSET
    name_field: Union[Unset, str] = UNSET
    email_field: Union[Unset, str] = UNSET
    type: Union[Unset, OtoroshiauthGenericOauth2ModuleConfigType] = UNSET
    introspection_url: Union[Unset, str] = UNSET
    login_url: Union[Unset, str] = UNSET
    scope: Union[Unset, str] = UNSET
    rights_override: Union[Unset, OtoroshiauthGenericOauth2ModuleConfigRightsOverride] = UNSET
    callback_url: Union[Unset, str] = UNSET
    client_secret: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    extra_metadata: Union[Unset, OtoroshiauthGenericOauth2ModuleConfigExtraMetadata] = UNSET
    access_token_field: Union[Unset, str] = UNSET
    user_info_url: Union[Unset, str] = UNSET
    client_id: Union[Unset, str] = UNSET
    use_cookie: Union[Unset, bool] = UNSET
    authorize_url: Union[Unset, str] = UNSET
    session_cookie_values: Union[Unset, OtoroshiauthSessionCookieValues] = UNSET
    data_override: Union[Unset, OtoroshiauthGenericOauth2ModuleConfigDataOverride] = UNSET
    super_admins: Union[Unset, bool] = UNSET
    api_key_meta_field: Union[Unset, str] = UNSET
    use_json: Union[Unset, bool] = UNSET
    api_key_tags_field: Union[Unset, str] = UNSET
    otoroshi_data_field: Union[Unset, str] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    jwt_verifier: Union[
        Null,
        Union[
            Null,
            Union[
                OtoroshimodelsESAlgoSettings,
                OtoroshimodelsESKPAlgoSettings,
                OtoroshimodelsHSAlgoSettings,
                OtoroshimodelsJWKSAlgoSettings,
                OtoroshimodelsKidAlgoSettings,
                OtoroshimodelsRSAKPAlgoSettings,
                OtoroshimodelsRSAlgoSettings,
            ],
        ],
        Unset,
    ] = UNSET
    session_max_age: Union[Unset, int] = UNSET
    proxy: Union[Null, Union[Null, PlayapilibswsWSProxyServer], Unset] = UNSET
    logout_url: Union[Unset, str] = UNSET
    oid_config: Union[Null, Unset, str] = UNSET
    read_profile_from_token: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    claims: Union[Unset, str] = UNSET
    location: Union[Unset, OtoroshimodelsEntityLocation] = UNSET
    desc: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        refresh_tokens = self.refresh_tokens
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        token_url = self.token_url
        mtls_config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mtls_config, Unset):
            mtls_config = self.mtls_config.to_dict()

        name_field = self.name_field
        email_field = self.email_field
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        introspection_url = self.introspection_url
        login_url = self.login_url
        scope = self.scope
        rights_override: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.rights_override, Unset):
            rights_override = self.rights_override.to_dict()

        callback_url = self.callback_url
        client_secret = self.client_secret
        id = self.id
        extra_metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.extra_metadata, Unset):
            extra_metadata = self.extra_metadata.to_dict()

        access_token_field = self.access_token_field
        user_info_url = self.user_info_url
        client_id = self.client_id
        use_cookie = self.use_cookie
        authorize_url = self.authorize_url
        session_cookie_values: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.session_cookie_values, Unset):
            session_cookie_values = self.session_cookie_values.to_dict()

        data_override: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data_override, Unset):
            data_override = self.data_override.to_dict()

        super_admins = self.super_admins
        api_key_meta_field = self.api_key_meta_field
        use_json = self.use_json
        api_key_tags_field = self.api_key_tags_field
        otoroshi_data_field = self.otoroshi_data_field
        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        jwt_verifier: Union[Dict[str, Any], Unset]
        if isinstance(self.jwt_verifier, Unset):
            jwt_verifier = UNSET
        elif isinstance(self.jwt_verifier, Null):
            jwt_verifier = UNSET
            if not isinstance(self.jwt_verifier, Unset):
                jwt_verifier = self.jwt_verifier.to_dict()

        else:
            jwt_verifier
            if isinstance(self.jwt_verifier, Unset):
                jwt_verifier = UNSET
            elif isinstance(self.jwt_verifier, Null):
                jwt_verifier = UNSET
                if not isinstance(self.jwt_verifier, Unset):
                    jwt_verifier = self.jwt_verifier.to_dict()

            else:
                jwt_verifier
                if isinstance(self.jwt_verifier, Unset):
                    jwt_verifier = UNSET
                elif isinstance(self.jwt_verifier, OtoroshimodelsESAlgoSettings):
                    jwt_verifier = self.jwt_verifier.to_dict()

                elif isinstance(self.jwt_verifier, OtoroshimodelsESKPAlgoSettings):
                    jwt_verifier = self.jwt_verifier.to_dict()

                elif isinstance(self.jwt_verifier, OtoroshimodelsHSAlgoSettings):
                    jwt_verifier = self.jwt_verifier.to_dict()

                elif isinstance(self.jwt_verifier, OtoroshimodelsJWKSAlgoSettings):
                    jwt_verifier = self.jwt_verifier.to_dict()

                elif isinstance(self.jwt_verifier, OtoroshimodelsKidAlgoSettings):
                    jwt_verifier = self.jwt_verifier.to_dict()

                elif isinstance(self.jwt_verifier, OtoroshimodelsRSAKPAlgoSettings):
                    jwt_verifier = self.jwt_verifier.to_dict()

                else:
                    jwt_verifier = self.jwt_verifier.to_dict()

        session_max_age = self.session_max_age
        proxy: Union[Dict[str, Any], Unset]
        if isinstance(self.proxy, Unset):
            proxy = UNSET
        elif isinstance(self.proxy, Null):
            proxy = UNSET
            if not isinstance(self.proxy, Unset):
                proxy = self.proxy.to_dict()

        else:
            proxy
            if isinstance(self.proxy, Unset):
                proxy = UNSET
            elif isinstance(self.proxy, Null):
                proxy = UNSET
                if not isinstance(self.proxy, Unset):
                    proxy = self.proxy.to_dict()

            else:
                proxy = UNSET
                if not isinstance(self.proxy, Unset):
                    proxy = self.proxy.to_dict()

        logout_url = self.logout_url
        oid_config: Union[Dict[str, Any], Unset, str]
        if isinstance(self.oid_config, Unset):
            oid_config = UNSET
        elif isinstance(self.oid_config, Null):
            oid_config = UNSET
            if not isinstance(self.oid_config, Unset):
                oid_config = self.oid_config.to_dict()

        else:
            oid_config = self.oid_config

        read_profile_from_token = self.read_profile_from_token
        name = self.name
        claims = self.claims
        location: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict()

        desc = self.desc

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if refresh_tokens is not UNSET:
            field_dict["refreshTokens"] = refresh_tokens
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if token_url is not UNSET:
            field_dict["tokenUrl"] = token_url
        if mtls_config is not UNSET:
            field_dict["mtlsConfig"] = mtls_config
        if name_field is not UNSET:
            field_dict["nameField"] = name_field
        if email_field is not UNSET:
            field_dict["emailField"] = email_field
        if type is not UNSET:
            field_dict["type"] = type
        if introspection_url is not UNSET:
            field_dict["introspectionUrl"] = introspection_url
        if login_url is not UNSET:
            field_dict["loginUrl"] = login_url
        if scope is not UNSET:
            field_dict["scope"] = scope
        if rights_override is not UNSET:
            field_dict["rightsOverride"] = rights_override
        if callback_url is not UNSET:
            field_dict["callbackUrl"] = callback_url
        if client_secret is not UNSET:
            field_dict["clientSecret"] = client_secret
        if id is not UNSET:
            field_dict["id"] = id
        if extra_metadata is not UNSET:
            field_dict["extraMetadata"] = extra_metadata
        if access_token_field is not UNSET:
            field_dict["accessTokenField"] = access_token_field
        if user_info_url is not UNSET:
            field_dict["userInfoUrl"] = user_info_url
        if client_id is not UNSET:
            field_dict["clientId"] = client_id
        if use_cookie is not UNSET:
            field_dict["useCookie"] = use_cookie
        if authorize_url is not UNSET:
            field_dict["authorizeUrl"] = authorize_url
        if session_cookie_values is not UNSET:
            field_dict["sessionCookieValues"] = session_cookie_values
        if data_override is not UNSET:
            field_dict["dataOverride"] = data_override
        if super_admins is not UNSET:
            field_dict["superAdmins"] = super_admins
        if api_key_meta_field is not UNSET:
            field_dict["apiKeyMetaField"] = api_key_meta_field
        if use_json is not UNSET:
            field_dict["useJson"] = use_json
        if api_key_tags_field is not UNSET:
            field_dict["apiKeyTagsField"] = api_key_tags_field
        if otoroshi_data_field is not UNSET:
            field_dict["otoroshiDataField"] = otoroshi_data_field
        if tags is not UNSET:
            field_dict["tags"] = tags
        if jwt_verifier is not UNSET:
            field_dict["jwtVerifier"] = jwt_verifier
        if session_max_age is not UNSET:
            field_dict["sessionMaxAge"] = session_max_age
        if proxy is not UNSET:
            field_dict["proxy"] = proxy
        if logout_url is not UNSET:
            field_dict["logoutUrl"] = logout_url
        if oid_config is not UNSET:
            field_dict["oidConfig"] = oid_config
        if read_profile_from_token is not UNSET:
            field_dict["readProfileFromToken"] = read_profile_from_token
        if name is not UNSET:
            field_dict["name"] = name
        if claims is not UNSET:
            field_dict["claims"] = claims
        if location is not UNSET:
            field_dict["location"] = location
        if desc is not UNSET:
            field_dict["desc"] = desc

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        refresh_tokens = d.pop("refreshTokens", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, OtoroshiauthGenericOauth2ModuleConfigMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = OtoroshiauthGenericOauth2ModuleConfigMetadata.from_dict(_metadata)

        token_url = d.pop("tokenUrl", UNSET)

        _mtls_config = d.pop("mtlsConfig", UNSET)
        mtls_config: Union[Unset, OtoroshiutilshttpMtlsConfig]
        if isinstance(_mtls_config, Unset):
            mtls_config = UNSET
        else:
            mtls_config = OtoroshiutilshttpMtlsConfig.from_dict(_mtls_config)

        name_field = d.pop("nameField", UNSET)

        email_field = d.pop("emailField", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, OtoroshiauthGenericOauth2ModuleConfigType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = OtoroshiauthGenericOauth2ModuleConfigType(_type)

        introspection_url = d.pop("introspectionUrl", UNSET)

        login_url = d.pop("loginUrl", UNSET)

        scope = d.pop("scope", UNSET)

        _rights_override = d.pop("rightsOverride", UNSET)
        rights_override: Union[Unset, OtoroshiauthGenericOauth2ModuleConfigRightsOverride]
        if isinstance(_rights_override, Unset):
            rights_override = UNSET
        else:
            rights_override = OtoroshiauthGenericOauth2ModuleConfigRightsOverride.from_dict(_rights_override)

        callback_url = d.pop("callbackUrl", UNSET)

        client_secret = d.pop("clientSecret", UNSET)

        id = d.pop("id", UNSET)

        _extra_metadata = d.pop("extraMetadata", UNSET)
        extra_metadata: Union[Unset, OtoroshiauthGenericOauth2ModuleConfigExtraMetadata]
        if isinstance(_extra_metadata, Unset):
            extra_metadata = UNSET
        else:
            extra_metadata = OtoroshiauthGenericOauth2ModuleConfigExtraMetadata.from_dict(_extra_metadata)

        access_token_field = d.pop("accessTokenField", UNSET)

        user_info_url = d.pop("userInfoUrl", UNSET)

        client_id = d.pop("clientId", UNSET)

        use_cookie = d.pop("useCookie", UNSET)

        authorize_url = d.pop("authorizeUrl", UNSET)

        _session_cookie_values = d.pop("sessionCookieValues", UNSET)
        session_cookie_values: Union[Unset, OtoroshiauthSessionCookieValues]
        if isinstance(_session_cookie_values, Unset):
            session_cookie_values = UNSET
        else:
            session_cookie_values = OtoroshiauthSessionCookieValues.from_dict(_session_cookie_values)

        _data_override = d.pop("dataOverride", UNSET)
        data_override: Union[Unset, OtoroshiauthGenericOauth2ModuleConfigDataOverride]
        if isinstance(_data_override, Unset):
            data_override = UNSET
        else:
            data_override = OtoroshiauthGenericOauth2ModuleConfigDataOverride.from_dict(_data_override)

        super_admins = d.pop("superAdmins", UNSET)

        api_key_meta_field = d.pop("apiKeyMetaField", UNSET)

        use_json = d.pop("useJson", UNSET)

        api_key_tags_field = d.pop("apiKeyTagsField", UNSET)

        otoroshi_data_field = d.pop("otoroshiDataField", UNSET)

        tags = cast(List[str], d.pop("tags", UNSET))

        def _parse_jwt_verifier(
            data: object,
        ) -> Union[
            Null,
            Union[
                Null,
                Union[
                    OtoroshimodelsESAlgoSettings,
                    OtoroshimodelsESKPAlgoSettings,
                    OtoroshimodelsHSAlgoSettings,
                    OtoroshimodelsJWKSAlgoSettings,
                    OtoroshimodelsKidAlgoSettings,
                    OtoroshimodelsRSAKPAlgoSettings,
                    OtoroshimodelsRSAlgoSettings,
                ],
            ],
            Unset,
        ]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _jwt_verifier_type_0 = data
                jwt_verifier_type_0: Union[Unset, Null]
                if isinstance(_jwt_verifier_type_0, Unset):
                    jwt_verifier_type_0 = UNSET
                else:
                    jwt_verifier_type_0 = Null.from_dict(_jwt_verifier_type_0)

                return jwt_verifier_type_0
            except:  # noqa: E722
                pass
            if not True:
                raise TypeError()

            def _parse_jwt_verifier_type_1(
                data: object,
            ) -> Union[
                Null,
                Union[
                    OtoroshimodelsESAlgoSettings,
                    OtoroshimodelsESKPAlgoSettings,
                    OtoroshimodelsHSAlgoSettings,
                    OtoroshimodelsJWKSAlgoSettings,
                    OtoroshimodelsKidAlgoSettings,
                    OtoroshimodelsRSAKPAlgoSettings,
                    OtoroshimodelsRSAlgoSettings,
                ],
                Unset,
            ]:
                if isinstance(data, Unset):
                    return data
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    _jwt_verifier_type_1_type_0 = data
                    jwt_verifier_type_1_type_0: Union[Unset, Null]
                    if isinstance(_jwt_verifier_type_1_type_0, Unset):
                        jwt_verifier_type_1_type_0 = UNSET
                    else:
                        jwt_verifier_type_1_type_0 = Null.from_dict(_jwt_verifier_type_1_type_0)

                    return jwt_verifier_type_1_type_0
                except:  # noqa: E722
                    pass
                if not True:
                    raise TypeError()

                def _parse_jwt_verifier_type_1_type_1(
                    data: object,
                ) -> Union[
                    OtoroshimodelsESAlgoSettings,
                    OtoroshimodelsESKPAlgoSettings,
                    OtoroshimodelsHSAlgoSettings,
                    OtoroshimodelsJWKSAlgoSettings,
                    OtoroshimodelsKidAlgoSettings,
                    OtoroshimodelsRSAKPAlgoSettings,
                    OtoroshimodelsRSAlgoSettings,
                    Unset,
                ]:
                    if isinstance(data, Unset):
                        return data
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemasotoroshimodels_algo_settings_type_0 = OtoroshimodelsESAlgoSettings.from_dict(
                            data
                        )

                        return componentsschemasotoroshimodels_algo_settings_type_0
                    except:  # noqa: E722
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemasotoroshimodels_algo_settings_type_1 = OtoroshimodelsESKPAlgoSettings.from_dict(
                            data
                        )

                        return componentsschemasotoroshimodels_algo_settings_type_1
                    except:  # noqa: E722
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemasotoroshimodels_algo_settings_type_2 = OtoroshimodelsHSAlgoSettings.from_dict(
                            data
                        )

                        return componentsschemasotoroshimodels_algo_settings_type_2
                    except:  # noqa: E722
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemasotoroshimodels_algo_settings_type_3 = OtoroshimodelsJWKSAlgoSettings.from_dict(
                            data
                        )

                        return componentsschemasotoroshimodels_algo_settings_type_3
                    except:  # noqa: E722
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemasotoroshimodels_algo_settings_type_4 = OtoroshimodelsKidAlgoSettings.from_dict(
                            data
                        )

                        return componentsschemasotoroshimodels_algo_settings_type_4
                    except:  # noqa: E722
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemasotoroshimodels_algo_settings_type_5 = (
                            OtoroshimodelsRSAKPAlgoSettings.from_dict(data)
                        )

                        return componentsschemasotoroshimodels_algo_settings_type_5
                    except:  # noqa: E722
                        pass
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemasotoroshimodels_algo_settings_type_6 = OtoroshimodelsRSAlgoSettings.from_dict(data)

                    return componentsschemasotoroshimodels_algo_settings_type_6

                jwt_verifier_type_1_type_1 = _parse_jwt_verifier_type_1_type_1(data)

                return jwt_verifier_type_1_type_1

            jwt_verifier_type_1 = _parse_jwt_verifier_type_1(data)

            return jwt_verifier_type_1

        jwt_verifier = _parse_jwt_verifier(d.pop("jwtVerifier", UNSET))

        session_max_age = d.pop("sessionMaxAge", UNSET)

        def _parse_proxy(data: object) -> Union[Null, Union[Null, PlayapilibswsWSProxyServer], Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _proxy_type_0 = data
                proxy_type_0: Union[Unset, Null]
                if isinstance(_proxy_type_0, Unset):
                    proxy_type_0 = UNSET
                else:
                    proxy_type_0 = Null.from_dict(_proxy_type_0)

                return proxy_type_0
            except:  # noqa: E722
                pass
            if not True:
                raise TypeError()

            def _parse_proxy_type_1(data: object) -> Union[Null, PlayapilibswsWSProxyServer, Unset]:
                if isinstance(data, Unset):
                    return data
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    _proxy_type_1_type_0 = data
                    proxy_type_1_type_0: Union[Unset, Null]
                    if isinstance(_proxy_type_1_type_0, Unset):
                        proxy_type_1_type_0 = UNSET
                    else:
                        proxy_type_1_type_0 = Null.from_dict(_proxy_type_1_type_0)

                    return proxy_type_1_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                _proxy_type_1_type_1 = data
                proxy_type_1_type_1: Union[Unset, PlayapilibswsWSProxyServer]
                if isinstance(_proxy_type_1_type_1, Unset):
                    proxy_type_1_type_1 = UNSET
                else:
                    proxy_type_1_type_1 = PlayapilibswsWSProxyServer.from_dict(_proxy_type_1_type_1)

                return proxy_type_1_type_1

            proxy_type_1 = _parse_proxy_type_1(data)

            return proxy_type_1

        proxy = _parse_proxy(d.pop("proxy", UNSET))

        logout_url = d.pop("logoutUrl", UNSET)

        def _parse_oid_config(data: object) -> Union[Null, Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _oid_config_type_0 = data
                oid_config_type_0: Union[Unset, Null]
                if isinstance(_oid_config_type_0, Unset):
                    oid_config_type_0 = UNSET
                else:
                    oid_config_type_0 = Null.from_dict(_oid_config_type_0)

                return oid_config_type_0
            except:  # noqa: E722
                pass
            return cast(Union[Null, Unset, str], data)

        oid_config = _parse_oid_config(d.pop("oidConfig", UNSET))

        read_profile_from_token = d.pop("readProfileFromToken", UNSET)

        name = d.pop("name", UNSET)

        claims = d.pop("claims", UNSET)

        _location = d.pop("location", UNSET)
        location: Union[Unset, OtoroshimodelsEntityLocation]
        if isinstance(_location, Unset):
            location = UNSET
        else:
            location = OtoroshimodelsEntityLocation.from_dict(_location)

        desc = d.pop("desc", UNSET)

        otoroshiauth_generic_oauth_2_module_config = cls(
            refresh_tokens=refresh_tokens,
            metadata=metadata,
            token_url=token_url,
            mtls_config=mtls_config,
            name_field=name_field,
            email_field=email_field,
            type=type,
            introspection_url=introspection_url,
            login_url=login_url,
            scope=scope,
            rights_override=rights_override,
            callback_url=callback_url,
            client_secret=client_secret,
            id=id,
            extra_metadata=extra_metadata,
            access_token_field=access_token_field,
            user_info_url=user_info_url,
            client_id=client_id,
            use_cookie=use_cookie,
            authorize_url=authorize_url,
            session_cookie_values=session_cookie_values,
            data_override=data_override,
            super_admins=super_admins,
            api_key_meta_field=api_key_meta_field,
            use_json=use_json,
            api_key_tags_field=api_key_tags_field,
            otoroshi_data_field=otoroshi_data_field,
            tags=tags,
            jwt_verifier=jwt_verifier,
            session_max_age=session_max_age,
            proxy=proxy,
            logout_url=logout_url,
            oid_config=oid_config,
            read_profile_from_token=read_profile_from_token,
            name=name,
            claims=claims,
            location=location,
            desc=desc,
        )

        otoroshiauth_generic_oauth_2_module_config.additional_properties = d
        return otoroshiauth_generic_oauth_2_module_config

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
