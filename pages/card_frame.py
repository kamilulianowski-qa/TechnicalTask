from selenium.webdriver.common.by import By

from models.card import Card
from pages.base.base_page import BasePage


class CardFrame(BasePage):
    @property
    def payment_iframe(self):
        return (By.ID, 'ccframe')

    @property
    def card_number_inp(self):
        return (By.ID, 'ccNum')

    @property
    def card_expiration_inp(self):
        return (By.CSS_SELECTOR, '[name="expirationDate"]')

    @property
    def card_cvv_inp(self):
        return (By.ID, 'ccCVV')

    @property
    def name_and_surname_inp(self):
        return (By.CSS_SELECTOR, '[name="cardholderName"]')

    @property
    def pay_btn(self):
        return (By.CSS_SELECTOR, '[data-test="cart-pay-securely"]')

    def fill_form(self, card: Card):
        self.switch_to_iframe(self.payment_iframe)
        self.send_keys(self.card_number_inp, card.number)
        self.slow_send_keys(self.card_cvv_inp, card.cvv)
        self.switch_to_base_frame()
        self.send_keys(self.card_expiration_inp, card.expiry_date)
        self.slow_send_keys(self.name_and_surname_inp, card.card_holder)

    def submit(self):
        self.click(self.pay_btn)