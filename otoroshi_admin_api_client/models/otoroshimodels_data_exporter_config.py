from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.null import Null
from ..models.otoroshievents_kafka_config import OtoroshieventsKafkaConfig
from ..models.otoroshievents_pulsar_config import OtoroshieventsPulsarConfig
from ..models.otoroshimodels_console_settings import OtoroshimodelsConsoleSettings
from ..models.otoroshimodels_data_exporter_config_filtering import OtoroshimodelsDataExporterConfigFiltering
from ..models.otoroshimodels_data_exporter_config_metadata import OtoroshimodelsDataExporterConfigMetadata
from ..models.otoroshimodels_data_exporter_config_projection import OtoroshimodelsDataExporterConfigProjection
from ..models.otoroshimodels_data_exporter_config_type import OtoroshimodelsDataExporterConfigType
from ..models.otoroshimodels_elastic_analytics_config import OtoroshimodelsElasticAnalyticsConfig
from ..models.otoroshimodels_entity_location import OtoroshimodelsEntityLocation
from ..models.otoroshimodels_exporter_ref import OtoroshimodelsExporterRef
from ..models.otoroshimodels_file_settings import OtoroshimodelsFileSettings
from ..models.otoroshimodels_metrics_settings import OtoroshimodelsMetricsSettings
from ..models.otoroshimodels_webhook import OtoroshimodelsWebhook
from ..models.otoroshiutilsmailer_console_mailer_settings import OtoroshiutilsmailerConsoleMailerSettings
from ..models.otoroshiutilsmailer_generic_mailer_settings import OtoroshiutilsmailerGenericMailerSettings
from ..models.otoroshiutilsmailer_mailgun_settings import OtoroshiutilsmailerMailgunSettings
from ..models.otoroshiutilsmailer_mailjet_settings import OtoroshiutilsmailerMailjetSettings
from ..models.otoroshiutilsmailer_none_mailer_settings import OtoroshiutilsmailerNoneMailerSettings
from ..models.otoroshiutilsmailer_sendgrid_settings import OtoroshiutilsmailerSendgridSettings
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshimodelsDataExporterConfig")


