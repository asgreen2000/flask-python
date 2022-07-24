from dataclasses import dataclass
import datetime

@dataclass
class JwtResult:
    __token: str
    __expired_at: datetime

    def get_token(self):
        return self.__token
    def get_expired_at(self):
        return self.__expired_at

    def to_json(self):
        return {
            'token': self.__token,
            'expired_at': self.__expired_at
        }