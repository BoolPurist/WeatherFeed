import sys
sys.path.append('C:\\Floskönigreich\\GitHub-BoolPurist\\WeatherFeed\\GetData')

import datetime

import GetData

current_time = datetime.datetime.now()


weather = GetData.get_weather_date()

print(f'Today\'s date {current_time.day}.{current_time.month}.{current_time.year}:', end='\n\n')

for value in weather:
    print(f'At {current_time.hour:02}:{current_time.minute:02}:{current_time.second:02}')
    celsius = GetData.kelvinToCelsuis(value['main']['temp'])
    print('Temp:' ,'{:5.2f}'.format(celsius),end=', ')
    print('Humidity:' ,value['main']['humidity'],end=', ')
    print('Weather:', value['weather'][0]['description'], end='\n\n')
    current_time += datetime.timedelta(hours=3)

