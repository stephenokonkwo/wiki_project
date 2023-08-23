# Created by stephenokonkwo at 7/31/23
Feature: Wikipedia Search & Search_Results Test Cases
  All search and search results test case will be written here.

  Scenario: Verify Python search results appear
    Given Open Wikipedia org
    When Locate the search input field
    When Search for Python
    Then Verify search results shown for Python