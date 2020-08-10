# -*- coding: utf-8 -*-
from .snowflake import Designation

__all__ = (
    'User'
)


class User(Designation):

    """Model depicting a Discord user object."""

    __slots__ = ('discriminator', 'avatar', 'public_flags')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.name = kwargs.get('username')
        self.discriminator = kwargs.get('discriminator')
        self.avatar = kwargs.get('avatar')
        self.public_flags = kwargs.get('public_flags')

    def __str__(self):
        return f'<{type(self).__name__} id={self.id}, name={self.name}, discriminator={self.discriminator}>'

    @property
    def mention(self) -> str:
        """:class:`str`: The role's mentionable string."""
        return f'<@{self.id}>'
