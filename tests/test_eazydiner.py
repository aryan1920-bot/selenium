import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from eazydiner_tester import EazyDinerTester

class Test_login:

    def test_login_successful(self):
        tester = EazyDinerTester()  
        tester.setup()
        print("Right mobile number and right otp")
        print("_________________________________")
        tester.login("8307284752", "9021")
        tester.teardown() 

    def test_booking_unsuccessful(self): 
        tester = EazyDinerTester()   
        tester.setup()
        print("Right mobile number and wrong otp")
        print("_________________________________")
        tester.login("8307284752","1234")
        tester.teardown() 





















# @pytest.fixture
# def setup_teardown():
#     tester = EazyDinerTester()
#     tester.setup()

#     yield tester.login_page, tester.search_page, tester.booking_page


#     tester.teardown()








# import sys
# import os
# import pytest

# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# from eazydiner_tester import EazyDinerTester


# @pytest.fixture
# def setup_teardown():
#     tester = EazyDinerTester()
#     tester.setup()

#     yield tester.login_page, tester.search_page, tester.booking_page

#     tester.teardown()

# def test_booking_successful(setup_teardown):
#     login_page, search_page, booking_page = setup_teardown

#     login_page.open_website()
#     login_page.click_login_button()
#     login_page.enter_mobile_number("8307284752")
#     login_page.click_get_otp_button()
#     login_page.enter_otp("9021")

#     search_page.enter_search_query("test")
#     search_page.click_search_button()

#     booking_page.click_book_now_button()
#     booking_page.click_submit_button()
#     booking_page.click_confirm_booking_button()

#     assert booking_page.is_booking_successful(), "Booking was not successful."
#     assert booking_page.get_booking_confirmation_message() == "Booking confirmed!", "Incorrect booking confirmation message."
