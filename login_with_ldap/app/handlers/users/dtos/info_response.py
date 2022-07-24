

class UserDto:
    def __init__(self, user_id, username, name):
        self.__user_id = user_id
        self.__username = username
        self.__name = name
    
    def to_json(self):
        return {
            'user_id': self.__user_id,
            'username': self.__username,
            'name': self.__name
        }

    def get_phone_number(self):
        return self.__phone_number
    def get_username(self):
        return self.__username
    def get_name(self):
        return self.__name
    def get_user_id(self):
        return self.__user_id
    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number
        return self
    def set_username(self, username):
        self.__username = username
        return self
    def set_name(self, name):
        self.__name = name
        return self
    def set_user_id(self, user_id):
        self.__user_id = user_id
        return self


class DetailUserDto(UserDto):
    def __init__(self, user_id, username, name, phone_number, role):
        super().__init__(user_id,username, name)
        self.__phone_number = phone_number
        self.__role = role

    def to_json(self):
        return {
            'user_id': self.get_user_id(),
            'username': self.get_username(),
            'name': self.get_name(),
            'phone_number': self.__phone_number,
            'role': self.__role
        }
