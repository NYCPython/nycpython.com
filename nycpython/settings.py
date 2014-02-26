"""Application settings."""

from os import environ as env

from nycpython.utils import DOES_NOT_EXIST


def bool_(key, default):
    """Return an environment setting represented as a boolean."""
    return env.get(key, str(default)).lower() == 'true'


DEBUG = bool_('DEBUG', False)
SECRET_KEY = env.get('SECRET_KEY', DOES_NOT_EXIST)

# Flask-Assets
ASSESTS_DEBUG = bool_('ASSETS_DEBUG', False)

# Flask-Cache
CACHE_REDIS_URL = env.get('CACHE_REDIS_URL')
CACHE_TYPE = 'redis' if CACHE_REDIS_URL else 'null'

# Meetup API
MEETUP_API_KEY = env.get('MEETUP_API_KEY')
MEETUP_GROUP_ID = env.get('MEETUP_GROUP_ID')

del bool_
del env
del DOES_NOT_EXIST
