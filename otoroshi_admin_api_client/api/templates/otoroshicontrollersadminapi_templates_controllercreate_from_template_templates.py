from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.empty import Empty
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    entity: str,
    json_body: Empty,
) -> Dict[str, Any]:
    url = "{}/api/{entity}/_template".format(client.base_url, entity=entity)

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


def _parse_response(*, response: httpx.Response) -> Optional[ErrorResponse]:
    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401
    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[ErrorResponse]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    entity: str,
    json_body: Empty,
) -> Response[ErrorResponse]:
    kwargs = _get_kwargs(
        client=client,
        entity=entity,
        json_body=json_body,
    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    entity: str,
    json_body: Empty,
) -> Optional[ErrorResponse]:
    """ """

    return sync_detailed(
        client=client,
        entity=entity,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    entity: str,
    json_body: Empty,
) -> Response[ErrorResponse]:
    kwargs = _get_kwargs(
        client=client,
        entity=entity,
        json_body=json_body,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    entity: str,
    json_body: Empty,
) -> Optional[ErrorResponse]:
    """ """

    return (
        await asyncio_detailed(
            client=client,
            entity=entity,
            json_body=json_body,
        )
    ).parsed
