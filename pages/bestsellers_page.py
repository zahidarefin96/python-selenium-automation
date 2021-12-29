from selenium.webdriver.common.by import By

from pages.base_page import Page


class Bestsellers(Page):
    TOP_LINKS = (By.CSS_SELECTOR, "#zg_header a")
    HEADER = (By.CSS_SELECTOR, "#zg_banner_text")

    def open(self):
        self.open_page(end_url="gp/bestsellers/")

    def click_thru_top(self):
        top_links = self.driver.find_elements(*self.TOP_LINKS)

        for x in range(len(top_links)):
            link = self.driver.find_elements(*self.TOP_LINKS)[x]
            link_text = link.text
            link.click()

            header_text = self.driver.find_element(*self.HEADER).text
            assert link_text in header_text, f"Expected {link_text} not in {header_text}"
