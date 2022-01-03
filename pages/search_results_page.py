from selenium.webdriver.common.by import By

from pages.base_page import Page


class SearchResults(Page):
    SEARCH_RESULT = (By.XPATH, "//span[@class= 'a-color-state a-text-bold']")
    SUB_NAV = (By.CSS_SELECTOR, "#nav-subnav[data-category='{CATEGORY}'")

    def _get_category_locator(self, category):
        return [self.SUB_NAV[0], self.SUB_NAV[1].replace('{CATEGORY}', category)]

    def verify_search_result(self, expected_text):
        self.verify_text(expected_text, *self.SEARCH_RESULT)

    def verify_correct_department(self, category):
        locator = self._get_category_locator(category)
        self.wait_for_element_appear(*locator)
