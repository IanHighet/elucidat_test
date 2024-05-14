Feature: Explore the Evidence

  Scenario Outline: Page Layout
    Given the Explore the Evidence page
    Then I expect an 6 buttons to display pop-up details 
    And I expect a "Continue" button

  Scenario Outline: Can display pop-up info
    Given the Explore the Evidence page
    When I click the <id> magnifier button
    Then I expect a pop-up to be displayed with <text>
    And when I select the Close button to close the pop-up
    Then the magnifier button is replaced with a tick
  Examples:
    | id | title          | text |
    | 1  | FINGERPRINTS   | A partial fingerprint was found on the lid of a bin that’s stored in the alleyway and analysis showed that this was a match to Kevin’s prints. |
    | 2  | FOOTPRINTS     | Police were able to take an impression of a footprint from the mud in the alleyway. The print was made by a shoe matching the size worn by Kevin. |
    | 3  | DNA            | Skin cells were found on Wesley’s hand that didn’t match his own. On analysis it was found that these cells contained Kevin’s DNA. |
    | 4  | HAIR           | A hair was found on the collar of Wesley’s shirt. Forensic teams took a strand of Kevin’s hair and compared the two samples under a microscope. They concluded that the hair taken from the victim was a good match to Kevin’s own hair. |
    | 5  | THE CONFESSION | Although initially Kevin claims to be innocent, after several days of questioning by the police he is recorded as saying, “Listen, I don’t remember killing the bloke but from what you say I guess maybe I did. He had been winding me up all night, and I remember finding him in that alley, so that must have been when it happened. You’re the police, and you have all this evidence, so I suppose it must have happened like you said.” |
    | 6  | EYEWITNESS     | Two eye witnesses have told police that they saw Kevin walking away from the alleyway late on Saturday night. One of the witnesses says he heard shouting. |

  Scenario Outline: Continue to next page
    Given the Explore the Evidence page
    When I select the "Continue" button
    Then I expect to be taken to the "You Decide" page