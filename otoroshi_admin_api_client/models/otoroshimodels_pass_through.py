from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.otoroshimodels_pass_through_type import OtoroshimodelsPassThroughType
from ..models.otoroshimodels_verification_settings import OtoroshimodelsVerificationSettings
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshimodelsPassThrough")


@attr.s(auto_attribs=True)
class OtoroshimodelsPassThrough:
    """jwt token validation policicy that just validate the token"""

    verification_settings: Union[Unset, OtoroshimodelsVerificationSettings] = UNSET
    type: Union[Unset, OtoroshimodelsPassThroughType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        verification_settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.verification_settings, Unset):
            verification_settings = self.verification_settings.to_dict()

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if verification_settings is not UNSET:
            field_dict["verificationSettings"] = verification_settings
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _verification_settings = d.pop("verificationSettings", UNSET)
        verification_settings: Union[Unset, OtoroshimodelsVerificationSettings]
        if isinstance(_verification_settings, Unset):
            verification_settings = UNSET
        else:
            verification_settings = OtoroshimodelsVerificationSettings.from_dict(_verification_settings)

        _type = d.pop("type", UNSET)
        type: Union[Unset, OtoroshimodelsPassThroughType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = OtoroshimodelsPassThroughType(_type)

        otoroshimodels_pass_through = cls(
            verification_settings=verification_settings,
            type=type,
        )

        otoroshimodels_pass_through.additional_properties = d
        return otoroshimodels_pass_through

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
