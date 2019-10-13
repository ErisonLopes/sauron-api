import datetime
from models.user import UserModel
from business.imageBusiness import ImageBusiness

class UserBusiness():

    def get_all_users():
        return [user.to_json() for user in UserModel.query.all()]

    def get_user(id_user):
        return UserModel.query.filter(UserModel.id==id_user).first() 

    def find_by_image(image_base_64):
        image = ImageBusiness.find_user(image_base_64)

        if image:
            user = UserBusiness.get_user(image['user_id'])
            user_json = user.to_json()

            return {**user_json, **image}
    
    def save_user(user):
        user['birthdate'] = datetime.datetime.strptime(user['birthdate'], '%d/%m/%Y')
        user_model = UserModel(**user)
        user_model.dt_create = datetime.datetime.now()
        user_model.dt_update = datetime.datetime.now()
        user_model.active = True
        user_model.Create()
        return user_model