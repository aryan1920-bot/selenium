# login_page.py

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from .base_page import BasePage
from utils.locators import *
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_website(self):     
        self.driver.get("https://new-react-test.easydiner.com/")
        print("Opened website")

    def click_login_button(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON))
        self.perform_action(BasePageLocators.LOGIN_BUTTON)
        print("Clicked on login button")

    def enter_mobile_number(self, mobile_number):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LoginPageLocators.MOBILE_INPUT))
        self.perform_action(LoginPageLocators.MOBILE_INPUT, action='input', value=mobile_number)
        print("Entered mobile number")

    def click_get_otp_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(LoginPageLocators.GET_OTP_BUTTON))
        self.perform_action(LoginPageLocators.GET_OTP_BUTTON)
        print("Clicked on get otp button")
        time.sleep(3)

    def enter_otp(self, otp):
        WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(LoginPageLocators.get_otp_input_locator(0)))
        for index, digit in enumerate(otp):
            otp_input_locator = LoginPageLocators.get_otp_input_locator(index)
            self.perform_action(otp_input_locator, action='input', value=digit)
            time.sleep(0.5)

        print("Entered otp")  
        time.sleep(3)  
        # search_locator = (By.XPATH, '<path d="m17 17 4 4M3 11a8 8 0 1 0 16 0 8 8 0 0 0-16 0z" stroke="#FF4612" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path>')
        # WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(search_locator))