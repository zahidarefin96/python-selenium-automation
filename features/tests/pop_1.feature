# Created by zahid at 12/29/2021
Feature: Tests for Sign-in  page and Cart page

#  Scenario 1
  Scenario: Logged out user sees Sign in page when clicking Orders
    #Given step is done in amazon_search.py
    Given Open Amazon page
    When Click Amazon Orders link
    Then Verify that Sign-In page is opened


#  Scenario 2
  Scenario: 'Your Shopping Cart is empty' shown if no product added
    #Given step is done in amazon_search.py
    Given Open Amazon page
    #When step is done in verify_cart_empty.py
    When Click on cart icon
    Then Verify Your Amazon Cart is empty text present