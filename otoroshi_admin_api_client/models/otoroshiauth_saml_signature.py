from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.otoroshiauth_saml_canocalization_method import OtoroshiauthSAMLCanocalizationMethod
from ..models.otoroshiauth_saml_signature_algorithm import OtoroshiauthSAMLSignatureAlgorithm
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshiauthSAMLSignature")


@attr.s(auto_attribs=True)
class OtoroshiauthSAMLSignature:
    """Algorithm and canocalization method used to sign SAML documents"""

    algorithm: Union[Unset, OtoroshiauthSAMLSignatureAlgorithm] = UNSET
    canocalization_method: Union[Unset, OtoroshiauthSAMLCanocalizationMethod] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        algorithm: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.algorithm, Unset):
            algorithm = self.algorithm.to_dict()

        canocalization_method: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.canocalization_method, Unset):
            canocalization_method = self.canocalization_method.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if algorithm is not UNSET:
            field_dict["algorithm"] = algorithm
        if canocalization_method is not UNSET:
            field_dict["canocalizationMethod"] = canocalization_method

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _algorithm = d.pop("algorithm", UNSET)
        algorithm: Union[Unset, OtoroshiauthSAMLSignatureAlgorithm]
        if isinstance(_algorithm, Unset):
            algorithm = UNSET
        else:
            algorithm = OtoroshiauthSAMLSignatureAlgorithm.from_dict(_algorithm)

        _canocalization_method = d.pop("canocalizationMethod", UNSET)
        canocalization_method: Union[Unset, OtoroshiauthSAMLCanocalizationMethod]
        if isinstance(_canocalization_method, Unset):
            canocalization_method = UNSET
        else:
            canocalization_method = OtoroshiauthSAMLCanocalizationMethod.from_dict(_canocalization_method)

        otoroshiauth_saml_signature = cls(
            algorithm=algorithm,
            canocalization_method=canocalization_method,
        )

        otoroshiauth_saml_signature.additional_properties = d
        return otoroshiauth_saml_signature

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
