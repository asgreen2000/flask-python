from email.policy import default
from enum import Enum
from tokenize import String
from unicodedata import name
from flask_mongoengine import MongoEngine
from dataclasses import dataclass
from mongoengine import *

class Role(Enum):
    ADMIN = 1
    USER = 2

class User(Document):
    id = IntField(primary_key=True)
    name = StringField(required=True)
    username = StringField(required=True, unique=True)
    role = StringField(required=True, default=Role.USER)
    phone_number = StringField(required=False)
    email = StringField(required=False, unique=True)
    address = StringField(required=False)
    meta = { 'collection': 'users' }

    # create a field that equals to the id of the user
    def get_id(self):
        return self.id
    def get_name(self):
        return self.name
    def get_username(self):
        return self.username
    def get_role(self):
        return self.role
    def get_phone_number(self):
        return self.phone_number
    def get_email(self):
        return self.email
    def get_address(self):
        return self.address
    def set_name(self, name):
        self.name = name
        return self
    def set_username(self, username):
        self.username = username
        return self
    def set_role(self, role):
        self.role = role
        return self
    def set_phone_number(self, phone_number):
        self.phone_number = phone_number
        return self
    def set_email(self, email):
        self.email = email
        return self
    def set_address(self, address):
        self.address = address
        return self
    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'username': self.username,
            'role': self.role,
            'phone_number': self.phone_number,
            'email': self.email,
            'address': self.address
        }
    def __str__(self):
        return str(self.to_json())
    def __repr__(self):
        return str(self.to_json())
    def __eq__(self, other):
        return self.id == other.id



    

class UserUtil:

    @staticmethod
    def cast(json: str) -> User:
        username = json['username']
        name = json['name']
        phone_number = json['phone_number']
        role = json['role']
        user_id = str(json['_id'])
        return User(username, name, phone_number, role).set_id(user_id)
       

