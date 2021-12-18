# Created by zahid at 12/13/2021
Feature: Tests for color selection on the product

  Scenario: User can loop through the colors
    Given Open Amazon product B081YS2F7N page in B081YS2F7N
    Then Verify user can click through the colors in Scenario 1


  Scenario: User can loop through the colors
    Given Open Amazon product B07BJKRR25 page in B07BJKRR25
    Then Verify user can click through the colors in Scenario 2

  Scenario: User can see all the product that contains text 'Regular'
    Given Open Amazon WholeFoods page
    Then Verify that every product on the page has a text ‘Regular’ and the product name