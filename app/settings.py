import os


class Config:
    SECRET_KEY = os.environ.get('REMINDERS_SECRET')
    SQLALCHEMY_DATABASE_URI = os.environ.get('REMINDERS_DB')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CELERY_RESULT_BACKEND = 'redis://localhost:6379'
    CELERY_BROKER_URL = 'redis://localhost:6379'


class ProdConfig(Config):
    ENV = 'prod'
    DEBUG = False


class DevConfig(Config):
    ENV = 'dev'
    DEBUG = True
