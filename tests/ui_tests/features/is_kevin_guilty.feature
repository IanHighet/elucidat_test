Feature: Is Kevin Guilty

  Scenario Outline: Page Layout
    Given the Is Kevin Guilty page
    Then I expect a radio button
    And the first option is "Guilty"
    And the second option is "Not guilty"
    And the second option is selected
    And there is a Vote button displayed

  Scenario Outline: Select Guilty or Not guilty
    Given the Is Kevin Guilty page
    When I select the "<verdict>" option
    And I press the Vote button
    Then I expect a <verdict> pop-up to be displayed
    And I can select a Continue button from the pop-up 
  Examples:
    | verdict    |
    | guilty     |
    | not guilty |