from flask_restful import Resource, reqparse
from business.userBusiness import UserBusiness

class UserController(Resource):

    def get(self):
        users = UserBusiness.get_all_users()

        if users:
            return users, 200
        return {'message': 'Não foi encontrado nenhum usuário'}, 404
    
    def post(self):
        parameters = reqparse.RequestParser()
        parameters.add_argument('name', type=str, required=True, help="O campo 'nome' não pode ser deixado em branco")
        parameters.add_argument('email', type=str, required=True, help="O campo 'email' não pode ser deixado em branco")
        parameters.add_argument('password', type=str, required=True, help="O campo 'senha' não pode ser deixado em branco")
        parameters.add_argument('rg', type=str, required=True, help="O campo 'Rg' não pode ser deixado em branco")
        parameters.add_argument('cpf', type=str, required=True, help="O campo 'CPF' não pode ser deixado em branco")
        parameters.add_argument('birthdate', type=str, required=True, help="O campo 'Data de nascimento' não pode ser deixado em branco")

        data = parameters.parse_args()

        user = UserBusiness.save_user(data)

        if user:
            return {'message': 'Usuário criado com sucesso'}, 201
        return {'message': 'Não foi possível criar o usuário'}, 400


