
from flask import request, Flask
from app.engine.ldap_service import auth as auth_engine
from app.engine.ldap_service.models.LdapUser import LdapUser
from . import users

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
            return 'Authenticated'
        else:
            return 'Not Authenticated'

    else:
        # if the content type is not json, return an error
        return '{"error": "Content-Type must be application/json"}'
        

