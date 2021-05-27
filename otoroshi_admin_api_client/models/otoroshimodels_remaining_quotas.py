from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshimodelsRemainingQuotas")


@attr.s(auto_attribs=True)
class OtoroshimodelsRemainingQuotas:
    """Remaining quotas for an apikey"""

    current_calls_per_sec: Union[Unset, int] = UNSET
    remaining_calls_per_sec: Union[Unset, int] = UNSET
    current_calls_per_day: Union[Unset, int] = UNSET
    authorized_calls_per_day: Union[Unset, int] = UNSET
    current_calls_per_month: Union[Unset, int] = UNSET
    remaining_calls_per_month: Union[Unset, int] = UNSET
    authorized_calls_per_sec: Union[Unset, int] = UNSET
    authorized_calls_per_month: Union[Unset, int] = UNSET
    remaining_calls_per_day: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        current_calls_per_sec = self.current_calls_per_sec
        remaining_calls_per_sec = self.remaining_calls_per_sec
        current_calls_per_day = self.current_calls_per_day
        authorized_calls_per_day = self.authorized_calls_per_day
        current_calls_per_month = self.current_calls_per_month
        remaining_calls_per_month = self.remaining_calls_per_month
        authorized_calls_per_sec = self.authorized_calls_per_sec
        authorized_calls_per_month = self.authorized_calls_per_month
        remaining_calls_per_day = self.remaining_calls_per_day

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if current_calls_per_sec is not UNSET:
            field_dict["currentCallsPerSec"] = current_calls_per_sec
        if remaining_calls_per_sec is not UNSET:
            field_dict["remainingCallsPerSec"] = remaining_calls_per_sec
        if current_calls_per_day is not UNSET:
            field_dict["currentCallsPerDay"] = current_calls_per_day
        if authorized_calls_per_day is not UNSET:
            field_dict["authorizedCallsPerDay"] = authorized_calls_per_day
        if current_calls_per_month is not UNSET:
            field_dict["currentCallsPerMonth"] = current_calls_per_month
        if remaining_calls_per_month is not UNSET:
            field_dict["remainingCallsPerMonth"] = remaining_calls_per_month
        if authorized_calls_per_sec is not UNSET:
            field_dict["authorizedCallsPerSec"] = authorized_calls_per_sec
        if authorized_calls_per_month is not UNSET:
            field_dict["authorizedCallsPerMonth"] = authorized_calls_per_month
        if remaining_calls_per_day is not UNSET:
            field_dict["remainingCallsPerDay"] = remaining_calls_per_day

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        current_calls_per_sec = d.pop("currentCallsPerSec", UNSET)

        remaining_calls_per_sec = d.pop("remainingCallsPerSec", UNSET)

        current_calls_per_day = d.pop("currentCallsPerDay", UNSET)

        authorized_calls_per_day = d.pop("authorizedCallsPerDay", UNSET)

        current_calls_per_month = d.pop("currentCallsPerMonth", UNSET)

        remaining_calls_per_month = d.pop("remainingCallsPerMonth", UNSET)

        authorized_calls_per_sec = d.pop("authorizedCallsPerSec", UNSET)

        authorized_calls_per_month = d.pop("authorizedCallsPerMonth", UNSET)

        remaining_calls_per_day = d.pop("remainingCallsPerDay", UNSET)

        otoroshimodels_remaining_quotas = cls(
            current_calls_per_sec=current_calls_per_sec,
            remaining_calls_per_sec=remaining_calls_per_sec,
            current_calls_per_day=current_calls_per_day,
            authorized_calls_per_day=authorized_calls_per_day,
            current_calls_per_month=current_calls_per_month,
            remaining_calls_per_month=remaining_calls_per_month,
            authorized_calls_per_sec=authorized_calls_per_sec,
            authorized_calls_per_month=authorized_calls_per_month,
            remaining_calls_per_day=remaining_calls_per_day,
        )

        otoroshimodels_remaining_quotas.additional_properties = d
        return otoroshimodels_remaining_quotas

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
