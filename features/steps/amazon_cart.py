from selenium.webdriver.common.by import By
from behave import given, when, then


@then('Verify amazon cart is empty')
def verify_amzon_cart_is_empty(context,):
    expected_result = "Your Amazon Cart is empty"
    actual_result = context.driver.find_element(By.CSS_SELECTOR, 'div.a-row.sc-your-amazon-cart-is-empty').text
    assert actual_result == expected_result, f'Test Case Error! expected {actual_result} but got {expected_result}'


    #Verify Your Amazon Cart is empty txt present
    #context.driver.find_element(By.CSS_SELECTOR,'div.a-row.sc-your-amazon-cart-is-empty')

