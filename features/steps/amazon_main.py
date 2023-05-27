from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open amazon main page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')
    context.driver.refresh()


@given('Open amazon bestsellers page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')
    context.driver.refresh()


@given('Open Amazon product page B07BJKRR25')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/gp/product/B07BJKRR25/')
    context.driver.refresh()

@when('Click on button from SignIn popup')
def click_sign_in_popup_btn(context):
    context.driver.wait.until(
        # EC.element_to_be_clickable('POPUP_SIGNIN_BTN'),
        message='Signin btn not clickable'
    ).click()

@when('Search for {search_word}')
def search_amazon(context, search_word):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys(search_word)
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()


@when('Click Orders')
def click_orders(context):
    context.driver.find_element(By.ID, 'nav-orders').click()


@when('Click Cart')
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, '#nav-cart-count-container').click()


@when('Click on Best Sellers BTN')
def click_best_sellers(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[href='/gp/bestsellers/?ref_=nav_cs_bestsellers']").click()


