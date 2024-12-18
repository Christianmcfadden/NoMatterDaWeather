# use for API interaction
# data retrieval 
# should be done - 000
import requests

def get_weather(city):
    api_key = '44fe3ad3eed08346835cd39fff4e032a'
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return {"Error": f"Failed to retrieve data. Status code: {response.status_code}"}
