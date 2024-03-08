# Importing necessary modules
from selenium import webdriver
from pages.login_page import LoginPage
from pages.search_page import SearchPage
from pages.booking_page import BookingPage
import time

# Defining the EazyDinerTester class
class EazyDinerTester:
    def __init__(self, driver=None, base_url='https://www.eazydiner.com/'):
        self.driver = driver
        self.base_url = base_url
        self.login_page = LoginPage(self.driver)
        self.search_page = SearchPage(self.driver)
        self.booking_page = BookingPage(self.driver)

    def setup(self):
        # Setting up the WebDriver
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

        # Initializing page objects with the WebDriver instance
        self.login_page = LoginPage(self.driver)
        self.search_page = SearchPage(self.driver)
        self.booking_page = BookingPage(self.driver)

    def teardown(self):
        # Cleaning up and quitting the WebDriver
        if self.driver:
            self.driver.quit()

    def login(self, mobile_number='8307284752'):
        # Method to simulate the login process
        self.login_page.open_website()
        print("Website opened.")

        self.login_page.click_login_button()
        print("Clicked on login button.")

        self.login_page.enter_mobile_number(mobile_number)
        print("Entered mobile number.")

        self.login_page.click_get_otp_button()
        print("Clicked on get-otp.")

        self.login_page.enter_otp()
        print("Entered OTP.")
        time.sleep(4)
        return True

    def booking(self, restaurant_name='test'):
        # Method to simulate the booking process
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
