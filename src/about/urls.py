from flask import Blueprint
from flask.ext.lazyviews import LazyViews

blueprint = Blueprint('about', __name__)
views = LazyViews(blueprint, 'about.views')

views.add('/', 'index')
