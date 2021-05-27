from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.otoroshimodels_es_algo_settings import OtoroshimodelsESAlgoSettings
from ..models.otoroshimodels_eskp_algo_settings import OtoroshimodelsESKPAlgoSettings
from ..models.otoroshimodels_hs_algo_settings import OtoroshimodelsHSAlgoSettings
from ..models.otoroshimodels_jwks_algo_settings import OtoroshimodelsJWKSAlgoSettings
from ..models.otoroshimodels_kid_algo_settings import OtoroshimodelsKidAlgoSettings
from ..models.otoroshimodels_rs_algo_settings import OtoroshimodelsRSAlgoSettings
from ..models.otoroshimodels_rsakp_algo_settings import OtoroshimodelsRSAKPAlgoSettings
from ..models.otoroshimodels_sign_type import OtoroshimodelsSignType
from ..models.otoroshimodels_verification_settings import OtoroshimodelsVerificationSettings
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshimodelsSign")


@attr.s(auto_attribs=True)
class OtoroshimodelsSign:
    """jwt token re-sign policy settings"""

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
    verification_settings: Union[Unset, OtoroshimodelsVerificationSettings] = UNSET
    type: Union[Unset, OtoroshimodelsSignType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
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

        verification_settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.verification_settings, Unset):
            verification_settings = self.verification_settings.to_dict()

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if algo_settings is not UNSET:
            field_dict["algoSettings"] = algo_settings
        if verification_settings is not UNSET:
            field_dict["verificationSettings"] = verification_settings
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

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

        _verification_settings = d.pop("verificationSettings", UNSET)
        verification_settings: Union[Unset, OtoroshimodelsVerificationSettings]
        if isinstance(_verification_settings, Unset):
            verification_settings = UNSET
        else:
            verification_settings = OtoroshimodelsVerificationSettings.from_dict(_verification_settings)

        _type = d.pop("type", UNSET)
        type: Union[Unset, OtoroshimodelsSignType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = OtoroshimodelsSignType(_type)

        otoroshimodels_sign = cls(
            algo_settings=algo_settings,
            verification_settings=verification_settings,
            type=type,
        )

        otoroshimodels_sign.additional_properties = d
        return otoroshimodels_sign

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
