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

from .snowflake import Snowflake

__all__ = (
    'PermissionOverwrite'
)

class PermissionOverwrite(Snowflake):

    __slots__ = ('type', 'allow', 'deny', 'allow_new', 'deny_new')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.type = kwargs.get('type')
        self.allow = kwargs.get('allow')
        self.deny = kwargs.get('deny')
        self.allow_new = kwargs.get('allow_new')
        self.deny_new = kwargs.get('deny_new')
