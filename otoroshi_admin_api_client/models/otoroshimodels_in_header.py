from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.otoroshimodels_in_header_type import OtoroshimodelsInHeaderType
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshimodelsInHeader")


@attr.s(auto_attribs=True)
class OtoroshimodelsInHeader:
    """JWT token location (header)"""

    name: Union[Unset, str] = UNSET
    type: Union[Unset, OtoroshimodelsInHeaderType] = UNSET
    remove: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        remove = self.remove

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if type is not UNSET:
            field_dict["type"] = type
        if remove is not UNSET:
            field_dict["remove"] = remove

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, OtoroshimodelsInHeaderType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = OtoroshimodelsInHeaderType(_type)

        remove = d.pop("remove", UNSET)

        otoroshimodels_in_header = cls(
            name=name,
            type=type,
            remove=remove,
        )

        otoroshimodels_in_header.additional_properties = d
        return otoroshimodels_in_header

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
