import datetime
import uuid
from typing import Dict, Iterable, Tuple

from app.main import db
from app.main.model.user import User


def generate_token(user: User) -> Dict:
    """
    Function to generate auth token based on user id and secret (key)
    """
    context: Dict = dict()
    status: int = 201

    try:
        auth_token: str = user.encode_auth_token(user.id)
        context.update(
            status='success',
            msg='User created successfully',
            Authorization=auth_token.decode()
        )
    except Exception:
        context.update(status='fail', msg='Server failure')
        status = 401

    return context, status


def create(data: Dict) -> Tuple[Dict, int]:
    """
    Function to create user instance in database.

    If user already exists with same email, related message and status code is returned.
    Else, new user instance is created in database, user token is generated and returned.
    """
    context: Dict = dict()
    status: int = 201

    email: str = data.get('email')
    instance: User = User.query.filter_by(email=email).first()

    if not instance:
        instance = User(
            email=email,
            admin=data.get('admin'),
            password=data.get('password')
        )
        db.session.add(instance)
        db.session.commit()
        return generate_token(instance)
    else:
        context.update(status='error', msg='User already exists')
        status = 409

    return context, status


def all() -> Iterable:
    """
    Function to get all available user instances from database
    """
    return User.query.all()


def get(**kw) -> User:
    """
    Function to get specific user instance from database
    """
    return User.query.filter_by(**kw).first()


def get_user_by_token(token: str) -> User:
    """
    Function to get user by token. Main difference is that, before user
    fetch from database, token decode is executed
    """
    user_id: int = User.decode_auth_token(token)
    return get(id=user_id)
