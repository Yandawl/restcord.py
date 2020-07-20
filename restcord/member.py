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

from .user import User

__all__ = (
    'Member'
)

class Member(User):

    """
    Model depicting a Discord member object.
    A member is an extention of :class:`User` where user is a member of a guild.
    """

    __slots__ = ('nick', 'premium_since', 'mute', 'deaf', 'joined_at')

    def __init__(self, **kwargs):
        user = kwargs.get('user')

        self.id = user.get('id')
        self.name = user.get('username')
        self.discriminator = user.get('discriminator')
        self.avatar = user.get('avatar')
        self.nick = kwargs.get('nick')
        self.premium_since = utils.parse_time(kwargs.get('premium_since'))
        self.mute = kwargs.get('mute')
        self.deaf = kwargs.get('deaf')
        self.joined_at = utils.parse_time(kwargs.get('joined_at'))

    def __str__(self):
        return f'<{type(self).__name__} id={self.id}, name={self.name}, discriminator={self.discriminator}, nick={self.nick}, joined_at={self.joined_at}>'
