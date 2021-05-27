from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.null import Null
from ..models.otoroshimodels_custom_timeouts import OtoroshimodelsCustomTimeouts
from ..models.playapilibsws_ws_proxy_server import PlayapilibswsWSProxyServer
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshimodelsClientConfig")


@attr.s(auto_attribs=True)
class OtoroshimodelsClientConfig:
    """Settings for the http client when http request is forwarded"""

    connection_timeout: Union[Unset, int] = UNSET
    use_circuit_breaker: Union[Unset, bool] = UNSET
    retry_initial_delay: Union[Unset, int] = UNSET
    proxy: Union[Null, Union[Null, PlayapilibswsWSProxyServer], Unset] = UNSET
    call_timeout: Union[Unset, int] = UNSET
    call_and_stream_timeout: Union[Unset, int] = UNSET
    global_timeout: Union[Unset, int] = UNSET
    max_errors: Union[Unset, int] = UNSET
    retries: Union[Unset, int] = UNSET
    backoff_factor: Union[Unset, int] = UNSET
    custom_timeouts: Union[Unset, List[OtoroshimodelsCustomTimeouts]] = UNSET
    idle_timeout: Union[Unset, int] = UNSET
    sample_interval: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        connection_timeout = self.connection_timeout
        use_circuit_breaker = self.use_circuit_breaker
        retry_initial_delay = self.retry_initial_delay
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

        call_timeout = self.call_timeout
        call_and_stream_timeout = self.call_and_stream_timeout
        global_timeout = self.global_timeout
        max_errors = self.max_errors
        retries = self.retries
        backoff_factor = self.backoff_factor
        custom_timeouts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.custom_timeouts, Unset):
            custom_timeouts = []
            for custom_timeouts_item_data in self.custom_timeouts:
                custom_timeouts_item = custom_timeouts_item_data.to_dict()

                custom_timeouts.append(custom_timeouts_item)

        idle_timeout = self.idle_timeout
        sample_interval = self.sample_interval

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if connection_timeout is not UNSET:
            field_dict["connectionTimeout"] = connection_timeout
        if use_circuit_breaker is not UNSET:
            field_dict["useCircuitBreaker"] = use_circuit_breaker
        if retry_initial_delay is not UNSET:
            field_dict["retryInitialDelay"] = retry_initial_delay
        if proxy is not UNSET:
            field_dict["proxy"] = proxy
        if call_timeout is not UNSET:
            field_dict["callTimeout"] = call_timeout
        if call_and_stream_timeout is not UNSET:
            field_dict["callAndStreamTimeout"] = call_and_stream_timeout
        if global_timeout is not UNSET:
            field_dict["globalTimeout"] = global_timeout
        if max_errors is not UNSET:
            field_dict["maxErrors"] = max_errors
        if retries is not UNSET:
            field_dict["retries"] = retries
        if backoff_factor is not UNSET:
            field_dict["backoffFactor"] = backoff_factor
        if custom_timeouts is not UNSET:
            field_dict["customTimeouts"] = custom_timeouts
        if idle_timeout is not UNSET:
            field_dict["idleTimeout"] = idle_timeout
        if sample_interval is not UNSET:
            field_dict["sampleInterval"] = sample_interval

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        connection_timeout = d.pop("connectionTimeout", UNSET)

        use_circuit_breaker = d.pop("useCircuitBreaker", UNSET)

        retry_initial_delay = d.pop("retryInitialDelay", UNSET)

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

        call_timeout = d.pop("callTimeout", UNSET)

        call_and_stream_timeout = d.pop("callAndStreamTimeout", UNSET)

        global_timeout = d.pop("globalTimeout", UNSET)

        max_errors = d.pop("maxErrors", UNSET)

        retries = d.pop("retries", UNSET)

        backoff_factor = d.pop("backoffFactor", UNSET)

        custom_timeouts = []
        _custom_timeouts = d.pop("customTimeouts", UNSET)
        for custom_timeouts_item_data in _custom_timeouts or []:
            custom_timeouts_item = OtoroshimodelsCustomTimeouts.from_dict(custom_timeouts_item_data)

            custom_timeouts.append(custom_timeouts_item)

        idle_timeout = d.pop("idleTimeout", UNSET)

        sample_interval = d.pop("sampleInterval", UNSET)

        otoroshimodels_client_config = cls(
            connection_timeout=connection_timeout,
            use_circuit_breaker=use_circuit_breaker,
            retry_initial_delay=retry_initial_delay,
            proxy=proxy,
            call_timeout=call_timeout,
            call_and_stream_timeout=call_and_stream_timeout,
            global_timeout=global_timeout,
            max_errors=max_errors,
            retries=retries,
            backoff_factor=backoff_factor,
            custom_timeouts=custom_timeouts,
            idle_timeout=idle_timeout,
            sample_interval=sample_interval,
        )

        otoroshimodels_client_config.additional_properties = d
        return otoroshimodels_client_config

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
