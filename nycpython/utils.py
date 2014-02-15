"""Application helper utilities."""

import importlib
import pkgutil

from flask import Blueprint

__all__ = 'register_blueprints',


def register_blueprints(app, package_name, package_path):
    """Register all :class:`~flask.Blueprint` instances on the app."""
    for _, name, _ in pkgutil.iter_modules(package_path):
        m = importlib.import_module('{}.{}'.format(package_name, name))
        for x in dir(m):
            item = getattr(m, x)
            if isinstance(item, Blueprint):
                app.register_blueprint(item)
