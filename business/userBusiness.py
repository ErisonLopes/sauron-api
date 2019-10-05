import datetime
from models.user import UserModel


class UserBusiness():

    def get_all_users():
        return [user.to_json() for user in UserModel.query.all()] 
    
    def save_user(user):
        user['birthdate'] = datetime.datetime.strptime(user['birthdate'], '%d/%m/%Y')
        user_model = UserModel(**user)
        user_model.dt_create = datetime.datetime.now()
        user_model.dt_update = datetime.datetime.now()
        user_model.active = 0
        print(user_model)
        user_model.Create()
        return user_model