from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.null import Null
from ..models.otoroshiauth_basic_auth_user_metadata import OtoroshiauthBasicAuthUserMetadata
from ..models.otoroshiauth_web_authn_details import OtoroshiauthWebAuthnDetails
from ..models.otoroshimodels_user_rights import OtoroshimodelsUserRights
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshiauthBasicAuthUser")


@attr.s(auto_attribs=True)
class OtoroshiauthBasicAuthUser:
    """A user model for the BasicAuthModuleConfig module"""

    metadata: Union[Unset, OtoroshiauthBasicAuthUserMetadata] = UNSET
    password: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    webauthn: Union[Null, Union[Null, OtoroshiauthWebAuthnDetails], Unset] = UNSET
    rights: Union[Unset, OtoroshimodelsUserRights] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        password = self.password
        email = self.email
        webauthn: Union[Dict[str, Any], Unset]
        if isinstance(self.webauthn, Unset):
            webauthn = UNSET
        elif isinstance(self.webauthn, Null):
            webauthn = UNSET
            if not isinstance(self.webauthn, Unset):
                webauthn = self.webauthn.to_dict()

        else:
            webauthn
            if isinstance(self.webauthn, Unset):
                webauthn = UNSET
            elif isinstance(self.webauthn, Null):
                webauthn = UNSET
                if not isinstance(self.webauthn, Unset):
                    webauthn = self.webauthn.to_dict()

            else:
                webauthn = UNSET
                if not isinstance(self.webauthn, Unset):
                    webauthn = self.webauthn.to_dict()

        rights: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.rights, Unset):
            rights = self.rights.to_dict()

        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if password is not UNSET:
            field_dict["password"] = password
        if email is not UNSET:
            field_dict["email"] = email
        if webauthn is not UNSET:
            field_dict["webauthn"] = webauthn
        if rights is not UNSET:
            field_dict["rights"] = rights
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, OtoroshiauthBasicAuthUserMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = OtoroshiauthBasicAuthUserMetadata.from_dict(_metadata)

        password = d.pop("password", UNSET)

        email = d.pop("email", UNSET)

        def _parse_webauthn(data: object) -> Union[Null, Union[Null, OtoroshiauthWebAuthnDetails], Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _webauthn_type_0 = data
                webauthn_type_0: Union[Unset, Null]
                if isinstance(_webauthn_type_0, Unset):
                    webauthn_type_0 = UNSET
                else:
                    webauthn_type_0 = Null.from_dict(_webauthn_type_0)

                return webauthn_type_0
            except:  # noqa: E722
                pass
            if not True:
                raise TypeError()

            def _parse_webauthn_type_1(data: object) -> Union[Null, OtoroshiauthWebAuthnDetails, Unset]:
                if isinstance(data, Unset):
                    return data
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    _webauthn_type_1_type_0 = data
                    webauthn_type_1_type_0: Union[Unset, Null]
                    if isinstance(_webauthn_type_1_type_0, Unset):
                        webauthn_type_1_type_0 = UNSET
                    else:
                        webauthn_type_1_type_0 = Null.from_dict(_webauthn_type_1_type_0)

                    return webauthn_type_1_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                _webauthn_type_1_type_1 = data
                webauthn_type_1_type_1: Union[Unset, OtoroshiauthWebAuthnDetails]
                if isinstance(_webauthn_type_1_type_1, Unset):
                    webauthn_type_1_type_1 = UNSET
                else:
                    webauthn_type_1_type_1 = OtoroshiauthWebAuthnDetails.from_dict(_webauthn_type_1_type_1)

                return webauthn_type_1_type_1

            webauthn_type_1 = _parse_webauthn_type_1(data)

            return webauthn_type_1

        webauthn = _parse_webauthn(d.pop("webauthn", UNSET))

        _rights = d.pop("rights", UNSET)
        rights: Union[Unset, OtoroshimodelsUserRights]
        if isinstance(_rights, Unset):
            rights = UNSET
        else:
            rights = OtoroshimodelsUserRights.from_dict(_rights)

        name = d.pop("name", UNSET)

        otoroshiauth_basic_auth_user = cls(
            metadata=metadata,
            password=password,
            email=email,
            webauthn=webauthn,
            rights=rights,
            name=name,
        )

        otoroshiauth_basic_auth_user.additional_properties = d
        return otoroshiauth_basic_auth_user

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
