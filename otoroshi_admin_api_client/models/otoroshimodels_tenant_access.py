from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshimodelsTenantAccess")


@attr.s(auto_attribs=True)
class OtoroshimodelsTenantAccess:
    """Access rights for organizations"""

    can_write: Union[Unset, bool] = UNSET
    value: Union[Unset, str] = UNSET
    can_read: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        can_write = self.can_write
        value = self.value
        can_read = self.can_read

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if can_write is not UNSET:
            field_dict["canWrite"] = can_write
        if value is not UNSET:
            field_dict["value"] = value
        if can_read is not UNSET:
            field_dict["canRead"] = can_read

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        can_write = d.pop("canWrite", UNSET)

        value = d.pop("value", UNSET)

        can_read = d.pop("canRead", UNSET)

        otoroshimodels_tenant_access = cls(
            can_write=can_write,
            value=value,
            can_read=can_read,
        )

        otoroshimodels_tenant_access.additional_properties = d
        return otoroshimodels_tenant_access

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
