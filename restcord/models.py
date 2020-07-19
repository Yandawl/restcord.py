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

import json
from abc import ABC

__all__ = (
    'Designation',
    'Guild',
    'Channel',
    'Role',
    'Member'
)

class Designation(ABC):

    __slots__ = ('id', 'name')

    def __init__(self, **kwargs):
        self.id = kwargs.get('id', None)
        self.name = kwargs.get('name', None)

    def __str__(self):
        return f'<{type(self).__name__} id={self.id}, name={self.name}>'

    def __repr__(self):
        return self.__str__()

class Guild(Designation):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class Channel(Designation):

    __slots__ = ('type', 'position', 'permission_overwrites', 'parent_id')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.type = kwargs.get('type', None)
        self.position = kwargs.get('position', None)
        self.permission_overwrites = kwargs.get('permission_overwrites', None)
        self.parent_id = kwargs.get('parent_id', None)

    def __str__(self):
        return f'<{type(self).__name__} id={self.id}, name={self.name}, type={self.type}, position={self.position}>'

class Role(Designation):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class User(Designation):

    __slots__ = ('discriminator', 'avatar')

    def __init__(self, **kwargs):
        user = kwargs.get('user', None)

        kwargs["id"] = user.get('id', None)
        kwargs["name"] = user.get('username', None)

        self.discriminator = user.get('discriminator', None)
        self.avatar = user.get('avatar', None)

        super().__init__(**kwargs)

    def __str__(self):
        return f'<{type(self).__name__} id={self.id}, name={self.name}, discriminator={self.discriminator}>'

class Member(User):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
