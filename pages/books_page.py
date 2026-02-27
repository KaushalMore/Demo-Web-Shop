from pages.base_page import BasePage

class BooksPage(BasePage):
    BOOK_BUTTON = ("css selector", "ul.top-menu>li>a[href='/books']")
    SORT_BY_DROPDOWN = ("id", "products-orderby")
    PAGE_SIZE_DROPDOWN = ("id", "products-pagesize")
    VIEW_MODE_DROPDOWN = ("id", "products-viewmode")
    FIRST_PRODUCT = ("css selector", "div.product-list > div:nth-of-type(1) img")

    def open_books(self):
        self.click(self.BOOK_BUTTON)

    def sort_by(self, option):
        self.select(self.SORT_BY_DROPDOWN, option)

    def set_page_size(self, size):
        self.select(self.PAGE_SIZE_DROPDOWN, size)

    def set_view_mode(self, mode):
        self.select(self.VIEW_MODE_DROPDOWN, mode)

    def open_first_product(self):
        self.click(self.FIRST_PRODUCT)