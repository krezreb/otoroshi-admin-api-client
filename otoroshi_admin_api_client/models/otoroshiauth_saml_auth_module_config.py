from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.null import Null
from ..models.otoroshiauth_name_id_format import OtoroshiauthNameIDFormat
from ..models.otoroshiauth_saml_auth_module_config_metadata import OtoroshiauthSamlAuthModuleConfigMetadata
from ..models.otoroshiauth_saml_auth_module_config_type import OtoroshiauthSamlAuthModuleConfigType
from ..models.otoroshiauth_saml_credentials import OtoroshiauthSAMLCredentials
from ..models.otoroshiauth_saml_protocol_binding import OtoroshiauthSAMLProtocolBinding
from ..models.otoroshiauth_saml_signature import OtoroshiauthSAMLSignature
from ..models.otoroshiauth_session_cookie_values import OtoroshiauthSessionCookieValues
from ..models.otoroshimodels_entity_location import OtoroshimodelsEntityLocation
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshiauthSamlAuthModuleConfig")


@attr.s(auto_attribs=True)
class OtoroshiauthSamlAuthModuleConfig:
    """Configuration of SAML Authentication module"""

    validate_signature: Union[Unset, bool] = UNSET
    metadata: Union[Unset, OtoroshiauthSamlAuthModuleConfigMetadata] = UNSET
    sso_protocol_binding: Union[Unset, OtoroshiauthSAMLProtocolBinding] = UNSET
    session_cookie_values: Union[Unset, OtoroshiauthSessionCookieValues] = UNSET
    validating_certificates: Union[Unset, List[str]] = UNSET
    signature: Union[Unset, OtoroshiauthSAMLSignature] = UNSET
    credentials: Union[Unset, OtoroshiauthSAMLCredentials] = UNSET
    validate_assertions: Union[Unset, bool] = UNSET
    type: Union[Unset, OtoroshiauthSamlAuthModuleConfigType] = UNSET
    issuer: Union[Unset, str] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    session_max_age: Union[Unset, int] = UNSET
    used_name_id_as_email: Union[Unset, bool] = UNSET
    single_logout_url: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    email_attribute_name: Union[Null, Unset, str] = UNSET
    single_sign_on_url: Union[Unset, str] = UNSET
    name_id_format: Union[Unset, OtoroshiauthNameIDFormat] = UNSET
    location: Union[Unset, OtoroshimodelsEntityLocation] = UNSET
    single_logout_protocol_binding: Union[Unset, OtoroshiauthSAMLProtocolBinding] = UNSET
    id: Union[Unset, str] = UNSET
    desc: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        validate_signature = self.validate_signature
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        sso_protocol_binding: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sso_protocol_binding, Unset):
            sso_protocol_binding = self.sso_protocol_binding.to_dict()

        session_cookie_values: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.session_cookie_values, Unset):
            session_cookie_values = self.session_cookie_values.to_dict()

        validating_certificates: Union[Unset, List[str]] = UNSET
        if not isinstance(self.validating_certificates, Unset):
            validating_certificates = self.validating_certificates

        signature: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.signature, Unset):
            signature = self.signature.to_dict()

        credentials: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.credentials, Unset):
            credentials = self.credentials.to_dict()

        validate_assertions = self.validate_assertions
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        issuer = self.issuer
        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        session_max_age = self.session_max_age
        used_name_id_as_email = self.used_name_id_as_email
        single_logout_url = self.single_logout_url
        name = self.name
        email_attribute_name: Union[Dict[str, Any], Unset, str]
        if isinstance(self.email_attribute_name, Unset):
            email_attribute_name = UNSET
        elif isinstance(self.email_attribute_name, Null):
            email_attribute_name = UNSET
            if not isinstance(self.email_attribute_name, Unset):
                email_attribute_name = self.email_attribute_name.to_dict()

        else:
            email_attribute_name = self.email_attribute_name

        single_sign_on_url = self.single_sign_on_url
        name_id_format: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.name_id_format, Unset):
            name_id_format = self.name_id_format.to_dict()

        location: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict()

        single_logout_protocol_binding: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.single_logout_protocol_binding, Unset):
            single_logout_protocol_binding = self.single_logout_protocol_binding.to_dict()

        id = self.id
        desc = self.desc

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if validate_signature is not UNSET:
            field_dict["validateSignature"] = validate_signature
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if sso_protocol_binding is not UNSET:
            field_dict["ssoProtocolBinding"] = sso_protocol_binding
        if session_cookie_values is not UNSET:
            field_dict["sessionCookieValues"] = session_cookie_values
        if validating_certificates is not UNSET:
            field_dict["validatingCertificates"] = validating_certificates
        if signature is not UNSET:
            field_dict["signature"] = signature
        if credentials is not UNSET:
            field_dict["credentials"] = credentials
        if validate_assertions is not UNSET:
            field_dict["validateAssertions"] = validate_assertions
        if type is not UNSET:
            field_dict["type"] = type
        if issuer is not UNSET:
            field_dict["issuer"] = issuer
        if tags is not UNSET:
            field_dict["tags"] = tags
        if session_max_age is not UNSET:
            field_dict["sessionMaxAge"] = session_max_age
        if used_name_id_as_email is not UNSET:
            field_dict["usedNameIDAsEmail"] = used_name_id_as_email
        if single_logout_url is not UNSET:
            field_dict["singleLogoutUrl"] = single_logout_url
        if name is not UNSET:
            field_dict["name"] = name
        if email_attribute_name is not UNSET:
            field_dict["emailAttributeName"] = email_attribute_name
        if single_sign_on_url is not UNSET:
            field_dict["singleSignOnUrl"] = single_sign_on_url
        if name_id_format is not UNSET:
            field_dict["nameIDFormat"] = name_id_format
        if location is not UNSET:
            field_dict["location"] = location
        if single_logout_protocol_binding is not UNSET:
            field_dict["singleLogoutProtocolBinding"] = single_logout_protocol_binding
        if id is not UNSET:
            field_dict["id"] = id
        if desc is not UNSET:
            field_dict["desc"] = desc

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        validate_signature = d.pop("validateSignature", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, OtoroshiauthSamlAuthModuleConfigMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = OtoroshiauthSamlAuthModuleConfigMetadata.from_dict(_metadata)

        _sso_protocol_binding = d.pop("ssoProtocolBinding", UNSET)
        sso_protocol_binding: Union[Unset, OtoroshiauthSAMLProtocolBinding]
        if isinstance(_sso_protocol_binding, Unset):
            sso_protocol_binding = UNSET
        else:
            sso_protocol_binding = OtoroshiauthSAMLProtocolBinding.from_dict(_sso_protocol_binding)

        _session_cookie_values = d.pop("sessionCookieValues", UNSET)
        session_cookie_values: Union[Unset, OtoroshiauthSessionCookieValues]
        if isinstance(_session_cookie_values, Unset):
            session_cookie_values = UNSET
        else:
            session_cookie_values = OtoroshiauthSessionCookieValues.from_dict(_session_cookie_values)

        validating_certificates = cast(List[str], d.pop("validatingCertificates", UNSET))

        _signature = d.pop("signature", UNSET)
        signature: Union[Unset, OtoroshiauthSAMLSignature]
        if isinstance(_signature, Unset):
            signature = UNSET
        else:
            signature = OtoroshiauthSAMLSignature.from_dict(_signature)

        _credentials = d.pop("credentials", UNSET)
        credentials: Union[Unset, OtoroshiauthSAMLCredentials]
        if isinstance(_credentials, Unset):
            credentials = UNSET
        else:
            credentials = OtoroshiauthSAMLCredentials.from_dict(_credentials)

        validate_assertions = d.pop("validateAssertions", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, OtoroshiauthSamlAuthModuleConfigType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = OtoroshiauthSamlAuthModuleConfigType(_type)

        issuer = d.pop("issuer", UNSET)

        tags = cast(List[str], d.pop("tags", UNSET))

        session_max_age = d.pop("sessionMaxAge", UNSET)

        used_name_id_as_email = d.pop("usedNameIDAsEmail", UNSET)

        single_logout_url = d.pop("singleLogoutUrl", UNSET)

        name = d.pop("name", UNSET)

        def _parse_email_attribute_name(data: object) -> Union[Null, Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _email_attribute_name_type_0 = data
                email_attribute_name_type_0: Union[Unset, Null]
                if isinstance(_email_attribute_name_type_0, Unset):
                    email_attribute_name_type_0 = UNSET
                else:
                    email_attribute_name_type_0 = Null.from_dict(_email_attribute_name_type_0)

                return email_attribute_name_type_0
            except:  # noqa: E722
                pass
            return cast(Union[Null, Unset, str], data)

        email_attribute_name = _parse_email_attribute_name(d.pop("emailAttributeName", UNSET))

        single_sign_on_url = d.pop("singleSignOnUrl", UNSET)

        _name_id_format = d.pop("nameIDFormat", UNSET)
        name_id_format: Union[Unset, OtoroshiauthNameIDFormat]
        if isinstance(_name_id_format, Unset):
            name_id_format = UNSET
        else:
            name_id_format = OtoroshiauthNameIDFormat.from_dict(_name_id_format)

        _location = d.pop("location", UNSET)
        location: Union[Unset, OtoroshimodelsEntityLocation]
        if isinstance(_location, Unset):
            location = UNSET
        else:
            location = OtoroshimodelsEntityLocation.from_dict(_location)

        _single_logout_protocol_binding = d.pop("singleLogoutProtocolBinding", UNSET)
        single_logout_protocol_binding: Union[Unset, OtoroshiauthSAMLProtocolBinding]
        if isinstance(_single_logout_protocol_binding, Unset):
            single_logout_protocol_binding = UNSET
        else:
            single_logout_protocol_binding = OtoroshiauthSAMLProtocolBinding.from_dict(_single_logout_protocol_binding)

        id = d.pop("id", UNSET)

        desc = d.pop("desc", UNSET)

        otoroshiauth_saml_auth_module_config = cls(
            validate_signature=validate_signature,
            metadata=metadata,
            sso_protocol_binding=sso_protocol_binding,
            session_cookie_values=session_cookie_values,
            validating_certificates=validating_certificates,
            signature=signature,
            credentials=credentials,
            validate_assertions=validate_assertions,
            type=type,
            issuer=issuer,
            tags=tags,
            session_max_age=session_max_age,
            used_name_id_as_email=used_name_id_as_email,
            single_logout_url=single_logout_url,
            name=name,
            email_attribute_name=email_attribute_name,
            single_sign_on_url=single_sign_on_url,
            name_id_format=name_id_format,
            location=location,
            single_logout_protocol_binding=single_logout_protocol_binding,
            id=id,
            desc=desc,
        )

        otoroshiauth_saml_auth_module_config.additional_properties = d
        return otoroshiauth_saml_auth_module_config

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
