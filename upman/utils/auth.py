#!/usr/bin/env python3
from flask import abort, request, current_app
from functools import wraps


def apikey_required(f):
    @wraps(f)
    def call(*args, **kwargs):
        auth_header = request.headers.get('Authorization')

        if not auth_header:
            return abort(401, "Authorization header missing")

        try:
            auth_type, auth_key = auth_header.split(' ', 1)
        except ValueError:
            return abort(400, "Bad Authorization header. Expected value 'Key <KEY>'")

        if auth_type != 'Key':
            return abort(400, "Bad Authorization type. Expected 'Key'")

        if current_app.config.get('API_KEY') and auth_key == current_app.config['API_KEY']:
            return f(*args, **kwargs)
        else:
            return abort(401, "Invalid key")

    return call
