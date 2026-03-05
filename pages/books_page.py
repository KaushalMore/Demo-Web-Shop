from pages.base_page import BasePage


class BooksPage(BasePage):
    BOOK_BUTTON = ("css selector", "ul.top-menu>li>a[href='/books']")
    SORT_BY_DROPDOWN = ("id", "products-orderby")
    PAGE_SIZE_DROPDOWN = ("id", "products-pagesize")
    VIEW_MODE_DROPDOWN = ("id", "products-viewmode")
    FIRST_PRODUCT = ("css selector", "div.product-list > div:nth-of-type(1) img")
    COMPUTING_AND_INTERNETS_ADD_TO_CART_BUTTON = ("xpath",
                                                  "//h2/a[@href='/computing-and-internet']/parent::h2/following-sibling::div/descendant::input")
    COMPUTING_AND_INTERNET_LINK = ("css selector", "h2>a[href='/computing-and-internet']")
    CART_QUANTITY = ("css selector", "a.ico-cart>span.cart-qty")
    PRODUCT_ADDED_TO_CART_MSG = ("css selector", "p[class='content']")
    PRICE_FILTER_UNDER_25 = ("css selector", "a[href$='price=-25']")
    PRICE_FILTER_25_TO_50 = ("css selector", "a[href$='price=25-50']")
    PRICE_FILTER_OVER_50 = ("css selector", "a[href$='price=25-50']")
    PRODUCTS_ACTUAL_PRICE = ("css selector", "span[class='price actual-price']")
    PRODUCTS_NAME = ("css selector", "h2[class='product-title']>a")

    def open_home_page(self, base_url):
        self.get_url(f"{base_url}")

    def open_books_page(self, base_url):
        self.get_url(f"{base_url}/books")

    def click_books(self):
        self.click(self.BOOK_BUTTON)

    def select_sort_by(self, option):
        self.select_by_visible_text(self.SORT_BY_DROPDOWN, option)

    def select_page_size(self, size):
        self.select_by_visible_text(self.PAGE_SIZE_DROPDOWN, size)

    def select_view_mode(self, mode):
        self.select_by_visible_text(self.VIEW_MODE_DROPDOWN, mode)

    def click_first_product(self):
        self.click(self.FIRST_PRODUCT)

    def click_computing_and_internets_add_to_cart_button(self):
        self.click(self.COMPUTING_AND_INTERNETS_ADD_TO_CART_BUTTON)

    def click_computing_and_internet_link(self):
        self.click(self.COMPUTING_AND_INTERNET_LINK)

    def click_price_filter_under_25(self):
        self.click(self.PRICE_FILTER_UNDER_25)

    def click_price_filter_25_to_50(self):
        self.click(self.PRICE_FILTER_UNDER_25)

    def click_price_filter_over_50(self):
        self.click(self.PRICE_FILTER_UNDER_25)

    def get_cart_quantity(self):
        return self.get_text(self.CART_QUANTITY)

    def get_product_added_to_cart(self):
        return self.get_text(self.PRODUCT_ADDED_TO_CART_MSG)

    def get_products_actual_price(self):
        product_prices = self.find_elements(self.PRODUCTS_ACTUAL_PRICE)
        prices = []
        for price in product_prices:
            prices.append(float(price.text))
        return prices

    def get_products_name(self):
        product_names = self.find_elements(self.PRODUCTS_NAME)
        names = []
        for name in product_names:
            names.append(name.text)
        return names
