from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.otoroshimodels_tenant_access import OtoroshimodelsTenantAccess
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshiauthGroupFilter")


@attr.s(auto_attribs=True)
class OtoroshiauthGroupFilter:
    """Filter for a LDAP group"""

    group: Union[Unset, str] = UNSET
    tenant: Union[Unset, OtoroshimodelsTenantAccess] = UNSET
    team: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        group = self.group
        tenant: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tenant, Unset):
            tenant = self.tenant.to_dict()

        team = self.team

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if group is not UNSET:
            field_dict["group"] = group
        if tenant is not UNSET:
            field_dict["tenant"] = tenant
        if team is not UNSET:
            field_dict["team"] = team

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        group = d.pop("group", UNSET)

        _tenant = d.pop("tenant", UNSET)
        tenant: Union[Unset, OtoroshimodelsTenantAccess]
        if isinstance(_tenant, Unset):
            tenant = UNSET
        else:
            tenant = OtoroshimodelsTenantAccess.from_dict(_tenant)

        team = d.pop("team", UNSET)

        otoroshiauth_group_filter = cls(
            group=group,
            tenant=tenant,
            team=team,
        )

        otoroshiauth_group_filter.additional_properties = d
        return otoroshiauth_group_filter

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
