# -*- coding: utf-8 -*-
from .snowflake import Designation

__all__ = (
    'VoiceRegion'
)


class VoiceRegion(Designation):

    """Model depicting a Discord voice region object."""

    __slots__ = ('vip', 'optimal', 'deprecated', 'custom')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.vip = kwargs.get('vip')
        self.optimal = kwargs.get('optimal')
        self.deprecated = kwargs.get('deprecated')
        self.custom = kwargs.get('custom')
