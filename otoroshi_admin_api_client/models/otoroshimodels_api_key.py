from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.null import Null
from ..models.otoroshimodels_api_key_metadata import OtoroshimodelsApiKeyMetadata
from ..models.otoroshimodels_api_key_rotation import OtoroshimodelsApiKeyRotation
from ..models.otoroshimodels_entity_location import OtoroshimodelsEntityLocation
from ..models.otoroshimodels_restrictions import OtoroshimodelsRestrictions
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshimodelsApiKey")


@attr.s(auto_attribs=True)
class OtoroshimodelsApiKey:
    """An otoroshi apikey that can allow you to access some services"""

    daily_quota: Union[Unset, int] = UNSET
    metadata: Union[Unset, OtoroshimodelsApiKeyMetadata] = UNSET
    throttling_quota: Union[Unset, int] = UNSET
    constrained_services_only: Union[Unset, bool] = UNSET
    allow_client_id_only: Union[Unset, bool] = UNSET
    location: Union[Unset, OtoroshimodelsEntityLocation] = UNSET
    restrictions: Union[Unset, OtoroshimodelsRestrictions] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    enabled: Union[Unset, bool] = UNSET
    read_only: Union[Unset, bool] = UNSET
    client_secret: Union[Unset, str] = UNSET
    valid_until: Union[Null, Unset, float] = UNSET
    client_name: Union[Unset, str] = UNSET
    monthly_quota: Union[Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    rotation: Union[Unset, OtoroshimodelsApiKeyRotation] = UNSET
    authorized_entities: Union[Unset, List[str]] = UNSET
    client_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        daily_quota = self.daily_quota
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        throttling_quota = self.throttling_quota
        constrained_services_only = self.constrained_services_only
        allow_client_id_only = self.allow_client_id_only
        location: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict()

        restrictions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.restrictions, Unset):
            restrictions = self.restrictions.to_dict()

        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        enabled = self.enabled
        read_only = self.read_only
        client_secret = self.client_secret
        valid_until: Union[Dict[str, Any], Unset, float]
        if isinstance(self.valid_until, Unset):
            valid_until = UNSET
        elif isinstance(self.valid_until, Null):
            valid_until = UNSET
            if not isinstance(self.valid_until, Unset):
                valid_until = self.valid_until.to_dict()

        else:
            valid_until = self.valid_until

        client_name = self.client_name
        monthly_quota = self.monthly_quota
        description = self.description
        rotation: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.rotation, Unset):
            rotation = self.rotation.to_dict()

        authorized_entities: Union[Unset, List[str]] = UNSET
        if not isinstance(self.authorized_entities, Unset):
            authorized_entities = []
            for authorized_entities_item_data in self.authorized_entities:
                authorized_entities_item = authorized_entities_item_data

                authorized_entities.append(authorized_entities_item)

        client_id = self.client_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if daily_quota is not UNSET:
            field_dict["dailyQuota"] = daily_quota
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if throttling_quota is not UNSET:
            field_dict["throttlingQuota"] = throttling_quota
        if constrained_services_only is not UNSET:
            field_dict["constrainedServicesOnly"] = constrained_services_only
        if allow_client_id_only is not UNSET:
            field_dict["allowClientIdOnly"] = allow_client_id_only
        if location is not UNSET:
            field_dict["location"] = location
        if restrictions is not UNSET:
            field_dict["restrictions"] = restrictions
        if tags is not UNSET:
            field_dict["tags"] = tags
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if read_only is not UNSET:
            field_dict["readOnly"] = read_only
        if client_secret is not UNSET:
            field_dict["clientSecret"] = client_secret
        if valid_until is not UNSET:
            field_dict["validUntil"] = valid_until
        if client_name is not UNSET:
            field_dict["clientName"] = client_name
        if monthly_quota is not UNSET:
            field_dict["monthlyQuota"] = monthly_quota
        if description is not UNSET:
            field_dict["description"] = description
        if rotation is not UNSET:
            field_dict["rotation"] = rotation
        if authorized_entities is not UNSET:
            field_dict["authorizedEntities"] = authorized_entities
        if client_id is not UNSET:
            field_dict["clientId"] = client_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        daily_quota = d.pop("dailyQuota", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, OtoroshimodelsApiKeyMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = OtoroshimodelsApiKeyMetadata.from_dict(_metadata)

        throttling_quota = d.pop("throttlingQuota", UNSET)

        constrained_services_only = d.pop("constrainedServicesOnly", UNSET)

        allow_client_id_only = d.pop("allowClientIdOnly", UNSET)

        _location = d.pop("location", UNSET)
        location: Union[Unset, OtoroshimodelsEntityLocation]
        if isinstance(_location, Unset):
            location = UNSET
        else:
            location = OtoroshimodelsEntityLocation.from_dict(_location)

        _restrictions = d.pop("restrictions", UNSET)
        restrictions: Union[Unset, OtoroshimodelsRestrictions]
        if isinstance(_restrictions, Unset):
            restrictions = UNSET
        else:
            restrictions = OtoroshimodelsRestrictions.from_dict(_restrictions)

        tags = cast(List[str], d.pop("tags", UNSET))

        enabled = d.pop("enabled", UNSET)

        read_only = d.pop("readOnly", UNSET)

        client_secret = d.pop("clientSecret", UNSET)

        def _parse_valid_until(data: object) -> Union[Null, Unset, float]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _valid_until_type_0 = data
                valid_until_type_0: Union[Unset, Null]
                if isinstance(_valid_until_type_0, Unset):
                    valid_until_type_0 = UNSET
                else:
                    valid_until_type_0 = Null.from_dict(_valid_until_type_0)

                return valid_until_type_0
            except:  # noqa: E722
                pass
            return cast(Union[Null, Unset, float], data)

        valid_until = _parse_valid_until(d.pop("validUntil", UNSET))

        client_name = d.pop("clientName", UNSET)

        monthly_quota = d.pop("monthlyQuota", UNSET)

        description = d.pop("description", UNSET)

        _rotation = d.pop("rotation", UNSET)
        rotation: Union[Unset, OtoroshimodelsApiKeyRotation]
        if isinstance(_rotation, Unset):
            rotation = UNSET
        else:
            rotation = OtoroshimodelsApiKeyRotation.from_dict(_rotation)

        authorized_entities = []
        _authorized_entities = d.pop("authorizedEntities", UNSET)
        for authorized_entities_item_data in _authorized_entities or []:

            def _parse_authorized_entities_item(data: object) -> str:
                return cast(str, data)

            authorized_entities_item = _parse_authorized_entities_item(authorized_entities_item_data)

            authorized_entities.append(authorized_entities_item)

        client_id = d.pop("clientId", UNSET)

        otoroshimodels_api_key = cls(
            daily_quota=daily_quota,
            metadata=metadata,
            throttling_quota=throttling_quota,
            constrained_services_only=constrained_services_only,
            allow_client_id_only=allow_client_id_only,
            location=location,
            restrictions=restrictions,
            tags=tags,
            enabled=enabled,
            read_only=read_only,
            client_secret=client_secret,
            valid_until=valid_until,
            client_name=client_name,
            monthly_quota=monthly_quota,
            description=description,
            rotation=rotation,
            authorized_entities=authorized_entities,
            client_id=client_id,
        )

        otoroshimodels_api_key.additional_properties = d
        return otoroshimodels_api_key

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
