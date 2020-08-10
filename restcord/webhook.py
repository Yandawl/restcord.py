# -*- coding: utf-8 -*-
from .snowflake import Designation
from .user import User

__all__ = (
    'Webhook'
)


class Webhook(Designation):

    """Model depicting a Discord webhook object."""

    __slots__ = ('type', 'guild_id', 'channel_id', 'avatar', 'token', 'user')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.type = kwargs.get('type')
        self.guild_id = kwargs.get('guild_id')
        self.channel_id = kwargs.get('channel_id')
        self.avatar = kwargs.get('avatar')
        self.token = kwargs.get('token')

        user = kwargs.get('user')
        if user:
            self.user = User(**user)
        else:
            self.user = None
