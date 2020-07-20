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

from .permissions import PermissionOverwrite
from .snowflake import Designation

__all__ = (
    'Channel'
)

class Channel(Designation):

    """
    Model depicting a Discord channel object.
    """

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
