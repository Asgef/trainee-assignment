import pytest
import aiohttp
import asyncio
from unittest.mock import AsyncMock
from trainee_assignment.spiral_matrix import fetch_data
from aiohttp import (
    ClientResponseError, ClientConnectorError, RequestInfo, ClientOSError,
)
from aiohttp.typedefs import CIMultiDict
from aiohttp.typedefs import URL


@pytest.mark.asyncio
async def test_fetch_matrix_data_success(monkeypatch):
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
    mock_response = AsyncMock()
    mock_response.text.return_value = expected
    async def mock_get(url):
        return mock_response

    monkeypatch.setattr(aiohttp.ClientSession, 'get', mock_get)
    async with aiohttp.ClientSession() as session:
        result = await fetch_data('https://example.com', session)
        assert result == expected


@pytest.mark.asyncio
async def test_fetch_dataserver_error(monkeypatch):
    mock_response = AsyncMock()
    url = URL('https://example.com')
    headers = CIMultiDict({'Host': 'example.com'})
    request_info = RequestInfo(
        url=url,
        method='GET',
        headers=headers
    )
    mock_response.text.side_effect = ClientResponseError(
        request_info=request_info, history=(), status=500
    )

    async def mock_get(url):
        return mock_response

    monkeypatch.setattr(aiohttp.ClientSession, 'get', mock_get)
    async with aiohttp.ClientSession() as session:
        result = await fetch_data('https://example.com', session)
        assert result == ''


@pytest.mark.asyncio
async def test_fetch_data_timeout(monkeypatch):
    # таймаут соединения
    async def mock_get(url):
        raise asyncio.TimeoutError

    monkeypatch.setattr(aiohttp.ClientSession, 'get', mock_get)

    async with aiohttp.ClientSession() as session:
        with pytest.raises(asyncio.TimeoutError):
            await fetch_data('https://example.com', session)


@pytest.mark.asyncio
async def test_fetch_data_connection_refused(monkeypatch):
    # ошибка соединения
    async def mock_get(url):
        os_error = OSError(111, 'Connection refused')
        raise ClientOSError(os_error.errno, os_error.strerror)

    monkeypatch.setattr(aiohttp.ClientSession, 'get', mock_get)

    async with aiohttp.ClientSession() as session:
        with pytest.raises(ClientConnectorError):
            await fetch_data('https://example.com', session)
