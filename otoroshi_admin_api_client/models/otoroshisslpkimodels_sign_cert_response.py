from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.null import Null
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshisslpkimodelsSignCertResponse")


@attr.s(auto_attribs=True)
class OtoroshisslpkimodelsSignCertResponse:
    """Response for a certificate signing operation"""

    cert: Union[Unset, str] = UNSET
    csr: Union[Unset, str] = UNSET
    ca: Union[Null, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cert = self.cert
        csr = self.csr
        ca: Union[Dict[str, Any], Unset, str]
        if isinstance(self.ca, Unset):
            ca = UNSET
        elif isinstance(self.ca, Null):
            ca = UNSET
            if not isinstance(self.ca, Unset):
                ca = self.ca.to_dict()

        else:
            ca = self.ca

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cert is not UNSET:
            field_dict["cert"] = cert
        if csr is not UNSET:
            field_dict["csr"] = csr
        if ca is not UNSET:
            field_dict["ca"] = ca

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cert = d.pop("cert", UNSET)

        csr = d.pop("csr", UNSET)

        def _parse_ca(data: object) -> Union[Null, Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _ca_type_0 = data
                ca_type_0: Union[Unset, Null]
                if isinstance(_ca_type_0, Unset):
                    ca_type_0 = UNSET
                else:
                    ca_type_0 = Null.from_dict(_ca_type_0)

                return ca_type_0
            except:  # noqa: E722
                pass
            return cast(Union[Null, Unset, str], data)

        ca = _parse_ca(d.pop("ca", UNSET))

        otoroshisslpkimodels_sign_cert_response = cls(
            cert=cert,
            csr=csr,
            ca=ca,
        )

        otoroshisslpkimodels_sign_cert_response.additional_properties = d
        return otoroshisslpkimodels_sign_cert_response

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
