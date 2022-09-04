import time

from constants import db_name
from selenium.webdriver.chrome.service import Service as ChromeService
from seleniumwire import webdriver
from seleniumwire.request import HTTPHeaders
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from webdriver_manager.chrome import ChromeDriverManager

ENGINE: Engine | None = None


def get_engine() -> Engine:
    global ENGINE
    if not ENGINE:
        ENGINE = create_engine(f'sqlite:///{db_name}', echo=False)
    return ENGINE


def get_headers(target_url: str) -> HTTPHeaders:
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.get(target_url)
    request = driver.requests[-1]
    headers = request.headers
    driver.quit()
    return headers


def get_pair_names_list() -> list[str]:
    engine = get_engine()
    with engine.connect() as connection:
        result = connection.execute('select id,symbol from currency')
        return result.fetchall()


# Decorator
def retrier(func):
    def wrapper(*args, **kwargs):
        for _ in range(5):
            try:
                return func(*args, **kwargs)
            except Exception:
                time.sleep(2)
                continue
        exit(1)

    return wrapper
