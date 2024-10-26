import asyncio
import aiohttp
from typing import List
from .parser import convert_str_to_matrix


async def fetch_data(url, session) -> str:
    try:
        async with session.get(url, allow_redirects=True) as response:
            response.raise_for_status()

            if response.status != 200:
                return ''

            data = await response.text()
            return data

    except aiohttp.ClientResponseError as e:
        if 400 <= e.status < 600:
            raise aiohttp.ClientResponseError(
                status=e.status, message=e.message,
                request_info=e.request_info,
                history=e.history
            )
    except aiohttp.ClientOSError as e:
        raise aiohttp.ClientConnectorError(os_error=e, connection_key=url)
    except asyncio.TimeoutError:
        raise



def matrix_to_spiral(data: list[int]) -> list[int]:
    pass


async def get_matrix(url: str) -> List[int]:
    async with aiohttp.ClientSession() as session:
        data_str = await fetch_data(url, session)
    data = convert_str_to_matrix(data_str)

    return matrix_to_spiral(data)
