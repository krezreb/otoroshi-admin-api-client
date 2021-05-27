from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.null import Null
from ..models.otoroshimodels_bad_responses_fault_config import OtoroshimodelsBadResponsesFaultConfig
from ..models.otoroshimodels_large_request_fault_config import OtoroshimodelsLargeRequestFaultConfig
from ..models.otoroshimodels_large_response_fault_config import OtoroshimodelsLargeResponseFaultConfig
from ..models.otoroshimodels_latency_injection_fault_config import OtoroshimodelsLatencyInjectionFaultConfig
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshimodelsChaosConfig")


@attr.s(auto_attribs=True)
class OtoroshimodelsChaosConfig:
    """Settings to enable chaos engineering for a service"""

    bad_responses_fault_config: Union[Null, Union[Null, OtoroshimodelsBadResponsesFaultConfig], Unset] = UNSET
    large_request_fault_config: Union[Null, Union[Null, OtoroshimodelsLargeRequestFaultConfig], Unset] = UNSET
    large_response_fault_config: Union[Null, Union[Null, OtoroshimodelsLargeResponseFaultConfig], Unset] = UNSET
    latency_injection_fault_config: Union[Null, Union[Null, OtoroshimodelsLatencyInjectionFaultConfig], Unset] = UNSET
    enabled: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        bad_responses_fault_config: Union[Dict[str, Any], Unset]
        if isinstance(self.bad_responses_fault_config, Unset):
            bad_responses_fault_config = UNSET
        elif isinstance(self.bad_responses_fault_config, Null):
            bad_responses_fault_config = UNSET
            if not isinstance(self.bad_responses_fault_config, Unset):
                bad_responses_fault_config = self.bad_responses_fault_config.to_dict()

        else:
            bad_responses_fault_config
            if isinstance(self.bad_responses_fault_config, Unset):
                bad_responses_fault_config = UNSET
            elif isinstance(self.bad_responses_fault_config, Null):
                bad_responses_fault_config = UNSET
                if not isinstance(self.bad_responses_fault_config, Unset):
                    bad_responses_fault_config = self.bad_responses_fault_config.to_dict()

            else:
                bad_responses_fault_config = UNSET
                if not isinstance(self.bad_responses_fault_config, Unset):
                    bad_responses_fault_config = self.bad_responses_fault_config.to_dict()

        large_request_fault_config: Union[Dict[str, Any], Unset]
        if isinstance(self.large_request_fault_config, Unset):
            large_request_fault_config = UNSET
        elif isinstance(self.large_request_fault_config, Null):
            large_request_fault_config = UNSET
            if not isinstance(self.large_request_fault_config, Unset):
                large_request_fault_config = self.large_request_fault_config.to_dict()

        else:
            large_request_fault_config
            if isinstance(self.large_request_fault_config, Unset):
                large_request_fault_config = UNSET
            elif isinstance(self.large_request_fault_config, Null):
                large_request_fault_config = UNSET
                if not isinstance(self.large_request_fault_config, Unset):
                    large_request_fault_config = self.large_request_fault_config.to_dict()

            else:
                large_request_fault_config = UNSET
                if not isinstance(self.large_request_fault_config, Unset):
                    large_request_fault_config = self.large_request_fault_config.to_dict()

        large_response_fault_config: Union[Dict[str, Any], Unset]
        if isinstance(self.large_response_fault_config, Unset):
            large_response_fault_config = UNSET
        elif isinstance(self.large_response_fault_config, Null):
            large_response_fault_config = UNSET
            if not isinstance(self.large_response_fault_config, Unset):
                large_response_fault_config = self.large_response_fault_config.to_dict()

        else:
            large_response_fault_config
            if isinstance(self.large_response_fault_config, Unset):
                large_response_fault_config = UNSET
            elif isinstance(self.large_response_fault_config, Null):
                large_response_fault_config = UNSET
                if not isinstance(self.large_response_fault_config, Unset):
                    large_response_fault_config = self.large_response_fault_config.to_dict()

            else:
                large_response_fault_config = UNSET
                if not isinstance(self.large_response_fault_config, Unset):
                    large_response_fault_config = self.large_response_fault_config.to_dict()

        latency_injection_fault_config: Union[Dict[str, Any], Unset]
        if isinstance(self.latency_injection_fault_config, Unset):
            latency_injection_fault_config = UNSET
        elif isinstance(self.latency_injection_fault_config, Null):
            latency_injection_fault_config = UNSET
            if not isinstance(self.latency_injection_fault_config, Unset):
                latency_injection_fault_config = self.latency_injection_fault_config.to_dict()

        else:
            latency_injection_fault_config
            if isinstance(self.latency_injection_fault_config, Unset):
                latency_injection_fault_config = UNSET
            elif isinstance(self.latency_injection_fault_config, Null):
                latency_injection_fault_config = UNSET
                if not isinstance(self.latency_injection_fault_config, Unset):
                    latency_injection_fault_config = self.latency_injection_fault_config.to_dict()

            else:
                latency_injection_fault_config = UNSET
                if not isinstance(self.latency_injection_fault_config, Unset):
                    latency_injection_fault_config = self.latency_injection_fault_config.to_dict()

        enabled = self.enabled

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bad_responses_fault_config is not UNSET:
            field_dict["badResponsesFaultConfig"] = bad_responses_fault_config
        if large_request_fault_config is not UNSET:
            field_dict["largeRequestFaultConfig"] = large_request_fault_config
        if large_response_fault_config is not UNSET:
            field_dict["largeResponseFaultConfig"] = large_response_fault_config
        if latency_injection_fault_config is not UNSET:
            field_dict["latencyInjectionFaultConfig"] = latency_injection_fault_config
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_bad_responses_fault_config(
            data: object,
        ) -> Union[Null, Union[Null, OtoroshimodelsBadResponsesFaultConfig], Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _bad_responses_fault_config_type_0 = data
                bad_responses_fault_config_type_0: Union[Unset, Null]
                if isinstance(_bad_responses_fault_config_type_0, Unset):
                    bad_responses_fault_config_type_0 = UNSET
                else:
                    bad_responses_fault_config_type_0 = Null.from_dict(_bad_responses_fault_config_type_0)

                return bad_responses_fault_config_type_0
            except:  # noqa: E722
                pass
            if not True:
                raise TypeError()

            def _parse_bad_responses_fault_config_type_1(
                data: object,
            ) -> Union[Null, OtoroshimodelsBadResponsesFaultConfig, Unset]:
                if isinstance(data, Unset):
                    return data
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    _bad_responses_fault_config_type_1_type_0 = data
                    bad_responses_fault_config_type_1_type_0: Union[Unset, Null]
                    if isinstance(_bad_responses_fault_config_type_1_type_0, Unset):
                        bad_responses_fault_config_type_1_type_0 = UNSET
                    else:
                        bad_responses_fault_config_type_1_type_0 = Null.from_dict(
                            _bad_responses_fault_config_type_1_type_0
                        )

                    return bad_responses_fault_config_type_1_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                _bad_responses_fault_config_type_1_type_1 = data
                bad_responses_fault_config_type_1_type_1: Union[Unset, OtoroshimodelsBadResponsesFaultConfig]
                if isinstance(_bad_responses_fault_config_type_1_type_1, Unset):
                    bad_responses_fault_config_type_1_type_1 = UNSET
                else:
                    bad_responses_fault_config_type_1_type_1 = OtoroshimodelsBadResponsesFaultConfig.from_dict(
                        _bad_responses_fault_config_type_1_type_1
                    )

                return bad_responses_fault_config_type_1_type_1

            bad_responses_fault_config_type_1 = _parse_bad_responses_fault_config_type_1(data)

            return bad_responses_fault_config_type_1

        bad_responses_fault_config = _parse_bad_responses_fault_config(d.pop("badResponsesFaultConfig", UNSET))

        def _parse_large_request_fault_config(
            data: object,
        ) -> Union[Null, Union[Null, OtoroshimodelsLargeRequestFaultConfig], Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _large_request_fault_config_type_0 = data
                large_request_fault_config_type_0: Union[Unset, Null]
                if isinstance(_large_request_fault_config_type_0, Unset):
                    large_request_fault_config_type_0 = UNSET
                else:
                    large_request_fault_config_type_0 = Null.from_dict(_large_request_fault_config_type_0)

                return large_request_fault_config_type_0
            except:  # noqa: E722
                pass
            if not True:
                raise TypeError()

            def _parse_large_request_fault_config_type_1(
                data: object,
            ) -> Union[Null, OtoroshimodelsLargeRequestFaultConfig, Unset]:
                if isinstance(data, Unset):
                    return data
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    _large_request_fault_config_type_1_type_0 = data
                    large_request_fault_config_type_1_type_0: Union[Unset, Null]
                    if isinstance(_large_request_fault_config_type_1_type_0, Unset):
                        large_request_fault_config_type_1_type_0 = UNSET
                    else:
                        large_request_fault_config_type_1_type_0 = Null.from_dict(
                            _large_request_fault_config_type_1_type_0
                        )

                    return large_request_fault_config_type_1_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                _large_request_fault_config_type_1_type_1 = data
                large_request_fault_config_type_1_type_1: Union[Unset, OtoroshimodelsLargeRequestFaultConfig]
                if isinstance(_large_request_fault_config_type_1_type_1, Unset):
                    large_request_fault_config_type_1_type_1 = UNSET
                else:
                    large_request_fault_config_type_1_type_1 = OtoroshimodelsLargeRequestFaultConfig.from_dict(
                        _large_request_fault_config_type_1_type_1
                    )

                return large_request_fault_config_type_1_type_1

            large_request_fault_config_type_1 = _parse_large_request_fault_config_type_1(data)

            return large_request_fault_config_type_1

        large_request_fault_config = _parse_large_request_fault_config(d.pop("largeRequestFaultConfig", UNSET))

        def _parse_large_response_fault_config(
            data: object,
        ) -> Union[Null, Union[Null, OtoroshimodelsLargeResponseFaultConfig], Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _large_response_fault_config_type_0 = data
                large_response_fault_config_type_0: Union[Unset, Null]
                if isinstance(_large_response_fault_config_type_0, Unset):
                    large_response_fault_config_type_0 = UNSET
                else:
                    large_response_fault_config_type_0 = Null.from_dict(_large_response_fault_config_type_0)

                return large_response_fault_config_type_0
            except:  # noqa: E722
                pass
            if not True:
                raise TypeError()

            def _parse_large_response_fault_config_type_1(
                data: object,
            ) -> Union[Null, OtoroshimodelsLargeResponseFaultConfig, Unset]:
                if isinstance(data, Unset):
                    return data
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    _large_response_fault_config_type_1_type_0 = data
                    large_response_fault_config_type_1_type_0: Union[Unset, Null]
                    if isinstance(_large_response_fault_config_type_1_type_0, Unset):
                        large_response_fault_config_type_1_type_0 = UNSET
                    else:
                        large_response_fault_config_type_1_type_0 = Null.from_dict(
                            _large_response_fault_config_type_1_type_0
                        )

                    return large_response_fault_config_type_1_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                _large_response_fault_config_type_1_type_1 = data
                large_response_fault_config_type_1_type_1: Union[Unset, OtoroshimodelsLargeResponseFaultConfig]
                if isinstance(_large_response_fault_config_type_1_type_1, Unset):
                    large_response_fault_config_type_1_type_1 = UNSET
                else:
                    large_response_fault_config_type_1_type_1 = OtoroshimodelsLargeResponseFaultConfig.from_dict(
                        _large_response_fault_config_type_1_type_1
                    )

                return large_response_fault_config_type_1_type_1

            large_response_fault_config_type_1 = _parse_large_response_fault_config_type_1(data)

            return large_response_fault_config_type_1

        large_response_fault_config = _parse_large_response_fault_config(d.pop("largeResponseFaultConfig", UNSET))

        def _parse_latency_injection_fault_config(
            data: object,
        ) -> Union[Null, Union[Null, OtoroshimodelsLatencyInjectionFaultConfig], Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _latency_injection_fault_config_type_0 = data
                latency_injection_fault_config_type_0: Union[Unset, Null]
                if isinstance(_latency_injection_fault_config_type_0, Unset):
                    latency_injection_fault_config_type_0 = UNSET
                else:
                    latency_injection_fault_config_type_0 = Null.from_dict(_latency_injection_fault_config_type_0)

                return latency_injection_fault_config_type_0
            except:  # noqa: E722
                pass
            if not True:
                raise TypeError()

            def _parse_latency_injection_fault_config_type_1(
                data: object,
            ) -> Union[Null, OtoroshimodelsLatencyInjectionFaultConfig, Unset]:
                if isinstance(data, Unset):
                    return data
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    _latency_injection_fault_config_type_1_type_0 = data
                    latency_injection_fault_config_type_1_type_0: Union[Unset, Null]
                    if isinstance(_latency_injection_fault_config_type_1_type_0, Unset):
                        latency_injection_fault_config_type_1_type_0 = UNSET
                    else:
                        latency_injection_fault_config_type_1_type_0 = Null.from_dict(
                            _latency_injection_fault_config_type_1_type_0
                        )

                    return latency_injection_fault_config_type_1_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                _latency_injection_fault_config_type_1_type_1 = data
                latency_injection_fault_config_type_1_type_1: Union[Unset, OtoroshimodelsLatencyInjectionFaultConfig]
                if isinstance(_latency_injection_fault_config_type_1_type_1, Unset):
                    latency_injection_fault_config_type_1_type_1 = UNSET
                else:
                    latency_injection_fault_config_type_1_type_1 = OtoroshimodelsLatencyInjectionFaultConfig.from_dict(
                        _latency_injection_fault_config_type_1_type_1
                    )

                return latency_injection_fault_config_type_1_type_1

            latency_injection_fault_config_type_1 = _parse_latency_injection_fault_config_type_1(data)

            return latency_injection_fault_config_type_1

        latency_injection_fault_config = _parse_latency_injection_fault_config(
            d.pop("latencyInjectionFaultConfig", UNSET)
        )

        enabled = d.pop("enabled", UNSET)

        otoroshimodels_chaos_config = cls(
            bad_responses_fault_config=bad_responses_fault_config,
            large_request_fault_config=large_request_fault_config,
            large_response_fault_config=large_response_fault_config,
            latency_injection_fault_config=latency_injection_fault_config,
            enabled=enabled,
        )

        otoroshimodels_chaos_config.additional_properties = d
        return otoroshimodels_chaos_config

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
