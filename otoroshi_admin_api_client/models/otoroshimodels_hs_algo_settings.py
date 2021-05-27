from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.otoroshimodels_hs_algo_settings_type import OtoroshimodelsHSAlgoSettingsType
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshimodelsHSAlgoSettings")


@attr.s(auto_attribs=True)
class OtoroshimodelsHSAlgoSettings:
    """Settings to use HMAC-SHA signing algorithm"""

    size: Union[Unset, int] = UNSET
    base_64: Union[Unset, bool] = UNSET
    secret: Union[Unset, str] = UNSET
    type: Union[Unset, OtoroshimodelsHSAlgoSettingsType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        size = self.size
        base_64 = self.base_64
        secret = self.secret
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if size is not UNSET:
            field_dict["size"] = size
        if base_64 is not UNSET:
            field_dict["base64"] = base_64
        if secret is not UNSET:
            field_dict["secret"] = secret
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        size = d.pop("size", UNSET)

        base_64 = d.pop("base64", UNSET)

        secret = d.pop("secret", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, OtoroshimodelsHSAlgoSettingsType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = OtoroshimodelsHSAlgoSettingsType(_type)

        otoroshimodels_hs_algo_settings = cls(
            size=size,
            base_64=base_64,
            secret=secret,
            type=type,
        )

        otoroshimodels_hs_algo_settings.additional_properties = d
        return otoroshimodels_hs_algo_settings

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
