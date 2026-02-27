from pages.login_page import LoginPage
from tests.base_test import BaseTest

class TestLogin(BaseTest):
    def test_valid_login(self):
        login_page = LoginPage(self.driver)

        login_page.open_login_page(self.config.get("base_url"))
        login_page.login(self.config.get("valid_email"), self.config.get("valid_password"))

        assert self.config.get("valid_email") in login_page.get_success_message()

    def test_invalid_login(self):
        login_page = LoginPage(self.driver)

        login_page.open_login_page(self.config.get("base_url"))
        login_page.login(self.config.get("invalid_email"), self.config.get("invalid_password"))

        assert "Login was unsuccessful. Please correct the errors and try again." in login_page.get_error_message()
