# Created by zahid at 12/6/2021
Feature: Test Scenarios to verify Customer Service’s page UI elements

  Scenario: User can see UI elements
    Given Open Amazon Help page
    Then Verify page opened successfully
    Then Verify there are 9 links are shown in body
    Then Verify Search Box is present
    Then Verify there are 12 links are shown in 'Browse Help'