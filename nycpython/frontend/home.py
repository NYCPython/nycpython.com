"""The NYC Python home page."""

from flask import Blueprint, current_app, render_template

from nycpython.meetup import APIWrapper

__all__ = 'blueprint',

blueprint = Blueprint(
    'home',
    __name__,
    static_folder='static',
    static_url_path='/frontend/static',
)


@blueprint.route('/')
def index():
    """Return the home page."""
    group_id = current_app.config.get('MEETUP_GROUP_ID')
    api_key = current_app.config.get('MEETUP_API_KEY')
    api = APIWrapper(api_key)
    events = api.events(group_id)
    photos = api.photos(group_id, 5)

    return render_template('home/index.html', events=events, photos=photos)
