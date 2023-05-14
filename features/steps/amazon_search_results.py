from selenium.webdriver.common.by import By
from behave import given, when, then



@then('Verify search results shown for {expected_result}')
def verify_search_results(context, expected_result):
    actual_result = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
    assert expected_result == actual_result, f'Error! Expected {expected_result} but got actual {actual_result}'
