# -*- coding: utf-8 -*-
import re
from datetime import datetime


def parse_time(timestamp):
    if timestamp:
        return datetime(*map(int, re.split(r'[^\d]', timestamp.replace('+00:00', ''))))
    return None


def try_cast(value, cast_to: type):
    if not value:
        return None
    return cast_to(value)
