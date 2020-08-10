# -*- coding: utf-8 -*-
import logging
from typing import List, Optional

from aiohttp import ClientSession

from .ban import Ban
from .channel import Channel
from .guild import Guild, GuildPreview
from .http import HTTPClient, Route
from .member import Member
from .role import Role

__log__ = logging.getLogger(__name__)

__all__ = (
    'GuildClient'
)


class GuildClient(HTTPClient):
    """HTTPClient for interacting with Discord's Guild API

    API Documentation
    ----------
        https://discord.com/developers/docs/resources/guild

    Parent
    ----------
    HTTPClient: :class:`HTTPClient`
        The class that handles the HTTP requests and responses including rate limit handling and HTTP status codes.
    """

    def __init__(self, token: str, loop=None, proxy=None, proxy_auth=None, session: Optional[ClientSession] = None) -> None:
        super().__init__(token=token, loop=loop, proxy=proxy, proxy_auth=proxy_auth, session=session)

    async def get_guild(self, guild_id: int, with_counts=False) -> Guild:
        """|coro| Get a guild.

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

    async def get_guild_preview(self, guild_id: int) -> GuildPreview:
        """|coro| Get a guild preview.

        Returns
        ---------
        Optional[:class:`GuildPreview`]
            The GuildPreview or ``None`` if not found.

        API Documentation
        ----------
            https://discord.com/developers/docs/resources/guild#guild-preview-object

        Parameters
        ----------
        guild_id: :class:`int`
            Discord's identifier for the guild.
        """
        if not guild_id:
            raise ValueError("Argument cannot be None: guild_id")

        guild = await self._request(Route("GET", f'/guilds/{guild_id}/preview'))

        return GuildPreview(**guild)

    async def get_member(self, guild_id: int, member_id: int) -> Member:
        """|coro| Get a guild's member.

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

    async def get_members(self, guild_id: int, limit: int = 1, after_id: int = 0) -> List[Member]:
        """|coro| Get a list of a guild's members.

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

    async def get_channels(self, guild_id: int) -> List[Channel]:
        """|coro| Get a list of a guild's channels.

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

    async def get_roles(self, guild_id: int) -> List[Role]:
        """|coro| Get a list of a guild's roles.

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

    async def get_ban(self, guild_id: int, user_id: int) -> Ban:
        """|coro| Get a guild ban.

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
        """|coro| Get a guild's bans.

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
