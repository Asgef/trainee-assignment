import asyncio
import aiohttp
from typing import List


async def fetch_matrix_data(url, session):
    pass

def convert_str_to_matrix(data: str) -> list[int]:
    pass


def matrix_to_spiral(data: list[int]) -> list[int]:
    pass


async def get_matrix(url: str) -> List[int]:
    async with aiohttp.ClientSession() as session:
        data_str = await fetch_matrix_data(url, session)
    data = convert_str_to_matrix(data_str)

    return matrix_to_spiral(data)

