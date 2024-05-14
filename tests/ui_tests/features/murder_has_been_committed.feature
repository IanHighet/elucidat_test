Feature: Murder has been Committed

  Scenario Outline: Page Layout
    Given the Murder has been Committed page
    Then I expect a embedded video player
    And I expect a "Judge This" button

  Scenario Outline: Can play the video
    Given the Murder has been Committed page
    When I click the start button on the video player
    Then I expect the video to start playing

  Scenario Outline: Select Victim or Accused
    Given the Murder has been Committed page
    When I select the "Judge This" button
    Then I expect to be taken to the "Is Kevin Guilty" page