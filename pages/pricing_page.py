from selenium.webdriver.common.by import By

from pages.base.base_page import BasePage


class PricingPage(BasePage):
    @property
    def continue_btn(self):
        return (By.CSS_SELECTOR, '[data-test="cart-plan-continue"]')

    def click_continue(self):
        self.click(self.continue_btn)