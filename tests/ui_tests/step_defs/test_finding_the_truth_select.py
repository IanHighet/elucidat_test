from pytest_bdd import scenarios, given, when, then, parsers
from selenium.webdriver.common.by import By
import time
from ui_helpers import UI_helpers
import pdb

TITLE_LOCATOR = "h2 > strong"
CARD_CLASS = "card__image"
MURDER_COMMITTED_EXPECTED_TEXT = "A murder has been committed in an alleyway outside a pub."

scenarios('../features/finding_the_truth_select.feature')


@given('the Finding the Truth Selection page')
def step_impl(browser, user_options):
    UI_helpers.goto_start_url(browser, user_options)
    UI_helpers.select_button_text(browser, "Start")


@then(parsers.parse('I expect the header to be "{title}"'))
def step_impl(browser, title):
    elements = browser.find_elements(By.CSS_SELECTOR, TITLE_LOCATOR)
    filtered_elements = [ elem for elem in elements if elem.text == title ]
    assert filtered_elements[0].text == title


@then(parsers.parse('I expect the paragraph "{text}" to be displayed'))
def step_impl(browser, text):
    elements = browser.find_elements(By.CSS_SELECTOR, "p")
    filtered_elements = [ elem for elem in elements if elem.text == text ]
    assert len(filtered_elements) == 1


@then(parsers.parse('I expect 2 cards to be displayed'))
def step_impl(browser):
    elements = browser.find_elements(By.CLASS_NAME, CARD_CLASS)
    assert len(elements) == 2


@when(parsers.parse('I select the card {card_id:d}'))
def step_impl(browser, card_id):
    elements = browser.find_elements(By.CLASS_NAME, CARD_CLASS)
    elements[card_id].click()


@then(parsers.parse('I expect to be taken to the murder has been committed page'))
def step_impl(browser):
    time.sleep(3)
    elements = browser.find_elements(By.CSS_SELECTOR, "p")
    filtered_elements = [ elem for elem in elements if elem.text == MURDER_COMMITTED_EXPECTED_TEXT ]
    assert len(filtered_elements) == 1
