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

from restcord import utils

from .snowflake import Snowflake
from .user import User

__all__ = (
    'Message'
)

class Message(Snowflake):

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
