from selenium.webdriver.common.by import By
from behave import given, when, then

# from time import sleep
RESULT_TEXT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
PRODUCT_PRICE = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")
SEARCH_RESULTS = (By.CSS_SELECTOR, "[data-component-type='s-search-result']")
PRODUCT_TITLE = (By.CSS_SELECTOR, 'h2 span.a-text-normal')
PRODUCT_IMG = (By.CSS_SELECTOR, ".s-image[data-image-latency='s-product-image']")
KINDLE_RESULT = (By.CSS_SELECTOR,
                 "a.a-link-normal.s-no-outline[href*= '/Kindle-Paperwhite-adjustable-Ad-Supported/dp/B08KTZ8249/ref" "=sr']")
BACKPACK_RESULT = (By.CSS_SELECTOR, 'span.a-price-whole')


# When Statements:
@when('Click on kindle item')
def click_search_item(context):
    context.driver.find_element(By.CSS_SELECTOR, KINDLE_RESULT).click()


@when('Click on backpack item')
def click_search_item(context):
    context.app.search_results_page.click_search_item()


@when("Go to the Cart Page")
def open_cart_page(context):
    context.driver.get('https://www.amazon.com/gp/cart/view.html?ref_=nav_cart')


@when('Search for {search_query}')
def search_amazon(context, search_query):
    context.app.header.search_for_product(search_query)


# Then Statements:

@then('Verify correct department shown')
def verify_dept(context):
    context.app.search_results_page.verify_dept()


@then('Verify search results shown for {expected_result}')
def verify_search_results(context, expected_result):
    context.app.search_results_page.verify_search_results(expected_result)


# assert expected_result in actual_result
@then('Verify the cart has the right product')
def verify_Kindle_text_appears_in_product_title(context, ):
    actual_result = context.driver.find_element(By.CSS_SELECTOR, 'span.a-truncate-cut').text
    assert 'Kindle' in actual_result
