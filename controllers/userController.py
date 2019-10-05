from flask_restful import Resource, reqparse
from business.userBusiness import UserBusiness

class UserController(Resource):

    def get(self):
        users = UserBusiness.get_all_users()

        if users:
            return users, 200
        return {'message': 'Não foi encontrado nenhum usuário'}, 404