from flask import request
from flask_restplus import Resource

from app.main.service.auth import Auth

from ..util.dto import AuthDTO

api = AuthDTO.api
user_auth = AuthDTO.user_auth


@api.route('/signin')
class UserLogin(Resource):
    @api.doc('user signin')
    @api.expect(user_auth, validate=True)
    def post(self):
        post_data = request.json
        return Auth.signin(data=post_data)
