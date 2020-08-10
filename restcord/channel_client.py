# -*- coding: utf-8 -*-
import logging
from typing import List, Optional

from aiohttp import ClientSession

from .channel import Channel
from .http import HTTPClient, Route
from .invite import Invite
from .message import Message
from .user import User

__log__ = logging.getLogger(__name__)

__all__ = (
    'ChannelClient'
)


class ChannelClient(HTTPClient):

    """HTTPClient for interacting with Discord's Channel API

    API Documentation
    ----------
        https://discord.com/developers/docs/resources/channel

    Parent
    ----------
    HTTPClient: :class:`HTTPClient`
        The class that handles the HTTP requests and responses including rate limit handling and HTTP status codes.
    """

    def __init__(self, token: str, loop=None, proxy=None, proxy_auth=None, session: Optional[ClientSession] = None) -> None:
        super().__init__(token=token, loop=loop, proxy=proxy, proxy_auth=proxy_auth, session=session)

    async def get_channel(self, channel_id: int) -> Channel:
        """|coro| Get a guild's channels.

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

    async def delete_channel(self, channel_id: int) -> None:
        """|coro| Deletes a guild channel or closes a private message.

        API Documentation
        ----------
            https://discord.com/developers/docs/resources/channel#deleteclose-channel

        Parameters
        ----------
        channel_id: :class:`int`
            Discord's identifier for the channel.
        """
        if not channel_id:
            raise ValueError("Argument cannot be None: channel_id")

        await self._request(Route('DELETE', f'/channels/{channel_id}'))

    async def get_message(self, channel_id: int, message_id: int) -> Message:
        """|coro| Get a channel's message.

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
        """|coro| Get a list of a channel's messages.

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
        """|coro| Add a reaction to a message.

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

    async def delete_reaction(self, channel_id: int, message_id: int, emoji: str):
        """|coro| Deletes a reaction this application has added to a message.

        API Documentation
        ----------
            https://discord.com/developers/docs/resources/channel#delete-own-reaction

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

        await self._request(Route('DELETE', f'/channels/{channel_id}/messages/{message_id}/reactions/{emoji}/@me'))

    async def delete_user_reaction(self, channel_id: int, message_id: int, emoji: str, user_id: int):
        """|coro| Deletes a reaction a user has added to a message.

        API Documentation
        ----------
            https://discord.com/developers/docs/resources/channel#delete-user-reaction

        Parameters
        ----------
        channel_id: :class:`int`
            Discord's identifier for the channel.
        message_id: :class:`int`
            Discord's identifier for the message.
        emoji: :class:`str`
            The URL encoded emoji
        user_id: :class:`int`
            Discord's identifier for the user.
        """
        if not channel_id:
            raise ValueError("Argument cannot be None: channel_id")

        if not message_id:
            raise ValueError("Argument cannot be None: message_id")

        if not emoji:
            raise ValueError("Argument cannot be None: emoji")

        if not user_id:
            raise ValueError("Argument cannot be None: user_id")

        await self._request(Route('DELETE', f'/channels/{channel_id}/messages/{message_id}/reactions/{emoji}/{user_id}'))

    async def get_reactions(self, channel_id: int, message_id: int, emoji: str, before=None, after=None, limit=25) -> List[User]:
        """|coro| Get a list of users who have reacted to this message with the emoji.

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

    async def delete_all_reactions(self, channel_id: int, message_id: int):
        """|coro| Deletes all reactions on a message.

        API Documentation
        ----------
            https://discord.com/developers/docs/resources/channel#delete-all-reactions

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

        await self._request(Route('DELETE', f'/channels/{channel_id}/messages/{message_id}/reactions'))

    async def delete_all_reactions_for_emoji(self, channel_id: int, message_id: int, emoji: str):
        """|coro| Deletes all reactions for an emoji on a message

        API Documentation
        ----------
            https://discord.com/developers/docs/resources/channel#delete-own-reaction

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

        await self._request(Route('DELETE', f'/channels/{channel_id}/messages/{message_id}/reactions/{emoji}'))

    async def delete_message(self, channel_id: int, message_id: int):
        """|coro| Deletes a message.

        API Documentation
        ----------
            https://discord.com/developers/docs/resources/channel#delete-message

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

        await self._request(Route('DELETE', f'/channels/{channel_id}/messages/{message_id}'))

    async def bulk_delete_messages(self, channel_id: int, message_ids: List[int]):
        """|coro| Bulk deletes message from a channel. Minimum 2, maximum 100.

        API Documentation
        ----------
            https://discord.com/developers/docs/resources/channel#bulk-delete-messages

        Parameters
        ----------
        channel_id: :class:`int`
            Discord's identifier for the channel.
        message_ids: :class:`int`
            Discord's identifier for the message.

        Raises
        ----------
        BadRequest
            If duplicate message ids are provided or if a message is older than 2 weeks.
        """
        if not channel_id:
            raise ValueError("Argument cannot be None: channel_id")

        if not message_ids:
            raise ValueError("Argument cannot be None: message_ids")

        length = len(message_ids)
        if length < 2 or length > 100:
            raise ValueError("List length must be at least 2 and no greater than 100: message_ids")

        params = {
            'messages': message_ids
        }

        await self._request(Route('POST', f'/channels/{channel_id}/messages/bulk-delete'), params=params)

    async def get_invites(self, channel_id: int) -> List[Invite]:
        """|coro| Get a list of a channel's invites.

        Returns
        ---------
        List[:class:`Invite`]:
            The list of Invites.

        API Documentation
        ----------
            https://discord.com/developers/docs/resources/channel#get-channel-invites

        Parameters
        ----------
        channel_id: :class:`int`
            Discord's identifier for the channel.
        """
        if not channel_id:
            raise ValueError("Argument cannot be None: channel_id")

        invites = await self._request(Route('GET', f'/channels/{channel_id}/invites'))

        return [Invite(**invite) for invite in invites]

    async def create_invite(self, channel_id: int, max_age: int = 86400, max_uses: int = 0, temporary=False, unique=False, target_user=None, target_user_type=None) -> Invite:
        """|coro| Creates a new invite object for the channel.

        Returns
        ---------
        :class:`Invite`:
            The invite that was created for the channel.

        API Documentation
        ----------
            https://discord.com/developers/docs/resources/channel#create-channel-invite

        Parameters
        ----------
        channel_id: :class:`int`
            Discord's identifier for the channel.
        max_age: :class:`int`
            Duration of invite in seconds before expiry, or 0 for never.
        max_uses: :class:`str`
            Maximum number of uses or 0 for unlimited.
        temporary: :class:`bool`
            Whether this invite only grants temporary membership.
        unique: :class:`bool`
            If true, don't try to reuse a similar invite (useful for creating many unique one time use invites).
        target_user: Optional[:class:`str`]
            The target user id for this invite.
        target_user_type: Optional[:class:`str`]
            The type of target user for this invite
        """
        if not channel_id:
            raise ValueError("Argument cannot be None: channel_id")

        params = {
            'max_age': max_age,
            'max_uses': max_uses,
            'temporary': temporary,
            'unique': unique
        }

        if target_user is not None:
            params['target_user'] = target_user

        if target_user_type is not None:
            params['target_user_type'] = target_user_type

        invite = await self._request(Route('POST', f'/channels/{channel_id}/invites'), params=params)

        return Invite(**invite)
