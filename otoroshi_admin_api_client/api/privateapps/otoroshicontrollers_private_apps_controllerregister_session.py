from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.empty import Empty
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    id: str,
    username: str,
    json_body: Empty,
) -> Dict[str, Any]:
    url = "{}/api/privateapps/sessions/{id}/{username}".format(client.base_url, id=id, username=username)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Empty, ErrorResponse]]:
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
        response_200 = Empty.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Empty, ErrorResponse]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    id: str,
    username: str,
    json_body: Empty,
) -> Response[Union[Empty, ErrorResponse]]:
    kwargs = _get_kwargs(
        client=client,
        id=id,
        username=username,
        json_body=json_body,
    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    id: str,
    username: str,
    json_body: Empty,
) -> Optional[Union[Empty, ErrorResponse]]:
    """ """

    return sync_detailed(
        client=client,
        id=id,
        username=username,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    id: str,
    username: str,
    json_body: Empty,
) -> Response[Union[Empty, ErrorResponse]]:
    kwargs = _get_kwargs(
        client=client,
        id=id,
        username=username,
        json_body=json_body,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    id: str,
    username: str,
    json_body: Empty,
) -> Optional[Union[Empty, ErrorResponse]]:
    """ """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
            username=username,
            json_body=json_body,
        )
    ).parsed
