from selenium.webdriver.common.by import By

from pages.base_page import Page


class ProductSearch(Page):
    PRODUCT_PRICE = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")
    ADD_TO_CART = (By.XPATH, "//input[@id='add-to-cart-button']")

    def click(self):
        self.find_element(*self.PRODUCT_PRICE).click()

    def add_cart_icon(self):
        self.find_element(*self.ADD_TO_CART).click()
