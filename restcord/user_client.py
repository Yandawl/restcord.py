# -*- coding: utf-8 -*-
import logging
from typing import Optional

from aiohttp import ClientSession

from .http import HTTPClient, Route
from .user import User

__log__ = logging.getLogger(__name__)

__all__ = (
    'UserClient'
)


class UserClient(HTTPClient):
    """HTTPClient for interacting with Discord's User API

    API Documentation
    ----------
        https://discord.com/developers/docs/resources/user

    Parent
    ----------
    HTTPClient: :class:`HTTPClient`
        The class that handles the HTTP requests and responses including rate limit handling and HTTP status codes.
    """

    def __init__(self, token: str, loop=None, proxy=None, proxy_auth=None, session: Optional[ClientSession] = None) -> None:
        super().__init__(token=token, loop=loop, proxy=proxy, proxy_auth=proxy_auth, session=session)

    async def get_user(self, user_id: int) -> User:
        """|coro| Get a user.

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
