import requests
import json


def get_weather_date(id='3220804', days=1):
    file = open('GetData\\APIkey.txt', 'r')
    API_key = file.read()    
    file.close()
    
    base_url = "http://api.openweathermap.org/data/2.5/forecast?"
    city_id = id

    # This is final url. This is concatenation of base_url, API_key and city_id
    Final_url = base_url + "appid=" + API_key + "&id=" + city_id
    print('End Url:', Final_url)
    
    weather_data = requests.get(Final_url)
    
    if weather_data.status_code != 200:
        print("HTTP request went wrong, Code:", weather_data.status_code)
        return None
    
    weather_data = weather_data.json()
    
    records = days * 8

    return weather_data['list'][:records]


def kelvinToCelsuis(kelvin):
    return kelvin - 273.15
