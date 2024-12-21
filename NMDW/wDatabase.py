"""
NoMatterDaWeather (Web App)

Contributers:
Christian Mcfadden


Date Started: 12/19/24

File: wDatabase.py
"""

import sqlite3

#The Weather App will store user info and 
CREATE_USERS_TABLE = """CREATE TABLE users (
        userid INTEGER PRIMARY KEY, 
        fname TEXT, 
        lname TEXT,       
        email TEXT,
        dob TEXT,
        password TEXT,
        city TEXT, 
        zip Integer,
        profile_pic TEXT);"""

INSERT_USER = """INSERT INTO users (
        fname, 
        lname, 
        dob, 
        email, 
        password, 
        city,
        zip, 
        profile_pic) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?);"""

GET_ALL_USERS = "SELECT * FROM users;"
GET_USERS_BY_NAME = "SELECT * FROM users WHERE fname = ? or lname = ?;"
DELETE_USER_BY_ID = "DELETE FROM users WHERE userid = ?;"  
GET_USER_BY_EMAIL = "SELECT * FROM users WHERE email = ?;"

# This function can be used the connect to the database 
def connect(db_name):
    return sqlite3.connect(db_name)

# This will be the function that you call on the first time starting the database
def create_tables(connection):
    with connection:
        connection.execute(CREATE_USERS_TABLE)

def add_user(connection, fname, lname, dob, email, password, city, zip, profile_pic):
    with connection:
        connection.execute(INSERT_USER, (fname, lname, dob, email, password, city, zip, profile_pic))

def get_all_users(connection):
    with connection:
        return connection.execute(GET_ALL_USERS).fetchall()

def get_users_by_name(connection, name):
    with connection:
        return connection.execute(GET_USERS_BY_NAME, (name,)).fetchall()
    
def delete_user(connection, user_id):
    with connection:
        connection.execute(DELETE_USER_BY_ID, (user_id,))
        print(f"User with ID {user_id} deleted successfully.")

def get_user_by_email(connection, email):
    with connection:
        cursor = connection.cursor()
        cursor.execute(GET_USER_BY_EMAIL, (email,))
        user = cursor.fetchone()  # Fetches the first matching user
        cursor.close()
        return user      

