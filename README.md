# restcord.py
An asynchronous Python client for Discord's API

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

## Installation
```python
pip install restcord.py
```

## Import
```python
from restcord import RestCord
```

## Instantiate
```python
client = RestCord("Your Discord application token here")
```

## Use
```python
guild = await client.get_guild(265561352683126786)
print(guild)
```