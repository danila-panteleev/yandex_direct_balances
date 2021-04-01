import yaml
from os import path
from typing import Dict, AnyStr
from datetime import date


def load_yaml(script_path: AnyStr, file_path: AnyStr) -> Dict:
    with open(path.join(script_path, file_path), mode='r', encoding='utf-8') as stream:
        result = yaml.safe_load(stream)

    return result


def safe_balance_data(balances: Dict[AnyStr, AnyStr]) -> None:
    with open('balance_data_yandex.yml', 'w', encoding='utf-8') as balances_dump_file:
        yaml.safe_dump(balances, balances_dump_file)