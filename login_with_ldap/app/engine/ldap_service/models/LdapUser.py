
class LdapUser:
    def __init__(self, username: str, password: str) -> None:
        self.__username = username
        self.__password = password

    # create a method to authenticate the user
    def authenticate(self) -> bool:
        return True

    # create a method to get the user's username
    def get_username(self) -> str:
        return self.__username

    # create a method to get the user's password
    def get_password(self) -> str:
        return self.__password