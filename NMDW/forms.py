"""
NoMatterDaWeather (Web App)

Contributers:
Christian Mcfadden


Date Started: 12/7/24

File: Forms.py
"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Regexp, ValidationError
from NMDW.models import User


class UserInfoForm(FlaskForm):
    username = StringField('Name', validators=[DataRequired()])
    fname = StringField('First Name', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])

    password = StringField("password", validators=[DataRequired(),Regexp(
                r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$',
                message="Password must contain at least one uppercase letter, one lowercase letter, one number, and one special character, and must be at least 8 characters long."
            )])
    
    conpassword = StringField("Confirm Password", validators=[DataRequired()])
    submit = SubmitField('Next')

    def validate_password(self):
        if self.password.data != self.conpassword.data:
            raise ValidationError("Passwords must match.")