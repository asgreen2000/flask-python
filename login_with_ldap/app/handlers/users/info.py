from flask import request, Flask
from app.engine.ldap_service import auth as auth_engine
from app.engine.ldap_service.models.LdapUser import LdapUser
from . import users
from app.engine.user import *
from app.engine.jwt import *
from app.constants import APIStatus, Response, ResponseObject
from .dtos import *
from .helper import *
from app import app

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
        user_info = cast_user_to_user_dto(target_user, True)
        return ResponseObject(APIStatus.SUCCESS, user_info.to_json()).to_json()
    user_info = cast_user_to_user_dto(target_user, False)
    return ResponseObject(APIStatus.SUCCESS, user_info.to_json()).to_json()

# create a route for update user info
@users.route('/', methods=['PUT'])
@token_required
def update_user_info(user: User):

    try:
         # get body
        body = request.get_json()
        # update user info
        # convert body to User
        target_user = cast_json_to_user_update(body)
        # update user info
        is_success: bool = update_user_info_by_id(user.get_id(), target_user.to_json())
        if is_success == True:
            return Response(APIStatus.SUCCESS).to_json()
        else:
            return Response(APIStatus.NOT_MODIFIED).to_json()
    # mongo exception
    except Exception as e:
        # log error
        app.logger.error(e)
        return Response(APIStatus.SERVER_ERROR).to_json()


   


