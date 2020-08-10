# -*- coding: utf-8 -*-
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
