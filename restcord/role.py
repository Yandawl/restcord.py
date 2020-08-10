# -*- coding: utf-8 -*-
from .snowflake import Designation

__all__ = (
    'Role'
)


class Role(Designation):

    """Model depicting a Discord role object."""

    __slots__ = ('permissions', 'position', 'color', 'hoist', 'managed', 'mentionable', 'permissions_new')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.permissions = kwargs.get('permissions')
        self.position = kwargs.get('position')
        self.color = kwargs.get('color')
        self.hoist = kwargs.get('hoist')
        self.managed = kwargs.get('managed')
        self.mentionable = kwargs.get('mentionable')
        self.permissions_new = kwargs.get('permissions_new')

    @property
    def mention(self) -> str:
        """:class:`str`: The role's mentionable string."""
        return f'<@&{self.id}>'
