from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshimodelsTeamAccess")


@attr.s(auto_attribs=True)
class OtoroshimodelsTeamAccess:
    """Access rights for teams"""

    can_read: Union[Unset, bool] = UNSET
    value: Union[Unset, str] = UNSET
    can_write: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        can_read = self.can_read
        value = self.value
        can_write = self.can_write

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if can_read is not UNSET:
            field_dict["canRead"] = can_read
        if value is not UNSET:
            field_dict["value"] = value
        if can_write is not UNSET:
            field_dict["canWrite"] = can_write

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        can_read = d.pop("canRead", UNSET)

        value = d.pop("value", UNSET)

        can_write = d.pop("canWrite", UNSET)

        otoroshimodels_team_access = cls(
            can_read=can_read,
            value=value,
            can_write=can_write,
        )

        otoroshimodels_team_access.additional_properties = d
        return otoroshimodels_team_access

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
