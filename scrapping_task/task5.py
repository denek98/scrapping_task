import pandas as pd
from constants import Task1, Task2, Task5
from utils import get_engine


def complete_task_5():
    engine = get_engine()
    df = pd.read_sql(
        f"SELECT symbol,shortName,min_rate,min_rate_date,max_rate,max_rate_date FROM {Task1.TABLE_NAME.value} LEFT JOIN "
        "(SELECT min_r.id,min_rate,min_rate_date,max_rate,max_rate_date FROM "
        f"(SELECT id,exchange_rate AS min_rate, date AS min_rate_date FROM {Task2.TABLE_NAME.value} GROUP BY id having exchange_rate = MIN(exchange_rate)) AS min_r LEFT JOIN "  # noqa: E501
        f"(SELECT id,exchange_rate AS max_rate, date AS max_rate_date FROM {Task2.TABLE_NAME.value} GROUP BY id having exchange_rate = MAX(exchange_rate)) AS max_r "
        "on min_r.id = max_r.id) AS r "
        "on currency.id = r.id",
        con=engine,
    )
    df.to_csv(Task5.FILE_NAME.value, index=False)


if __name__ == '__main__':
    complete_task_5()
