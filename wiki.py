import requests
import urllib
import json


def searchEntities():
    sea = input("What do you want to search for?")
    url = "https://www.wikidata.org/w/api.php?action=wbsearchentities&search=" + sea + "&language=en&limit=10&format=json"
    r = requests.get(url)
    json_data = r.json()
    print(json_data)
    with open(sea + ".json", 'w') as f:
        json.dump(json_data, f, indent=4, separators=(". ", " = "))

def getEntities():
    sea = input("What do you want to search for?")
    url = "https://www.wikidata.org/w/api.php?action=wbgetentities&ids=" + sea + "&language=en&limit=10&format=json"
    r = requests.get(url)
    json_data = r.json()
    print(json_data)
    with open(sea + ".json", 'w') as f:
        json.dump(json_data, f)
        json.dump(json_data, f, indent=4, separators=(". ", " = "))


option = input("1 to search entities or 2 to get entities: ")
option = int(option)
if option == 1:
    searchEntities()
elif option == 2:
    getEntities()
# else:
#     print("wrong selection")

print(option)

"""
url = "https://www.wikidata.org/w/api.php?action=wbsearchentities&search=abc&language=en&format=json"
r = requests.get(url)
json_data = r.json()
print(json_data)
with open('data.json', 'w') as f:
    json.dump(json_data, f)
    """
