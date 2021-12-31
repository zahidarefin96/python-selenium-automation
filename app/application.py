from pages.bestsellers_page import Bestsellers
from pages.cart_page import Cart
from pages.header import Header
from pages.main_page import MainPage
from pages.product_search_page import ProductSearch
from pages.search_results_page import SearchResults
from pages.sign_in_page import SignInPage


class Application:

    def __init__(self, driver):
        self.driver = driver

        self.bestsellers_page = Bestsellers(self.driver)
        self.cart_page = Cart(self.driver)
        self.header = Header(self.driver)
        self.main_page = MainPage(self.driver)
        self.product_search_page = ProductSearch(self.driver)
        self.search_results_page = SearchResults(self.driver)
        self.sign_in_page = SignInPage(self.driver)
