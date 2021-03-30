# Балансы Яндекс Директ
Получение баланса(ов) аккаунта(ов) Яндекс Директ и отправка информации на e-mail
### Как пользоваться:
1. Создайте папку yandex_direct_balances
2. Внутри папки ```git clone https://github.com/danila-panteleev/yandex_direct_balances.git```
3. ```pip install -r requirements.txt``` 
4. Введите нужные настройки в [config_example.yml](source/config/config_example.yml)
5. Переименуйте config_example.yml в config.yml
6. Запустите yandex_direct_balances.py

### Фичи:
- возможность получить данные с нескольких аккаунтов (пример в [конфиге](source/config/config_example.yml))
- отправка данных по e-mail
- отравка данных в таблицу Google Sheets 
(обязательно наличие тестового доступа в [Google API Console](https://console.cloud.google.com/) как минимум)

### Предупреждение
- отправка писем работает только из-под аккаунта Gmail, в настройках безопасности которого 
[разрешен доступ ненадежных приложений](https://support.google.com/accounts/answer/6010255?hl=ru)