import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path=dotenv_path)
BASEDIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret_key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(BASEDIR, 'minimart.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get(
        'SQLALCHEMY_TRACK_MODIFICATIONS') or True
    ITEMS_PER_PAGE = os.environ.get('ITEMS_PER_PAGE') or 9
    MAX_CONTENT_LENGTH = os.environ.get('MAX_CONTENT_LENGTH') or 5120 * 5120
    UPLOAD_EXTENSIONS = os.environ.get('UPLOAD_EXTENSIONS') or ['.jpg', '.png', '.jpeg']
    IMAGE_UPLOADS = os.environ.get('IMAGE_UPLOADS') or '/home/bit/Documents/Spaces/PySpace/FlaskProjects/revival/minimart-project/minimart/public/images'
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.gmail.com'
    MAIL_PORT = os.environ.get('MAIL_PORT') or 465
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'biteatertest@gmail.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'b1t3at3r'
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') or True
    MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL') or False


class TestingConfig(Config):
    FLASK_DEBUG = os.environ.get('FLASK_DEBUG') or True
    FLASK_ENV = os.environ.get('FLASK_ENV') or 'development'
    TESTING = os.environ.get('TESTING') or True
    PRESERVE_CONTEXT_ON_EXCEPTION = os.environ.get('PRESERVE_CONTEXT_ON_EXCEPTION') or False


class DevelopmentConfig(Config):
    FLASK_DEBUG = os.environ.get('FLASK_DEBUG') or True
    FLASK_ENV = os.environ.get('FLASK_ENV') or 'development'
    TESTING = os.environ.get('TESTING') or False


class ProductionConfig(Config):
    FLASK_DEBUG = os.environ.get('FLASK_DEBUG') or False
    TESTING = os.environ.get('TESTING') or False