import asyncio

import aiohttp
import pandas as pd
from constants import Task1
from utils import get_engine, get_headers, retrier


async def get_response() -> str:
    headers = get_headers(target_url=Task1.TARGET_URL.value)
    async with aiohttp.ClientSession(trust_env=True, headers=headers) as session:
        async with session.get(Task1.TARGET_URL.value) as resp:
            return await resp.text()


def get_normalized_dataframe_from_response() -> pd.DataFrame:
    response_text = asyncio.run(get_response())
    df = pd.read_html(response_text)[0]
    df['id'] = df.index
    df = df[['id', 'Symbol', 'Name']]
    df.columns = ['id', 'symbol', 'shortName']
    return df


@retrier
def complete_task_1() -> None:
    df = get_normalized_dataframe_from_response()
    df.to_sql(name=Task1.TABLE_NAME.value, index=False, con=get_engine(), if_exists='replace')


if __name__ == '__main__':
    complete_task_1()
