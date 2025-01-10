"""
NoMatterDaWeather (Web App)

Contributers:
Christian Mcfadden


Date Started: 12/7/24

File: Methods.py
"""

import requests
import json
from datetime import datetime, timedelta

# This function will take in a zip code and get the city name
def get_geolocal():
    try:
        # Use ip-api.com to fetch geolocation data
        url = 'http://ip-api.com/json/'
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200 and data['status'] == 'success':
            locationData = { # Update location Data
                'display' : f"{data['city']}, {data['region']}",
                'city' : data['city'],
                'state' : data['region'],
                'zip' : data['zip'],
                'timezone' : data['timezone'],
                'cCode' : data['countryCode'],
                'provider' : data['org']
            }
            return locationData
        else: 
            return {}
    
    except Exception as e:
        print(f"Error occurred: {e}")
        return {"Error": f"Failed to retrieve location data. Status code: {response.status_code}"}

# Get weather checks if locationData is a str or dic and handles it correctly  
def get_weather(locationData):
    api_key = 'RCFA2FC8DPYXDBMG75A4HRUXC'
    today, sevenDay = getRange()
    if isinstance(locationData, str):
        try:
            locationData = json.loads(locationData)
        except json.JSONDecodeError:
            raise ValueError("locationData is not valid JSON.")
        
    if isinstance(locationData, dict) and 'zip' in locationData:
        zip_code = locationData['zip']
        locationData = get_location_data(zip_code)
        url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{zip_code}/{today}/{sevenDay}?unitGroup=us&key={api_key}&contentType=json"
        response = requests.get(url)
        return response.json(), locationData
    else:
        raise TypeError("Dictionary doesn't containing a 'zip' key.")
    
def getCurrentLocal():
    try:
        # Use to fetch geolocation data
        url = 'http://ip-api.com/json/'
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200 and data['status'] == 'success':
            locationData = {
                'display' : f"{data['city']}, {data['region']}",
                'city' : data['city'],
                'state' : data['region'],
                'zip' : data['zip'],
                'timezone' : data['timezone'],
                'cCode' : data['countryCode'],
                'provider' : data['org']
            }
            return locationData
        else:
            locationData = {
                'display' : "",
                'city' : "",
                'state' : "",
                'zip' : "",
                'timezone' : "",
                'cCode' : "",
                'provider' : ""
            }
            print("Error : Empty locationData variable")
            return locationData

    except Exception as e:
        print(f"Error occurred: {e}")
        return ""
    
def get_location_data(zip):
    url = f"http://api.zippopotam.us/us/{zip}"
    try:
        response = requests.get(url)
        data = response.json()
        locationData = {
                'display' : f"{data['places'][0]['place name']}, {data['places'][0]['state abbreviation']}",
                'city' : data['places'][0]['place name'],
                'state' : data['places'][0]['state abbreviation'],
                'zip' : zip,
                'timezone' : "",
                'cCode' : data['country abbreviation'],
                'provider' : ""
        }
        return locationData
    except requests.exceptions.RequestException as e:
        print(f"Error fetching lat/lon: {e}")
        return None
    
def findDay(hour):
    date_string = hour
    date_object = datetime.strptime(date_string, '%Y-%m-%d')
    day_of_week = date_object.strftime('%A')
    return day_of_week

def getRange():
    current_date = datetime.today().date() 
    next_7_days = []
    for i in range(7):
        next_day = current_date + timedelta(days=i)
        next_7_days.append(next_day)
    today = str(next_7_days[0])
    sevenDay = str(next_7_days[-1])
    return today, sevenDay
# Update all of the following 
def getDates(week):
    result = []
    for i in week:
        result.append(i[5:])
    return result[0], result[1], result[2], result[3], result[4], result[5], result[6]

def milToNormal(hour):
    return 

