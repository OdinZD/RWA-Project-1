
from flask import Blueprint
from flask_restplus import Api

from .main.controller.auth import api as auth_api
from .main.controller.ticket import api as ticket_api
from .main.controller.user import api as user_api

blueprint = Blueprint('api', __name__)
api = Api(blueprint, title='FLASK RESTPLUS', version='1.0')
api.add_namespace(user_api, path='/user')
api.add_namespace(auth_api, path='/auth')
api.add_namespace(ticket_api, path='/ticket')
