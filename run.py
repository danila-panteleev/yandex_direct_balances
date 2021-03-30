from source import (yandex_direct_balances,
                    google_sheets_handler)
import time
import logging


logging.basicConfig(filename='.log', filemode='a', level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


if __name__ == '__main__':
    yandex_direct_balances.main()
    time.sleep(5)
    google_sheets_handler.main()