# -*- coding: utf-8 -*-
import logging
from typing import List, Optional

from aiohttp import ClientSession

from .http import HTTPClient, Route
from .voice import VoiceRegion

__log__ = logging.getLogger(__name__)

__all__ = (
    'VoiceClient'
)


class VoiceClient(HTTPClient):
    """HTTPClient for interacting with Discord's Voice API

    API Documentation
    ----------
        https://discord.com/developers/docs/resources/voice

    Parent
    ----------
    HTTPClient: :class:`HTTPClient`
        The class that handles the HTTP requests and responses including rate limit handling and HTTP status codes.
    """

    def __init__(self, token: str, loop=None, proxy=None, proxy_auth=None, session: Optional[ClientSession] = None) -> None:
        super().__init__(token=token, loop=loop, proxy=proxy, proxy_auth=proxy_auth, session=session)

    async def get_voice_regions(self) -> List[VoiceRegion]:
        """|coro| Get a list of voice regions.

        Returns
        ---------
        List[:class:`VoiceRegion`]:
            The list of VoiceRegions.

        API Documentation
        ----------
            https://discord.com/developers/docs/resources/voice#list-voice-regions
        """

        voice_regions = await self._request(Route('GET', '/voice/regions'))

        return [VoiceRegion(**voice_region) for voice_region in voice_regions]
