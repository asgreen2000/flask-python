from app.engine.user.models import User
from app.handlers.users.dtos import *

# cast User to UserDto
def cast_user_to_user_dto(user: User, is_detail: bool):
    if is_detail:
        return DetailUserDto(user.get_id(), user.get_username(), user.get_name(), user.get_phone_number(), user.get_role())
    else:
        return UserDto(user.get_id(), user.get_username(), user.get_name())

# cast UserDto to User
def cast_user_dto_to_user(user_dto: UserDto):
    return User(user_dto.get_id(), user_dto.get_username(), user_dto.get_name(), user_dto.get_phone_number(), user_dto.get_role())

# cast json to user dto
def cast_json_to_user_dto(json: dict):
    return UserDto(json['id'], json['username'], json['name'], json['phone_number'], json['role'])

# cast json to User
def cast_json_to_user(json: dict):
    return User(json['username'], json['name'], json['phone_number'], json['role'])

# cast json to UserUpdate
def cast_json_to_user_update(json: dict):
    return UserUpdate(json['name'], json['phone_number'])