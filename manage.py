"""Management commands."""

from flask.ext.script import Manager

from nycpython.factory import create_app

manager = Manager(create_app(__name__, ''))

if __name__ == '__main__':
    manager.run()
