import os
import sys
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from config import Config

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = Config.SQLALCHEMY_DATABASE_URI
MIGRATION_DIR = os.path.join("event_wave_app", "migrations")

db = SQLAlchemy(app)
migrate = Migrate(app, db, directory=MIGRATION_DIR)

api = Api(app)

# Set the logging level
app.logger.setLevel(logging.DEBUG)

# Create a rotating file handler to save the logs to a file
file_handler = RotatingFileHandler("logs/app.log", maxBytes=10000, backupCount=1)
file_handler.setLevel(logging.DEBUG)

stdstream_handler = logging.StreamHandler(sys.stdout)
stdstream_handler.setLevel(logging.DEBUG)

# Set the log format
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

# Replace handlers of the app's logger
app.logger.handlers.clear()
app.logger.addHandler(file_handler)
app.logger.addHandler(stdstream_handler)
app.logger.setLevel(logging.DEBUG)

# Replace handlers of werkzeug logger
werkzeug_logger = logging.getLogger("werkzeug")
werkzeug_logger.handlers.clear()
werkzeug_logger.addHandler(file_handler)
werkzeug_logger.addHandler(stdstream_handler)
werkzeug_logger.setLevel(logging.DEBUG)

# pylint: disable=wrong-import-position
# import from submodule
from .models import customer, event, order
from .rest import init_api

init_api()
