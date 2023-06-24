from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResultsPage(Page):
    RESULT_TEXT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
    BACKPACK_RESULT = (By.CSS_SELECTOR, 'span.a-price-whole')
    SEARCH_FILED = (By.ID, 'twotabsearchtextbox')
    SEARCH_BTN = (By.ID, 'nav-search-submit-button')
    BOOKS_SUBMENU = (By.CSS_SELECTOR, "a[aria-label= 'Books']")
    ALL_ELECTRONICS_SUBMENU = (By.CSS_SELECTOR, "a[aria-label= 'All Electronics']")

    def verify_search_results(self, expected_result):
        self.verify_element_text(expected_result, *self.RESULT_TEXT)

    def click_search_item(self, ):
        self.find_element(*self.BACKPACK_RESULT).click()

    def verify_dept(self):
        self.wait_for_element_appear(*self.BOOKS_SUBMENU)

    def verify_all_electronic_dept(self):
        self.wait_for_element_appear(*self.ALL_ELECTRONICS_SUBMENU)
