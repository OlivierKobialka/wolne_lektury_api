from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config
import logging

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    with app.app_context():
        from .routes import init_routes
        init_routes(app)
        db.create_all()

    logging.basicConfig(level=app.config['LOG_LEVEL'])
    app.logger.setLevel(app.config['LOG_LEVEL'])

    return app
