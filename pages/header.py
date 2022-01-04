from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from pages.base_page import Page


class Header(Page):
    SEARCH_INPUT = (By.ID, "twotabsearchtextbox")
    SEARCH_ICON = (By.ID, "nav-search-submit-button")
    RETURN_ORDER_LINK = (By.XPATH, "//a[@id='nav-orders']")
    CART_ICON = (By.ID, "nav-cart")
    FLAG = (By.CSS_SELECTOR, ".icp-nav-flag.icp-nav-flag-us")
    SPANISH_LANG = (By.CSS_SELECTOR, "[href='#switch-lang=es_US']")
    DEPARTMENT_DROPDOWN = (By.ID, "searchDropdownBox")
    NEW_ARRIVALS_LINK = (By.XPATH, "//span[contains(text(),'New Arrivals')]")

    def search_input(self, text):
        self.input_text(text, *self.SEARCH_INPUT)

    def click_search(self):
        self.click(*self.SEARCH_ICON)

    def click_return_order(self):
        self.click(*self.RETURN_ORDER_LINK)

    def click_cart(self):
        self.click(*self.CART_ICON)

    def hover_lang(self):
        flag = self.find_element(*self.FLAG)
        actions = ActionChains(self.driver)
        actions.move_to_element(flag)
        actions.perform()

    def hover_new_arrivals_link(self):
        flag = self.find_element(*self.NEW_ARRIVALS_LINK)
        actions = ActionChains(self.driver)
        actions.move_to_element(flag)
        actions.perform()

    def verify_spanish_language_present(self):
        self.wait_for_element_appear(*self.SPANISH_LANG)

    def select_department(self, department: str):
        dropdown = self.find_element(*self.DEPARTMENT_DROPDOWN)
        select = Select(dropdown)
        select.select_by_value(f'search-alias={department}')
