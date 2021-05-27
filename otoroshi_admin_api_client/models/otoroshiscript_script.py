from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.otoroshimodels_entity_location import OtoroshimodelsEntityLocation
from ..models.otoroshiscript_plugin_type import OtoroshiscriptPluginType
from ..models.otoroshiscript_script_metadata import OtoroshiscriptScriptMetadata
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshiscriptScript")


@attr.s(auto_attribs=True)
class OtoroshiscriptScript:
    """An otoroshi plugins stored as scala code in the otoroshi datastore"""

    name: Union[Unset, str] = UNSET
    metadata: Union[Unset, OtoroshiscriptScriptMetadata] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    location: Union[Unset, OtoroshimodelsEntityLocation] = UNSET
    desc: Union[Unset, str] = UNSET
    code: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    type: Union[Unset, OtoroshiscriptPluginType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        location: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict()

        desc = self.desc
        code = self.code
        id = self.id
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if tags is not UNSET:
            field_dict["tags"] = tags
        if location is not UNSET:
            field_dict["location"] = location
        if desc is not UNSET:
            field_dict["desc"] = desc
        if code is not UNSET:
            field_dict["code"] = code
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, OtoroshiscriptScriptMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = OtoroshiscriptScriptMetadata.from_dict(_metadata)

        tags = cast(List[str], d.pop("tags", UNSET))

        _location = d.pop("location", UNSET)
        location: Union[Unset, OtoroshimodelsEntityLocation]
        if isinstance(_location, Unset):
            location = UNSET
        else:
            location = OtoroshimodelsEntityLocation.from_dict(_location)

        desc = d.pop("desc", UNSET)

        code = d.pop("code", UNSET)

        id = d.pop("id", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, OtoroshiscriptPluginType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = OtoroshiscriptPluginType(_type)

        otoroshiscript_script = cls(
            name=name,
            metadata=metadata,
            tags=tags,
            location=location,
            desc=desc,
            code=code,
            id=id,
            type=type,
        )

        otoroshiscript_script.additional_properties = d
        return otoroshiscript_script

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
