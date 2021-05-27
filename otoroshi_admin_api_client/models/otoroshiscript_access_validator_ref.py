from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.otoroshiscript_access_validator_ref_config import OtoroshiscriptAccessValidatorRefConfig
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshiscriptAccessValidatorRef")


@attr.s(auto_attribs=True)
class OtoroshiscriptAccessValidatorRef:
    """References to access validation plugins"""

    enabled: Union[Unset, bool] = UNSET
    excluded_patterns: Union[Unset, List[str]] = UNSET
    refs: Union[Unset, List[str]] = UNSET
    config: Union[Unset, OtoroshiscriptAccessValidatorRefConfig] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enabled = self.enabled
        excluded_patterns: Union[Unset, List[str]] = UNSET
        if not isinstance(self.excluded_patterns, Unset):
            excluded_patterns = self.excluded_patterns

        refs: Union[Unset, List[str]] = UNSET
        if not isinstance(self.refs, Unset):
            refs = self.refs

        config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if excluded_patterns is not UNSET:
            field_dict["excludedPatterns"] = excluded_patterns
        if refs is not UNSET:
            field_dict["refs"] = refs
        if config is not UNSET:
            field_dict["config"] = config

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        enabled = d.pop("enabled", UNSET)

        excluded_patterns = cast(List[str], d.pop("excludedPatterns", UNSET))

        refs = cast(List[str], d.pop("refs", UNSET))

        _config = d.pop("config", UNSET)
        config: Union[Unset, OtoroshiscriptAccessValidatorRefConfig]
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = OtoroshiscriptAccessValidatorRefConfig.from_dict(_config)

        otoroshiscript_access_validator_ref = cls(
            enabled=enabled,
            excluded_patterns=excluded_patterns,
            refs=refs,
            config=config,
        )

        otoroshiscript_access_validator_ref.additional_properties = d
        return otoroshiscript_access_validator_ref

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
