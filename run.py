import time
import logging
import os
import sys
import argparse
import yaml
from source.yandex_direct_balances import yandex_direct_balances_with_data
from source.google_sheets_handler import google_sheets_receiver
from source.yaml_handler import load_yaml, safe_balance_data
from source.email_handler import email_receiver

logging.basicConfig(filename='.log', filemode='a', level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

script_path = os.path.dirname(sys.argv[0])
config_path = r'source/config/config.yml'
balance_data_path = r'balance_data_yandex.yml'

config = load_yaml(script_path, config_path)

# yandex direct
tokens = config['token']
logins = config['login']

# email
email_user = config['email_user']
email_password = config['email_password']
email_body = config['email_body']
receiver = config['receiver']

# google spreadsheets
spreadsheet = config['spreadsheet']
sheet = config['sheet']


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-g', action='store_true')  # use google sheet
    parser.add_argument('-e', action='store_true')  # use email receiver
    args = parser.parse_args()

    balances = yandex_direct_balances_with_data(tokens, logins)
    safe_balance_data(balances)  # just for debugging
    if args.g:
        google_sheets_receiver(spreadsheet, sheet, balances)
    if args.e:
        email_receiver(email_user,
                       email_password,
                       receiver,
                       subject="Балансы Яндекс Директ",
                       body=email_body,
                       balances=balances)


if __name__ == '__main__':
    main()