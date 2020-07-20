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
    'Snowflake',
    'Designation'
)

class Snowflake(ABC):

    """
    Abstract base class depicting a Discord object that has an ID.
    """

    __slots__ = ('id')

    def __init__(self, **kwargs):
        self.id = kwargs.get('id')

    def __str__(self) -> str:
        return f'<{type(self).__name__} id={self.id}>'

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, other) -> bool:
        return self.id == other.id

class Designation(Snowflake):

    """
    An extention to the Snowflake abstract base class depicting a Discord object that has a name.
    """

    __slots__ = ('name')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.name = kwargs.get('name')

    def __str__(self) -> str:
        return f'<{type(self).__name__} id={self.id}, name={self.name}>'
