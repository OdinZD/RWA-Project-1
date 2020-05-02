from typing import Dict, Tuple

from app.main.model.user import User

from ..service import user as user_manager


class Auth:

    @staticmethod
    def signin(data: Dict) -> Dict:
        """
        Method to sign user in based on email & password.

        If both param match - user is signed in and auth token is generated.
        Else, related status and error message is returned.
        """
        context: Dict = dict()
        status: int = 200

        try:
            user: User = user_manager.get(email=data.get('email'))
            if (user and user.check_password(data.get('password'))):
                auth_token = user.encode_auth_token(user.id)
                if auth_token:
                    context.update(
                        status='success',
                        msg='Log in successful',
                        Authorization=auth_token.decode()
                    )
            else:
                context.update(
                    status='error',
                    msg='Email or password mismatch'
                )
                status = 401
        except Exception:
            context.update(status='fail', msg='Server failure')
            status = 500

        return context, status

    @staticmethod
    def get_user(request) -> Tuple[Dict, int]:
        """
        method to get user based on incomin request and associated token.

        If token present and is valid - user instance is returned.
        Else related error message and status code is returned.
        """
        context: Dict = dict()
        status: int = 401
        auth_token: str = request.headers.get('Authorization')

        if auth_token:
            user_id: int = User.decode_auth_token(auth_token)
            instance: User = user_manager.get(id=user_id)
            if instance:
                context.update(
                    status='success',
                    data={
                        'user_id': instance.id,
                        'email': instance.email,
                        'admin': instance.admin
                    }
                )
                status = 200
            else:
                context.update(status='fail', msg='Invalid auth token')
        else:
            context.update(status='fail', msg='Provide an auth token')

        return context, status
