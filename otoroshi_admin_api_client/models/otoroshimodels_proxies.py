from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.null import Null
from ..models.playapilibsws_ws_proxy_server import PlayapilibswsWSProxyServer
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshimodelsProxies")


@attr.s(auto_attribs=True)
class OtoroshimodelsProxies:
    """Various web proxy settings for http client"""

    elastic: Union[Null, Union[Null, PlayapilibswsWSProxyServer], Unset] = UNSET
    events_webhooks: Union[Null, Union[Null, PlayapilibswsWSProxyServer], Unset] = UNSET
    jwk: Union[Null, Union[Null, PlayapilibswsWSProxyServer], Unset] = UNSET
    auth: Union[Null, Union[Null, PlayapilibswsWSProxyServer], Unset] = UNSET
    clevercloud: Union[Null, Union[Null, PlayapilibswsWSProxyServer], Unset] = UNSET
    alert_emails: Union[Null, Union[Null, PlayapilibswsWSProxyServer], Unset] = UNSET
    authority: Union[Null, Union[Null, PlayapilibswsWSProxyServer], Unset] = UNSET
    services: Union[Null, Union[Null, PlayapilibswsWSProxyServer], Unset] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        elastic: Union[Dict[str, Any], Unset]
        if isinstance(self.elastic, Unset):
            elastic = UNSET
        elif isinstance(self.elastic, Null):
            elastic = UNSET
            if not isinstance(self.elastic, Unset):
                elastic = self.elastic.to_dict()

        else:
            elastic
            if isinstance(self.elastic, Unset):
                elastic = UNSET
            elif isinstance(self.elastic, Null):
                elastic = UNSET
                if not isinstance(self.elastic, Unset):
                    elastic = self.elastic.to_dict()

            else:
                elastic = UNSET
                if not isinstance(self.elastic, Unset):
                    elastic = self.elastic.to_dict()

        events_webhooks: Union[Dict[str, Any], Unset]
        if isinstance(self.events_webhooks, Unset):
            events_webhooks = UNSET
        elif isinstance(self.events_webhooks, Null):
            events_webhooks = UNSET
            if not isinstance(self.events_webhooks, Unset):
                events_webhooks = self.events_webhooks.to_dict()

        else:
            events_webhooks
            if isinstance(self.events_webhooks, Unset):
                events_webhooks = UNSET
            elif isinstance(self.events_webhooks, Null):
                events_webhooks = UNSET
                if not isinstance(self.events_webhooks, Unset):
                    events_webhooks = self.events_webhooks.to_dict()

            else:
                events_webhooks = UNSET
                if not isinstance(self.events_webhooks, Unset):
                    events_webhooks = self.events_webhooks.to_dict()

        jwk: Union[Dict[str, Any], Unset]
        if isinstance(self.jwk, Unset):
            jwk = UNSET
        elif isinstance(self.jwk, Null):
            jwk = UNSET
            if not isinstance(self.jwk, Unset):
                jwk = self.jwk.to_dict()

        else:
            jwk
            if isinstance(self.jwk, Unset):
                jwk = UNSET
            elif isinstance(self.jwk, Null):
                jwk = UNSET
                if not isinstance(self.jwk, Unset):
                    jwk = self.jwk.to_dict()

            else:
                jwk = UNSET
                if not isinstance(self.jwk, Unset):
                    jwk = self.jwk.to_dict()

        auth: Union[Dict[str, Any], Unset]
        if isinstance(self.auth, Unset):
            auth = UNSET
        elif isinstance(self.auth, Null):
            auth = UNSET
            if not isinstance(self.auth, Unset):
                auth = self.auth.to_dict()

        else:
            auth
            if isinstance(self.auth, Unset):
                auth = UNSET
            elif isinstance(self.auth, Null):
                auth = UNSET
                if not isinstance(self.auth, Unset):
                    auth = self.auth.to_dict()

            else:
                auth = UNSET
                if not isinstance(self.auth, Unset):
                    auth = self.auth.to_dict()

        clevercloud: Union[Dict[str, Any], Unset]
        if isinstance(self.clevercloud, Unset):
            clevercloud = UNSET
        elif isinstance(self.clevercloud, Null):
            clevercloud = UNSET
            if not isinstance(self.clevercloud, Unset):
                clevercloud = self.clevercloud.to_dict()

        else:
            clevercloud
            if isinstance(self.clevercloud, Unset):
                clevercloud = UNSET
            elif isinstance(self.clevercloud, Null):
                clevercloud = UNSET
                if not isinstance(self.clevercloud, Unset):
                    clevercloud = self.clevercloud.to_dict()

            else:
                clevercloud = UNSET
                if not isinstance(self.clevercloud, Unset):
                    clevercloud = self.clevercloud.to_dict()

        alert_emails: Union[Dict[str, Any], Unset]
        if isinstance(self.alert_emails, Unset):
            alert_emails = UNSET
        elif isinstance(self.alert_emails, Null):
            alert_emails = UNSET
            if not isinstance(self.alert_emails, Unset):
                alert_emails = self.alert_emails.to_dict()

        else:
            alert_emails
            if isinstance(self.alert_emails, Unset):
                alert_emails = UNSET
            elif isinstance(self.alert_emails, Null):
                alert_emails = UNSET
                if not isinstance(self.alert_emails, Unset):
                    alert_emails = self.alert_emails.to_dict()

            else:
                alert_emails = UNSET
                if not isinstance(self.alert_emails, Unset):
                    alert_emails = self.alert_emails.to_dict()

        authority: Union[Dict[str, Any], Unset]
        if isinstance(self.authority, Unset):
            authority = UNSET
        elif isinstance(self.authority, Null):
            authority = UNSET
            if not isinstance(self.authority, Unset):
                authority = self.authority.to_dict()

        else:
            authority
            if isinstance(self.authority, Unset):
                authority = UNSET
            elif isinstance(self.authority, Null):
                authority = UNSET
                if not isinstance(self.authority, Unset):
                    authority = self.authority.to_dict()

            else:
                authority = UNSET
                if not isinstance(self.authority, Unset):
                    authority = self.authority.to_dict()

        services: Union[Dict[str, Any], Unset]
        if isinstance(self.services, Unset):
            services = UNSET
        elif isinstance(self.services, Null):
            services = UNSET
            if not isinstance(self.services, Unset):
                services = self.services.to_dict()

        else:
            services
            if isinstance(self.services, Unset):
                services = UNSET
            elif isinstance(self.services, Null):
                services = UNSET
                if not isinstance(self.services, Unset):
                    services = self.services.to_dict()

            else:
                services = UNSET
                if not isinstance(self.services, Unset):
                    services = self.services.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if elastic is not UNSET:
            field_dict["elastic"] = elastic
        if events_webhooks is not UNSET:
            field_dict["eventsWebhooks"] = events_webhooks
        if jwk is not UNSET:
            field_dict["jwk"] = jwk
        if auth is not UNSET:
            field_dict["auth"] = auth
        if clevercloud is not UNSET:
            field_dict["clevercloud"] = clevercloud
        if alert_emails is not UNSET:
            field_dict["alertEmails"] = alert_emails
        if authority is not UNSET:
            field_dict["authority"] = authority
        if services is not UNSET:
            field_dict["services"] = services

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_elastic(data: object) -> Union[Null, Union[Null, PlayapilibswsWSProxyServer], Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _elastic_type_0 = data
                elastic_type_0: Union[Unset, Null]
                if isinstance(_elastic_type_0, Unset):
                    elastic_type_0 = UNSET
                else:
                    elastic_type_0 = Null.from_dict(_elastic_type_0)

                return elastic_type_0
            except:  # noqa: E722
                pass
            if not True:
                raise TypeError()

            def _parse_elastic_type_1(data: object) -> Union[Null, PlayapilibswsWSProxyServer, Unset]:
                if isinstance(data, Unset):
                    return data
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    _elastic_type_1_type_0 = data
                    elastic_type_1_type_0: Union[Unset, Null]
                    if isinstance(_elastic_type_1_type_0, Unset):
                        elastic_type_1_type_0 = UNSET
                    else:
                        elastic_type_1_type_0 = Null.from_dict(_elastic_type_1_type_0)

                    return elastic_type_1_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                _elastic_type_1_type_1 = data
                elastic_type_1_type_1: Union[Unset, PlayapilibswsWSProxyServer]
                if isinstance(_elastic_type_1_type_1, Unset):
                    elastic_type_1_type_1 = UNSET
                else:
                    elastic_type_1_type_1 = PlayapilibswsWSProxyServer.from_dict(_elastic_type_1_type_1)

                return elastic_type_1_type_1

            elastic_type_1 = _parse_elastic_type_1(data)

            return elastic_type_1

        elastic = _parse_elastic(d.pop("elastic", UNSET))

        def _parse_events_webhooks(data: object) -> Union[Null, Union[Null, PlayapilibswsWSProxyServer], Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _events_webhooks_type_0 = data
                events_webhooks_type_0: Union[Unset, Null]
                if isinstance(_events_webhooks_type_0, Unset):
                    events_webhooks_type_0 = UNSET
                else:
                    events_webhooks_type_0 = Null.from_dict(_events_webhooks_type_0)

                return events_webhooks_type_0
            except:  # noqa: E722
                pass
            if not True:
                raise TypeError()

            def _parse_events_webhooks_type_1(data: object) -> Union[Null, PlayapilibswsWSProxyServer, Unset]:
                if isinstance(data, Unset):
                    return data
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    _events_webhooks_type_1_type_0 = data
                    events_webhooks_type_1_type_0: Union[Unset, Null]
                    if isinstance(_events_webhooks_type_1_type_0, Unset):
                        events_webhooks_type_1_type_0 = UNSET
                    else:
                        events_webhooks_type_1_type_0 = Null.from_dict(_events_webhooks_type_1_type_0)

                    return events_webhooks_type_1_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                _events_webhooks_type_1_type_1 = data
                events_webhooks_type_1_type_1: Union[Unset, PlayapilibswsWSProxyServer]
                if isinstance(_events_webhooks_type_1_type_1, Unset):
                    events_webhooks_type_1_type_1 = UNSET
                else:
                    events_webhooks_type_1_type_1 = PlayapilibswsWSProxyServer.from_dict(_events_webhooks_type_1_type_1)

                return events_webhooks_type_1_type_1

            events_webhooks_type_1 = _parse_events_webhooks_type_1(data)

            return events_webhooks_type_1

        events_webhooks = _parse_events_webhooks(d.pop("eventsWebhooks", UNSET))

        def _parse_jwk(data: object) -> Union[Null, Union[Null, PlayapilibswsWSProxyServer], Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _jwk_type_0 = data
                jwk_type_0: Union[Unset, Null]
                if isinstance(_jwk_type_0, Unset):
                    jwk_type_0 = UNSET
                else:
                    jwk_type_0 = Null.from_dict(_jwk_type_0)

                return jwk_type_0
            except:  # noqa: E722
                pass
            if not True:
                raise TypeError()

            def _parse_jwk_type_1(data: object) -> Union[Null, PlayapilibswsWSProxyServer, Unset]:
                if isinstance(data, Unset):
                    return data
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    _jwk_type_1_type_0 = data
                    jwk_type_1_type_0: Union[Unset, Null]
                    if isinstance(_jwk_type_1_type_0, Unset):
                        jwk_type_1_type_0 = UNSET
                    else:
                        jwk_type_1_type_0 = Null.from_dict(_jwk_type_1_type_0)

                    return jwk_type_1_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                _jwk_type_1_type_1 = data
                jwk_type_1_type_1: Union[Unset, PlayapilibswsWSProxyServer]
                if isinstance(_jwk_type_1_type_1, Unset):
                    jwk_type_1_type_1 = UNSET
                else:
                    jwk_type_1_type_1 = PlayapilibswsWSProxyServer.from_dict(_jwk_type_1_type_1)

                return jwk_type_1_type_1

            jwk_type_1 = _parse_jwk_type_1(data)

            return jwk_type_1

        jwk = _parse_jwk(d.pop("jwk", UNSET))

        def _parse_auth(data: object) -> Union[Null, Union[Null, PlayapilibswsWSProxyServer], Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _auth_type_0 = data
                auth_type_0: Union[Unset, Null]
                if isinstance(_auth_type_0, Unset):
                    auth_type_0 = UNSET
                else:
                    auth_type_0 = Null.from_dict(_auth_type_0)

                return auth_type_0
            except:  # noqa: E722
                pass
            if not True:
                raise TypeError()

            def _parse_auth_type_1(data: object) -> Union[Null, PlayapilibswsWSProxyServer, Unset]:
                if isinstance(data, Unset):
                    return data
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    _auth_type_1_type_0 = data
                    auth_type_1_type_0: Union[Unset, Null]
                    if isinstance(_auth_type_1_type_0, Unset):
                        auth_type_1_type_0 = UNSET
                    else:
                        auth_type_1_type_0 = Null.from_dict(_auth_type_1_type_0)

                    return auth_type_1_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                _auth_type_1_type_1 = data
                auth_type_1_type_1: Union[Unset, PlayapilibswsWSProxyServer]
                if isinstance(_auth_type_1_type_1, Unset):
                    auth_type_1_type_1 = UNSET
                else:
                    auth_type_1_type_1 = PlayapilibswsWSProxyServer.from_dict(_auth_type_1_type_1)

                return auth_type_1_type_1

            auth_type_1 = _parse_auth_type_1(data)

            return auth_type_1

        auth = _parse_auth(d.pop("auth", UNSET))

        def _parse_clevercloud(data: object) -> Union[Null, Union[Null, PlayapilibswsWSProxyServer], Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _clevercloud_type_0 = data
                clevercloud_type_0: Union[Unset, Null]
                if isinstance(_clevercloud_type_0, Unset):
                    clevercloud_type_0 = UNSET
                else:
                    clevercloud_type_0 = Null.from_dict(_clevercloud_type_0)

                return clevercloud_type_0
            except:  # noqa: E722
                pass
            if not True:
                raise TypeError()

            def _parse_clevercloud_type_1(data: object) -> Union[Null, PlayapilibswsWSProxyServer, Unset]:
                if isinstance(data, Unset):
                    return data
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    _clevercloud_type_1_type_0 = data
                    clevercloud_type_1_type_0: Union[Unset, Null]
                    if isinstance(_clevercloud_type_1_type_0, Unset):
                        clevercloud_type_1_type_0 = UNSET
                    else:
                        clevercloud_type_1_type_0 = Null.from_dict(_clevercloud_type_1_type_0)

                    return clevercloud_type_1_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                _clevercloud_type_1_type_1 = data
                clevercloud_type_1_type_1: Union[Unset, PlayapilibswsWSProxyServer]
                if isinstance(_clevercloud_type_1_type_1, Unset):
                    clevercloud_type_1_type_1 = UNSET
                else:
                    clevercloud_type_1_type_1 = PlayapilibswsWSProxyServer.from_dict(_clevercloud_type_1_type_1)

                return clevercloud_type_1_type_1

            clevercloud_type_1 = _parse_clevercloud_type_1(data)

            return clevercloud_type_1

        clevercloud = _parse_clevercloud(d.pop("clevercloud", UNSET))

        def _parse_alert_emails(data: object) -> Union[Null, Union[Null, PlayapilibswsWSProxyServer], Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _alert_emails_type_0 = data
                alert_emails_type_0: Union[Unset, Null]
                if isinstance(_alert_emails_type_0, Unset):
                    alert_emails_type_0 = UNSET
                else:
                    alert_emails_type_0 = Null.from_dict(_alert_emails_type_0)

                return alert_emails_type_0
            except:  # noqa: E722
                pass
            if not True:
                raise TypeError()

            def _parse_alert_emails_type_1(data: object) -> Union[Null, PlayapilibswsWSProxyServer, Unset]:
                if isinstance(data, Unset):
                    return data
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    _alert_emails_type_1_type_0 = data
                    alert_emails_type_1_type_0: Union[Unset, Null]
                    if isinstance(_alert_emails_type_1_type_0, Unset):
                        alert_emails_type_1_type_0 = UNSET
                    else:
                        alert_emails_type_1_type_0 = Null.from_dict(_alert_emails_type_1_type_0)

                    return alert_emails_type_1_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                _alert_emails_type_1_type_1 = data
                alert_emails_type_1_type_1: Union[Unset, PlayapilibswsWSProxyServer]
                if isinstance(_alert_emails_type_1_type_1, Unset):
                    alert_emails_type_1_type_1 = UNSET
                else:
                    alert_emails_type_1_type_1 = PlayapilibswsWSProxyServer.from_dict(_alert_emails_type_1_type_1)

                return alert_emails_type_1_type_1

            alert_emails_type_1 = _parse_alert_emails_type_1(data)

            return alert_emails_type_1

        alert_emails = _parse_alert_emails(d.pop("alertEmails", UNSET))

        def _parse_authority(data: object) -> Union[Null, Union[Null, PlayapilibswsWSProxyServer], Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _authority_type_0 = data
                authority_type_0: Union[Unset, Null]
                if isinstance(_authority_type_0, Unset):
                    authority_type_0 = UNSET
                else:
                    authority_type_0 = Null.from_dict(_authority_type_0)

                return authority_type_0
            except:  # noqa: E722
                pass
            if not True:
                raise TypeError()

            def _parse_authority_type_1(data: object) -> Union[Null, PlayapilibswsWSProxyServer, Unset]:
                if isinstance(data, Unset):
                    return data
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    _authority_type_1_type_0 = data
                    authority_type_1_type_0: Union[Unset, Null]
                    if isinstance(_authority_type_1_type_0, Unset):
                        authority_type_1_type_0 = UNSET
                    else:
                        authority_type_1_type_0 = Null.from_dict(_authority_type_1_type_0)

                    return authority_type_1_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                _authority_type_1_type_1 = data
                authority_type_1_type_1: Union[Unset, PlayapilibswsWSProxyServer]
                if isinstance(_authority_type_1_type_1, Unset):
                    authority_type_1_type_1 = UNSET
                else:
                    authority_type_1_type_1 = PlayapilibswsWSProxyServer.from_dict(_authority_type_1_type_1)

                return authority_type_1_type_1

            authority_type_1 = _parse_authority_type_1(data)

            return authority_type_1

        authority = _parse_authority(d.pop("authority", UNSET))

        def _parse_services(data: object) -> Union[Null, Union[Null, PlayapilibswsWSProxyServer], Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _services_type_0 = data
                services_type_0: Union[Unset, Null]
                if isinstance(_services_type_0, Unset):
                    services_type_0 = UNSET
                else:
                    services_type_0 = Null.from_dict(_services_type_0)

                return services_type_0
            except:  # noqa: E722
                pass
            if not True:
                raise TypeError()

            def _parse_services_type_1(data: object) -> Union[Null, PlayapilibswsWSProxyServer, Unset]:
                if isinstance(data, Unset):
                    return data
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    _services_type_1_type_0 = data
                    services_type_1_type_0: Union[Unset, Null]
                    if isinstance(_services_type_1_type_0, Unset):
                        services_type_1_type_0 = UNSET
                    else:
                        services_type_1_type_0 = Null.from_dict(_services_type_1_type_0)

                    return services_type_1_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                _services_type_1_type_1 = data
                services_type_1_type_1: Union[Unset, PlayapilibswsWSProxyServer]
                if isinstance(_services_type_1_type_1, Unset):
                    services_type_1_type_1 = UNSET
                else:
                    services_type_1_type_1 = PlayapilibswsWSProxyServer.from_dict(_services_type_1_type_1)

                return services_type_1_type_1

            services_type_1 = _parse_services_type_1(data)

            return services_type_1

        services = _parse_services(d.pop("services", UNSET))

        otoroshimodels_proxies = cls(
            elastic=elastic,
            events_webhooks=events_webhooks,
            jwk=jwk,
            auth=auth,
            clevercloud=clevercloud,
            alert_emails=alert_emails,
            authority=authority,
            services=services,
        )

        otoroshimodels_proxies.additional_properties = d
        return otoroshimodels_proxies

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
