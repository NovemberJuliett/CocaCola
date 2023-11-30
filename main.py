import requests
import os
from dotenv import load_dotenv
import datetime

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

today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
utc_date = datetime.datetime(year=2023, month=11, day=29, tzinfo=datetime.timezone.utc).timestamp()
# print(int(utc_date))

start_date = datetime.date.today()
for count in range(7):
    start_date = start_date - datetime.timedelta(days=1)
    print(start_date)




