import json

import requests
from lxml import etree

url = f'https://tianqi.2345.com/Pc/apiGet15Days?area_id=58357&area_type=2'
headers = {
    'User-Agent': ')Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0\
     Safari/537.36 Edg/120.0.0.0'
}

resp = requests.get(url, headers=headers)
data = resp.json()

weather_data_list = data.get('data', [])
weather_data_list = weather_data_list[1:]

with open('weather.txt', 'w', encoding='utf-8') as f:
    for day_data in weather_data_list:
        date = day_data.get('date')
        weather = day_data.get('whole_wea')
        day_wind_direction = day_data.get('day_wind_direction')
        whole_temp = day_data.get('whole_temp')

        f.write(f"日期: {date}\n")
        f.write(f"天气: {weather}\n")
        f.write(f"白天风向: {day_wind_direction}\n")
        f.write(f"气温: {whole_temp}\n\n")

