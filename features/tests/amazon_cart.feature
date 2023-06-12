# Created by stephenokonkwo at 5/14/23
Feature: Amazon Cart tests

#  Scenario: User can see Cart page
#    Given Open amazon main page
#    When Click Cart
#    Then Verify amazon cart is empty
#
#  Scenario: User item appears in Cart
#    Given Open amazon main page
#    When Click Cart
#    Then Verify that item is in cart


  Scenario: 'Your Shopping Cart is empty' shown if no product added
    Given Open amazon main page
    When Click Cart
    Then Verify amazon cart is empty

  Scenario: Add item to Cart
    Given Open amazon main page
    When Search for backpack
    And Click on backpack item
    And Click add to cart
    And Click go to cart
    Then Verify item appears in cart
