#!/usr/bin/env python3

import os
import requests
from bs4 import BeautifulSoup

weather = requests.get('https://swd.weatherflow.com/swd/rest/better_forecast?station_id=71686&token=' + os.environ['TEMPEST_PUT'] + '&units_temp=f').json()

print(weather)

profile = BeautifulSoup(open('README.md'), 'html.parser')
profile.find(id='weather').string = str(round(weather['current_conditions']['air_temperature'], 1)) + '°' + weather['units']['units_temp'].upper() + ' and ' + weather['current_conditions']['conditions']

overwrite = open('README.md', 'w')
overwrite.write(profile.prettify())
overwrite.close()