import requests
import os
from dotenv import load_dotenv

load_dotenv()

token = os.environ["TOKEN"]
params = {
        "q": "Кока-Кола",
        "access_token": token,
        "v": "5.199"
    }
response = requests.get("https://api.vk.com/method/newsfeed.search", params=params)
response.raise_for_status()
result = response.json()
print(result.keys)
