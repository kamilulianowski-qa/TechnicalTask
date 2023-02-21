import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from pages.base.page_factory import PageFactory


@pytest.fixture
def default_timeout(config):
    return config['default_timeout']


@pytest.fixture()
def ui_browser(base_url):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(base_url)

    yield driver
    driver.quit()


@pytest.fixture
def page_factory(ui_browser):
    return PageFactory(ui_browser)
