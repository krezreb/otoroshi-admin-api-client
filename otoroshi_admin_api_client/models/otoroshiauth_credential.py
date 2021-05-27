from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.null import Null
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshiauthCredential")


@attr.s(auto_attribs=True)
class OtoroshiauthCredential:
    """Pair of raw certificate, private key and certId for SAML protocol"""

    certificate: Union[Null, Unset, str] = UNSET
    private_key: Union[Null, Unset, str] = UNSET
    cert_id: Union[Null, Unset, str] = UNSET
    use_otoroshi_certificate: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        certificate: Union[Dict[str, Any], Unset, str]
        if isinstance(self.certificate, Unset):
            certificate = UNSET
        elif isinstance(self.certificate, Null):
            certificate = UNSET
            if not isinstance(self.certificate, Unset):
                certificate = self.certificate.to_dict()

        else:
            certificate = self.certificate

        private_key: Union[Dict[str, Any], Unset, str]
        if isinstance(self.private_key, Unset):
            private_key = UNSET
        elif isinstance(self.private_key, Null):
            private_key = UNSET
            if not isinstance(self.private_key, Unset):
                private_key = self.private_key.to_dict()

        else:
            private_key = self.private_key

        cert_id: Union[Dict[str, Any], Unset, str]
        if isinstance(self.cert_id, Unset):
            cert_id = UNSET
        elif isinstance(self.cert_id, Null):
            cert_id = UNSET
            if not isinstance(self.cert_id, Unset):
                cert_id = self.cert_id.to_dict()

        else:
            cert_id = self.cert_id

        use_otoroshi_certificate = self.use_otoroshi_certificate

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if certificate is not UNSET:
            field_dict["certificate"] = certificate
        if private_key is not UNSET:
            field_dict["privateKey"] = private_key
        if cert_id is not UNSET:
            field_dict["certId"] = cert_id
        if use_otoroshi_certificate is not UNSET:
            field_dict["useOtoroshiCertificate"] = use_otoroshi_certificate

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_certificate(data: object) -> Union[Null, Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _certificate_type_0 = data
                certificate_type_0: Union[Unset, Null]
                if isinstance(_certificate_type_0, Unset):
                    certificate_type_0 = UNSET
                else:
                    certificate_type_0 = Null.from_dict(_certificate_type_0)

                return certificate_type_0
            except:  # noqa: E722
                pass
            return cast(Union[Null, Unset, str], data)

        certificate = _parse_certificate(d.pop("certificate", UNSET))

        def _parse_private_key(data: object) -> Union[Null, Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _private_key_type_0 = data
                private_key_type_0: Union[Unset, Null]
                if isinstance(_private_key_type_0, Unset):
                    private_key_type_0 = UNSET
                else:
                    private_key_type_0 = Null.from_dict(_private_key_type_0)

                return private_key_type_0
            except:  # noqa: E722
                pass
            return cast(Union[Null, Unset, str], data)

        private_key = _parse_private_key(d.pop("privateKey", UNSET))

        def _parse_cert_id(data: object) -> Union[Null, Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _cert_id_type_0 = data
                cert_id_type_0: Union[Unset, Null]
                if isinstance(_cert_id_type_0, Unset):
                    cert_id_type_0 = UNSET
                else:
                    cert_id_type_0 = Null.from_dict(_cert_id_type_0)

                return cert_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[Null, Unset, str], data)

        cert_id = _parse_cert_id(d.pop("certId", UNSET))

        use_otoroshi_certificate = d.pop("useOtoroshiCertificate", UNSET)

        otoroshiauth_credential = cls(
            certificate=certificate,
            private_key=private_key,
            cert_id=cert_id,
            use_otoroshi_certificate=use_otoroshi_certificate,
        )

        otoroshiauth_credential.additional_properties = d
        return otoroshiauth_credential

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
