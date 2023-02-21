import json
import os

import pytest

from models.card import Card
from models.user import User


def pytest_addoption(parser):
    parser.addoption("--headless", action="store", default='0')


@pytest.fixture(scope='session', autouse=True)
def read_pytest_options(request):
    os.environ["HEADLESS"] = request.config.getoption("--headless")


@pytest.fixture(scope='session')
def config():
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), f"config/test_env.json")) as f:
        return json.load(f)


@pytest.fixture(scope='session')
def base_url(config):
    return config['url']


@pytest.fixture(scope='session')
def base_user(config) -> User:
    return User(config['email'], config['password'])

@pytest.fixture(scope='session')
def invalid_card(config):
    card = config['invalid_card']

    return Card(
        card['number'],
        card['expiry_date'],
        card['cvc'],
        card['card_holder']
    )
