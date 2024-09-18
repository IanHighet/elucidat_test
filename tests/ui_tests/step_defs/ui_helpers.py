"""Ui helpers"""
import time
from selenium.webdriver.common.by import By

class UiHelpers:
    """Ui Helpers Class"""

    @staticmethod
    def goto_start_url(browser, user_options):
        """Go to URL"""
        browser.get(user_options["URL"])
        time.sleep(5)
        # try:
        #     WebDriverWait(browser, 10).until(
        #         EC.presence_of_element_located((By.CLASS_NAME, "image"))
        #     )
        # except:
        #     pass


    @staticmethod
    def select_button_text(browser, text):
        """Select button by text"""
        elements = browser.find_elements(By.CLASS_NAME, "button__text")
        filtered_elements = [
            elem for elem in elements
                if elem.get_attribute("textContent") == text.upper()
        ]
        assert len(filtered_elements) == 1
        filtered_elements[0].click()
