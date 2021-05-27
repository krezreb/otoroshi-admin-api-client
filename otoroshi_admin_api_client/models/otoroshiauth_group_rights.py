from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.otoroshimodels_user_rights import OtoroshimodelsUserRights
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshiauthGroupRights")


@attr.s(auto_attribs=True)
class OtoroshiauthGroupRights:
    """User rights associated with a group"""

    user_rights: Union[Unset, OtoroshimodelsUserRights] = UNSET
    users: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user_rights: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user_rights, Unset):
            user_rights = self.user_rights.to_dict()

        users: Union[Unset, List[str]] = UNSET
        if not isinstance(self.users, Unset):
            users = self.users

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user_rights is not UNSET:
            field_dict["userRights"] = user_rights
        if users is not UNSET:
            field_dict["users"] = users

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _user_rights = d.pop("userRights", UNSET)
        user_rights: Union[Unset, OtoroshimodelsUserRights]
        if isinstance(_user_rights, Unset):
            user_rights = UNSET
        else:
            user_rights = OtoroshimodelsUserRights.from_dict(_user_rights)

        users = cast(List[str], d.pop("users", UNSET))

        otoroshiauth_group_rights = cls(
            user_rights=user_rights,
            users=users,
        )

        otoroshiauth_group_rights.additional_properties = d
        return otoroshiauth_group_rights

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
