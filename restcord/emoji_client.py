# -*- coding: utf-8 -*-
import logging
from typing import List, Optional

from aiohttp import ClientSession

from .emoji import Emoji
from .http import HTTPClient, Route

__log__ = logging.getLogger(__name__)

__all__ = (
    'EmojiClient'
)


class EmojiClient(HTTPClient):
    """ HTTPClient for interacting with Discord's Emoji API

    API Documentation
    ----------
        https://discord.com/developers/docs/resources/emoji

    Parent
    ----------
    HTTPClient: :class:`HTTPClient`
        The class that handles the HTTP requests and responses including rate limit handling and HTTP status codes.
    """

    def __init__(self, token: str, loop=None, proxy=None, proxy_auth=None, session: Optional[ClientSession] = None) -> None:
        super().__init__(token=token, loop=loop, proxy=proxy, proxy_auth=proxy_auth, session=session)

    async def get_emoji(self, guild_id: int, emoji_id: int) -> Emoji:
        """|coro| Get a guild emoji.

        Returns
        ---------
        Optional[:class:`Emoji`]
            The Emoji or ``None`` if not found.

        API Documentation
        ----------
            https://discord.com/developers/docs/resources/emoji#get-guild-emoji

        Parameters
        ----------
        guild_id: :class:`int`
            Discord's identifier for the guild.
        emoji_id: :class:`int`
            Discord's identifier for the emoji.
        """
        if not guild_id:
            raise ValueError("Argument cannot be None: guild_id")

        if not emoji_id:
            raise ValueError("Argument cannot be None: emoji_id")

        emoji = await self._request(Route("GET", f'/guilds/{guild_id}/emojis/{emoji_id}'))

        return Emoji(**emoji)

    async def get_emojis(self, guild_id: int) -> List[Emoji]:
        """|coro| Get a guild's emojis.

        Returns
        ---------
        List[:class:`Emoji`]:
            The list of Emoji.

        API Documentation
        ----------
            https://discord.com/developers/docs/resources/emoji#list-guild-emojis

        Parameters
        ----------
        guild_id: :class:`int`
            Discord's identifier for the guild.
        """
        if not guild_id:
            raise ValueError("Argument cannot be None: guild_id")

        emojis = await self._request(Route("GET", f'/guilds/{guild_id}/emojis'))

        return [Emoji(**emojis) for emoji in emojis]

    async def delete_emoji(self, guild_id: int, emoji_id: int):
        """|coro| Deletes an emoji from a guild.

        API Documentation
        ----------
            https://discord.com/developers/docs/resources/emoji#delete-guild-emoji

        Parameters
        ----------
        guild_id: :class:`int`
            Discord's identifier for the guild.
        emoji_id: :class:`int`
            Discord's identifier for the emoji.
        """
        if not guild_id:
            raise ValueError("Argument cannot be None: channel_id")

        if not emoji_id:
            raise ValueError("Argument cannot be None: emoji_id")

        await self._request(Route('DELETE', f'/guilds/{guild_id}/emojis/{emoji_id}'))
