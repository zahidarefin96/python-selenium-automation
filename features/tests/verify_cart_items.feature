# Created by zahid at 12/6/2021
Feature: Test Scenarios for Cart functionality on Amazon

  Scenario: User can add a product to the cart
    Given Open Amazon page
    When Search for amazon basics water bottle
    And Click search icon
    And Click on the first product
    And Click on Add to Cart icon
    And Open Cart page
    Then Verify cart has 1 item(s)