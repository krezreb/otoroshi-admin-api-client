from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.null import Null
from ..models.otoroshimodels_api_descriptor import OtoroshimodelsApiDescriptor
from ..models.otoroshimodels_api_key_constraints import OtoroshimodelsApiKeyConstraints
from ..models.otoroshimodels_canary import OtoroshimodelsCanary
from ..models.otoroshimodels_chaos_config import OtoroshimodelsChaosConfig
from ..models.otoroshimodels_client_config import OtoroshimodelsClientConfig
from ..models.otoroshimodels_cors_settings import OtoroshimodelsCorsSettings
from ..models.otoroshimodels_entity_location import OtoroshimodelsEntityLocation
from ..models.otoroshimodels_es_algo_settings import OtoroshimodelsESAlgoSettings
from ..models.otoroshimodels_eskp_algo_settings import OtoroshimodelsESKPAlgoSettings
from ..models.otoroshimodels_global_jwt_verifier import OtoroshimodelsGlobalJwtVerifier
from ..models.otoroshimodels_health_check import OtoroshimodelsHealthCheck
from ..models.otoroshimodels_hs_algo_settings import OtoroshimodelsHSAlgoSettings
from ..models.otoroshimodels_ip_filtering import OtoroshimodelsIpFiltering
from ..models.otoroshimodels_jwks_algo_settings import OtoroshimodelsJWKSAlgoSettings
from ..models.otoroshimodels_kid_algo_settings import OtoroshimodelsKidAlgoSettings
from ..models.otoroshimodels_load_balancing import OtoroshimodelsLoadBalancing
from ..models.otoroshimodels_local_jwt_verifier import OtoroshimodelsLocalJwtVerifier
from ..models.otoroshimodels_redirection_settings import OtoroshimodelsRedirectionSettings
from ..models.otoroshimodels_ref_jwt_verifier import OtoroshimodelsRefJwtVerifier
from ..models.otoroshimodels_restrictions import OtoroshimodelsRestrictions
from ..models.otoroshimodels_rs_algo_settings import OtoroshimodelsRSAlgoSettings
from ..models.otoroshimodels_rsakp_algo_settings import OtoroshimodelsRSAKPAlgoSettings
from ..models.otoroshimodels_sec_com_headers import OtoroshimodelsSecComHeaders
from ..models.otoroshimodels_sec_com_info_token_version import OtoroshimodelsSecComInfoTokenVersion
from ..models.otoroshimodels_sec_com_version import OtoroshimodelsSecComVersion
from ..models.otoroshimodels_service_descriptor_additional_headers import (
    OtoroshimodelsServiceDescriptorAdditionalHeaders,
)
from ..models.otoroshimodels_service_descriptor_additional_headers_out import (
    OtoroshimodelsServiceDescriptorAdditionalHeadersOut,
)
from ..models.otoroshimodels_service_descriptor_headers_verification import (
    OtoroshimodelsServiceDescriptorHeadersVerification,
)
from ..models.otoroshimodels_service_descriptor_matching_headers import OtoroshimodelsServiceDescriptorMatchingHeaders
from ..models.otoroshimodels_service_descriptor_metadata import OtoroshimodelsServiceDescriptorMetadata
from ..models.otoroshimodels_service_descriptor_missing_only_headers_in import (
    OtoroshimodelsServiceDescriptorMissingOnlyHeadersIn,
)
from ..models.otoroshimodels_service_descriptor_missing_only_headers_out import (
    OtoroshimodelsServiceDescriptorMissingOnlyHeadersOut,
)
from ..models.otoroshimodels_service_descriptor_transformer_config import (
    OtoroshimodelsServiceDescriptorTransformerConfig,
)
from ..models.otoroshimodels_target import OtoroshimodelsTarget
from ..models.otoroshiscript_access_validator_ref import OtoroshiscriptAccessValidatorRef
from ..models.otoroshiscript_pre_routing_ref import OtoroshiscriptPreRoutingRef
from ..models.otoroshiscriptplugins_plugins import OtoroshiscriptpluginsPlugins
from ..models.otoroshiutilsgzip_gzip_config import OtoroshiutilsgzipGzipConfig
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshimodelsServiceDescriptor")


