"""Tests for Finding the Truth page"""
import time
from pytest_bdd import scenarios, given, when, then, parsers
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from ui_helpers import UiHelpers


scenarios('../features/finding_the_truth.feature')


@given('the Finding the Truth page')
def step_impl(browser, user_options):
    """Go to Finding the Truth URL"""
    UiHelpers.goto_start_url(browser, user_options)


@then(parsers.parse('I expect the header to be "{title}"'))
def step_impl(browser, title):
    """Check header"""
    text = browser.find_element(By.CSS_SELECTOR, "h1").text
    assert text == title


@then(parsers.parse('I expect a "{button_name}" button to be displayed'))
def step_impl(browser, button_name):
    """Check button"""
    elements = browser.find_elements(By.CLASS_NAME, "button__text")
    filtered_elements = [
        elem for elem in elements
            if elem.get_attribute("textContent") == button_name.upper()
    ]
    assert len(filtered_elements) == 1


@when(parsers.parse('I click the "{button_name}" button'))
def step_impl(browser, button_name):
    """Click button"""
    UiHelpers.select_button_text(browser, button_name)


@then(parsers.parse('I expect to be taken to the "{expected_page}" page'))
def step_impl(browser, expected_page):
    """Verify destination page"""
    time.sleep(5)
    # try:
    #     WebDriverWait(browser, 10).until(
    #         EC.presence_of_element_located((By.CSS_SELECTOR, "p"))
    #     )
    # except:
    #     pass
    elements = browser.find_elements(By.CSS_SELECTOR, "h2")
    filtered_elements = [ elem for elem in elements if elem.text == expected_page.upper() ]
    assert len(filtered_elements) == 1


@then(parsers.parse('I expect the paragraph "{expected_text}" to be displayed'))
def step_impl(browser, expected_text):
    """Verify paragraph"""
    elements = browser.find_elements(By.CSS_SELECTOR, "p")
    filtered_elements = [ elem for elem in elements if elem.text.lower() == expected_text.lower() ]
    assert len(filtered_elements) == 1
