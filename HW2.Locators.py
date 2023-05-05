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

                                        # Locators HW2 Assignment

# Amazon Logo
driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")

# Continue Button
driver.find_element(By.XPATH, "//input[@type='submit']")

# Need Help Link -text and contains
driver.find_element(By.XPATH, "//span[contains(text(),'Need help')]")

# Forgot your password link -with contains and parent => child
driver.find_element(By.XPATH, "//div[contains(@class, 'a-row a-expander')]//a[@id='auth-fpp-link-bottom']")

# Other issues with Sign-In link by ID
driver.find_elements(By.ID, "//a[@id= 'ap-other-signin-issues-link']")

# Create your Amazon account button by ID
driver.find_element(By.XPATH, "//a[@id='createAccountSubmit']")

# *Conditions of use link
driver.find_element(By.XPATH, "//a[contains(@href, '/gp/help/customer/display.html/ref=ap_desktop_footer_c')]")

# Privacy Notice link
driver.find_element(By.XPATH, "//a[contains(@href,'/gp/help/customer/display.html/ref=ap_desktop_footer_p')]")