@attr.s(auto_attribs=True)
class OtoroshimodelsServiceDescriptor:
    """The otoroshi model for a service (handles routing)"""

    build_mode: Union[Unset, bool] = UNSET
    hosts: Union[Unset, List[str]] = UNSET
    private_app: Union[Unset, bool] = UNSET
    local_scheme: Union[Unset, str] = UNSET
    auth_config_ref: Union[Null, Unset, str] = UNSET
    issue_cert_ca: Union[Null, Unset, str] = UNSET
    root: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    additional_headers: Union[Unset, OtoroshimodelsServiceDescriptorAdditionalHeaders] = UNSET
    domain: Union[Unset, str] = UNSET
    client_config: Union[Unset, OtoroshimodelsClientConfig] = UNSET
    matching_root: Union[Null, Unset, str] = UNSET
    force_https: Union[Unset, bool] = UNSET
    local_host: Union[Unset, str] = UNSET
    send_otoroshi_headers_back: Union[Unset, bool] = UNSET
    health_check: Union[Unset, OtoroshimodelsHealthCheck] = UNSET
    strictly_private: Union[Unset, bool] = UNSET
    detect_api_key_sooner: Union[Unset, bool] = UNSET
    allow_http_10: Union[Unset, bool] = UNSET
    subdomain: Union[Unset, str] = UNSET
    paths: Union[Unset, List[str]] = UNSET
    strip_path: Union[Unset, bool] = UNSET
    sec_com_algo_challenge_oto_to_back: Union[
        OtoroshimodelsESAlgoSettings,
        OtoroshimodelsESKPAlgoSettings,
        OtoroshimodelsHSAlgoSettings,
        OtoroshimodelsJWKSAlgoSettings,
        OtoroshimodelsKidAlgoSettings,
        OtoroshimodelsRSAKPAlgoSettings,
        OtoroshimodelsRSAlgoSettings,
        Unset,
    ] = UNSET
    api_key_constraints: Union[Unset, OtoroshimodelsApiKeyConstraints] = UNSET
    env: Union[Unset, str] = UNSET
    x_forwarded_headers: Union[Unset, bool] = UNSET
    transformer_refs: Union[Unset, List[str]] = UNSET
    enabled: Union[Unset, bool] = UNSET
    gzip: Union[Unset, OtoroshiutilsgzipGzipConfig] = UNSET
    send_info_token: Union[Unset, bool] = UNSET
    tcp_udp_tunneling: Union[Unset, bool] = UNSET
    remove_headers_out: Union[Unset, List[str]] = UNSET
    use_akka_http_client: Union[Unset, bool] = UNSET
    maintenance_mode: Union[Unset, bool] = UNSET
    id: Union[Unset, str] = UNSET
    remove_headers_in: Union[Unset, List[str]] = UNSET
    log_analytics_on_server: Union[Unset, bool] = UNSET
    sec_com_algo_info_token: Union[
        OtoroshimodelsESAlgoSettings,
        OtoroshimodelsESKPAlgoSettings,
        OtoroshimodelsHSAlgoSettings,
        OtoroshimodelsJWKSAlgoSettings,
        OtoroshimodelsKidAlgoSettings,
        OtoroshimodelsRSAKPAlgoSettings,
        OtoroshimodelsRSAlgoSettings,
        Unset,
    ] = UNSET
    user_facing: Union[Unset, bool] = UNSET
    transformer_config: Union[Unset, OtoroshimodelsServiceDescriptorTransformerConfig] = UNSET
    client_validator_ref: Union[Null, Unset, str] = UNSET
    security_excluded_patterns: Union[Unset, List[str]] = UNSET
    ip_filtering: Union[Unset, OtoroshimodelsIpFiltering] = UNSET
    targets: Union[Unset, List[OtoroshimodelsTarget]] = UNSET
    redirection: Union[Unset, OtoroshimodelsRedirectionSettings] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    restrictions: Union[Unset, OtoroshimodelsRestrictions] = UNSET
    override_host: Union[Unset, bool] = UNSET
    access_validator: Union[Unset, OtoroshiscriptAccessValidatorRef] = UNSET
    send_state_challenge: Union[Unset, bool] = UNSET
    chaos_config: Union[Unset, OtoroshimodelsChaosConfig] = UNSET
    sec_com_info_token_version: Union[Unset, OtoroshimodelsSecComInfoTokenVersion] = UNSET
    additional_headers_out: Union[Unset, OtoroshimodelsServiceDescriptorAdditionalHeadersOut] = UNSET
    sec_com_headers: Union[Unset, OtoroshimodelsSecComHeaders] = UNSET
    matching_headers: Union[Unset, OtoroshimodelsServiceDescriptorMatchingHeaders] = UNSET
    sec_com_algo_challenge_back_to_oto: Union[
        OtoroshimodelsESAlgoSettings,
        OtoroshimodelsESKPAlgoSettings,
        OtoroshimodelsHSAlgoSettings,
        OtoroshimodelsJWKSAlgoSettings,
        OtoroshimodelsKidAlgoSettings,
        OtoroshimodelsRSAKPAlgoSettings,
        OtoroshimodelsRSAlgoSettings,
        Unset,
    ] = UNSET
    sec_com_use_same_algo: Union[Unset, bool] = UNSET
    use_new_ws_client: Union[Unset, bool] = UNSET
    sec_com_excluded_patterns: Union[Unset, List[str]] = UNSET
    redirect_to_local: Union[Unset, bool] = UNSET
    enforce_secure_communication: Union[Unset, bool] = UNSET
    missing_only_headers_out: Union[Unset, OtoroshimodelsServiceDescriptorMissingOnlyHeadersOut] = UNSET
    sec_com_settings: Union[
        OtoroshimodelsESAlgoSettings,
        OtoroshimodelsESKPAlgoSettings,
        OtoroshimodelsHSAlgoSettings,
        OtoroshimodelsJWKSAlgoSettings,
        OtoroshimodelsKidAlgoSettings,
        OtoroshimodelsRSAKPAlgoSettings,
        OtoroshimodelsRSAlgoSettings,
        Unset,
    ] = UNSET
    handle_legacy_domain: Union[Unset, bool] = UNSET
    canary: Union[Unset, OtoroshimodelsCanary] = UNSET
    location: Union[Unset, OtoroshimodelsEntityLocation] = UNSET
    plugins: Union[Unset, OtoroshiscriptpluginsPlugins] = UNSET
    sec_com_ttl: Union[Unset, float] = UNSET
    description: Union[Unset, str] = UNSET
    sec_com_version: Union[Unset, OtoroshimodelsSecComVersion] = UNSET
    pre_routing: Union[Unset, OtoroshiscriptPreRoutingRef] = UNSET
    groups: Union[Unset, List[str]] = UNSET
    read_only: Union[Unset, bool] = UNSET
    private_patterns: Union[Unset, List[str]] = UNSET
    targets_load_balancing: Union[Unset, OtoroshimodelsLoadBalancing] = UNSET
    cors: Union[Unset, OtoroshimodelsCorsSettings] = UNSET
    metadata: Union[Unset, OtoroshimodelsServiceDescriptorMetadata] = UNSET
    public_patterns: Union[Unset, List[str]] = UNSET
    api: Union[Unset, OtoroshimodelsApiDescriptor] = UNSET
    missing_only_headers_in: Union[Unset, OtoroshimodelsServiceDescriptorMissingOnlyHeadersIn] = UNSET
    issue_cert: Union[Unset, bool] = UNSET
    headers_verification: Union[Unset, OtoroshimodelsServiceDescriptorHeadersVerification] = UNSET
    jwt_verifier: Union[
        OtoroshimodelsGlobalJwtVerifier, OtoroshimodelsLocalJwtVerifier, OtoroshimodelsRefJwtVerifier, Unset
    ] = UNSET
    lets_encrypt: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        build_mode = self.build_mode
        hosts: Union[Unset, List[str]] = UNSET
        if not isinstance(self.hosts, Unset):
            hosts = self.hosts

        private_app = self.private_app
        local_scheme = self.local_scheme
        auth_config_ref: Union[Dict[str, Any], Unset, str]
        if isinstance(self.auth_config_ref, Unset):
            auth_config_ref = UNSET
        elif isinstance(self.auth_config_ref, Null):
            auth_config_ref = UNSET
            if not isinstance(self.auth_config_ref, Unset):
                auth_config_ref = self.auth_config_ref.to_dict()

        else:
            auth_config_ref = self.auth_config_ref

        issue_cert_ca: Union[Dict[str, Any], Unset, str]
        if isinstance(self.issue_cert_ca, Unset):
            issue_cert_ca = UNSET
        elif isinstance(self.issue_cert_ca, Null):
            issue_cert_ca = UNSET
            if not isinstance(self.issue_cert_ca, Unset):
                issue_cert_ca = self.issue_cert_ca.to_dict()

        else:
            issue_cert_ca = self.issue_cert_ca

        root = self.root
        name = self.name
        additional_headers: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.additional_headers, Unset):
            additional_headers = self.additional_headers.to_dict()

        domain = self.domain
        client_config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.client_config, Unset):
            client_config = self.client_config.to_dict()

        matching_root: Union[Dict[str, Any], Unset, str]
        if isinstance(self.matching_root, Unset):
            matching_root = UNSET
        elif isinstance(self.matching_root, Null):
            matching_root = UNSET
            if not isinstance(self.matching_root, Unset):
                matching_root = self.matching_root.to_dict()

        else:
            matching_root = self.matching_root

        force_https = self.force_https
        local_host = self.local_host
        send_otoroshi_headers_back = self.send_otoroshi_headers_back
        health_check: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.health_check, Unset):
            health_check = self.health_check.to_dict()

        strictly_private = self.strictly_private
        detect_api_key_sooner = self.detect_api_key_sooner
        allow_http_10 = self.allow_http_10
        subdomain = self.subdomain
        paths: Union[Unset, List[str]] = UNSET
        if not isinstance(self.paths, Unset):
            paths = self.paths

        strip_path = self.strip_path
        sec_com_algo_challenge_oto_to_back: Union[Dict[str, Any], Unset]
        if isinstance(self.sec_com_algo_challenge_oto_to_back, Unset):
            sec_com_algo_challenge_oto_to_back = UNSET
        elif isinstance(self.sec_com_algo_challenge_oto_to_back, OtoroshimodelsESAlgoSettings):
            sec_com_algo_challenge_oto_to_back = self.sec_com_algo_challenge_oto_to_back.to_dict()

        elif isinstance(self.sec_com_algo_challenge_oto_to_back, OtoroshimodelsESKPAlgoSettings):
            sec_com_algo_challenge_oto_to_back = self.sec_com_algo_challenge_oto_to_back.to_dict()

        elif isinstance(self.sec_com_algo_challenge_oto_to_back, OtoroshimodelsHSAlgoSettings):
            sec_com_algo_challenge_oto_to_back = self.sec_com_algo_challenge_oto_to_back.to_dict()

        elif isinstance(self.sec_com_algo_challenge_oto_to_back, OtoroshimodelsJWKSAlgoSettings):
            sec_com_algo_challenge_oto_to_back = self.sec_com_algo_challenge_oto_to_back.to_dict()

        elif isinstance(self.sec_com_algo_challenge_oto_to_back, OtoroshimodelsKidAlgoSettings):
            sec_com_algo_challenge_oto_to_back = self.sec_com_algo_challenge_oto_to_back.to_dict()

        elif isinstance(self.sec_com_algo_challenge_oto_to_back, OtoroshimodelsRSAKPAlgoSettings):
            sec_com_algo_challenge_oto_to_back = self.sec_com_algo_challenge_oto_to_back.to_dict()

        else:
            sec_com_algo_challenge_oto_to_back = self.sec_com_algo_challenge_oto_to_back.to_dict()

        api_key_constraints: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.api_key_constraints, Unset):
            api_key_constraints = self.api_key_constraints.to_dict()

        env = self.env
        x_forwarded_headers = self.x_forwarded_headers
        transformer_refs: Union[Unset, List[str]] = UNSET
        if not isinstance(self.transformer_refs, Unset):
            transformer_refs = self.transformer_refs

        enabled = self.enabled
        gzip: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.gzip, Unset):
            gzip = self.gzip.to_dict()

        send_info_token = self.send_info_token
        tcp_udp_tunneling = self.tcp_udp_tunneling
        remove_headers_out: Union[Unset, List[str]] = UNSET
        if not isinstance(self.remove_headers_out, Unset):
            remove_headers_out = self.remove_headers_out

        use_akka_http_client = self.use_akka_http_client
        maintenance_mode = self.maintenance_mode
        id = self.id
        remove_headers_in: Union[Unset, List[str]] = UNSET
        if not isinstance(self.remove_headers_in, Unset):
            remove_headers_in = self.remove_headers_in

        log_analytics_on_server = self.log_analytics_on_server
        sec_com_algo_info_token: Union[Dict[str, Any], Unset]
        if isinstance(self.sec_com_algo_info_token, Unset):
            sec_com_algo_info_token = UNSET
        elif isinstance(self.sec_com_algo_info_token, OtoroshimodelsESAlgoSettings):
            sec_com_algo_info_token = self.sec_com_algo_info_token.to_dict()

        elif isinstance(self.sec_com_algo_info_token, OtoroshimodelsESKPAlgoSettings):
            sec_com_algo_info_token = self.sec_com_algo_info_token.to_dict()

        elif isinstance(self.sec_com_algo_info_token, OtoroshimodelsHSAlgoSettings):
            sec_com_algo_info_token = self.sec_com_algo_info_token.to_dict()

        elif isinstance(self.sec_com_algo_info_token, OtoroshimodelsJWKSAlgoSettings):
            sec_com_algo_info_token = self.sec_com_algo_info_token.to_dict()

        elif isinstance(self.sec_com_algo_info_token, OtoroshimodelsKidAlgoSettings):
            sec_com_algo_info_token = self.sec_com_algo_info_token.to_dict()

        elif isinstance(self.sec_com_algo_info_token, OtoroshimodelsRSAKPAlgoSettings):
            sec_com_algo_info_token = self.sec_com_algo_info_token.to_dict()

        else:
            sec_com_algo_info_token = self.sec_com_algo_info_token.to_dict()

        user_facing = self.user_facing
        transformer_config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.transformer_config, Unset):
            transformer_config = self.transformer_config.to_dict()

        client_validator_ref: Union[Dict[str, Any], Unset, str]
        if isinstance(self.client_validator_ref, Unset):
            client_validator_ref = UNSET
        elif isinstance(self.client_validator_ref, Null):
            client_validator_ref = UNSET
            if not isinstance(self.client_validator_ref, Unset):
                client_validator_ref = self.client_validator_ref.to_dict()

        else:
            client_validator_ref = self.client_validator_ref

        security_excluded_patterns: Union[Unset, List[str]] = UNSET
        if not isinstance(self.security_excluded_patterns, Unset):
            security_excluded_patterns = self.security_excluded_patterns

        ip_filtering: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ip_filtering, Unset):
            ip_filtering = self.ip_filtering.to_dict()

        targets: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.targets, Unset):
            targets = []
            for targets_item_data in self.targets:
                targets_item = targets_item_data.to_dict()

                targets.append(targets_item)

        redirection: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.redirection, Unset):
            redirection = self.redirection.to_dict()

        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        restrictions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.restrictions, Unset):
            restrictions = self.restrictions.to_dict()

        override_host = self.override_host
        access_validator: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.access_validator, Unset):
            access_validator = self.access_validator.to_dict()

        send_state_challenge = self.send_state_challenge
        chaos_config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.chaos_config, Unset):
            chaos_config = self.chaos_config.to_dict()

        sec_com_info_token_version: Union[Unset, str] = UNSET
        if not isinstance(self.sec_com_info_token_version, Unset):
            sec_com_info_token_version = self.sec_com_info_token_version.value

        additional_headers_out: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.additional_headers_out, Unset):
            additional_headers_out = self.additional_headers_out.to_dict()

        sec_com_headers: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sec_com_headers, Unset):
            sec_com_headers = self.sec_com_headers.to_dict()

        matching_headers: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.matching_headers, Unset):
            matching_headers = self.matching_headers.to_dict()

        sec_com_algo_challenge_back_to_oto: Union[Dict[str, Any], Unset]
        if isinstance(self.sec_com_algo_challenge_back_to_oto, Unset):
            sec_com_algo_challenge_back_to_oto = UNSET
        elif isinstance(self.sec_com_algo_challenge_back_to_oto, OtoroshimodelsESAlgoSettings):
            sec_com_algo_challenge_back_to_oto = self.sec_com_algo_challenge_back_to_oto.to_dict()

        elif isinstance(self.sec_com_algo_challenge_back_to_oto, OtoroshimodelsESKPAlgoSettings):
            sec_com_algo_challenge_back_to_oto = self.sec_com_algo_challenge_back_to_oto.to_dict()

        elif isinstance(self.sec_com_algo_challenge_back_to_oto, OtoroshimodelsHSAlgoSettings):
            sec_com_algo_challenge_back_to_oto = self.sec_com_algo_challenge_back_to_oto.to_dict()

        elif isinstance(self.sec_com_algo_challenge_back_to_oto, OtoroshimodelsJWKSAlgoSettings):
            sec_com_algo_challenge_back_to_oto = self.sec_com_algo_challenge_back_to_oto.to_dict()

        elif isinstance(self.sec_com_algo_challenge_back_to_oto, OtoroshimodelsKidAlgoSettings):
            sec_com_algo_challenge_back_to_oto = self.sec_com_algo_challenge_back_to_oto.to_dict()

        elif isinstance(self.sec_com_algo_challenge_back_to_oto, OtoroshimodelsRSAKPAlgoSettings):
            sec_com_algo_challenge_back_to_oto = self.sec_com_algo_challenge_back_to_oto.to_dict()

        else:
            sec_com_algo_challenge_back_to_oto = self.sec_com_algo_challenge_back_to_oto.to_dict()

        sec_com_use_same_algo = self.sec_com_use_same_algo
        use_new_ws_client = self.use_new_ws_client
        sec_com_excluded_patterns: Union[Unset, List[str]] = UNSET
        if not isinstance(self.sec_com_excluded_patterns, Unset):
            sec_com_excluded_patterns = self.sec_com_excluded_patterns

        redirect_to_local = self.redirect_to_local
        enforce_secure_communication = self.enforce_secure_communication
        missing_only_headers_out: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.missing_only_headers_out, Unset):
            missing_only_headers_out = self.missing_only_headers_out.to_dict()

        sec_com_settings: Union[Dict[str, Any], Unset]
        if isinstance(self.sec_com_settings, Unset):
            sec_com_settings = UNSET
        elif isinstance(self.sec_com_settings, OtoroshimodelsESAlgoSettings):
            sec_com_settings = self.sec_com_settings.to_dict()

        elif isinstance(self.sec_com_settings, OtoroshimodelsESKPAlgoSettings):
            sec_com_settings = self.sec_com_settings.to_dict()

        elif isinstance(self.sec_com_settings, OtoroshimodelsHSAlgoSettings):
            sec_com_settings = self.sec_com_settings.to_dict()

        elif isinstance(self.sec_com_settings, OtoroshimodelsJWKSAlgoSettings):
            sec_com_settings = self.sec_com_settings.to_dict()

        elif isinstance(self.sec_com_settings, OtoroshimodelsKidAlgoSettings):
            sec_com_settings = self.sec_com_settings.to_dict()

        elif isinstance(self.sec_com_settings, OtoroshimodelsRSAKPAlgoSettings):
            sec_com_settings = self.sec_com_settings.to_dict()

        else:
            sec_com_settings = self.sec_com_settings.to_dict()

        handle_legacy_domain = self.handle_legacy_domain
        canary: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.canary, Unset):
            canary = self.canary.to_dict()

        location: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict()

        plugins: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.plugins, Unset):
            plugins = self.plugins.to_dict()

        sec_com_ttl = self.sec_com_ttl
        description = self.description
        sec_com_version: Union[Unset, str] = UNSET
        if not isinstance(self.sec_com_version, Unset):
            sec_com_version = self.sec_com_version.value

        pre_routing: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pre_routing, Unset):
            pre_routing = self.pre_routing.to_dict()

        groups: Union[Unset, List[str]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = self.groups

        read_only = self.read_only
        private_patterns: Union[Unset, List[str]] = UNSET
        if not isinstance(self.private_patterns, Unset):
            private_patterns = self.private_patterns

        targets_load_balancing: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.targets_load_balancing, Unset):
            targets_load_balancing = self.targets_load_balancing.to_dict()

        cors: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cors, Unset):
            cors = self.cors.to_dict()

        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        public_patterns: Union[Unset, List[str]] = UNSET
        if not isinstance(self.public_patterns, Unset):
            public_patterns = self.public_patterns

        api: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.api, Unset):
            api = self.api.to_dict()

        missing_only_headers_in: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.missing_only_headers_in, Unset):
            missing_only_headers_in = self.missing_only_headers_in.to_dict()

        issue_cert = self.issue_cert
        headers_verification: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.headers_verification, Unset):
            headers_verification = self.headers_verification.to_dict()

        jwt_verifier: Union[Dict[str, Any], Unset]
        if isinstance(self.jwt_verifier, Unset):
            jwt_verifier = UNSET
        elif isinstance(self.jwt_verifier, OtoroshimodelsGlobalJwtVerifier):
            jwt_verifier = self.jwt_verifier.to_dict()

        elif isinstance(self.jwt_verifier, OtoroshimodelsLocalJwtVerifier):
            jwt_verifier = self.jwt_verifier.to_dict()

        else:
            jwt_verifier = self.jwt_verifier.to_dict()

        lets_encrypt = self.lets_encrypt

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if build_mode is not UNSET:
            field_dict["buildMode"] = build_mode
        if hosts is not UNSET:
            field_dict["hosts"] = hosts
        if private_app is not UNSET:
            field_dict["privateApp"] = private_app
        if local_scheme is not UNSET:
            field_dict["localScheme"] = local_scheme
        if auth_config_ref is not UNSET:
            field_dict["authConfigRef"] = auth_config_ref
        if issue_cert_ca is not UNSET:
            field_dict["issueCertCA"] = issue_cert_ca
        if root is not UNSET:
            field_dict["root"] = root
        if name is not UNSET:
            field_dict["name"] = name
        if additional_headers is not UNSET:
            field_dict["additionalHeaders"] = additional_headers
        if domain is not UNSET:
            field_dict["domain"] = domain
        if client_config is not UNSET:
            field_dict["clientConfig"] = client_config
        if matching_root is not UNSET:
            field_dict["matchingRoot"] = matching_root
        if force_https is not UNSET:
            field_dict["forceHttps"] = force_https
        if local_host is not UNSET:
            field_dict["localHost"] = local_host
        if send_otoroshi_headers_back is not UNSET:
            field_dict["sendOtoroshiHeadersBack"] = send_otoroshi_headers_back
        if health_check is not UNSET:
            field_dict["healthCheck"] = health_check
        if strictly_private is not UNSET:
            field_dict["strictlyPrivate"] = strictly_private
        if detect_api_key_sooner is not UNSET:
            field_dict["detectApiKeySooner"] = detect_api_key_sooner
        if allow_http_10 is not UNSET:
            field_dict["allowHttp10"] = allow_http_10
        if subdomain is not UNSET:
            field_dict["subdomain"] = subdomain
        if paths is not UNSET:
            field_dict["paths"] = paths
        if strip_path is not UNSET:
            field_dict["stripPath"] = strip_path
        if sec_com_algo_challenge_oto_to_back is not UNSET:
            field_dict["secComAlgoChallengeOtoToBack"] = sec_com_algo_challenge_oto_to_back
        if api_key_constraints is not UNSET:
            field_dict["apiKeyConstraints"] = api_key_constraints
        if env is not UNSET:
            field_dict["env"] = env
        if x_forwarded_headers is not UNSET:
            field_dict["xForwardedHeaders"] = x_forwarded_headers
        if transformer_refs is not UNSET:
            field_dict["transformerRefs"] = transformer_refs
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if gzip is not UNSET:
            field_dict["gzip"] = gzip
        if send_info_token is not UNSET:
            field_dict["sendInfoToken"] = send_info_token
        if tcp_udp_tunneling is not UNSET:
            field_dict["tcpUdpTunneling"] = tcp_udp_tunneling
        if remove_headers_out is not UNSET:
            field_dict["removeHeadersOut"] = remove_headers_out
        if use_akka_http_client is not UNSET:
            field_dict["useAkkaHttpClient"] = use_akka_http_client
        if maintenance_mode is not UNSET:
            field_dict["maintenanceMode"] = maintenance_mode
        if id is not UNSET:
            field_dict["id"] = id
        if remove_headers_in is not UNSET:
            field_dict["removeHeadersIn"] = remove_headers_in
        if log_analytics_on_server is not UNSET:
            field_dict["logAnalyticsOnServer"] = log_analytics_on_server
        if sec_com_algo_info_token is not UNSET:
            field_dict["secComAlgoInfoToken"] = sec_com_algo_info_token
        if user_facing is not UNSET:
            field_dict["userFacing"] = user_facing
        if transformer_config is not UNSET:
            field_dict["transformerConfig"] = transformer_config
        if client_validator_ref is not UNSET:
            field_dict["clientValidatorRef"] = client_validator_ref
        if security_excluded_patterns is not UNSET:
            field_dict["securityExcludedPatterns"] = security_excluded_patterns
        if ip_filtering is not UNSET:
            field_dict["ipFiltering"] = ip_filtering
        if targets is not UNSET:
            field_dict["targets"] = targets
        if redirection is not UNSET:
            field_dict["redirection"] = redirection
        if tags is not UNSET:
            field_dict["tags"] = tags
        if restrictions is not UNSET:
            field_dict["restrictions"] = restrictions
        if override_host is not UNSET:
            field_dict["overrideHost"] = override_host
        if access_validator is not UNSET:
            field_dict["accessValidator"] = access_validator
        if send_state_challenge is not UNSET:
            field_dict["sendStateChallenge"] = send_state_challenge
        if chaos_config is not UNSET:
            field_dict["chaosConfig"] = chaos_config
        if sec_com_info_token_version is not UNSET:
            field_dict["secComInfoTokenVersion"] = sec_com_info_token_version
        if additional_headers_out is not UNSET:
            field_dict["additionalHeadersOut"] = additional_headers_out
        if sec_com_headers is not UNSET:
            field_dict["secComHeaders"] = sec_com_headers
        if matching_headers is not UNSET:
            field_dict["matchingHeaders"] = matching_headers
        if sec_com_algo_challenge_back_to_oto is not UNSET:
            field_dict["secComAlgoChallengeBackToOto"] = sec_com_algo_challenge_back_to_oto
        if sec_com_use_same_algo is not UNSET:
            field_dict["secComUseSameAlgo"] = sec_com_use_same_algo
        if use_new_ws_client is not UNSET:
            field_dict["useNewWSClient"] = use_new_ws_client
        if sec_com_excluded_patterns is not UNSET:
            field_dict["secComExcludedPatterns"] = sec_com_excluded_patterns
        if redirect_to_local is not UNSET:
            field_dict["redirectToLocal"] = redirect_to_local
        if enforce_secure_communication is not UNSET:
            field_dict["enforceSecureCommunication"] = enforce_secure_communication
        if missing_only_headers_out is not UNSET:
            field_dict["missingOnlyHeadersOut"] = missing_only_headers_out
        if sec_com_settings is not UNSET:
            field_dict["secComSettings"] = sec_com_settings
        if handle_legacy_domain is not UNSET:
            field_dict["handleLegacyDomain"] = handle_legacy_domain
        if canary is not UNSET:
            field_dict["canary"] = canary
        if location is not UNSET:
            field_dict["location"] = location
        if plugins is not UNSET:
            field_dict["plugins"] = plugins
        if sec_com_ttl is not UNSET:
            field_dict["secComTtl"] = sec_com_ttl
        if description is not UNSET:
            field_dict["description"] = description
        if sec_com_version is not UNSET:
            field_dict["secComVersion"] = sec_com_version
        if pre_routing is not UNSET:
            field_dict["preRouting"] = pre_routing
        if groups is not UNSET:
            field_dict["groups"] = groups
        if read_only is not UNSET:
            field_dict["readOnly"] = read_only
        if private_patterns is not UNSET:
            field_dict["privatePatterns"] = private_patterns
        if targets_load_balancing is not UNSET:
            field_dict["targetsLoadBalancing"] = targets_load_balancing
        if cors is not UNSET:
            field_dict["cors"] = cors
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if public_patterns is not UNSET:
            field_dict["publicPatterns"] = public_patterns
        if api is not UNSET:
            field_dict["api"] = api
        if missing_only_headers_in is not UNSET:
            field_dict["missingOnlyHeadersIn"] = missing_only_headers_in
        if issue_cert is not UNSET:
            field_dict["issueCert"] = issue_cert
        if headers_verification is not UNSET:
            field_dict["headersVerification"] = headers_verification
        if jwt_verifier is not UNSET:
            field_dict["jwtVerifier"] = jwt_verifier
        if lets_encrypt is not UNSET:
            field_dict["letsEncrypt"] = lets_encrypt

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        build_mode = d.pop("buildMode", UNSET)

        hosts = cast(List[str], d.pop("hosts", UNSET))

        private_app = d.pop("privateApp", UNSET)

        local_scheme = d.pop("localScheme", UNSET)

        def _parse_auth_config_ref(data: object) -> Union[Null, Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _auth_config_ref_type_0 = data
                auth_config_ref_type_0: Union[Unset, Null]
                if isinstance(_auth_config_ref_type_0, Unset):
                    auth_config_ref_type_0 = UNSET
                else:
                    auth_config_ref_type_0 = Null.from_dict(_auth_config_ref_type_0)

                return auth_config_ref_type_0
            except:  # noqa: E722
                pass
            return cast(Union[Null, Unset, str], data)

        auth_config_ref = _parse_auth_config_ref(d.pop("authConfigRef", UNSET))

        def _parse_issue_cert_ca(data: object) -> Union[Null, Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _issue_cert_ca_type_0 = data
                issue_cert_ca_type_0: Union[Unset, Null]
                if isinstance(_issue_cert_ca_type_0, Unset):
                    issue_cert_ca_type_0 = UNSET
                else:
                    issue_cert_ca_type_0 = Null.from_dict(_issue_cert_ca_type_0)

                return issue_cert_ca_type_0
            except:  # noqa: E722
                pass
            return cast(Union[Null, Unset, str], data)

        issue_cert_ca = _parse_issue_cert_ca(d.pop("issueCertCA", UNSET))

        root = d.pop("root", UNSET)

        name = d.pop("name", UNSET)

        _additional_headers = d.pop("additionalHeaders", UNSET)
        additional_headers: Union[Unset, OtoroshimodelsServiceDescriptorAdditionalHeaders]
        if isinstance(_additional_headers, Unset):
            additional_headers = UNSET
        else:
            additional_headers = OtoroshimodelsServiceDescriptorAdditionalHeaders.from_dict(_additional_headers)

        domain = d.pop("domain", UNSET)

        _client_config = d.pop("clientConfig", UNSET)
        client_config: Union[Unset, OtoroshimodelsClientConfig]
        if isinstance(_client_config, Unset):
            client_config = UNSET
        else:
            client_config = OtoroshimodelsClientConfig.from_dict(_client_config)

        def _parse_matching_root(data: object) -> Union[Null, Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _matching_root_type_0 = data
                matching_root_type_0: Union[Unset, Null]
                if isinstance(_matching_root_type_0, Unset):
                    matching_root_type_0 = UNSET
                else:
                    matching_root_type_0 = Null.from_dict(_matching_root_type_0)

                return matching_root_type_0
            except:  # noqa: E722
                pass
            return cast(Union[Null, Unset, str], data)

        matching_root = _parse_matching_root(d.pop("matchingRoot", UNSET))

        force_https = d.pop("forceHttps", UNSET)

        local_host = d.pop("localHost", UNSET)

        send_otoroshi_headers_back = d.pop("sendOtoroshiHeadersBack", UNSET)

        _health_check = d.pop("healthCheck", UNSET)
        health_check: Union[Unset, OtoroshimodelsHealthCheck]
        if isinstance(_health_check, Unset):
            health_check = UNSET
        else:
            health_check = OtoroshimodelsHealthCheck.from_dict(_health_check)

        strictly_private = d.pop("strictlyPrivate", UNSET)

        detect_api_key_sooner = d.pop("detectApiKeySooner", UNSET)

        allow_http_10 = d.pop("allowHttp10", UNSET)

        subdomain = d.pop("subdomain", UNSET)

        paths = cast(List[str], d.pop("paths", UNSET))

        strip_path = d.pop("stripPath", UNSET)

        def _parse_sec_com_algo_challenge_oto_to_back(
            data: object,
        ) -> Union[
            OtoroshimodelsESAlgoSettings,
            OtoroshimodelsESKPAlgoSettings,
            OtoroshimodelsHSAlgoSettings,
            OtoroshimodelsJWKSAlgoSettings,
            OtoroshimodelsKidAlgoSettings,
            OtoroshimodelsRSAKPAlgoSettings,
            OtoroshimodelsRSAlgoSettings,
            Unset,
        ]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasotoroshimodels_algo_settings_type_0 = OtoroshimodelsESAlgoSettings.from_dict(data)

                return componentsschemasotoroshimodels_algo_settings_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasotoroshimodels_algo_settings_type_1 = OtoroshimodelsESKPAlgoSettings.from_dict(data)

                return componentsschemasotoroshimodels_algo_settings_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasotoroshimodels_algo_settings_type_2 = OtoroshimodelsHSAlgoSettings.from_dict(data)

                return componentsschemasotoroshimodels_algo_settings_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasotoroshimodels_algo_settings_type_3 = OtoroshimodelsJWKSAlgoSettings.from_dict(data)

                return componentsschemasotoroshimodels_algo_settings_type_3
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasotoroshimodels_algo_settings_type_4 = OtoroshimodelsKidAlgoSettings.from_dict(data)

                return componentsschemasotoroshimodels_algo_settings_type_4
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasotoroshimodels_algo_settings_type_5 = OtoroshimodelsRSAKPAlgoSettings.from_dict(data)

                return componentsschemasotoroshimodels_algo_settings_type_5
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemasotoroshimodels_algo_settings_type_6 = OtoroshimodelsRSAlgoSettings.from_dict(data)

            return componentsschemasotoroshimodels_algo_settings_type_6

        sec_com_algo_challenge_oto_to_back = _parse_sec_com_algo_challenge_oto_to_back(
            d.pop("secComAlgoChallengeOtoToBack", UNSET)
        )

        _api_key_constraints = d.pop("apiKeyConstraints", UNSET)
        api_key_constraints: Union[Unset, OtoroshimodelsApiKeyConstraints]
        if isinstance(_api_key_constraints, Unset):
            api_key_constraints = UNSET
        else:
            api_key_constraints = OtoroshimodelsApiKeyConstraints.from_dict(_api_key_constraints)

        env = d.pop("env", UNSET)

        x_forwarded_headers = d.pop("xForwardedHeaders", UNSET)

        transformer_refs = cast(List[str], d.pop("transformerRefs", UNSET))

        enabled = d.pop("enabled", UNSET)

        _gzip = d.pop("gzip", UNSET)
        gzip: Union[Unset, OtoroshiutilsgzipGzipConfig]
        if isinstance(_gzip, Unset):
            gzip = UNSET
        else:
            gzip = OtoroshiutilsgzipGzipConfig.from_dict(_gzip)

        send_info_token = d.pop("sendInfoToken", UNSET)

        tcp_udp_tunneling = d.pop("tcpUdpTunneling", UNSET)

        remove_headers_out = cast(List[str], d.pop("removeHeadersOut", UNSET))

        use_akka_http_client = d.pop("useAkkaHttpClient", UNSET)

        maintenance_mode = d.pop("maintenanceMode", UNSET)

        id = d.pop("id", UNSET)

        remove_headers_in = cast(List[str], d.pop("removeHeadersIn", UNSET))

        log_analytics_on_server = d.pop("logAnalyticsOnServer", UNSET)

        def _parse_sec_com_algo_info_token(
            data: object,
        ) -> Union[
            OtoroshimodelsESAlgoSettings,
            OtoroshimodelsESKPAlgoSettings,
            OtoroshimodelsHSAlgoSettings,
            OtoroshimodelsJWKSAlgoSettings,
            OtoroshimodelsKidAlgoSettings,
            OtoroshimodelsRSAKPAlgoSettings,
            OtoroshimodelsRSAlgoSettings,
            Unset,
        ]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasotoroshimodels_algo_settings_type_0 = OtoroshimodelsESAlgoSettings.from_dict(data)

                return componentsschemasotoroshimodels_algo_settings_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasotoroshimodels_algo_settings_type_1 = OtoroshimodelsESKPAlgoSettings.from_dict(data)

                return componentsschemasotoroshimodels_algo_settings_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasotoroshimodels_algo_settings_type_2 = OtoroshimodelsHSAlgoSettings.from_dict(data)

                return componentsschemasotoroshimodels_algo_settings_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasotoroshimodels_algo_settings_type_3 = OtoroshimodelsJWKSAlgoSettings.from_dict(data)

                return componentsschemasotoroshimodels_algo_settings_type_3
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasotoroshimodels_algo_settings_type_4 = OtoroshimodelsKidAlgoSettings.from_dict(data)

                return componentsschemasotoroshimodels_algo_settings_type_4
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasotoroshimodels_algo_settings_type_5 = OtoroshimodelsRSAKPAlgoSettings.from_dict(data)

                return componentsschemasotoroshimodels_algo_settings_type_5
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemasotoroshimodels_algo_settings_type_6 = OtoroshimodelsRSAlgoSettings.from_dict(data)

            return componentsschemasotoroshimodels_algo_settings_type_6

        sec_com_algo_info_token = _parse_sec_com_algo_info_token(d.pop("secComAlgoInfoToken", UNSET))

        user_facing = d.pop("userFacing", UNSET)

        _transformer_config = d.pop("transformerConfig", UNSET)
        transformer_config: Union[Unset, OtoroshimodelsServiceDescriptorTransformerConfig]
        if isinstance(_transformer_config, Unset):
            transformer_config = UNSET
        else:
            transformer_config = OtoroshimodelsServiceDescriptorTransformerConfig.from_dict(_transformer_config)

        def _parse_client_validator_ref(data: object) -> Union[Null, Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _client_validator_ref_type_0 = data
                client_validator_ref_type_0: Union[Unset, Null]
                if isinstance(_client_validator_ref_type_0, Unset):
                    client_validator_ref_type_0 = UNSET
                else:
                    client_validator_ref_type_0 = Null.from_dict(_client_validator_ref_type_0)

                return client_validator_ref_type_0
            except:  # noqa: E722
                pass
            return cast(Union[Null, Unset, str], data)

        client_validator_ref = _parse_client_validator_ref(d.pop("clientValidatorRef", UNSET))

        security_excluded_patterns = cast(List[str], d.pop("securityExcludedPatterns", UNSET))

        _ip_filtering = d.pop("ipFiltering", UNSET)
        ip_filtering: Union[Unset, OtoroshimodelsIpFiltering]
        if isinstance(_ip_filtering, Unset):
            ip_filtering = UNSET
        else:
            ip_filtering = OtoroshimodelsIpFiltering.from_dict(_ip_filtering)

        targets = []
        _targets = d.pop("targets", UNSET)
        for targets_item_data in _targets or []:
            targets_item = OtoroshimodelsTarget.from_dict(targets_item_data)

            targets.append(targets_item)

        _redirection = d.pop("redirection", UNSET)
        redirection: Union[Unset, OtoroshimodelsRedirectionSettings]
        if isinstance(_redirection, Unset):
            redirection = UNSET
        else:
            redirection = OtoroshimodelsRedirectionSettings.from_dict(_redirection)

        tags = cast(List[str], d.pop("tags", UNSET))

        _restrictions = d.pop("restrictions", UNSET)
        restrictions: Union[Unset, OtoroshimodelsRestrictions]
        if isinstance(_restrictions, Unset):
            restrictions = UNSET
        else:
            restrictions = OtoroshimodelsRestrictions.from_dict(_restrictions)

        override_host = d.pop("overrideHost", UNSET)

        _access_validator = d.pop("accessValidator", UNSET)
        access_validator: Union[Unset, OtoroshiscriptAccessValidatorRef]
        if isinstance(_access_validator, Unset):
            access_validator = UNSET
        else:
            access_validator = OtoroshiscriptAccessValidatorRef.from_dict(_access_validator)

        send_state_challenge = d.pop("sendStateChallenge", UNSET)

        _chaos_config = d.pop("chaosConfig", UNSET)
        chaos_config: Union[Unset, OtoroshimodelsChaosConfig]
        if isinstance(_chaos_config, Unset):
            chaos_config = UNSET
        else:
            chaos_config = OtoroshimodelsChaosConfig.from_dict(_chaos_config)

        _sec_com_info_token_version = d.pop("secComInfoTokenVersion", UNSET)
        sec_com_info_token_version: Union[Unset, OtoroshimodelsSecComInfoTokenVersion]
        if isinstance(_sec_com_info_token_version, Unset):
            sec_com_info_token_version = UNSET
        else:
            sec_com_info_token_version = OtoroshimodelsSecComInfoTokenVersion(_sec_com_info_token_version)

        _additional_headers_out = d.pop("additionalHeadersOut", UNSET)
        additional_headers_out: Union[Unset, OtoroshimodelsServiceDescriptorAdditionalHeadersOut]
        if isinstance(_additional_headers_out, Unset):
            additional_headers_out = UNSET
        else:
            additional_headers_out = OtoroshimodelsServiceDescriptorAdditionalHeadersOut.from_dict(
                _additional_headers_out
            )

        _sec_com_headers = d.pop("secComHeaders", UNSET)
        sec_com_headers: Union[Unset, OtoroshimodelsSecComHeaders]
        if isinstance(_sec_com_headers, Unset):
            sec_com_headers = UNSET
        else:
            sec_com_headers = OtoroshimodelsSecComHeaders.from_dict(_sec_com_headers)

        _matching_headers = d.pop("matchingHeaders", UNSET)
        matching_headers: Union[Unset, OtoroshimodelsServiceDescriptorMatchingHeaders]
        if isinstance(_matching_headers, Unset):
            matching_headers = UNSET
        else:
            matching_headers = OtoroshimodelsServiceDescriptorMatchingHeaders.from_dict(_matching_headers)

        def _parse_sec_com_algo_challenge_back_to_oto(
            data: object,
        ) -> Union[
            OtoroshimodelsESAlgoSettings,
            OtoroshimodelsESKPAlgoSettings,
            OtoroshimodelsHSAlgoSettings,
            OtoroshimodelsJWKSAlgoSettings,
            OtoroshimodelsKidAlgoSettings,
            OtoroshimodelsRSAKPAlgoSettings,
            OtoroshimodelsRSAlgoSettings,
            Unset,
        ]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasotoroshimodels_algo_settings_type_0 = OtoroshimodelsESAlgoSettings.from_dict(data)

                return componentsschemasotoroshimodels_algo_settings_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasotoroshimodels_algo_settings_type_1 = OtoroshimodelsESKPAlgoSettings.from_dict(data)

                return componentsschemasotoroshimodels_algo_settings_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasotoroshimodels_algo_settings_type_2 = OtoroshimodelsHSAlgoSettings.from_dict(data)

                return componentsschemasotoroshimodels_algo_settings_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasotoroshimodels_algo_settings_type_3 = OtoroshimodelsJWKSAlgoSettings.from_dict(data)

                return componentsschemasotoroshimodels_algo_settings_type_3
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasotoroshimodels_algo_settings_type_4 = OtoroshimodelsKidAlgoSettings.from_dict(data)

                return componentsschemasotoroshimodels_algo_settings_type_4
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasotoroshimodels_algo_settings_type_5 = OtoroshimodelsRSAKPAlgoSettings.from_dict(data)

                return componentsschemasotoroshimodels_algo_settings_type_5
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemasotoroshimodels_algo_settings_type_6 = OtoroshimodelsRSAlgoSettings.from_dict(data)

            return componentsschemasotoroshimodels_algo_settings_type_6

        sec_com_algo_challenge_back_to_oto = _parse_sec_com_algo_challenge_back_to_oto(
            d.pop("secComAlgoChallengeBackToOto", UNSET)
        )

        sec_com_use_same_algo = d.pop("secComUseSameAlgo", UNSET)

        use_new_ws_client = d.pop("useNewWSClient", UNSET)

        sec_com_excluded_patterns = cast(List[str], d.pop("secComExcludedPatterns", UNSET))

        redirect_to_local = d.pop("redirectToLocal", UNSET)

        enforce_secure_communication = d.pop("enforceSecureCommunication", UNSET)

        _missing_only_headers_out = d.pop("missingOnlyHeadersOut", UNSET)
        missing_only_headers_out: Union[Unset, OtoroshimodelsServiceDescriptorMissingOnlyHeadersOut]
        if isinstance(_missing_only_headers_out, Unset):
            missing_only_headers_out = UNSET
        else:
            missing_only_headers_out = OtoroshimodelsServiceDescriptorMissingOnlyHeadersOut.from_dict(
                _missing_only_headers_out
            )

        def _parse_sec_com_settings(
            data: object,
        ) -> Union[
            OtoroshimodelsESAlgoSettings,
            OtoroshimodelsESKPAlgoSettings,
            OtoroshimodelsHSAlgoSettings,
            OtoroshimodelsJWKSAlgoSettings,
            OtoroshimodelsKidAlgoSettings,
            OtoroshimodelsRSAKPAlgoSettings,
            OtoroshimodelsRSAlgoSettings,
            Unset,
        ]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasotoroshimodels_algo_settings_type_0 = OtoroshimodelsESAlgoSettings.from_dict(data)

                return componentsschemasotoroshimodels_algo_settings_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasotoroshimodels_algo_settings_type_1 = OtoroshimodelsESKPAlgoSettings.from_dict(data)

                return componentsschemasotoroshimodels_algo_settings_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasotoroshimodels_algo_settings_type_2 = OtoroshimodelsHSAlgoSettings.from_dict(data)

                return componentsschemasotoroshimodels_algo_settings_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasotoroshimodels_algo_settings_type_3 = OtoroshimodelsJWKSAlgoSettings.from_dict(data)

                return componentsschemasotoroshimodels_algo_settings_type_3
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasotoroshimodels_algo_settings_type_4 = OtoroshimodelsKidAlgoSettings.from_dict(data)

                return componentsschemasotoroshimodels_algo_settings_type_4
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasotoroshimodels_algo_settings_type_5 = OtoroshimodelsRSAKPAlgoSettings.from_dict(data)

                return componentsschemasotoroshimodels_algo_settings_type_5
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemasotoroshimodels_algo_settings_type_6 = OtoroshimodelsRSAlgoSettings.from_dict(data)

            return componentsschemasotoroshimodels_algo_settings_type_6

        sec_com_settings = _parse_sec_com_settings(d.pop("secComSettings", UNSET))

        handle_legacy_domain = d.pop("handleLegacyDomain", UNSET)

        _canary = d.pop("canary", UNSET)
        canary: Union[Unset, OtoroshimodelsCanary]
        if isinstance(_canary, Unset):
            canary = UNSET
        else:
            canary = OtoroshimodelsCanary.from_dict(_canary)

        _location = d.pop("location", UNSET)
        location: Union[Unset, OtoroshimodelsEntityLocation]
        if isinstance(_location, Unset):
            location = UNSET
        else:
            location = OtoroshimodelsEntityLocation.from_dict(_location)

        _plugins = d.pop("plugins", UNSET)
        plugins: Union[Unset, OtoroshiscriptpluginsPlugins]
        if isinstance(_plugins, Unset):
            plugins = UNSET
        else:
            plugins = OtoroshiscriptpluginsPlugins.from_dict(_plugins)

        sec_com_ttl = d.pop("secComTtl", UNSET)

        description = d.pop("description", UNSET)

        _sec_com_version = d.pop("secComVersion", UNSET)
        sec_com_version: Union[Unset, OtoroshimodelsSecComVersion]
        if isinstance(_sec_com_version, Unset):
            sec_com_version = UNSET
        else:
            sec_com_version = OtoroshimodelsSecComVersion(_sec_com_version)

        _pre_routing = d.pop("preRouting", UNSET)
        pre_routing: Union[Unset, OtoroshiscriptPreRoutingRef]
        if isinstance(_pre_routing, Unset):
            pre_routing = UNSET
        else:
            pre_routing = OtoroshiscriptPreRoutingRef.from_dict(_pre_routing)

        groups = cast(List[str], d.pop("groups", UNSET))

        read_only = d.pop("readOnly", UNSET)

        private_patterns = cast(List[str], d.pop("privatePatterns", UNSET))

        _targets_load_balancing = d.pop("targetsLoadBalancing", UNSET)
        targets_load_balancing: Union[Unset, OtoroshimodelsLoadBalancing]
        if isinstance(_targets_load_balancing, Unset):
            targets_load_balancing = UNSET
        else:
            targets_load_balancing = OtoroshimodelsLoadBalancing.from_dict(_targets_load_balancing)

        _cors = d.pop("cors", UNSET)
        cors: Union[Unset, OtoroshimodelsCorsSettings]
        if isinstance(_cors, Unset):
            cors = UNSET
        else:
            cors = OtoroshimodelsCorsSettings.from_dict(_cors)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, OtoroshimodelsServiceDescriptorMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = OtoroshimodelsServiceDescriptorMetadata.from_dict(_metadata)

        public_patterns = cast(List[str], d.pop("publicPatterns", UNSET))

        _api = d.pop("api", UNSET)
        api: Union[Unset, OtoroshimodelsApiDescriptor]
        if isinstance(_api, Unset):
            api = UNSET
        else:
            api = OtoroshimodelsApiDescriptor.from_dict(_api)

        _missing_only_headers_in = d.pop("missingOnlyHeadersIn", UNSET)
        missing_only_headers_in: Union[Unset, OtoroshimodelsServiceDescriptorMissingOnlyHeadersIn]
        if isinstance(_missing_only_headers_in, Unset):
            missing_only_headers_in = UNSET
        else:
            missing_only_headers_in = OtoroshimodelsServiceDescriptorMissingOnlyHeadersIn.from_dict(
                _missing_only_headers_in
            )

        issue_cert = d.pop("issueCert", UNSET)

        _headers_verification = d.pop("headersVerification", UNSET)
        headers_verification: Union[Unset, OtoroshimodelsServiceDescriptorHeadersVerification]
        if isinstance(_headers_verification, Unset):
            headers_verification = UNSET
        else:
            headers_verification = OtoroshimodelsServiceDescriptorHeadersVerification.from_dict(_headers_verification)

        def _parse_jwt_verifier(
            data: object,
        ) -> Union[
            OtoroshimodelsGlobalJwtVerifier, OtoroshimodelsLocalJwtVerifier, OtoroshimodelsRefJwtVerifier, Unset
        ]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasotoroshimodels_jwt_verifier_type_0 = OtoroshimodelsGlobalJwtVerifier.from_dict(data)

                return componentsschemasotoroshimodels_jwt_verifier_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasotoroshimodels_jwt_verifier_type_1 = OtoroshimodelsLocalJwtVerifier.from_dict(data)

                return componentsschemasotoroshimodels_jwt_verifier_type_1
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemasotoroshimodels_jwt_verifier_type_2 = OtoroshimodelsRefJwtVerifier.from_dict(data)

            return componentsschemasotoroshimodels_jwt_verifier_type_2

        jwt_verifier = _parse_jwt_verifier(d.pop("jwtVerifier", UNSET))

        lets_encrypt = d.pop("letsEncrypt", UNSET)

        otoroshimodels_service_descriptor = cls(
            build_mode=build_mode,
            hosts=hosts,
            private_app=private_app,
            local_scheme=local_scheme,
            auth_config_ref=auth_config_ref,
            issue_cert_ca=issue_cert_ca,
            root=root,
            name=name,
            additional_headers=additional_headers,
            domain=domain,
            client_config=client_config,
            matching_root=matching_root,
            force_https=force_https,
            local_host=local_host,
            send_otoroshi_headers_back=send_otoroshi_headers_back,
            health_check=health_check,
            strictly_private=strictly_private,
            detect_api_key_sooner=detect_api_key_sooner,
            allow_http_10=allow_http_10,
            subdomain=subdomain,
            paths=paths,
            strip_path=strip_path,
            sec_com_algo_challenge_oto_to_back=sec_com_algo_challenge_oto_to_back,
            api_key_constraints=api_key_constraints,
            env=env,
            x_forwarded_headers=x_forwarded_headers,
            transformer_refs=transformer_refs,
            enabled=enabled,
            gzip=gzip,
            send_info_token=send_info_token,
            tcp_udp_tunneling=tcp_udp_tunneling,
            remove_headers_out=remove_headers_out,
            use_akka_http_client=use_akka_http_client,
            maintenance_mode=maintenance_mode,
            id=id,
            remove_headers_in=remove_headers_in,
            log_analytics_on_server=log_analytics_on_server,
            sec_com_algo_info_token=sec_com_algo_info_token,
            user_facing=user_facing,
            transformer_config=transformer_config,
            client_validator_ref=client_validator_ref,
            security_excluded_patterns=security_excluded_patterns,
            ip_filtering=ip_filtering,
            targets=targets,
            redirection=redirection,
            tags=tags,
            restrictions=restrictions,
            override_host=override_host,
            access_validator=access_validator,
            send_state_challenge=send_state_challenge,
            chaos_config=chaos_config,
            sec_com_info_token_version=sec_com_info_token_version,
            additional_headers_out=additional_headers_out,
            sec_com_headers=sec_com_headers,
            matching_headers=matching_headers,
            sec_com_algo_challenge_back_to_oto=sec_com_algo_challenge_back_to_oto,
            sec_com_use_same_algo=sec_com_use_same_algo,
            use_new_ws_client=use_new_ws_client,
            sec_com_excluded_patterns=sec_com_excluded_patterns,
            redirect_to_local=redirect_to_local,
            enforce_secure_communication=enforce_secure_communication,
            missing_only_headers_out=missing_only_headers_out,
            sec_com_settings=sec_com_settings,
            handle_legacy_domain=handle_legacy_domain,
            canary=canary,
            location=location,
            plugins=plugins,
            sec_com_ttl=sec_com_ttl,
            description=description,
            sec_com_version=sec_com_version,
            pre_routing=pre_routing,
            groups=groups,
            read_only=read_only,
            private_patterns=private_patterns,
            targets_load_balancing=targets_load_balancing,
            cors=cors,
            metadata=metadata,
            public_patterns=public_patterns,
            api=api,
            missing_only_headers_in=missing_only_headers_in,
            issue_cert=issue_cert,
            headers_verification=headers_verification,
            jwt_verifier=jwt_verifier,
            lets_encrypt=lets_encrypt,
        )

        otoroshimodels_service_descriptor.additional_properties = d
        return otoroshimodels_service_descriptor

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