@attr.s(auto_attribs=True)
class OtoroshimodelsDataExporterConfig:
    """Module to export otoroshi specific events to whatever destination you want"""

    desc: Union[Unset, str] = UNSET
    location: Union[Unset, OtoroshimodelsEntityLocation] = UNSET
    buffer_size: Union[Unset, int] = UNSET
    json_workers: Union[Unset, int] = UNSET
    group_duration: Union[Unset, float] = UNSET
    group_size: Union[Unset, int] = UNSET
    typ: Union[Unset, OtoroshimodelsDataExporterConfigType] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    send_workers: Union[Unset, int] = UNSET
    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    metadata: Union[Unset, OtoroshimodelsDataExporterConfigMetadata] = UNSET
    config: Union[
        Null,
        OtoroshieventsKafkaConfig,
        OtoroshieventsPulsarConfig,
        OtoroshimodelsConsoleSettings,
        OtoroshimodelsElasticAnalyticsConfig,
        OtoroshimodelsExporterRef,
        OtoroshimodelsFileSettings,
        OtoroshimodelsMetricsSettings,
        OtoroshimodelsWebhook,
        OtoroshiutilsmailerConsoleMailerSettings,
        OtoroshiutilsmailerGenericMailerSettings,
        OtoroshiutilsmailerMailgunSettings,
        OtoroshiutilsmailerMailjetSettings,
        OtoroshiutilsmailerNoneMailerSettings,
        OtoroshiutilsmailerSendgridSettings,
        Union[
            OtoroshiutilsmailerConsoleMailerSettings,
            OtoroshiutilsmailerGenericMailerSettings,
            OtoroshiutilsmailerMailgunSettings,
            OtoroshiutilsmailerMailjetSettings,
            OtoroshiutilsmailerNoneMailerSettings,
            OtoroshiutilsmailerSendgridSettings,
        ],
        Unset,
    ] = UNSET
    projection: Union[Unset, OtoroshimodelsDataExporterConfigProjection] = UNSET
    enabled: Union[Unset, bool] = UNSET
    filtering: Union[Unset, OtoroshimodelsDataExporterConfigFiltering] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        desc = self.desc
        location: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict()

        buffer_size = self.buffer_size
        json_workers = self.json_workers
        group_duration = self.group_duration
        group_size = self.group_size
        typ: Union[Unset, str] = UNSET
        if not isinstance(self.typ, Unset):
            typ = self.typ.value

        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        send_workers = self.send_workers
        id = self.id
        name = self.name
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        config: Union[Dict[str, Any], Unset]
        if isinstance(self.config, Unset):
            config = UNSET
        elif isinstance(self.config, OtoroshieventsKafkaConfig):
            config = self.config.to_dict()

        elif isinstance(self.config, OtoroshieventsPulsarConfig):
            config = self.config.to_dict()

        elif isinstance(self.config, OtoroshimodelsConsoleSettings):
            config = self.config.to_dict()

        elif isinstance(self.config, OtoroshimodelsElasticAnalyticsConfig):
            config = self.config.to_dict()

        elif isinstance(self.config, Null):
            config = self.config.to_dict()

        elif isinstance(self.config, OtoroshimodelsExporterRef):
            config = self.config.to_dict()

        elif isinstance(self.config, OtoroshimodelsFileSettings):
            config = self.config.to_dict()

        elif isinstance(self.config, OtoroshimodelsMetricsSettings):
            config = self.config.to_dict()

        elif isinstance(self.config, OtoroshimodelsWebhook):
            config = self.config.to_dict()

        elif isinstance(self.config, OtoroshiutilsmailerConsoleMailerSettings):
            config = self.config.to_dict()

        elif isinstance(self.config, OtoroshiutilsmailerGenericMailerSettings):
            config = self.config.to_dict()

        elif isinstance(
            self.config,
            Union[
                OtoroshiutilsmailerConsoleMailerSettings,
                OtoroshiutilsmailerGenericMailerSettings,
                OtoroshiutilsmailerMailgunSettings,
                OtoroshiutilsmailerMailjetSettings,
                OtoroshiutilsmailerNoneMailerSettings,
                OtoroshiutilsmailerSendgridSettings,
            ],
        ):
            if isinstance(self.config, OtoroshiutilsmailerConsoleMailerSettings):
                config = self.config.to_dict()

            elif isinstance(self.config, OtoroshiutilsmailerGenericMailerSettings):
                config = self.config.to_dict()

            elif isinstance(self.config, OtoroshiutilsmailerMailgunSettings):
                config = self.config.to_dict()

            elif isinstance(self.config, OtoroshiutilsmailerMailjetSettings):
                config = self.config.to_dict()

            elif isinstance(self.config, OtoroshiutilsmailerNoneMailerSettings):
                config = self.config.to_dict()

            else:
                config = self.config.to_dict()

        elif isinstance(self.config, OtoroshiutilsmailerMailgunSettings):
            config = self.config.to_dict()

        elif isinstance(self.config, OtoroshiutilsmailerMailjetSettings):
            config = self.config.to_dict()

        elif isinstance(self.config, OtoroshiutilsmailerNoneMailerSettings):
            config = self.config.to_dict()

        else:
            config = self.config.to_dict()

        projection: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.projection, Unset):
            projection = self.projection.to_dict()

        enabled = self.enabled
        filtering: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.filtering, Unset):
            filtering = self.filtering.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if desc is not UNSET:
            field_dict["desc"] = desc
        if location is not UNSET:
            field_dict["location"] = location
        if buffer_size is not UNSET:
            field_dict["bufferSize"] = buffer_size
        if json_workers is not UNSET:
            field_dict["jsonWorkers"] = json_workers
        if group_duration is not UNSET:
            field_dict["groupDuration"] = group_duration
        if group_size is not UNSET:
            field_dict["groupSize"] = group_size
        if typ is not UNSET:
            field_dict["typ"] = typ
        if tags is not UNSET:
            field_dict["tags"] = tags
        if send_workers is not UNSET:
            field_dict["sendWorkers"] = send_workers
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if config is not UNSET:
            field_dict["config"] = config
        if projection is not UNSET:
            field_dict["projection"] = projection
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if filtering is not UNSET:
            field_dict["filtering"] = filtering

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        desc = d.pop("desc", UNSET)

        _location = d.pop("location", UNSET)
        location: Union[Unset, OtoroshimodelsEntityLocation]
        if isinstance(_location, Unset):
            location = UNSET
        else:
            location = OtoroshimodelsEntityLocation.from_dict(_location)

        buffer_size = d.pop("bufferSize", UNSET)

        json_workers = d.pop("jsonWorkers", UNSET)

        group_duration = d.pop("groupDuration", UNSET)

        group_size = d.pop("groupSize", UNSET)

        _typ = d.pop("typ", UNSET)
        typ: Union[Unset, OtoroshimodelsDataExporterConfigType]
        if isinstance(_typ, Unset):
            typ = UNSET
        else:
            typ = OtoroshimodelsDataExporterConfigType(_typ)

        tags = cast(List[str], d.pop("tags", UNSET))

        send_workers = d.pop("sendWorkers", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, OtoroshimodelsDataExporterConfigMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = OtoroshimodelsDataExporterConfigMetadata.from_dict(_metadata)

        def _parse_config(
            data: object,
        ) -> Union[
            Null,
            OtoroshieventsKafkaConfig,
            OtoroshieventsPulsarConfig,
            OtoroshimodelsConsoleSettings,
            OtoroshimodelsElasticAnalyticsConfig,
            OtoroshimodelsExporterRef,
            OtoroshimodelsFileSettings,
            OtoroshimodelsMetricsSettings,
            OtoroshimodelsWebhook,
            OtoroshiutilsmailerConsoleMailerSettings,
            OtoroshiutilsmailerGenericMailerSettings,
            OtoroshiutilsmailerMailgunSettings,
            OtoroshiutilsmailerMailjetSettings,
            OtoroshiutilsmailerNoneMailerSettings,
            OtoroshiutilsmailerSendgridSettings,
            Union[
                OtoroshiutilsmailerConsoleMailerSettings,
                OtoroshiutilsmailerGenericMailerSettings,
                OtoroshiutilsmailerMailgunSettings,
                OtoroshiutilsmailerMailjetSettings,
                OtoroshiutilsmailerNoneMailerSettings,
                OtoroshiutilsmailerSendgridSettings,
            ],
            Unset,
        ]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasotoroshimodels_exporter_type_0 = OtoroshieventsKafkaConfig.from_dict(data)

                return componentsschemasotoroshimodels_exporter_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasotoroshimodels_exporter_type_1 = OtoroshieventsPulsarConfig.from_dict(data)

                return componentsschemasotoroshimodels_exporter_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasotoroshimodels_exporter_type_2 = OtoroshimodelsConsoleSettings.from_dict(data)

                return componentsschemasotoroshimodels_exporter_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasotoroshimodels_exporter_type_3 = OtoroshimodelsElasticAnalyticsConfig.from_dict(data)

                return componentsschemasotoroshimodels_exporter_type_3
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasotoroshimodels_exporter_type_4 = Null.from_dict(data)

                return componentsschemasotoroshimodels_exporter_type_4
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasotoroshimodels_exporter_type_5 = OtoroshimodelsExporterRef.from_dict(data)

                return componentsschemasotoroshimodels_exporter_type_5
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasotoroshimodels_exporter_type_6 = OtoroshimodelsFileSettings.from_dict(data)

                return componentsschemasotoroshimodels_exporter_type_6
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasotoroshimodels_exporter_type_7 = OtoroshimodelsMetricsSettings.from_dict(data)

                return componentsschemasotoroshimodels_exporter_type_7
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasotoroshimodels_exporter_type_8 = OtoroshimodelsWebhook.from_dict(data)

                return componentsschemasotoroshimodels_exporter_type_8
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasotoroshimodels_exporter_type_9 = OtoroshiutilsmailerConsoleMailerSettings.from_dict(
                    data
                )

                return componentsschemasotoroshimodels_exporter_type_9
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasotoroshimodels_exporter_type_10 = OtoroshiutilsmailerGenericMailerSettings.from_dict(
                    data
                )

                return componentsschemasotoroshimodels_exporter_type_10
            except:  # noqa: E722
                pass
            try:
                if not True:
                    raise TypeError()

                def _parse_componentsschemasotoroshimodels_exporter_type_11(
                    data: object,
                ) -> Union[
                    OtoroshiutilsmailerConsoleMailerSettings,
                    OtoroshiutilsmailerGenericMailerSettings,
                    OtoroshiutilsmailerMailgunSettings,
                    OtoroshiutilsmailerMailjetSettings,
                    OtoroshiutilsmailerNoneMailerSettings,
                    OtoroshiutilsmailerSendgridSettings,
                ]:
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemasotoroshiutilsmailer_mailer_settings_type_0 = (
                            OtoroshiutilsmailerConsoleMailerSettings.from_dict(data)
                        )

                        return componentsschemasotoroshiutilsmailer_mailer_settings_type_0
                    except:  # noqa: E722
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemasotoroshiutilsmailer_mailer_settings_type_1 = (
                            OtoroshiutilsmailerGenericMailerSettings.from_dict(data)
                        )

                        return componentsschemasotoroshiutilsmailer_mailer_settings_type_1
                    except:  # noqa: E722
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemasotoroshiutilsmailer_mailer_settings_type_2 = (
                            OtoroshiutilsmailerMailgunSettings.from_dict(data)
                        )

                        return componentsschemasotoroshiutilsmailer_mailer_settings_type_2
                    except:  # noqa: E722
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemasotoroshiutilsmailer_mailer_settings_type_3 = (
                            OtoroshiutilsmailerMailjetSettings.from_dict(data)
                        )

                        return componentsschemasotoroshiutilsmailer_mailer_settings_type_3
                    except:  # noqa: E722
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemasotoroshiutilsmailer_mailer_settings_type_4 = (
                            OtoroshiutilsmailerNoneMailerSettings.from_dict(data)
                        )

                        return componentsschemasotoroshiutilsmailer_mailer_settings_type_4
                    except:  # noqa: E722
                        pass
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemasotoroshiutilsmailer_mailer_settings_type_5 = (
                        OtoroshiutilsmailerSendgridSettings.from_dict(data)
                    )

                    return componentsschemasotoroshiutilsmailer_mailer_settings_type_5

                componentsschemasotoroshimodels_exporter_type_11 = (
                    _parse_componentsschemasotoroshimodels_exporter_type_11(data)
                )

                return componentsschemasotoroshimodels_exporter_type_11
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasotoroshimodels_exporter_type_12 = OtoroshiutilsmailerMailgunSettings.from_dict(data)

                return componentsschemasotoroshimodels_exporter_type_12
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasotoroshimodels_exporter_type_13 = OtoroshiutilsmailerMailjetSettings.from_dict(data)

                return componentsschemasotoroshimodels_exporter_type_13
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasotoroshimodels_exporter_type_14 = OtoroshiutilsmailerNoneMailerSettings.from_dict(data)

                return componentsschemasotoroshimodels_exporter_type_14
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemasotoroshimodels_exporter_type_15 = OtoroshiutilsmailerSendgridSettings.from_dict(data)

            return componentsschemasotoroshimodels_exporter_type_15

        config = _parse_config(d.pop("config", UNSET))

        _projection = d.pop("projection", UNSET)
        projection: Union[Unset, OtoroshimodelsDataExporterConfigProjection]
        if isinstance(_projection, Unset):
            projection = UNSET
        else:
            projection = OtoroshimodelsDataExporterConfigProjection.from_dict(_projection)

        enabled = d.pop("enabled", UNSET)

        _filtering = d.pop("filtering", UNSET)
        filtering: Union[Unset, OtoroshimodelsDataExporterConfigFiltering]
        if isinstance(_filtering, Unset):
            filtering = UNSET
        else:
            filtering = OtoroshimodelsDataExporterConfigFiltering.from_dict(_filtering)

        otoroshimodels_data_exporter_config = cls(
            desc=desc,
            location=location,
            buffer_size=buffer_size,
            json_workers=json_workers,
            group_duration=group_duration,
            group_size=group_size,
            typ=typ,
            tags=tags,
            send_workers=send_workers,
            id=id,
            name=name,
            metadata=metadata,
            config=config,
            projection=projection,
            enabled=enabled,
            filtering=filtering,
        )

        otoroshimodels_data_exporter_config.additional_properties = d
        return otoroshimodels_data_exporter_config

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
