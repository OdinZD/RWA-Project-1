from typing import Dict, Iterable, Tuple

from app.main import db
from app.main.model.ticket import Ticket


def create(data: Dict) -> Tuple[Dict, int]:
    """
    Function to create ticket instance in database
    """
    context: Dict = dict()
    status: int = 201

    instance = Ticket(
        content=data.get('content'),
        active=data.get('active')
    )

    if data.get('user'):
        instance.user_id = data.get('user').id

    db.session.add(instance)
    db.session.commit()

    context.update(status='success', msg='Ticket created successfully')
    return context, status


def all() -> Iterable:
    """
    Function to get all available ticket instances from database
    """
    return Ticket.query.all()


def get(**kw) -> Ticket:
    """
    Function to get specific ticket instance from database
    """
    return Ticket.query.filter_by(**kw).first()
