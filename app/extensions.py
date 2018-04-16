from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_celery import Celery


db = SQLAlchemy()
login_manager = LoginManager()
celery = Celery()
