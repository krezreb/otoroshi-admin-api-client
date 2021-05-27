from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.error_response import ErrorResponse
from ...models.otoroshievents_health_check_event import OtoroshieventsHealthCheckEvent
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    service_id: str,
) -> Dict[str, Any]:
    url = "{}/api/services/{serviceId}/health".format(client.base_url, serviceId=service_id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[ErrorResponse, List[OtoroshieventsHealthCheckEvent]]]:
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
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_health_check_event_list_item_data in _response_200:
            componentsschemas_health_check_event_list_item = OtoroshieventsHealthCheckEvent.from_dict(
                componentsschemas_health_check_event_list_item_data
            )

            response_200.append(componentsschemas_health_check_event_list_item)

        return response_200
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[ErrorResponse, List[OtoroshieventsHealthCheckEvent]]]:
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
) -> Response[Union[ErrorResponse, List[OtoroshieventsHealthCheckEvent]]]:
    kwargs = _get_kwargs(
        client=client,
        service_id=service_id,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    service_id: str,
) -> Optional[Union[ErrorResponse, List[OtoroshieventsHealthCheckEvent]]]:
    """ """

    return sync_detailed(
        client=client,
        service_id=service_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    service_id: str,
) -> Response[Union[ErrorResponse, List[OtoroshieventsHealthCheckEvent]]]:
    kwargs = _get_kwargs(
        client=client,
        service_id=service_id,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    service_id: str,
) -> Optional[Union[ErrorResponse, List[OtoroshieventsHealthCheckEvent]]]:
    """ """

    return (
        await asyncio_detailed(
            client=client,
            service_id=service_id,
        )
    ).parsed
