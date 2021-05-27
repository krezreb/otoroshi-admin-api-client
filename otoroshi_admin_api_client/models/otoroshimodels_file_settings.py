from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.otoroshimodels_file_settings_type import OtoroshimodelsFileSettingsType
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshimodelsFileSettings")


@attr.s(auto_attribs=True)
class OtoroshimodelsFileSettings:
    """Settings for a file data exporter"""

    path: Union[Unset, str] = UNSET
    max_file_size: Union[Unset, int] = UNSET
    type: Union[Unset, OtoroshimodelsFileSettingsType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        path = self.path
        max_file_size = self.max_file_size
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if path is not UNSET:
            field_dict["path"] = path
        if max_file_size is not UNSET:
            field_dict["maxFileSize"] = max_file_size
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        path = d.pop("path", UNSET)

        max_file_size = d.pop("maxFileSize", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, OtoroshimodelsFileSettingsType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = OtoroshimodelsFileSettingsType(_type)

        otoroshimodels_file_settings = cls(
            path=path,
            max_file_size=max_file_size,
            type=type,
        )

        otoroshimodels_file_settings.additional_properties = d
        return otoroshimodels_file_settings

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
