from flask import request, Flask
from app.engine.ldap_service import auth as auth_engine
from app.engine.ldap_service.models.LdapUser import LdapUser
from . import users
from app.engine.user import BaseEngineBL as ENGINE_USER
from app.engine.jwt import *
from app.constants import APIStatus, Response, ResponseObject
from .dtos import *
from .helper import *
from app import app

# create a route for get user info
@users.route('/<string:targetUserId>', methods=['GET'])
@token_required
def get_user_info(userId: User, targetUserId: str):

    target_user: User = ENGINE_USER.find_user_by_id(targetUserId)
    
    if target_user is None:
        return Response(APIStatus.NOT_FOUND).to_json()
    if (targetUserId == userId):
        user_info = cast_user_to_user_dto(target_user, True)
        return ResponseObject(APIStatus.SUCCESS, user_info.to_json()).to_json()
    user_info = cast_user_to_user_dto(target_user, False)
    return ResponseObject(APIStatus.SUCCESS, user_info.to_json()).to_json()

# create a route for update user info
@users.route('/<string:targetUserId>', methods=['PUT'])
@token_required
def update_user_info(userId: str, targetUserId: str):
    try:
        if (userId != targetUserId):
            return Response(APIStatus.NOT_ALLOWED).to_json()
         # get body
        body = request.get_json()
        # not allowed to update Id field
        if 'id' in body:
            del body['id']
        is_success: bool = ENGINE_USER.update_user(userId, body)
        if is_success == True:
            return Response(APIStatus.SUCCESS).to_json()
        else:
            return Response(APIStatus.NOT_MODIFIED).to_json()
    # mongo exception
    except Exception as e:
        # log error
        app.logger.error(e)
        return Response(APIStatus.SERVER_ERROR).to_json()


   


