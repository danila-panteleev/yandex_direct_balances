# -*- coding: utf-8 -*-
# coding=utf-8
import json
import requests
from typing import List


def get_account_data(token: str, logins: List[str]) -> List[dict]:
    # адрес для отправки json-запросов
    url = 'https://api.direct.yandex.ru/live/v4/json/'

    # структура входных данных (словарь)
    data = {
        "method": "AccountManagement",
        "token": token,
        "param": {
            "SelectionCriteria": {
                "Logins": logins,
            },
            "Action": "Get",
        }
    }

    headers = {
        'Host': 'api.direct.yandex.com',
        'Authorization': f'Bearer {token}',
        'Accept-Language': 'ru',
        'Content-Type': 'application/json; charset=utf-8',
    }

    # конвертировать словарь в JSON-формат и перекодировать в UTF-8
    jdata = json.dumps(data, ensure_ascii=False)
    jdata = jdata.encode('utf-8')

    # выполнить запрос
    response = requests.post(url, data=jdata, headers=headers)

    result = response.content.decode('utf8')

    return dict(json.loads(result))['data']['Accounts']


def get_balance_data(account_data: List[dict]) -> dict:
    balance_data = {}
    for account in account_data:
        balance_data.update({account['Login']: account['Amount']})
    return balance_data
