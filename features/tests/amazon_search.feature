Feature: Tests for Amazon search

#  Scenario 1
  Scenario: User can search for a product on Amazon
    Given Open Amazon Page
    When Search for coffee
    And Click search button
    Then Search results have "coffee"


#  Scenario 2
  Scenario: User can see language options
    Given Open Amazon Page
    When Hover over language options
    Then Verify Spanish option present


#  Scenario 3
  Scenario: User can select and search in a department
    Given Open Amazon Page
    When Select department by alias stripbooks
    And Search for Faust
    And Click search button
    Then Verify books department is selected

