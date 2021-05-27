from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.otoroshimodels_team_metadata import OtoroshimodelsTeamMetadata
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshimodelsTeam")


@attr.s(auto_attribs=True)
class OtoroshimodelsTeam:
    """An otoroshi model for a team of users in the organization (otoroshi-ui)"""

    tags: Union[Unset, List[str]] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    tenant: Union[Unset, str] = UNSET
    metadata: Union[Unset, OtoroshimodelsTeamMetadata] = UNSET
    id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        name = self.name
        description = self.description
        tenant = self.tenant
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tags is not UNSET:
            field_dict["tags"] = tags
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if tenant is not UNSET:
            field_dict["tenant"] = tenant
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        tags = cast(List[str], d.pop("tags", UNSET))

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        tenant = d.pop("tenant", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, OtoroshimodelsTeamMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = OtoroshimodelsTeamMetadata.from_dict(_metadata)

        id = d.pop("id", UNSET)

        otoroshimodels_team = cls(
            tags=tags,
            name=name,
            description=description,
            tenant=tenant,
            metadata=metadata,
            id=id,
        )

        otoroshimodels_team.additional_properties = d
        return otoroshimodels_team

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
