# Created by zahid at 12/6/2021
Feature: Test Scenarios for Link count on Amazon

#  Scenario 1
  Scenario: User can see 39 footer links
    Given Open Amazon main-page
    Then Verify footer has 39 links

#  Scenario 2
  Scenario: User can see 5 footer links
    Given Open Amazon best-sellers page
    Then Verify header has 5 links