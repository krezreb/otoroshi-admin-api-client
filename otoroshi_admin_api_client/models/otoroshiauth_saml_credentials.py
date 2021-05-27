from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.otoroshiauth_credential import OtoroshiauthCredential
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshiauthSAMLCredentials")


@attr.s(auto_attribs=True)
class OtoroshiauthSAMLCredentials:
    """Used to sign, encrypt assertions and sign SAML documents"""

    signing_key: Union[Unset, OtoroshiauthCredential] = UNSET
    encryption_key: Union[Unset, OtoroshiauthCredential] = UNSET
    signed_documents: Union[Unset, bool] = UNSET
    encrypted_assertions: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        signing_key: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.signing_key, Unset):
            signing_key = self.signing_key.to_dict()

        encryption_key: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.encryption_key, Unset):
            encryption_key = self.encryption_key.to_dict()

        signed_documents = self.signed_documents
        encrypted_assertions = self.encrypted_assertions

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if signing_key is not UNSET:
            field_dict["signingKey"] = signing_key
        if encryption_key is not UNSET:
            field_dict["encryptionKey"] = encryption_key
        if signed_documents is not UNSET:
            field_dict["signedDocuments"] = signed_documents
        if encrypted_assertions is not UNSET:
            field_dict["encryptedAssertions"] = encrypted_assertions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _signing_key = d.pop("signingKey", UNSET)
        signing_key: Union[Unset, OtoroshiauthCredential]
        if isinstance(_signing_key, Unset):
            signing_key = UNSET
        else:
            signing_key = OtoroshiauthCredential.from_dict(_signing_key)

        _encryption_key = d.pop("encryptionKey", UNSET)
        encryption_key: Union[Unset, OtoroshiauthCredential]
        if isinstance(_encryption_key, Unset):
            encryption_key = UNSET
        else:
            encryption_key = OtoroshiauthCredential.from_dict(_encryption_key)

        signed_documents = d.pop("signedDocuments", UNSET)

        encrypted_assertions = d.pop("encryptedAssertions", UNSET)

        otoroshiauth_saml_credentials = cls(
            signing_key=signing_key,
            encryption_key=encryption_key,
            signed_documents=signed_documents,
            encrypted_assertions=encrypted_assertions,
        )

        otoroshiauth_saml_credentials.additional_properties = d
        return otoroshiauth_saml_credentials

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
