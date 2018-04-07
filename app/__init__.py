from flask import Flask
from .views import reminders
from .extensions import db
from .models import Reminder, User


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
    db.init_app(app)


def register_shell(app):
    def shell_context():
        return {
            'db': db,
            'Reminder': Reminder,
            'User': User,
        }

    app.shell_context_processor(shell_context)
