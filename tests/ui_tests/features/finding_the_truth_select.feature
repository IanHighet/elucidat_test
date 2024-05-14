Feature: Finding the Truth

  Scenario: Page Layout
   Given the Finding the Truth Selection page
   Then I expect the header to be "FINDING THE TRUTH"
   And I expect the paragraph "Press on a case to get started." to be displayed
   And I expect 2 cards to be displayed

  Scenario Outline: Select Victim or Accused
    Given the Finding the Truth Selection page
    When I select the card <card_id>
    Then I expect to be taken to the murder has been committed page
  Examples:
    | card_id |
    | 0       |
    | 1       |