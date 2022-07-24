import json
from re import U
from .models.User import User

def castJsonUser(jsonUser: str) -> User:
    username = jsonUser['username']
    name = jsonUser['name']
    phone_number = jsonUser['phone_number']
    role = jsonUser['role']
    user_id = str(jsonUser['_id'])
    return User(username, name, phone_number, role).set_id(user_id)
    
   