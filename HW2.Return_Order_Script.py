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


                                                #HW2 Return_Order_Script
# Verify that the user can access this amazon link
driver.get('https://www.amazon.com/ref=nav_logo')

# Verify that user locates "Result & Orders" Link and is able to click.
driver.find_element(By.ID, 'nav-orders').click()

# Verify that "Sign in" page appears once "Result & Order" link is clicked
expected_result = "Sign in"
actual_result = driver.find_element(By.XPATH, "//h1['class=a-spacing-small']").text
assert expected_result == actual_result, f'Test Case Error! expected {expected_result} but got {actual_result}'

#expected_result = "Email or mobile phone number"
#actual_result = driver.find_element(By.XPATH, "//label[contains(text(), 'Email or mobile phone number')]")
#assert expected_result == actual_result, f'Test case No Good {expected_result} instead got {actual_result}'


print('Test case passed')

sleep(8)
quit()
