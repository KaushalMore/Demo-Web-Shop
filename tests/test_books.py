import allure
import pytest

from pages.books_page import BooksPage
from pages.product_page import ProductPage
from tests.base_test import BaseTest


class TestBooks(BaseTest):

    @allure.feature("Demo Web Shop - Product")
    @allure.description(
        "To verify that the user is able to successfully navigate to the Books section from the homepage.")
    @pytest.mark.smoke
    def test_verify_navigation_to_book_page(self):
        books_page = BooksPage(self.driver)

        allure.dynamic.story(self.driver)
        with allure.step("Opening Demo Web Shop homepage."):
            books_page.open_home_page(self.config.get("base_url"))

        with allure.step("Click on the 'Books' link."):
            books_page.click_books()

        with allure.step("Verifying the user is redirected to the Books page"):
            assert "books" in books_page.driver.current_url

    @allure.feature("Demo Web Shop - Product")
    @allure.description("To verify that a user can add a book to the shopping cart from the Books listing page.")
    @pytest.mark.smoke
    def test_add_book_to_shopping_cart(self):
        books_page = BooksPage(self.driver)

        allure.dynamic.story(self.driver)

        with allure.step("Opening Demo Web Shop books page."):
            books_page.open_books_page(self.config.get("base_url"))

        with allure.step("Identify 'Computing and Internet' book and click on 'Add to cart' button."):
            books_page.click_computing_and_internets_add_to_cart_button()

        with allure.step("Verifying product added to cart message displayed."):
            assert "product has been added" in books_page.get_product_added_to_cart()

    @allure.feature("Demo Web Shop - Product")
    @allure.description("To verify that the 'Sort by' feature correctly reorganizes books by price.")
    @pytest.mark.regression
    def test_verify_sorting_functionality(self):
        books_page = BooksPage(self.driver)

        allure.dynamic.story(self.driver)
        with allure.step("Opening Demo Web Shop books page."):
            books_page.open_books_page(self.config.get("base_url"))

        with allure.step("Select Sort By and choose 'Price: Low to High' option from dropdown."):
            books_page.select_sort_by("Price: Low to High")

        with allure.step("Verifying sorted products."):
            prices = books_page.get_products_actual_price()
            sorted_price = prices.copy()
            sorted_price.sort()
            assert sorted_price == prices

    @allure.feature("Demo Web Shop - Product")
    @allure.description("To verify that the user can change the number of products displayed per page.")
    @pytest.mark.regression
    def test_change_display_page_size(self):
        books_page = BooksPage(self.driver)

        allure.dynamic.story(self.driver)
        with allure.step("Opening Demo Web Shop books page."):
            books_page.open_books_page(self.config.get("base_url"))

        with allure.step("Select Display and choose '4' option from dropdown."):
            books_page.select_page_size("4")

        with allure.step("Verifying number of products on page are exactly '4'."):
            names = books_page.get_products_name()
            assert "4" == str(len(names))

    @allure.feature("Demo Web Shop - Product ")
    @allure.description("To verify that clicking on a book name opens the detailed product page.")
    @pytest.mark.regression
    def test_product_information(self):
        books_page = BooksPage(self.driver)
        product_page = ProductPage(self.driver)

        allure.dynamic.story(self.driver)
        with allure.step("Opening Demo Web Shop books page."):
            books_page.open_books_page(self.config.get("base_url"))

        with allure.step("Clicking the first book."):
            books_page.click_computing_and_internet_link()

        with allure.step("Verifying details of product."):
            names = product_page.get_product_name()
            description = product_page.get_product_description()
            price = product_page.get_product_price()
            assert "Computing and Internet" in names and "More Than 100 tips about computing and internet." in description and "10.00" in price
