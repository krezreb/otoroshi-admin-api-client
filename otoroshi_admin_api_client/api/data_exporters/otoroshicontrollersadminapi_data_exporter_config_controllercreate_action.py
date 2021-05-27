from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.error_response import ErrorResponse
from ...models.otoroshimodels_data_exporter_config import OtoroshimodelsDataExporterConfig
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: OtoroshimodelsDataExporterConfig,
) -> Dict[str, Any]:
    url = "{}/api/data-exporter-configs".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[ErrorResponse, OtoroshimodelsDataExporterConfig]]:
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
        response_201 = OtoroshimodelsDataExporterConfig.from_dict(response.json())

        return response_201
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[ErrorResponse, OtoroshimodelsDataExporterConfig]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: OtoroshimodelsDataExporterConfig,
) -> Response[Union[ErrorResponse, OtoroshimodelsDataExporterConfig]]:
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
    json_body: OtoroshimodelsDataExporterConfig,
) -> Optional[Union[ErrorResponse, OtoroshimodelsDataExporterConfig]]:
    """ """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: OtoroshimodelsDataExporterConfig,
) -> Response[Union[ErrorResponse, OtoroshimodelsDataExporterConfig]]:
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
    json_body: OtoroshimodelsDataExporterConfig,
) -> Optional[Union[ErrorResponse, OtoroshimodelsDataExporterConfig]]:
    """ """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
