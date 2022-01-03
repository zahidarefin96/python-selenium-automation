# Created by zahid at 12/20/2021
Feature: User can open amazon applications from Terms of Conditions

# Scenario 1
  Scenario: User can open and close Amazon Privacy Notice
    Given Open Amazon T&C page
    When Store original windows
    And Click on Amazon Privacy Notice link
    And Switch to the newly opened window
    Then Verify Amazon Privacy Notice page is opened
    And User can close new window and switch back to original

# Scenario 2
  Scenario: User can open Best Sellers each link on the top menu
    Given Open Amazon BestSellers page
    Then click each top link and verifies that new page opens
