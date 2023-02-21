import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from pages.base.page_factory import PageFactory


@pytest.fixture
def default_timeout(config):
    return config['default_timeout']


@pytest.fixture()
def ui_browser(request, base_url):
    if request.config.getoption("--browser") == 'chrome':
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif request.config.getoption("--browser") == 'firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    driver.get(base_url)

    yield driver
    driver.quit()


@pytest.fixture
def page_factory(ui_browser):
    return PageFactory(ui_browser)
