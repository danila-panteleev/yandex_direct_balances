from yandex_direct_balances.source import (yandex_direct_balances,
                                           google_sheets_handler)
import time


if __name__ == '__main__':
    yandex_direct_balances.main()
    time.sleep(5)
    google_sheets_handler.main()