from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


# Given Test Steps

# Opens up Wiki's Main Page
@given('Open Wikipedia org')
def open_main_page(context):
    context.app.main_page.open_main_page()


# When Tests Steps

# Locates Search Input Field on thw Main Page
@when('Locate the search input field')
def locate_search_input(context):
    context.app.main_page.locate_search_input()
