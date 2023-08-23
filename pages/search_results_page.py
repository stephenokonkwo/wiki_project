from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResultsPage(Page):
    SEARCH_INPUT = (By.CSS_SELECTOR, '#searchInput')
    PYTHON_TEXT = (By.CSS_SELECTOR, 'h1#firstHeading')

    def search_for_python(self, search_query):
        search_input = self.driver.find_element(*self.SEARCH_INPUT)
        search_input.clear()
        search_input.send_keys(search_query)
        search_input.send_keys(Keys.RETURN)
        # sleep(.5)

    def verify_search_results(self, expected_result):
        self.verify_element_text(expected_result, *self.PYTHON_TEXT)
        # sleep(.5)
