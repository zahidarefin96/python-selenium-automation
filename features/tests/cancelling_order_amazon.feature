# Created by zahid at 11/29/2021
Feature: Test Scenarios for Cancel functionality on Amazon

  Scenario: User can search for Cancelling an order
    Given Open Amazon Help page
    When Click on Search Help Library
    And Input Cancel order
    Then Verify ‘Cancel Items or Orders’ text is present