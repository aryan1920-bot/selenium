#login_page.py

from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_website(self): 
        self.driver.get("https://new-react-test.easydiner.com/")
        print("Opened website")

    def click_login_button(self):
        login_button_locator = (By.XPATH, '//div[@class="flex login_btn_home full-height font-14 white align-v-center pointer" and text()="Login"]')
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(login_button_locator))
        self.perform_action(login_button_locator)
        print("Clicked on login button")
    def enter_mobile_number(self, mobile_number):
        mobile_input_locator = (By.XPATH, '//input[@class="full-width float_input remove-spin-buttons" and @name="mobile"]')
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(mobile_input_locator))
        self.perform_action(mobile_input_locator, action='input', value=mobile_number)
        print("Entered mobile number")

    def click_get_otp_button(self):
        get_otp_button_locator = (By.XPATH, '//button[contains(@class, "white pointer relative text-center font-15 semi-bold full-width flex-1 btns_main active_main block border_none") and contains(text(), "Get OTP")]')
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(get_otp_button_locator))
        self.perform_action(get_otp_button_locator)
        print("Clicked on get otp button")
        time.sleep(3)
        
    def enter_otp(self, otp):
        otp_input_locator = (By.XPATH, '//div[@class="flex align-v-center"]/input[@class="full-width float_input otp_inputs radius-8 h-50 margin-r-20 outline-0 text-center remove-spin-buttons"]')

        WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located(otp_input_locator)
            )
        for index, digit in enumerate(otp):
            otp_input_locator[index].send_keys(digit)
            time.sleep(0.5)
        print("Entered otp")  
        time.sleep(3)  
        search_locator = (By.ID, 'apxor_search')
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(search_locator))
        
