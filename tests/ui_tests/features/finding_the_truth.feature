Feature: Finding the Truth
  Test the Finding the Truth page

  Scenario: Page Layout
    Given the Finding the Truth page
    Then I expect the header to be "FINDING THE TRUTH"
    And I expect a "Start" button to be displayed

  Scenario: Selecting Start
    Given the Finding the Truth page
    When I click the "Start" button
    Then I expect to be taken to the "Finding the Truth" page
    And I expect the paragraph "Press on a case to get started." to be displayed
