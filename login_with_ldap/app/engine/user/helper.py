import json
from re import U
from .models.User import User

class EngineHelper:
    @staticmethod
    def castJsonUser(jsonUser: str) -> User:
        # convert json user to User object
        return User(**json.loads(jsonUser))
        
   