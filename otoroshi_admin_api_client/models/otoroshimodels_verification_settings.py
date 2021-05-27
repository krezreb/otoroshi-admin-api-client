from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.otoroshimodels_verification_settings_array_fields import OtoroshimodelsVerificationSettingsArrayFields
from ..models.otoroshimodels_verification_settings_fields import OtoroshimodelsVerificationSettingsFields
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshimodelsVerificationSettings")


@attr.s(auto_attribs=True)
class OtoroshimodelsVerificationSettings:
    """jwt token verification settings"""

    fields: Union[Unset, OtoroshimodelsVerificationSettingsFields] = UNSET
    array_fields: Union[Unset, OtoroshimodelsVerificationSettingsArrayFields] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        fields: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.fields, Unset):
            fields = self.fields.to_dict()

        array_fields: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.array_fields, Unset):
            array_fields = self.array_fields.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fields is not UNSET:
            field_dict["fields"] = fields
        if array_fields is not UNSET:
            field_dict["arrayFields"] = array_fields

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _fields = d.pop("fields", UNSET)
        fields: Union[Unset, OtoroshimodelsVerificationSettingsFields]
        if isinstance(_fields, Unset):
            fields = UNSET
        else:
            fields = OtoroshimodelsVerificationSettingsFields.from_dict(_fields)

        _array_fields = d.pop("arrayFields", UNSET)
        array_fields: Union[Unset, OtoroshimodelsVerificationSettingsArrayFields]
        if isinstance(_array_fields, Unset):
            array_fields = UNSET
        else:
            array_fields = OtoroshimodelsVerificationSettingsArrayFields.from_dict(_array_fields)

        otoroshimodels_verification_settings = cls(
            fields=fields,
            array_fields=array_fields,
        )

        otoroshimodels_verification_settings.additional_properties = d
        return otoroshimodels_verification_settings

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
