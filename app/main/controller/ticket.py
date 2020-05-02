from typing import Dict

from flask import request
from flask_restplus import Resource

from ..service import ticket as ticket_manager
from ..service import user as user_manager
from ..util.decorators import admin_required, auth_required
from ..util.dto import TicketDTO

api = TicketDTO.api
_ticket = TicketDTO.ticket


@api.route('/')
class TicketList(Resource):
    @api.doc('list_of_all_tickets')
    @admin_required
    @api.marshal_list_with(_ticket, envelope='data')
    def get(self):
        return ticket_manager.all()

    @api.response(201, 'Ticket successfully created.')
    @api.doc('create a new ticket')
    @auth_required
    @api.expect(_ticket, validate=True)
    def post(self):
        data: Dict = request.json
        token = request.headers.get('Authorization')
        data.update(user=user_manager.get_user_by_token(token))
        return ticket_manager.create(data=data)


@api.route('/<id>')
@api.param('id', 'Ticket id')
@api.response(404, 'Ticket not found.')
class User(Resource):
    @api.doc('get a ticket')
    @api.marshal_with(_ticket)
    def get(self, id: int):
        instance: User = ticket_manager.get(id=id)
        if not instance:
            api.abort(404)
        else:
            return instance
