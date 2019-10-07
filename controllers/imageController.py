from flask_restful import Resource, reqparse
from business.imageBusiness import ImageBusiness

class ImageController(Resource):

    def get(self):
        images = ImageBusiness.get_all_images()

        if images:
            return images, 200
        return {'message': 'Não foi encontrado nenhuma imagem'}, 404
    
    def get_by_id(self, id_image):
        image = ImageBusiness.get_image(id_image)

        if image:
            return image.to_json(), 200
        return {'message': 'Não foi encontrado nenhuma imagem com o id expecificado'}, 400
    
    def post(self):
        parameters = reqparse.RequestParser()
        parameters.add_argument('imageBase64', type=str, required=True, help="O campo 'Imagem' não pode ser deixado em branco")
        parameters.add_argument('user_id', type=str, required=True, help="O campo 'user_id' não pode ser deixado em branco")

        data = parameters.parse_args()

        image = ImageBusiness.save_image(data)

        if image:
            return {'message': 'Imagem criada com sucesso'}, 201
        return {'message': 'Não foi possível criar a imagem'}, 400
    
    def delete(self):
        parameters = reqparse.RequestParser()
        parameters.add_argument('id', type=int, required=True, help="O campo 'id' não pode ser deixado em branco")
        
        data = parameters.parse_args()

        image = ImageBusiness.get_image(data['id'])

        if image:
            ImageBusiness.delete_image(image)
            return {'message': 'Imagem deletada com sucesso'}, 200
        return {'Não foi encontrado nenhuma imagem com o id expecificado'}


