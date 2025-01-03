"""
NoMatterDaWeather (Web App)

Contributers:
Christian Mcfadden


Date Started: 12/7/24

File: Methods.py
"""

import requests
from datetime import datetime, timedelta

# This function will take in a zip code and get the city name
def get_geolocal():
    try:
        # Use ip-api.com to fetch geolocation data
        url = 'http://ip-api.com/json/'
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200 and data['status'] == 'success':
            locationData = {
                'current_city' : f"{data['city']}, {data['region']} {data['zip']}",
                'zip' : data['zip'],
                'timezone' : data['timezone']
            }
            return locationData
        else: 
            return {}
    
    except Exception as e:
        print(f"Error occurred: {e}")
        return {"Error": f"Failed to retrieve location data. Status code: {response.status_code}"}

# Need new api key and link 
def get_weather(locationData):
    api_key = 'RCFA2FC8DPYXDBMG75A4HRUXC'
    today, sevenDay = getRange()
    if locationData['display'] == "":
        locationData = get_location_data(locationData['zip'])
        url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{locationData['zip']}/{today}/{sevenDay}?unitGroup=us&key={api_key}&contentType=json"
        response = requests.get(url)
        return response.json(), locationData
    else:
        url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{locationData['zip']}/{today}/{sevenDay}?unitGroup=us&key={api_key}&contentType=json"
        response = requests.get(url)
        return response.json(), locationData
    
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
            print("Error : Empty locationdata variable")
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

