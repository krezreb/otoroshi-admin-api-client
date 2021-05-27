from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.bulk_response_body_item import BulkResponseBodyItem
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: str,
) -> Dict[str, Any]:
    url = "{}/api/tcp/services/_bulk".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[ErrorResponse, List[BulkResponseBodyItem]]]:
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
        for componentsschemas_bulk_response_body_item_data in _response_200:
            componentsschemas_bulk_response_body_item = BulkResponseBodyItem.from_dict(
                componentsschemas_bulk_response_body_item_data
            )

            response_200.append(componentsschemas_bulk_response_body_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[ErrorResponse, List[BulkResponseBodyItem]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: str,
) -> Response[Union[ErrorResponse, List[BulkResponseBodyItem]]]:
    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.put(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    json_body: str,
) -> Optional[Union[ErrorResponse, List[BulkResponseBodyItem]]]:
    """ """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: str,
) -> Response[Union[ErrorResponse, List[BulkResponseBodyItem]]]:
    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.put(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    json_body: str,
) -> Optional[Union[ErrorResponse, List[BulkResponseBodyItem]]]:
    """ """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
