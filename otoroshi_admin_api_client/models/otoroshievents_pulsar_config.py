from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.null import Null
from ..models.otoroshievents_pulsar_config_type import OtoroshieventsPulsarConfigType
from ..models.otoroshiutilshttp_mtls_config import OtoroshiutilshttpMtlsConfig
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshieventsPulsarConfig")


@attr.s(auto_attribs=True)
class OtoroshieventsPulsarConfig:
    """Settings for connection to a pulsar cluster"""

    mtls_config: Union[Unset, OtoroshiutilshttpMtlsConfig] = UNSET
    tls_trust_certs_file_path: Union[Null, Unset, str] = UNSET
    namespace: Union[Unset, str] = UNSET
    topic: Union[Unset, str] = UNSET
    type: Union[Unset, OtoroshieventsPulsarConfigType] = UNSET
    uri: Union[Unset, str] = UNSET
    tenant: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mtls_config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mtls_config, Unset):
            mtls_config = self.mtls_config.to_dict()

        tls_trust_certs_file_path: Union[Dict[str, Any], Unset, str]
        if isinstance(self.tls_trust_certs_file_path, Unset):
            tls_trust_certs_file_path = UNSET
        elif isinstance(self.tls_trust_certs_file_path, Null):
            tls_trust_certs_file_path = UNSET
            if not isinstance(self.tls_trust_certs_file_path, Unset):
                tls_trust_certs_file_path = self.tls_trust_certs_file_path.to_dict()

        else:
            tls_trust_certs_file_path = self.tls_trust_certs_file_path

        namespace = self.namespace
        topic = self.topic
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        uri = self.uri
        tenant = self.tenant

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mtls_config is not UNSET:
            field_dict["mtlsConfig"] = mtls_config
        if tls_trust_certs_file_path is not UNSET:
            field_dict["tlsTrustCertsFilePath"] = tls_trust_certs_file_path
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if topic is not UNSET:
            field_dict["topic"] = topic
        if type is not UNSET:
            field_dict["type"] = type
        if uri is not UNSET:
            field_dict["uri"] = uri
        if tenant is not UNSET:
            field_dict["tenant"] = tenant

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _mtls_config = d.pop("mtlsConfig", UNSET)
        mtls_config: Union[Unset, OtoroshiutilshttpMtlsConfig]
        if isinstance(_mtls_config, Unset):
            mtls_config = UNSET
        else:
            mtls_config = OtoroshiutilshttpMtlsConfig.from_dict(_mtls_config)

        def _parse_tls_trust_certs_file_path(data: object) -> Union[Null, Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _tls_trust_certs_file_path_type_0 = data
                tls_trust_certs_file_path_type_0: Union[Unset, Null]
                if isinstance(_tls_trust_certs_file_path_type_0, Unset):
                    tls_trust_certs_file_path_type_0 = UNSET
                else:
                    tls_trust_certs_file_path_type_0 = Null.from_dict(_tls_trust_certs_file_path_type_0)

                return tls_trust_certs_file_path_type_0
            except:  # noqa: E722
                pass
            return cast(Union[Null, Unset, str], data)

        tls_trust_certs_file_path = _parse_tls_trust_certs_file_path(d.pop("tlsTrustCertsFilePath", UNSET))

        namespace = d.pop("namespace", UNSET)

        topic = d.pop("topic", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, OtoroshieventsPulsarConfigType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = OtoroshieventsPulsarConfigType(_type)

        uri = d.pop("uri", UNSET)

        tenant = d.pop("tenant", UNSET)

        otoroshievents_pulsar_config = cls(
            mtls_config=mtls_config,
            tls_trust_certs_file_path=tls_trust_certs_file_path,
            namespace=namespace,
            topic=topic,
            type=type,
            uri=uri,
            tenant=tenant,
        )

        otoroshievents_pulsar_config.additional_properties = d
        return otoroshievents_pulsar_config

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
