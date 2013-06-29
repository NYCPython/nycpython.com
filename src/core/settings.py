import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))

DEBUG = False

SQLALCHEMY_DATABASE_URI = 'postgresql://nycpython:nycpython@localhost:5432/subwars'
TEMPLATE_FOLDER = os.path.join(PROJECT_ROOT, 'templates')
STATIC_FOLDER = os.path.join(PROJECT_ROOT, 'static')
STATIC_URL_PATH = '/static'
BCRYPT_ROUNDS = 12 # the default at the time of this writing

try:
    from core.dev_settings import *
except ImportError:
    pass
