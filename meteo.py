from contextlib import closing
from urllib.request import urlopen
import json
from bs4 import BeautifulSoup

# with closing(urlopen('https://api.meteo-concept.com/api/location/city?token=e8f9c5fd0701920f7fff2fcaec99851dca1e5e6d7acb0faab96f1f4578d4dc0f')) as f:
#    city = json.loads(f.read())['paris']
#    print(u'La ville de {} ({}) a pour coordonnées {},{}.'.format(
#        city['Paris'], city['cp'], city['latitude'], city['longitude']))

import urllib.request

# urllib.request.urlretrieve(
#    'https://api.meteo-concept.com/api/forecast/daily?token=e8f9c5fd0701920f7fff2fcaec99851dca1e5e6d7acb0faab96f1f4578d4dc0f&insee=35238', "test.xml").read().decode()


with open("test.xml", "r") as file:
    content = file.readlines()
    content = "".join(content)
    bs_content = BeautifulSoup(content, "lxml")

result = bs_content.find_all("cp")
print(result)
