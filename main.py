import requests
import os
from dotenv import load_dotenv
import datetime
import plotly.express as px
import pandas as pd

load_dotenv()

start_date = datetime.date.today()
start_date_time = datetime.datetime(start_date.year, start_date.month, start_date.day)
end_date_time = start_date_time - datetime.timedelta(days=1)
date_tuple = tuple((start_date, start_date_time, end_date_time))
date_list = []
token = os.environ["TOKEN"]

for count in range(7):
    start_date_time = start_date_time - datetime.timedelta(days=1)
    end_date_time = start_date_time - datetime.timedelta(days=1)
    params = {
        "q": "Кока-Кола",
        "access_token": token,
        "start_time": end_date_time.timestamp(),
        "end_time": start_date_time.timestamp(),
        "v": "5.199"
    }
    response = requests.get("https://api.vk.com/method/newsfeed.search", params=params)
    response.raise_for_status()
    result = response.json()
    values = result.values()
    for value in values:
        item_count = value["count"]
    date_tuple = tuple((start_date, item_count))
    date_list.append(date_tuple)
    start_date = start_date - datetime.timedelta(days=1)

seven_days_statistics = pd.DataFrame(date_list, columns=['День', 'Количество'])
fig = px.bar(seven_days_statistics, x='День', y='Количество', title='Количество упоминаний Кока-Кола ВК за 7 дней')
fig.show()

