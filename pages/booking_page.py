# booking_page.py

from selenium.webdriver.common.by import By
from .base_page import BasePage


class BookingPage(BasePage):
    def click_book_now_button(self):
        book_now_button_locator = (By.XPATH, '/html/body/div[7]/div[2]/div[2]/div/div[2]/div/form/div[4]/button[2]')
        self.perform_action(book_now_button_locator)

    def click_submit_button(self):
        submit_button_locator = (By.XPATH, '//button[@id="checkout-button" and @type="button" and @class="button pay-delivery"]')
        self.perform_action(submit_button_locator)

    def click_confirm_booking_button(self):
        book_now_button_locator = (By.XPATH, '//button[@class="bold btn btn-block btn-primary font-18 padding-15 radius-8 relative book_cta" and contains(text(), "Book Now")]')
        self.perform_action(book_now_button_locator)
