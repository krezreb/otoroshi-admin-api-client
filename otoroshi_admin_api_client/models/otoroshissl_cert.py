from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.null import Null
from ..models.otoroshimodels_entity_location import OtoroshimodelsEntityLocation
from ..models.otoroshissl_cert_entity_metadata import OtoroshisslCertEntityMetadata
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshisslCert")


@attr.s(auto_attribs=True)
class OtoroshisslCert:
    """The otoroshi model for X509 certificates"""

    lets_encrypt: Union[Unset, bool] = UNSET
    keypair: Union[Unset, bool] = UNSET
    to: Union[Unset, float] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    exposed: Union[Unset, bool] = UNSET
    auto_renew: Union[Unset, bool] = UNSET
    id: Union[Unset, str] = UNSET
    revoked: Union[Unset, bool] = UNSET
    from_: Union[Unset, float] = UNSET
    client: Union[Unset, bool] = UNSET
    ca: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    chain: Union[Unset, str] = UNSET
    location: Union[Unset, OtoroshimodelsEntityLocation] = UNSET
    password: Union[Null, Unset, str] = UNSET
    sans: Union[Unset, List[str]] = UNSET
    self_signed: Union[Unset, bool] = UNSET
    entity_metadata: Union[Unset, OtoroshisslCertEntityMetadata] = UNSET
    private_key: Union[Unset, str] = UNSET
    domain: Union[Unset, str] = UNSET
    ca_ref: Union[Null, Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    subject: Union[Unset, str] = UNSET
    valid: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        lets_encrypt = self.lets_encrypt
        keypair = self.keypair
        to = self.to
        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        exposed = self.exposed
        auto_renew = self.auto_renew
        id = self.id
        revoked = self.revoked
        from_ = self.from_
        client = self.client
        ca = self.ca
        name = self.name
        chain = self.chain
        location: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict()

        password: Union[Dict[str, Any], Unset, str]
        if isinstance(self.password, Unset):
            password = UNSET
        elif isinstance(self.password, Null):
            password = UNSET
            if not isinstance(self.password, Unset):
                password = self.password.to_dict()

        else:
            password = self.password

        sans: Union[Unset, List[str]] = UNSET
        if not isinstance(self.sans, Unset):
            sans = self.sans

        self_signed = self.self_signed
        entity_metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.entity_metadata, Unset):
            entity_metadata = self.entity_metadata.to_dict()

        private_key = self.private_key
        domain = self.domain
        ca_ref: Union[Dict[str, Any], Unset, str]
        if isinstance(self.ca_ref, Unset):
            ca_ref = UNSET
        elif isinstance(self.ca_ref, Null):
            ca_ref = UNSET
            if not isinstance(self.ca_ref, Unset):
                ca_ref = self.ca_ref.to_dict()

        else:
            ca_ref = self.ca_ref

        description = self.description
        subject = self.subject
        valid = self.valid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lets_encrypt is not UNSET:
            field_dict["letsEncrypt"] = lets_encrypt
        if keypair is not UNSET:
            field_dict["keypair"] = keypair
        if to is not UNSET:
            field_dict["to"] = to
        if tags is not UNSET:
            field_dict["tags"] = tags
        if exposed is not UNSET:
            field_dict["exposed"] = exposed
        if auto_renew is not UNSET:
            field_dict["autoRenew"] = auto_renew
        if id is not UNSET:
            field_dict["id"] = id
        if revoked is not UNSET:
            field_dict["revoked"] = revoked
        if from_ is not UNSET:
            field_dict["from"] = from_
        if client is not UNSET:
            field_dict["client"] = client
        if ca is not UNSET:
            field_dict["ca"] = ca
        if name is not UNSET:
            field_dict["name"] = name
        if chain is not UNSET:
            field_dict["chain"] = chain
        if location is not UNSET:
            field_dict["location"] = location
        if password is not UNSET:
            field_dict["password"] = password
        if sans is not UNSET:
            field_dict["sans"] = sans
        if self_signed is not UNSET:
            field_dict["selfSigned"] = self_signed
        if entity_metadata is not UNSET:
            field_dict["entityMetadata"] = entity_metadata
        if private_key is not UNSET:
            field_dict["privateKey"] = private_key
        if domain is not UNSET:
            field_dict["domain"] = domain
        if ca_ref is not UNSET:
            field_dict["caRef"] = ca_ref
        if description is not UNSET:
            field_dict["description"] = description
        if subject is not UNSET:
            field_dict["subject"] = subject
        if valid is not UNSET:
            field_dict["valid"] = valid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        lets_encrypt = d.pop("letsEncrypt", UNSET)

        keypair = d.pop("keypair", UNSET)

        to = d.pop("to", UNSET)

        tags = cast(List[str], d.pop("tags", UNSET))

        exposed = d.pop("exposed", UNSET)

        auto_renew = d.pop("autoRenew", UNSET)

        id = d.pop("id", UNSET)

        revoked = d.pop("revoked", UNSET)

        from_ = d.pop("from", UNSET)

        client = d.pop("client", UNSET)

        ca = d.pop("ca", UNSET)

        name = d.pop("name", UNSET)

        chain = d.pop("chain", UNSET)

        _location = d.pop("location", UNSET)
        location: Union[Unset, OtoroshimodelsEntityLocation]
        if isinstance(_location, Unset):
            location = UNSET
        else:
            location = OtoroshimodelsEntityLocation.from_dict(_location)

        def _parse_password(data: object) -> Union[Null, Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _password_type_0 = data
                password_type_0: Union[Unset, Null]
                if isinstance(_password_type_0, Unset):
                    password_type_0 = UNSET
                else:
                    password_type_0 = Null.from_dict(_password_type_0)

                return password_type_0
            except:  # noqa: E722
                pass
            return cast(Union[Null, Unset, str], data)

        password = _parse_password(d.pop("password", UNSET))

        sans = cast(List[str], d.pop("sans", UNSET))

        self_signed = d.pop("selfSigned", UNSET)

        _entity_metadata = d.pop("entityMetadata", UNSET)
        entity_metadata: Union[Unset, OtoroshisslCertEntityMetadata]
        if isinstance(_entity_metadata, Unset):
            entity_metadata = UNSET
        else:
            entity_metadata = OtoroshisslCertEntityMetadata.from_dict(_entity_metadata)

        private_key = d.pop("privateKey", UNSET)

        domain = d.pop("domain", UNSET)

        def _parse_ca_ref(data: object) -> Union[Null, Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _ca_ref_type_0 = data
                ca_ref_type_0: Union[Unset, Null]
                if isinstance(_ca_ref_type_0, Unset):
                    ca_ref_type_0 = UNSET
                else:
                    ca_ref_type_0 = Null.from_dict(_ca_ref_type_0)

                return ca_ref_type_0
            except:  # noqa: E722
                pass
            return cast(Union[Null, Unset, str], data)

        ca_ref = _parse_ca_ref(d.pop("caRef", UNSET))

        description = d.pop("description", UNSET)

        subject = d.pop("subject", UNSET)

        valid = d.pop("valid", UNSET)

        otoroshissl_cert = cls(
            lets_encrypt=lets_encrypt,
            keypair=keypair,
            to=to,
            tags=tags,
            exposed=exposed,
            auto_renew=auto_renew,
            id=id,
            revoked=revoked,
            from_=from_,
            client=client,
            ca=ca,
            name=name,
            chain=chain,
            location=location,
            password=password,
            sans=sans,
            self_signed=self_signed,
            entity_metadata=entity_metadata,
            private_key=private_key,
            domain=domain,
            ca_ref=ca_ref,
            description=description,
            subject=subject,
            valid=valid,
        )

        otoroshissl_cert.additional_properties = d
        return otoroshissl_cert

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
