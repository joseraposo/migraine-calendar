from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

DATABASE_LOCATION = 'sqlite:///../databases/migraines.db'

app = Flask(__name__)
app.config["DEBUG"] = True
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_LOCATION
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

from migraine_calendar import main_routes
from migraine_calendar import migraine_routes
from migraine_calendar import sleep_routes
from migraine_calendar import error_routes
