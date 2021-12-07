# Created by zahid at 12/6/2021
Feature: Test Scenarios for Link count on Amazon

  Scenario: User can see 40 footer links
    Given Open Amazon page
    Then Verify footer has 40 links

  Scenario: User can see 5 footer links
    Given Open Amazon BestSellers page
    Then Verify header has 5 links