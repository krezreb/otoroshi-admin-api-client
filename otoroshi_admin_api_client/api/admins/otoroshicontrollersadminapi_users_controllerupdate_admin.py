from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.error_response import ErrorResponse
from ...models.otoroshimodels_simple_otoroshi_admin import OtoroshimodelsSimpleOtoroshiAdmin
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    username: str,
    json_body: OtoroshimodelsSimpleOtoroshiAdmin,
) -> Dict[str, Any]:
    url = "{}/api/admins/simple/{username}".format(client.base_url, username=username)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[ErrorResponse, OtoroshimodelsSimpleOtoroshiAdmin]]:
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
        response_200 = OtoroshimodelsSimpleOtoroshiAdmin.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[ErrorResponse, OtoroshimodelsSimpleOtoroshiAdmin]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    username: str,
    json_body: OtoroshimodelsSimpleOtoroshiAdmin,
) -> Response[Union[ErrorResponse, OtoroshimodelsSimpleOtoroshiAdmin]]:
    kwargs = _get_kwargs(
        client=client,
        username=username,
        json_body=json_body,
    )

    response = httpx.put(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    username: str,
    json_body: OtoroshimodelsSimpleOtoroshiAdmin,
) -> Optional[Union[ErrorResponse, OtoroshimodelsSimpleOtoroshiAdmin]]:
    """ """

    return sync_detailed(
        client=client,
        username=username,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    username: str,
    json_body: OtoroshimodelsSimpleOtoroshiAdmin,
) -> Response[Union[ErrorResponse, OtoroshimodelsSimpleOtoroshiAdmin]]:
    kwargs = _get_kwargs(
        client=client,
        username=username,
        json_body=json_body,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.put(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    username: str,
    json_body: OtoroshimodelsSimpleOtoroshiAdmin,
) -> Optional[Union[ErrorResponse, OtoroshimodelsSimpleOtoroshiAdmin]]:
    """ """

    return (
        await asyncio_detailed(
            client=client,
            username=username,
            json_body=json_body,
        )
    ).parsed
