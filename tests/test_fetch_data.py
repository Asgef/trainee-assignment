import pytest
import aiohttp
import asyncio
import os
from trainee_assignment.spiral_matrix import fetch_data
from aiohttp import (
    ClientConnectorError, ClientOSError, ClientSession
)
from aioresponses import aioresponses


def read_fixture_file(filename: str) -> str:
    test_dir = os.path.dirname(__file__)
    file_path = os.path.join(test_dir, 'fixtures', filename)
    with open(file_path, 'r') as f:
        expected = f.read()
    return expected


@pytest.mark.asyncio
async def test_fetch_data_success():
    expected = read_fixture_file('required_matrix.txt')
    text_data = expected

    with aioresponses() as mocked:
        mocked.get('https://example.com', status=200, body=text_data)
        async with ClientSession() as session:
            result = await fetch_data('https://example.com', session)
            assert result == expected


@pytest.mark.asyncio
async def test_fetch_data_unsuccessful():
    expected = ''
    text_data = '204 No Content'

    with aioresponses() as mocked:
        mocked.get('https://example.com', status=204, body=text_data)
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
