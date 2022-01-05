# Created by zahid at 1/3/2022
Feature: Tests for select, search and hover elements

#  Scenario 1
  Scenario: User can select and search in a department
    #Given Open Amazon Page --> done in amazon_search.py [Scenario 1]
    Given Open Amazon Page
    #When Select department by alias mobile-apps --> done in amazon_search.py [Scenario 1]
    When Select department by alias mobile-apps
    #And Search for Amazon Music --> done in amazon_search.py [Scenario 1]
    And Search for Amazon Music
    #And Click search button --> done in amazon_search.py [Scenario 1]
    And Click search button
    #Then Verify mobile-apps department is selected --> done in amazon_search.py [Scenario 3]
    Then Verify mobile-apps department is selected


#   Scenario 2
  Scenario: User can select and see the new arrivals list
    #Given Open Amazon Page --> done in amazon_search.py [Scenario 1]
    Given Open Amazon Page
    #When Select department by alias mobile-apps --> done in amazon_search.py [Scenario 1]
    When Select department by alias fashion
    #And Click search button --> done in amazon_search.py [Scenario 1]
    And Click search button
    And Hover over New Arrivals options
    Then Verify Women option is visible