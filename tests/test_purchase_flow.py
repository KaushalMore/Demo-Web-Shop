from tests.base_test import BaseTest
from pages.login_page import LoginPage
from pages.books_page import BooksPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

from time import sleep


class TestPurchaseFlow(BaseTest):
    def test_purchase_book(self):
        login_page = LoginPage(self.driver)
        books_page = BooksPage(self.driver)
        product_page = ProductPage(self.driver)
        cart_page = CartPage(self.driver)
        checkout_page = CheckoutPage(self.driver)

        # Login
        login_page.open_login_page(self.config.get("base_url"))
        login_page.login(self.config.get("valid_email"), self.config.get("valid_password"))

        # Books
        books_page.open_books()
        books_page.sort_by("Position")
        books_page.set_page_size("12")
        books_page.set_view_mode("List")
        books_page.open_first_product()

        # Product
        assert "Computing and Internet" in product_page.get_product_name()
        product_page.set_quantity(2)
        product_page.add_to_cart()

        # Cart
        cart_page.open_cart()
        cart_page.select_country("United States")
        sleep(2)
        cart_page.select_state("California")
        cart_page.estimate_shipping()
        cart_page.accept_terms()
        cart_page.checkout()

        # Checkout
        checkout_page.complete_checkout()
        assert "Cash On Delivery (COD)" in checkout_page.get_order_review()
        checkout_page.confirm_order()
        sleep(2)
        assert "Your order has been successfully processed!" in checkout_page.get_order_details()
        checkout_page.open_order_link()

        checkout_page.click_logout()
        # sleep(2)
        # assert "Log in" in checkout_page.get_confirm_logout()
