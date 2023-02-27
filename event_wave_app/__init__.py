import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
MIGRATION_DIR = os.path.join('event_wave_app', 'migrations')

db = SQLAlchemy(app)
migrate = Migrate(app, db, directory=MIGRATION_DIR)

#pylint: disable=wrong-import-position
#import from submodule
from .models import customer, event, order
