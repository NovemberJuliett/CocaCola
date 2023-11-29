import requests


params = {
        "q": "Кока-Кола",
        "access_token": "aab36c77aab36c77aab36c770aa9a51addaaab3aab36c77cfd55b3447a5a9eab522c07e",
        "v": "5.199"
    }
response = requests.get("https://api.vk.com/method/newsfeed.search", params=params)
response.raise_for_status()
result = response.json()
print(result)