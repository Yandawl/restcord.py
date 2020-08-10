# -*- coding: utf-8 -*-
from .permissions import PermissionOverwrite
from .snowflake import Designation

__all__ = (
    'Channel'
)


class Channel(Designation):

    """Model depicting a Discord channel object."""

    __slots__ = ('guild_id', 'type', 'position', 'permission_overwrites', 'parent_id', 'last_message_id', 'last_pin_timestamp', 'topic', 'nsfw', 'permission_overwrites')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.guild_id = kwargs.get('guild_id')
        self.type = kwargs.get('type')
        self.position = kwargs.get('position')
        self.permission_overwrites = kwargs.get('permission_overwrites')
        self.parent_id = kwargs.get('parent_id')
        self.last_message_id = kwargs.get('last_message_id')
        self.last_pin_timestamp = kwargs.get('last_pin_timestamp')
        self.topic = kwargs.get('topic')
        self.nsfw = kwargs.get('nsfw')
        self.permission_overwrites = [PermissionOverwrite(**p) for p in kwargs.get('permission_overwrites', [])]

    def __str__(self):
        return f'<{type(self).__name__} id={self.id}, name={self.name}, type={self.type}, position={self.position}>'

    @property
    def mention(self) -> str:
        """:class:`str`: The channel's mentionable string."""
        return f'<#{self.id}>'
