from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.null import Null
from ..models.otoroshievents_kafka_config import OtoroshieventsKafkaConfig
from ..models.otoroshievents_statsd_config import OtoroshieventsStatsdConfig
from ..models.otoroshimodels_auto_cert import OtoroshimodelsAutoCert
from ..models.otoroshimodels_clever_cloud_settings import OtoroshimodelsCleverCloudSettings
from ..models.otoroshimodels_elastic_analytics_config import OtoroshimodelsElasticAnalyticsConfig
from ..models.otoroshimodels_global_config_metadata import OtoroshimodelsGlobalConfigMetadata
from ..models.otoroshimodels_global_scripts import OtoroshimodelsGlobalScripts
from ..models.otoroshimodels_ip_filtering import OtoroshimodelsIpFiltering
from ..models.otoroshimodels_ip_stack_geolocation_settings import OtoroshimodelsIpStackGeolocationSettings
from ..models.otoroshimodels_maxmind_geolocation_settings import OtoroshimodelsMaxmindGeolocationSettings
from ..models.otoroshimodels_none_geolocation_settings import OtoroshimodelsNoneGeolocationSettings
from ..models.otoroshimodels_proxies import OtoroshimodelsProxies
from ..models.otoroshimodels_snow_monkey_config import OtoroshimodelsSnowMonkeyConfig
from ..models.otoroshimodels_tls_settings import OtoroshimodelsTlsSettings
from ..models.otoroshimodels_user_agent_settings import OtoroshimodelsUserAgentSettings
from ..models.otoroshimodels_webhook import OtoroshimodelsWebhook
from ..models.otoroshiscriptplugins_plugins import OtoroshiscriptpluginsPlugins
from ..models.otoroshiutilsletsencrypt_lets_encrypt_settings import OtoroshiutilsletsencryptLetsEncryptSettings
from ..models.otoroshiutilsmailer_console_mailer_settings import OtoroshiutilsmailerConsoleMailerSettings
from ..models.otoroshiutilsmailer_generic_mailer_settings import OtoroshiutilsmailerGenericMailerSettings
from ..models.otoroshiutilsmailer_mailgun_settings import OtoroshiutilsmailerMailgunSettings
from ..models.otoroshiutilsmailer_mailjet_settings import OtoroshiutilsmailerMailjetSettings
from ..models.otoroshiutilsmailer_none_mailer_settings import OtoroshiutilsmailerNoneMailerSettings
from ..models.otoroshiutilsmailer_sendgrid_settings import OtoroshiutilsmailerSendgridSettings
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshimodelsGlobalConfig")


