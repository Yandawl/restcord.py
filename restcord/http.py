# -*- coding: utf-8 -*-

"""
The MIT License (MIT)

Copyright (c) 2015-2020 Rapptz

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

import asyncio
import datetime
import json
import logging
import sys
from typing import Optional
from urllib.parse import quote as _uriquote
from weakref import WeakValueDictionary

import aiohttp
from aiohttp import ClientSession

from . import __version__
from .errors import Forbidden, HTTPException, NotFound

__log__ = logging.getLogger(__name__)

__all__ = (
    'Unlockable',
    'Route',
    'HTTPClient'
)

class Unlockable:

    def __init__(self, lock):
        self.lock = lock
        self._unlock = True

    def __enter__(self):
        return self

    def defer(self):
        self._unlock = False

    def __exit__(self, type, value, traceback):
        if self._unlock:
            self.lock.release()

class Route:

    BASE = 'https://discord.com/api'

    def __init__(self, method, path, **kwargs):
        self.path = path
        self.method = method
        url = (self.BASE + self.path)
        if kwargs:
            self.url = url.format(**{k: _uriquote(v) if isinstance(v, str) else v for k, v in kwargs.items()})
        else:
            self.url = url

        self.channel_id = kwargs.get('channel_id')
        self.guild_id = kwargs.get('guild_id')

    @property
    def bucket(self):
        return f'{self.channel_id}:{self.guild_id}:{self.path}'


class HTTPClient:

    __slots__ = ('token', 'loop', 'proxy', 'proxy_auth', '__locks', '__global_over', '__session', '__agent')

    def __init__(self, token: str, loop=None, proxy=None, proxy_auth=None, session: Optional[ClientSession]=None) -> None:
        self.token = token
        self.loop = asyncio.get_event_loop() if loop is None else loop
        self.proxy = proxy
        self.proxy_auth = proxy_auth
        self.__locks = WeakValueDictionary()
        self.__global_over = asyncio.Event()
        self.__global_over.set()
        self.__session = session
        self.__agent = f'RestCord.py (https://github.com/Yandawl/restcord.py {__version__}) Python/{sys.version_info[0]}.{sys.version_info[1]} aiohttp/{aiohttp.__version__}'

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
        bucket = route.bucket
        method = route.method
        url = route.url

        lock = self.__locks.get(bucket)
        if lock is None:
            lock = asyncio.Lock()
            if bucket is not None:
                self.__locks[bucket] = lock

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

        if not self.__global_over.is_set():
            await self.__global_over.wait()

        await lock.acquire()

        with Unlockable(lock) as unlockable:
            for tries in range(5):

                async with self.session.request(method, url, **kwargs) as r:
                    __log__.debug('%s %s with %s has returned %s', method, url, kwargs.get('data'), r.status)

                    data = await self.__get_data(r)

                    remaining = r.headers.get('X-Ratelimit-Remaining')
                    if remaining == '0' and r.status != 429:
                        delta = self.__parse_ratelimit_header(r)
                        __log__.debug('A rate limit bucket has been exhausted (bucket: %s, retry: %s).', bucket, delta)
                        unlockable.defer()
                        self.loop.call_later(delta, lock.release)
                    
                    if 300 > r.status >= 200:
                        __log__.debug('%s %s has received %s', method, url, data)
                        return data
                    
                    if r.status == 429:
                        if not r.headers.get('Via'):
                            raise Exception()

                        fmt = 'We are being rate limited. Retrying in %.2f seconds. Handled under the bucket "%s"'

                        retry_after = data['retry_after'] / 1000.0
                        __log__.warning(fmt, retry_after, bucket)

                        is_global = data.get('global', False)
                        if is_global:
                            __log__.warning('Global rate limit has been hit. Retrying in %.2f seconds.', retry_after)
                            self.__global_over.clear()

                        await asyncio.sleep(retry_after)
                        __log__.debug('Done sleeping for the rate limit. Retrying...')

                        if is_global:
                            self.__global_over.set()
                            __log__.debug('Global rate limit is now over.')
                        continue

                    if r.status in [500, 502]:
                        await asyncio.sleep(1 + tries * 2)
                        continue
                
                    if r.status == 403:
                        raise Forbidden(r, data)
                    elif r.status == 404:
                        raise NotFound(r, data)
                    else:
                        raise HTTPException(r, data)

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
