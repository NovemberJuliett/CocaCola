import requests
import os
from dotenv import load_dotenv
import datetime
import plotly.express as px
import pandas as pd
import argparse


def main():
    load_dotenv()
    token = os.environ["TOKEN"]

    start_date = datetime.date.today()
    start_date_time = datetime.datetime(start_date.year, start_date.month, start_date.day)
    date_list = []

    parser = argparse.ArgumentParser(description="Put here the number of days")
    parser.add_argument("--number_of_days", type=int)
    args = parser.parse_args()

    for day in range(args.number_of_days):
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
        all_mentions = response.json()
        mentions_content = all_mentions.values()
        for item in mentions_content:
            item_count = item["count"]
        date_tuple = tuple((start_date, item_count))
        date_list.append(date_tuple)
        start_date = start_date - datetime.timedelta(days=1)

    seven_days_statistics = pd.DataFrame(date_list, columns=['День', 'Количество'])
    fig = px.bar(seven_days_statistics, x='День', y='Количество',
                 title='Количество упоминаний Кока-Кола ВК за {} дней'.format(args.number_of_days))
    fig.show()


if __name__ == '__main__':
    main()
