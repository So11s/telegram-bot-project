import requests
import time

from TOKEN import TOKEN

API_URL: str = "https://api.telegram.org/bot"
BOT_TOKEN: str = TOKEN
API_CATS: str = "https://meow.senither.com/v1/random"
ERROR_TEXT: str = "Здесь должна быть картинка с котом"

MAX_COUNTER: int = 100

offset: int = -2
counter: int = 0
chat_id: int

while counter < MAX_COUNTER:
    print(f"attempt = {counter}")
    updates = requests.get(f"{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}").json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            photo = requests.get(API_CATS)
            if photo.status_code == 200:
                CAT_LINK = photo.json()['data']['url']
                requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={CAT_LINK}')
            else:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={ERROR_TEXT}')

    time.sleep(1)
    counter += 1
