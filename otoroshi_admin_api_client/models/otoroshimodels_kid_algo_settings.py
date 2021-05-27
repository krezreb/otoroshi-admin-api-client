from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.otoroshimodels_kid_algo_settings_type import OtoroshimodelsKidAlgoSettingsType
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshimodelsKidAlgoSettings")


@attr.s(auto_attribs=True)
class OtoroshimodelsKidAlgoSettings:
    """Settings to find keypair based on header kid for verification"""

    only_exposed_certs: Union[Unset, bool] = UNSET
    type: Union[Unset, OtoroshimodelsKidAlgoSettingsType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        only_exposed_certs = self.only_exposed_certs
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if only_exposed_certs is not UNSET:
            field_dict["onlyExposedCerts"] = only_exposed_certs
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        only_exposed_certs = d.pop("onlyExposedCerts", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, OtoroshimodelsKidAlgoSettingsType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = OtoroshimodelsKidAlgoSettingsType(_type)

        otoroshimodels_kid_algo_settings = cls(
            only_exposed_certs=only_exposed_certs,
            type=type,
        )

        otoroshimodels_kid_algo_settings.additional_properties = d
        return otoroshimodels_kid_algo_settings

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
