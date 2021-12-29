# Created by zahid at 12/26/2021
Feature: Tests for Amazon search

  Scenario: User can search for a product on Amazon
    Given Open Amazon Page
    When Search for coffee
    And Click search button
    Then Search results have "coffee"
