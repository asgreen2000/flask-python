from flask import request, Flask
from app.engine.ldap_service import auth as auth_engine
from app.engine.ldap_service.models.LdapUser import LdapUser
from . import users
from app.engine.user import *
from app.engine.jwt import *
from app.constants import APIStatus, Response, ResponseObject
from .dtos import *
from .helper import *

# create a route for get user info
@users.route('/<string:userId>', methods=['GET'])
@token_required
def get_user_info(user: User, userId: str):

    
    # if (user.get_id() == userId):
    #     user_info = cast_user_to_user_dto(user, True)
    #     return ResponseObject(APIStatus.SUCCESS, user_info.to_json()).to_json()
    target_user: User = find_user_by_id(userId)
    
    if target_user is None:
        return Response(APIStatus.NOT_FOUND).to_json()
    if (user.get_id() == userId):
        user_info = cast_user_to_user_dto(user, True)
        return ResponseObject(APIStatus.SUCCESS, user_info.to_json()).to_json()
    user_info = cast_user_to_user_dto(target_user, False)
    return ResponseObject(APIStatus.SUCCESS, user_info.to_json()).to_json()


