#!/usr/bin/env python3

import os
import json
import urllib.request

icons = {
  "clear-day": "☀️",
  "clear-night": "🌙",
  "cloudy": "☁️",
  "foggy": "🌁",
  "partly-cloudy-day": "⛅",
  "partly-cloudy-night": "⛅",
  "possibly-rainy-day": "🌦️",
  "possibly-rainy-night": "🌦️",
  "possibly-sleet-day": "🌨️",
  "possibly-sleet-night": "🌨️",
  "possibly-snow-day": "🌨️",
  "possibly-snow-night": "🌨️",
  "possibly-thunderstorm-day": "⛈️",
  "possibly-thunderstorm-night": "⛈️",
  "rainy": "🌧️",
  "sleet": "🌨️",
  "snow": "🌨️",
  "thunderstorm": "⛈️",
  "windy": "🍃"
}

url = 'https://swd.weatherflow.com/swd/rest/better_forecast?station_id=71686&token=' + os.environ['TEMPEST_PUT'] + '&units_temp=f'
with urllib.request.urlopen(url) as response:
  data = response.read()
  weather = json.loads(data.decode('utf-8'))

print(weather)

profile = open('README.md', 'r', encoding='utf-8').read()
start_pos = profile.find('\u200B') + len('\u200B') # zero-width spaces
end_pos = profile.find('\u200B', start_pos)

temp = str(round(weather['current_conditions']['air_temperature'])) + '°' + weather['units']['units_temp'].upper()
condition = icons[weather['current_conditions']['icon']] + ' ' + weather['current_conditions']['conditions']
profile = profile[:start_pos] + temp + ' and ' + condition + profile[end_pos:]

overwrite = open('README.md', 'w', encoding='utf-8')
overwrite.write(profile)
overwrite.close()