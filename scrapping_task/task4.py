import matplotlib.pyplot as plt
import pandas as pd
from constants import Task3
from utils import get_engine


def complete_task_4(symbol: str = 'BTC-USD'):
    engine = get_engine()
    df = pd.read_sql(f'select month,min_rate,max_rate,standard from {Task3.TABLE_NAME.value} where symbol = "{symbol}"', con=engine)
    df.plot(x='month', y=['min_rate', 'max_rate', 'standard'], ylabel='exchange rate')
    plt.show(block=True)


if __name__ == '__main__':
    complete_task_4()
