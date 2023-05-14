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
driver.maximize_window()



                                                     # Homework 3 CSS Selectors Locators

# Amazon Logo- By Class
driver.find_element(By.CSS_SELECTOR, 'i.a-icon.a-icon-logo')

# Create account-By Class
driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small')

# Your name text field-By ID
driver.find_element(By.CSS_SELECTOR, 'input#ap_customer_name')

# Mobile number or email- By ID
driver.find_element(By.CSS_SELECTOR, '#ap_email')

# Password-Mix
driver.find_element(By.CSS_SELECTOR, '#ap_password.a-input-text')

# Passwords must be at least 6 characters.-BY Class
driver.find_element(By.CSS_SELECTOR, 'div.a-box-inner div.a-alert-content')

# Re-enter password field- BY ID
driver.find_element(By.CSS_SELECTOR, '#ap_password_check')

# Continue button- Mix
driver.find_element(By.CSS_SELECTOR, '#continue.a-button-input')

# Conditions of Use-Parent to Child
driver.find_element(By.CSS_SELECTOR, "#legalTextRow, a[href*='/gp/help/customer/]")

# Privacy Notice-
driver.find_element(By.CSS_SELECTOR, "#legalTextRow, a[href*= 'ref=ap_register_notification_privacy_notice?'")

# Sign In- Parent to Child
driver.find_element(By.CSS_SELECTOR, "div.a-row a[href*='/ap/signin']")


