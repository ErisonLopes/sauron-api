from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from sql_alchemy import db
from controllers.userController import UserController, UserImageController
from controllers.imageController import ImageController
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'sauronDb.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)

@app.before_first_request
def create_database():
    db.create_all()

api.add_resource(UserController, '/user')
api.add_resource(UserImageController, '/userImage')
api.add_resource(ImageController, '/image')
api.add_resource(ImageController, '/image/<int:id_image>', endpoint='get_by_id')

if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)