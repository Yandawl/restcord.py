# -*- coding: utf-8 -*-
import asyncio
import datetime
import json
import logging
import sys
from typing import Optional

import aiohttp
from aiohttp import ClientSession

from . import __version__
from .errors import (
    BadGateway,
    BadRequest,
    Forbidden,
    HTTPException,
    InternalServerError,
    NotFound,
    RateLimited
)

__log__ = logging.getLogger(__name__)

__all__ = (
    'Route',
    'HTTPClient'
)


class Route:

    BASE = 'https://discord.com/api'

    def __init__(self, method, path):
        self.path = path
        self.method = method
        self.url = (self.BASE + self.path)


class HTTPClient:

    __slots__ = ('token', 'loop', 'proxy', 'proxy_auth', '__session', '__agent')

    def __init__(self, token: str, loop=None, proxy=None, proxy_auth=None, session: Optional[ClientSession] = None) -> None:
        self.token = token
        self.loop = asyncio.get_event_loop() if loop is None else loop
        self.proxy = proxy
        self.proxy_auth = proxy_auth
        self.__session = session
        self.__agent = f'RestCord.py (https://github.com/Yandawl/restcord.py {__version__}) Python/{sys.version_info[0]}.{sys.version_info[1]} aiohttp/{aiohttp.__version__}'

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.close()

    @property
    def session(self) -> ClientSession:
        """:class:`ClientSession`: The aiohttp ClientSession."""
        if self.__session is None or self.__session.closed:
            self.__session = ClientSession()
        return self.__session

    async def close(self):
        if self.__session:
            await self.__session.close()

    async def _request(self, route: Route, **kwargs):
        method = route.method
        url = route.url

        kwargs['headers'] = {
            'User-Agent': self.__agent,
            'X-Ratelimit-Precision': 'millisecond',
            'Authorization': f'Bot {self.token}'
        }

        if 'json' in kwargs:
            kwargs['headers']['Content-Type'] = 'application/json'
            kwargs['data'] = self.__to_json(kwargs.pop('json'))

        if self.proxy is not None:
            kwargs['proxy'] = self.proxy

        if self.proxy_auth is not None:
            kwargs['proxy_auth'] = self.proxy_auth

        async with self.session.request(method, url, **kwargs) as r:
            __log__.debug(f'{method} {url} with {kwargs.get("data")} has returned {r.status}')

            data = await self.__get_data(r)

            remaining = r.headers.get('X-Ratelimit-Remaining')
            if remaining == '0' and r.status != 429:
                __log__.debug(f'A rate limit bucket has been exhausted (retry: {self.__parse_ratelimit_header(r)}).')

            if 300 > r.status >= 200:
                __log__.debug(f'{method} {url} has received {data}')
                return data

            if r.status == 429:
                raise RateLimited(r, data)

            if r.status == 400:
                raise BadRequest(r, data)

            if r.status == 403:
                raise Forbidden(r, data)

            if r.status == 404:
                raise NotFound(r, data)

            if r.status == 500:
                raise InternalServerError(r, data)

            if r.status == 502:
                raise BadGateway(r, data)

            raise HTTPException(r, data)

    async def __get_data(self, response):
        text = await response.text(encoding='utf-8')
        try:
            if response.headers['content-type'] == 'application/json':
                return json.loads(text)
        except KeyError:
            pass

        return text

    def __parse_ratelimit_header(self, request, *, use_clock=False):
        reset_after = request.headers.get('X-Ratelimit-Reset-After')
        if use_clock or not reset_after:
            utc = datetime.timezone.utc
            now = datetime.datetime.now(utc)
            reset = datetime.datetime.fromtimestamp(float(request.headers['X-Ratelimit-Reset']), utc)
            return (reset - now).total_seconds()
        else:
            return float(reset_after)

    def __to_json(self, obj):
        return json.dumps(obj, separators=(',', ':'), ensure_ascii=True)
