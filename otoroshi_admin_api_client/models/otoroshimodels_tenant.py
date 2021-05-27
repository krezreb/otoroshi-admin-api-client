from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.otoroshimodels_tenant_metadata import OtoroshimodelsTenantMetadata
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshimodelsTenant")


@attr.s(auto_attribs=True)
class OtoroshimodelsTenant:
    """An otoroshi model for an organization (otoroshi-ui)"""

    description: Union[Unset, str] = UNSET
    metadata: Union[Unset, OtoroshimodelsTenantMetadata] = UNSET
    name: Union[Unset, str] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        name = self.name
        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if name is not UNSET:
            field_dict["name"] = name
        if tags is not UNSET:
            field_dict["tags"] = tags
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, OtoroshimodelsTenantMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = OtoroshimodelsTenantMetadata.from_dict(_metadata)

        name = d.pop("name", UNSET)

        tags = cast(List[str], d.pop("tags", UNSET))

        id = d.pop("id", UNSET)

        otoroshimodels_tenant = cls(
            description=description,
            metadata=metadata,
            name=name,
            tags=tags,
            id=id,
        )

        otoroshimodels_tenant.additional_properties = d
        return otoroshimodels_tenant

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
