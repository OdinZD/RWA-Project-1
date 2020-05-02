from datetime import datetime, timedelta
from typing import Dict, Union

import jwt

from .. import config, db, flask_bcrypt


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)
    password_hash = db.Column(db.String(100))

    tickets = db.relationship('Ticket', back_populates='user')

    @property
    def password(self):
        return self.password_hash

    @password.setter
    def password(self, value: str) -> None:
        pswd_hash: str = flask_bcrypt.generate_password_hash(value)
        self.password_hash = pswd_hash.decode('utf-8')

    def check_password(self, password: str) -> bool:
        return flask_bcrypt.check_password_hash(self.password_hash, password)

    def __repr__(self) -> str:
        return "<User '{}'>".format(self.email)

    @staticmethod
    def encode_auth_token(user_id: int) -> str:
        """
        generate user auth token using jwt.encode with secret (key)
        """
        try:
            cdt: datetime = datetime.now()
            exp = cdt + timedelta(config.get_env_var('AUTH_TOKEN_EXP_TIME'))
            payload: Dict = {'exp': exp, 'iat': cdt, 'sub': user_id}
            return jwt.encode(payload, key=config.key, algorithm='HS256')
        except Exception as exception:
            return str(exception)

    @staticmethod
    def decode_auth_token(auth_token: str) -> Union[str, int]:
        """
        decode generated token. Mainly for getting user id & fetch from db
        """
        try:
            payload = jwt.decode(auth_token, config.key)
            return payload.get('sub')
        except jwt.ExpiredSignatureError:
            return 'Signature expired, log in again'
        except jwt.InvalidTokenError:
            return 'Invalid token, log in again'
