from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.null import Null
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshimodelsAutoCert")


@attr.s(auto_attribs=True)
class OtoroshimodelsAutoCert:
    """Settings to generate certificates on the fly"""

    allowed: Union[Unset, List[str]] = UNSET
    enabled: Union[Unset, bool] = UNSET
    reply_nicely: Union[Unset, bool] = UNSET
    not_allowed: Union[Unset, List[str]] = UNSET
    ca_ref: Union[Null, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        allowed: Union[Unset, List[str]] = UNSET
        if not isinstance(self.allowed, Unset):
            allowed = self.allowed

        enabled = self.enabled
        reply_nicely = self.reply_nicely
        not_allowed: Union[Unset, List[str]] = UNSET
        if not isinstance(self.not_allowed, Unset):
            not_allowed = self.not_allowed

        ca_ref: Union[Dict[str, Any], Unset, str]
        if isinstance(self.ca_ref, Unset):
            ca_ref = UNSET
        elif isinstance(self.ca_ref, Null):
            ca_ref = UNSET
            if not isinstance(self.ca_ref, Unset):
                ca_ref = self.ca_ref.to_dict()

        else:
            ca_ref = self.ca_ref

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allowed is not UNSET:
            field_dict["allowed"] = allowed
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if reply_nicely is not UNSET:
            field_dict["replyNicely"] = reply_nicely
        if not_allowed is not UNSET:
            field_dict["notAllowed"] = not_allowed
        if ca_ref is not UNSET:
            field_dict["caRef"] = ca_ref

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        allowed = cast(List[str], d.pop("allowed", UNSET))

        enabled = d.pop("enabled", UNSET)

        reply_nicely = d.pop("replyNicely", UNSET)

        not_allowed = cast(List[str], d.pop("notAllowed", UNSET))

        def _parse_ca_ref(data: object) -> Union[Null, Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _ca_ref_type_0 = data
                ca_ref_type_0: Union[Unset, Null]
                if isinstance(_ca_ref_type_0, Unset):
                    ca_ref_type_0 = UNSET
                else:
                    ca_ref_type_0 = Null.from_dict(_ca_ref_type_0)

                return ca_ref_type_0
            except:  # noqa: E722
                pass
            return cast(Union[Null, Unset, str], data)

        ca_ref = _parse_ca_ref(d.pop("caRef", UNSET))

        otoroshimodels_auto_cert = cls(
            allowed=allowed,
            enabled=enabled,
            reply_nicely=reply_nicely,
            not_allowed=not_allowed,
            ca_ref=ca_ref,
        )

        otoroshimodels_auto_cert.additional_properties = d
        return otoroshimodels_auto_cert

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
