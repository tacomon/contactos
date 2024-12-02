import os
from os import path

BASE_DIR = path.abspath(path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'tu_clave_secreta_aqui')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'mysql+pymysql://root:1234@localhost:3306/contactos_crud')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# from os import path

# BASE_DIR = path.abspath(path.dirname(__file__))

# class Config:
#     SECRET_KEY = 'tu_clave_secreta_aqui'
#     SQLALCHEMY_DATABASE_URI = 'sqlite:///' + path.join(BASE_DIR, 'contacts.db')
#     SQLALCHEMY_TRACK_MODIFICATIONS = False