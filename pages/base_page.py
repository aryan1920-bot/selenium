# base_page.py

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from utils.locators import BasePageLocators

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def perform_action(self, locator, sleep=0, action='click', value=None, maxtries=1, noloop=False):
        try_count = 0
        while try_count < maxtries:
            try:
                element = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(locator)
                )
                time.sleep(sleep)

                if action == 'click':
                    element.click()
                elif action == 'input':
                    element.send_keys(value)
                elif action == 'submit':
                    element.submit()
                else:
                    raise ValueError(f"Invalid action: {action}")

                return True

            except Exception as e:
                print(f"Error: {e}")
                try_count += 1

                if noloop:
                    break

        return False
