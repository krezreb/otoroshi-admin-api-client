from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.otoroshimodels_global_scripts_job_config import OtoroshimodelsGlobalScriptsJobConfig
from ..models.otoroshimodels_global_scripts_pre_route_config import OtoroshimodelsGlobalScriptsPreRouteConfig
from ..models.otoroshimodels_global_scripts_sink_config import OtoroshimodelsGlobalScriptsSinkConfig
from ..models.otoroshimodels_global_scripts_transformers_config import OtoroshimodelsGlobalScriptsTransformersConfig
from ..models.otoroshimodels_global_scripts_validator_config import OtoroshimodelsGlobalScriptsValidatorConfig
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshimodelsGlobalScripts")


@attr.s(auto_attribs=True)
class OtoroshimodelsGlobalScripts:
    """Settings to apply plugins globally"""

    job_config: Union[Unset, OtoroshimodelsGlobalScriptsJobConfig] = UNSET
    enabled: Union[Unset, bool] = UNSET
    transformers_config: Union[Unset, OtoroshimodelsGlobalScriptsTransformersConfig] = UNSET
    transformers_refs: Union[Unset, List[str]] = UNSET
    pre_route_refs: Union[Unset, List[str]] = UNSET
    sink_config: Union[Unset, OtoroshimodelsGlobalScriptsSinkConfig] = UNSET
    job_refs: Union[Unset, List[str]] = UNSET
    validator_refs: Union[Unset, List[str]] = UNSET
    sink_refs: Union[Unset, List[str]] = UNSET
    pre_route_config: Union[Unset, OtoroshimodelsGlobalScriptsPreRouteConfig] = UNSET
    validator_config: Union[Unset, OtoroshimodelsGlobalScriptsValidatorConfig] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        job_config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.job_config, Unset):
            job_config = self.job_config.to_dict()

        enabled = self.enabled
        transformers_config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.transformers_config, Unset):
            transformers_config = self.transformers_config.to_dict()

        transformers_refs: Union[Unset, List[str]] = UNSET
        if not isinstance(self.transformers_refs, Unset):
            transformers_refs = self.transformers_refs

        pre_route_refs: Union[Unset, List[str]] = UNSET
        if not isinstance(self.pre_route_refs, Unset):
            pre_route_refs = self.pre_route_refs

        sink_config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sink_config, Unset):
            sink_config = self.sink_config.to_dict()

        job_refs: Union[Unset, List[str]] = UNSET
        if not isinstance(self.job_refs, Unset):
            job_refs = self.job_refs

        validator_refs: Union[Unset, List[str]] = UNSET
        if not isinstance(self.validator_refs, Unset):
            validator_refs = self.validator_refs

        sink_refs: Union[Unset, List[str]] = UNSET
        if not isinstance(self.sink_refs, Unset):
            sink_refs = self.sink_refs

        pre_route_config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pre_route_config, Unset):
            pre_route_config = self.pre_route_config.to_dict()

        validator_config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.validator_config, Unset):
            validator_config = self.validator_config.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if job_config is not UNSET:
            field_dict["jobConfig"] = job_config
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if transformers_config is not UNSET:
            field_dict["transformersConfig"] = transformers_config
        if transformers_refs is not UNSET:
            field_dict["transformersRefs"] = transformers_refs
        if pre_route_refs is not UNSET:
            field_dict["preRouteRefs"] = pre_route_refs
        if sink_config is not UNSET:
            field_dict["sinkConfig"] = sink_config
        if job_refs is not UNSET:
            field_dict["jobRefs"] = job_refs
        if validator_refs is not UNSET:
            field_dict["validatorRefs"] = validator_refs
        if sink_refs is not UNSET:
            field_dict["sinkRefs"] = sink_refs
        if pre_route_config is not UNSET:
            field_dict["preRouteConfig"] = pre_route_config
        if validator_config is not UNSET:
            field_dict["validatorConfig"] = validator_config

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _job_config = d.pop("jobConfig", UNSET)
        job_config: Union[Unset, OtoroshimodelsGlobalScriptsJobConfig]
        if isinstance(_job_config, Unset):
            job_config = UNSET
        else:
            job_config = OtoroshimodelsGlobalScriptsJobConfig.from_dict(_job_config)

        enabled = d.pop("enabled", UNSET)

        _transformers_config = d.pop("transformersConfig", UNSET)
        transformers_config: Union[Unset, OtoroshimodelsGlobalScriptsTransformersConfig]
        if isinstance(_transformers_config, Unset):
            transformers_config = UNSET
        else:
            transformers_config = OtoroshimodelsGlobalScriptsTransformersConfig.from_dict(_transformers_config)

        transformers_refs = cast(List[str], d.pop("transformersRefs", UNSET))

        pre_route_refs = cast(List[str], d.pop("preRouteRefs", UNSET))

        _sink_config = d.pop("sinkConfig", UNSET)
        sink_config: Union[Unset, OtoroshimodelsGlobalScriptsSinkConfig]
        if isinstance(_sink_config, Unset):
            sink_config = UNSET
        else:
            sink_config = OtoroshimodelsGlobalScriptsSinkConfig.from_dict(_sink_config)

        job_refs = cast(List[str], d.pop("jobRefs", UNSET))

        validator_refs = cast(List[str], d.pop("validatorRefs", UNSET))

        sink_refs = cast(List[str], d.pop("sinkRefs", UNSET))

        _pre_route_config = d.pop("preRouteConfig", UNSET)
        pre_route_config: Union[Unset, OtoroshimodelsGlobalScriptsPreRouteConfig]
        if isinstance(_pre_route_config, Unset):
            pre_route_config = UNSET
        else:
            pre_route_config = OtoroshimodelsGlobalScriptsPreRouteConfig.from_dict(_pre_route_config)

        _validator_config = d.pop("validatorConfig", UNSET)
        validator_config: Union[Unset, OtoroshimodelsGlobalScriptsValidatorConfig]
        if isinstance(_validator_config, Unset):
            validator_config = UNSET
        else:
            validator_config = OtoroshimodelsGlobalScriptsValidatorConfig.from_dict(_validator_config)

        otoroshimodels_global_scripts = cls(
            job_config=job_config,
            enabled=enabled,
            transformers_config=transformers_config,
            transformers_refs=transformers_refs,
            pre_route_refs=pre_route_refs,
            sink_config=sink_config,
            job_refs=job_refs,
            validator_refs=validator_refs,
            sink_refs=sink_refs,
            pre_route_config=pre_route_config,
            validator_config=validator_config,
        )

        otoroshimodels_global_scripts.additional_properties = d
        return otoroshimodels_global_scripts

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
