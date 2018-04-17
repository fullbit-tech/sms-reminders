import os


class Config:
    SECRET_KEY = os.environ.get('REMINDERS_SECRET')
    SQLALCHEMY_DATABASE_URI = os.environ.get('REMINDERS_DB')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CELERY_RESULT_BACKEND = 'redis://localhost:6379'
    CELERY_BROKER_URL = 'redis://localhost:6379'
    TWILIO_AUTH_ID = os.environ.get('TWILIO_AUTH_ID')
    TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
    TWILIO_TO_NUMBER = os.environ.get('TWILIO_TO_NUMBER')
    TWILIO_FROM_NUMBER = os.environ.get('TWILIO_FROM_NUMBER')


class ProdConfig(Config):
    ENV = 'prod'
    DEBUG = False


class DevConfig(Config):
    ENV = 'dev'
    DEBUG = True
