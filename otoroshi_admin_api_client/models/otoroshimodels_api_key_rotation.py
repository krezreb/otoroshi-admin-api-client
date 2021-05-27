from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.null import Null
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshimodelsApiKeyRotation")


@attr.s(auto_attribs=True)
class OtoroshimodelsApiKeyRotation:
    """Settings for automatic apikey rotation with grace period"""

    enabled: Union[Unset, bool] = UNSET
    rotation_every: Union[Unset, int] = UNSET
    grace_period: Union[Unset, int] = UNSET
    next_secret: Union[Null, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enabled = self.enabled
        rotation_every = self.rotation_every
        grace_period = self.grace_period
        next_secret: Union[Dict[str, Any], Unset, str]
        if isinstance(self.next_secret, Unset):
            next_secret = UNSET
        elif isinstance(self.next_secret, Null):
            next_secret = UNSET
            if not isinstance(self.next_secret, Unset):
                next_secret = self.next_secret.to_dict()

        else:
            next_secret = self.next_secret

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if rotation_every is not UNSET:
            field_dict["rotationEvery"] = rotation_every
        if grace_period is not UNSET:
            field_dict["gracePeriod"] = grace_period
        if next_secret is not UNSET:
            field_dict["nextSecret"] = next_secret

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        enabled = d.pop("enabled", UNSET)

        rotation_every = d.pop("rotationEvery", UNSET)

        grace_period = d.pop("gracePeriod", UNSET)

        def _parse_next_secret(data: object) -> Union[Null, Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _next_secret_type_0 = data
                next_secret_type_0: Union[Unset, Null]
                if isinstance(_next_secret_type_0, Unset):
                    next_secret_type_0 = UNSET
                else:
                    next_secret_type_0 = Null.from_dict(_next_secret_type_0)

                return next_secret_type_0
            except:  # noqa: E722
                pass
            return cast(Union[Null, Unset, str], data)

        next_secret = _parse_next_secret(d.pop("nextSecret", UNSET))

        otoroshimodels_api_key_rotation = cls(
            enabled=enabled,
            rotation_every=rotation_every,
            grace_period=grace_period,
            next_secret=next_secret,
        )

        otoroshimodels_api_key_rotation.additional_properties = d
        return otoroshimodels_api_key_rotation

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
