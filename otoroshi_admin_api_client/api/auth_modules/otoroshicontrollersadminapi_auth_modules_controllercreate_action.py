from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.error_response import ErrorResponse
from ...models.otoroshiauth_basic_auth_module_config import OtoroshiauthBasicAuthModuleConfig
from ...models.otoroshiauth_generic_oauth_2_module_config import OtoroshiauthGenericOauth2ModuleConfig
from ...models.otoroshiauth_ldap_auth_module_config import OtoroshiauthLdapAuthModuleConfig
from ...models.otoroshiauth_oauth_1_module_config import OtoroshiauthOauth1ModuleConfig
from ...models.otoroshiauth_saml_auth_module_config import OtoroshiauthSamlAuthModuleConfig
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: Union[
        OtoroshiauthBasicAuthModuleConfig,
        OtoroshiauthGenericOauth2ModuleConfig,
        OtoroshiauthLdapAuthModuleConfig,
        OtoroshiauthOauth1ModuleConfig,
        OtoroshiauthSamlAuthModuleConfig,
    ],
) -> Dict[str, Any]:
    url = "{}/api/auths".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if isinstance(json_body, OtoroshiauthBasicAuthModuleConfig):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, OtoroshiauthGenericOauth2ModuleConfig):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, OtoroshiauthLdapAuthModuleConfig):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, OtoroshiauthOauth1ModuleConfig):
        json_json_body = json_body.to_dict()

    else:
        json_json_body = json_body.to_dict()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[
    Union[
        ErrorResponse,
        Union[
            OtoroshiauthBasicAuthModuleConfig,
            OtoroshiauthGenericOauth2ModuleConfig,
            OtoroshiauthLdapAuthModuleConfig,
            OtoroshiauthOauth1ModuleConfig,
            OtoroshiauthSamlAuthModuleConfig,
        ],
    ]
]:
    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401
    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404
    if response.status_code == 201:

        def _parse_response_201(
            data: object,
        ) -> Union[
            OtoroshiauthBasicAuthModuleConfig,
            OtoroshiauthGenericOauth2ModuleConfig,
            OtoroshiauthLdapAuthModuleConfig,
            OtoroshiauthOauth1ModuleConfig,
            OtoroshiauthSamlAuthModuleConfig,
        ]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasotoroshiauth_auth_module_config_type_0 = OtoroshiauthBasicAuthModuleConfig.from_dict(
                    data
                )

                return componentsschemasotoroshiauth_auth_module_config_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasotoroshiauth_auth_module_config_type_1 = (
                    OtoroshiauthGenericOauth2ModuleConfig.from_dict(data)
                )

                return componentsschemasotoroshiauth_auth_module_config_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasotoroshiauth_auth_module_config_type_2 = OtoroshiauthLdapAuthModuleConfig.from_dict(
                    data
                )

                return componentsschemasotoroshiauth_auth_module_config_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasotoroshiauth_auth_module_config_type_3 = OtoroshiauthOauth1ModuleConfig.from_dict(data)

                return componentsschemasotoroshiauth_auth_module_config_type_3
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemasotoroshiauth_auth_module_config_type_4 = OtoroshiauthSamlAuthModuleConfig.from_dict(data)

            return componentsschemasotoroshiauth_auth_module_config_type_4

        response_201 = _parse_response_201(response.json())

        return response_201
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[
    Union[
        ErrorResponse,
        Union[
            OtoroshiauthBasicAuthModuleConfig,
            OtoroshiauthGenericOauth2ModuleConfig,
            OtoroshiauthLdapAuthModuleConfig,
            OtoroshiauthOauth1ModuleConfig,
            OtoroshiauthSamlAuthModuleConfig,
        ],
    ]
]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: Union[
        OtoroshiauthBasicAuthModuleConfig,
        OtoroshiauthGenericOauth2ModuleConfig,
        OtoroshiauthLdapAuthModuleConfig,
        OtoroshiauthOauth1ModuleConfig,
        OtoroshiauthSamlAuthModuleConfig,
    ],
) -> Response[
    Union[
        ErrorResponse,
        Union[
            OtoroshiauthBasicAuthModuleConfig,
            OtoroshiauthGenericOauth2ModuleConfig,
            OtoroshiauthLdapAuthModuleConfig,
            OtoroshiauthOauth1ModuleConfig,
            OtoroshiauthSamlAuthModuleConfig,
        ],
    ]
]:
    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    json_body: Union[
        OtoroshiauthBasicAuthModuleConfig,
        OtoroshiauthGenericOauth2ModuleConfig,
        OtoroshiauthLdapAuthModuleConfig,
        OtoroshiauthOauth1ModuleConfig,
        OtoroshiauthSamlAuthModuleConfig,
    ],
) -> Optional[
    Union[
        ErrorResponse,
        Union[
            OtoroshiauthBasicAuthModuleConfig,
            OtoroshiauthGenericOauth2ModuleConfig,
            OtoroshiauthLdapAuthModuleConfig,
            OtoroshiauthOauth1ModuleConfig,
            OtoroshiauthSamlAuthModuleConfig,
        ],
    ]
]:
    """ """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: Union[
        OtoroshiauthBasicAuthModuleConfig,
        OtoroshiauthGenericOauth2ModuleConfig,
        OtoroshiauthLdapAuthModuleConfig,
        OtoroshiauthOauth1ModuleConfig,
        OtoroshiauthSamlAuthModuleConfig,
    ],
) -> Response[
    Union[
        ErrorResponse,
        Union[
            OtoroshiauthBasicAuthModuleConfig,
            OtoroshiauthGenericOauth2ModuleConfig,
            OtoroshiauthLdapAuthModuleConfig,
            OtoroshiauthOauth1ModuleConfig,
            OtoroshiauthSamlAuthModuleConfig,
        ],
    ]
]:
    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    json_body: Union[
        OtoroshiauthBasicAuthModuleConfig,
        OtoroshiauthGenericOauth2ModuleConfig,
        OtoroshiauthLdapAuthModuleConfig,
        OtoroshiauthOauth1ModuleConfig,
        OtoroshiauthSamlAuthModuleConfig,
    ],
) -> Optional[
    Union[
        ErrorResponse,
        Union[
            OtoroshiauthBasicAuthModuleConfig,
            OtoroshiauthGenericOauth2ModuleConfig,
            OtoroshiauthLdapAuthModuleConfig,
            OtoroshiauthOauth1ModuleConfig,
            OtoroshiauthSamlAuthModuleConfig,
        ],
    ]
]:
    """ """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
