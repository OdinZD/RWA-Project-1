"""
Data Transfer Object definitions for user and auth API endpoints:
    - to generate API docs
    - to validate and normalize incoming requests
"""

from flask_restplus import Namespace, fields


class UserDTO:
    api = Namespace('user', description='user ops')
    user = api.model(
        name='user',
        model={
            'email': fields.String(required=True, description='email'),
            'password': fields.String(required=True, description='password'),
            'admin': fields.Boolean(required=True, description='is admin')
        }
    )


class AuthDTO:
    api = Namespace('auth', description='auth ops')
    user_auth = api.model(
        name='auth',
        model={
            'email': fields.String(required=True, description='email'),
            'password': fields.String(required=True, description='password')
        }
    )


class TicketDTO:
    api = Namespace('ticket', description='ticket ops')
    ticket = api.model(
        name='ticket',
        model={
            'content': fields.String(required=True, description='content'),
            'active': fields.Boolean(required=True, description='is active'),
            'user_id': fields.Integer(required=False, description='user')
        }
    )
