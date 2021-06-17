from models.user import UserModel
from werkzeug.security import safe_str_cmp


def authenticate(username, password):
    user = UserModel.find_by_username(username)
    # print(user.password)
    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload1):
    user_id = payload1['identity']
    return UserModel.find_by_id(user_id)

# authenticate('bob', 'abcd')    