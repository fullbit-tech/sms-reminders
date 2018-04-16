import os
from app import create_app
from app.settings import DevConfig, ProdConfig
from app.extensions import celery


app = create_app(
    ProdConfig if os.environ.get('FLASK_ENV') == 'prod' else DevConfig
)
