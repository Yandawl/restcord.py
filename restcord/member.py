# -*- coding: utf-8 -*-
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
