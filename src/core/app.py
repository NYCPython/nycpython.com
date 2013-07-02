from core import settings
from flask import Flask

app = Flask(
    __name__,
    template_folder=settings.TEMPLATE_FOLDER,
    static_folder=settings.STATIC_FOLDER,
    static_url_path=settings.STATIC_URL_PATH,
)
app.config.from_object(settings)

# Register new blueprints here
from core.urls import blueprint as core_blueprint
app.register_blueprint(core_blueprint, url_prefix='')

from about.urls import blueprint as about_blueprint
app.register_blueprint(about_blueprint, url_prefix='/about')
