
from flask import request, Flask
from app.engine.ldap_service import auth as auth_engine
from app.engine.ldap_service.models.LdapUser import LdapUser
from . import users
from app.engine.user import User, BaseEngineBL as ENGINE_USER
from app.engine.jwt import *
from app.constants import APIStatus, Response, ResponseObject
from .dtos import *

# create a flask routes for the login page
@users.route('/', methods=['POST'])
def login():
    # set content type to json
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        # get the username and password from the request
        username = request.json.get('username')
        password = request.json.get('password')
        
        is_authenticated:bool = auth_engine.ldap_login(LdapUser(username, password))
        if is_authenticated:
            user : User = ENGINE_USER.find_user_by_username(username)
            if user is None:
                user = User(username=username, name=username, role=User.Role.USER, phone_number=None, email=None, address=None)
                user = ENGINE_USER.insert_user(user)

            jwt_user: JwtResult = generate_token(user)
            jwt_user_refresh: JwtResult = generate_token(user, True)

            response_data = AuthReponse(user.get_id(), username, jwt_user.get_token(), jwt_user.get_expired_at(), jwt_user_refresh.get_token())
            return ResponseObject(APIStatus.SUCCESS, response_data.to_json()).to_json()
        else:
            return Response(APIStatus.INVALID_CREDENTIALS).to_json()

    else:
        # if the content type is not json, return an error
        return Response(APIStatus.BAD_REQUEST).to_json()




    
        

