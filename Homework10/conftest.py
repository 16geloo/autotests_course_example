from datetime import datetime
import pytest


@pytest.fixture(scope='class')
def class_timer():
    print(f'\nНачало класса: {datetime.now().strftime("%H:%M:%S")}')
    yield
    print(f'\nКонец класса: {datetime.now().strftime("%H:%M:%S")}')


@pytest.fixture()
def test_timer():
    start = datetime.now()
    yield
    end = datetime.now()
    print(f'\nВремя теста: {end - start}')
