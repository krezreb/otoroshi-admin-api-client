from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.otoroshimodels_team_access import OtoroshimodelsTeamAccess
from ..models.otoroshimodels_tenant_access import OtoroshimodelsTenantAccess
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshimodelsUserRight")


@attr.s(auto_attribs=True)
class OtoroshimodelsUserRight:
    """Represent a user right (teams, organizations) in otoroshi-ui"""

    tenant: Union[Unset, OtoroshimodelsTenantAccess] = UNSET
    teams: Union[Unset, List[OtoroshimodelsTeamAccess]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tenant: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tenant, Unset):
            tenant = self.tenant.to_dict()

        teams: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.teams, Unset):
            teams = []
            for teams_item_data in self.teams:
                teams_item = teams_item_data.to_dict()

                teams.append(teams_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tenant is not UNSET:
            field_dict["tenant"] = tenant
        if teams is not UNSET:
            field_dict["teams"] = teams

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _tenant = d.pop("tenant", UNSET)
        tenant: Union[Unset, OtoroshimodelsTenantAccess]
        if isinstance(_tenant, Unset):
            tenant = UNSET
        else:
            tenant = OtoroshimodelsTenantAccess.from_dict(_tenant)

        teams = []
        _teams = d.pop("teams", UNSET)
        for teams_item_data in _teams or []:
            teams_item = OtoroshimodelsTeamAccess.from_dict(teams_item_data)

            teams.append(teams_item)

        otoroshimodels_user_right = cls(
            tenant=tenant,
            teams=teams,
        )

        otoroshimodels_user_right.additional_properties = d
        return otoroshimodels_user_right

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
