# -*- coding: utf-8 -*-
from restcord import utils

from .snowflake import Snowflake
from .user import User

__all__ = (
    'Message'
)


class Message(Snowflake):

    """Model depicting a Discord message object."""

    __slots__ = ('channel_id', 'type', 'content', 'author', 'pinned', 'tts', 'mention_everyone', 'timestamp', 'edited_timestamp')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.channel_id = kwargs.get('channel_id')
        self.type = kwargs.get('type')
        self.content = kwargs.get('content')

        author = kwargs.get('author')
        if author:
            self.author = User(**author)
        else:
            self.author = None

        self.pinned = kwargs.get('pinned')
        self.tts = kwargs.get('tts')
        self.mention_everyone = kwargs.get('mention_everyone')

        self.timestamp = utils.parse_time(kwargs.get('timestamp'))

        edited_timestamp = kwargs.get('edited_timestamp')
        if edited_timestamp:
            self.edited_timestamp = utils.parse_time(edited_timestamp)
        else:
            self.edited_timestamp = None

    def __str__(self) -> str:
        return f'<{type(self).__name__} id={self.id}, channel_id={self.channel_id}, timestamp={self.timestamp}>'
