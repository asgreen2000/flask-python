from .models.User import User
from .helper import *
from bson import ObjectId


class BaseEngineBL:
    
    @staticmethod
    def find_user_by_id(id : str) -> User:
        data = User.objects(id=id).first()
        return data
    
    @staticmethod
    def find_user_by_username(username) -> User:
        data = User.objects(username=username).first()
        return data

    @staticmethod
    def insert_user(user: User) -> User:
        user.id = str(ObjectId())
        result = user.save()
        return result

    @staticmethod
    def insert_if_absent(user: User) -> User:
        if not BaseEngineBL.find_user_by_username(user.username):
            return BaseEngineBL.insert_user(user)
        return user

    @staticmethod
    def update_user(id: str, user: dict) -> bool:
        user_data = User.objects(id=id).first()
        if user_data:
            user_data.update(**user)
            user_data.save()
            return True
        return False


