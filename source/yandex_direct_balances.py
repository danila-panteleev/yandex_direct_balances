import yaml
import os
import sys
from source import data_handler as dh
from datetime import date


def main():
    script_path = os.path.dirname(sys.argv[0])

    with open(os.path.join(script_path, r'source/config/config.yml'), 'r', encoding='utf-8') as stream:
        data_loaded = yaml.safe_load(stream)

    access_tokens = data_loaded['token']
    logins = data_loaded['login']

    balances = {}
    date_today = date.today().strftime('%d.%m.%Y')
    for i in range(len(access_tokens)):
        account = list(access_tokens[i].keys())[0]
        token = access_tokens[i][account]
        clients = logins[i][account]
        for client in clients:
            client_name = list(client.keys())[0]
            client_login = client[client_name]
            account_data = dh.get_account_data(logins=[client_login], token=token)
            balance_data = dh.get_balance_data(account_data)
            balances.update({client_name: list(balance_data.values())[0]})

    with open('balance_data_yandex.yml', 'w') as balances_dump_file:
        dump_data = balances.copy()
        dump_data.update({'Last update': date_today})
        yaml.safe_dump(dump_data, balances_dump_file)

    return None


if __name__ == '__main__':
    main()