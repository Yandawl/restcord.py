# -*- coding: utf-8 -*-
import logging
from typing import Optional

from aiohttp import ClientSession

from .channel_client import ChannelClient
from .emoji_client import EmojiClient
from .guild_client import GuildClient
from .invite_client import InviteClient
from .user_client import UserClient
from .voice_client import VoiceClient
from .webhook_client import WebhookClient

__log__ = logging.getLogger(__name__)

__all__ = (
    'RestCord'
)


class RestCord:
    """Asynchronous Python client for communicating with Discord's API.

    Parameters
    ------------
    token: str
        Your application's token from: https://discord.com/developers/applications
    session: Optional[ClientSession]
        Optionally include your aiohttp session
    """

    __slots__ = ('channel_client', 'emoji_client', 'guild_client', 'invite_client', 'user_client', 'voice_client', 'webhook_client')

    def __init__(self, token: str, loop=None, proxy=None, proxy_auth=None, session: Optional[ClientSession] = None) -> None:
        self.channel_client = ChannelClient(token, loop, proxy, proxy_auth, session)
        self.emoji_client = EmojiClient(token, loop, proxy, proxy_auth, session)
        self.guild_client = GuildClient(token, loop, proxy, proxy_auth, session)
        self.invite_client = InviteClient(token, loop, proxy, proxy_auth, session)
        self.user_client = UserClient(token, loop, proxy, proxy_auth, session)
        self.voice_client = VoiceClient(token, loop, proxy, proxy_auth, session)
        self.webhook_client = WebhookClient(token, loop, proxy, proxy_auth, session)

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.close()

    async def close(self):
        await self.channel_client.close()
        await self.emoji_client.close()
        await self.guild_client.close()
        await self.invite_client.close()
        await self.user_client.close()
        await self.voice_client.close()
        await self.webhook_client.close()
