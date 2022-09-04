from constants import Task1, Task2, Task3
from utils import get_engine


def complete_task_3():
    engine = get_engine()
    with engine.connect() as connection:
        connection.execute(
            f'''
            DROP TABLE IF EXISTS {Task3.TABLE_NAME.value}
            '''
        )
        connection.execute(
            f"CREATE TABLE {Task3.TABLE_NAME.value} AS "
            f"SELECT r.*,shortName,symbol FROM {Task1.TABLE_NAME.value} LEFT JOIN "
            f"(SELECT id,strftime('%Y-%m', date) AS month, CAST(MIN(exchange_rate) AS integer) AS min_rate, CAST(MAX(exchange_rate) AS integer) AS max_rate, CAST(AVG(exchange_rate) AS integer) AS standard from "  # noqa: E501
            f"{Task2.TABLE_NAME.value} GROUP BY STRFTIME('%Y-%m', date), id) AS r ON currency.id = r.id"
        )


if __name__ == '__main__':
    complete_task_3()
