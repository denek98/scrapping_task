import asyncio
import time
from datetime import datetime

import aiohttp
import pandas as pd
from constants import Task1, Task2
from utils import get_engine, get_headers, get_pair_names_list, retrier


def split_dates(start_date: str = Task2.START_DATE.value, end_date: str = Task2.END_DATE.value, chunk_size: int = 90) -> list[list[int]]:
    d1 = datetime.strptime(start_date, "%Y-%m-%d").timetuple()
    d2 = datetime.strptime(end_date, "%Y-%m-%d").timetuple()

    d1_timestamp = int(time.mktime(d1))
    d2_timestamp = int(time.mktime(d2))

    intervals = []
    days90inseconds = chunk_size * 24 * 60 * 60
    i = d1_timestamp
    while i <= d2_timestamp:
        if d2_timestamp - i >= days90inseconds:
            intervals.append([i, i + days90inseconds])
        else:
            intervals.append([i, d2_timestamp])
        i += days90inseconds
    return intervals


async def get_df_from_link(headers, parametrized_link: str, currency_id: int) -> pd.DataFrame:
    async with aiohttp.ClientSession(trust_env=True, headers=headers) as session:
        async with session.get(parametrized_link) as resp:
            df = pd.read_html(await resp.text())[0].iloc[:-1]
            df['id'] = currency_id
            return df


def parametrize_link(pair_name: str, start_date: int, end_date: int) -> str:
    return Task2.TARGET_URL.value.format(pair_name, start_date, end_date)


async def parse_all_links() -> list:
    headers = get_headers(target_url=Task1.TARGET_URL.value)
    pair_names = get_pair_names_list()
    date_list = split_dates()
    tasks = []
    for id, pair_name in pair_names:
        for date_interval in date_list:
            link = parametrize_link(pair_name=pair_name, start_date=date_interval[0], end_date=date_interval[1])
            tasks.append(get_df_from_link(headers=headers, parametrized_link=link, currency_id=id))
    return await asyncio.gather(*tasks)


def concat_and_normalize_list_of_dfs(list_of_dfs: list[pd.DataFrame]) -> pd.DataFrame:
    df = pd.concat(list_of_dfs)
    df = df[['id', 'Date', 'Adj Close**']]
    df['Date'] = df['Date'].apply(pd.to_datetime)
    df.columns = ['id', 'date', 'exchange_rate']
    df.drop_duplicates(inplace=True)
    df.sort_values(by='id')
    return df


@retrier
def complete_task_2() -> None:
    df_list = asyncio.run(parse_all_links())
    df = concat_and_normalize_list_of_dfs(list_of_dfs=df_list)
    df.to_sql(name=Task2.TABLE_NAME.value, index=False, con=get_engine(), if_exists='replace')


if __name__ == '__main__':
    complete_task_2()
