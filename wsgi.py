"""WSGI application."""

from werkzeug._internal import _easteregg
from werkzeug.serving import run_simple
from werkzeug.wsgi import DispatcherMiddleware

from nycpython import frontend

application = DispatcherMiddleware(_easteregg(frontend.create_app()))

if __name__ == '__main__':
    run_simple(
        '0.0.0.0', 5000, application, use_reloader=True, use_debugger=True)
