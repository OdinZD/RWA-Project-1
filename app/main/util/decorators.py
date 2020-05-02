from functools import wraps

from flask import request

from app.main.service.auth import Auth


def auth_required(function):
    """
    Decorator which checks whether user is authenticated, based on incoming
    request token.

    If token validation is successful, decorated API handler is executed.
    Else, related error message and code is returned.
    """
    @wraps(function)
    def wrapper(*a, **kw):
        data, status = Auth.get_user(request)
        token = data.get('data')

        if not token:
            return data, status

        return function(*a, **kw)

    return wrapper


def admin_required(function):
    """
    Decorator which checks whether user is authenticated and is admin, based
    on incoming request token.

    If token validation is successful and user is admin, decorated API handler is executed.
    Else, related error message and code is returned.
    """
    @wraps(function)
    def wrapper(*a, **kw):
        data, status = Auth.get_user(request)
        token = data.get('data')

        if not token:
            return data, status

        if not data.get('data', {}).get('admin'):
            return {'status': 'fail', 'msg': 'admin privilege required'}, 401

        return function(*a, **kw)

    return wrapper
