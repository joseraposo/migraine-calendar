from flask import Flask
from flask_sqlalchemy import SQLAlchemy

DATABASE_LOCATION = 'sqlite:///../databases/migraines.db'

app = Flask(__name__)
app.config["DEBUG"] = True
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_LOCATION
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from migraine_calendar import migraine_routes
from migraine_calendar import main_routes
from migraine_calendar import error_routes
