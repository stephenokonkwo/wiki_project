from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep



@then('Verify search results shown for "{expected_result}"')
def verify_search_results(context, expected_result):
    actual_result = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
    assert expected_result == actual_result, f'Error! Expected {expected_result} but got actual {actual_result}'

#assert expected_result in actual_result
@then('Verify the cart has the right product')
def verify_Kindle_text_appears_in_product_title(context, expected_result):
    actual_result = context.driver.find_element(By.CSS_SELECTOR, 'span.a-truncate-cut').text
    assert expected_result in actual_result


@when('Click on kindle item')
def Click_on_kindle_item(context):
    context.driver.find_element(By.CSS_SELECTOR, "a.a-link-normal.s-no-outline[href*= '/Kindle-Paperwhite-adjustable-Ad-Supported/dp/B08KTZ8249/ref=sr']").click()

@when('Click add to cart')
def add_item_to_cart(context):
    context.driver.find_element(By.ID, 'add-to-cart-button').click()



@when("Go to the Cart Page")
def open_cart_page(context):
    context.driver.get('https://www.amazon.com/gp/cart/view.html?ref_=nav_cart')
    from time import sleep
    sleep(10)
