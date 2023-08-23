from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


@when('Search for {search_query}')
def search_for_python(context, search_query):
    context.app.search_results_page.search_for_python(search_query)



@then('Verify search results shown for {expected_result}')
def verify_search_results(context, expected_result):
    context.app.search_results_page.verify_search_results(expected_result)
