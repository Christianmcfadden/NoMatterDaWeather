"""
NoMatterDaWeather (Web App)

Contributers:
Christian Mcfadden


Date Started: 12/7/24

File: Models.py
"""
from datetime import datetime
from NMDW import db
from NMDW import login_manager
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(50), nullable=True)  
    lname = db.Column(db.String(50), nullable=True) 
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    @login_manager.user_loadergit #rm --cached NoMatterDaWeather

    def load_user(user_id):
        return User.query.get(int(user_id))

    def to_dict(self):
        return {
            'id': self.id,
            'fname': self.fname,
            'lname': self.lname,
            'username': self.username,
            'email': self.email
        }

    def __repr__(self):
        return (f"User(id={self.id!r}, username={self.username!r}, email={self.email!r}, password={self.password!r}, ")