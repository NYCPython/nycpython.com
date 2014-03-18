"""Frontend application."""

from functools import wraps
import os

from flask import render_template
from werkzeug._internal import _easteregg

from nycpython import factory

__all__ = 'create_app', 'route'


def create_app(settings_override=None):
    """Return the NYC Python frontend application.

    :param settings_override: a ``dict`` of settings to override.

    """
    app = factory.create_app(__name__, __path__, settings_override)

    if not app.debug:
        for e in (404, 500):
            app.errorhandler(e)(handle_error)

    return _easteregg(app)


def handle_error(error):
    """Return the rendered error template."""
    return render_template('errors/{}.html'.format(error.code)), error.code


def route(blueprint, *args, **kwargs):
    """Return a route."""
    def decorator(f):
        @blueprint.route(*args, **kwargs)
        @wraps(f)
        def wrapper(*args, **kwargs):
            return f(*args, **kwargs)
        return f
    return decorator
