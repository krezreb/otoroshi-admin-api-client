from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.otoroshimodels_metrics_settings_labels import OtoroshimodelsMetricsSettingsLabels
from ..models.otoroshimodels_metrics_settings_type import OtoroshimodelsMetricsSettingsType
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshimodelsMetricsSettings")


@attr.s(auto_attribs=True)
class OtoroshimodelsMetricsSettings:
    """Settings for metrics labels"""

    type: Union[Unset, OtoroshimodelsMetricsSettingsType] = UNSET
    labels: Union[Unset, OtoroshimodelsMetricsSettingsLabels] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        labels: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if labels is not UNSET:
            field_dict["labels"] = labels

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: Union[Unset, OtoroshimodelsMetricsSettingsType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = OtoroshimodelsMetricsSettingsType(_type)

        _labels = d.pop("labels", UNSET)
        labels: Union[Unset, OtoroshimodelsMetricsSettingsLabels]
        if isinstance(_labels, Unset):
            labels = UNSET
        else:
            labels = OtoroshimodelsMetricsSettingsLabels.from_dict(_labels)

        otoroshimodels_metrics_settings = cls(
            type=type,
            labels=labels,
        )

        otoroshimodels_metrics_settings.additional_properties = d
        return otoroshimodels_metrics_settings

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
