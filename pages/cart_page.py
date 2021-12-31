from selenium.webdriver.common.by import By

from pages.base_page import Page


class Cart(Page):
    ITEM_COUNT = (By.XPATH, "//span[@id='sc-subtotal-label-activecart']")

    AMAZON_CART_EMPTY_TEXT = (By.XPATH, "//h2[contains(text(),'Your Amazon Cart is empty')]")

    def verify_search_result(self, expected_text):
        self.verify_text(expected_text, *self.ITEM_COUNT)

    def verify_cart_empty_text(self, expected_text):
        self.verify_text(expected_text, *self.AMAZON_CART_EMPTY_TEXT)
