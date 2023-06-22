from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


class Header(Page):
    SEARCH_FILED = (By.ID, 'twotabsearchtextbox')
    SEARCH_BTN = (By.ID, 'nav-search-submit-button')
    ORDERS_BTN = (By.ID, 'nav-orders')
    CART_BTN = (By.CSS_SELECTOR, '#nav-cart-count-container')
    LANG_OPTIONS = (By.ID, 'icp-nav-flyout')
    SPANISH_LANG = (By.CSS_SELECTOR, "a[href= '#switch-lang=es_US']")
    DEPT_SELECT = (By.ID, 'searchDropdownBox')

    def search_for_product(self, search_query):
        self.input_text(search_query, *self.SEARCH_FILED)
        self.click(*self.SEARCH_BTN)

    def click_orders(self, ):
        self.click(*self.ORDERS_BTN)

    def hover_lang(self):
        lang_options = self.find_element(*self.LANG_OPTIONS)
        actions = ActionChains(self.driver)
        actions.move_to_element(lang_options)
        actions.perform()

    def verify_spanish_option(self):
        self.wait_for_element_appear(*self.SPANISH_LANG)

    def select_dept(self):
        dept_select = self.find_element(*self.DEPT_SELECT)
        select = Select(dept_select)
        select.select_by_value('search-alias=stripbooks')
