import os
import requests
from pprint import pprint as pp

def sendMessage (token, msg='') :
    chat_id=getID(token)
    requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={msg}")
    print(f"{msg}를 {chat_id}님에게 보냈었습니다")

def getID(token):
    return requests.get(f"https://api.telegram.org/bot{token}/getUpdates").json()['result'][0]['message']['chat']['id']

token = os.getenv('TELEGRAM_TOKEN')

sendMessage(token,input())
