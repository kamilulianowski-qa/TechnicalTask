from selenium.webdriver.common.by import By

from pages.base.base_page import BasePage


class PaymentStatusPage(BasePage):
    @property
    def back_to_payment_methods(self):
        return (By.CSS_SELECTOR, 'a[href="/cart/payment-details"]')

    @property
    def something_is_wrong_msg(self):
        return self.get_text_locator("Coś poszło nie tak z Twoją płatnością")

    @property
    def payment_fail_reason(self):
        return self.get_text_locator("Twoja płatność nie mogła zostać zrealizowana.")

    def invalid_payment_page_is_displayed_correctly(self):
        expected_texts = [
            "Coś poszło nie tak z Twoją płatnością",
            "Twoja płatność nie mogła zostać zrealizowana.",
            "Sprawdź swoje dane do płatności lub spróbuj jeszcze raz inną metodą płatności."
        ]
        for text in expected_texts:
            if not self.element_is_loaded(self.get_text_locator(text)):
                return False
        return self.element_is_loaded(self.back_to_payment_methods)

