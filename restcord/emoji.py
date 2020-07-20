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

from .snowflake import Designation
from .user import User

__all__ = (
    'Emoji'
)

class Emoji(Designation):

    """
    Model depicting a Discord emoji object.
    """

    __slots__ = ('roles', 'require_colons', 'managed', 'animated', 'available', 'user')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.roles = kwargs.get('roles')
        self.require_colons = kwargs.get('require_colons')
        self.managed = kwargs.get('managed')
        self.animated = kwargs.get('animated')
        self.available = kwargs.get('available')

        user = kwargs.get('user')
        if user:
            self.user = User(**user)
        else:
            self.user = None

    @property
    def mention(self) -> str:
        """:class:`str`: The emoji's mentionable string."""
        if self.animated:
            return f'<a:{self.name}:{self.id}>'
        return f'<:{self.name}:{self.id}>'
