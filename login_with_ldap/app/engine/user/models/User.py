from tokenize import String
from flask_mongoengine import MongoEngine
from app import db_connector
from dataclasses import dataclass
import json

collection = db_connector["users"]
@dataclass
class User:
    
    def __init__(self, username: str, name: str = "Not set", phone_number: str = "000000",role='guest'):
        self.__username = username
        self.__name = name
        self.__role = role
        self.__phone_number = phone_number
    def to_json(self):
        return {
            'username': self.__username,
            'name': self.__name,
            'role': self.__role,
            'phone_number': self.__phone_number
        }

    def set_id(self, id):
        self.__id = id
        return self

    def toJSON(self):
        return {
            '_id': self.__id,
            'username': self.__username,
            'name': self.__name,
            'role': self.__role,
            'phone_number': self.__phone_number
        }

    def get_username(self):
        return self.__username
    def get_name(self):
        return self.__name
    def get_role(self):
        return self.__role
    def get_phone_number(self):
        return self.__phone_number
    def set_username(self, username):
        self.__username = username
        return self
    def set_name(self, name):
        self.__name = name
        return self
    def set_role(self, role):
        self.__role = role
        return self
    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number
        return self

    def get_id(self) -> str:
        return self.__id
    

   

class UserUtil:

    @staticmethod
    def cast(json: str) -> User:
        print("json" , json)
        username = json['username']
        name = json['name']
        phone_number = json['phone_number']
        role = json['role']
        user_id = str(json['_id'])
        return User(username, name, phone_number, role).set_id(user_id)
       

