from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.null import Null
from ..models.otoroshimodels_always_match import OtoroshimodelsAlwaysMatch
from ..models.otoroshimodels_data_center_match import OtoroshimodelsDataCenterMatch
from ..models.otoroshimodels_geolocation_match import OtoroshimodelsGeolocationMatch
from ..models.otoroshimodels_infra_provider_match import OtoroshimodelsInfraProviderMatch
from ..models.otoroshimodels_network_location_match import OtoroshimodelsNetworkLocationMatch
from ..models.otoroshimodels_rack_match import OtoroshimodelsRackMatch
from ..models.otoroshimodels_region_match import OtoroshimodelsRegionMatch
from ..models.otoroshimodels_zone_match import OtoroshimodelsZoneMatch
from ..models.otoroshiutilshttp_mtls_config import OtoroshiutilshttpMtlsConfig
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshimodelsTarget")


@attr.s(auto_attribs=True)
class OtoroshimodelsTarget:
    """A target model for a service (destination for forwarded requests)"""

    host: Union[Unset, str] = UNSET
    weight: Union[Unset, int] = UNSET
    protocol: Union[Unset, str] = UNSET
    predicate: Union[
        OtoroshimodelsAlwaysMatch,
        OtoroshimodelsDataCenterMatch,
        OtoroshimodelsGeolocationMatch,
        OtoroshimodelsInfraProviderMatch,
        OtoroshimodelsNetworkLocationMatch,
        OtoroshimodelsRackMatch,
        OtoroshimodelsRegionMatch,
        OtoroshimodelsZoneMatch,
        Unset,
    ] = UNSET
    ip_address: Union[Null, Unset, str] = UNSET
    mtls_config: Union[Unset, OtoroshiutilshttpMtlsConfig] = UNSET
    scheme: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        host = self.host
        weight = self.weight
        protocol = self.protocol
        predicate: Union[Dict[str, Any], Unset]
        if isinstance(self.predicate, Unset):
            predicate = UNSET
        elif isinstance(self.predicate, OtoroshimodelsAlwaysMatch):
            predicate = self.predicate.to_dict()

        elif isinstance(self.predicate, OtoroshimodelsDataCenterMatch):
            predicate = self.predicate.to_dict()

        elif isinstance(self.predicate, OtoroshimodelsGeolocationMatch):
            predicate = self.predicate.to_dict()

        elif isinstance(self.predicate, OtoroshimodelsInfraProviderMatch):
            predicate = self.predicate.to_dict()

        elif isinstance(self.predicate, OtoroshimodelsNetworkLocationMatch):
            predicate = self.predicate.to_dict()

        elif isinstance(self.predicate, OtoroshimodelsRackMatch):
            predicate = self.predicate.to_dict()

        elif isinstance(self.predicate, OtoroshimodelsRegionMatch):
            predicate = self.predicate.to_dict()

        else:
            predicate = self.predicate.to_dict()

        ip_address: Union[Dict[str, Any], Unset, str]
        if isinstance(self.ip_address, Unset):
            ip_address = UNSET
        elif isinstance(self.ip_address, Null):
            ip_address = UNSET
            if not isinstance(self.ip_address, Unset):
                ip_address = self.ip_address.to_dict()

        else:
            ip_address = self.ip_address

        mtls_config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mtls_config, Unset):
            mtls_config = self.mtls_config.to_dict()

        scheme = self.scheme

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if host is not UNSET:
            field_dict["host"] = host
        if weight is not UNSET:
            field_dict["weight"] = weight
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if predicate is not UNSET:
            field_dict["predicate"] = predicate
        if ip_address is not UNSET:
            field_dict["ipAddress"] = ip_address
        if mtls_config is not UNSET:
            field_dict["mtlsConfig"] = mtls_config
        if scheme is not UNSET:
            field_dict["scheme"] = scheme

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        host = d.pop("host", UNSET)

        weight = d.pop("weight", UNSET)

        protocol = d.pop("protocol", UNSET)

        def _parse_predicate(
            data: object,
        ) -> Union[
            OtoroshimodelsAlwaysMatch,
            OtoroshimodelsDataCenterMatch,
            OtoroshimodelsGeolocationMatch,
            OtoroshimodelsInfraProviderMatch,
            OtoroshimodelsNetworkLocationMatch,
            OtoroshimodelsRackMatch,
            OtoroshimodelsRegionMatch,
            OtoroshimodelsZoneMatch,
            Unset,
        ]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasotoroshimodels_target_predicate_type_0 = OtoroshimodelsAlwaysMatch.from_dict(data)

                return componentsschemasotoroshimodels_target_predicate_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasotoroshimodels_target_predicate_type_1 = OtoroshimodelsDataCenterMatch.from_dict(data)

                return componentsschemasotoroshimodels_target_predicate_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasotoroshimodels_target_predicate_type_2 = OtoroshimodelsGeolocationMatch.from_dict(data)

                return componentsschemasotoroshimodels_target_predicate_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasotoroshimodels_target_predicate_type_3 = OtoroshimodelsInfraProviderMatch.from_dict(
                    data
                )

                return componentsschemasotoroshimodels_target_predicate_type_3
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasotoroshimodels_target_predicate_type_4 = OtoroshimodelsNetworkLocationMatch.from_dict(
                    data
                )

                return componentsschemasotoroshimodels_target_predicate_type_4
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasotoroshimodels_target_predicate_type_5 = OtoroshimodelsRackMatch.from_dict(data)

                return componentsschemasotoroshimodels_target_predicate_type_5
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasotoroshimodels_target_predicate_type_6 = OtoroshimodelsRegionMatch.from_dict(data)

                return componentsschemasotoroshimodels_target_predicate_type_6
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemasotoroshimodels_target_predicate_type_7 = OtoroshimodelsZoneMatch.from_dict(data)

            return componentsschemasotoroshimodels_target_predicate_type_7

        predicate = _parse_predicate(d.pop("predicate", UNSET))

        def _parse_ip_address(data: object) -> Union[Null, Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _ip_address_type_0 = data
                ip_address_type_0: Union[Unset, Null]
                if isinstance(_ip_address_type_0, Unset):
                    ip_address_type_0 = UNSET
                else:
                    ip_address_type_0 = Null.from_dict(_ip_address_type_0)

                return ip_address_type_0
            except:  # noqa: E722
                pass
            return cast(Union[Null, Unset, str], data)

        ip_address = _parse_ip_address(d.pop("ipAddress", UNSET))

        _mtls_config = d.pop("mtlsConfig", UNSET)
        mtls_config: Union[Unset, OtoroshiutilshttpMtlsConfig]
        if isinstance(_mtls_config, Unset):
            mtls_config = UNSET
        else:
            mtls_config = OtoroshiutilshttpMtlsConfig.from_dict(_mtls_config)

        scheme = d.pop("scheme", UNSET)

        otoroshimodels_target = cls(
            host=host,
            weight=weight,
            protocol=protocol,
            predicate=predicate,
            ip_address=ip_address,
            mtls_config=mtls_config,
            scheme=scheme,
        )

        otoroshimodels_target.additional_properties = d
        return otoroshimodels_target

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
