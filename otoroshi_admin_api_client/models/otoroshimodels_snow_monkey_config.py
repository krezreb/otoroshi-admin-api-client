from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.otoroshimodels_chaos_config import OtoroshimodelsChaosConfig
from ..models.otoroshimodels_outage_strategy import OtoroshimodelsOutageStrategy
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshimodelsSnowMonkeyConfig")


@attr.s(auto_attribs=True)
class OtoroshimodelsSnowMonkeyConfig:
    """Settings for the snow monkey (chaos engineering)"""

    dry_run: Union[Unset, bool] = UNSET
    outage_duration_to: Union[Unset, float] = UNSET
    chaos_config: Union[Unset, OtoroshimodelsChaosConfig] = UNSET
    times_per_day: Union[Unset, int] = UNSET
    outage_duration_from: Union[Unset, float] = UNSET
    start_time: Union[Unset, str] = UNSET
    include_user_facing_descriptors: Union[Unset, bool] = UNSET
    target_groups: Union[Unset, List[str]] = UNSET
    enabled: Union[Unset, bool] = UNSET
    stop_time: Union[Unset, str] = UNSET
    outage_strategy: Union[Unset, OtoroshimodelsOutageStrategy] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        dry_run = self.dry_run
        outage_duration_to = self.outage_duration_to
        chaos_config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.chaos_config, Unset):
            chaos_config = self.chaos_config.to_dict()

        times_per_day = self.times_per_day
        outage_duration_from = self.outage_duration_from
        start_time = self.start_time
        include_user_facing_descriptors = self.include_user_facing_descriptors
        target_groups: Union[Unset, List[str]] = UNSET
        if not isinstance(self.target_groups, Unset):
            target_groups = self.target_groups

        enabled = self.enabled
        stop_time = self.stop_time
        outage_strategy: Union[Unset, str] = UNSET
        if not isinstance(self.outage_strategy, Unset):
            outage_strategy = self.outage_strategy.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dry_run is not UNSET:
            field_dict["dryRun"] = dry_run
        if outage_duration_to is not UNSET:
            field_dict["outageDurationTo"] = outage_duration_to
        if chaos_config is not UNSET:
            field_dict["chaosConfig"] = chaos_config
        if times_per_day is not UNSET:
            field_dict["timesPerDay"] = times_per_day
        if outage_duration_from is not UNSET:
            field_dict["outageDurationFrom"] = outage_duration_from
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if include_user_facing_descriptors is not UNSET:
            field_dict["includeUserFacingDescriptors"] = include_user_facing_descriptors
        if target_groups is not UNSET:
            field_dict["targetGroups"] = target_groups
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if stop_time is not UNSET:
            field_dict["stopTime"] = stop_time
        if outage_strategy is not UNSET:
            field_dict["outageStrategy"] = outage_strategy

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        dry_run = d.pop("dryRun", UNSET)

        outage_duration_to = d.pop("outageDurationTo", UNSET)

        _chaos_config = d.pop("chaosConfig", UNSET)
        chaos_config: Union[Unset, OtoroshimodelsChaosConfig]
        if isinstance(_chaos_config, Unset):
            chaos_config = UNSET
        else:
            chaos_config = OtoroshimodelsChaosConfig.from_dict(_chaos_config)

        times_per_day = d.pop("timesPerDay", UNSET)

        outage_duration_from = d.pop("outageDurationFrom", UNSET)

        start_time = d.pop("startTime", UNSET)

        include_user_facing_descriptors = d.pop("includeUserFacingDescriptors", UNSET)

        target_groups = cast(List[str], d.pop("targetGroups", UNSET))

        enabled = d.pop("enabled", UNSET)

        stop_time = d.pop("stopTime", UNSET)

        _outage_strategy = d.pop("outageStrategy", UNSET)
        outage_strategy: Union[Unset, OtoroshimodelsOutageStrategy]
        if isinstance(_outage_strategy, Unset):
            outage_strategy = UNSET
        else:
            outage_strategy = OtoroshimodelsOutageStrategy(_outage_strategy)

        otoroshimodels_snow_monkey_config = cls(
            dry_run=dry_run,
            outage_duration_to=outage_duration_to,
            chaos_config=chaos_config,
            times_per_day=times_per_day,
            outage_duration_from=outage_duration_from,
            start_time=start_time,
            include_user_facing_descriptors=include_user_facing_descriptors,
            target_groups=target_groups,
            enabled=enabled,
            stop_time=stop_time,
            outage_strategy=outage_strategy,
        )

        otoroshimodels_snow_monkey_config.additional_properties = d
        return otoroshimodels_snow_monkey_config

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
