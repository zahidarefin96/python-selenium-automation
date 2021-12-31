# Created by zahid at 12/6/2021
Feature: Test Scenarios for Cart functionality on Amazon

  Scenario: User can add a product to the cart
    #Given Open Amazon page -> already done in amazon_search.py
    Given Open Amazon page
    When type in search amazon basics water bottle
    #And Click search button -> already done in amazon_search.py
    And Click search button
    And Click on the first product
    And Click on Add to Cart icon
    And Open Cart page
    Then Verify cart has Subtotal (1 item): item(s)