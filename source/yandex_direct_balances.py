import yaml
import os
import sys
import data_handler as dh

script_path = os.path.dirname(sys.argv[0])

with open(os.path.join(script_path, r'config.yml'), 'r', encoding='utf-8') as stream:
    data_loaded = yaml.safe_load(stream)

ACCESS_TOKEN = data_loaded['token']
LOGIN = data_loaded['login']

if __name__ == '__main__':
    account_data = dh.get_account_data(logins=LOGIN, token=ACCESS_TOKEN)
    balance_data = dh.get_balance_data(account_data)
    print(balance_data)