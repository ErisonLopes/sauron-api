from models.user import UserModel

class UserBusiness():

    def get_all_users():
        return UserModel.query.all()