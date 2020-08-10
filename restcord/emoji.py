# -*- coding: utf-8 -*-
from .snowflake import Designation
from .user import User

__all__ = (
    'Emoji'
)


class Emoji(Designation):

    """Model depicting a Discord emoji object."""

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
