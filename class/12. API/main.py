import json

import requests

keyword = input("Give me a keyword: ")

request = "https://api.tvmaze.com/search/shows?q= " + keyword
# response = requests.get(request).json()

# print(response)
# print(json.dumps(response, indent= 2))
"""
for i in response:
    print(i["show"] ["name"])
"""


try:
    response = requests.get(request)
    if response.status_code == 200:
        json_response = response.json()
        for i in json_response:
            print(i["show"]["name"])
except requests.exceptions.RequestException as e:
    print("Request cannot be performed")  # request wrong address