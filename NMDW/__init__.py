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

# i might use firebase to handle login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

#Encoding integration
bcrypt = Bcrypt(app)



from NMDW import routes

"""
How To refreeze the requirements

    * Freeze Any New Requirements:
        (pip freeze > requirements.txt)

    * Mention in request to submit that you need the requirements updated Note the packages added

Clone the GitHub Repository
    * Clone the Repositiory:
        (git clone https://github.com/Christianmcfadden/NoMatterDaWeather.git)

    * Navigate to Repositiory:
        (cd my-repo)

How To Stage The File
    (git add .)   <-- Adds modified files to the staging area
    (git add file1.txt file2.txt) <-- If you manually want to stage specific files

    
How To Commit Files To The Main Branch In The Repository
    * Stage The Files:
        
    * Commit The Files:
        Commit Files With Message:
            (git commit -m "Your commit message")
        Push To Main:
            (git push origin main)


How To Commit Files To A New Branch In The Repository
    * Stage The Files:

    * Commit The Files:
        Create a New Branch:
            (git checkout -b your-branch-name)
        
        Push the New Branch:
            (git push origin your-branch-name)

        Submit a Pull Request (PR):
            Go to the original repository on GitHub.
            You’ll see a prompt to create a pull request for the new branch.
            Click Compare & pull request.
            Add a description of your changes and submit the PR for review.


"""
