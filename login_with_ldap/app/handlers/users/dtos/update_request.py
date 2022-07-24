

class UserUpdate:
    def __init__(self, name: str, phone_number):
        self.__name = name
        self.__phone_number = phone_number
    @property
    def name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name
        return self
    @property
    def phone_number(self):
        return self.__phone_number
    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number
        return self
    def to_json(self):
        return {
            'name': self.__name,
            'phone_number': self.__phone_number
        }