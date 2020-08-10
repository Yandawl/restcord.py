# -*- coding: utf-8 -*-
import logging
from typing import Optional

from aiohttp import ClientSession

from .invite import Invite
from .http import HTTPClient, Route

__log__ = logging.getLogger(__name__)

__all__ = (
    'InviteClient'
)


class InviteClient(HTTPClient):
    """HTTPClient for interacting with Discord's Invite API

    API Documentation
    ----------
        https://discord.com/developers/docs/resources/invite

    Parent
    ----------
    HTTPClient: :class:`HTTPClient`
        The class that handles the HTTP requests and responses including rate limit handling and HTTP status codes.
    """

    def __init__(self, token: str, loop=None, proxy=None, proxy_auth=None, session: Optional[ClientSession] = None) -> None:
        super().__init__(token=token, loop=loop, proxy=proxy, proxy_auth=proxy_auth, session=session)

    async def get_invite(self, invite_code: str, with_counts=False) -> Invite:
        """|coro| Gets an invite.

        Returns
        ---------
        Optional[:class:`Invite`]
            The Invite or ``None`` if not found.

        API Documentation
        ----------
            https://discord.com/developers/docs/resources/invite#delete-invite

        Parameters
        ----------
        invite_code: :class:`str`
            Discord's code for the invite.
        with_counts: :class:`bool`
            Whether to include approximate member counts.
            Defaults to ``False``.
        """
        if not invite_code:
            raise ValueError("Argument cannot be None: invite_code")

        params = {
            'with_counts': int(with_counts)
        }

        invite = await self._request(Route('GET', f'/invites/{invite_code}'), params=params)

        return Invite(**invite)

    async def delete_invite(self, invite_code: str) -> Invite:
        """|coro| Deletes an invite.

        Returns
        ---------
        Optional[:class:`Invite`]
            The Invite or ``None`` if not found.

        API Documentation
        ----------
            https://discord.com/developers/docs/resources/invite#delete-invite

        Parameters
        ----------
        invite_code: :class:`str`
            Discord's code for the invite.
        """
        if not invite_code:
            raise ValueError("Argument cannot be None: invite_code")

        invite = await self._request(Route('DELETE', f'/invites/{invite_code}'))

        return Invite(**invite)
