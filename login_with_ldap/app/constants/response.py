import enum
from dataclasses import dataclass
from http.client import NOT_MODIFIED


class _Status:
    
    def __init__(self, code : int, message : str):
        self.__code = code
        self.__message = message

    def get_code(self):
        return self.__code
    def get_message(self):
        return self.__message


class APIStatus:
    SUCCESS = _Status(0, 'success')
    FAIL = _Status(-100, 'fail')
    NOT_FOUND = _Status(-102, 'not found')
    NOT_ALLOWED = _Status(-103, 'not allowed')
    NOT_ACCEPTABLE = _Status(-104, 'not acceptable')
    CONFLICT = _Status(-105, 'conflict')
    UNPROCESSABLE_ENTITY = _Status(-106, 'unprocessable entity')
    UNAUTHORIZED = _Status(-107, 'unauthorized')
    FORBIDDEN = _Status(-108, 'forbidden')
    BAD_REQUEST = _Status(-109, 'bad request')
    INSUFFICIENT_DATA = _Status(-110, 'insufficient data')
    INVALID_DATA = _Status(-111, 'invalid data')
    INVALID_CREDENTIALS = _Status(-112, 'invalid credentials')
    INVALID_TOKEN = _Status(-113, 'invalid token')
    EX_PIRED_TOKEN = _Status(-114, 'expired token'),
    NOT_MODIFIED = _Status(-115, 'not modified')
    SERVER_ERROR = _Status(-200, 'server error')
    NOT_IMPLEMENTED = _Status(-201, 'not implemented')
    SERVICE_UNAVAILABLE = _Status(-202, 'service unavailable')


class Response:
    def __init__(self, status : _Status):
        self.__status = status
       

    def get_status(self):
        return self.__status
  
    def to_json(self):
        return {
            'code': self.__status.get_code(),
            'message': self.__status.get_message()
        }


class ResponseObject:
    def __init__(self, status : _Status, data : dict):
        self.__status = status
        self.__data = data

    def get_status(self):
        return self.__status
    def get_data(self):
        return self.__data
    def to_json(self):
        return {
            'code': self.__status.get_code(),
            'message': self.__status.get_message(),
            'data': self.__data
        }

class ResponseListObject:
    def __init__(self, status : _Status, data : list):
        self.__status = status
        self.__data = data
        self.total = len(data)

    def get_status(self):
        return self.__status
    def get_data(self):
        return self.__data
    def to_json(self):
        return {
            'code': self.__status.get_code(),
            'message': self.__status.get_message(),
            'data': self.__data,
            'total': self.total
        }

    