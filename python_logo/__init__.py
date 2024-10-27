from flask import Flask

from .routes import main


def logo() -> str:
    """Returns logo string"""
    return "logo"


def create_app():
    """Create and configure the Flask application.

    :return: Flask application instance.
    """
    app = Flask(__name__)
    app.register_blueprint(main)

    return app
