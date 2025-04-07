import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit()
response = requests.get("https://itunes.apple.com/search?entity=song&limit=10&term="+sys.argv[1])

# json.dumps() used to print code pretty in python dictionary format
# print(json.dumps(response.json(), indent = 2))

# Getting the response in a json format, alternatively in a dictionary format in python
o = response.json()
# print(o)
# getting the trackname fron the Api response
for item in o["results"]:
    print(item["trackName"])
