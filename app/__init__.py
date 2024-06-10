from flask import Flask

from app.modules.icon import icons

def create_app() -> object:
    """
    Create Flask App
    """
    app = Flask(__name__)
    origins = "*"
    app.register_blueprint(icons, url_prefix='/icon')
    return app