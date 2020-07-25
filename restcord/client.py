# -*- coding: utf-8 -*-
import logging
from typing import Optional

from aiohttp import ClientSession

from .channel_client import ChannelClient
from .emoji_client import EmojiClient
from .guild_client import GuildClient
from .user_client import UserClient
from .voice_client import VoiceClient

__log__ = logging.getLogger(__name__)

__all__ = (
    'RestCord'
)

class RestCord:

    """
    Asynchronous Python clinet for communicating with Discord's API.

    Parameters
    ------------
    token: str
        Your application's token from: https://discord.com/developers/applications
    session: Optional[ClientSession]
        Optionally include your aiohttp session
    """

    __slots__ = ('channel_client', 'emoji_client', 'guild_client', 'user_client', 'voice_client')

    def __init__(self, token: str, loop=None, proxy=None, proxy_auth=None, session: Optional[ClientSession]=None) -> None:
        self.channel_client = ChannelClient(token=token, loop=loop, proxy=proxy, proxy_auth=proxy_auth, session=session)
        self.emoji_client = EmojiClient(token=token, loop=loop, proxy=proxy, proxy_auth=proxy_auth, session=session)
        self.guild_client = GuildClient(token=token, loop=loop, proxy=proxy, proxy_auth=proxy_auth, session=session)
        self.user_client = UserClient(token=token, loop=loop, proxy=proxy, proxy_auth=proxy_auth, session=session)
        self.voice_client = VoiceClient(token=token, loop=loop, proxy=proxy, proxy_auth=proxy_auth, session=session)

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.close()

    async def close(self):
        await self.channel_client.close()
        await self.emoji_client.close()
        await self.guild_client.close()
        await self.user_client.close()
        await self.voice_client.close()
