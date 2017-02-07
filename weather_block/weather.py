#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
from city_id_fetcher import CityIdFetcher
from urllib import request

API_KEY = "52c8551a9d71dde5a242a125e4b70235"
URGENT_LOWER = 0
URGENT_HIGHER = 30

ICON_SUNNY = ""
ICON_CLOUDY = ""
ICON_RAINY = ""
ICON_STORM = ""
ICON_SNOW = ""
ICON_FOG = ""

SYMBOL_CELSIUS = "℃"
WEATHER_URL = "http://api.openweathermap.org/data/2.5/weather?id="


def hasWeather(weather, weather_type):
    return weather.lower().find(weather_type) != -1


def main():
    fetcher = CityIdFetcher()
    city_id = fetcher.getCityId()
    weather_url = WEATHER_URL+str(city_id)+"&appid="+API_KEY+"&units=metric"
    response = request.urlopen(weather_url)
    content = response.read()
    data = json.loads(content)
    temp = data["main"]["temp"]
    weather = data["weather"][0]["main"]
    if (hasWeather(weather, "snow")):
        print(ICON_SNOW+str(temp)+SYMBOL_CELSIUS)
        print(ICON_SNOW+str(temp)+SYMBOL_CELSIUS)
    elif (hasWeather(weather, "rain")):
        print(ICON_RAINY+str(temp)+SYMBOL_CELSIUS)
        print(ICON_RAINY+str(temp)+SYMBOL_CELSIUS)
    elif (hasWeather(weather, "cloud")):
        print(ICON_CLOUDY+str(temp)+SYMBOL_CELSIUS)
        print(ICON_CLOUDY+str(temp)+SYMBOL_CELSIUS)
    elif (hasWeather(weather, "clear")):
        print(ICON_SUNNY+str(temp)+SYMBOL_CELSIUS)
        print(ICON_SUNNY+str(temp)+SYMBOL_CELSIUS)
    elif (hasWeather(weather, "fog")):
        print(ICON_FOG+str(temp)+SYMBOL_CELSIUS)
        print(ICON_FOG+str(temp)+SYMBOL_CELSIUS)
    else:
        print(weather+str(temp)+SYMBOL_CELSIUS)
        print(weather+str(temp)+SYMBOL_CELSIUS)

    print()

if __name__ == '__main__':
    main()
