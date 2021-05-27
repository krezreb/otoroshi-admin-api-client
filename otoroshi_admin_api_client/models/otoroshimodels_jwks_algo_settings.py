from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.null import Null
from ..models.otoroshimodels_jwks_algo_settings_headers import OtoroshimodelsJWKSAlgoSettingsHeaders
from ..models.otoroshimodels_jwks_algo_settings_type import OtoroshimodelsJWKSAlgoSettingsType
from ..models.otoroshiutilshttp_mtls_config import OtoroshiutilshttpMtlsConfig
from ..models.playapilibsws_ws_proxy_server import PlayapilibswsWSProxyServer
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshimodelsJWKSAlgoSettings")


@attr.s(auto_attribs=True)
class OtoroshimodelsJWKSAlgoSettings:
    """Settings to use keypair from JWKS for verification"""

    kty: Union[Unset, str] = UNSET
    proxy: Union[Null, Union[Null, PlayapilibswsWSProxyServer], Unset] = UNSET
    headers: Union[Unset, OtoroshimodelsJWKSAlgoSettingsHeaders] = UNSET
    mtls_config: Union[Unset, OtoroshiutilshttpMtlsConfig] = UNSET
    type: Union[Unset, OtoroshimodelsJWKSAlgoSettingsType] = UNSET
    ttl: Union[Unset, float] = UNSET
    url: Union[Unset, str] = UNSET
    timeout: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        kty = self.kty
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

        headers: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        mtls_config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mtls_config, Unset):
            mtls_config = self.mtls_config.to_dict()

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        ttl = self.ttl
        url = self.url
        timeout = self.timeout

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if kty is not UNSET:
            field_dict["kty"] = kty
        if proxy is not UNSET:
            field_dict["proxy"] = proxy
        if headers is not UNSET:
            field_dict["headers"] = headers
        if mtls_config is not UNSET:
            field_dict["mtlsConfig"] = mtls_config
        if type is not UNSET:
            field_dict["type"] = type
        if ttl is not UNSET:
            field_dict["ttl"] = ttl
        if url is not UNSET:
            field_dict["url"] = url
        if timeout is not UNSET:
            field_dict["timeout"] = timeout

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        kty = d.pop("kty", UNSET)

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

        _headers = d.pop("headers", UNSET)
        headers: Union[Unset, OtoroshimodelsJWKSAlgoSettingsHeaders]
        if isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = OtoroshimodelsJWKSAlgoSettingsHeaders.from_dict(_headers)

        _mtls_config = d.pop("mtlsConfig", UNSET)
        mtls_config: Union[Unset, OtoroshiutilshttpMtlsConfig]
        if isinstance(_mtls_config, Unset):
            mtls_config = UNSET
        else:
            mtls_config = OtoroshiutilshttpMtlsConfig.from_dict(_mtls_config)

        _type = d.pop("type", UNSET)
        type: Union[Unset, OtoroshimodelsJWKSAlgoSettingsType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = OtoroshimodelsJWKSAlgoSettingsType(_type)

        ttl = d.pop("ttl", UNSET)

        url = d.pop("url", UNSET)

        timeout = d.pop("timeout", UNSET)

        otoroshimodels_jwks_algo_settings = cls(
            kty=kty,
            proxy=proxy,
            headers=headers,
            mtls_config=mtls_config,
            type=type,
            ttl=ttl,
            url=url,
            timeout=timeout,
        )

        otoroshimodels_jwks_algo_settings.additional_properties = d
        return otoroshimodels_jwks_algo_settings

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
