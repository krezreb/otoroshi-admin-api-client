from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.otoroshiscriptplugins_plugins_config import OtoroshiscriptpluginsPluginsConfig
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshiscriptpluginsPlugins")


@attr.s(auto_attribs=True)
class OtoroshiscriptpluginsPlugins:
    """Settings for plugins (of any kind)"""

    config: Union[Unset, OtoroshiscriptpluginsPluginsConfig] = UNSET
    enabled: Union[Unset, bool] = UNSET
    excluded: Union[Unset, List[str]] = UNSET
    refs: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        enabled = self.enabled
        excluded: Union[Unset, List[str]] = UNSET
        if not isinstance(self.excluded, Unset):
            excluded = self.excluded

        refs: Union[Unset, List[str]] = UNSET
        if not isinstance(self.refs, Unset):
            refs = self.refs

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if config is not UNSET:
            field_dict["config"] = config
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if excluded is not UNSET:
            field_dict["excluded"] = excluded
        if refs is not UNSET:
            field_dict["refs"] = refs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _config = d.pop("config", UNSET)
        config: Union[Unset, OtoroshiscriptpluginsPluginsConfig]
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = OtoroshiscriptpluginsPluginsConfig.from_dict(_config)

        enabled = d.pop("enabled", UNSET)

        excluded = cast(List[str], d.pop("excluded", UNSET))

        refs = cast(List[str], d.pop("refs", UNSET))

        otoroshiscriptplugins_plugins = cls(
            config=config,
            enabled=enabled,
            excluded=excluded,
            refs=refs,
        )

        otoroshiscriptplugins_plugins.additional_properties = d
        return otoroshiscriptplugins_plugins

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
