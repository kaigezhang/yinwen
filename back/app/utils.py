# -*- coding: utf-8 -*-
"""Helper utilities and decorators."""
from flask import flash, _request_ctx_stack
from functools import wraps
from flask_jwt import _jwt
import jwt


def jwt_optional(realm=None):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            token = _jwt.request_callback()
            try:
                payload = _jwt.jwt_decode_callback(token)
            except jwt.exceptions.DecodeError:
                pass
            else:
                _request_ctx_stack.top.current_identity = _jwt.identity_callback(payload)
            return fn(*args, **kwargs)
        return decorator
    return wrapper


# from app.user.models import User # noqa
#
#
# def jwt_identity(payload):
#     user_id = payload['identity']
#     return User.get_by_id(user_id)
#
#
# def authenticate(email, password):
#     user = User.query.filter_by(email=email).first()
#     if user and user.check_password(password):
#         return user
