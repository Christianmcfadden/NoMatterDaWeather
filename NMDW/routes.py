"""
NoMatterDaWeather (Web App)

Contributers:
Christian Mcfadden


Date Started: 12/7/24

File: Routes.py
"""
from flask import render_template, url_for, flash, redirect, session, request
from NMDW import app, db, bcrypt
from NMDW.forms import LoginForm, UserInfoForm, UserCredentialsForm, UpdateNameForm, UpdateUsernameForm, UpdateEmailForm, UpdateDobForm, UpdateGenderForm, UpdatePasswordForm, UpdateZipForm, UpdateBioForm, UpdateProfilePicForm, PostForm
from NMDW.models import User, Post, Flag, Review, ActivityLog
from flask_login import login_user, current_user, logout_user, login_required
from datetime import datetime, date
import os
from werkzeug.utils import secure_filename
from NMDW.methods import *

@app.route('/')
def home():
    log_in_form = LoginForm()
    return render_template("login.html", form=log_in_form)
