from time import sleep
from selenium.webdriver.common.by import By
from pages.base_page import Page


class MainPage(Page):
    SEARCH_INPUT = (By.CSS_SELECTOR, '#searchInput')


    def open_main_page(self):
        self.open_url('https://www.wikipedia.org/')

    def locate_search_input(self):
        self.find_element(*self.SEARCH_INPUT)
        # sleep(.5)
