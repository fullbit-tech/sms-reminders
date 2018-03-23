from flask import Flask
from .views import reminders


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    register_blueprints(app)
    register_extensions(app)
    register_shell(app)

    return app


def register_blueprints(app):
    app.register_blueprint(reminders)


def register_extensions(app):
    return


def register_shell(app):
    return
