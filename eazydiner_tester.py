from selenium import webdriver
from pages.login_page import LoginPage
from pages.search_page import SearchPage
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.booking_page import BookingPage
import time
from utils.locators import *

class EazyDinerTester:
    def __init__(self, driver=None, base_url='https://new-react-test.easydiner.com/'):
        self.driver = driver or webdriver.Chrome()
        self.base_url = base_url
        self.login_page = LoginPage(self.driver)
        self.search_page = SearchPage(self.driver)
        self.booking_page = BookingPage(self.driver)

    def setup(self):
        # Maximize the window during setup if needed
        self.driver.maximize_window()

    def teardown(self):
        if self.driver:
            self.driver.quit()

    def login(self, mobile_number,otp):
        self.login_page.open_website()
        print("Website opened.")

        self.login_page.click_login_button()
        print("Clicked on login button.")

        self.login_page.enter_mobile_number(mobile_number)
        print("Entered mobile number.")

        self.login_page.click_get_otp_button()
        print("Clicked on get-otp.")

        self.login_page.enter_otp(otp)
        print("Entered OTP.")
        time.sleep(4)

        try:
            # Check if the element specified by E_msg is visible
            WebDriverWait(self.driver, 10).until_not(
                EC.visibility_of_element_located(LoginPageLocators.E_msg)
            )
            print("login successful.")
            return True
        except TimeoutException:
            print("login unsuccessful.")
            return False


    def booking(self, restaurant_name='test'):
        self.search_page.enter_search_query(restaurant_name)
        print("Entered restaurant name.")

        self.search_page.click_search_button()
        print("Clicked on search button.")

        self.booking_page.click_book_now_button()
        print("Clicked on book now button.")

        self.booking_page.click_submit_button()
        print("Clicked on submit button.")

        self.booking_page.click_confirm_booking_button()

# Example usage:
# tester = EazyDinerTester()
# tester.setup()
# tester.login()
# tester.booking()
# tester.teardown()
