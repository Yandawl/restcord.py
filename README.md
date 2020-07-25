# restcord.py
An asynchronous Python client for Discord's API.

You can aquire an application token from Discord's [developer portal](https://discord.com/developers/applications) but please
take care to read through Discord's developer [terms of service](https://discord.com/developers/docs/legal) 
and [policy document](https://discord.com/developers/docs/policy) as you agree to use this library in accordance with these terms.

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/730c9a3ace144475baf0cc626eaf364a)](https://www.codacy.com/manual/Yandawl/restcord.py?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Yandawl/restcord.py&amp;utm_campaign=Badge_Grade)
[![PyPI version](https://badge.fury.io/py/restcord.py.svg)](https://badge.fury.io/py/restcord.py.svg)
[![Python 3.6](https://img.shields.io/badge/python-3.6-green.svg)](https://www.python.org/downloads/release/python-360/)

## Requirements
```python
python>=3.6.0
asyncio
aiohttp
json
```

## Install
```python
pip3 install restcord.py
```

## Import
```python
from restcord import RestCord
from restcord.errors import (
    BadRequest,
    Forbidden,
    NotFound,
    RateLimited,
    InternalServerError,
    BadGateway
)
```

## Instantiate

```python
client = RestCord("Your Discord application token here")
```

## Get a Guild
```python
try:
    async with client as rc:
        guild = await rc.guildget_guild(guild_id=265561352683126786)
        print(guild)
except Forbidden as ex:
    print(ex)
```

## Add a reaction to a message
```python
try:
    async with client as rc:
        await rc.channel.add_reaction(
            channel_id=331893934454472707, 
            message_id=736436235140333599, 
            emoji="msq:285508293596807168"
        )
except BadRequest as ex:
    print(ex)
except RateLimited as ex:
    if ex.is_global:
        print(f'Global rate limit has been hit. Retry in {ex.retry_after:.2f} seconds.')
    else:
        print(f'Rate limit hit. Retry in {ex.retry_after:.2f} seconds.')
```