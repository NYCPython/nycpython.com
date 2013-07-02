import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))

DEBUG = False

SECRET_KEY = b'\x7f\xebt.Y\xea\xd5\x19"\x1ftu5\x9d\xaa.FD\xac5\xbc\x86\xe7c=\xc5_\xfe\xf5\x96\x1eH'  # NOQA

SQLALCHEMY_DATABASE_URI = \
    'postgresql://nycpython:nycpython@localhost:5432/nycpython'
TEMPLATE_FOLDER = os.path.join(PROJECT_ROOT, 'templates')
STATIC_FOLDER = os.path.join(PROJECT_ROOT, 'static')
STATIC_URL_PATH = '/static'
BCRYPT_ROUNDS = 12  # the default at the time of this writing

try:
    from core.dev_settings import *  # NOQA
except ImportError:
    pass
