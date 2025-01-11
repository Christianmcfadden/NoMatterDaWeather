"""
NoMatterDaWeather (Web App)

Contributers:
Christian Mcfadden


Date Started: 12/7/24

File: Methods.py
"""

import requests
import json
from time import strftime, gmtime
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
    """Convert military time to normal time with AM/PM suffix."""
    hour_value = int(hour['hour'])
    if hour_value >= 12:
        hour['suffix'] = 'pm'
        if hour_value > 12:
            hour['hour'] = hour_value - 12
    else:
        hour['suffix'] = 'am'
        if hour_value == 0:
            hour['hour'] = 12
    return hour

def convert(military_time):
    """Convert military time (HH:mm) to normal time with AM/PM suffix."""
    hour = int(military_time[:2])  # Extract hour from military time
    if hour >= 12:
        suffix = 'pm'
        if hour > 12:
            hour -= 12
    else:
        suffix = 'am'
        if hour == 0:
            hour = 12
    return hour, suffix

def correctHour(hour):
    """Adjust time by subtracting 5 hours for timezone correction."""
    adjusted_time = datetime.strptime(str(hour['hour']), "%H") - timedelta(hours=5)
    hour['hour'] = adjusted_time.strftime("%H")
    return hour

def createCity(weather_data, location):
    # Get the current UTC time and adjust for the timezone (-5 hours)
    current_hour_utc = int(strftime("%H", gmtime()))
    current_minute = strftime("%M", gmtime())
    adjusted_hour = (current_hour_utc - 5) % 24

    # Convert 24-hour time to 12-hour format with AM/PM
    def convert_to_12_hour(hour):
        period = "AM" if hour < 12 else "PM"
        hour_12 = hour if hour <= 12 else hour - 12
        return hour_12, period

    current_hour_12, current_period = convert_to_12_hour(adjusted_hour)

    # Prepare the hours for the day
    hours_in_day = []
    for i in range(24):  # Iterate through 24 hours in weather data
        hour_24 = int(weather_data['days'][0]['hours'][i]['datetime'].split(':')[0])
        temp = round(weather_data['days'][0]['hours'][i]['temp'])
        conditions = weather_data['days'][0]['hours'][i]['conditions']
        hour_12, period = convert_to_12_hour(hour_24)

        if (hour_24 >= adjusted_hour) or (hour_24 == adjusted_hour and int(current_minute) == 0):
            hours_in_day.append({
                'hour': hour_12,
                'suffix': period,
                'temp': temp,
                'weather_descriptions': conditions
            })

    # Extract and process week dates
    week_dates_original = [weather_data['days'][i]['datetime'] for i in range(7)]  # Original format
    week_dates_formatted = [
        datetime.strptime(date, "%Y-%m-%d").strftime("%m-%d") for date in week_dates_original
    ]

    # Format daily summaries
    days_summary = [
        {
            'date': week_dates_formatted[i],  # Display format: mm-dd
            'dOW': findDay(week_dates_original[i]),  # Original format: yyyy-mm-dd
            'weather_descriptions': weather_data['days'][i]['conditions'],
            'temp': round(weather_data['days'][i]['temp']),
            'max': round(weather_data['days'][i]['tempmax']),
            'min': round(weather_data['days'][i]['tempmin']),
        }
        for i in range(7)
    ]

    city = {
        'display': location['display'],
        'visibility': weather_data['days'][0]['visibility'],
        'feels_like': round(weather_data['days'][0]['feelslike']),
        'humidity': weather_data['days'][0]['humidity'],
        'precip': weather_data['days'][0]['precip'],
        'wind_speed': weather_data['days'][0]['windspeed'],
        'weather_descriptions': weather_data['days'][0]['conditions'],
        'temperature': round(weather_data['days'][0]['temp']),
        'observation_date': strftime("%d-%m", gmtime()),
        'observation_time': f"{current_hour_12}:{current_minute}{current_period}",
        'city': location['city'],
        'state': location['state'],
        'feels_like_min': round(weather_data['days'][0]['feelslikemin']),
        'feels_like_max': round(weather_data['days'][0]['feelslikemax']),
        'hours': hours_in_day,
        'days': days_summary,
    }

    return city

"""
This how cities info is processed

>>> locationData = getCurrentLocal()
>>> weatherData, locationData = get_weather(locationData)
>>> city = createCity(weatherData, locationData)
>>> print(city)

"""
