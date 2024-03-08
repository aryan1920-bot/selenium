# search_page.py

from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# import time 

class SearchPage(BasePage):
    def enter_restaurant_name(self, restaurant_name):
        search_locator = (By.ID, 'apxor_search')
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(search_locator))
        self.perform_action(search_locator, action='input', value=restaurant_name)

    def click_search_button(self):
        search_button_locator = (By.XPATH, '/html/body/div[7]/div[2]/div[2]/div/div[2]/div/form/div[4]/button[2]')
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(search_button_locator))    
        self.perform_action(search_button_locator)
