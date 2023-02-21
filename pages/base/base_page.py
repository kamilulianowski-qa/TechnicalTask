import time

from selenium.common import ElementClickInterceptedException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    DEFAULT_TIMEOUT = 15

    def __init__(self, driver):
        self.driver = driver

    @property
    def accept_cookies_btn(self):
        return (By.CSS_SELECTOR, '[data-test="accept-cookies-button"]')

    @property
    def loader(self):
        return (By.CSS_SELECTOR, '.init-loader-circle')

    def accept_cookies(self):
        self.click(self.accept_cookies_btn)

    def get_text_locator(self, text):
        return (By.XPATH, f"//*[contains(text(), '{text}')]")

    def click(self, locator, timeout=DEFAULT_TIMEOUT):
        try:
            WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator)).click()
        except ElementClickInterceptedException:
            #try again if interrupted
            time.sleep(0.3)
            WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator)).click()

    def send_keys(self, locator, text, timeout=DEFAULT_TIMEOUT):
        self.ensure_input_is_empty(locator)
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator)).send_keys(text)

    def slow_send_keys(self, locator, text):
        time.sleep(0.3)
        self.ensure_input_is_empty(locator)
        self.send_keys(locator, text)
        time.sleep(0.3)

    def ensure_input_is_empty(self, locator, timeout=DEFAULT_TIMEOUT):
        element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        element.clear()
        while element.get_attribute("value") != "":
            element.send_keys(Keys.BACKSPACE)

    def get_element(self, locator, timeout=DEFAULT_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def get_text(self, locator, timeout=DEFAULT_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator)).get_attribute(
            "innerText")

    def wait_until_visible(self, locator, timeout=DEFAULT_TIMEOUT):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def wait_until_invisible(self, locator, timeout=DEFAULT_TIMEOUT):
        WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def switch_to_iframe(self, locator, timeout=DEFAULT_TIMEOUT):
        WebDriverWait(self.driver, timeout).until(EC.frame_to_be_available_and_switch_to_it(locator))

    def switch_to_base_frame(self):
        self.driver.switch_to.default_content()

    def wait_for_loader_finish(self):
        self.wait_until_invisible(self.loader)

    def element_is_loaded(self, locator):
        try:
            self.wait_until_visible(locator)
            return True
        except Exception as e:
            return False
