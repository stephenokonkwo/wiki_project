from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page


class CartPage(Page):
    CART_EMPTY = (By.CSS_SELECTOR, 'div.a-row.sc-your-amazon-cart-is-empty')
    BACKPACK_IMG_CART = (By.CSS_SELECTOR, "img[src*= 'https://m.media-amazon.com/images/I/81OFxhFWmML._AC']")
    GO_TO_CART_BTN = (By.CSS_SELECTOR, "#sw-gtc")
    ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
    ITEM_TITLE = (By.CSS_SELECTOR, 'span.a-truncate.sc-grid-item-product-title.a-size-base-plus')

    def verify_amazon_cart_is_empty(self):
        self.driver.wait.until(EC.url_contains('https://www.amazon.com/gp/cart/view.html?ref_=nav_cart'))
        self.verify_element_text('Your Amazon Cart is empty', *self.CART_EMPTY)

    def add_item_to_cart(self):
        self.find_element(*self.ADD_TO_CART_BTN).click()

    def click_go_to_cart_btn(self):
        self.find_element(*self.GO_TO_CART_BTN).click()

    def verify_item_in_cart(self):
        self.verify_partial_text('Backpack', *self.ITEM_TITLE)
