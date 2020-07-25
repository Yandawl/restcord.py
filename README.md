# restcord.py
An asynchronous Python client for Discord's REST API.

You can aquire an application token from Discord's [developer portal](https://discord.com/developers/applications) but please
take care to read through Discord's developer [terms of service](https://discord.com/developers/docs/legal) 
and [policy document](https://discord.com/developers/docs/policy) as you agree to use this library in accordance with these terms.

Find Discord's REST API documentation [here](https://discord.com/developers/docs/intro).

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

## Initialise
You can initialise the RestCord client with an application token, but you may also provide your own asyncio event loop, aiohttp client session.
```python
client = RestCord("Your Discord application token here")
```

## Structure
RestCord is structured in the same way as Discord's REST API [documentation](https://discord.com/developers/docs/intro). Once you have initialised RestCord you will have access to channel_client, emoji_client, guild_client, user_client and voice_client objects, which contain asynchronous methods to communicate with API end points.

#### Example: get a guild object
In this example, we use RestCord to perform a GET request to Discord's [guild](https://discord.com/developers/docs/resources/guild#get-guild) API end point, which will return a guild object. Printing this object will output some basic details about the guild such as id and name but the object contains fields as per the documentation.

```python
try:
    async with client as rc:
        guild = await rc.guild_client.get_guild(guild_id=265561352683126786)
        print(guild)
except Forbidden as ex:
    print(ex)
```

## AsyncContextManager
RestCord can be used with or without the AsyncContextManager. Using it will ensure that any open aiohttp client sessions are closed.
```python
async with client as rc:
    voice_regions = await rc.voice_client.get_voice_regions()
```

Or more granularly:

```python
async with client.guild_client as gc:
    channel = await gc.get_channel(265586371178135562)
    print(channel)
```

If you do not use the AsyncContextManager, you must call the close() function on RestCord to close any open aiohttp client sessions.
```python
member = await client.guild_client.get_member(265561352683126786, 50527603626344448)
await client.close()
```

## Errors
If Discord return error HTTP status codes, RestCord will throw a relevent exception for you to handle in your own way.

#### Example: add a reaction to a message
In this example we try to add a reaction to a message. There are several things to be aware of here:

*   Does our application have permission to add reactions to messages? If not, a Forbidden exception will be thrown.

*   Have we URL encoded the emoji as per specified by the [documentation](https://discord.com/developers/docs/resources/channel#create-reaction
). If not, a BadRequest exception will be thrown.

*   This particular end point has strict rate limits. If we have already added a reaction to the message we may be rate limited. In this case a RateLimited exception will be thrown and you can get more information about that limit from the exception object.

```python
try:
    async with client.channel_client as cc:
        await cc.add_reaction(331893934454472707, 736436235140333599, emoji="msq:285508293596807168")
except Forbidden as ex:
    print(ex)
except BadRequest as ex:
    print(ex)
except RateLimited as ex:
    if ex.is_global:
        print(f'Global rate limit has been hit. Retry in {ex.retry_after:.2f} seconds.')
    else:
        print(f'Rate limit hit. Retry in {ex.retry_after:.2f} seconds.')
```
