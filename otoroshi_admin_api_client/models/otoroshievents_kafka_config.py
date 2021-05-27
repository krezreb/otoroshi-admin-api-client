from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.null import Null
from ..models.otoroshievents_kafka_config_type import OtoroshieventsKafkaConfigType
from ..models.otoroshiutilshttp_mtls_config import OtoroshiutilshttpMtlsConfig
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshieventsKafkaConfig")


@attr.s(auto_attribs=True)
class OtoroshieventsKafkaConfig:
    """Settings for connection to a kafka cluster"""

    servers: Union[Unset, List[str]] = UNSET
    key_pass: Union[Null, Unset, str] = UNSET
    mtls_config: Union[Unset, OtoroshiutilshttpMtlsConfig] = UNSET
    topic: Union[Unset, str] = UNSET
    truststore: Union[Null, Unset, str] = UNSET
    keystore: Union[Null, Unset, str] = UNSET
    send_events: Union[Unset, bool] = UNSET
    type: Union[Unset, OtoroshieventsKafkaConfigType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        servers: Union[Unset, List[str]] = UNSET
        if not isinstance(self.servers, Unset):
            servers = self.servers

        key_pass: Union[Dict[str, Any], Unset, str]
        if isinstance(self.key_pass, Unset):
            key_pass = UNSET
        elif isinstance(self.key_pass, Null):
            key_pass = UNSET
            if not isinstance(self.key_pass, Unset):
                key_pass = self.key_pass.to_dict()

        else:
            key_pass = self.key_pass

        mtls_config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mtls_config, Unset):
            mtls_config = self.mtls_config.to_dict()

        topic = self.topic
        truststore: Union[Dict[str, Any], Unset, str]
        if isinstance(self.truststore, Unset):
            truststore = UNSET
        elif isinstance(self.truststore, Null):
            truststore = UNSET
            if not isinstance(self.truststore, Unset):
                truststore = self.truststore.to_dict()

        else:
            truststore = self.truststore

        keystore: Union[Dict[str, Any], Unset, str]
        if isinstance(self.keystore, Unset):
            keystore = UNSET
        elif isinstance(self.keystore, Null):
            keystore = UNSET
            if not isinstance(self.keystore, Unset):
                keystore = self.keystore.to_dict()

        else:
            keystore = self.keystore

        send_events = self.send_events
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if servers is not UNSET:
            field_dict["servers"] = servers
        if key_pass is not UNSET:
            field_dict["keyPass"] = key_pass
        if mtls_config is not UNSET:
            field_dict["mtlsConfig"] = mtls_config
        if topic is not UNSET:
            field_dict["topic"] = topic
        if truststore is not UNSET:
            field_dict["truststore"] = truststore
        if keystore is not UNSET:
            field_dict["keystore"] = keystore
        if send_events is not UNSET:
            field_dict["sendEvents"] = send_events
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        servers = cast(List[str], d.pop("servers", UNSET))

        def _parse_key_pass(data: object) -> Union[Null, Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _key_pass_type_0 = data
                key_pass_type_0: Union[Unset, Null]
                if isinstance(_key_pass_type_0, Unset):
                    key_pass_type_0 = UNSET
                else:
                    key_pass_type_0 = Null.from_dict(_key_pass_type_0)

                return key_pass_type_0
            except:  # noqa: E722
                pass
            return cast(Union[Null, Unset, str], data)

        key_pass = _parse_key_pass(d.pop("keyPass", UNSET))

        _mtls_config = d.pop("mtlsConfig", UNSET)
        mtls_config: Union[Unset, OtoroshiutilshttpMtlsConfig]
        if isinstance(_mtls_config, Unset):
            mtls_config = UNSET
        else:
            mtls_config = OtoroshiutilshttpMtlsConfig.from_dict(_mtls_config)

        topic = d.pop("topic", UNSET)

        def _parse_truststore(data: object) -> Union[Null, Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _truststore_type_0 = data
                truststore_type_0: Union[Unset, Null]
                if isinstance(_truststore_type_0, Unset):
                    truststore_type_0 = UNSET
                else:
                    truststore_type_0 = Null.from_dict(_truststore_type_0)

                return truststore_type_0
            except:  # noqa: E722
                pass
            return cast(Union[Null, Unset, str], data)

        truststore = _parse_truststore(d.pop("truststore", UNSET))

        def _parse_keystore(data: object) -> Union[Null, Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _keystore_type_0 = data
                keystore_type_0: Union[Unset, Null]
                if isinstance(_keystore_type_0, Unset):
                    keystore_type_0 = UNSET
                else:
                    keystore_type_0 = Null.from_dict(_keystore_type_0)

                return keystore_type_0
            except:  # noqa: E722
                pass
            return cast(Union[Null, Unset, str], data)

        keystore = _parse_keystore(d.pop("keystore", UNSET))

        send_events = d.pop("sendEvents", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, OtoroshieventsKafkaConfigType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = OtoroshieventsKafkaConfigType(_type)

        otoroshievents_kafka_config = cls(
            servers=servers,
            key_pass=key_pass,
            mtls_config=mtls_config,
            topic=topic,
            truststore=truststore,
            keystore=keystore,
            send_events=send_events,
            type=type,
        )

        otoroshievents_kafka_config.additional_properties = d
        return otoroshievents_kafka_config

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
