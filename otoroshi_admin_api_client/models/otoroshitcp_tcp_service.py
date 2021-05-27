from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.otoroshimodels_entity_location import OtoroshimodelsEntityLocation
from ..models.otoroshissl_client_auth import OtoroshisslClientAuth
from ..models.otoroshitcp_sni_settings import OtoroshitcpSniSettings
from ..models.otoroshitcp_tcp_rule import OtoroshitcpTcpRule
from ..models.otoroshitcp_tcp_service_metadata import OtoroshitcpTcpServiceMetadata
from ..models.otoroshitcp_tls_mode import OtoroshitcpTlsMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshitcpTcpService")


@attr.s(auto_attribs=True)
class OtoroshitcpTcpService:
    """Model for a TCP proxy"""

    enabled: Union[Unset, bool] = UNSET
    description: Union[Unset, str] = UNSET
    metadata: Union[Unset, OtoroshitcpTcpServiceMetadata] = UNSET
    port: Union[Unset, int] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    rules: Union[Unset, List[OtoroshitcpTcpRule]] = UNSET
    client_auth: Union[Unset, OtoroshisslClientAuth] = UNSET
    interface: Union[Unset, str] = UNSET
    sni: Union[Unset, OtoroshitcpSniSettings] = UNSET
    id: Union[Unset, str] = UNSET
    location: Union[Unset, OtoroshimodelsEntityLocation] = UNSET
    name: Union[Unset, str] = UNSET
    tls: Union[Unset, OtoroshitcpTlsMode] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enabled = self.enabled
        description = self.description
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        port = self.port
        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        rules: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.rules, Unset):
            rules = []
            for rules_item_data in self.rules:
                rules_item = rules_item_data.to_dict()

                rules.append(rules_item)

        client_auth: Union[Unset, str] = UNSET
        if not isinstance(self.client_auth, Unset):
            client_auth = self.client_auth.value

        interface = self.interface
        sni: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sni, Unset):
            sni = self.sni.to_dict()

        id = self.id
        location: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict()

        name = self.name
        tls: Union[Unset, str] = UNSET
        if not isinstance(self.tls, Unset):
            tls = self.tls.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if description is not UNSET:
            field_dict["description"] = description
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if port is not UNSET:
            field_dict["port"] = port
        if tags is not UNSET:
            field_dict["tags"] = tags
        if rules is not UNSET:
            field_dict["rules"] = rules
        if client_auth is not UNSET:
            field_dict["clientAuth"] = client_auth
        if interface is not UNSET:
            field_dict["interface"] = interface
        if sni is not UNSET:
            field_dict["sni"] = sni
        if id is not UNSET:
            field_dict["id"] = id
        if location is not UNSET:
            field_dict["location"] = location
        if name is not UNSET:
            field_dict["name"] = name
        if tls is not UNSET:
            field_dict["tls"] = tls

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        enabled = d.pop("enabled", UNSET)

        description = d.pop("description", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, OtoroshitcpTcpServiceMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = OtoroshitcpTcpServiceMetadata.from_dict(_metadata)

        port = d.pop("port", UNSET)

        tags = cast(List[str], d.pop("tags", UNSET))

        rules = []
        _rules = d.pop("rules", UNSET)
        for rules_item_data in _rules or []:
            rules_item = OtoroshitcpTcpRule.from_dict(rules_item_data)

            rules.append(rules_item)

        _client_auth = d.pop("clientAuth", UNSET)
        client_auth: Union[Unset, OtoroshisslClientAuth]
        if isinstance(_client_auth, Unset):
            client_auth = UNSET
        else:
            client_auth = OtoroshisslClientAuth(_client_auth)

        interface = d.pop("interface", UNSET)

        _sni = d.pop("sni", UNSET)
        sni: Union[Unset, OtoroshitcpSniSettings]
        if isinstance(_sni, Unset):
            sni = UNSET
        else:
            sni = OtoroshitcpSniSettings.from_dict(_sni)

        id = d.pop("id", UNSET)

        _location = d.pop("location", UNSET)
        location: Union[Unset, OtoroshimodelsEntityLocation]
        if isinstance(_location, Unset):
            location = UNSET
        else:
            location = OtoroshimodelsEntityLocation.from_dict(_location)

        name = d.pop("name", UNSET)

        _tls = d.pop("tls", UNSET)
        tls: Union[Unset, OtoroshitcpTlsMode]
        if isinstance(_tls, Unset):
            tls = UNSET
        else:
            tls = OtoroshitcpTlsMode(_tls)

        otoroshitcp_tcp_service = cls(
            enabled=enabled,
            description=description,
            metadata=metadata,
            port=port,
            tags=tags,
            rules=rules,
            client_auth=client_auth,
            interface=interface,
            sni=sni,
            id=id,
            location=location,
            name=name,
            tls=tls,
        )

        otoroshitcp_tcp_service.additional_properties = d
        return otoroshitcp_tcp_service

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
