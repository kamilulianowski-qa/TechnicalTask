import pytest


@pytest.fixture
def login_page(page_factory):
    return page_factory.get_page('login_page')


@pytest.fixture
def dashboard_main_page(page_factory):
    return page_factory.get_page('dashboard_main_page')


@pytest.fixture
def pricing_page(page_factory):
    return page_factory.get_page('pricing_page')


@pytest.fixture
def card_frame(page_factory):
    return page_factory.get_page('card_frame')


@pytest.fixture
def payment_status_page(page_factory):
    return page_factory.get_page('payment_status_page')
