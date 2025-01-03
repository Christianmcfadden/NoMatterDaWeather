"""
NoMatterDaWeather (Web App)

Contributers:
Christian Mcfadden


Date Started: 12/7/24

File: __init__.py
"""
import dbm
import os
from sqlite3 import dbapi2
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from NMDW import routes
from flask_login import UserMixin

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.debug = True

# use sql to store user info
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

#Encoding integration
bcrypt = Bcrypt(app)


