from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshieventsStatsdConfig")


@attr.s(auto_attribs=True)
class OtoroshieventsStatsdConfig:
    """Settings for connection to a statsd agent"""

    datadog: Union[Unset, bool] = UNSET
    host: Union[Unset, str] = UNSET
    port: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        datadog = self.datadog
        host = self.host
        port = self.port

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if datadog is not UNSET:
            field_dict["datadog"] = datadog
        if host is not UNSET:
            field_dict["host"] = host
        if port is not UNSET:
            field_dict["port"] = port

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        datadog = d.pop("datadog", UNSET)

        host = d.pop("host", UNSET)

        port = d.pop("port", UNSET)

        otoroshievents_statsd_config = cls(
            datadog=datadog,
            host=host,
            port=port,
        )

        otoroshievents_statsd_config.additional_properties = d
        return otoroshievents_statsd_config

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
