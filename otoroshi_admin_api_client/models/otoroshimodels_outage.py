from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshimodelsOutage")


@attr.s(auto_attribs=True)
class OtoroshimodelsOutage:
    """A snowmonkey outage model"""

    descriptor_name: Union[Unset, str] = UNSET
    descriptor_id: Union[Unset, str] = UNSET
    until: Union[Unset, str] = UNSET
    duration: Union[Unset, float] = UNSET
    started_at: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        descriptor_name = self.descriptor_name
        descriptor_id = self.descriptor_id
        until = self.until
        duration = self.duration
        started_at = self.started_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if descriptor_name is not UNSET:
            field_dict["descriptorName"] = descriptor_name
        if descriptor_id is not UNSET:
            field_dict["descriptorId"] = descriptor_id
        if until is not UNSET:
            field_dict["until"] = until
        if duration is not UNSET:
            field_dict["duration"] = duration
        if started_at is not UNSET:
            field_dict["startedAt"] = started_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        descriptor_name = d.pop("descriptorName", UNSET)

        descriptor_id = d.pop("descriptorId", UNSET)

        until = d.pop("until", UNSET)

        duration = d.pop("duration", UNSET)

        started_at = d.pop("startedAt", UNSET)

        otoroshimodels_outage = cls(
            descriptor_name=descriptor_name,
            descriptor_id=descriptor_id,
            until=until,
            duration=duration,
            started_at=started_at,
        )

        otoroshimodels_outage.additional_properties = d
        return otoroshimodels_outage

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
