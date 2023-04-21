import requests
from TOKEN import TOKEN
from pprint import pprint

response = requests.get(f"https://api.telegram.org/bot{TOKEN}/getUpdates")
pprint(response.json())
