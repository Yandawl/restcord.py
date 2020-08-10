# -*- coding: utf-8 -*-
from abc import ABC

__all__ = (
    'Snowflake',
    'Designation'
)


class Snowflake(ABC):

    """Abstract base class depicting a Discord object that has an ID."""

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

    """An extention to the Snowflake abstract base class depicting a Discord object that has a name."""

    __slots__ = ('name')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.name = kwargs.get('name')

    def __str__(self) -> str:
        return f'<{type(self).__name__} id={self.id}, name={self.name}>'
