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

from .emoji import Emoji
from .role import Role
from .snowflake import Designation

__all__ = (
    'Guild'
)

class Guild(Designation):

    """
    Model depicting a Discord guild object.
    """

    __slots__ = (
        'owner_id', 'application_id', 'region', 'description', 'splash', 'discovery_splash', 'banner', 'afk_channel_id', 'afk_timeout',
        'system_channel_id', 'widget_enabled', 'widget_channel_id', 'verification_level', 'features', 'emojis', 'roles', 'default_message_notifications',
        'mfa_level', 'explicit_content_filter', 'max_presences', 'max_members', 'max_video_channel_users', 'vanity_url_code', 'premium_tier', 'premium_subscription_count',
        'system_channel_flags', 'preferred_locale', 'rules_channel_id', 'public_updates_channel_id', 'embed_enabled', 'embed_channel_id', 'approximate_member_count',
        'approximate_presence_count'
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
        self.embed_enabled = kwargs.get('embed_enabled')
        self.embed_channel_id = kwargs.get('embed_channel_id')
        self.approximate_member_count = kwargs.get('approximate_member_count')
        self.approximate_presence_count = kwargs.get('approximate_presence_count')
