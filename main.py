from pprint import pprint

import requests
import os
from dotenv import load_dotenv

load_dotenv()

token = os.environ["TOKEN"]
params = {
        "q": "Coca-Cola",
        "access_token": token,
        "start_time": 1701295140,
        "end_time": 1701381540,
        "v": "5.199"
    }
response = requests.get("https://api.vk.com/method/newsfeed.search", params=params)
response.raise_for_status()
result = response.json()
values = result.values()
for value in values:
    items = value["items"]
    for item in items:
        date = item["date"]
        print(date)


