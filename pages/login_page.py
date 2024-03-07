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
        login_button_locator = (By.XPATH, '//span[@class="grey" and contains(text(), "Login")]')
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(login_button_locator))
        self.perform_action(login_button_locator)
        print("Clicked on login button")
    def enter_mobile_number(self, mobile_number):
        mobile_input_locator = (By.XPATH, '//input[@id="mobile_number"]')
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(mobile_input_locator))
        self.perform_action(mobile_input_locator, action='input', value=mobile_number)
        print("Entered mobile number")
    def click_get_otp_button(self):
        get_otp_button_locator = (By.XPATH, '//div[@class="get_otp flex bold white margin-t-20 pointer relative full-width radius-8 padding-15"]')
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(get_otp_button_locator))
        self.perform_action(get_otp_button_locator)
        print("Clicked on get otp button")
        time.sleep(3)
    def enter_otp(self, otp):
        otp_input_fields = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, '//input[@class="otp_input radius-8 width-50 text-center margin-r-20 h-50 outline-0 black"]'))
            )
        for index, digit in enumerate(otp):
            otp_input_fields[index].send_keys(digit)
            time.sleep(0.5)
        print("Entered otp")  
        time.sleep(3)  
        search_locator = (By.ID, 'apxor_search')
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(search_locator))
        
