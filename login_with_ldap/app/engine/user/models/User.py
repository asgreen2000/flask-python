from tokenize import String
from flask_mongoengine import MongoEngine
from app import db_connector
from dataclasses import dataclass
import json

collection = db_connector["users"]
@dataclass
class User:
    
    def __init__(self, username, name = "Not set", role='guest'):
        self.__username = username
        self.__name = name
        self.__role = role
    def to_json(self):
        return {
            'username': self.__username,
            'name': self.__name,
            'role': self.__role
        }

    def set_id(self, id):
        self.id = id
        return self

    def toJSON(self):
        return {
            'username': self.__username,
            'name': self.__name,
            'role': self.__role
        }

