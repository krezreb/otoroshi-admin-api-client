from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.otoroshimodels_default_token import OtoroshimodelsDefaultToken
from ..models.otoroshimodels_es_algo_settings import OtoroshimodelsESAlgoSettings
from ..models.otoroshimodels_eskp_algo_settings import OtoroshimodelsESKPAlgoSettings
from ..models.otoroshimodels_hs_algo_settings import OtoroshimodelsHSAlgoSettings
from ..models.otoroshimodels_in_cookie import OtoroshimodelsInCookie
from ..models.otoroshimodels_in_header import OtoroshimodelsInHeader
from ..models.otoroshimodels_in_query_param import OtoroshimodelsInQueryParam
from ..models.otoroshimodels_jwks_algo_settings import OtoroshimodelsJWKSAlgoSettings
from ..models.otoroshimodels_kid_algo_settings import OtoroshimodelsKidAlgoSettings
from ..models.otoroshimodels_local_jwt_verifier_type import OtoroshimodelsLocalJwtVerifierType
from ..models.otoroshimodels_pass_through import OtoroshimodelsPassThrough
from ..models.otoroshimodels_rs_algo_settings import OtoroshimodelsRSAlgoSettings
from ..models.otoroshimodels_rsakp_algo_settings import OtoroshimodelsRSAKPAlgoSettings
from ..models.otoroshimodels_sign import OtoroshimodelsSign
from ..models.otoroshimodels_transform import OtoroshimodelsTransform
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshimodelsLocalJwtVerifier")


