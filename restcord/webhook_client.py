# -*- coding: utf-8 -*-
import logging
from typing import List, Optional

from aiohttp import ClientSession

from .webhook import Webhook
from .http import HTTPClient, Route

__log__ = logging.getLogger(__name__)

__all__ = (
    'WebhookClient'
)


class WebhookClient(HTTPClient):
    """HTTPClient for interacting with Discord's Webhooks API

    API Documentation
    ----------
        https://discord.com/developers/docs/resources/webhook

    Parent
    ----------
    HTTPClient: :class:`HTTPClient`
        The class that handles the HTTP requests and responses including rate limit handling and HTTP status codes.
    """

    def __init__(self, token: str, loop=None, proxy=None, proxy_auth=None, session: Optional[ClientSession] = None) -> None:
        super().__init__(token=token, loop=loop, proxy=proxy, proxy_auth=proxy_auth, session=session)

    async def get_webhook(self, webhook_id: int) -> Webhook:
        """|coro| Get a webhook.

        Returns
        ---------
        Optional[:class:`Webhook`]
            The Webhook or ``None`` if not found.

        API Documentation
        ----------
            https://discord.com/developers/docs/resources/webhook#get-webhook

        Parameters
        ----------
        webhook_id: :class:`int`
            Discord's identifier for the webhook.
        """
        if not webhook_id:
            raise ValueError("Argument cannot be None: webhook_id")

        webhook = await self._request(Route('GET', f'/webhooks/{webhook_id}'))

        return Webhook(**webhook)

    async def get_webhook_with_token(self, webhook_id: int, token: str) -> Webhook:
        """|coro| Get a webhook with token.

        Returns
        ---------
        Optional[:class:`Webhook`]
            The Webhook or ``None`` if not found.

        API Documentation
        ----------
            https://discord.com/developers/docs/resources/webhook#get-webhook-with-token

        Parameters
        ----------
        webhook_id: :class:`int`
            Discord's identifier for the webhook.
        token: :class:`str`
            Discord's identifier for the webhook.
        """
        if not webhook_id:
            raise ValueError("Argument cannot be None: webhook_id")

        if not token:
            raise ValueError("Argument cannot be None: token")

        webhook = await self._request(Route('GET', f'/webhooks/{webhook_id}/{token}'))

        return Webhook(**webhook)

    async def get_channel_webhooks(self, channel_id: int) -> List[Webhook]:
        """|coro| Get a list of a channel's webhooks.

        Returns
        ---------
        List[:class:`Webhook`]:
            The list of Webhooks.

        API Documentation
        ----------
            https://discord.com/developers/docs/resources/webhook#get-channel-webhooks

        Parameters
        ----------
        channel_id: :class:`int`
            Discord's identifier for the channel.
        """
        if not channel_id:
            raise ValueError("Argument cannot be None: channel_id")

        webhooks = await self._request(Route('GET', f'/channels/{channel_id}/webhooks'))

        return [Webhook(**webhook) for webhook in webhooks]

    async def get_guild_webhooks(self, guild_id: int) -> List[Webhook]:
        """|coro| Get a list of a guild's webhooks.

        Returns
        ---------
        List[:class:`Webhook`]:
            The list of Webhooks.

        API Documentation
        ----------
            https://discord.com/developers/docs/resources/webhook#get-guild-webhooks

        Parameters
        ----------
        guild_id: :class:`int`
            Discord's identifier for the channel.
        """
        if not guild_id:
            raise ValueError("Argument cannot be None: guild_id")

        webhooks = await self._request(Route('GET', f'/guilds/{guild_id}/webhooks'))

        return [Webhook(**webhook) for webhook in webhooks]

    async def delete_webhook(self, webhook_id: int) -> None:
        """|coro| Deletes a webhook.

        API Documentation
        ----------
            https://discord.com/developers/docs/resources/webhook#delete-webhook

        Parameters
        ----------
        webhook_id: :class:`int`
            Discord's identifier for the webhook.
        """
        if not webhook_id:
            raise ValueError("Argument cannot be None: webhook_id")

        await self._request(Route('DELETE', f'/webhooks/{webhook_id}'))

    async def delete_webhook_with_token(self, webhook_id: int, token: str) -> None:
        """|coro| Deletes a webhook with token.

        API Documentation
        ----------
            https://discord.com/developers/docs/resources/webhook#delete-webhook-with-token

        Parameters
        ----------
        webhook_id: :class:`int`
            Discord's identifier for the webhook.
        token: :class:`str`
            Discord's identifier for the webhook.
        """
        if not webhook_id:
            raise ValueError("Argument cannot be None: webhook_id")

        await self._request(Route('DELETE', f'/webhooks/{webhook_id}/{token}'))
