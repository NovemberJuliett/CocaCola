import requests
import os
from dotenv import load_dotenv
import datetime
from pprint import pprint

load_dotenv()

token = os.environ["TOKEN"]
params = {
        "q": "Кока-Кола",
        "access_token": token,
        "start_time": 1700949600,
        "end_time": 1701381600,
        "v": "5.199"
    }
response = requests.get("https://api.vk.com/method/newsfeed.search", params=params)
response.raise_for_status()
result = response.json()
# pprint(result)
values = result.values()
for value in values:
    items = value["items"]
    for item in items:
        date = item["date"]

today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
utc_date = datetime.datetime(year=2023, month=11, day=29, tzinfo=datetime.timezone.utc).timestamp()

start_date = datetime.date.today()
start_date_time = datetime.datetime(start_date.year, start_date.month, start_date.day)
end_date_time = start_date_time - datetime.timedelta(days=1)
date_tuple = tuple((start_date, start_date_time, end_date_time))
date_list = []
for count in range(7):
    date_tuple = tuple((start_date, end_date_time.timestamp(), start_date_time.timestamp()))
    date_list.append(date_tuple)
    start_date = start_date - datetime.timedelta(days=1)
    start_date_time = start_date_time - datetime.timedelta(days=1)
    end_date_time = start_date_time - datetime.timedelta(days=1)


pprint(date_list)





