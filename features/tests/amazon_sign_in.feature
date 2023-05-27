# Created by stephenokonkwo at 5/14/23
Feature: Amazon Sign in tests

  Scenario: User can see sign in page
    Given Open amazon main page
    When Click Orders
    Then Verify Sign in page opens


 Scenario: Sign In page can be opened from SignIn popup
   Given Open amazon main page
   When Click on button from SignIn popup
   Then Verify Sign In page opens from the popup
