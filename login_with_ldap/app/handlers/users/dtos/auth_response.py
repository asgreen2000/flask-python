from dataclasses import dataclass
import datetime

class AuthReponse:
    token: str
    expired_at: datetime
    refresh_token: str

    def __init__(self, user_id: str, username: str, token: str, expired_at: datetime, refresh_token: str):
        self.__user_id = user_id
        self.__username = username
        self.__token = token
        self.__expried_at = expired_at
        self.__refresh_token = refresh_token

    def to_json(self):
        return {
            'user_id': self.__user_id,
            'username': self.__username,
            'token': self.__token,
            'expired_at': self.__expried_at,
            'refresh_token': self.__refresh_token
        }
