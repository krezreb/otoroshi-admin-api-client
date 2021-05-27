from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshimodelsEntityLocation")


@attr.s(auto_attribs=True)
class OtoroshimodelsEntityLocation:
    """Location of any entity (teams and organization)"""

    tenant: Union[Unset, str] = UNSET
    teams: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tenant = self.tenant
        teams: Union[Unset, List[str]] = UNSET
        if not isinstance(self.teams, Unset):
            teams = self.teams

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
        tenant = d.pop("tenant", UNSET)

        teams = cast(List[str], d.pop("teams", UNSET))

        otoroshimodels_entity_location = cls(
            tenant=tenant,
            teams=teams,
        )

        otoroshimodels_entity_location.additional_properties = d
        return otoroshimodels_entity_location

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
