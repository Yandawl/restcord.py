# -*- coding: utf-8 -*-
from .emoji import Emoji
from .role import Role
from .snowflake import Designation

__all__ = (
    'Guild',
    'GuildPreview',
    'WelcomeScreen',
    'WelcomeChannel'
)


class GuildPreview(Designation):

    """Model depicting a Discord guild object."""

    __slots__ = (
        'icon', 'splash', 'discovery_splash', 'features', 'emojis', 'approximate_member_count', 'approximate_presence_count', 'description', 'welcome_screen'
    )

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.icon = kwargs.get('icon')
        self.splash = kwargs.get('splash')
        self.discovery_splash = kwargs.get('discovery_splash')
        self.features = kwargs.get('features')
        self.emojis = [Emoji(**e) for e in kwargs.get('emojis', [])]
        self.approximate_member_count = kwargs.get('approximate_member_count')
        self.approximate_presence_count = kwargs.get('approximate_presence_count')
        self.description = kwargs.get('description')

        welcome_screen = kwargs.get('welcome_screen')
        if welcome_screen:
            self.welcome_screen = WelcomeScreen(**welcome_screen)
        else:
            self.welcome_screen = None


class Guild(GuildPreview):

    """Model depicting a Discord guild object."""

    __slots__ = (
        'owner_id', 'application_id', 'region', 'banner', 'afk_channel_id', 'afk_timeout',
        'system_channel_id', 'widget_enabled', 'widget_channel_id', 'verification_level', 'roles', 'default_message_notifications',
        'mfa_level', 'explicit_content_filter', 'max_presences', 'max_members', 'max_video_channel_users', 'vanity_url_code', 'premium_tier', 'premium_subscription_count',
        'system_channel_flags', 'preferred_locale', 'rules_channel_id', 'public_updates_channel_id', 'embed_enabled', 'embed_channel_id'
    )

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.owner_id = kwargs.get('owner_id')
        self.application_id = kwargs.get('application_id')
        self.region = kwargs.get('region')
        self.banner = kwargs.get('banner')
        self.afk_channel_id = kwargs.get('afk_channel_id')
        self.afk_timeout = kwargs.get('afk_timeout')
        self.system_channel_id = kwargs.get('system_channel_id')
        self.widget_enabled = kwargs.get('widget_enabled')
        self.widget_channel_id = kwargs.get('widget_channel_id')
        self.verification_level = kwargs.get('verification_level')
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


class WelcomeScreen:

    """Model depicting a Discord welcome screen object."""

    __slots__ = (
        'description', 'channels'
    )

    def __init__(self, **kwargs):
        self.description = kwargs.get('description')
        self.channels = [WelcomeChannel(**c) for c in kwargs.get('welcome_channels', [])]

    def __str__(self) -> str:
        return f'<{type(self).__name__} description={self.description}, channels={len(self.channels)}>'

    def __repr__(self) -> str:
        return self.__str__()


class WelcomeChannel:

    """Model depicting a Discord welcome screen channel object."""

    __slots__ = (
        'channel_id', 'description', 'emoji_id', 'emoji_name'
    )

    def __init__(self, **kwargs):
        self.channel_id = kwargs.get('channel_id')
        self.description = kwargs.get('description')
        self.emoji_id = kwargs.get('emoji_id')
        self.emoji_name = kwargs.get('emoji_name')

    def __str__(self) -> str:
        return f'<{type(self).__name__} channel_id={self.channel_id}, description={self.description}>'

    def __repr__(self) -> str:
        return self.__str__()
