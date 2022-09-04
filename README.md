## Project structure
```
├── Makefile
├── README.rst
├── mydb.db # Will be generated after task 1 execution
├── poetry.lock
├── pyproject.toml
├── requirements.txt
├── scrapping_task
│   ├── __init__.py
│   ├── constants.py
│   ├── task1.py
│   ├── task2.py
│   ├── task3.py
│   ├── task4.py
│   ├── task5.py
│   └── utils.py
├── setup.cfg
├── task5.csv # Will be generated after task 5 execution
└── tests
    ├── __init__.py
    └── test_scrapping_task.py
```
## Installation and running

Clone repository 

```sh
git clone https://github.com/denek98/scrapping_task
```
Install the dependencies using poetry
```sh
cd scrapping_task
poetry install
```
or using requirements.txt file
```sh
cd scrapping_task
pip install -r requirements.txt
```
All following tasks should be run one by one. The order is **important**!
## Task 1
### Conditions
> Scrape top 100 crypto currencies (with highest "Market Cap") from https://finance.yahoo.com/cryptocurrencies and load data into table currency ("id": xxx, "symbol":"BTC-USD","shortName":"Bitcoin USD")
### Usage
Run command
```sh
make task_1
```
or
```
python scrapping_task/task1.py
```
### Result
Table named **currency** with top 100 currencies info will be created (or updated)  
```If this is the first run, SQLite database named mydb.db will be created in the root directory of the project```
## Task 2
### Conditions
> For each currency scrape exchange rates ("Adj Close") for the last year (01 September 2021 - 31 August 2022) from https://finance.yahoo.com/quote/BTC-USD/history and load into table exchange_rate ("currency_id": xxx, "date": 01-09-2022, "exchange_rate": 20068.56)
### Usage
Run command
```sh
make task_2
```
or
```
python scrapping_task/task2.py
```
### Result
Table named **exchange_rate** with top 100 currencies info will be created (or updated)  
## Task 3
### Conditions
> For each currency calculate in each month min, max and standard deviation of exchange rate values. Store it into statistics table
### Usage
Run command
```sh
make task_3
```
or
```
python scrapping_task/task3.py
```
### Result
Table named **statistics** with top 100 currencies info will be created (or updated)  
## Task 4
### Conditions
> Develop a function that, based on the previously stored data, displays a graph of min, max and standard deviation values of the last year, taking crypto currency symbol as a parameter.
### Usage
Run command
```sh
make task_4
```
or
```
python scrapping_task/task4.py
```
### Result
The graph will be displayed
## Task 5
### Conditions
> Develop a function that generates csv file containing following data: currency symbol, currency short name, min exchange rate of the whole dataset, min exchange rate date, max exchange rate of the whole dataset and max exchange rate date.
### Usage
Run command
```sh
make task_5
```
or
```
python scrapping_task/task5.py
```
### Result
CSV file will be generated in the root directory of the project
