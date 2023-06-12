from selenium.webdriver.common.by import By
from behave import given, when, then

ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
GO_TO_CART_BTN = (By.CSS_SELECTOR, "#sw-gtc")


# When
@when('Click add to cart')
def add_item_to_cart(context):
    context.app.cart_page.add_item_to_cart()


@when('Click go to cart')
def click_go_to_cart_btn(context, ):
    context.app.cart_page.click_go_to_cart_btn()


@then('Verify item appears in cart')
def verify_item_in_cart(context, ):
    context.app.cart_page.verify_item_in_cart()


@then('Verify amazon cart is empty')
def verify_amazon_cart_is_empty(context, ):
    context.app.cart_page.verify_amazon_cart_is_empty()
