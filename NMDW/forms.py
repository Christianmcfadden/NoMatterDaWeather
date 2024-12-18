"""
NoMatterDaWeather (Web App)

Contributers:
Christian Mcfadden


Date Started: 12/7/24

File: Forms.py
"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DateField, RadioField, SelectField, TextAreaField, FileField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from NMDW.models import User


class UserInfoForm(FlaskForm):
    username = StringField('Name', validators=[DataRequired()])
    fname = StringField('First Name', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = StringField("password", validators=[DataRequired()])
    conpassword = StringField("Confirm Password", validators=[DataRequired()])
    submit = SubmitField('Next')

    def validate_password(self):
        if self.password == self.conpassword:
            raise ValidationError("")
        #Add more password criteria here