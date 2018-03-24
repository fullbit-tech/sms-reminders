import os


class Config:
    SECRET_KEY = os.environ.get('REMINDERS_SECRET')
    SQLALCHEMY_DATABASE_URI = os.environ.get('REMINDERS_DB')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(Config):
    ENV = 'prod'
    DEBUG = False


class DevConfig(Config):
    ENV = 'dev'
    DEBUG = True
