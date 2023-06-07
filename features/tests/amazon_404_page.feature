# Created by stephenokonkwo at 6/5/23
Feature: Tests for 404 page

  Scenario: User is able to navigate to amazon
    Given Open Amazon product qqwqqqqw page
    And Store original window
    When Click on a dog image
    And Switch to new window
    Then Verify blog is opened
    And Close blog
    And Return to original window
