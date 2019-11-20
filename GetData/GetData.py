import requests
import json


def get_weather_date(id='3220804', days=1):
    pass
    base_url = "http://api.openweathermap.org/data/2.5/forecast?"
    API_key = "f6633771b45cd04203686b97ff8bfa08"    
    city_id = id

    # This is final url. This is concatenation of base_url, API_key and city_id
    Final_url = base_url + "appid=" + API_key + "&id=" + city_id
    weather_data = requests.get(Final_url).json()
    records = days * 8

    return weather_data['list'][:records]

def kelvinToCelsuis(kelvin):
    return kelvin - 273.15



# API_key = "f6633771b45cd04203686b97ff8bfa08"
 
# # This stores the url
# base_url = "http://api.openweathermap.org/data/2.5/forecast?"
 
# # This will ask the user to enter city ID
# city_id = '3220804'

# # This is final url. This is concatenation of base_url, API_key and city_id
# Final_url = base_url + "appid=" + API_key + "&id=" + city_id
# weather_data = requests.get(Final_url).json()

# print('Days',len(weather_data['list']))

# for value in weather_data['list']:
#     print('Temp:' ,value['main']['temp'],end=', ')
#     print('Temp:' ,value['main']['humidity'],end=', ')
#     print('Weather:', value['weather'][0]['description'])

# # humidity 


