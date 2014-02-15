"""Application settings."""

from os import environ as env


def bool_(key, default):
    """Return an environment setting represented as a boolean."""
    return env.get(key, str(default)).lower() == 'true'


def required(key):
    """Return the value for a required environment setting."""
    try:
        return env[key]
    except KeyError:
        message = 'The {} environment setting is required.'.format(key)
        raise RuntimeError(message)


DEBUG = bool_('DEBUG', False)
SECRET_KEY = required('SECRET_KEY')

# Flask-Assets
ASSESTS_BUDEG = bool_('ASSETS_DEBUG', False)

# Flask-Cache
CACHE_REDIS_URL = env.get('CACHE_REDIS_URL')
CACHE_TYPE = 'redis' if CACHE_REDIS_URL else 'null'

# Meetup API
MEETUP_API_KEY = env.get('MEETUP_API_KEY')
MEETUP_GROUP_ID = env.get('MEETUP_GROUP_ID')

del bool_
del env
del required
