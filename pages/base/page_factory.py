from pages.base.base_page import BasePage
from pages.card_frame import CardFrame
from pages.dashboard_main_page import DashboardMainPage
from pages.login_page import LoginPage
from pages.payment_status_page import PaymentStatusPage
from pages.pricing_page import PricingPage


class PageFactory:
    def __init__(self, driver):
        self.driver = driver
        self.pages = {
            'login_page': LoginPage,
            'dashboard_main_page': DashboardMainPage,
            'pricing_page': PricingPage,
            'card_frame': CardFrame,
            'payment_status_page': PaymentStatusPage
        }
        self.instances = {}

    def get_page(self, page: str) -> 'BasePage':
        if page not in self.instances:
            self.instances[page] = self.pages[page](self.driver)
        return self.instances[page]
