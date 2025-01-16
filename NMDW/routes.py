"""
NoMatterDaWeather (Web App)

Contributers:
Christian Mcfadden


Date Started: 12/7/24

File: Routes.py
"""
from flask import render_template, url_for, flash, redirect, session, request
from NMDW import app, db, bcrypt
from NMDW.forms import LoginForm, UserInfoForm
from NMDW.models import User
from flask_login import login_user, current_user, logout_user, login_required
from datetime import datetime, date
import os
import json #NEW 
from werkzeug.utils import secure_filename
from NMDW.methods import *
from NMDW.forms import *

# Initial route that loads a search and login options
@app.route("/")
def get_location():
    user = {
        'logged' : False
    }
    locationData = {
        'display' : "",
        'city' : "",
        'state' : "",
        'zip' : "",
        'timezone' : "",
        'cCode' : "",
        'provider' : ""
    }
    stored_locationData = json.dumps(locationData)
    session['locationData'] = stored_locationData
    stored_user = json.dumps(user)
    session['user'] = stored_user
    return render_template("FindLocalWeatherPage.html", user=user)

# get zip from user or provide one for them  
@app.route('/set_location', methods=["POST", "GET"])
def get_zip():
    locationData = session['locationData']
    locationData = json.loads(locationData)
    user = session['user']
    user = json.loads(user)
    zip = request.form.get("zip")
    if not zip:
        if locationData['zip'] == "":
            locationData = get_geolocal()
            weatherData, locationData = get_weather(locationData)
            city = createCity(weatherData, locationData) # Add location
            return render_template("DetailedWeatherPage.html", city=city, user=user) # Remove location 
        else:
            weatherData, locationData = get_weather(locationData)
            city = createCity(weatherData, locationData) # Add location
            return render_template("DetailedWeatherPage.html", city=city, user=user) # Remove location 
    else:
        locationData = {
                'current_city' : f"{zip}",
                'zip' : zip,
                'timezone' : "",
                'lon' : "",
                'lat' : ""
        }
        weatherData, locationData = get_weather(locationData) 
        city = createCity(weatherData, locationData) # Add location
        return render_template("DetailedWeatherPage.html", city=city, user=user) # Remove location 

# This route gets a users current location
@app.route('/current_location')
def getCurrentLocal():
    user = session['user']
    user = json.loads(user)
    locationData = get_geolocal()
    if locationData:
        weatherData, locationData = get_weather(locationData)
        city = createCity(weatherData, locationData) # Add location
        return render_template("DetailedWeatherPage.html", city=city, user=user) # Remove location 
    else:
        return render_template("FindLocalWeatherPage.html", user=user)

@app.route('/search_again')
def find():
    user = session['user']
    user = json.loads(user)
    locationData = {
        'display' : "",
        'city' : "",
        'state' : "",
        'zip' : "",
        'timezone' : "",
        'cCode' : "",
        'provider' : ""
    }
    session['locationData'] = locationData
    return render_template("FindLocalWeatherPage.html", user=user)
   
# registration route
@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = UserInfoForm()
    return render_template('SignUpPage.html', form = form)

@app.route('/validate_register', methods = ['GET', 'POST'])
def validate_register():
   if current_user.is_authenticated:
      return redirect(url_for('dashboard'))
   # this form is from forms.py
   form = UserInfoForm()
   if form.validate_on_submit():
      hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
      user = User(username = form.username.data, email = form.email.data, password = hashed_password)
      db.session.add(user) # change - use connection =, pass paramter, fname,lname,zip
      db.session.commit() # change - connection.close()
      flash('Account created. You can now log in.', 'Success')
      return redirect(url_for('dashboard')) # load page with favs
   return render_template('register.html', form = form)

# dashboard route
@app.route('/dashboard') # dashboard
# @login_required
def dashboard():
    favsList = []
    locationData = get_geolocal() # Current Location 
    weatherData, locationData = get_weather(locationData)
    current = createCity(weatherData, locationData) # Storing current location weather
    favs = [] # Pull favs from db 12542, 28328, 28303, 10010
    for zip in favs:
        location = get_location_data(zip) # Getting location info for favs
        weatherData, location = get_weather(location)
        city = createCity(weatherData, location)
        favsList.append(city)
    return render_template('MainWeatherPage.html', current=current, favsList=favsList)

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
    if form.validate_on_submit():
        #update users profile info
       current_user.username = form.username.data
       current_user.fname = form.fname.data
       current_user.lname = form.lname.data
       current_user.email = form.email.data
       current_user.zip_code = form.zip_code.data
       db.session.commit()
       flash('Your profile has been updated.', 'Success.')
       return redirect(url_for('dashboard'))

# route to login
@app.route('/login', methods = ['GET', 'POST'])
def login(): 
    form = LoginForm()
    return render_template('LogInPage.html', form=form)

@app.route('/validate_login', methods = ['GET', 'POST'])
def validate_login():
   if current_user.is_authenticated: # logged in users get sent to dashboard
      return redirect(url_for('dashboard'))
   form = LoginForm()
   if form.validate_on_submit():
      user = User.query.filter_by(email=form.email.data).first()
      if user and bcrypt.check_password_hash(user.password, form.password.data):
         login_user(user, remember=form.remember.data)
         flash('Login successful.', 'Success.')
         next_page = request.args.get('next') # redirect to intended page
         return redirect(next_page) if next_page else redirect(url_for('dashboard'))
      else:
         flash('Login failed. Check your email and password.')
   return render_template('LogInPage.html', form=form)
