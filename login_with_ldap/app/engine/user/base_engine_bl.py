from pydoc import Helper
from .models.User import User, UserUtil, collection as users_collection
from .helper import *
from bson import ObjectId

def find_user_by_id(id : str) -> User:
    data = users_collection.find_one({'_id': ObjectId(id)})
    return UserUtil.cast(data) if data else None

def find_user_by_username(username) -> User:
    data = users_collection.find_one({'username': username})
    return UserUtil.cast(data) if data else None

def insert_user(user: User) -> User:
    result = users_collection.insert_one(user.to_json())
    user.set_id(str(result.inserted_id))
    return user

def insert_if_absent(user: User) -> User:
    current_user = find_user_by_username(user.username)
    if current_user is None:
        return insert_user(user)
    else:
        return current_user
