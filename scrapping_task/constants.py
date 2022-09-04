from enum import Enum

db_name = 'mydb.db'


class Task1(Enum):
    TABLE_NAME = 'currency'
    TARGET_URL = 'https://finance.yahoo.com/cryptocurrencies?offset=0&count=100&guccounter=1'


class Task2(Enum):
    TABLE_NAME = 'exchange_rate'
    TARGET_URL = 'https://finance.yahoo.com/quote/{0}/history?period1={1}&period2={2}'
    START_DATE = '2021-09-01'
    END_DATE = '2022-08-31'


class Task3(Enum):
    TABLE_NAME = 'statistics'


class Task5(Enum):
    FILE_NAME = 'task5.csv'
