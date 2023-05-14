from selenium.webdriver.common.by import By
from behave import given, when, then


@then('Verify Sign in page opens')
def verify_signin_opens(context):
    actual_result = context.driver.find_element(By.XPATH, "//h1['class=a-spacing-small']").text
    assert actual_result == "Sign in", f'Expected Sign in header but got {actual_result}'
    # Verify emaiil field present
    context.driver.find_element(By.ID, 'ap_email')