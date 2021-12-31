from selenium.webdriver.common.by import By

from pages.base_page import Page


class SignInPage(Page):
    SIGN_IN = (By.XPATH, "//h1[contains(text(),'Sign-In')]")

    def verify_search_result(self, expected_text):
        self.verify_text(expected_text, *self.SIGN_IN)
