import pytest

from models.card import Card
from models.user import User


@pytest.fixture(scope="session")
def base_document():
    return 'CV - TEST'


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
