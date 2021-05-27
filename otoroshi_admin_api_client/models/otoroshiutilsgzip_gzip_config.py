from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshiutilsgzipGzipConfig")


@attr.s(auto_attribs=True)
class OtoroshiutilsgzipGzipConfig:
    """Settings for gzip support"""

    compression_level: Union[Unset, int] = UNSET
    black_list: Union[Unset, List[str]] = UNSET
    chunked_threshold: Union[Unset, int] = UNSET
    excluded_patterns: Union[Unset, List[str]] = UNSET
    buffer_size: Union[Unset, int] = UNSET
    white_list: Union[Unset, List[str]] = UNSET
    enabled: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        compression_level = self.compression_level
        black_list: Union[Unset, List[str]] = UNSET
        if not isinstance(self.black_list, Unset):
            black_list = self.black_list

        chunked_threshold = self.chunked_threshold
        excluded_patterns: Union[Unset, List[str]] = UNSET
        if not isinstance(self.excluded_patterns, Unset):
            excluded_patterns = self.excluded_patterns

        buffer_size = self.buffer_size
        white_list: Union[Unset, List[str]] = UNSET
        if not isinstance(self.white_list, Unset):
            white_list = self.white_list

        enabled = self.enabled

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if compression_level is not UNSET:
            field_dict["compressionLevel"] = compression_level
        if black_list is not UNSET:
            field_dict["blackList"] = black_list
        if chunked_threshold is not UNSET:
            field_dict["chunkedThreshold"] = chunked_threshold
        if excluded_patterns is not UNSET:
            field_dict["excludedPatterns"] = excluded_patterns
        if buffer_size is not UNSET:
            field_dict["bufferSize"] = buffer_size
        if white_list is not UNSET:
            field_dict["whiteList"] = white_list
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        compression_level = d.pop("compressionLevel", UNSET)

        black_list = cast(List[str], d.pop("blackList", UNSET))

        chunked_threshold = d.pop("chunkedThreshold", UNSET)

        excluded_patterns = cast(List[str], d.pop("excludedPatterns", UNSET))

        buffer_size = d.pop("bufferSize", UNSET)

        white_list = cast(List[str], d.pop("whiteList", UNSET))

        enabled = d.pop("enabled", UNSET)

        otoroshiutilsgzip_gzip_config = cls(
            compression_level=compression_level,
            black_list=black_list,
            chunked_threshold=chunked_threshold,
            excluded_patterns=excluded_patterns,
            buffer_size=buffer_size,
            white_list=white_list,
            enabled=enabled,
        )

        otoroshiutilsgzip_gzip_config.additional_properties = d
        return otoroshiutilsgzip_gzip_config

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
