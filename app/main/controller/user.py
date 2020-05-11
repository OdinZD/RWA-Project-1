from typing import Dict

from flask import request
from flask_restplus import Resource

from ..service import user as user_manager
from ..util.decorators import admin_required, auth_required
from ..util.dto import UserDTO

api = UserDTO.api
_user = UserDTO.user


@api.route('/')
class UserList(Resource):
    @api.doc('list_of_registered_users', params={'Authorization': {'in': 'header', 'description': 'An authorization token'}})
    @admin_required
    @api.marshal_list_with(_user, envelope='data')
    def get(self):
        return user_manager.all()

    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    @api.expect(_user, validate=True)
    def post(self):
        data: Dict = request.json
        return user_manager.create(data=data)


@api.route('/<email>')
@api.param('email', 'User email')
@api.response(404, 'User not found.')
class User(Resource):
    @api.doc('get a user')
    @api.marshal_with(_user)
    def get(self, email: str):
        instance: User = user_manager.get(email=email)
        if not instance:
            api.abort(404)
        else:
            return instance
