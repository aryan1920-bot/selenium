# locators.py

from selenium.webdriver.common.by import By

class BasePageLocators:
    SEARCH_TAB = (By.XPATH, '//path[@d="m17 17 4 4M3 11a8 8 0 1 0 16 0 8 8 0 0 0-16 0z"]')
    LOGIN_BUTTON = (By.XPATH, '//div[@class="flex login_btn_home full-height font-14 white align-v-center pointer" and text()="Login"]')
    
class LoginPageLocators(BasePageLocators):
    MOBILE_INPUT = (By.XPATH, '//input[@class="full-width float_input remove-spin-buttons" and @name="mobile"]')
    GET_OTP_BUTTON = (By.XPATH, '//button[contains(@class, "white pointer relative text-center font-15 semi-bold full-width flex-1 btns_main active_main block border_none") and contains(text(), "Get OTP")]')
    @staticmethod
    def get_otp_input_locator(index):
        return (By.CSS_SELECTOR, f'div.flex.align-v-center input.full-width.float_input.otp_inputs[name="otp{index}"]')
    E_msg=(By.XPATH,'//*[@id="__next"]/div[2]/div[1]/div[3]/div/div/div[3]/div')
class SearchPageLocators(BasePageLocators):
    SEARCH_BUTTON = (By.XPATH, '/html/body/div[7]/div[2]/div[2]/div/div[2]/div/form/div[4]/button[2]')

class BookingPageLocators(BasePageLocators):
    BOOK_NOW_BUTTON = (By.XPATH, '/html/body/div[7]/div[2]/div[2]/div/div[2]/div/form/div[4]/button[2]')
    SUBMIT_BUTTON = (By.XPATH, '//button[@id="checkout-button" and @type="button" and @class="button pay-delivery"]')
    CONFIRM_BOOKING_BUTTON = (By.XPATH, '//button[@class="bold btn btn-block btn-primary font-18 padding-15 radius-8 relative book_cta" and contains(text(), "Book Now")]')
