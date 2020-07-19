# -*- coding: utf-8 -*-
"""
The MIT License (MIT)

Copyright (c) 2020 Lethys

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

import json
from abc import ABC

from . import utils

__all__ = (
    'Snowflake',
    'Guild',
    'Channel',
    'Role',
    'Member'
)

class Snowflake(ABC):

    __slots__ = ('_raw', 'id')

    def __init__(self, **kwargs):
        self._raw = kwargs
        self.id = kwargs.get('id')

    def __str__(self) -> str:
        return f'<{type(self).__name__} id={self.id}>'

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, other) -> bool:
        return self.id == other.id

    def to_json(self):
        return json.dumps(self._raw, separators=(',', ':'), ensure_ascii=True)

class Designation(Snowflake):

    __slots__ = ('name')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.name = kwargs.get('name')

    def __str__(self) -> str:
        return f'<{type(self).__name__} id={self.id}, name={self.name}>'

class PermissionOverwrite(Snowflake):

    __slots__ = ('type', 'allow', 'deny', 'allow_new', 'deny_new')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.type = kwargs.get('type')
        self.allow = kwargs.get('allow')
        self.deny = kwargs.get('deny')
        self.allow_new = kwargs.get('allow_new')
        self.deny_new = kwargs.get('deny_new')


class Emoji(Designation):

    __slots__ = ('roles', 'require_colons', 'managed', 'animated', 'available')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.roles = kwargs.get('roles')
        self.require_colons = kwargs.get('require_colons')
        self.managed = kwargs.get('managed')
        self.animated = kwargs.get('animated')
        self.available = kwargs.get('available')

    @property
    def mention(self) -> str:
        """:class:`str`: The emoji's mentionable string."""
        if self.animated:
            return f'<a:{self.name}:{self.id}>'
        return f'<:{self.name}:{self.id}>'

class Guild(Designation):

    __slots__ = (
        'owner_id', 'application_id', 'region', 'description', 'splash', 'discovery_splash', 'banner', 'afk_channel_id', 'afk_timeout',
        'system_channel_id', 'widget_enabled', 'widget_channel_id', 'verification_level', 'features', 'emojis', 'roles', 'default_message_notifications',
        'mfa_level', 'explicit_content_filter', 'max_presences', 'max_members', 'max_video_channel_users', 'vanity_url_code', 'premium_tier', 'premium_subscription_count',
        'system_channel_flags', 'preferred_locale', 'rules_channel_id', 'public_updates_channel_id', 'embed_enabled', 'embed_channel_id'
    )

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.owner_id = kwargs.get('owner_id')
        self.application_id = kwargs.get('application_id')
        self.region = kwargs.get('region')
        self.description = kwargs.get('description')
        self.splash = kwargs.get('splash')
        self.discovery_splash = kwargs.get('discovery_splash')
        self.banner = kwargs.get('banner')
        self.afk_channel_id = kwargs.get('afk_channel_id')
        self.afk_timeout = kwargs.get('afk_timeout')
        self.system_channel_id = kwargs.get('system_channel_id')
        self.widget_enabled = kwargs.get('widget_enabled')
        self.widget_channel_id = kwargs.get('widget_channel_id')
        self.verification_level = kwargs.get('verification_level')
        self.features = kwargs.get('features')
        self.emojis = [Emoji(**e) for e in kwargs.get('emojis', [])]
        self.roles = [Role(**r) for r in kwargs.get('roles', [])]
        self.default_message_notifications = kwargs.get('default_message_notifications')
        self.mfa_level = kwargs.get('mfa_level')
        self.explicit_content_filter = kwargs.get('explicit_content_filter')
        self.max_presences = kwargs.get('max_presences')
        self.max_members = kwargs.get('max_members')
        self.max_video_channel_users = kwargs.get('max_video_channel_users')
        self.vanity_url_code = kwargs.get('vanity_url_code')
        self.premium_tier = kwargs.get('premium_tier')
        self.premium_subscription_count = kwargs.get('premium_subscription_count')
        self.system_channel_flags = kwargs.get('system_channel_flags')
        self.preferred_locale = kwargs.get('preferred_locale')
        self.rules_channel_id = kwargs.get('rules_channel_id')
        self.public_updates_channel_id = kwargs.get('public_updates_channel_id')
        self.embed_enabled = kwargs.get('owner_id')
        self.embed_channel_id = kwargs.get('owner_id')

class Channel(Designation):

    __slots__ = ('guild_id', 'type', 'position', 'permission_overwrites', 'parent_id', 'last_message_id', 'last_pin_timestamp', 'topic', 'nsfw', 'permission_overwrites')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.guild_id = kwargs.get('guild_id')
        self.type = kwargs.get('type')
        self.position = kwargs.get('position')
        self.permission_overwrites = kwargs.get('permission_overwrites')
        self.parent_id = kwargs.get('parent_id')
        self.last_message_id = kwargs.get('last_message_id')
        self.last_pin_timestamp = kwargs.get('last_pin_timestamp')
        self.topic = kwargs.get('topic')
        self.nsfw = kwargs.get('nsfw')
        self.permission_overwrites = [PermissionOverwrite(**p) for p in kwargs.get('permission_overwrites', [])]

    def __str__(self):
        return f'<{type(self).__name__} id={self.id}, name={self.name}, type={self.type}, position={self.position}>'

    @property
    def mention(self) -> str:
        """:class:`str`: The channel's mentionable string."""
        return f'<#{self.id}>'

class Role(Designation):

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

class User(Designation):

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

class Member(User):

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
