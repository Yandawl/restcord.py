# -*- coding: utf-8 -*-
from .user import User
from .guild import GuildPreview

__all__ = (
    'Invite'
)


class Invite:

    """Model depicting a Discord invite object."""

    __slots__ = ('code', 'guild', 'channel', 'inviter', 'target_user', 'target_user_type', 'approximate_presence_count', 'approximate_member_count')

    def __init__(self, **kwargs):
        self.code = kwargs.get('code')
        self.guild = GuildPreview(**kwargs.get('guild'))
        self.channel = kwargs.get('channel')

        inviter = kwargs.get('inviter')
        if inviter:
            self.inviter = User(**inviter)
        else:
            self.inviter = None

        self.target_user = kwargs.get('target_user')
        self.target_user_type = kwargs.get('target_user_type')
        self.approximate_presence_count = kwargs.get('approximate_presence_count')
        self.approximate_member_count = kwargs.get('approximate_member_count')

    def __str__(self) -> str:
        return f'<{type(self).__name__} code={self.code}>'

    def __repr__(self) -> str:
        return self.__str__()
