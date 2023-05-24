from selenium.webdriver.common.by import By
from behave import given, when, then


@then('Verify Best Sellers Page appears')
def Verify_Best_Sellers_Page_appears(context,):
    BEST_SELLER_LINKS = context.driver.find_elements(By.CSS_SELECTOR, 'div._p13n-zg-nav-tab-all_style_zg-tabs-li-div__1YdPR')
    assert BEST_SELLER_LINKS, f'Links arent there'

    for items in BEST_SELLER_LINKS:
        print(items.text)