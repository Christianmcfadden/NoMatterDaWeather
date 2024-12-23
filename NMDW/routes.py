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

# home route
@app.route('/')
def home():
   if current_user.is_authenticated:
      return redirect(url_for('dashboard'))
   login_form = LoginForm()
   return render_template("login.html", form = login_form)

# registration route
@app.route('/register', methods = ['GET', 'POST'])
def register():
   if current_user.is_authenticated:
      return redirect(url_for('dashboard'))
   # this form is from forms.py
   form = UserInfoForm()
   if form.validate_on_submit():
      hashed_password = bcrypt.generate_password_hash(form.password.data).decode('urf-8')
      user = User(username = form.username.data, email = form.email.data, password = hashed_password)
      db.session.add(user) # change - use connection =, pass paramter, fname,lname,zip
      db.session.commit() # change - connection.close()
      flash('Account created. You can now log in.', 'Success')
      return redirect(url_for('home'))
   return render_template('register.html', form = form)

# dashboard route
@app.route('/dashboard')
@login_required
def dashboard():
   return render_template('dashboard.html', user = current_user)

# logout route
@app.route('/logout')
def logout():
   logout_user()
   flash('You have been logged out')
   return redirect(url_for('home'))

# route for updating profile
@app.route('/profile', methods = ['GET', 'POST'])
@login_required
def profile():
    form = UpdatedProfileForm()  # change this in forms.py, get to dashboard
    if form.validate_on_submit:
        return