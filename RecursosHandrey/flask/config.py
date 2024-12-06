from flask import Flask
from flask_jwt_extended import JWTManager
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'supersecretkey'
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(BASE_DIR, "empresa.db")}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CLOUDINARY_URL = os.getenv('CLOUDINARY_URL', 'cloudinary://API_KEY:API_SECRET@CLOUD_NAME')


from flask import Flask
from flask_jwt_extended import JWTManager

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'mi_clave_secreta'  
jwt = JWTManager(app)


