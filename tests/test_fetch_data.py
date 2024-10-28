import os
import pytest
import asyncio
from aiohttp import web
from aioresponses import aioresponses
from trainee_assignment.spiral_matrix import fetch_data
from aiohttp import (
    ClientConnectorError, ClientOSError, ClientSession
)


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
async def test_fetch_dataserver_error_404():
    with aioresponses() as mocked:
        mocked.get('https://example.com', status=404)
        async with ClientSession() as session:
            with pytest.raises(web.HTTPNotFound):
                await fetch_data('https://example.com', session)


@pytest.mark.asyncio
async def test_fetch_dataserver_error_500():
    with aioresponses() as mocked:
        mocked.get('https://example.com', status=500)
        async with ClientSession() as session:
            with pytest.raises(web.HTTPBadGateway):
                await fetch_data('https://example.com', session)


@pytest.mark.asyncio
async def test_fetch_data_error_timeout():
    with aioresponses() as mocked:
        mocked.get('https://example.com', exception=asyncio.TimeoutError())
        async with ClientSession() as session:
            with pytest.raises(asyncio.TimeoutError):
                await fetch_data('https://example.com', session)


@pytest.mark.asyncio
async def test_fetch_data_error_connection():
    with aioresponses() as mocked:
        mocked.get(
            'https://example.com', exception=ClientOSError(
                111, 'Connection refused'
            )
        )
        async with ClientSession() as session:
            with pytest.raises(ClientConnectorError):
                await fetch_data('https://example.com', session)
