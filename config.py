from os import environ, path

BASE_DIR = path.abspath(path.dirname(__file__))



# config class
class Config(object):
    """set Flask configuration variables from .env file."""

    # general
    DEBUG = environ.get('DEBUG')
    SECRET_KEY = environ.get('SECRET_KEY')

    # sqlalchemy
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:qfalinc5@192.168.10.234:5432/reduxcartdb" # if you do not create an environment file then it will create a sqlite database
    SQLALCHEMY_TRACK_MODIFICATIONS = False