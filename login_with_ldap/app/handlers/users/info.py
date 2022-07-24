from flask import request, Flask
from app.engine.ldap_service import auth as auth_engine
from app.engine.ldap_service.models.LdapUser import LdapUser
from . import users
from app.engine.user import *
from app.engine.jwt import *
from app.constants import APIStatus, Response, ResponseObject
from .dtos import *


# create a route for get user info
@users.route('/<string:username>', methods=['GET'])
@token_required
def get_user_info(user: User, username: str):
    user: User = find_user_by_username(username)
    if user is None:
        return Response(APIStatus.NOT_FOUND).to_json()
    else:
        return ResponseObject(APIStatus.SUCCESS, user.to_json()).to_json()
