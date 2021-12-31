from selenium.webdriver.common.by import By

from pages.base_page import Page


class Header(Page):
    SEARCH_INPUT = (By.ID, "twotabsearchtextbox")
    SEARCH_ICON = (By.ID, "nav-search-submit-button")
    RETURN_ORDER_LINK = (By.XPATH, "//a[@id='nav-orders']")
    CART_ICON = (By.ID, "nav-cart")

    def search_input(self, text):
        self.input_text(text, *self.SEARCH_INPUT)

    def click_search(self):
        self.click(*self.SEARCH_ICON)

    def click_return_order(self):
        self.click(*self.RETURN_ORDER_LINK)

    def click_cart(self):
        self.click(*self.CART_ICON)
