from re import U
from .models.User import User

def castJsonUser(jsonUser: str) -> User:
    return User(jsonUser['username'], jsonUser['name'], jsonUser['role']) \
    .set_id(jsonUser['_id'])