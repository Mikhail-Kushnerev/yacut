from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from settings import Config, configure_logging


app: Flask = Flask(__name__)
app.config.from_object(Config)

db: SQLAlchemy = SQLAlchemy(app)
migrate: Migrate = Migrate(app, db)

configure_logging()

from . import api_views, constants, error_handlers, exceptions, views
