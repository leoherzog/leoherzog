#!/usr/bin/env python3

import os
import requests
from bs4 import BeautifulSoup

weather = requests.get('https://api.openweathermap.org/data/2.5/weather?lat=42.7777&lon=-86.1000&units=imperial&appid=' + os.environ['OWMAPIKEY']).json()

print(weather)

profile = BeautifulSoup(open('README.md'), 'html.parser')
profile.find(id='weather').string = weather['weather'][0]['description'] + ' and ' + str(round(weather['main']['temp'], 1)) + '°F'

overwrite = open('README.md', 'w')
overwrite.write(profile.prettify())
overwrite.close()