import asyncio
import aiohttp
from typing import List
from aiohttp import web
from .matrix_parsing import prepare_matrix
from .matrix_operation import matrix_to_spiral


async def fetch_data(url, session) -> str:  # noqa C901
    """
    Fetches data from a given URL using an aiohttp session.

    Args:
        url (str): URL to fetch data from
        session (aiohttp.ClientSession): aiohttp session to use

    Returns:
        str: Fetched data

    Raises:
        web.HTTPNotFound: If response status is 400-499
        web.HTTPBadGateway: If response status is 500-599
        aiohttp.ClientConnectorError: If a connection error occurs
        asyncio.TimeoutError: If the request times out
    """
    try:
        async with session.get(url, allow_redirects=True) as response:
            if 400 <= response.status < 500:
                raise web.HTTPNotFound()
            elif 500 <= response.status < 599:
                raise web.HTTPBadGateway()
            return await response.text()

    except aiohttp.ClientOSError as e:
        raise aiohttp.ClientConnectorError(os_error=e, connection_key=url)
    except asyncio.TimeoutError:
        raise asyncio.TimeoutError()


async def get_matrix(url: str) -> List[int]:
    """
    Fetches data from a URL, converts it into a matrix and
    extracts a spiral pattern.

    Args:
        url (str): URL to fetch data from

    Returns:
        List[int]: Spiral pattern from the matrix

    Raises:
        aiohttp.ClientConnectorError: If a connection error occurs
        asyncio.TimeoutError: If the request times out
    """
    async with aiohttp.ClientSession() as session:
        data_str: str = await fetch_data(url, session)

    data: list[list[int]] = prepare_matrix(data_str)

    return matrix_to_spiral(data)
