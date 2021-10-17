import requests
import json
import datetime
from time import *


def getWind(ville):
    url_weather = "http://api.openweathermap.org/data/2.5/weather?q=" + \
        ville+"&APPID=beb97c1ce62559bba4e81e28de8be095"

    r_weather = requests.get(url_weather)
    data = r_weather.json()

    wind = data['wind']['speed']
    return wind
