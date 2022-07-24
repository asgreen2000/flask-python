from app.engine.user.models import User
from app.handlers.users.dtos.info_response import *

# cast User to UserDto
def cast_user_to_user_dto(user: User, is_detail: bool):
    print(user)
    if is_detail:
        return DetailUserDto(user.get_id(), user.get_username(), user.get_name(), user.get_phone_number(), user.get_role())
    else:
        return UserDto(user.get_id(), user.get_username(), user.get_name())