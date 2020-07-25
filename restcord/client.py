# -*- coding: utf-8 -*-
import logging

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

    __slots__ = ('channel', 'emoji', 'guild', 'user', 'voice')

    def __init__(self, token: str, loop=None, proxy=None, proxy_auth=None, session: Optional[ClientSession]=None) -> None:
        self.channel = ChannelClient(token=token, loop=loop, proxy=proxy, proxy_auth=proxy_auth, session=session)
        self.emoji = EmojiClient(token=token, loop=loop, proxy=proxy, proxy_auth=proxy_auth, session=session)
        self.guild = GuildClient(token=token, loop=loop, proxy=proxy, proxy_auth=proxy_auth, session=session)
        self.user = UserClient(token=token, loop=loop, proxy=proxy, proxy_auth=proxy_auth, session=session)
        self.voice = VoiceClient(token=token, loop=loop, proxy=proxy, proxy_auth=proxy_auth, session=session)

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.channel.close()
        await self.emoji.close()
        await self.guild.close()
        await self.user.close()
        await self.voice.close()