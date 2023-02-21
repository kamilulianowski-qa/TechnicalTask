from selenium.webdriver.common.by import By

from pages.base.base_page import BasePage


class LoginPage(BasePage):
    @property
    def email_inp(self):
        return (By.CSS_SELECTOR, '[data-test="auth-login-email"]')

    @property
    def password_inp(self):
        return (By.CSS_SELECTOR, '[data-test="auth-login-password"]')

    @property
    def sign_in_btn(self):
        return (By.CSS_SELECTOR, '[data-test="auth-login-submit"]')

    def wait_for_page_load(self):
        self.wait_for_loader_finish()
        self.wait_until_visible(self.sign_in_btn)

    def login(self, email, password):
        self.send_keys(self.email_inp, email)
        self.send_keys(self.password_inp, password)
        self.click(self.sign_in_btn)
