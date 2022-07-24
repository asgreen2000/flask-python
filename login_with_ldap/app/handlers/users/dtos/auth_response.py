from dataclasses import dataclass
import datetime

class AuthReponse:
    token: str
    expired_at: datetime
    refresh_token: str

    def __init__(self, token: str, expired_at: datetime, refresh_token: str):
        self.token = token
        self.expired_at = expired_at
        self.refresh_token = refresh_token

    def to_json(self):
        return {
            'token': self.token,
            'expired_at': self.expired_at,
            'refresh_token': self.refresh_token,
        }
