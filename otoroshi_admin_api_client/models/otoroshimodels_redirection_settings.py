from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshimodelsRedirectionSettings")


@attr.s(auto_attribs=True)
class OtoroshimodelsRedirectionSettings:
    """Settings for routing redirection"""

    enabled: Union[Unset, bool] = UNSET
    code: Union[Unset, int] = UNSET
    to: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enabled = self.enabled
        code = self.code
        to = self.to

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if code is not UNSET:
            field_dict["code"] = code
        if to is not UNSET:
            field_dict["to"] = to

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        enabled = d.pop("enabled", UNSET)

        code = d.pop("code", UNSET)

        to = d.pop("to", UNSET)

        otoroshimodels_redirection_settings = cls(
            enabled=enabled,
            code=code,
            to=to,
        )

        otoroshimodels_redirection_settings.additional_properties = d
        return otoroshimodels_redirection_settings

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
