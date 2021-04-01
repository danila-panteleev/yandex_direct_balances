# -*- coding: utf-8 -*-
# coding=utf-8
from typing import AnyStr, List, Dict
from source.data_handler import (get_account_data,
                                 get_balance_data)
from datetime import date


def yandex_direct_balances_with_data(tokens: List[AnyStr], logins: List[AnyStr]) -> Dict[AnyStr, AnyStr]:
    balances = {}
    date_today = date.today().strftime('%d.%m.%Y')

    for i in range(len(tokens)):
        account = list(tokens[i].keys())[0]
        token = tokens[i][account]
        clients = logins[i][account]
        for client in clients:
            client_name = list(client.keys())[0]
            client_login = client[client_name]
            account_data = get_account_data(logins=[client_login], token=token)
            balance_data = get_balance_data(account_data)
            balances.update({client_name: list(balance_data.values())[0]})

    balances.update({'Last update': date_today})

    return balances
