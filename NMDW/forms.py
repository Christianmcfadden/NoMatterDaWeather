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
from flask_login import LoginManager
from NMDW.models import User



class UserInfoForm(FlaskForm):
    username = StringField('Name', validators=[DataRequired()])
    fname = StringField('First Name', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    # add zip

    # use Passwordfield for more security
    password = PasswordField("password", validators=[DataRequired(),Regexp(
                r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$',
                message="Password must contain at least one uppercase letter, one lowercase letter, one number, and one special character, and must be at least 8 characters long."
            )])
    
    conpassword = PasswordField("Confirm Password", validators=[DataRequired()])
    submit = SubmitField('Next')

    def validate_conpassword(self, conpassword):
        if self.password.data != conpassword.data:
            raise ValidationError("Passwords must match.")
    
    def validate_username(self, username):
        user = User.query.filter_by(username = username.data).first()
        if user:
            raise ValidationError("This username is already taken.")

class UpdatedProfileForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired()])
    fname = StringField('First Name', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    zip_code = StringField('Zip Code', validators = [Regexp(r'^\d{5}(-\d{4})?$', message="Enter a valid ZIP code.")])
    submit = SubmitField('Update Profile')

    def validate_username(self, username):
        user = User.query.filter_by(username = username.data).first()
        if user:
            raise ValidationError("This username is already taken.")
    
    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError("This email is already registered.")