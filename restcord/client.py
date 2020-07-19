# -*- coding: utf-8 -*-
"""
The MIT License (MIT)

Copyright (c) 2020 Lethys

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

import logging
from typing import List, Optional

from aiohttp import ClientSession

from .http import HTTPClient, Route
from .models import Channel, Guild, Member, Role, User

__log__ = logging.getLogger(__name__)

__all__ = (
    'RestCord'
)

class RestCord(HTTPClient):

    """
    Asynchronous Python clinet for communicating with Discord's API.

    Parameters
    ------------
    token: str
        Your application's token from: https://discord.com/developers/applications
    session: Optional[ClientSession]
        Optionally include your aiohttp session
    """

    def __init__(self, token: str, loop=None, proxy=None, proxy_auth=None, session: Optional[ClientSession]=None) -> None:
        super().__init__(token=token, loop=loop, proxy=proxy, proxy_auth=proxy_auth, session=session)

    async def get_user(self, user_id: int) -> User:
        """|coro|
        Get a user.

        Returns
        ---------
        Optional[:class:`User`]
            The User or ``None`` if not found.

        API Documentation
        ----------
            https://discord.com/developers/docs/resources/user#get-user

        Parameters
        ----------
        user_id: :class:`int`
            Discord's identifier for the user.
        """
        r = Route('GET', '/users/{user_id}', user_id=user_id)
        user = await self._request(r)

        return User(**user)

    async def get_guild(self, guild_id: int, with_counts=False) -> Guild:
        """|coro|
        Get a guild.

        Returns
        ---------
        Optional[:class:`Guild`]
            The Guild or ``None`` if not found.

        API Documentation
        ----------
            https://discord.com/developers/docs/resources/guild#get-guild

        Parameters
        ----------
        guild_id: :class:`int`
            Discord's identifier for the guild.
        with_counts: :class:`bool`
            Whether to include approximate member counts.
            Defaults to ``False``.
        """

        if not guild_id:
            raise ValueError("Argument cannot be None: guild_id")

        r = Route("GET", '/guilds/{guild_id}?with_counts={with_counts}', guild_id=guild_id, with_counts=with_counts)
        guild = await self._request(r)

        return Guild(**guild)

    async def get_member(self, guild_id: int, member_id: int) -> Member:
        """|coro|
        Get a guild's member.

        Returns
        ---------
        Optional[:class:`Member`]
            The Member or ``None`` if not found.

        API Documentation
        ----------
            https://discord.com/developers/docs/resources/guild#get-guild-member

        Parameters
        ----------
        guild_id: :class:`int`
            Discord's identifier for the guild.
        member_id: :class:`int`
            Discord's identifier for the member.
        """

        if not guild_id:
            raise ValueError("Argument cannot be None: guild_id")

        if not member_id:
            raise ValueError("Argument cannot be None: member_id")

        r = Route('GET', '/guilds/{guild_id}/members/{member_id}', guild_id=guild_id, member_id=member_id)
        member = await self._request(r)

        return Member(**member)

    async def get_members(self, guild_id: int, limit: int=1, after_id: int=0) -> List[Member]:
        """|coro|
        Get a list of a guild's members.

        Returns
        ---------
        List[:class:`Member`]:
            The list of Members.

        API Documentation
        ----------
            https://discord.com/developers/docs/resources/guild#list-guild-members

        Parameters
        ----------
        guild_id: :class:`int`
            Discord's identifier for the guild.
        limit: Optional[:class:`int`]
            Limit the amount of members returned.
            Defaults to ``1``.
        after_id: Optional[:class:`int`]
            Only get members with an id greater than after_id.
            Defaults to ``0``.
        """

        if not guild_id:
            raise ValueError("Argument cannot be None: guild_id")

        params = {
            'limit': limit,
            'after': after_id
        }

        r = Route('GET', '/guilds/{guild_id}/members', guild_id=guild_id)
        members = await self._request(r, params=params)

        return [Member(**member) for member in members]

    async def get_channel(self, channel_id: int) -> Channel:
        """|coro|
        Get a guild's channels.

        Returns
        ---------
        Optional[:class:`Channel`]
            The Channel or ``None`` if not found.

        API Documentation
        ----------
            https://discord.com/developers/docs/resources/channel#get-channel

        Parameters
        ----------
        channel_id: :class:`int`
            Discord's identifier for the channel.
        """

        if not channel_id:
            raise ValueError("Argument cannot be None: channel_id")

        r = Route('GET', '/channels/{channel_id}', channel_id=channel_id)
        channel = await self._request(r)

        return Channel(**channel)

    async def get_channels(self, guild_id: int) -> List[Channel]:
        """|coro|
        Get a list of a guild's channels.

        Returns
        ---------
        List[:class:`Channel`]:
            The list of Channels.

        API Documentation
        ----------
            https://discord.com/developers/docs/resources/guild#get-guild-channels

        Parameters
        ----------
        guild_id: :class:`int`
            Discord's identifier for the guild.
        """

        if not guild_id:
            raise ValueError("Argument cannot be None: guild_id")
        
        r = Route('GET', '/guilds/{guild_id}/channels', guild_id=guild_id)
        channels = await self._request(r)

        return [Channel(**channel) for channel in channels]

    async def get_roles(self, guild_id: int) -> List[Role]:
        """|coro|
        Get a list of a guild's roles.

        Returns
        ---------
        List[:class:`Role`]:
            The list of Roles.

        API Documentation
        ----------
            https://discord.com/developers/docs/resources/guild#get-guild-roles

        Parameters
        ----------
        channel_id: :class:`int`
            Discord's identifier for the channel.
        """

        if not guild_id:
            raise ValueError("Argument cannot be None: guild_id")

        r = Route('GET', '/guilds/{guild_id}/roles', guild_id=guild_id)
        roles = await self._request(r)

        return [Role(**role) for role in roles]