# i need to make the hourly forcast only show current time and on and also make the hours go from 12am to 11pm
def createCity(weather_data, location): 
    time = strftime("%H:%M", gmtime())
    date = strftime("%d-%m", gmtime())
    current_hour = strftime("%H", gmtime())
    week = [weather_data['days'][0]['datetime'], weather_data['days'][1]['datetime'], weather_data['days'][2]['datetime'], weather_data['days'][3]['datetime'], weather_data['days'][4]['datetime'], weather_data['days'][5]['datetime'], weather_data['days'][6]['datetime']]
    day1, day2, day3, day4, day5, day6, day7 = getDates(week)
    city = { 
        'display': location['display'],
        'visibility': weather_data['days'][0]['visibility'],
        'feels_like': round(weather_data['days'][0]['feelslike']),
        'humidity': weather_data['days'][0]['humidity'],
        'precip': weather_data['days'][0]['precip'],
        'wind_speed': weather_data['days'][0]['windspeed'],
        'weather_descriptions': weather_data['days'][0]['conditions'],
        'temperature': round(weather_data['days'][0]['temp']),
        'observation_date': date, # format mm-dd
        'observation_time': time, # time is 5 hours ahead 
        'city': location['city'], 
        'state': location['state'], 
        'feels_like_min': round(weather_data['days'][0]['feelslikemin']),
        'feels_like_max': round(weather_data['days'][0]['feelslikemax']),
        'hours':[{'time': weather_data['days'][0]['hours'][0]['datetime'],
                  'temp': round(weather_data['days'][0]['hours'][0]['temp']),
                  'weather_descriptions': weather_data['days'][0]['hours'][0]['conditions']},
                  {'time': weather_data['days'][0]['hours'][1]['datetime'],
                  'temp': round(weather_data['days'][0]['hours'][1]['temp']),
                  'weather_descriptions': weather_data['days'][0]['hours'][1]['conditions']},
                  {'time': weather_data['days'][0]['hours'][2]['datetime'],
                  'temp': round(weather_data['days'][0]['hours'][2]['temp']),
                  'weather_descriptions': weather_data['days'][0]['hours'][2]['conditions']},
                  {'time': weather_data['days'][0]['hours'][3]['datetime'],
                  'temp': round(weather_data['days'][0]['hours'][3]['temp']),
                  'weather_descriptions':weather_data['days'][0]['hours'][3]['conditions']},
                  {'time': weather_data['days'][0]['hours'][4]['datetime'],
                  'temp': round(weather_data['days'][0]['hours'][4]['temp']),
                  'weather_descriptions': weather_data['days'][0]['hours'][4]['conditions']},
                  {'time': weather_data['days'][0]['hours'][5]['datetime'],
                  'temp': round(weather_data['days'][0]['hours'][5]['temp']),
                  'weather_descriptions': weather_data['days'][0]['hours'][5]['conditions']},
                  {'time': weather_data['days'][0]['hours'][6]['datetime'],
                  'temp': round(weather_data['days'][0]['hours'][6]['temp']),
                  'weather_descriptions': weather_data['days'][0]['hours'][6]['conditions']},
                  {'time': weather_data['days'][0]['hours'][7]['datetime'],
                  'temp': round(weather_data['days'][0]['hours'][7]['temp']),
                  'weather_descriptions': weather_data['days'][0]['hours'][7]['conditions']},
                  {'time': weather_data['days'][0]['hours'][8]['datetime'],
                  'temp': round(weather_data['days'][0]['hours'][8]['temp']),
                  'weather_descriptions': weather_data['days'][0]['hours'][8]['conditions']},
                  {'time': weather_data['days'][0]['hours'][9]['datetime'],
                  'temp': round(weather_data['days'][0]['hours'][9]['temp']),
                  'weather_descriptions': weather_data['days'][0]['hours'][9]['conditions']},
                  {'time': weather_data['days'][0]['hours'][10]['datetime'],
                  'temp': round(weather_data['days'][0]['hours'][10]['temp']),
                  'weather_descriptions': weather_data['days'][0]['hours'][10]['conditions']},
                  {'time': weather_data['days'][0]['hours'][11]['datetime'],
                  'temp': round(weather_data['days'][0]['hours'][11]['temp']),
                  'weather_descriptions': weather_data['days'][0]['hours'][11]['conditions']},
                  {'time': weather_data['days'][0]['hours'][12]['datetime'],
                  'temp': round(weather_data['days'][0]['hours'][12]['temp']),
                  'weather_descriptions': weather_data['days'][0]['hours'][12]['conditions']},
                  {'time': weather_data['days'][0]['hours'][13]['datetime'],
                  'temp': round(weather_data['days'][0]['hours'][13]['temp']),
                  'weather_descriptions': weather_data['days'][0]['hours'][13]['conditions']},
                  {'time': weather_data['days'][0]['hours'][14]['datetime'],
                  'temp': round(weather_data['days'][0]['hours'][14]['temp']),
                  'weather_descriptions': weather_data['days'][0]['hours'][14]['conditions']},
                  {'time': weather_data['days'][0]['hours'][15]['datetime'],
                  'temp': round(weather_data['days'][0]['hours'][15]['temp']),
                  'weather_descriptions': weather_data['days'][0]['hours'][15]['conditions']},
                  {'time': weather_data['days'][0]['hours'][16]['datetime'],
                  'temp': round(weather_data['days'][0]['hours'][16]['temp']),
                  'weather_descriptions': weather_data['days'][0]['hours'][16]['conditions']},
                  {'time': weather_data['days'][0]['hours'][17]['datetime'],
                  'temp': round(weather_data['days'][0]['hours'][17]['temp']),
                  'weather_descriptions': weather_data['days'][0]['hours'][17]['conditions']},
                  {'time': weather_data['days'][0]['hours'][18]['datetime'],
                  'temp': round(weather_data['days'][0]['hours'][18]['temp']),
                  'weather_descriptions': weather_data['days'][0]['hours'][18]['conditions']},
                  {'time': weather_data['days'][0]['hours'][19]['datetime'],
                  'temp': round(weather_data['days'][0]['hours'][19]['temp']),
                  'weather_descriptions': weather_data['days'][0]['hours'][19]['conditions']},
                  {'time': weather_data['days'][0]['hours'][20]['datetime'],
                  'temp': round(weather_data['days'][0]['hours'][20]['temp']),
                  'weather_descriptions': weather_data['days'][0]['hours'][20]['conditions']},
                  {'time': weather_data['days'][0]['hours'][21]['datetime'],
                  'temp': round(weather_data['days'][0]['hours'][21]['temp']),
                  'weather_descriptions': weather_data['days'][0]['hours'][21]['conditions']},
                  {'time': weather_data['days'][0]['hours'][22]['datetime'],
                  'temp': round(weather_data['days'][0]['hours'][22]['temp']),
                  'weather_descriptions': weather_data['days'][0]['hours'][22]['conditions']},
                  {'time': weather_data['days'][0]['hours'][23]['datetime'],
                  'temp': round(weather_data['days'][0]['hours'][23]['temp']),
                  'weather_descriptions': weather_data['days'][0]['hours'][23]['conditions']},],
        'days':[{'date': day1,
                 'dOW': findDay(weather_data['days'][0]['datetime']),
                 'weather_descriptions': weather_data['days'][0]['conditions'],
                 'temp': round(weather_data['days'][0]['temp']),
                 'max': round(weather_data['days'][0]['tempmax']),
                 'min': round(weather_data['days'][0]['tempmin'])},
                 {'date': day2,
                 'dOW': findDay(weather_data['days'][1]['datetime']),
                 'weather_descriptions': weather_data['days'][1]['conditions'],
                 'temp': round(weather_data['days'][1]['temp']),
                 'max': round(weather_data['days'][1]['tempmax']),
                 'min': round(weather_data['days'][1]['tempmin'])},
                 {'date': day3,
                 'dOW': findDay(weather_data['days'][2]['datetime']),
                 'weather_descriptions': weather_data['days'][2]['conditions'],
                 'temp': round(weather_data['days'][2]['temp']),
                 'max': round(weather_data['days'][2]['tempmax']),
                 'min': round(weather_data['days'][2]['tempmin'])},
                 {'date': day4,
                 'dOW': findDay(weather_data['days'][3]['datetime']),
                 'weather_descriptions': weather_data['days'][3]['conditions'],
                 'temp': round(weather_data['days'][3]['temp']),
                 'max': round(weather_data['days'][3]['tempmax']),
                 'min': round(weather_data['days'][3]['tempmin'])},
                 {'date': day5,
                 'dOW': findDay(weather_data['days'][4]['datetime']),
                 'weather_descriptions': weather_data['days'][4]['conditions'],
                 'temp': round(weather_data['days'][4]['temp']),
                 'max': round(weather_data['days'][4]['tempmax']),
                 'min': round(weather_data['days'][4]['tempmin'])},
                 {'date': day6,
                 'dOW': findDay(weather_data['days'][5]['datetime']),
                 'weather_descriptions': weather_data['days'][5]['conditions'],
                 'temp': round(weather_data['days'][5]['temp']),
                 'max': round(weather_data['days'][5]['tempmax']),
                 'min': round(weather_data['days'][5]['tempmin'])},
                 {'date': day7,
                 'dOW': findDay(weather_data['days'][6]['datetime']),
                 'weather_descriptions': weather_data['days'][6]['conditions'],
                 'temp': round(weather_data['days'][6]['temp']),
                 'max': round(weather_data['days'][6]['tempmax']),
                 'min': round(weather_data['days'][6]['tempmin'])}]
    }
    return city

"""
This how cities info is processed

>>> locationData = getCurrentLocal()
>>> weatherData, locationData = get_weather(locationData)
>>> city = createCity(weatherData, locationData)
>>> print(city)

"""
