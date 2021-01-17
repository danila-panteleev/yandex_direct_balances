import yaml
import os
import sys
import data_handler as dh
import email_handler as eh

script_path = os.path.dirname(sys.argv[0])

with open(os.path.join(script_path, r'config/config.yml'), 'r', encoding='utf-8') as stream:
    data_loaded = yaml.safe_load(stream)

access_tokens = data_loaded['token']  # dict
logins = data_loaded['login']  # dict
email_user = data_loaded['email_user']
email_password = data_loaded['email_password']
email_receiver = data_loaded['receiver']

if __name__ == '__main__':
    balances = {}
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

    email_body = data_loaded['email_body']

    # for client in balances:
    #     email_body = email_body + f'{client}: {balances[client]} руб.\n '
    #
    # eh.email_wrapper(email_user, email_password, email_receiver,
    #                  subject='Балансы клиентов Яндекс Директ',
    #                  body=email_body)

    with open('balance_data_yandex.yml', 'w') as balances_dump_file:
        yaml.safe_dump(balances, balances_dump_file)