import os
from app import create_app
from app.settings import DevConfig, ProdConfig


app = create_app(
    ProdConfig if os.environ.get('FLASK_ENV') == 'prod' else DevConfig
)
