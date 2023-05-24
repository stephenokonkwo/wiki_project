# Created by stephenokonkwo at 5/14/23
Feature: Amazon Cart tests

  Scenario: User can see Cart page
    Given Open amazon main page
    When Click Cart
    Then Verify amazon cart is empty

    Scenario: User item appears in Cart
    Given Open amazon main page
    When Click Cart
    Then Verify that item is in cart
