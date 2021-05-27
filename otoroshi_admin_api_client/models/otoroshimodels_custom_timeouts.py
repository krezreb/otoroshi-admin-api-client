from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshimodelsCustomTimeouts")


@attr.s(auto_attribs=True)
class OtoroshimodelsCustomTimeouts:
    """Settings for custom timeouts for a specific path"""

    path: Union[Unset, str] = UNSET
    call_and_stream_timeout: Union[Unset, int] = UNSET
    call_timeout: Union[Unset, int] = UNSET
    idle_timeout: Union[Unset, int] = UNSET
    global_timeout: Union[Unset, int] = UNSET
    connection_timeout: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        path = self.path
        call_and_stream_timeout = self.call_and_stream_timeout
        call_timeout = self.call_timeout
        idle_timeout = self.idle_timeout
        global_timeout = self.global_timeout
        connection_timeout = self.connection_timeout

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if path is not UNSET:
            field_dict["path"] = path
        if call_and_stream_timeout is not UNSET:
            field_dict["callAndStreamTimeout"] = call_and_stream_timeout
        if call_timeout is not UNSET:
            field_dict["callTimeout"] = call_timeout
        if idle_timeout is not UNSET:
            field_dict["idleTimeout"] = idle_timeout
        if global_timeout is not UNSET:
            field_dict["globalTimeout"] = global_timeout
        if connection_timeout is not UNSET:
            field_dict["connectionTimeout"] = connection_timeout

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        path = d.pop("path", UNSET)

        call_and_stream_timeout = d.pop("callAndStreamTimeout", UNSET)

        call_timeout = d.pop("callTimeout", UNSET)

        idle_timeout = d.pop("idleTimeout", UNSET)

        global_timeout = d.pop("globalTimeout", UNSET)

        connection_timeout = d.pop("connectionTimeout", UNSET)

        otoroshimodels_custom_timeouts = cls(
            path=path,
            call_and_stream_timeout=call_and_stream_timeout,
            call_timeout=call_timeout,
            idle_timeout=idle_timeout,
            global_timeout=global_timeout,
            connection_timeout=connection_timeout,
        )

        otoroshimodels_custom_timeouts.additional_properties = d
        return otoroshimodels_custom_timeouts

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
