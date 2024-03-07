#test_eazydiner.py

import sys
import os
import pytest

# Add the parent directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Now, you can use relative imports
from eazydiner_tester import EazyDinerTester
from pages.login_page import LoginPage
from pages.search_page import SearchPage
from pages.booking_page import BookingPage
# Pytest fixture for setup and teardown
@pytest.fixture
def setup_teardown():
    tester = EazyDinerTester()
    tester.setup()

    yield tester.login_page, tester.search_page, tester.booking_page  # Provide the instances to the test function

    tester.teardown()

def test_booking_successful(setup_teardown):
    login_page, search_page, booking_page = setup_teardown

    login_page.open_website()
    login_page.click_login_button()
    login_page.enter_mobile_number("8307284752")
    login_page.click_get_otp_button()
    login_page.enter_otp("9021")

    # Login successful, now perform booking
    search_page.enter_search_query("test")
    search_page.click_search_button()

    booking_page.click_book_now_button()
    booking_page.click_submit_button()
    booking_page.click_confirm_booking_button()

    # Assertions or additional checks can be added here
