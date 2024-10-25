import pytest
import aiohttp
import asyncio
from trainee_assignment.spiral_matrix import fetch_data
from aiohttp import (
    ClientConnectorError, ClientOSError, ClientSession
)
from aioresponses import aioresponses


@pytest.mark.asyncio
async def test_fetch_data_success():
    expected = (
        '+-----+-----+-----+-----+\n'
        '|  10 |  20 |  30 |  40 |\n'
        '+-----+-----+-----+-----+\n'
        '|  50 |  60 |  70 |  80 |\n'
        '+-----+-----+-----+-----+\n'
        '|  90 | 100 | 110 | 120 |\n'
        '+-----+-----+-----+-----+\n'
        '| 130 | 140 | 150 | 160 |\n'
        '+-----+-----+-----+-----+'
    )

    with aioresponses() as mocked:
        mocked.get('https://example.com', status=200, body=expected)
        async with ClientSession() as session:
            result = await fetch_data('https://example.com', session)
            assert result == expected


@pytest.mark.asyncio
async def test_fetch_dataserver_error():
    with aioresponses() as mocked:
        mocked.get('https://example.com', status=500)
        async with ClientSession() as session:
            with pytest.raises(aiohttp.ClientResponseError):
                await fetch_data('https://example.com', session)


@pytest.mark.asyncio
async def test_fetch_data_timeout():
    with aioresponses() as mocked:
        mocked.get('https://example.com', exception=asyncio.TimeoutError())
        async with ClientSession() as session:
            with pytest.raises(asyncio.TimeoutError):
                await fetch_data('https://example.com', session)


@pytest.mark.asyncio
async def test_fetch_data_connection_refused():
    with aioresponses() as mocked:
        mocked.get(
            'https://example.com', exception=ClientOSError(
                111, 'Connection refused'
            )
        )
        async with ClientSession() as session:
            with pytest.raises(ClientConnectorError):
                await fetch_data('https://example.com', session)
