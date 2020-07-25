# -*- coding: utf-8 -*-
import logging
from typing import List, Optional

from aiohttp import ClientSession

from .http import HTTPClient, Route
from .message import Message
from .user import User

__log__ = logging.getLogger(__name__)

__all__ = (
    'ChannelClient'
)

class ChannelClient(HTTPClient):

    def __init__(self, token: str, loop=None, proxy=None, proxy_auth=None, session: Optional[ClientSession]=None) -> None:
        super().__init__(token=token, loop=loop, proxy=proxy, proxy_auth=proxy_auth, session=session)

    async def get_message(self, channel_id: int, message_id: int) -> Message:
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

    async def add_reaction(self, channel_id: int, message_id: int, emoji: str):
        """|coro|
        Add a reaction to a message.

        API Documentation
        ----------
            https://discord.com/developers/docs/resources/channel#create-reaction

        Parameters
        ----------
        channel_id: :class:`int`
            Discord's identifier for the channel.
        message_id: :class:`int`
            Discord's identifier for the message.
        emoji: :class:`str`
            The URL encoded emoji
        """

        if not channel_id:
            raise ValueError("Argument cannot be None: channel_id")

        if not message_id:
            raise ValueError("Argument cannot be None: message_id")

        if not emoji:
            raise ValueError("Argument cannot be None: emoji")

        await self._request(Route('PUT', f'/channels/{channel_id}/messages/{message_id}/reactions/{emoji}/@me'))

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