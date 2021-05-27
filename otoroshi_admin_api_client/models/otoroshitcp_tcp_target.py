from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.null import Null
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshitcpTcpTarget")


@attr.s(auto_attribs=True)
class OtoroshitcpTcpTarget:
    """Target for a TCP proxy"""

    host: Union[Unset, str] = UNSET
    ip: Union[Null, Unset, str] = UNSET
    port: Union[Unset, int] = UNSET
    tls: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        host = self.host
        ip: Union[Dict[str, Any], Unset, str]
        if isinstance(self.ip, Unset):
            ip = UNSET
        elif isinstance(self.ip, Null):
            ip = UNSET
            if not isinstance(self.ip, Unset):
                ip = self.ip.to_dict()

        else:
            ip = self.ip

        port = self.port
        tls = self.tls

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if host is not UNSET:
            field_dict["host"] = host
        if ip is not UNSET:
            field_dict["ip"] = ip
        if port is not UNSET:
            field_dict["port"] = port
        if tls is not UNSET:
            field_dict["tls"] = tls

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        host = d.pop("host", UNSET)

        def _parse_ip(data: object) -> Union[Null, Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _ip_type_0 = data
                ip_type_0: Union[Unset, Null]
                if isinstance(_ip_type_0, Unset):
                    ip_type_0 = UNSET
                else:
                    ip_type_0 = Null.from_dict(_ip_type_0)

                return ip_type_0
            except:  # noqa: E722
                pass
            return cast(Union[Null, Unset, str], data)

        ip = _parse_ip(d.pop("ip", UNSET))

        port = d.pop("port", UNSET)

        tls = d.pop("tls", UNSET)

        otoroshitcp_tcp_target = cls(
            host=host,
            ip=ip,
            port=port,
            tls=tls,
        )

        otoroshitcp_tcp_target.additional_properties = d
        return otoroshitcp_tcp_target

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
