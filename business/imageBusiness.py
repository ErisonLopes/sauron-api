import datetime
from models.image import ImageModel

class ImageBusiness():

    def get_all_images():
        return [image.to_json() for image in ImageModel.query.filter(ImageModel.active==True)] 
    
    def get_image(id_image):
        return ImageModel.query.filter(ImageModel.active==True, ImageModel.id==id_image).first() 
    
    def save_image(image):
        image_model = ImageModel(**image)
        image_model.dt_create = datetime.datetime.now()
        image_model.active = True
        image_model.Create()
        return image_model

    def delete_image(image):
        image.Delete()
    
