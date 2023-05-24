Feature: Amazon Search tests

#  Scenario: User can search for table on Amazon
#    Given Open amazon main page
#    When Search for table
#    Then Verify search results shown for "table"
#
#  Scenario: User can search for coffee on Amazon
#    Given Open amazon main page
#    When Search for coffee
#    Then Verify search results shown for "coffee"

Scenario: User can search for kindle on Amazon
    Given Open amazon main page
    When Search for kindle
    When Click on kindle item
    When Click add to cart
    When Go to the Cart Page
    Then Verify the cart has the right product