from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.null import Null
from ..models.otoroshimodels_elastic_analytics_config_headers import OtoroshimodelsElasticAnalyticsConfigHeaders
from ..models.otoroshimodels_elastic_analytics_config_type import OtoroshimodelsElasticAnalyticsConfigType
from ..models.otoroshiutilshttp_mtls_config import OtoroshiutilshttpMtlsConfig
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshimodelsElasticAnalyticsConfig")


@attr.s(auto_attribs=True)
class OtoroshimodelsElasticAnalyticsConfig:
    """Settings for connection to an elastic cluster"""

    cluster_uri: Union[Unset, str] = UNSET
    headers: Union[Unset, OtoroshimodelsElasticAnalyticsConfigHeaders] = UNSET
    password: Union[Null, Unset, str] = UNSET
    mtls_config: Union[Unset, OtoroshiutilshttpMtlsConfig] = UNSET
    index: Union[Null, Unset, str] = UNSET
    type: Union[Unset, OtoroshimodelsElasticAnalyticsConfigType] = UNSET
    user: Union[Null, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cluster_uri = self.cluster_uri
        headers: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        password: Union[Dict[str, Any], Unset, str]
        if isinstance(self.password, Unset):
            password = UNSET
        elif isinstance(self.password, Null):
            password = UNSET
            if not isinstance(self.password, Unset):
                password = self.password.to_dict()

        else:
            password = self.password

        mtls_config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mtls_config, Unset):
            mtls_config = self.mtls_config.to_dict()

        index: Union[Dict[str, Any], Unset, str]
        if isinstance(self.index, Unset):
            index = UNSET
        elif isinstance(self.index, Null):
            index = UNSET
            if not isinstance(self.index, Unset):
                index = self.index.to_dict()

        else:
            index = self.index

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        user: Union[Dict[str, Any], Unset, str]
        if isinstance(self.user, Unset):
            user = UNSET
        elif isinstance(self.user, Null):
            user = UNSET
            if not isinstance(self.user, Unset):
                user = self.user.to_dict()

        else:
            user = self.user

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cluster_uri is not UNSET:
            field_dict["clusterUri"] = cluster_uri
        if headers is not UNSET:
            field_dict["headers"] = headers
        if password is not UNSET:
            field_dict["password"] = password
        if mtls_config is not UNSET:
            field_dict["mtlsConfig"] = mtls_config
        if index is not UNSET:
            field_dict["index"] = index
        if type is not UNSET:
            field_dict["type"] = type
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cluster_uri = d.pop("clusterUri", UNSET)

        _headers = d.pop("headers", UNSET)
        headers: Union[Unset, OtoroshimodelsElasticAnalyticsConfigHeaders]
        if isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = OtoroshimodelsElasticAnalyticsConfigHeaders.from_dict(_headers)

        def _parse_password(data: object) -> Union[Null, Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _password_type_0 = data
                password_type_0: Union[Unset, Null]
                if isinstance(_password_type_0, Unset):
                    password_type_0 = UNSET
                else:
                    password_type_0 = Null.from_dict(_password_type_0)

                return password_type_0
            except:  # noqa: E722
                pass
            return cast(Union[Null, Unset, str], data)

        password = _parse_password(d.pop("password", UNSET))

        _mtls_config = d.pop("mtlsConfig", UNSET)
        mtls_config: Union[Unset, OtoroshiutilshttpMtlsConfig]
        if isinstance(_mtls_config, Unset):
            mtls_config = UNSET
        else:
            mtls_config = OtoroshiutilshttpMtlsConfig.from_dict(_mtls_config)

        def _parse_index(data: object) -> Union[Null, Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _index_type_0 = data
                index_type_0: Union[Unset, Null]
                if isinstance(_index_type_0, Unset):
                    index_type_0 = UNSET
                else:
                    index_type_0 = Null.from_dict(_index_type_0)

                return index_type_0
            except:  # noqa: E722
                pass
            return cast(Union[Null, Unset, str], data)

        index = _parse_index(d.pop("index", UNSET))

        _type = d.pop("type", UNSET)
        type: Union[Unset, OtoroshimodelsElasticAnalyticsConfigType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = OtoroshimodelsElasticAnalyticsConfigType(_type)

        def _parse_user(data: object) -> Union[Null, Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _user_type_0 = data
                user_type_0: Union[Unset, Null]
                if isinstance(_user_type_0, Unset):
                    user_type_0 = UNSET
                else:
                    user_type_0 = Null.from_dict(_user_type_0)

                return user_type_0
            except:  # noqa: E722
                pass
            return cast(Union[Null, Unset, str], data)

        user = _parse_user(d.pop("user", UNSET))

        otoroshimodels_elastic_analytics_config = cls(
            cluster_uri=cluster_uri,
            headers=headers,
            password=password,
            mtls_config=mtls_config,
            index=index,
            type=type,
            user=user,
        )

        otoroshimodels_elastic_analytics_config.additional_properties = d
        return otoroshimodels_elastic_analytics_config

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
