from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.otoroshimodels_user_right import OtoroshimodelsUserRight
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshimodelsUserRights")


@attr.s(auto_attribs=True)
class OtoroshimodelsUserRights:
    """Represent a list of user rights"""

    rights: Union[Unset, List[OtoroshimodelsUserRight]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        rights: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.rights, Unset):
            rights = []
            for rights_item_data in self.rights:
                rights_item = rights_item_data.to_dict()

                rights.append(rights_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rights is not UNSET:
            field_dict["rights"] = rights

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        rights = []
        _rights = d.pop("rights", UNSET)
        for rights_item_data in _rights or []:
            rights_item = OtoroshimodelsUserRight.from_dict(rights_item_data)

            rights.append(rights_item)

        otoroshimodels_user_rights = cls(
            rights=rights,
        )

        otoroshimodels_user_rights.additional_properties = d
        return otoroshimodels_user_rights

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
