from pages.bestsellers_page import Bestsellers
from pages.header import Header
from pages.main_page import MainPage
from pages.search_results_page import SearchResults


class Application:

    def __init__(self, driver):
        self.driver = driver

        self.bestsellers_page = Bestsellers(self.driver)
        self.header = Header(self.driver)
        self.main_page = MainPage(self.driver)
        self.search_results_page = SearchResults(self.driver)
