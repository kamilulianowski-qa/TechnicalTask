from pages.base.base_page import BasePage


class DashboardMainPage(BasePage):
    @property
    def get_cv_btn(self):
        return self.get_text_locator("Pobierz CV")

    def check_if_document_is_visible(self, text: str):
        return self.element_is_loaded(self.get_text_locator(text))

    def download_cv(self):
        self.click(self.get_cv_btn)
