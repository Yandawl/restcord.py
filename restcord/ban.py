# -*- coding: utf-8 -*-
from .user import User

__all__ = (
    'Ban'
)


class Ban:

    """
    Model depicting a Discord ban object.
    """

    __slots__ = ('reason', 'user')

    def __init__(self, **kwargs):

        self.reason = kwargs.get('reason')
        self.user = User(**kwargs.get('user'))

    def __str__(self):
        return f'<{type(self).__name__} user_id={self.user.id}, reason={self.reason}>'
