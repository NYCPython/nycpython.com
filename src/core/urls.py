from flask import Blueprint
from flask.ext.lazyviews import LazyViews

blueprint = Blueprint('core', __name__)
views = LazyViews(blueprint, 'core.views')

#views.add('/', 'index')
views.add('/', 'example')
