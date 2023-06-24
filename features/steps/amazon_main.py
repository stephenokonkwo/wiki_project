from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

SEARCH_FILED = (By.ID, 'twotabsearchtextbox')
SEARCH_BTN = (By.ID, 'nav-search-submit-button')
RESULT_TEXT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
POPUP_SIGNIN_BTN = (By.CSS_SELECTOR, "#nav-signin-tooltip a.nav-action-signin-button span.nav-action-inner")
ORDERS_BTN = (By.ID, 'nav-orders')
CART_BTN = (By.ID, 'nav-cart')


# Given: Statements
@given('Open amazon main page')
def open_main_page(context):
    context.app.main_page.open_main_page()


@given('Open amazon bestsellers page')
def open_amazon_best_sellers_page(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')
    context.driver.refresh()


@given('Open Amazon product page B07BJKRR25')
def open_amazon_product_page(context):
    context.driver.get('https://www.amazon.com/gp/product/B07BJKRR25/')
    context.driver.refresh()


# When: Statements
@when('Select department electronics')
def select_electronic_dept(context):
    context.app.header.select_electronic_dept()


@when('Select department books')
def select_dept(context):
    context.app.header.select_dept()


@when('Hover over language options')
def hover_lang(context):
    context.app.header.hover_lang()


@when('Click on button from SignIn popup')
def click_sign_in_popup_btn(context):
    context.driver.wait.until(
        EC.element_to_be_clickable(POPUP_SIGNIN_BTN),
        message='Signin btn not clickable').click()


@when('Wait for {sec_amount} sec')
def wait_sec(context, sec_amount):
    sleep(int(sec_amount))


# @when('Search for {search_query}')
# def search_amazon(context, search_query):
#     context.app.header.search_for_product(search_query)


@when('Click Orders')
def click_orders(context):
    context.app.header.click_orders()


@when('Click Cart')
def click_cart(context):
    context.app.header.click_cart()


@when('Click on Best Sellers BTN')
def click_best_sellers(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[href='/gp/bestsellers/?ref_=nav_cs_bestsellers']").click()

    # Then: Statements


@then('Verify Sign In is clickable')
def verify_signin_popup_btn_clickable(context):
    context.driver.wait.until(
        EC.element_to_be_clickable(POPUP_SIGNIN_BTN),
        message='Signin btn not clickable')


@then('Verify Sign In disappears')
def verify_signin_popup_btn_disappears(context):
    context.driver.wait.until(
        EC.invisibility_of_element_located(POPUP_SIGNIN_BTN),
        message='Signin btn did not disappear')


@then('Verify spanish option is present')
def verify_spanish_option(context):
    context.app.header.verify_spanish_option()
