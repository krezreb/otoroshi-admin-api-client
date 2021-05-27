from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.error_response import ErrorResponse
from ...models.otoroshimodels_error_template import OtoroshimodelsErrorTemplate
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    service_id: str,
    json_body: OtoroshimodelsErrorTemplate,
) -> Dict[str, Any]:
    url = "{}/api/services/{serviceId}/template".format(client.base_url, serviceId=service_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[ErrorResponse, OtoroshimodelsErrorTemplate]]:
    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401
    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404
    if response.status_code == 200:
        response_200 = OtoroshimodelsErrorTemplate.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[ErrorResponse, OtoroshimodelsErrorTemplate]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    service_id: str,
    json_body: OtoroshimodelsErrorTemplate,
) -> Response[Union[ErrorResponse, OtoroshimodelsErrorTemplate]]:
    kwargs = _get_kwargs(
        client=client,
        service_id=service_id,
        json_body=json_body,
    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    service_id: str,
    json_body: OtoroshimodelsErrorTemplate,
) -> Optional[Union[ErrorResponse, OtoroshimodelsErrorTemplate]]:
    """ """

    return sync_detailed(
        client=client,
        service_id=service_id,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    service_id: str,
    json_body: OtoroshimodelsErrorTemplate,
) -> Response[Union[ErrorResponse, OtoroshimodelsErrorTemplate]]:
    kwargs = _get_kwargs(
        client=client,
        service_id=service_id,
        json_body=json_body,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    service_id: str,
    json_body: OtoroshimodelsErrorTemplate,
) -> Optional[Union[ErrorResponse, OtoroshimodelsErrorTemplate]]:
    """ """

    return (
        await asyncio_detailed(
            client=client,
            service_id=service_id,
            json_body=json_body,
        )
    ).parsed
