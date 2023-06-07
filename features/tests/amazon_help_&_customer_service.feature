# Created by stephenokonkwo at 6/5/23
Feature: Amazon Terms & Conditions page tests

Scenario: User can open and close Amazon Privacy Notice
 Given Open Amazon T&C page
 When Store original windows
 And Click on Amazon Privacy Notice link
 And Switch to the newly opened window
 Then Verify Amazon Privacy Notice page is opened
 And Close Privacy Notice Window
 And Switch back to original window