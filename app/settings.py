import os


class Config:
    SECRET_KEY = os.environ.get('REMINDERS_SECRET')


class ProdConfig(Config):
    ENV = 'prod'
    DEBUG = False


class DevConfig(Config):
    ENV = 'dev'
    DEBUG = True
