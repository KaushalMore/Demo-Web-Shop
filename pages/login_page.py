from selenium.common import NoSuchElementException

from pages.base_page import BasePage


class LoginPage(BasePage):
    EMAIL_FIELD = ("id", "Email")
    PASSWORD_FIELD = ("id", "Password")
    REMEMBER_ME_CHECKBOX = ("id", "RememberMe")
    LOGIN_BUTTON = ("css selector", "input[value='Log in']")
    CUSTOMER_INFO = ("css selector", "div[class='header-links'] a[href='/customer/info']")
    ERROR_MESSAGE = ("css selector", "div.validation-summary-errors")

    def open_login_page(self, base_url):
        self.get_url(f"{base_url}/login")

    def enter_email(self, email):
        self.send_keys(self.EMAIL_FIELD, email)
        self.logger.info(f"Entered email : {email}")

    def enter_password(self, password):
        self.send_keys(self.PASSWORD_FIELD, password)
        self.logger.info(f"Entered password : {password}")

    def click_remember_me(self):
        self.click(self.REMEMBER_ME_CHECKBOX)
        self.logger.info(f"remember checkbox is clicked")

    def click_submit(self):
        self.click(self.LOGIN_BUTTON)
        self.logger.info(f"submit button is clicked")

    def login(self, username, password):
        self.enter_email(username)
        self.enter_password(password)
        self.click_remember_me()
        self.click_submit()

    def get_success_message(self):
        try:
            return self.get_text(self.CUSTOMER_INFO)
        except NoSuchElementException as e:
            print(e)
            return None

    def get_error_message(self):
        try:
            return self.get_text(self.ERROR_MESSAGE)
        except NoSuchElementException as e:
            print(e)
            return None