def createCity(weather_data):
    city = {
        'name': weather_data['resolvedAddress'],
        'visibility': weather_data['days'][0]['visibility'],
        'feels_like': weather_data['days'][0]['feelslike'],
        'humidity': weather_data['days'][0]['humidity'],
        'precip': weather_data['days'][0]['precip'],
        'wind_speed': weather_data['days'][0]['windspeed'],
        'weather_descriptions': weather_data['days'][0]['conditions'],
        'temperature': weather_data['days'][0]['temp'],
        'observation_time': weather_data['days'][0]['datetime'],
        'feels_like_min': weather_data['days'][0]['feelslikemin'],
        'feels_like_max': weather_data['days'][0]['feelslikemax'],
        'hours':[{'time': weather_data['days'][0]['hours'][0]['datetime'],
                  'temp': weather_data['days'][0]['hours'][0]['temp'],
                  'weather_descriptions': weather_data['days'][0]['hours'][0]['conditions']},
                  {'time': weather_data['days'][0]['hours'][1]['datetime'],
                  'temp': weather_data['days'][0]['hours'][1]['temp'],
                  'weather_descriptions': weather_data['days'][0]['hours'][1]['conditions']},
                  {'time': weather_data['days'][0]['hours'][2]['datetime'],
                  'temp': weather_data['days'][0]['hours'][2]['temp'],
                  'weather_descriptions': weather_data['days'][0]['hours'][2]['conditions']},
                  {'time': weather_data['days'][0]['hours'][3]['datetime'],
                  'temp': weather_data['days'][0]['hours'][3]['temp'],
                  'weather_descriptions':weather_data['days'][0]['hours'][3]['conditions']},
                  {'time': weather_data['days'][0]['hours'][4]['datetime'],
                  'temp': weather_data['days'][0]['hours'][4]['temp'],
                  'weather_descriptions': weather_data['days'][0]['hours'][4]['conditions']},
                  {'time': weather_data['days'][0]['hours'][5]['datetime'],
                  'temp': weather_data['days'][0]['hours'][5]['temp'],
                  'weather_descriptions': weather_data['days'][0]['hours'][5]['conditions']},
                  {'time': weather_data['days'][0]['hours'][6]['datetime'],
                  'temp': weather_data['days'][0]['hours'][6]['temp'],
                  'weather_descriptions': weather_data['days'][0]['hours'][6]['conditions']},
                  {'time': weather_data['days'][0]['hours'][7]['datetime'],
                  'temp': weather_data['days'][0]['hours'][7]['temp'],
                  'weather_descriptions': weather_data['days'][0]['hours'][7]['conditions']},
                  {'time': weather_data['days'][0]['hours'][8]['datetime'],
                  'temp': weather_data['days'][0]['hours'][8]['temp'],
                  'weather_descriptions': weather_data['days'][0]['hours'][8]['conditions']},
                  {'time': weather_data['days'][0]['hours'][9]['datetime'],
                  'temp': weather_data['days'][0]['hours'][9]['temp'],
                  'weather_descriptions': weather_data['days'][0]['hours'][9]['conditions']},
                  {'time': weather_data['days'][0]['hours'][10]['datetime'],
                  'temp': weather_data['days'][0]['hours'][10]['temp'],
                  'weather_descriptions': weather_data['days'][0]['hours'][10]['conditions']},
                  {'time': weather_data['days'][0]['hours'][11]['datetime'],
                  'temp': weather_data['days'][0]['hours'][11]['temp'],
                  'weather_descriptions': weather_data['days'][0]['hours'][11]['conditions']},
                  {'time': weather_data['days'][0]['hours'][12]['datetime'],
                  'temp': weather_data['days'][0]['hours'][12]['temp'],
                  'weather_descriptions': weather_data['days'][0]['hours'][12]['conditions']},
                  {'time': weather_data['days'][0]['hours'][13]['datetime'],
                  'temp': weather_data['days'][0]['hours'][13]['temp'],
                  'weather_descriptions': weather_data['days'][0]['hours'][13]['conditions']},
                  {'time': weather_data['days'][0]['hours'][14]['datetime'],
                  'temp': weather_data['days'][0]['hours'][14]['temp'],
                  'weather_descriptions': weather_data['days'][0]['hours'][14]['conditions']},
                  {'time': weather_data['days'][0]['hours'][15]['datetime'],
                  'temp': weather_data['days'][0]['hours'][15]['temp'],
                  'weather_descriptions': weather_data['days'][0]['hours'][15]['conditions']},
                  {'time': weather_data['days'][0]['hours'][16]['datetime'],
                  'temp': weather_data['days'][0]['hours'][16]['temp'],
                  'weather_descriptions': weather_data['days'][0]['hours'][16]['conditions']},
                  {'time': weather_data['days'][0]['hours'][17]['datetime'],
                  'temp': weather_data['days'][0]['hours'][17]['temp'],
                  'weather_descriptions': weather_data['days'][0]['hours'][17]['conditions']},
                  {'time': weather_data['days'][0]['hours'][18]['datetime'],
                  'temp': weather_data['days'][0]['hours'][18]['temp'],
                  'weather_descriptions': weather_data['days'][0]['hours'][18]['conditions']},
                  {'time': weather_data['days'][0]['hours'][19]['datetime'],
                  'temp': weather_data['days'][0]['hours'][19]['temp'],
                  'weather_descriptions': weather_data['days'][0]['hours'][19]['conditions']},
                  {'time': weather_data['days'][0]['hours'][20]['datetime'],
                  'temp': weather_data['days'][0]['hours'][20]['temp'],
                  'weather_descriptions': weather_data['days'][0]['hours'][20]['conditions']},
                  {'time': weather_data['days'][0]['hours'][21]['datetime'],
                  'temp': weather_data['days'][0]['hours'][21]['temp'],
                  'weather_descriptions': weather_data['days'][0]['hours'][21]['conditions']},
                  {'time': weather_data['days'][0]['hours'][22]['datetime'],
                  'temp': weather_data['days'][0]['hours'][22]['temp'],
                  'weather_descriptions': weather_data['days'][0]['hours'][22]['conditions']},
                  {'time': weather_data['days'][0]['hours'][23]['datetime'],
                  'temp': weather_data['days'][0]['hours'][23]['temp'],
                  'weather_descriptions': weather_data['days'][0]['hours'][23]['conditions']},],
        'days':[{'date': weather_data['days'][0]['datetime'],
                 'dOW': findDay(weather_data['days'][0]['datetime']),
                 'weather_descriptions': weather_data['days'][0]['conditions'],
                 'temp': weather_data['days'][0]['temp'],
                 'max': weather_data['days'][0]['tempmax'],
                 'min': weather_data['days'][0]['tempmin']},
                 {'date': weather_data['days'][1]['datetime'],
                 'dOW': findDay(weather_data['days'][1]['datetime']),
                 'weather_descriptions': weather_data['days'][1]['conditions'],
                 'temp': weather_data['days'][1]['temp'],
                 'max': weather_data['days'][1]['tempmax'],
                 'min': weather_data['days'][1]['tempmin']},
                 {'date': weather_data['days'][2]['datetime'],
                 'dOW': findDay(weather_data['days'][2]['datetime']),
                 'weather_descriptions': weather_data['days'][2]['conditions'],
                 'temp': weather_data['days'][2]['temp'],
                 'max': weather_data['days'][2]['tempmax'],
                 'min': weather_data['days'][2]['tempmin']},
                 {'date': weather_data['days'][3]['datetime'],
                 'dOW': findDay(weather_data['days'][3]['datetime']),
                 'weather_descriptions': weather_data['days'][3]['conditions'],
                 'temp': weather_data['days'][3]['temp'],
                 'max': weather_data['days'][3]['tempmax'],
                 'min': weather_data['days'][3]['tempmin']},
                 {'date': weather_data['days'][4]['datetime'],
                 'dOW': findDay(weather_data['days'][4]['datetime']),
                 'weather_descriptions': weather_data['days'][4]['conditions'],
                 'temp': weather_data['days'][4]['temp'],
                 'max': weather_data['days'][4]['tempmax'],
                 'min': weather_data['days'][4]['tempmin']},
                 {'date': weather_data['days'][5]['datetime'],
                 'dOW': findDay(weather_data['days'][5]['datetime']),
                 'weather_descriptions': weather_data['days'][5]['conditions'],
                 'temp': weather_data['days'][5]['temp'],
                 'max': weather_data['days'][5]['tempmax'],
                 'min': weather_data['days'][5]['tempmin']},
                 {'date': weather_data['days'][6]['datetime'],
                 'dOW': findDay(weather_data['days'][6]['datetime']),
                 'weather_descriptions': weather_data['days'][6]['conditions'],
                 'temp': weather_data['days'][6]['temp'],
                 'max': weather_data['days'][6]['tempmax'],
                 'min': weather_data['days'][6]['tempmin']}]
    }
    return city
