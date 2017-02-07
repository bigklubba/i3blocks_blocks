import json
import unicodedata
import os
from urllib import request

NFKD = "NFKD"
url = "http://ipinfo.io/json"
FILE_PATH = os.path.dirname(os.path.abspath(__file__)) + "/"


def isSubstring(city1, city2):
    normal_city1 = unicodedata.normalize(NFKD, city1).encode("ascii", "ignore")
    normal_city2 = unicodedata.normalize(NFKD, city2).encode("ascii", "ignore")
    return normal_city2.find(normal_city1) != -1


class CityIdFetcher:
    def getCityId(self):
        """Get the city id from the current ip"""
        """if no id is found -1 will be returned"""

        response = request.urlopen(url)
        content = response.read()
        string_content = content.decode("utf-8")
        data = json.loads(string_content)
        city = data["city"]
        f = open(FILE_PATH + "city.list.json", "r")
        for row in f.readlines():
            json_line = json.loads(row)
            json_city = json_line["name"]

            if (isSubstring(city, json_city)):
                return json_line["_id"]

        return -1
