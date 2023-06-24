# Created by stephenokonkwo at 5/25/23
Feature: Tests for product page

#  Scenario: User can select colors
#    Given Open Amazon product page
#    Then Verify user can click through colors


#  Scenario: User can select colors
#    Given Open Amazon product page B07BJKRR25
#    Then Verify user can click through Slim-Fit Stretch Jean colors

   Scenario: User can see new arrival options
    Given Open Amazon product page B074TBCSC8
    When Hover over New Arrivals tab
    Then Verify Men option is present