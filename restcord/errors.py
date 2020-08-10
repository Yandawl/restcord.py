# -*- coding: utf-8 -*-
"""
The MIT License (MIT)

Copyright (c) 2015-2020 Rapptz

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


class HTTPException(Exception):

    """Exception that's thrown when an HTTP request operation fails.
    Attributes
    ------------
    response: :class:`aiohttp.ClientResponse`
        The response of the failed HTTP request. This is an
        instance of :class:`aiohttp.ClientResponse`. In some cases
        this could also be a :class:`requests.Response`.
    text: :class:`str`
        The text of the error. Could be an empty string.
    status: :class:`int`
        The status code of the HTTP request.
    code: :class:`int`
        The Discord specific error code for the failure.
    """

    def __init__(self, response, message):
        self.response = response
        self.status = response.status
        if isinstance(message, dict):
            self.code = message.get('code', 0)
            base = message.get('message', '')
            errors = message.get('errors')
            if errors:
                errors = self.flatten_dict(errors)
                helpful = '\n'.join('In %s: %s' % t for t in errors.items())
                self.text = base + '\n' + helpful
            else:
                self.text = base
        else:
            self.text = message
            self.code = 0

        fmt = '{0.status} {0.reason} (error code: {1})'
        if len(self.text):
            fmt = fmt + ': {2}'

        super().__init__(fmt.format(self.response, self.code, self.text))

    def flatten_dict(self, d, key=''):
        items = []
        for k, v in d.items():
            new_key = key + '.' + k if key else k
            if isinstance(v, dict):
                try:
                    _errors = v['_errors']
                except KeyError:
                    items.extend(self.flatten_dict(v, new_key).items())
                else:
                    items.append((new_key, ' '.join(x.get('message', '') for x in _errors)))
            else:
                items.append((new_key, v))
        return dict(items)


class BadRequest(HTTPException):

    """Exception that's thrown for when status code 400 occurs."""
    pass


class Forbidden(HTTPException):

    """Exception that's thrown for when status code 403 occurs."""
    pass


class NotFound(HTTPException):

    """Exception that's thrown for when status code 404 occurs."""
    pass


class RateLimited(HTTPException):

    """Exception that's thrown for when status code 429 occurs."""

    __slots__ = ('retry_after', 'is_global')

    def __init__(self, response, message):
        super().__init__(response, message)

        self.retry_after = message['retry_after'] / 1000.0
        self.is_global = message.get('global', False)


class InternalServerError(HTTPException):

    """Exception that's thrown for when status code 500 occurs."""
    pass


class BadGateway(HTTPException):

    """Exception that's thrown for when status code 403 occurs."""
    pass
