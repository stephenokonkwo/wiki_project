from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


class ProductPage(Page):
    NEW_ARRIVALS_TAB = (By.XPATH, "//span[@class='nav-a-content' and contains(text(), 'New Arrivals')]")
    MEN_SUB_OPTION = (By.XPATH, "//ul[@class='mm-category-list']//h3[contains(text(), 'Men')]")

    def open_amazon_fashion_page(self):
        self.open_url('https://www.amazon.com/gp/product/B074TBCSC8')

    def hover_new_arrival(self):
        new_arrival_opt = self.find_element(*self.NEW_ARRIVALS_TAB)
        actions = ActionChains(self.driver)
        actions.move_to_element(new_arrival_opt)
        actions.perform()

    def verify_men_option(self):
        self.wait_for_element_appear(*self.MEN_SUB_OPTION)
