from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.otoroshimodels_in_query_param_type import OtoroshimodelsInQueryParamType
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshimodelsInQueryParam")


@attr.s(auto_attribs=True)
class OtoroshimodelsInQueryParam:
    """JWT token location (query param)"""

    name: Union[Unset, str] = UNSET
    type: Union[Unset, OtoroshimodelsInQueryParamType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, OtoroshimodelsInQueryParamType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = OtoroshimodelsInQueryParamType(_type)

        otoroshimodels_in_query_param = cls(
            name=name,
            type=type,
        )

        otoroshimodels_in_query_param.additional_properties = d
        return otoroshimodels_in_query_param

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
