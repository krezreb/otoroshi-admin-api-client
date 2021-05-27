from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.otoroshimodels_entity_location import OtoroshimodelsEntityLocation
from ..models.otoroshimodels_otoroshi_admin_type import OtoroshimodelsOtoroshiAdminType
from ..models.otoroshimodels_simple_otoroshi_admin_metadata import OtoroshimodelsSimpleOtoroshiAdminMetadata
from ..models.otoroshimodels_simple_otoroshi_admin_type import OtoroshimodelsSimpleOtoroshiAdminType
from ..models.otoroshimodels_user_rights import OtoroshimodelsUserRights
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshimodelsSimpleOtoroshiAdmin")


@attr.s(auto_attribs=True)
class OtoroshimodelsSimpleOtoroshiAdmin:
    """An otoroshi admin user"""

    created_at: Union[Unset, float] = UNSET
    metadata: Union[Unset, OtoroshimodelsSimpleOtoroshiAdminMetadata] = UNSET
    password: Union[Unset, str] = UNSET
    rights: Union[Unset, OtoroshimodelsUserRights] = UNSET
    location: Union[Unset, OtoroshimodelsEntityLocation] = UNSET
    typ: Union[Unset, OtoroshimodelsOtoroshiAdminType] = UNSET
    label: Union[Unset, str] = UNSET
    type: Union[Unset, OtoroshimodelsSimpleOtoroshiAdminType] = UNSET
    username: Union[Unset, str] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_at = self.created_at
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        password = self.password
        rights: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.rights, Unset):
            rights = self.rights.to_dict()

        location: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict()

        typ: Union[Unset, str] = UNSET
        if not isinstance(self.typ, Unset):
            typ = self.typ.value

        label = self.label
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        username = self.username
        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if password is not UNSET:
            field_dict["password"] = password
        if rights is not UNSET:
            field_dict["rights"] = rights
        if location is not UNSET:
            field_dict["location"] = location
        if typ is not UNSET:
            field_dict["typ"] = typ
        if label is not UNSET:
            field_dict["label"] = label
        if type is not UNSET:
            field_dict["type"] = type
        if username is not UNSET:
            field_dict["username"] = username
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        created_at = d.pop("createdAt", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, OtoroshimodelsSimpleOtoroshiAdminMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = OtoroshimodelsSimpleOtoroshiAdminMetadata.from_dict(_metadata)

        password = d.pop("password", UNSET)

        _rights = d.pop("rights", UNSET)
        rights: Union[Unset, OtoroshimodelsUserRights]
        if isinstance(_rights, Unset):
            rights = UNSET
        else:
            rights = OtoroshimodelsUserRights.from_dict(_rights)

        _location = d.pop("location", UNSET)
        location: Union[Unset, OtoroshimodelsEntityLocation]
        if isinstance(_location, Unset):
            location = UNSET
        else:
            location = OtoroshimodelsEntityLocation.from_dict(_location)

        _typ = d.pop("typ", UNSET)
        typ: Union[Unset, OtoroshimodelsOtoroshiAdminType]
        if isinstance(_typ, Unset):
            typ = UNSET
        else:
            typ = OtoroshimodelsOtoroshiAdminType(_typ)

        label = d.pop("label", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, OtoroshimodelsSimpleOtoroshiAdminType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = OtoroshimodelsSimpleOtoroshiAdminType(_type)

        username = d.pop("username", UNSET)

        tags = cast(List[str], d.pop("tags", UNSET))

        otoroshimodels_simple_otoroshi_admin = cls(
            created_at=created_at,
            metadata=metadata,
            password=password,
            rights=rights,
            location=location,
            typ=typ,
            label=label,
            type=type,
            username=username,
            tags=tags,
        )

        otoroshimodels_simple_otoroshi_admin.additional_properties = d
        return otoroshimodels_simple_otoroshi_admin

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
