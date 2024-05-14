Feature: You Decide

  Scenario Outline: Page Layout
    Given the You Decide page
    Then I expect the "You Decice" header
    And I expect an image
    And I expect a text block
    And I expect a "Continue" button

  Scenario Outline: Continue to next page
    Given the You Decide page
    When I select the "Continue" button
    Then I expect to be taken to the "The Fingerprint" page