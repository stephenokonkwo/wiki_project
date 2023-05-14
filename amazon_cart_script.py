from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)


                                                #HW3 Cart Test case
# Verify that the user can access this amazon link
driver.get('https://www.amazon.com/')

# Verify that user locates "Cart BTN" and is able to click.
driver.find_element(By.CSS_SELECTOR, '#nav-cart-count-container').click()

# Verify that "Amazon Cart" is empty once "Cart BTN" is clicked
expected_result = "Your Amazon Cart is empty"
actual_result = driver.find_element(By.CSS_SELECTOR, 'div.a-row.sc-your-amazon-cart-is-empty').text
assert actual_result == expected_result, f'Test Case Error! expected {expected_result} but got {actual_result}'

#Verify Your Amazon Cart is empty txt present
driver.find_element(By.CSS_SELECTOR,'div.a-row.sc-your-amazon-cart-is-empty')

print('Test case passed')
sleep(8)
driver.quit()