import gspread
import yaml
import os
import sys


def main():
    gc = gspread.oauth()
    with open(os.path.join(os.path.dirname(sys.argv[0]), r'source/config/config.yml'), mode='r', encoding='utf-8') as config_file:
        config = yaml.safe_load(config_file)
    spreadsheet = config['spreadsheet']
    sheet = config['sheet']
    sh = gc.open(spreadsheet)

    worksheet = sh.worksheet(sheet)

    with open('balance_data_yandex.yml', 'r') as stream:
        balance_data = yaml.safe_load(stream)

    # update values from "Яндекс Директ" column
    for i in range(2, len(worksheet.get()) + 1):
        client_name = worksheet.get(f'A{i}')[0][0]
        balance = balance_data[client_name]
        worksheet.update(f'B{i}', balance)

    worksheet.update('G2', balance_data['Last update'])


if __name__ == '__main__':
    main()