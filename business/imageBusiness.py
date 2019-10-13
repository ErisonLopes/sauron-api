import datetime
import face_recognition
import openface
import dlib
import base64
import cv2
import numpy as np
from PIL import Image
from io import BytesIO
from models.image import ImageModel

class ImageBusiness():

    def get_all_images():
        return [image.to_json() for image in ImageModel.query.filter(ImageModel.active==True)] 
    
    def get_image(id_image):
        return ImageModel.query.filter(ImageModel.active==True, ImageModel.id==id_image).first() 
    
    def find_user(image_base_64):
        predictor_model = "predictor/shape_predictor_68_face_landmarks.dat"

        face_detector = dlib.get_frontal_face_detector()
        face_pose_predictor = dlib.shape_predictor(predictor_model)
        face_aligner = openface.AlignDlib(predictor_model)

        images = ImageBusiness.get_all_images()

        for image in images:
            encoding_image_db = [ImageBusiness.get_image_encoding(image['imageBase64'])]

            image_to_find = ImageBusiness.image_to_array(image_base_64)

            detected_faces = face_detector(image_to_find, 1)

            for i, face_rect in enumerate(detected_faces):
                pose_landmarks = face_pose_predictor(image_to_find ,face_rect)
                alignedFace = face_aligner.align(534, image_to_find, face_rect, landmarkIndices=openface.AlignDlib.OUTER_EYES_AND_NOSE)
                face_encodings = face_recognition.face_encodings(alignedFace)
                
                for face_encoding in face_encodings:
                    matches = face_recognition.compare_faces(encoding_image_db, face_encoding)

                    if True in matches:
                        return image
    
    def save_image(image):
        image_model = ImageModel(**image)
        image_model.dt_create = datetime.datetime.now()
        image_model.active = True
        image_model.Create()
        return image_model

    def delete_image(image):
        image.Delete()
    
    def image_to_array(image_base_64):
        byteIo = BytesIO()
        byteIo.write(base64.b64decode(image_base_64))

        p_img = Image.open(byteIo)
        return cv2.cvtColor(np.array(p_img),cv2.COLOR_RGB2BGR)
    
    def get_image_encoding(image_base_64):
        image_array = ImageBusiness.image_to_array(image_base_64)
        return face_recognition.face_encodings(image_array)[0]