@attr.s(auto_attribs=True)
class OtoroshimodelsGlobalConfig:
    """The global config (dynamic) for otoroshi"""

    geolocation_settings: Union[
        OtoroshimodelsIpStackGeolocationSettings,
        OtoroshimodelsMaxmindGeolocationSettings,
        OtoroshimodelsNoneGeolocationSettings,
        Unset,
    ] = UNSET
    alerts_emails: Union[Unset, List[str]] = UNSET
    throttling_quota: Union[Unset, int] = UNSET
    max_webhook_size: Union[Unset, int] = UNSET
    max_concurrent_requests: Union[Unset, int] = UNSET
    clever_settings: Union[Null, Union[Null, OtoroshimodelsCleverCloudSettings], Unset] = UNSET
    endless_ip_addresses: Union[Unset, List[str]] = UNSET
    plugins: Union[Unset, OtoroshiscriptpluginsPlugins] = UNSET
    kafka_config: Union[Null, Union[Null, OtoroshieventsKafkaConfig], Unset] = UNSET
    max_logs_size: Union[Unset, int] = UNSET
    proxies: Union[Unset, OtoroshimodelsProxies] = UNSET
    enable_embedded_metrics: Union[Unset, bool] = UNSET
    elastic_reads_config: Union[Null, Union[Null, OtoroshimodelsElasticAnalyticsConfig], Unset] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    limit_concurrent_requests: Union[Unset, bool] = UNSET
    use_akka_http_client: Union[Unset, bool] = UNSET
    elastic_writes_configs: Union[Unset, List[OtoroshimodelsElasticAnalyticsConfig]] = UNSET
    log_analytics_on_server: Union[Unset, bool] = UNSET
    metadata: Union[Unset, OtoroshimodelsGlobalConfigMetadata] = UNSET
    api_read_only: Union[Unset, bool] = UNSET
    back_office_auth_ref: Union[Null, Unset, str] = UNSET
    stream_entity_only: Union[Unset, bool] = UNSET
    otoroshi_id: Union[Unset, str] = UNSET
    mailer_settings: Union[
        Null,
        Union[
            Null,
            Union[
                OtoroshiutilsmailerConsoleMailerSettings,
                OtoroshiutilsmailerGenericMailerSettings,
                OtoroshiutilsmailerMailgunSettings,
                OtoroshiutilsmailerMailjetSettings,
                OtoroshiutilsmailerNoneMailerSettings,
                OtoroshiutilsmailerSendgridSettings,
            ],
        ],
        Unset,
    ] = UNSET
    lines: Union[Unset, List[str]] = UNSET
    middle_fingers: Union[Unset, bool] = UNSET
    analytics_webhooks: Union[Unset, List[OtoroshimodelsWebhook]] = UNSET
    auto_cert: Union[Unset, OtoroshimodelsAutoCert] = UNSET
    maintenance_mode: Union[Unset, bool] = UNSET
    lets_encrypt_settings: Union[Unset, OtoroshiutilsletsencryptLetsEncryptSettings] = UNSET
    snow_monkey_config: Union[Unset, OtoroshimodelsSnowMonkeyConfig] = UNSET
    scripts: Union[Unset, OtoroshimodelsGlobalScripts] = UNSET
    per_ip_throttling_quota: Union[Unset, int] = UNSET
    use_circuit_breakers: Union[Unset, bool] = UNSET
    max_http_10_response_size: Union[Unset, int] = UNSET
    tls_settings: Union[Unset, OtoroshimodelsTlsSettings] = UNSET
    statsd_config: Union[Null, Union[Null, OtoroshieventsStatsdConfig], Unset] = UNSET
    auto_link_to_default_group: Union[Unset, bool] = UNSET
    alerts_webhooks: Union[Unset, List[OtoroshimodelsWebhook]] = UNSET
    ip_filtering: Union[Unset, OtoroshimodelsIpFiltering] = UNSET
    u_2_f_login_only: Union[Unset, bool] = UNSET
    user_agent_settings: Union[Unset, OtoroshimodelsUserAgentSettings] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        geolocation_settings: Union[Dict[str, Any], Unset]
        if isinstance(self.geolocation_settings, Unset):
            geolocation_settings = UNSET
        elif isinstance(self.geolocation_settings, OtoroshimodelsIpStackGeolocationSettings):
            geolocation_settings = self.geolocation_settings.to_dict()

        elif isinstance(self.geolocation_settings, OtoroshimodelsMaxmindGeolocationSettings):
            geolocation_settings = self.geolocation_settings.to_dict()

        else:
            geolocation_settings = self.geolocation_settings.to_dict()

        alerts_emails: Union[Unset, List[str]] = UNSET
        if not isinstance(self.alerts_emails, Unset):
            alerts_emails = self.alerts_emails

        throttling_quota = self.throttling_quota
        max_webhook_size = self.max_webhook_size
        max_concurrent_requests = self.max_concurrent_requests
        clever_settings: Union[Dict[str, Any], Unset]
        if isinstance(self.clever_settings, Unset):
            clever_settings = UNSET
        elif isinstance(self.clever_settings, Null):
            clever_settings = UNSET
            if not isinstance(self.clever_settings, Unset):
                clever_settings = self.clever_settings.to_dict()

        else:
            clever_settings
            if isinstance(self.clever_settings, Unset):
                clever_settings = UNSET
            elif isinstance(self.clever_settings, Null):
                clever_settings = UNSET
                if not isinstance(self.clever_settings, Unset):
                    clever_settings = self.clever_settings.to_dict()

            else:
                clever_settings = UNSET
                if not isinstance(self.clever_settings, Unset):
                    clever_settings = self.clever_settings.to_dict()

        endless_ip_addresses: Union[Unset, List[str]] = UNSET
        if not isinstance(self.endless_ip_addresses, Unset):
            endless_ip_addresses = self.endless_ip_addresses

        plugins: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.plugins, Unset):
            plugins = self.plugins.to_dict()

        kafka_config: Union[Dict[str, Any], Unset]
        if isinstance(self.kafka_config, Unset):
            kafka_config = UNSET
        elif isinstance(self.kafka_config, Null):
            kafka_config = UNSET
            if not isinstance(self.kafka_config, Unset):
                kafka_config = self.kafka_config.to_dict()

        else:
            kafka_config
            if isinstance(self.kafka_config, Unset):
                kafka_config = UNSET
            elif isinstance(self.kafka_config, Null):
                kafka_config = UNSET
                if not isinstance(self.kafka_config, Unset):
                    kafka_config = self.kafka_config.to_dict()

            else:
                kafka_config = UNSET
                if not isinstance(self.kafka_config, Unset):
                    kafka_config = self.kafka_config.to_dict()

        max_logs_size = self.max_logs_size
        proxies: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.proxies, Unset):
            proxies = self.proxies.to_dict()

        enable_embedded_metrics = self.enable_embedded_metrics
        elastic_reads_config: Union[Dict[str, Any], Unset]
        if isinstance(self.elastic_reads_config, Unset):
            elastic_reads_config = UNSET
        elif isinstance(self.elastic_reads_config, Null):
            elastic_reads_config = UNSET
            if not isinstance(self.elastic_reads_config, Unset):
                elastic_reads_config = self.elastic_reads_config.to_dict()

        else:
            elastic_reads_config
            if isinstance(self.elastic_reads_config, Unset):
                elastic_reads_config = UNSET
            elif isinstance(self.elastic_reads_config, Null):
                elastic_reads_config = UNSET
                if not isinstance(self.elastic_reads_config, Unset):
                    elastic_reads_config = self.elastic_reads_config.to_dict()

            else:
                elastic_reads_config = UNSET
                if not isinstance(self.elastic_reads_config, Unset):
                    elastic_reads_config = self.elastic_reads_config.to_dict()

        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        limit_concurrent_requests = self.limit_concurrent_requests
        use_akka_http_client = self.use_akka_http_client
        elastic_writes_configs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.elastic_writes_configs, Unset):
            elastic_writes_configs = []
            for elastic_writes_configs_item_data in self.elastic_writes_configs:
                elastic_writes_configs_item = elastic_writes_configs_item_data.to_dict()

                elastic_writes_configs.append(elastic_writes_configs_item)

        log_analytics_on_server = self.log_analytics_on_server
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        api_read_only = self.api_read_only
        back_office_auth_ref: Union[Dict[str, Any], Unset, str]
        if isinstance(self.back_office_auth_ref, Unset):
            back_office_auth_ref = UNSET
        elif isinstance(self.back_office_auth_ref, Null):
            back_office_auth_ref = UNSET
            if not isinstance(self.back_office_auth_ref, Unset):
                back_office_auth_ref = self.back_office_auth_ref.to_dict()

        else:
            back_office_auth_ref = self.back_office_auth_ref

        stream_entity_only = self.stream_entity_only
        otoroshi_id = self.otoroshi_id
        mailer_settings: Union[Dict[str, Any], Unset]
        if isinstance(self.mailer_settings, Unset):
            mailer_settings = UNSET
        elif isinstance(self.mailer_settings, Null):
            mailer_settings = UNSET
            if not isinstance(self.mailer_settings, Unset):
                mailer_settings = self.mailer_settings.to_dict()

        else:
            mailer_settings
            if isinstance(self.mailer_settings, Unset):
                mailer_settings = UNSET
            elif isinstance(self.mailer_settings, Null):
                mailer_settings = UNSET
                if not isinstance(self.mailer_settings, Unset):
                    mailer_settings = self.mailer_settings.to_dict()

            else:
                mailer_settings
                if isinstance(self.mailer_settings, Unset):
                    mailer_settings = UNSET
                elif isinstance(self.mailer_settings, OtoroshiutilsmailerConsoleMailerSettings):
                    mailer_settings = self.mailer_settings.to_dict()

                elif isinstance(self.mailer_settings, OtoroshiutilsmailerGenericMailerSettings):
                    mailer_settings = self.mailer_settings.to_dict()

                elif isinstance(self.mailer_settings, OtoroshiutilsmailerMailgunSettings):
                    mailer_settings = self.mailer_settings.to_dict()

                elif isinstance(self.mailer_settings, OtoroshiutilsmailerMailjetSettings):
                    mailer_settings = self.mailer_settings.to_dict()

                elif isinstance(self.mailer_settings, OtoroshiutilsmailerNoneMailerSettings):
                    mailer_settings = self.mailer_settings.to_dict()

                else:
                    mailer_settings = self.mailer_settings.to_dict()

        lines: Union[Unset, List[str]] = UNSET
        if not isinstance(self.lines, Unset):
            lines = self.lines

        middle_fingers = self.middle_fingers
        analytics_webhooks: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.analytics_webhooks, Unset):
            analytics_webhooks = []
            for analytics_webhooks_item_data in self.analytics_webhooks:
                analytics_webhooks_item = analytics_webhooks_item_data.to_dict()

                analytics_webhooks.append(analytics_webhooks_item)

        auto_cert: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.auto_cert, Unset):
            auto_cert = self.auto_cert.to_dict()

        maintenance_mode = self.maintenance_mode
        lets_encrypt_settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.lets_encrypt_settings, Unset):
            lets_encrypt_settings = self.lets_encrypt_settings.to_dict()

        snow_monkey_config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.snow_monkey_config, Unset):
            snow_monkey_config = self.snow_monkey_config.to_dict()

        scripts: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.scripts, Unset):
            scripts = self.scripts.to_dict()

        per_ip_throttling_quota = self.per_ip_throttling_quota
        use_circuit_breakers = self.use_circuit_breakers
        max_http_10_response_size = self.max_http_10_response_size
        tls_settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tls_settings, Unset):
            tls_settings = self.tls_settings.to_dict()

        statsd_config: Union[Dict[str, Any], Unset]
        if isinstance(self.statsd_config, Unset):
            statsd_config = UNSET
        elif isinstance(self.statsd_config, Null):
            statsd_config = UNSET
            if not isinstance(self.statsd_config, Unset):
                statsd_config = self.statsd_config.to_dict()

        else:
            statsd_config
            if isinstance(self.statsd_config, Unset):
                statsd_config = UNSET
            elif isinstance(self.statsd_config, Null):
                statsd_config = UNSET
                if not isinstance(self.statsd_config, Unset):
                    statsd_config = self.statsd_config.to_dict()

            else:
                statsd_config = UNSET
                if not isinstance(self.statsd_config, Unset):
                    statsd_config = self.statsd_config.to_dict()

        auto_link_to_default_group = self.auto_link_to_default_group
        alerts_webhooks: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.alerts_webhooks, Unset):
            alerts_webhooks = []
            for alerts_webhooks_item_data in self.alerts_webhooks:
                alerts_webhooks_item = alerts_webhooks_item_data.to_dict()

                alerts_webhooks.append(alerts_webhooks_item)

        ip_filtering: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ip_filtering, Unset):
            ip_filtering = self.ip_filtering.to_dict()

        u_2_f_login_only = self.u_2_f_login_only
        user_agent_settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user_agent_settings, Unset):
            user_agent_settings = self.user_agent_settings.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if geolocation_settings is not UNSET:
            field_dict["geolocationSettings"] = geolocation_settings
        if alerts_emails is not UNSET:
            field_dict["alertsEmails"] = alerts_emails
        if throttling_quota is not UNSET:
            field_dict["throttlingQuota"] = throttling_quota
        if max_webhook_size is not UNSET:
            field_dict["maxWebhookSize"] = max_webhook_size
        if max_concurrent_requests is not UNSET:
            field_dict["maxConcurrentRequests"] = max_concurrent_requests
        if clever_settings is not UNSET:
            field_dict["cleverSettings"] = clever_settings
        if endless_ip_addresses is not UNSET:
            field_dict["endlessIpAddresses"] = endless_ip_addresses
        if plugins is not UNSET:
            field_dict["plugins"] = plugins
        if kafka_config is not UNSET:
            field_dict["kafkaConfig"] = kafka_config
        if max_logs_size is not UNSET:
            field_dict["maxLogsSize"] = max_logs_size
        if proxies is not UNSET:
            field_dict["proxies"] = proxies
        if enable_embedded_metrics is not UNSET:
            field_dict["enableEmbeddedMetrics"] = enable_embedded_metrics
        if elastic_reads_config is not UNSET:
            field_dict["elasticReadsConfig"] = elastic_reads_config
        if tags is not UNSET:
            field_dict["tags"] = tags
        if limit_concurrent_requests is not UNSET:
            field_dict["limitConcurrentRequests"] = limit_concurrent_requests
        if use_akka_http_client is not UNSET:
            field_dict["useAkkaHttpClient"] = use_akka_http_client
        if elastic_writes_configs is not UNSET:
            field_dict["elasticWritesConfigs"] = elastic_writes_configs
        if log_analytics_on_server is not UNSET:
            field_dict["logAnalyticsOnServer"] = log_analytics_on_server
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if api_read_only is not UNSET:
            field_dict["apiReadOnly"] = api_read_only
        if back_office_auth_ref is not UNSET:
            field_dict["backOfficeAuthRef"] = back_office_auth_ref
        if stream_entity_only is not UNSET:
            field_dict["streamEntityOnly"] = stream_entity_only
        if otoroshi_id is not UNSET:
            field_dict["otoroshiId"] = otoroshi_id
        if mailer_settings is not UNSET:
            field_dict["mailerSettings"] = mailer_settings
        if lines is not UNSET:
            field_dict["lines"] = lines
        if middle_fingers is not UNSET:
            field_dict["middleFingers"] = middle_fingers
        if analytics_webhooks is not UNSET:
            field_dict["analyticsWebhooks"] = analytics_webhooks
        if auto_cert is not UNSET:
            field_dict["autoCert"] = auto_cert
        if maintenance_mode is not UNSET:
            field_dict["maintenanceMode"] = maintenance_mode
        if lets_encrypt_settings is not UNSET:
            field_dict["letsEncryptSettings"] = lets_encrypt_settings
        if snow_monkey_config is not UNSET:
            field_dict["snowMonkeyConfig"] = snow_monkey_config
        if scripts is not UNSET:
            field_dict["scripts"] = scripts
        if per_ip_throttling_quota is not UNSET:
            field_dict["perIpThrottlingQuota"] = per_ip_throttling_quota
        if use_circuit_breakers is not UNSET:
            field_dict["useCircuitBreakers"] = use_circuit_breakers
        if max_http_10_response_size is not UNSET:
            field_dict["maxHttp10ResponseSize"] = max_http_10_response_size
        if tls_settings is not UNSET:
            field_dict["tlsSettings"] = tls_settings
        if statsd_config is not UNSET:
            field_dict["statsdConfig"] = statsd_config
        if auto_link_to_default_group is not UNSET:
            field_dict["autoLinkToDefaultGroup"] = auto_link_to_default_group
        if alerts_webhooks is not UNSET:
            field_dict["alertsWebhooks"] = alerts_webhooks
        if ip_filtering is not UNSET:
            field_dict["ipFiltering"] = ip_filtering
        if u_2_f_login_only is not UNSET:
            field_dict["u2fLoginOnly"] = u_2_f_login_only
        if user_agent_settings is not UNSET:
            field_dict["userAgentSettings"] = user_agent_settings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_geolocation_settings(
            data: object,
        ) -> Union[
            OtoroshimodelsIpStackGeolocationSettings,
            OtoroshimodelsMaxmindGeolocationSettings,
            OtoroshimodelsNoneGeolocationSettings,
            Unset,
        ]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasotoroshimodels_geolocation_settings_type_0 = (
                    OtoroshimodelsIpStackGeolocationSettings.from_dict(data)
                )

                return componentsschemasotoroshimodels_geolocation_settings_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasotoroshimodels_geolocation_settings_type_1 = (
                    OtoroshimodelsMaxmindGeolocationSettings.from_dict(data)
                )

                return componentsschemasotoroshimodels_geolocation_settings_type_1
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemasotoroshimodels_geolocation_settings_type_2 = (
                OtoroshimodelsNoneGeolocationSettings.from_dict(data)
            )

            return componentsschemasotoroshimodels_geolocation_settings_type_2

        geolocation_settings = _parse_geolocation_settings(d.pop("geolocationSettings", UNSET))

        alerts_emails = cast(List[str], d.pop("alertsEmails", UNSET))

        throttling_quota = d.pop("throttlingQuota", UNSET)

        max_webhook_size = d.pop("maxWebhookSize", UNSET)

        max_concurrent_requests = d.pop("maxConcurrentRequests", UNSET)

        def _parse_clever_settings(data: object) -> Union[Null, Union[Null, OtoroshimodelsCleverCloudSettings], Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _clever_settings_type_0 = data
                clever_settings_type_0: Union[Unset, Null]
                if isinstance(_clever_settings_type_0, Unset):
                    clever_settings_type_0 = UNSET
                else:
                    clever_settings_type_0 = Null.from_dict(_clever_settings_type_0)

                return clever_settings_type_0
            except:  # noqa: E722
                pass
            if not True:
                raise TypeError()

            def _parse_clever_settings_type_1(data: object) -> Union[Null, OtoroshimodelsCleverCloudSettings, Unset]:
                if isinstance(data, Unset):
                    return data
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    _clever_settings_type_1_type_0 = data
                    clever_settings_type_1_type_0: Union[Unset, Null]
                    if isinstance(_clever_settings_type_1_type_0, Unset):
                        clever_settings_type_1_type_0 = UNSET
                    else:
                        clever_settings_type_1_type_0 = Null.from_dict(_clever_settings_type_1_type_0)

                    return clever_settings_type_1_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                _clever_settings_type_1_type_1 = data
                clever_settings_type_1_type_1: Union[Unset, OtoroshimodelsCleverCloudSettings]
                if isinstance(_clever_settings_type_1_type_1, Unset):
                    clever_settings_type_1_type_1 = UNSET
                else:
                    clever_settings_type_1_type_1 = OtoroshimodelsCleverCloudSettings.from_dict(
                        _clever_settings_type_1_type_1
                    )

                return clever_settings_type_1_type_1

            clever_settings_type_1 = _parse_clever_settings_type_1(data)

            return clever_settings_type_1

        clever_settings = _parse_clever_settings(d.pop("cleverSettings", UNSET))

        endless_ip_addresses = cast(List[str], d.pop("endlessIpAddresses", UNSET))

        _plugins = d.pop("plugins", UNSET)
        plugins: Union[Unset, OtoroshiscriptpluginsPlugins]
        if isinstance(_plugins, Unset):
            plugins = UNSET
        else:
            plugins = OtoroshiscriptpluginsPlugins.from_dict(_plugins)

        def _parse_kafka_config(data: object) -> Union[Null, Union[Null, OtoroshieventsKafkaConfig], Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _kafka_config_type_0 = data
                kafka_config_type_0: Union[Unset, Null]
                if isinstance(_kafka_config_type_0, Unset):
                    kafka_config_type_0 = UNSET
                else:
                    kafka_config_type_0 = Null.from_dict(_kafka_config_type_0)

                return kafka_config_type_0
            except:  # noqa: E722
                pass
            if not True:
                raise TypeError()

            def _parse_kafka_config_type_1(data: object) -> Union[Null, OtoroshieventsKafkaConfig, Unset]:
                if isinstance(data, Unset):
                    return data
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    _kafka_config_type_1_type_0 = data
                    kafka_config_type_1_type_0: Union[Unset, Null]
                    if isinstance(_kafka_config_type_1_type_0, Unset):
                        kafka_config_type_1_type_0 = UNSET
                    else:
                        kafka_config_type_1_type_0 = Null.from_dict(_kafka_config_type_1_type_0)

                    return kafka_config_type_1_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                _kafka_config_type_1_type_1 = data
                kafka_config_type_1_type_1: Union[Unset, OtoroshieventsKafkaConfig]
                if isinstance(_kafka_config_type_1_type_1, Unset):
                    kafka_config_type_1_type_1 = UNSET
                else:
                    kafka_config_type_1_type_1 = OtoroshieventsKafkaConfig.from_dict(_kafka_config_type_1_type_1)

                return kafka_config_type_1_type_1

            kafka_config_type_1 = _parse_kafka_config_type_1(data)

            return kafka_config_type_1

        kafka_config = _parse_kafka_config(d.pop("kafkaConfig", UNSET))

        max_logs_size = d.pop("maxLogsSize", UNSET)

        _proxies = d.pop("proxies", UNSET)
        proxies: Union[Unset, OtoroshimodelsProxies]
        if isinstance(_proxies, Unset):
            proxies = UNSET
        else:
            proxies = OtoroshimodelsProxies.from_dict(_proxies)

        enable_embedded_metrics = d.pop("enableEmbeddedMetrics", UNSET)

        def _parse_elastic_reads_config(
            data: object,
        ) -> Union[Null, Union[Null, OtoroshimodelsElasticAnalyticsConfig], Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _elastic_reads_config_type_0 = data
                elastic_reads_config_type_0: Union[Unset, Null]
                if isinstance(_elastic_reads_config_type_0, Unset):
                    elastic_reads_config_type_0 = UNSET
                else:
                    elastic_reads_config_type_0 = Null.from_dict(_elastic_reads_config_type_0)

                return elastic_reads_config_type_0
            except:  # noqa: E722
                pass
            if not True:
                raise TypeError()

            def _parse_elastic_reads_config_type_1(
                data: object,
            ) -> Union[Null, OtoroshimodelsElasticAnalyticsConfig, Unset]:
                if isinstance(data, Unset):
                    return data
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    _elastic_reads_config_type_1_type_0 = data
                    elastic_reads_config_type_1_type_0: Union[Unset, Null]
                    if isinstance(_elastic_reads_config_type_1_type_0, Unset):
                        elastic_reads_config_type_1_type_0 = UNSET
                    else:
                        elastic_reads_config_type_1_type_0 = Null.from_dict(_elastic_reads_config_type_1_type_0)

                    return elastic_reads_config_type_1_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                _elastic_reads_config_type_1_type_1 = data
                elastic_reads_config_type_1_type_1: Union[Unset, OtoroshimodelsElasticAnalyticsConfig]
                if isinstance(_elastic_reads_config_type_1_type_1, Unset):
                    elastic_reads_config_type_1_type_1 = UNSET
                else:
                    elastic_reads_config_type_1_type_1 = OtoroshimodelsElasticAnalyticsConfig.from_dict(
                        _elastic_reads_config_type_1_type_1
                    )

                return elastic_reads_config_type_1_type_1

            elastic_reads_config_type_1 = _parse_elastic_reads_config_type_1(data)

            return elastic_reads_config_type_1

        elastic_reads_config = _parse_elastic_reads_config(d.pop("elasticReadsConfig", UNSET))

        tags = cast(List[str], d.pop("tags", UNSET))

        limit_concurrent_requests = d.pop("limitConcurrentRequests", UNSET)

        use_akka_http_client = d.pop("useAkkaHttpClient", UNSET)

        elastic_writes_configs = []
        _elastic_writes_configs = d.pop("elasticWritesConfigs", UNSET)
        for elastic_writes_configs_item_data in _elastic_writes_configs or []:
            elastic_writes_configs_item = OtoroshimodelsElasticAnalyticsConfig.from_dict(
                elastic_writes_configs_item_data
            )

            elastic_writes_configs.append(elastic_writes_configs_item)

        log_analytics_on_server = d.pop("logAnalyticsOnServer", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, OtoroshimodelsGlobalConfigMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = OtoroshimodelsGlobalConfigMetadata.from_dict(_metadata)

        api_read_only = d.pop("apiReadOnly", UNSET)

        def _parse_back_office_auth_ref(data: object) -> Union[Null, Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _back_office_auth_ref_type_0 = data
                back_office_auth_ref_type_0: Union[Unset, Null]
                if isinstance(_back_office_auth_ref_type_0, Unset):
                    back_office_auth_ref_type_0 = UNSET
                else:
                    back_office_auth_ref_type_0 = Null.from_dict(_back_office_auth_ref_type_0)

                return back_office_auth_ref_type_0
            except:  # noqa: E722
                pass
            return cast(Union[Null, Unset, str], data)

        back_office_auth_ref = _parse_back_office_auth_ref(d.pop("backOfficeAuthRef", UNSET))

        stream_entity_only = d.pop("streamEntityOnly", UNSET)

        otoroshi_id = d.pop("otoroshiId", UNSET)

        def _parse_mailer_settings(
            data: object,
        ) -> Union[
            Null,
            Union[
                Null,
                Union[
                    OtoroshiutilsmailerConsoleMailerSettings,
                    OtoroshiutilsmailerGenericMailerSettings,
                    OtoroshiutilsmailerMailgunSettings,
                    OtoroshiutilsmailerMailjetSettings,
                    OtoroshiutilsmailerNoneMailerSettings,
                    OtoroshiutilsmailerSendgridSettings,
                ],
            ],
            Unset,
        ]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _mailer_settings_type_0 = data
                mailer_settings_type_0: Union[Unset, Null]
                if isinstance(_mailer_settings_type_0, Unset):
                    mailer_settings_type_0 = UNSET
                else:
                    mailer_settings_type_0 = Null.from_dict(_mailer_settings_type_0)

                return mailer_settings_type_0
            except:  # noqa: E722
                pass
            if not True:
                raise TypeError()

            def _parse_mailer_settings_type_1(
                data: object,
            ) -> Union[
                Null,
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
                    _mailer_settings_type_1_type_0 = data
                    mailer_settings_type_1_type_0: Union[Unset, Null]
                    if isinstance(_mailer_settings_type_1_type_0, Unset):
                        mailer_settings_type_1_type_0 = UNSET
                    else:
                        mailer_settings_type_1_type_0 = Null.from_dict(_mailer_settings_type_1_type_0)

                    return mailer_settings_type_1_type_0
                except:  # noqa: E722
                    pass
                if not True:
                    raise TypeError()

                def _parse_mailer_settings_type_1_type_1(
                    data: object,
                ) -> Union[
                    OtoroshiutilsmailerConsoleMailerSettings,
                    OtoroshiutilsmailerGenericMailerSettings,
                    OtoroshiutilsmailerMailgunSettings,
                    OtoroshiutilsmailerMailjetSettings,
                    OtoroshiutilsmailerNoneMailerSettings,
                    OtoroshiutilsmailerSendgridSettings,
                    Unset,
                ]:
                    if isinstance(data, Unset):
                        return data
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

                mailer_settings_type_1_type_1 = _parse_mailer_settings_type_1_type_1(data)

                return mailer_settings_type_1_type_1

            mailer_settings_type_1 = _parse_mailer_settings_type_1(data)

            return mailer_settings_type_1

        mailer_settings = _parse_mailer_settings(d.pop("mailerSettings", UNSET))

        lines = cast(List[str], d.pop("lines", UNSET))

        middle_fingers = d.pop("middleFingers", UNSET)

        analytics_webhooks = []
        _analytics_webhooks = d.pop("analyticsWebhooks", UNSET)
        for analytics_webhooks_item_data in _analytics_webhooks or []:
            analytics_webhooks_item = OtoroshimodelsWebhook.from_dict(analytics_webhooks_item_data)

            analytics_webhooks.append(analytics_webhooks_item)

        _auto_cert = d.pop("autoCert", UNSET)
        auto_cert: Union[Unset, OtoroshimodelsAutoCert]
        if isinstance(_auto_cert, Unset):
            auto_cert = UNSET
        else:
            auto_cert = OtoroshimodelsAutoCert.from_dict(_auto_cert)

        maintenance_mode = d.pop("maintenanceMode", UNSET)

        _lets_encrypt_settings = d.pop("letsEncryptSettings", UNSET)
        lets_encrypt_settings: Union[Unset, OtoroshiutilsletsencryptLetsEncryptSettings]
        if isinstance(_lets_encrypt_settings, Unset):
            lets_encrypt_settings = UNSET
        else:
            lets_encrypt_settings = OtoroshiutilsletsencryptLetsEncryptSettings.from_dict(_lets_encrypt_settings)

        _snow_monkey_config = d.pop("snowMonkeyConfig", UNSET)
        snow_monkey_config: Union[Unset, OtoroshimodelsSnowMonkeyConfig]
        if isinstance(_snow_monkey_config, Unset):
            snow_monkey_config = UNSET
        else:
            snow_monkey_config = OtoroshimodelsSnowMonkeyConfig.from_dict(_snow_monkey_config)

        _scripts = d.pop("scripts", UNSET)
        scripts: Union[Unset, OtoroshimodelsGlobalScripts]
        if isinstance(_scripts, Unset):
            scripts = UNSET
        else:
            scripts = OtoroshimodelsGlobalScripts.from_dict(_scripts)

        per_ip_throttling_quota = d.pop("perIpThrottlingQuota", UNSET)

        use_circuit_breakers = d.pop("useCircuitBreakers", UNSET)

        max_http_10_response_size = d.pop("maxHttp10ResponseSize", UNSET)

        _tls_settings = d.pop("tlsSettings", UNSET)
        tls_settings: Union[Unset, OtoroshimodelsTlsSettings]
        if isinstance(_tls_settings, Unset):
            tls_settings = UNSET
        else:
            tls_settings = OtoroshimodelsTlsSettings.from_dict(_tls_settings)

        def _parse_statsd_config(data: object) -> Union[Null, Union[Null, OtoroshieventsStatsdConfig], Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _statsd_config_type_0 = data
                statsd_config_type_0: Union[Unset, Null]
                if isinstance(_statsd_config_type_0, Unset):
                    statsd_config_type_0 = UNSET
                else:
                    statsd_config_type_0 = Null.from_dict(_statsd_config_type_0)

                return statsd_config_type_0
            except:  # noqa: E722
                pass
            if not True:
                raise TypeError()

            def _parse_statsd_config_type_1(data: object) -> Union[Null, OtoroshieventsStatsdConfig, Unset]:
                if isinstance(data, Unset):
                    return data
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    _statsd_config_type_1_type_0 = data
                    statsd_config_type_1_type_0: Union[Unset, Null]
                    if isinstance(_statsd_config_type_1_type_0, Unset):
                        statsd_config_type_1_type_0 = UNSET
                    else:
                        statsd_config_type_1_type_0 = Null.from_dict(_statsd_config_type_1_type_0)

                    return statsd_config_type_1_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                _statsd_config_type_1_type_1 = data
                statsd_config_type_1_type_1: Union[Unset, OtoroshieventsStatsdConfig]
                if isinstance(_statsd_config_type_1_type_1, Unset):
                    statsd_config_type_1_type_1 = UNSET
                else:
                    statsd_config_type_1_type_1 = OtoroshieventsStatsdConfig.from_dict(_statsd_config_type_1_type_1)

                return statsd_config_type_1_type_1

            statsd_config_type_1 = _parse_statsd_config_type_1(data)

            return statsd_config_type_1

        statsd_config = _parse_statsd_config(d.pop("statsdConfig", UNSET))

        auto_link_to_default_group = d.pop("autoLinkToDefaultGroup", UNSET)

        alerts_webhooks = []
        _alerts_webhooks = d.pop("alertsWebhooks", UNSET)
        for alerts_webhooks_item_data in _alerts_webhooks or []:
            alerts_webhooks_item = OtoroshimodelsWebhook.from_dict(alerts_webhooks_item_data)

            alerts_webhooks.append(alerts_webhooks_item)

        _ip_filtering = d.pop("ipFiltering", UNSET)
        ip_filtering: Union[Unset, OtoroshimodelsIpFiltering]
        if isinstance(_ip_filtering, Unset):
            ip_filtering = UNSET
        else:
            ip_filtering = OtoroshimodelsIpFiltering.from_dict(_ip_filtering)

        u_2_f_login_only = d.pop("u2fLoginOnly", UNSET)

        _user_agent_settings = d.pop("userAgentSettings", UNSET)
        user_agent_settings: Union[Unset, OtoroshimodelsUserAgentSettings]
        if isinstance(_user_agent_settings, Unset):
            user_agent_settings = UNSET
        else:
            user_agent_settings = OtoroshimodelsUserAgentSettings.from_dict(_user_agent_settings)

        otoroshimodels_global_config = cls(
            geolocation_settings=geolocation_settings,
            alerts_emails=alerts_emails,
            throttling_quota=throttling_quota,
            max_webhook_size=max_webhook_size,
            max_concurrent_requests=max_concurrent_requests,
            clever_settings=clever_settings,
            endless_ip_addresses=endless_ip_addresses,
            plugins=plugins,
            kafka_config=kafka_config,
            max_logs_size=max_logs_size,
            proxies=proxies,
            enable_embedded_metrics=enable_embedded_metrics,
            elastic_reads_config=elastic_reads_config,
            tags=tags,
            limit_concurrent_requests=limit_concurrent_requests,
            use_akka_http_client=use_akka_http_client,
            elastic_writes_configs=elastic_writes_configs,
            log_analytics_on_server=log_analytics_on_server,
            metadata=metadata,
            api_read_only=api_read_only,
            back_office_auth_ref=back_office_auth_ref,
            stream_entity_only=stream_entity_only,
            otoroshi_id=otoroshi_id,
            mailer_settings=mailer_settings,
            lines=lines,
            middle_fingers=middle_fingers,
            analytics_webhooks=analytics_webhooks,
            auto_cert=auto_cert,
            maintenance_mode=maintenance_mode,
            lets_encrypt_settings=lets_encrypt_settings,
            snow_monkey_config=snow_monkey_config,
            scripts=scripts,
            per_ip_throttling_quota=per_ip_throttling_quota,
            use_circuit_breakers=use_circuit_breakers,
            max_http_10_response_size=max_http_10_response_size,
            tls_settings=tls_settings,
            statsd_config=statsd_config,
            auto_link_to_default_group=auto_link_to_default_group,
            alerts_webhooks=alerts_webhooks,
            ip_filtering=ip_filtering,
            u_2_f_login_only=u_2_f_login_only,
            user_agent_settings=user_agent_settings,
        )

        otoroshimodels_global_config.additional_properties = d
        return otoroshimodels_global_config

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
