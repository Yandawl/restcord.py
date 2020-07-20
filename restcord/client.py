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

from .ban import Ban
from .channel import Channel
from .emoji import Emoji
from .guild import Guild
from .http import HTTPClient, Route
from .member import Member
from .message import Message
from .role import Role
from .user import User

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

        if not user_id:
            raise ValueError("Argument cannot be None: user_id")

        user = await self._request(Route('GET', f'/users/{user_id}'))

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

        params = {
            'with_counts': int(with_counts)
        }

        guild = await self._request(Route("GET", f'/guilds/{guild_id}'), params=params)

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

        member = await self._request(Route('GET', f'/guilds/{guild_id}/members/{member_id}'))

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

        members = await self._request(Route('GET', f'/guilds/{guild_id}/members'), params=params)

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

        channel = await self._request(Route('GET', f'/channels/{channel_id}'))

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

        channels = await self._request(Route('GET', f'/guilds/{guild_id}/channels'))

        return [Channel(**channel) for channel in channels]

    async def get_message(self, channel_id: int, message_id: int, ) -> Message:
        """|coro|
        Get a channel's message.

        Returns
        ---------
        Optional[:class:`Message`]
            The Message or ``None`` if not found.

        API Documentation
        ----------
            https://discord.com/developers/docs/resources/channel#get-channel-message

        Parameters
        ----------
        channel_id: :class:`int`
            Discord's identifier for the channel.
        message_id: :class:`int`
            Discord's identifier for the message.
        """

        if not channel_id:
            raise ValueError("Argument cannot be None: channel_id")

        if not message_id:
            raise ValueError("Argument cannot be None: message_id")

        message = await self._request(Route('GET', f'/channels/{channel_id}/messages/{message_id}'))

        return Message(**message)

    async def get_messages(self, channel_id: int, around=None, before=None, after=None, limit=50) -> List[Message]:
        """|coro|
        Get a list of a channel's messages.

        Returns
        ---------
        List[:class:`Message`]:
            The list of Channels.

        API Documentation
        ----------
            https://discord.com/developers/docs/resources/channel#get-channel-messages

        Parameters
        ----------
        channel_id: :class:`int`
            Discord's identifier for the channel.
        around: Optional[:class:`int`]
	        Get messages around this message ID
        before: Optional[:class:`int`]
	        Get messages before this message ID
        after: Optional[:class:`int`]
	        Get messages after this message ID
        limit: Optional[:class:`int`]
	        Max number of messages to return (1-100).
            Defaults to 50.
        """

        if not channel_id:
            raise ValueError("Argument cannot be None: channel_id")

        params = {
            'limit': limit
        }

        if before is not None:
            params['before'] = before

        if after is not None:
            params['after'] = after

        if around is not None:
            params['around'] = around

        messages = await self._request(Route('GET', f'/channels/{channel_id}/messages'), params=params)

        return [Message(**message) for message in messages]

    async def get_reactions(self, channel_id: int, message_id: int, emoji: str, before=None, after=None, limit=25) -> List[User]:
        """|coro|
        Get a list of users who have reacted to this message with the emoji.

        Returns
        ---------
        List[:class:`User`]:
            The list of Users who have added this reaction.

        API Documentation
        ----------
            https://discord.com/developers/docs/resources/channel#get-reactions

        Parameters
        ----------
        channel_id: :class:`int`
            Discord's identifier for the channel.
        message_id: :class:`int`
            Discord's identifier for the message_id.
        emoji: :class:`str`
            Discord's identifier for the channel.
        before: Optional[:class:`int`]
	        Get reactions before this user ID
        after: Optional[:class:`int`]
	        Get reactions after this user ID
        limit: Optional[:class:`int`]
	        Max number of users to return.
            Defaults to 25.
        """

        if not channel_id:
            raise ValueError("Argument cannot be None: channel_id")

        if not message_id:
            raise ValueError("Argument cannot be None: message_id")

        if not emoji:
            raise ValueError("Argument cannot be None: emoji")

        params = {
            'limit': limit
        }

        if before is not None:
            params['before'] = before

        if after is not None:
            params['after'] = after

        users = await self._request(Route('GET', f'/channels/{channel_id}/messages/{message_id}/reactions/{emoji}'), params=params)

        return [User(**user) for user in users]

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

        roles = await self._request(Route('GET', f'/guilds/{guild_id}/roles'))

        return [Role(**role) for role in roles]

    async def get_emoji(self, guild_id: int, emoji_id: int) -> Emoji:
        """|coro|
        Get a guild emoji.

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
        """|coro|
        Get a guild's emojis.

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

    async def get_ban(self, guild_id: int, user_id: int) -> Ban:
        """|coro|
        Get a guild ban.

        Returns
        ---------
        Optional[:class:`Ban`]
            The Ban or ``None`` if not found.

        API Documentation
        ----------
            https://discord.com/developers/docs/resources/guild#get-guild-ban

        Parameters
        ----------
        guild_id: :class:`int`
            Discord's identifier for the guild.
        user_id: :class:`int`
            Discord's identifier for the user.

        Raises
        -------
        Forbidden
            You do not have proper permissions to get the information.
        HTTPException
            An error occurred while fetching the information.
        """

        if not guild_id:
            raise ValueError("Argument cannot be None: guild_id")

        if not user_id:
            raise ValueError("Argument cannot be None: user_id")

        ban = await self._request(Route("GET", f'/guilds/{guild_id}/bans/{user_id}'))

        return Ban(**ban)

    async def get_bans(self, guild_id: int) -> List[Ban]:
        """|coro|
        Get a guild's bans.

        Returns
        ---------
        List[:class:`Role`]:
            The list of Roles.

        API Documentation
        ----------
            https://discord.com/developers/docs/resources/guild#get-guild-bans

        Parameters
        ----------
        guild_id: :class:`int`
            Discord's identifier for the guild.
        with_counts: :class:`bool`

        Raises
        -------
        Forbidden
            You do not have proper permissions to get the information.
        HTTPException
            An error occurred while fetching the information.
        """

        if not guild_id:
            raise ValueError("Argument cannot be None: guild_id")

        bans = await self._request(Route("GET", f'/guilds/{guild_id}/bans'))

        return [Ban(**bans) for ban in bans]