@attr.s(auto_attribs=True)
class OtoroshimodelsLocalJwtVerifier:
    """Local jwt verifier (deprecated)"""

    excluded_patterns: Union[Unset, List[str]] = UNSET
    algo_settings: Union[
        OtoroshimodelsESAlgoSettings,
        OtoroshimodelsESKPAlgoSettings,
        OtoroshimodelsHSAlgoSettings,
        OtoroshimodelsJWKSAlgoSettings,
        OtoroshimodelsKidAlgoSettings,
        OtoroshimodelsRSAKPAlgoSettings,
        OtoroshimodelsRSAlgoSettings,
        Unset,
    ] = UNSET
    source: Union[OtoroshimodelsInCookie, OtoroshimodelsInHeader, OtoroshimodelsInQueryParam, Unset] = UNSET
    type: Union[Unset, OtoroshimodelsLocalJwtVerifierType] = UNSET
    strict: Union[Unset, bool] = UNSET
    strategy: Union[
        OtoroshimodelsDefaultToken, OtoroshimodelsPassThrough, OtoroshimodelsSign, OtoroshimodelsTransform, Unset
    ] = UNSET
    enabled: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        excluded_patterns: Union[Unset, List[str]] = UNSET
        if not isinstance(self.excluded_patterns, Unset):
            excluded_patterns = self.excluded_patterns

        algo_settings: Union[Dict[str, Any], Unset]
        if isinstance(self.algo_settings, Unset):
            algo_settings = UNSET
        elif isinstance(self.algo_settings, OtoroshimodelsESAlgoSettings):
            algo_settings = self.algo_settings.to_dict()

        elif isinstance(self.algo_settings, OtoroshimodelsESKPAlgoSettings):
            algo_settings = self.algo_settings.to_dict()

        elif isinstance(self.algo_settings, OtoroshimodelsHSAlgoSettings):
            algo_settings = self.algo_settings.to_dict()

        elif isinstance(self.algo_settings, OtoroshimodelsJWKSAlgoSettings):
            algo_settings = self.algo_settings.to_dict()

        elif isinstance(self.algo_settings, OtoroshimodelsKidAlgoSettings):
            algo_settings = self.algo_settings.to_dict()

        elif isinstance(self.algo_settings, OtoroshimodelsRSAKPAlgoSettings):
            algo_settings = self.algo_settings.to_dict()

        else:
            algo_settings = self.algo_settings.to_dict()

        source: Union[Dict[str, Any], Unset]
        if isinstance(self.source, Unset):
            source = UNSET
        elif isinstance(self.source, OtoroshimodelsInCookie):
            source = self.source.to_dict()

        elif isinstance(self.source, OtoroshimodelsInHeader):
            source = self.source.to_dict()

        else:
            source = self.source.to_dict()

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        strict = self.strict
        strategy: Union[Dict[str, Any], Unset]
        if isinstance(self.strategy, Unset):
            strategy = UNSET
        elif isinstance(self.strategy, OtoroshimodelsDefaultToken):
            strategy = self.strategy.to_dict()

        elif isinstance(self.strategy, OtoroshimodelsPassThrough):
            strategy = self.strategy.to_dict()

        elif isinstance(self.strategy, OtoroshimodelsSign):
            strategy = self.strategy.to_dict()

        else:
            strategy = self.strategy.to_dict()

        enabled = self.enabled

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if excluded_patterns is not UNSET:
            field_dict["excludedPatterns"] = excluded_patterns
        if algo_settings is not UNSET:
            field_dict["algoSettings"] = algo_settings
        if source is not UNSET:
            field_dict["source"] = source
        if type is not UNSET:
            field_dict["type"] = type
        if strict is not UNSET:
            field_dict["strict"] = strict
        if strategy is not UNSET:
            field_dict["strategy"] = strategy
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        excluded_patterns = cast(List[str], d.pop("excludedPatterns", UNSET))

        def _parse_algo_settings(
            data: object,
        ) -> Union[
            OtoroshimodelsESAlgoSettings,
            OtoroshimodelsESKPAlgoSettings,
            OtoroshimodelsHSAlgoSettings,
            OtoroshimodelsJWKSAlgoSettings,
            OtoroshimodelsKidAlgoSettings,
            OtoroshimodelsRSAKPAlgoSettings,
            OtoroshimodelsRSAlgoSettings,
            Unset,
        ]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasotoroshimodels_algo_settings_type_0 = OtoroshimodelsESAlgoSettings.from_dict(data)

                return componentsschemasotoroshimodels_algo_settings_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasotoroshimodels_algo_settings_type_1 = OtoroshimodelsESKPAlgoSettings.from_dict(data)

                return componentsschemasotoroshimodels_algo_settings_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasotoroshimodels_algo_settings_type_2 = OtoroshimodelsHSAlgoSettings.from_dict(data)

                return componentsschemasotoroshimodels_algo_settings_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasotoroshimodels_algo_settings_type_3 = OtoroshimodelsJWKSAlgoSettings.from_dict(data)

                return componentsschemasotoroshimodels_algo_settings_type_3
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasotoroshimodels_algo_settings_type_4 = OtoroshimodelsKidAlgoSettings.from_dict(data)

                return componentsschemasotoroshimodels_algo_settings_type_4
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasotoroshimodels_algo_settings_type_5 = OtoroshimodelsRSAKPAlgoSettings.from_dict(data)

                return componentsschemasotoroshimodels_algo_settings_type_5
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemasotoroshimodels_algo_settings_type_6 = OtoroshimodelsRSAlgoSettings.from_dict(data)

            return componentsschemasotoroshimodels_algo_settings_type_6

        algo_settings = _parse_algo_settings(d.pop("algoSettings", UNSET))

        def _parse_source(
            data: object,
        ) -> Union[OtoroshimodelsInCookie, OtoroshimodelsInHeader, OtoroshimodelsInQueryParam, Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasotoroshimodels_jwt_token_location_type_0 = OtoroshimodelsInCookie.from_dict(data)

                return componentsschemasotoroshimodels_jwt_token_location_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasotoroshimodels_jwt_token_location_type_1 = OtoroshimodelsInHeader.from_dict(data)

                return componentsschemasotoroshimodels_jwt_token_location_type_1
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemasotoroshimodels_jwt_token_location_type_2 = OtoroshimodelsInQueryParam.from_dict(data)

            return componentsschemasotoroshimodels_jwt_token_location_type_2

        source = _parse_source(d.pop("source", UNSET))

        _type = d.pop("type", UNSET)
        type: Union[Unset, OtoroshimodelsLocalJwtVerifierType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = OtoroshimodelsLocalJwtVerifierType(_type)

        strict = d.pop("strict", UNSET)

        def _parse_strategy(
            data: object,
        ) -> Union[
            OtoroshimodelsDefaultToken, OtoroshimodelsPassThrough, OtoroshimodelsSign, OtoroshimodelsTransform, Unset
        ]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasotoroshimodels_verifier_strategy_type_0 = OtoroshimodelsDefaultToken.from_dict(data)

                return componentsschemasotoroshimodels_verifier_strategy_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasotoroshimodels_verifier_strategy_type_1 = OtoroshimodelsPassThrough.from_dict(data)

                return componentsschemasotoroshimodels_verifier_strategy_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasotoroshimodels_verifier_strategy_type_2 = OtoroshimodelsSign.from_dict(data)

                return componentsschemasotoroshimodels_verifier_strategy_type_2
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemasotoroshimodels_verifier_strategy_type_3 = OtoroshimodelsTransform.from_dict(data)

            return componentsschemasotoroshimodels_verifier_strategy_type_3

        strategy = _parse_strategy(d.pop("strategy", UNSET))

        enabled = d.pop("enabled", UNSET)

        otoroshimodels_local_jwt_verifier = cls(
            excluded_patterns=excluded_patterns,
            algo_settings=algo_settings,
            source=source,
            type=type,
            strict=strict,
            strategy=strategy,
            enabled=enabled,
        )

        otoroshimodels_local_jwt_verifier.additional_properties = d
        return otoroshimodels_local_jwt_verifier

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
