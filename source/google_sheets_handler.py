import gspread
from typing import AnyStr, Dict


def google_sheets_receiver(spreadsheet: AnyStr, sheet: AnyStr, balances: Dict[AnyStr, AnyStr]) -> None:
    gc = gspread.oauth()
    sh = gc.open(spreadsheet)
    worksheet = sh.worksheet(sheet)
    balances = balances.copy()
    last_update = balances.pop('Last update')

    # update values from "Яндекс Директ" column
    client_names = sorted(balances.keys())
    for i in range(len(client_names)):
        client_name = client_names[i]
        balance = [balances[client_name]][0]
        if worksheet.findall(client_name):
            row_index = worksheet.findall(client_name)[0].row
            worksheet.update(f'B{row_index}', balance)
        else:
            row = client_name, balance
            worksheet.append_row(row)

    worksheet.update('G2', last_update)

    return None