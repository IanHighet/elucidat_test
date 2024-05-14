Feature: Evidence

  Scenario Outline: Page Layout
    Given the <page title> page
    Then I expect the "<page title>" header
    And I expect two flip-cards
    And I expect a radio button with four options
    And I expect a "Vote" button
  Examples:
    | page title      |
    | THE FINGERPRINT |

  Scenario Outline: Can turn the flip cards
    Given the <page title> page
    When I select the <id> flip-card
    Then I expect to see the flip-card <text>
  Examples:
    | id | text |
    | 1  | “We were able to recover a partial print from the bin and following analysis, we feel very confident that it matches the suspect’s.” The Prosecution" |
    | 2  | "“Fingerprint analysis relies on a human comparing one set of patterns with another, so there is room for error. It’s possible for fingerprint ‘experts’ to find a match when there isn’t one.” The Defence" |

  Scenario Outline: Can vote on evidence
    Given the <page title> page
    When I select the <id> flip-card
    Then I expect to see the flip-card <text>
  Examples:
    | id | text |
    | 1  | “We were able to recover a partial print from the bin and following analysis, we feel very confident that it matches the suspect’s.” The Prosecution" |
    | 2  | "“Fingerprint analysis relies on a human comparing one set of patterns with another, so there is room for error. It’s possible for fingerprint ‘experts’ to find a match when there isn’t one.” The Defence" |
