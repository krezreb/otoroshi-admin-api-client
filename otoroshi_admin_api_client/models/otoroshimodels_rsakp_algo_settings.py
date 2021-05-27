from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.otoroshimodels_rsakp_algo_settings_type import OtoroshimodelsRSAKPAlgoSettingsType
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshimodelsRSAKPAlgoSettings")


@attr.s(auto_attribs=True)
class OtoroshimodelsRSAKPAlgoSettings:
    """Settings to use RSA signing algorithm from a certificate keypair"""

    size: Union[Unset, int] = UNSET
    cert_id: Union[Unset, str] = UNSET
    type: Union[Unset, OtoroshimodelsRSAKPAlgoSettingsType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        size = self.size
        cert_id = self.cert_id
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if size is not UNSET:
            field_dict["size"] = size
        if cert_id is not UNSET:
            field_dict["certId"] = cert_id
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        size = d.pop("size", UNSET)

        cert_id = d.pop("certId", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, OtoroshimodelsRSAKPAlgoSettingsType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = OtoroshimodelsRSAKPAlgoSettingsType(_type)

        otoroshimodels_rsakp_algo_settings = cls(
            size=size,
            cert_id=cert_id,
            type=type,
        )

        otoroshimodels_rsakp_algo_settings.additional_properties = d
        return otoroshimodels_rsakp_algo_settings

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
